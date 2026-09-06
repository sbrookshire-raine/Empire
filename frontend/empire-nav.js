(function () {
  var NAV_LINKS = [
    { id: "dashboard", label: "Dashboard", href: "http://127.0.0.1:8080/dashboard.html" },
    { id: "eve", label: "Eve", href: "http://127.0.0.1:8080/eve.html" },
    { id: "daze", label: "DAZE", href: "http://127.0.0.1:8080/daze.html" },
    { id: "primitives", label: "Primitives", href: "http://127.0.0.1:8080/primitives.html" },
    { id: "wiki", label: "Wiki", href: "http://127.0.0.1:8080/wiki.html" },
    { id: "tasks", label: "Tasks", href: "http://127.0.0.1:8080/" },
    { id: "backend", label: "Backend", href: "http://127.0.0.1:8090/" },
    { id: "health", label: "Health", href: "http://127.0.0.1:8090/health.html" },
    { id: "admin", label: "Admin", href: "http://127.0.0.1:8090/_/" },
  ];

  function renderNav() {
    var mount = document.getElementById("empire-nav");
    if (!mount) return;

    var current = mount.getAttribute("data-current") || "";

    var brand = document.createElement("strong");
    brand.className = "empire-brand";
    brand.textContent = "EMPIRE";

    var list = document.createElement("ul");
    NAV_LINKS.forEach(function (link) {
      var item = document.createElement("li");
      var anchor = document.createElement("a");
      anchor.href = link.href;
      anchor.textContent = link.label;
      if (link.id === current) {
        anchor.setAttribute("aria-current", "page");
      }
      item.appendChild(anchor);
      list.appendChild(item);
    });

    mount.classList.add("empire-nav");
    mount.replaceChildren(brand, list);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderNav);
  } else {
    renderNav();
  }
})();
