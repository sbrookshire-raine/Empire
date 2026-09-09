(function () {
  "use strict";

  var API = "/api/daze";
  var CX = 160;
  var CY = 160;
  var R_PLANNED = 118;
  var R_ACTUAL = 92;
  var PLANNED_INNER = 106;
  var PLANNED_OUTER = 130;
  var ACTUAL_INNER = 83;
  var ACTUAL_OUTER = 101;

  var KIND_COLORS = {
    focus: "#00e5ff",
    body: "#00fa9a",
    admin: "#ffea00",
    creative: "#ff00ff",
    rest: "#00bfff",
    other: "#e0f2fe",
  };

  function pad(n) {
    return String(n).padStart(2, "0");
  }

  function todayIso() {
    var d = new Date();
    return d.getFullYear() + "-" + pad(d.getMonth() + 1) + "-" + pad(d.getDate());
  }

  function timeToMinute(value) {
    if (!value || value.indexOf(":") < 0) return 0;
    var parts = value.split(":");
    var h = parseInt(parts[0], 10) || 0;
    var m = parseInt(parts[1], 10) || 0;
    return Math.max(0, Math.min(1439, h * 60 + m));
  }

  function minuteToTime(minute) {
    var m = Math.max(0, Math.min(1439, minute | 0));
    return pad(Math.floor(m / 60)) + ":" + pad(m % 60);
  }

  function minuteToAngle(minute) {
    return (minute / 1440) * Math.PI * 2 - Math.PI / 2;
  }

  function polar(angle, radius) {
    return {
      x: CX + Math.cos(angle) * radius,
      y: CY + Math.sin(angle) * radius,
    };
  }

  function sectorPath(startMinute, endMinute, innerR, outerR) {
    var start = startMinute | 0;
    var end = endMinute | 0;
    if (end <= start) {
      return "";
    }
    var a0 = minuteToAngle(start);
    var a1 = minuteToAngle(end);
    var p0o = polar(a0, outerR);
    var p1o = polar(a1, outerR);
    var p1i = polar(a1, innerR);
    var p0i = polar(a0, innerR);
    var large = end - start > 720 ? 1 : 0;
    return (
      "M " +
      p0o.x +
      " " +
      p0o.y +
      " A " +
      outerR +
      " " +
      outerR +
      " 0 " +
      large +
      " 1 " +
      p1o.x +
      " " +
      p1o.y +
      " L " +
      p1i.x +
      " " +
      p1i.y +
      " A " +
      innerR +
      " " +
      innerR +
      " 0 " +
      large +
      " 0 " +
      p0i.x +
      " " +
      p0i.y +
      " Z"
    );
  }

  function arcPathAtRadius(startMinute, endMinute, radius) {
    var a0 = minuteToAngle(startMinute);
    var a1 = minuteToAngle(endMinute);
    var p0 = polar(a0, radius);
    var p1 = polar(a1, radius);
    var sweep = endMinute - startMinute;
    var large = sweep > 720 ? 1 : 0;
    return (
      "M " +
      p0.x +
      " " +
      p0.y +
      " A " +
      radius +
      " " +
      radius +
      " 0 " +
      large +
      " 1 " +
      p1.x +
      " " +
      p1.y
    );
  }

  function kindColor(kind) {
    return KIND_COLORS[kind] || KIND_COLORS.focus;
  }

  function findConflicts(items) {
    var conflicts = [];
    var sorted = items.slice().sort(function (a, b) {
      return a.start_minute - b.start_minute;
    });
    for (var i = 0; i < sorted.length; i += 1) {
      for (var j = i + 1; j < sorted.length; j += 1) {
        var a = sorted[i];
        var b = sorted[j];
        if (b.start_minute >= a.end_minute) break;
        if (a.start_minute < b.end_minute && b.start_minute < a.end_minute) {
          conflicts.push({ a_id: a.id, b_id: b.id });
        }
      }
    }
    return conflicts;
  }

  function freeWindows(items, minMinutes) {
    var occupied = items
      .slice()
      .sort(function (a, b) {
        return a.start_minute - b.start_minute;
      })
      .map(function (x) {
        return [x.start_minute | 0, x.end_minute | 0];
      });
    var merged = [];
    occupied.forEach(function (pair) {
      if (!merged.length || pair[0] > merged[merged.length - 1][1]) {
        merged.push([pair[0], pair[1]]);
      } else {
        merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], pair[1]);
      }
    });
    var free = [];
    var cursor = 0;
    var minM = minMinutes || 30;
    merged.forEach(function (pair) {
      if (pair[0] - cursor >= minM) {
        free.push({
          start_minute: cursor,
          end_minute: pair[0],
          minutes: pair[0] - cursor,
          label: minuteToTime(cursor) + "–" + minuteToTime(pair[0]),
        });
      }
      cursor = Math.max(cursor, pair[1]);
    });
    if (1440 - cursor >= minM) {
      free.push({
        start_minute: cursor,
        end_minute: 1440,
        minutes: 1440 - cursor,
        label: minuteToTime(cursor) + "–24:00",
      });
    }
    return free;
  }

  function formatHourLabel(hour) {
    return pad(hour % 24);
  }

  function currentTimeLabel() {
    var now = new Date();
    return pad(now.getHours()) + ":" + pad(now.getMinutes());
  }

  function buildHourTicks() {
    var ticks = [];
    for (var h = 0; h < 24; h += 1) {
      var major = h % 6 === 0;
      var labeled = h % 3 === 0;
      var angle = minuteToAngle(h * 60);
      var outer = polar(angle, major ? R_PLANNED + 22 : R_PLANNED + 16);
      var inner = polar(angle, major ? R_PLANNED - 14 : R_PLANNED - 8);
      var labelPt = polar(angle, R_PLANNED + 34);
      ticks.push({
        hour: h,
        major: major,
        labeled: labeled,
        label: formatHourLabel(h),
        x1: inner.x,
        y1: inner.y,
        x2: outer.x,
        y2: outer.y,
        tx: labelPt.x,
        ty: labelPt.y,
      });
    }
    return ticks;
  }

  function buildSectors(items, innerR, outerR, conflicts) {
    var conflictIds = conflictIdMap(conflicts);
    return items.map(function (item) {
      return {
        id: item.id,
        title: item.title,
        color: item.color || kindColor(item.kind),
        conflict: !!conflictIds[item.id],
        d: sectorPath(item.start_minute | 0, item.end_minute | 0, innerR, outerR),
      };
    });
  }

  function buildArcs(items, radius, conflictIds) {
    return items.map(function (item) {
      return {
        id: item.id,
        title: item.title,
        color: item.color || kindColor(item.kind),
        conflict: !!conflictIds[item.id],
        d: arcPathAtRadius(item.start_minute | 0, item.end_minute | 0, radius),
      };
    });
  }

  function conflictIdMap(conflicts) {
    var map = {};
    conflicts.forEach(function (c) {
      map[c.a_id] = true;
      map[c.b_id] = true;
    });
    return map;
  }

  function isEmbedMode() {
    try {
      var q = new URLSearchParams(window.location.search);
      return q.get("embed") === "1" || q.get("widget") === "1";
    } catch (err) {
      return false;
    }
  }

  window.dazeDay = function dazeDay() {
    return {
      embedMode: isEmbedMode(),
      dockScreen: 0,
      dockScreenMax: 2,
      dockScreenLabels: ["Dial", "Schedule", "Blocks"],
      dockMaxBlocks: 4,
      dockMaxFree: 2,
      date: todayIso(),
      phase: "both",
      items: [],
      plannedItems: [],
      actualItems: [],
      conflicts: [],
      plannedConflicts: [],
      actualConflicts: [],
      free: [],
      loading: false,
      saving: false,
      status: "",
      editingId: "",
      nowTimeLabel: currentTimeLabel(),
      clockTimer: null,
      hourTicks: buildHourTicks(),
      form: {
        title: "",
        start: "09:00",
        end: "10:00",
        kind: "focus",
        phase: "planned",
        notes: "",
      },
      get dateShort() {
        return (this.date || "").slice(5) || "--";
      },
      get isToday() {
        return this.date === todayIso();
      },
      get nowNeedle() {
        if (!this.isToday) return null;
        var now = new Date();
        var minute = now.getHours() * 60 + now.getMinutes();
        var angle = minuteToAngle(minute);
        var outer = polar(angle, R_PLANNED + 24);
        var inner = polar(angle, R_ACTUAL - 24);
        return {
          x1: inner.x,
          y1: inner.y,
          x2: outer.x,
          y2: outer.y,
        };
      },
      get plannedArcs() {
        return buildSectors(this.plannedItems, PLANNED_INNER, PLANNED_OUTER, this.plannedConflicts);
      },
      get actualArcs() {
        return buildSectors(this.actualItems, ACTUAL_INNER, ACTUAL_OUTER, this.actualConflicts);
      },
      get singleArcs() {
        return buildSectors(this.items, PLANNED_INNER, PLANNED_OUTER, this.conflicts);
      },
      get dockTrackStyle() {
        return { transform: "translateX(-" + this.dockScreen * 100 + "%)" };
      },
      get dockScreenLabel() {
        return this.dockScreenLabels[this.dockScreen] || "Dial";
      },
      get dockBlockItems() {
        return this.items.slice(0, this.dockMaxBlocks);
      },
      get dockBlocksOverflow() {
        return Math.max(0, this.items.length - this.dockMaxBlocks);
      },
      get dockFreeItems() {
        return this.free.slice(0, this.dockMaxFree);
      },
      updateDockCapacity(viewportHeight) {
        var h = viewportHeight | 0;
        if (h >= 520) {
          this.dockMaxBlocks = 9;
          this.dockMaxFree = 4;
        } else if (h >= 420) {
          this.dockMaxBlocks = 7;
          this.dockMaxFree = 3;
        } else if (h >= 320) {
          this.dockMaxBlocks = 5;
          this.dockMaxFree = 3;
        } else if (h >= 240) {
          this.dockMaxBlocks = 4;
          this.dockMaxFree = 2;
        } else {
          this.dockMaxBlocks = 3;
          this.dockMaxFree = 1;
        }
      },
      notifyDockScreen() {
        if (!this.embedMode || !window.parent || window.parent === window) {
          return;
        }
        try {
          window.parent.postMessage(
            {
              type: "empire-tool-dock",
              tool: "daze",
              screen: this.dockScreen,
              label: this.dockScreenLabel,
            },
            window.location.origin
          );
        } catch (err) {
          /* ignore cross-origin */
        }
      },
      prevDockScreen() {
        if (this.dockScreen > 0) {
          this.dockScreen -= 1;
          this.notifyDockScreen();
        }
      },
      nextDockScreen() {
        if (this.dockScreen < this.dockScreenMax) {
          this.dockScreen += 1;
          this.notifyDockScreen();
        }
      },
      goDockScreen(index) {
        var n = index | 0;
        if (n < 0 || n > this.dockScreenMax) {
          return;
        }
        this.dockScreen = n;
        this.notifyDockScreen();
      },
      startAddBlock() {
        this.resetForm();
        this.goDockScreen(1);
      },
      editInDock(item) {
        this.edit(item);
        this.goDockScreen(1);
      },
      paintHourTicks(groupEl) {
        if (!groupEl) {
          return;
        }
        while (groupEl.firstChild) {
          groupEl.removeChild(groupEl.firstChild);
        }
        buildHourTicks().forEach(function (tick) {
          var line = document.createElementNS("http://www.w3.org/2000/svg", "line");
          line.setAttribute("x1", String(tick.x1));
          line.setAttribute("y1", String(tick.y1));
          line.setAttribute("x2", String(tick.x2));
          line.setAttribute("y2", String(tick.y2));
          line.setAttribute(
            "class",
            tick.major ? "daze__tick daze__tick--major" : "daze__tick"
          );
          groupEl.appendChild(line);
          if (tick.labeled) {
            var text = document.createElementNS("http://www.w3.org/2000/svg", "text");
            text.setAttribute("x", String(tick.tx));
            text.setAttribute("y", String(tick.ty));
            text.setAttribute(
              "class",
              tick.major
                ? "daze__tick-label daze__tick-label--major"
                : "daze__tick-label"
            );
            text.textContent = tick.label;
            groupEl.appendChild(text);
          }
        });
      },
      renderNowNeedle() {
        var needle = document.getElementById("daze-now-needle");
        var dot = document.getElementById("daze-now-dot");
        var n = this.nowNeedle;
        if (!needle) {
          return;
        }
        if (!n) {
          needle.style.display = "none";
          if (dot) {
            dot.style.display = "none";
          }
          return;
        }
        needle.setAttribute("x1", String(n.x1));
        needle.setAttribute("y1", String(n.y1));
        needle.setAttribute("x2", String(n.x2));
        needle.setAttribute("y2", String(n.y2));
        needle.style.display = "";
        if (dot) {
          dot.setAttribute("cx", String(n.x2));
          dot.setAttribute("cy", String(n.y2));
          dot.style.display = "";
        }
      },
      startClock() {
        var self = this;
        function tick() {
          self.nowTimeLabel = currentTimeLabel();
          if (self.isToday) {
            self.renderNowNeedle();
          }
        }
        tick();
        if (self.clockTimer) {
          clearInterval(self.clockTimer);
        }
        self.clockTimer = setInterval(tick, 30000);
      },
      stopClock() {
        if (this.clockTimer) {
          clearInterval(this.clockTimer);
          this.clockTimer = null;
        }
      },
      paintSectors(groupEl, sectors, classPrefix) {
        if (!groupEl) {
          return;
        }
        while (groupEl.firstChild) {
          groupEl.removeChild(groupEl.firstChild);
        }
        (sectors || []).forEach(function (sector) {
          if (!sector.d) {
            return;
          }
          var path = document.createElementNS("http://www.w3.org/2000/svg", "path");
          path.setAttribute("d", sector.d);
          path.setAttribute(
            "class",
            "daze__sector " +
              classPrefix +
              (sector.conflict ? " daze__sector--conflict" : "")
          );
          path.setAttribute("fill", sector.conflict ? "#ff4d6d" : sector.color);
          path.setAttribute("title", sector.title || "");
          groupEl.appendChild(path);
        });
      },
      renderDial() {
        var both = this.phase === "both";
        var tickG = document.getElementById("daze-hour-ticks");
        var plannedG = document.getElementById("daze-planned-sectors");
        var actualG = document.getElementById("daze-actual-sectors");
        var singleG = document.getElementById("daze-single-sectors");
        var actualRing = document.getElementById("daze-actual-ring");
        this.paintHourTicks(tickG);
        if (plannedG) {
          plannedG.style.display = both ? "" : "none";
        }
        if (actualG) {
          actualG.style.display = both ? "" : "none";
        }
        if (singleG) {
          singleG.style.display = both ? "none" : "";
        }
        if (actualRing) {
          actualRing.style.display = both ? "" : "none";
        }
        if (both) {
          this.paintSectors(plannedG, this.plannedArcs, "daze__sector--planned");
          this.paintSectors(actualG, this.actualArcs, "daze__sector--actual");
          if (singleG) {
            while (singleG.firstChild) {
              singleG.removeChild(singleG.firstChild);
            }
          }
        } else {
          this.paintSectors(singleG, this.singleArcs, "daze__sector--single");
          if (plannedG) {
            while (plannedG.firstChild) {
              plannedG.removeChild(plannedG.firstChild);
            }
          }
          if (actualG) {
            while (actualG.firstChild) {
              actualG.removeChild(actualG.firstChild);
            }
          }
        }
        this.renderNowNeedle();
      },
      bindDockResize() {
        if (!this.embedMode || typeof ResizeObserver === "undefined") {
          return;
        }
        var self = this;
        var viewport = document.querySelector(".tool-dock-carousel__viewport");
        if (!viewport) {
          return;
        }
        var ro = new ResizeObserver(function () {
          self.updateDockCapacity(viewport.clientHeight);
          self.renderDial();
        });
        self.updateDockCapacity(viewport.clientHeight);
        ro.observe(viewport);
      },
      async init() {
        if (this.embedMode) {
          document.documentElement.classList.add("daze-embed");
          document.body.classList.add("daze-embed");
        }
        this.startClock();
        await this.load();
        this.$nextTick(function () {
          this.bindDockResize();
        }.bind(this));
        this.notifyDockScreen();
      },
      fmtRange(start, end) {
        return minuteToTime(start) + "–" + minuteToTime(end);
      },
      isConflict(id) {
        var inList = function (list) {
          return list.some(function (c) {
            return c.a_id === id || c.b_id === id;
          });
        };
        if (this.phase === "both") {
          return inList(this.plannedConflicts) || inList(this.actualConflicts);
        }
        return inList(this.conflicts);
      },
      resetForm() {
        this.editingId = "";
        this.form = {
          title: "",
          start: "09:00",
          end: "10:00",
          kind: "focus",
          phase: this.phase === "actual" ? "actual" : "planned",
          notes: "",
        };
      },
      edit(item) {
        this.editingId = item.id;
        this.form = {
          title: item.title || "",
          start: minuteToTime(item.start_minute),
          end: minuteToTime(item.end_minute),
          kind: item.kind || "focus",
          phase: item.phase || "planned",
          notes: item.notes || "",
        };
      },
      applyBothPayload(data) {
        this.plannedItems = data.planned || [];
        this.actualItems = data.actual || [];
        this.plannedConflicts = data.planned_conflicts || [];
        this.actualConflicts = data.actual_conflicts || [];
        if (this.phase === "planned") {
          this.items = this.plannedItems;
          this.conflicts = this.plannedConflicts;
        } else if (this.phase === "actual") {
          this.items = this.actualItems;
          this.conflicts = this.actualConflicts;
        } else {
          this.items = this.plannedItems.concat(this.actualItems);
          this.conflicts = this.plannedConflicts.concat(this.actualConflicts);
        }
        this.free = freeWindows(this.items.filter(function (x) {
          return x.phase === (this.phase === "actual" ? "actual" : "planned");
        }.bind(this)), 30);
        if (this.phase === "both") {
          this.free = freeWindows(this.plannedItems, 30);
        }
      },
      async load() {
        this.loading = true;
        this.status = "Loading…";
        try {
          var phaseParam = this.phase === "both" ? "both" : this.phase;
          var url =
            API +
            "/day?date=" +
            encodeURIComponent(this.date) +
            "&phase=" +
            encodeURIComponent(phaseParam);
          var res = await fetch(url);
          var data = await res.json();
          if (!res.ok || !data.ok) {
            throw new Error(data.error || "DAZE API " + res.status);
          }
          if (phaseParam === "both") {
            this.applyBothPayload(data);
          } else {
            this.items = data.items || [];
            this.conflicts = data.conflicts || [];
            this.plannedItems = this.phase === "planned" ? this.items : [];
            this.actualItems = this.phase === "actual" ? this.items : [];
            this.plannedConflicts = this.phase === "planned" ? this.conflicts : [];
            this.actualConflicts = this.phase === "actual" ? this.conflicts : [];
            this.free = freeWindows(this.items, 30);
          }
          var blockCount =
            this.phase === "both"
              ? this.plannedItems.length + " planned · " + this.actualItems.length + " actual"
              : this.items.length + " block(s)";
          var conflictCount =
            this.phase === "both"
              ? this.plannedConflicts.length + this.actualConflicts.length
              : this.conflicts.length;
          this.status =
            blockCount + (conflictCount ? " · " + conflictCount + " conflict(s)" : "");
          this.renderDial();
        } catch (err) {
          this.items = [];
          this.plannedItems = [];
          this.actualItems = [];
          this.conflicts = [];
          this.plannedConflicts = [];
          this.actualConflicts = [];
          this.free = [];
          this.status = err && err.message ? err.message : String(err);
          this.renderDial();
        } finally {
          this.loading = false;
        }
      },
      async save() {
        this.saving = true;
        try {
          var body = {
            date: this.date,
            title: this.form.title,
            start_minute: timeToMinute(this.form.start),
            end_minute: timeToMinute(this.form.end),
            kind: this.form.kind,
            phase: this.form.phase,
            notes: this.form.notes || "",
            color: kindColor(this.form.kind),
          };
          if (body.end_minute <= body.start_minute) {
            throw new Error("End must be after start.");
          }
          if (this.editingId) {
            body.id = this.editingId;
          }
          var res = await fetch(API + "/block", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
          });
          var data = await res.json();
          if (!res.ok || !data.ok) {
            throw new Error(data.error || "Save failed");
          }
          this.resetForm();
          await this.load();
          if (this.embedMode) {
            this.goDockScreen(0);
          }
        } catch (err) {
          this.status = err && err.message ? err.message : String(err);
        } finally {
          this.saving = false;
        }
      },
      async remove(id) {
        if (!id || !window.confirm("Delete this block?")) return;
        try {
          var res = await fetch(API + "/block?id=" + encodeURIComponent(id), {
            method: "DELETE",
          });
          var data = await res.json();
          if (!res.ok || !data.ok) {
            throw new Error(data.error || "Delete failed");
          }
          await this.load();
        } catch (err) {
          this.status = err && err.message ? err.message : String(err);
        }
      },
    };
  };
})();
