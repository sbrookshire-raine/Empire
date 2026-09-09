function legoBoard() {
  const ORIGIN = window.location.origin;

  function uid(prefix) {
    return prefix + "_" + Math.random().toString(36).slice(2, 9);
  }

  return {
    bricks: [],
    recipes: [],
    nodes: [],
    edges: [],
    viewport: { x: 40, y: 40, zoom: 1 },
    status: "Loading…",
    busy: false,
    boardPath: "",
    recipeId: "",
    recipeLabel: "",
    mergeToolbelt: true,
    validationIssues: [],
    selectedNode: null,
    selectedEdge: null,
    selectedNodeMeta: { brick: "", enabled: true },
    drag: null,
    connect: null,
    draftPath: "",
    pan: null,

    get viewBox() {
      return "0 0 1200 800";
    },

    get selectedBrickMeta() {
      if (!this.selectedNodeMeta.brick) return null;
      return this.brickMap()[this.selectedNodeMeta.brick] || null;
    },

    async init() {
      await this.loadBricks();
      await this.loadRecipes();
      await this.loadBoard();
      window.addEventListener("keydown", (e) => {
        if (e.key === "Delete" || e.key === "Backspace") {
          const tag = (e.target && e.target.tagName) || "";
          if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
          this.deleteSelected();
        }
      });
    },

    brickMap() {
      const map = {};
      this.bricks.forEach((b) => {
        map[b.id] = b;
      });
      return map;
    },

    brickLabel(id) {
      const b = this.brickMap()[id];
      return b ? b.label : id;
    },

    isCore(id) {
      const b = this.brickMap()[id];
      return !!(b && !b.toolbelt);
    },

    async api(method, path, body) {
      const opts = {
        method,
        headers: { Accept: "application/json", Origin: ORIGIN },
      };
      if (body !== undefined) {
        opts.headers["Content-Type"] = "application/json";
        opts.body = JSON.stringify(body);
      }
      const res = await fetch(ORIGIN + path, opts);
      const data = await res.json().catch(() => ({}));
      return { status: res.status, data };
    },

    async loadBricks() {
      const { data } = await this.api("GET", "/api/lego/bricks");
      if (!data.ok) {
        this.status = data.error || "Failed to load bricks";
        return;
      }
      this.bricks = data.bricks || [];
    },

    async loadRecipes() {
      const { data } = await this.api("GET", "/api/lego/recipes");
      if (!data.ok) {
        this.recipes = [];
        return;
      }
      this.recipes = data.recipes || [];
    },

    boardPayload() {
      const payload = {
        nodes: this.nodes,
        edges: this.edges,
        viewport: this.viewport,
      };
      if (this.recipeId) payload.recipe_id = this.recipeId;
      if (this.recipeLabel) payload.recipe_label = this.recipeLabel;
      return payload;
    },

    applyBoardData(board) {
      this.nodes = Array.isArray(board.nodes) ? board.nodes : [];
      this.edges = Array.isArray(board.edges) ? board.edges : [];
      this.viewport = board.viewport || { x: 40, y: 40, zoom: 1 };
      this.recipeId = board.recipe_id || "";
      this.recipeLabel = board.recipe_label || "";
      this.validationIssues = [];
      this.selectedNode = null;
      this.selectedEdge = null;
    },

    async loadBoard() {
      this.busy = true;
      try {
        const { data } = await this.api("GET", "/api/lego/board");
        if (!data.ok) {
          this.status = data.error || "Failed to load board";
          return;
        }
        this.applyBoardData(data.board || {});
        this.boardPath = data.path || "";
        this.status = data.exists
          ? "Board loaded"
          : "Empty board — pick a recipe or place bricks";
      } finally {
        this.busy = false;
      }
    },

    async saveBoard() {
      this.busy = true;
      try {
        const { data } = await this.api("PUT", "/api/lego/board", this.boardPayload());
        if (!data.ok) {
          this.status = data.error || "Save failed";
          return false;
        }
        this.boardPath = data.path || this.boardPath;
        this.status = "Saved board";
        return true;
      } finally {
        this.busy = false;
      }
    },

    async validateBoard() {
      this.busy = true;
      try {
        const { data } = await this.api("POST", "/api/lego/validate", this.boardPayload());
        this.validationIssues = data.issues || [];
        if (!data.ok) {
          this.status =
            "Validation failed — " +
            (this.validationIssues[0] ? this.validationIssues[0].message : "see inspector");
          return false;
        }
        const warns = this.validationIssues.filter((i) => i.level === "warn").length;
        this.status =
          warns > 0
            ? "Valid with " + warns + " port hint(s)"
            : "Board valid — " + (data.enabled_optional_limbs || 0) + " optional limb(s) enabled";
        return true;
      } finally {
        this.busy = false;
      }
    },

    async loadRecipe() {
      const select = document.getElementById("lego-recipe-select");
      const recipeId = select ? select.value : "";
      if (!recipeId) {
        this.status = "Choose a recipe first";
        return;
      }
      if (
        this.nodes.length &&
        !window.confirm("Replace current board with recipe '" + recipeId + "'?")
      ) {
        return;
      }
      this.busy = true;
      try {
        const { data } = await this.api("POST", "/api/lego/recipe", { id: recipeId });
        if (!data.ok) {
          this.status = data.error || "Recipe load failed";
          return;
        }
        this.applyBoardData(data.board || {});
        this.status = "Loaded recipe: " + (data.board.recipe_label || recipeId);
        await this.validateBoard();
      } finally {
        this.busy = false;
      }
    },

    async applyToolbelt() {
      this.busy = true;
      try {
        const valid = await this.validateBoard();
        if (!valid) return;
        await this.saveBoard();
        const { data } = await this.api("POST", "/api/lego/apply-toolbelt", {
          nodes: this.nodes,
          edges: this.edges,
          merge: !!this.mergeToolbelt,
        });
        if (!data.ok) {
          this.validationIssues = data.issues || this.validationIssues;
          this.status = data.error || "Apply failed";
          return;
        }
        const limbs = (data.active_tools || []).join(", ") || "(none)";
        this.status =
          (data.merge ? "Merged" : "Set") + " Toolbelt: " + limbs;
      } finally {
        this.busy = false;
      }
    },

    addBrick(brickId) {
      const n = {
        id: uid("n"),
        brick: brickId,
        x: 80 + this.nodes.length * 24,
        y: 80 + this.nodes.length * 18,
        enabled: true,
      };
      this.nodes.push(n);
      this.recipeId = "";
      this.recipeLabel = "";
      this.selectNode(n.id);
      this.status = "Placed " + brickId;
    },

    selectNode(id) {
      this.selectedNode = id;
      this.selectedEdge = null;
      const node = this.nodes.find((n) => n.id === id);
      if (node) {
        this.selectedNodeMeta = {
          brick: node.brick,
          enabled: !!node.enabled,
        };
      }
    },

    selectEdge(id) {
      this.selectedEdge = id;
      this.selectedNode = null;
    },

    touchNode() {
      const node = this.nodes.find((n) => n.id === this.selectedNode);
      if (!node) return;
      node.enabled = !!this.selectedNodeMeta.enabled;
    },

    deleteSelected() {
      if (this.selectedNode) {
        const id = this.selectedNode;
        this.nodes = this.nodes.filter((n) => n.id !== id);
        this.edges = this.edges.filter((e) => e.from !== id && e.to !== id);
        this.selectedNode = null;
        this.status = "Deleted brick";
        return;
      }
      if (this.selectedEdge) {
        this.edges = this.edges.filter((e) => e.id !== this.selectedEdge);
        this.selectedEdge = null;
        this.status = "Deleted edge";
      }
    },

    nodeCenter(id, side) {
      const node = this.nodes.find((n) => n.id === id);
      if (!node) return { x: 0, y: 0 };
      return {
        x: node.x + (side === "out" ? 160 : 0),
        y: node.y + 36,
      };
    },

    edgePath(edge) {
      const a = this.nodeCenter(edge.from, "out");
      const b = this.nodeCenter(edge.to, "in");
      const dx = Math.max(40, Math.abs(b.x - a.x) * 0.45);
      return (
        "M " +
        a.x +
        " " +
        a.y +
        " C " +
        (a.x + dx) +
        " " +
        a.y +
        ", " +
        (b.x - dx) +
        " " +
        b.y +
        ", " +
        b.x +
        " " +
        b.y
      );
    },

    svgPoint(evt) {
      const wrap = evt.currentTarget.closest
        ? evt.currentTarget.closest(".lego__canvas-wrap") || evt.currentTarget
        : evt.currentTarget;
      const svg = wrap.querySelector
        ? wrap.querySelector("svg")
        : document.querySelector(".lego__canvas");
      const rect = svg.getBoundingClientRect();
      const sx = ((evt.clientX - rect.left) / rect.width) * 1200;
      const sy = ((evt.clientY - rect.top) / rect.height) * 800;
      return {
        x: (sx - this.viewport.x) / this.viewport.zoom,
        y: (sy - this.viewport.y) / this.viewport.zoom,
      };
    },

    onWheel(evt) {
      const factor = evt.deltaY < 0 ? 1.08 : 0.92;
      const next = Math.min(2.5, Math.max(0.4, this.viewport.zoom * factor));
      this.viewport.zoom = next;
    },

    onCanvasDown(evt) {
      if (evt.button !== 0) return;
      if (this.connect) return;
      this.pan = {
        x: evt.clientX,
        y: evt.clientY,
        vx: this.viewport.x,
        vy: this.viewport.y,
      };
      this.selectedNode = null;
      this.selectedEdge = null;
    },

    onCanvasMove(evt) {
      if (this.pan) {
        const dx = evt.clientX - this.pan.x;
        const dy = evt.clientY - this.pan.y;
        this.viewport.x = this.pan.vx + dx;
        this.viewport.y = this.pan.vy + dy;
        return;
      }
      if (this.drag) {
        const p = this.svgPoint(evt);
        const node = this.nodes.find((n) => n.id === this.drag.id);
        if (node) {
          node.x = p.x - this.drag.ox;
          node.y = p.y - this.drag.oy;
        }
        return;
      }
      if (this.connect) {
        const p = this.svgPoint(evt);
        const a = this.nodeCenter(this.connect.from, "out");
        const dx = Math.max(40, Math.abs(p.x - a.x) * 0.45);
        this.draftPath =
          "M " +
          a.x +
          " " +
          a.y +
          " C " +
          (a.x + dx) +
          " " +
          a.y +
          ", " +
          (p.x - dx) +
          " " +
          p.y +
          ", " +
          p.x +
          " " +
          p.y;
      }
    },

    onCanvasUp() {
      this.pan = null;
      this.drag = null;
      this.connect = null;
      this.draftPath = "";
    },

    startDragNode(id, evt) {
      if (evt.button !== 0) return;
      const p = this.svgPoint(evt);
      const node = this.nodes.find((n) => n.id === id);
      if (!node) return;
      this.drag = { id, ox: p.x - node.x, oy: p.y - node.y };
      this.selectNode(id);
    },

    connectionKind(fromId, toId) {
      const fromNode = this.nodes.find((n) => n.id === fromId);
      const toNode = this.nodes.find((n) => n.id === toId);
      if (!fromNode || !toNode) return "scratch";
      const fromBrick = this.brickMap()[fromNode.brick];
      const toBrick = this.brickMap()[toNode.brick];
      if (!fromBrick || !toBrick) return "scratch";
      const outs = (fromBrick.ports && fromBrick.ports.out) || [];
      const ins = (toBrick.ports && toBrick.ports.in) || [];
      for (let i = 0; i < outs.length; i += 1) {
        if (ins.indexOf(outs[i]) >= 0) return outs[i];
      }
      return outs[0] || ins[0] || "scratch";
    },

    startConnect(id, side, evt) {
      if (evt.button !== 0) return;
      if (side === "in") {
        if (this.connect && this.connect.from !== id) {
          const exists = this.edges.some(
            (e) => e.from === this.connect.from && e.to === id
          );
          if (!exists) {
            const kind = this.connectionKind(this.connect.from, id);
            this.edges.push({
              id: uid("e"),
              from: this.connect.from,
              to: id,
              kind: kind,
            });
            this.status = "Connected (" + kind + ")";
          }
          this.connect = null;
          this.draftPath = "";
        }
        return;
      }
      this.connect = { from: id };
      this.draftPath = "";
    },
  };
}
