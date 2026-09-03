(function () {
  var key = "second-engine-theme";
  function stored() { try { return localStorage.getItem(key); } catch (_) { return null; } }
  function apply(mode) {
    if (mode === "dark" || mode === "light") document.documentElement.setAttribute("data-theme", mode);
    else document.documentElement.removeAttribute("data-theme");
  }
  function dark() {
    var value = stored();
    return value ? value === "dark" : window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
  }
  apply(stored());
  document.addEventListener("DOMContentLoaded", function () {
    var button = document.querySelector(".theme-toggle");
    if (!button) return;
    function label() { button.textContent = dark() ? "☀ Light" : "☾ Dark"; }
    label();
    button.addEventListener("click", function () {
      var next = dark() ? "light" : "dark";
      try { localStorage.setItem(key, next); } catch (_) {}
      apply(next);
      label();
    });
  });
})();
