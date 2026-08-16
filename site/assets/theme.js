(() => {
  const STORAGE_KEY = "aac-color-theme";
  const OPTIONS = new Set(["system", "light", "dark"]);
  const root = document.documentElement;
  const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");

  function readPreference() {
    try {
      const stored = window.localStorage.getItem(STORAGE_KEY);
      return OPTIONS.has(stored) ? stored : "system";
    } catch (error) {
      return "system";
    }
  }

  function resolvedTheme(preference) {
    return preference === "system"
      ? systemTheme.matches
        ? "dark"
        : "light"
      : preference;
  }

  function updateControls(preference) {
    document.querySelectorAll("[data-theme-option]").forEach((button) => {
      button.setAttribute(
        "aria-pressed",
        String(button.dataset.themeOption === preference),
      );
    });
  }

  function applyTheme(preference, persist = false) {
    const choice = OPTIONS.has(preference) ? preference : "system";
    const resolved = resolvedTheme(choice);

    root.dataset.themePreference = choice;
    root.dataset.resolvedTheme = resolved;
    if (choice === "system") {
      root.removeAttribute("data-theme");
    } else {
      root.dataset.theme = choice;
    }
    root.style.colorScheme = resolved;

    const themeColor = document.querySelector("#theme-color");
    if (themeColor) {
      themeColor.content = resolved === "dark" ? "#101620" : "#ffffff";
    }
    updateControls(choice);

    if (persist) {
      try {
        window.localStorage.setItem(STORAGE_KEY, choice);
      } catch (error) {
        // The selected theme still applies when storage is unavailable.
      }
    }

    window.dispatchEvent(
      new CustomEvent("aac:themechange", {
        detail: { preference: choice, resolvedTheme: resolved },
      }),
    );
  }

  const initialPreference = readPreference();
  applyTheme(initialPreference);

  function initializeControls() {
    updateControls(initialPreference);
    document.querySelectorAll("[data-theme-option]").forEach((button) => {
      button.addEventListener("click", () => {
        applyTheme(button.dataset.themeOption, true);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initializeControls, { once: true });
  } else {
    initializeControls();
  }

  systemTheme.addEventListener("change", () => {
    if (root.dataset.themePreference === "system") applyTheme("system");
  });
})();
