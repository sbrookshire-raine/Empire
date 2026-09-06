(function () {
  "use strict";

  var PB = "http://127.0.0.1:8090/api/collections/day_blocks/records";
  var R = 120;
  var CX = 160;
  var CY = 160;

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
    // 0 at top (midnight), clockwise through the day.
    return (minute / 1440) * Math.PI * 2 - Math.PI / 2;
  }

  function polar(angle, radius) {
    return {
      x: CX + Math.cos(angle) * radius,
      y: CY + Math.sin(angle) * radius,
    };
  }

  function arcPath(startMinute, endMinute) {
    var a0 = minuteToAngle(startMinute);
    var a1 = minuteToAngle(endMinute);
    var p0 = polar(a0, R);
    var p1 = polar(a1, R);
    var sweep = endMinute - startMinute;
    var large = sweep > 720 ? 1 : 0;
    return (
      "M " +
      p0.x +
      " " +
      p0.y +
      " A " +
      R +
      " " +
      R +
      " 0 " +
      large +
      " 1 " +
      p1.x +
      " " +
      p1.y
    );
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

  function buildHourTicks() {
    var ticks = [];
    for (var h = 0; h < 24; h += 3) {
      var angle = minuteToAngle(h * 60);
      var outer = polar(angle, R + 18);
      var inner = polar(angle, R - 18);
      var label = polar(angle, R + 28);
      ticks.push({
        label: String(h),
        x1: inner.x,
        y1: inner.y,
        x2: outer.x,
        y2: outer.y,
        tx: label.x,
        ty: label.y,
      });
    }
    return ticks;
  }

  window.dazeDay = function dazeDay() {
    return {
      date: todayIso(),
      phase: "planned",
      items: [],
      conflicts: [],
      free: [],
      loading: false,
      saving: false,
      status: "",
      editingId: "",
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
      get arcs() {
        var conflictIds = {};
        this.conflicts.forEach(function (c) {
          conflictIds[c.a_id] = true;
          conflictIds[c.b_id] = true;
        });
        return this.items.map(function (item) {
          return {
            id: item.id,
            title: item.title,
            color: item.color || "#5b8def",
            conflict: !!conflictIds[item.id],
            d: arcPath(item.start_minute | 0, item.end_minute | 0),
          };
        });
      },
      async init() {
        await this.load();
      },
      fmtRange(start, end) {
        return minuteToTime(start) + "–" + minuteToTime(end);
      },
      isConflict(id) {
        return this.conflicts.some(function (c) {
          return c.a_id === id || c.b_id === id;
        });
      },
      resetForm() {
        this.editingId = "";
        this.form = {
          title: "",
          start: "09:00",
          end: "10:00",
          kind: "focus",
          phase: this.phase,
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
      async load() {
        this.loading = true;
        this.status = "Loading…";
        try {
          var filter =
            'date = "' +
            this.date +
            '" && phase = "' +
            this.phase +
            '"';
          var url =
            PB +
            "?filter=" +
            encodeURIComponent(filter) +
            "&sort=start_minute&perPage=200";
          var res = await fetch(url);
          if (!res.ok) {
            throw new Error("PocketBase " + res.status + " — is day_blocks migrated?");
          }
          var data = await res.json();
          this.items = data.items || [];
          this.conflicts = findConflicts(this.items);
          this.free = freeWindows(this.items, 30);
          this.status =
            this.items.length +
            " block(s)" +
            (this.conflicts.length ? " · " + this.conflicts.length + " conflict(s)" : "");
        } catch (err) {
          this.items = [];
          this.conflicts = [];
          this.free = [];
          this.status = err && err.message ? err.message : String(err);
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
            color: "",
          };
          if (body.end_minute <= body.start_minute) {
            throw new Error("End must be after start.");
          }
          var url = this.editingId ? PB + "/" + this.editingId : PB;
          var res = await fetch(url, {
            method: this.editingId ? "PATCH" : "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(body),
          });
          if (!res.ok) {
            throw new Error(await res.text());
          }
          this.resetForm();
          await this.load();
        } catch (err) {
          this.status = err && err.message ? err.message : String(err);
        } finally {
          this.saving = false;
        }
      },
      async remove(id) {
        if (!id || !window.confirm("Delete this block?")) return;
        try {
          var res = await fetch(PB + "/" + id, { method: "DELETE" });
          if (!res.ok && res.status !== 204) {
            throw new Error(await res.text());
          }
          await this.load();
        } catch (err) {
          this.status = err && err.message ? err.message : String(err);
        }
      },
    };
  };
})();
