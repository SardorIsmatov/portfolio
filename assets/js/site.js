/* Sardor Ismatov - portfolio. Small, dependency-free progressive enhancements. */
(function () {
  "use strict";

  var root = document.documentElement;
  root.classList.add("js");

  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function storageGet(key) {
    try { return window.localStorage.getItem(key); } catch (e) { return null; }
  }
  function storageSet(key, value) {
    try { window.localStorage.setItem(key, value); } catch (e) { /* storage unavailable */ }
  }

  /* ---------- Footer year ---------- */
  var years = document.querySelectorAll("[data-year]");
  for (var y = 0; y < years.length; y++) years[y].textContent = String(new Date().getFullYear());

  /* ---------- Theme toggle ---------- */
  var darkQuery = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function currentTheme() {
    var set = root.getAttribute("data-theme");
    if (set === "light" || set === "dark") return set;
    return darkQuery && darkQuery.matches ? "dark" : "light";
  }

  function syncThemeUI() {
    var theme = currentTheme();
    var next = theme === "dark" ? "light" : "dark";
    var toggles = document.querySelectorAll("[data-theme-toggle]");
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute("aria-label", "Switch to " + next + " theme");
      toggles[i].setAttribute("title", "Switch to " + next + " theme");
    }
    var metas = document.querySelectorAll('meta[name="theme-color"]');
    for (var m = 0; m < metas.length; m++) {
      if (root.getAttribute("data-theme")) {
        metas[m].setAttribute("content", theme === "dark" ? "#0b1120" : "#f6f8fb");
      }
    }
  }

  document.addEventListener("click", function (event) {
    var btn = event.target.closest && event.target.closest("[data-theme-toggle]");
    if (!btn) return;
    var next = currentTheme() === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    storageSet("theme", next);
    syncThemeUI();
  });

  if (darkQuery) {
    var onSchemeChange = function () { if (!storageGet("theme")) syncThemeUI(); };
    if (darkQuery.addEventListener) darkQuery.addEventListener("change", onSchemeChange);
    else if (darkQuery.addListener) darkQuery.addListener(onSchemeChange);
  }
  syncThemeUI();

  /* ---------- Header: scrolled state ---------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("is-scrolled", window.scrollY > 4); };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Mobile menu ---------- */
  var menuBtn = document.querySelector("[data-menu-toggle]");
  var nav = document.getElementById("site-nav");
  if (menuBtn && nav) {
    var setOpen = function (open, returnFocus) {
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
      menuBtn.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      nav.classList.toggle("is-open", open);
      if (open) {
        var first = nav.querySelector("a");
        if (first) first.focus();
      } else if (returnFocus) {
        menuBtn.focus();
      }
    };
    menuBtn.addEventListener("click", function () {
      setOpen(menuBtn.getAttribute("aria-expanded") !== "true", false);
    });
    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setOpen(false, false);
    });
    document.addEventListener("keydown", function (event) {
      if ((event.key === "Escape" || event.key === "Esc") && menuBtn.getAttribute("aria-expanded") === "true") {
        setOpen(false, true);
      }
    });
    document.addEventListener("click", function (event) {
      if (menuBtn.getAttribute("aria-expanded") !== "true") return;
      if (nav.contains(event.target) || menuBtn.contains(event.target)) return;
      setOpen(false, false);
    });
    var desktop = window.matchMedia ? window.matchMedia("(min-width: 800px)") : null;
    if (desktop) {
      var onDesktop = function () { if (desktop.matches) setOpen(false, false); };
      if (desktop.addEventListener) desktop.addEventListener("change", onDesktop);
      else if (desktop.addListener) desktop.addListener(onDesktop);
    }
  }

  /* ---------- Scroll-spy for in-page nav links (home page) ---------- */
  var spyLinks = document.querySelectorAll("[data-spy]");
  if (spyLinks.length && "IntersectionObserver" in window) {
    var byId = {};
    var sections = [];
    for (var s = 0; s < spyLinks.length; s++) {
      var id = spyLinks[s].getAttribute("data-spy");
      var el = document.getElementById(id);
      if (el) { byId[id] = spyLinks[s]; sections.push(el); }
    }
    var visible = {};
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) { visible[entry.target.id] = entry.isIntersecting; });
      var active = null;
      for (var i = 0; i < sections.length; i++) {
        if (visible[sections[i].id]) { active = sections[i].id; break; }
      }
      Object.keys(byId).forEach(function (key) {
        if (key === active) byId[key].setAttribute("aria-current", "true");
        else byId[key].removeAttribute("aria-current");
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (section) { spy.observe(section); });
  }

  /* ---------- Reveal on scroll (never hides above-the-fold content) ---------- */
  if (!reduceMotion && "IntersectionObserver" in window) {
    var revealEls = document.querySelectorAll(".reveal");
    var viewportH = window.innerHeight || 800;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("reveal-in");
        entry.target.classList.remove("reveal-pending");
        io.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    for (var r = 0; r < revealEls.length; r++) {
      if (revealEls[r].getBoundingClientRect().top > viewportH) {
        revealEls[r].classList.add("reveal-pending");
        io.observe(revealEls[r]);
      }
    }
  }

  /* ---------- Power BI embeds: load the iframe only on wider screens ---------- */
  var frames = document.querySelectorAll("iframe[data-src]");
  if (frames.length) {
    var wide = window.matchMedia ? window.matchMedia("(min-width: 768px)") : null;
    var loadFrames = function () {
      if (wide && !wide.matches) return;
      for (var f = 0; f < frames.length; f++) {
        if (!frames[f].getAttribute("src")) frames[f].setAttribute("src", frames[f].getAttribute("data-src"));
      }
    };
    loadFrames();
    if (wide) {
      if (wide.addEventListener) wide.addEventListener("change", loadFrames);
      else if (wide.addListener) wide.addListener(loadFrames);
    }
  }

  /* ---------- Project filter ---------- */
  var filterBar = document.querySelector("[data-filters]");
  if (filterBar) {
    var items = document.querySelectorAll("[data-type]");
    var buttons = filterBar.querySelectorAll("[data-filter]");
    var live = document.querySelector("[data-filter-status]");
    filterBar.hidden = false;
    filterBar.addEventListener("click", function (event) {
      var btn = event.target.closest("[data-filter]");
      if (!btn) return;
      var value = btn.getAttribute("data-filter");
      var shown = 0;
      for (var b = 0; b < buttons.length; b++) {
        buttons[b].setAttribute("aria-pressed", buttons[b] === btn ? "true" : "false");
      }
      for (var i = 0; i < items.length; i++) {
        var match = value === "all" || items[i].getAttribute("data-type") === value;
        items[i].hidden = !match;
        if (match) shown++;
      }
      if (live) live.textContent = "Showing " + shown + " project" + (shown === 1 ? "" : "s");
    });
  }

  /* ---------- Contact form ---------- */
  var form = document.querySelector("[data-contact-form]");
  if (form && window.fetch && window.FormData) {
    var status = form.querySelector("[data-form-status]");
    var submit = form.querySelector('button[type="submit"]');
    var submitLabel = submit ? submit.innerHTML : "";
    var email = form.getAttribute("data-email") || "";

    var showStatus = function (kind, html) {
      if (!status) return;
      status.className = "form-status " + (kind === "ok" ? "is-success" : "is-error");
      var icon = kind === "ok"
        ? '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.6 2.5L16 9.5"/></svg>'
        : '<svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5.5"/><path d="M12 16.5h.01"/></svg>';
      status.innerHTML = icon + "<div>" + html + "</div>";
      status.hidden = false;
    };

    form.addEventListener("submit", function (event) {
      if (typeof form.checkValidity === "function" && !form.checkValidity()) return;
      event.preventDefault();
      if (status) status.hidden = true;
      if (submit) {
        submit.disabled = true;
        submit.textContent = "Sending…";
      }
      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (response) {
          if (response.ok) {
            form.reset();
            showStatus("ok", "<strong>Thank you, your message has been sent.</strong> I will get back to you as soon as I can.");
          } else {
            throw new Error("Request failed with status " + response.status);
          }
        })
        .catch(function () {
          showStatus("error", "<strong>Sorry, the message could not be sent.</strong> Please email me directly at " +
            '<a href="mailto:' + email + '">' + email + "</a>.");
        })
        .then(function () {
          if (submit) {
            submit.disabled = false;
            submit.innerHTML = submitLabel;
          }
        });
    });
  }
})();
