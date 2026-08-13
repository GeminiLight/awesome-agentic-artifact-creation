document.documentElement.classList.add("js");

const DEFAULT_PAGE_SIZE = 25;
const PAGE_SIZE_OPTIONS = [10, 25, 50, 100];
const FALLBACK_COLOR = "#8a96a8";

const state = {
  catalog: null,
  view: "artifact",
  primary: "",
  year: "",
  kind: "",
  status: "",
  search: "",
  sort: "recent",
  page: 1,
  pageSize: DEFAULT_PAGE_SIZE,
};

const elements = {
  resultsPanel: document.querySelector(".results-panel"),
  paperList: document.querySelector("#paper-list"),
  resultCount: document.querySelector("#result-count"),
  emptyState: document.querySelector("#empty-state"),
  pagination: document.querySelector("#pagination"),
  search: document.querySelector("#paper-search"),
  primary: document.querySelector("#primary-filter"),
  primaryLabel: document.querySelector("#primary-filter-label"),
  year: document.querySelector("#year-filter"),
  kind: document.querySelector("#kind-filter"),
  status: document.querySelector("#status-filter"),
  sort: document.querySelector("#sort-order"),
  pageSize: document.querySelector("#page-size"),
  activeFilters: document.querySelector("#active-filters"),
  clearFilters: document.querySelector("#clear-filters"),
  familyOverview: document.querySelector("#family-overview"),
  applicationOverview: document.querySelector("#application-overview"),
};

const selectWidgets = new WeakMap();
const selectWidgetList = [];
let selectWidgetCount = 0;

function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function createIcon(name) {
  const icon = createElement("i", `ph ${name}`);
  icon.setAttribute("aria-hidden", "true");
  return icon;
}

function titleCase(value) {
  return value ? value.charAt(0).toUpperCase() + value.slice(1) : "";
}

function formatNumber(value) {
  return new Intl.NumberFormat("en").format(value);
}

function closeCustomSelect(widget, { restoreFocus = false } = {}) {
  if (!widget || !widget.wrapper.classList.contains("is-open")) return;
  widget.wrapper.classList.remove("is-open");
  widget.trigger.setAttribute("aria-expanded", "false");
  widget.menu.hidden = true;
  if (restoreFocus) widget.trigger.focus();
}

function closeOtherCustomSelects(activeWidget) {
  selectWidgetList.forEach((widget) => {
    if (widget !== activeWidget) closeCustomSelect(widget);
  });
}

function customSelectOptions(widget) {
  return [...widget.menu.querySelectorAll('[role="option"]')];
}

function focusCustomSelectOption(widget, index) {
  const options = customSelectOptions(widget);
  if (!options.length) return;
  const nextIndex = Math.max(0, Math.min(index, options.length - 1));
  options[nextIndex].focus();
  options[nextIndex].scrollIntoView({ block: "nearest" });
}

function openCustomSelect(widget, preferredIndex = widget.select.selectedIndex) {
  closeOtherCustomSelects(widget);
  widget.wrapper.classList.add("is-open");
  widget.trigger.setAttribute("aria-expanded", "true");
  widget.menu.hidden = false;
  focusCustomSelectOption(widget, preferredIndex < 0 ? 0 : preferredIndex);
}

function chooseCustomSelectOption(widget, index) {
  const option = widget.select.options[index];
  if (!option || option.disabled) return;
  const changed = widget.select.selectedIndex !== index;
  widget.select.selectedIndex = index;
  refreshCustomSelect(widget.select);
  widget.trigger.focus();
  if (changed) {
    widget.select.dispatchEvent(new Event("change", { bubbles: true }));
  }
}

function handleCustomSelectKeydown(event, widget, index) {
  const lastIndex = widget.select.options.length - 1;
  if (event.key === "ArrowDown") {
    event.preventDefault();
    focusCustomSelectOption(widget, index === lastIndex ? 0 : index + 1);
  } else if (event.key === "ArrowUp") {
    event.preventDefault();
    focusCustomSelectOption(widget, index === 0 ? lastIndex : index - 1);
  } else if (event.key === "Home") {
    event.preventDefault();
    focusCustomSelectOption(widget, 0);
  } else if (event.key === "End") {
    event.preventDefault();
    focusCustomSelectOption(widget, lastIndex);
  } else if (event.key === "Enter" || event.key === " ") {
    event.preventDefault();
    chooseCustomSelectOption(widget, index);
  } else if (event.key === "Escape") {
    event.preventDefault();
    closeCustomSelect(widget, { restoreFocus: true });
  } else if (event.key === "Tab") {
    closeCustomSelect(widget);
  }
}

function refreshCustomSelect(select) {
  const widget = selectWidgets.get(select);
  if (!widget) return;

  closeCustomSelect(widget);
  const fragment = document.createDocumentFragment();
  [...select.options].forEach((option, index) => {
    const item = createElement("div", "select-option", option.textContent);
    item.id = `${widget.menu.id}-option-${index}`;
    item.dataset.index = String(index);
    item.setAttribute("role", "option");
    item.setAttribute("aria-selected", String(option.selected));
    item.tabIndex = -1;
    if (option.selected) item.classList.add("is-selected");
    if (option.disabled) item.setAttribute("aria-disabled", "true");
    item.addEventListener("click", () => chooseCustomSelectOption(widget, index));
    item.addEventListener("keydown", (event) =>
      handleCustomSelectKeydown(event, widget, index),
    );
    fragment.append(item);
  });
  widget.menu.replaceChildren(fragment);
  const selected = select.options[select.selectedIndex] || select.options[0];
  widget.value.textContent = selected ? selected.textContent : "Select";
}

function enhanceSelect(select) {
  if (selectWidgets.has(select)) return;

  selectWidgetCount += 1;
  const wrapper = createElement("div", "custom-select");
  const trigger = createElement("button", "select-trigger");
  const value = createElement("span", "select-value");
  const caret = createElement("span", "select-caret");
  const menu = createElement("div", "select-menu");
  const menuId = `select-menu-${selectWidgetCount}`;
  const labelId = select.getAttribute("aria-labelledby");

  trigger.type = "button";
  trigger.setAttribute("aria-haspopup", "listbox");
  trigger.setAttribute("aria-expanded", "false");
  trigger.setAttribute("aria-controls", menuId);
  if (labelId) trigger.setAttribute("aria-labelledby", `${labelId} ${menuId}-value`);
  value.id = `${menuId}-value`;
  caret.setAttribute("aria-hidden", "true");
  menu.id = menuId;
  menu.setAttribute("role", "listbox");
  if (labelId) menu.setAttribute("aria-labelledby", labelId);
  menu.hidden = true;

  select.classList.add("select-native-hidden");
  select.tabIndex = -1;
  select.setAttribute("aria-hidden", "true");
  const selectParent = select.parentNode;
  selectParent.insertBefore(wrapper, select);
  wrapper.append(select, trigger, menu);
  trigger.append(value, caret);

  const widget = { select, wrapper, trigger, value, menu };
  selectWidgets.set(select, widget);
  selectWidgetList.push(widget);
  refreshCustomSelect(select);

  trigger.addEventListener("click", () => {
    if (wrapper.classList.contains("is-open")) {
      closeCustomSelect(widget);
    } else {
      openCustomSelect(widget);
    }
  });
  trigger.addEventListener("keydown", (event) => {
    if (["ArrowDown", "ArrowUp", "Enter", " "].includes(event.key)) {
      event.preventDefault();
      const preferredIndex =
        event.key === "ArrowUp" ? select.options.length - 1 : select.selectedIndex;
      openCustomSelect(widget, preferredIndex);
    } else if (event.key === "Escape") {
      closeCustomSelect(widget);
    }
  });
}

function setupCustomSelects() {
  [
    elements.primary,
    elements.year,
    elements.kind,
    elements.status,
    elements.pageSize,
    elements.sort,
  ].forEach(enhanceSelect);
  document.addEventListener("pointerdown", (event) => {
    selectWidgetList.forEach((widget) => {
      if (!widget.wrapper.contains(event.target)) closeCustomSelect(widget);
    });
  });
}

function familyColor(paper) {
  const family = state.catalog.families.find(
    (candidate) => candidate.name === paper.artifact_family,
  );
  return family ? family.color : FALLBACK_COLOR;
}

function setSelectOptions(select, options, emptyLabel) {
  select.replaceChildren();
  const empty = new Option(emptyLabel, "");
  select.add(empty);
  options.forEach(({ label, value }) => select.add(new Option(label, value)));
  refreshCustomSelect(select);
}

function hydrateSummary() {
  const { summary } = state.catalog;
  document.querySelectorAll("[data-stat]").forEach((element) => {
    element.textContent = formatNumber(summary[element.dataset.stat]);
  });
  document.querySelector("#hero-total").textContent = `${formatNumber(summary.total)} audited papers`;
}

function renderTaxonomyOverview() {
  const familyFragment = document.createDocumentFragment();
  state.catalog.families.forEach((family) => {
    const button = createElement("button", "taxonomy-item");
    button.type = "button";
    button.style.setProperty("--family-color", family.color);
    button.setAttribute("aria-label", `Browse ${family.name}`);

    button.append(createElement("span", "taxonomy-swatch"));
    button.append(createElement("strong", "", family.name));
    button.append(
      createElement(
        "span",
        "taxonomy-types",
        family.types
          .filter((type) => type.count)
          .map((type) => type.name)
          .join(" · "),
      ),
    );
    button.append(
      createElement("span", "taxonomy-count", `${family.count} papers`),
    );
    button.addEventListener("click", () => openCatalog("artifact", family.name));
    familyFragment.append(button);
  });
  elements.familyOverview.replaceChildren(familyFragment);

  const applicationFragment = document.createDocumentFragment();
  state.catalog.applications.forEach((application, index) => {
    const button = createElement("button", "application-item");
    button.type = "button";
    button.setAttribute("aria-label", `Browse ${application.name}`);
    button.append(
      createElement("span", "application-index", String(index + 1).padStart(2, "0")),
    );
    button.append(createElement("strong", "", application.name));
    button.append(
      createElement("span", "application-count", `${application.count} papers`),
    );
    button.addEventListener("click", () => openCatalog("application", application.name));
    applicationFragment.append(button);
  });
  elements.applicationOverview.replaceChildren(applicationFragment);
}

function renderFilterOptions() {
  const options =
    state.view === "artifact"
      ? state.catalog.families.map((family) => ({
          label: `${family.name} (${family.count})`,
          value: family.name,
        }))
      : state.catalog.applications.map((application) => ({
          label: `${application.name} (${application.count})`,
          value: application.name,
        }));

  const noneLabel =
    state.view === "artifact" ? "No artifact label" : "No application label";
  const emptyLabel = state.view === "artifact" ? "All families" : "All domains";
  options.push({ label: noneLabel, value: "__none__" });
  setSelectOptions(elements.primary, options, emptyLabel);
  elements.primary.value = state.primary;
  refreshCustomSelect(elements.primary);
  elements.primaryLabel.textContent =
    state.view === "artifact" ? "Artifact family" : "Application domain";

  document.querySelectorAll('input[name="catalog-view"]').forEach((input) => {
    input.checked = input.value === state.view;
  });
}

function renderYearOptions() {
  setSelectOptions(
    elements.year,
    state.catalog.years.map(({ year, count }) => ({
      label: `${year} (${count})`,
      value: year,
    })),
    "All years",
  );
  elements.year.value = state.year;
  refreshCustomSelect(elements.year);
}

function searchableText(paper) {
  return [
    paper.title,
    paper.name,
    paper.authors,
    paper.venue_display_name,
    paper.artifact_family,
    paper.artifact_type,
    paper.artifact_subtype,
    paper.application_domain,
    paper.application_subdomain,
  ]
    .join(" ")
    .toLocaleLowerCase();
}

function filteredPapers() {
  const primaryField =
    state.view === "artifact" ? "artifact_family" : "application_domain";
  const queryTerms = state.search
    .trim()
    .toLocaleLowerCase()
    .split(/\s+/)
    .filter(Boolean);

  const papers = state.catalog.papers.filter((paper) => {
    const primaryMatches =
      !state.primary ||
      (state.primary === "__none__"
        ? !paper[primaryField]
        : paper[primaryField] === state.primary);
    return (
      primaryMatches &&
      (!state.year || paper.year === state.year) &&
      (!state.kind || paper.entry_kind === state.kind) &&
      (!state.status || paper.type === state.status) &&
      (!queryTerms.length ||
        queryTerms.every((term) => searchableText(paper).includes(term)))
    );
  });

  return papers.sort((left, right) => {
    if (state.sort === "title") {
      return left.title.localeCompare(right.title);
    }
    return (
      Number(right.year) - Number(left.year) ||
      left.venue_display_name.localeCompare(right.venue_display_name) ||
      left.title.localeCompare(right.title)
    );
  });
}

function paperTag(value) {
  return value ? createElement("span", "paper-tag", value) : null;
}

function externalLink(label, href, iconName = "") {
  const link = createElement("a");
  link.href = href;
  link.target = "_blank";
  link.rel = "noreferrer";
  if (iconName) {
    link.append(createIcon(iconName), createElement("span", "", label));
  } else {
    link.textContent = label;
  }
  return link;
}

function renderPaper(paper) {
  const item = createElement("li", "paper-item");
  item.style.setProperty("--paper-color", familyColor(paper));

  const body = createElement("div", "paper-body");
  const kicker = createElement("div", "paper-kicker");
  kicker.append(createElement("span", "", titleCase(paper.entry_kind)));
  if (paper.name && !["n/a", "na", "none"].includes(paper.name.toLowerCase())) {
    kicker.append(createElement("span", "system-name", paper.name));
  }
  body.append(kicker);

  const title = createElement("h3", "paper-title");
  title.append(externalLink(paper.title, paper.link));
  body.append(title);
  body.append(createElement("p", "paper-authors", paper.authors));

  const tags = createElement("div", "paper-tags");
  const tagValues =
    state.view === "artifact"
      ? [paper.artifact_family, paper.artifact_type, paper.application_domain]
      : [paper.application_domain, paper.artifact_family, paper.artifact_type];
  tagValues.forEach((value) => {
    const tag = paperTag(value);
    if (tag) tags.append(tag);
  });
  if (!tags.children.length) tags.append(paperTag("Unclassified"));
  body.append(tags);

  const meta = createElement("div", "paper-meta");
  meta.append(createElement("span", "paper-venue", paper.venue_display_name));
  meta.append(createElement("span", "paper-year", paper.year));
  meta.append(createElement("span", `status-pill ${paper.type}`, titleCase(paper.type)));
  const links = createElement("div", "paper-links");
  links.append(externalLink("Paper", paper.link, "ph-file-text"));
  if (paper.code) links.append(externalLink("Code", paper.code, "ph-code"));
  meta.append(links);

  item.append(body, meta);
  return item;
}

function activeFilterDefinitions() {
  const primaryLabel =
    state.primary === "__none__"
      ? state.view === "artifact"
        ? "No artifact label"
        : "No application label"
      : state.primary;
  return [
    { key: "search", label: state.search ? `Search: ${state.search}` : "" },
    { key: "primary", label: primaryLabel },
    { key: "year", label: state.year },
    { key: "kind", label: state.kind ? titleCase(state.kind) : "" },
    { key: "status", label: state.status ? titleCase(state.status) : "" },
  ].filter((filter) => filter.label);
}

function renderActiveFilters() {
  const fragment = document.createDocumentFragment();
  activeFilterDefinitions().forEach((filter) => {
    const button = createElement("button", "filter-chip");
    button.type = "button";
    button.setAttribute("aria-label", `Remove filter ${filter.label}`);
    button.append(createElement("span", "", filter.label));
    button.append(createElement("span", "", "×"));
    button.addEventListener("click", () => {
      state[filter.key] = "";
      syncControls();
      updateCatalog();
    });
    fragment.append(button);
  });
  elements.activeFilters.replaceChildren(fragment);
}

function syncControls() {
  elements.search.value = state.search;
  elements.primary.value = state.primary;
  elements.year.value = state.year;
  elements.kind.value = state.kind;
  elements.status.value = state.status;
  elements.sort.value = state.sort;
  elements.pageSize.value = String(state.pageSize);
  [
    elements.primary,
    elements.year,
    elements.kind,
    elements.status,
    elements.pageSize,
    elements.sort,
  ].forEach(refreshCustomSelect);
}

function updateUrl() {
  const params = new URLSearchParams();
  if (state.view !== "artifact") params.set("view", state.view);
  if (state.primary) params.set("filter", state.primary);
  if (state.year) params.set("year", state.year);
  if (state.kind) params.set("kind", state.kind);
  if (state.status) params.set("status", state.status);
  if (state.search) params.set("q", state.search);
  if (state.sort !== "recent") params.set("sort", state.sort);
  if (state.page > 1) params.set("page", String(state.page));
  if (state.pageSize !== DEFAULT_PAGE_SIZE) {
    params.set("perPage", String(state.pageSize));
  }
  const query = params.toString();
  history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}${location.hash}`);
}

function paginationItems(currentPage, totalPages) {
  if (totalPages <= 7) {
    return Array.from({ length: totalPages }, (_, index) => index + 1);
  }
  if (currentPage <= 4) return [1, 2, 3, 4, 5, "ellipsis", totalPages];
  if (currentPage >= totalPages - 3) {
    return [
      1,
      "ellipsis",
      totalPages - 4,
      totalPages - 3,
      totalPages - 2,
      totalPages - 1,
      totalPages,
    ];
  }
  return [
    1,
    "ellipsis-start",
    currentPage - 1,
    currentPage,
    currentPage + 1,
    "ellipsis-end",
    totalPages,
  ];
}

function scrollToCatalogResults() {
  const behavior = window.matchMedia("(prefers-reduced-motion: reduce)").matches
    ? "auto"
    : "smooth";
  elements.resultsPanel.scrollIntoView({ behavior, block: "start" });
}

function setCatalogPage(page) {
  state.page = page;
  updateCatalog({ resetPage: false });
  window.requestAnimationFrame(() => {
    elements.pagination
      .querySelector(`[data-page="${state.page}"]`)
      ?.focus({ preventScroll: true });
    scrollToCatalogResults();
  });
}

function renderPagination(totalPapers, firstVisible, lastVisible, totalPages) {
  elements.pagination.hidden = totalPages <= 1 || totalPapers === 0;
  if (elements.pagination.hidden) {
    elements.pagination.replaceChildren();
    return;
  }

  const summary = createElement(
    "p",
    "pagination-summary",
    `${formatNumber(firstVisible)}–${formatNumber(lastVisible)} of ${formatNumber(totalPapers)}`,
  );
  const controls = createElement("div", "pagination-controls");
  const previous = createElement("button", "pagination-direction");
  previous.type = "button";
  previous.append(createIcon("ph-arrow-left"), createElement("span", "", "Previous"));
  previous.disabled = state.page === 1;
  previous.addEventListener("click", () => setCatalogPage(state.page - 1));
  controls.append(previous);

  const pages = createElement("div", "pagination-pages");
  paginationItems(state.page, totalPages).forEach((item) => {
    if (typeof item !== "number") {
      const ellipsis = createElement("span", "pagination-ellipsis", "…");
      ellipsis.setAttribute("aria-hidden", "true");
      pages.append(ellipsis);
      return;
    }
    const page = createElement("button", "pagination-page", String(item));
    page.type = "button";
    page.dataset.page = String(item);
    page.setAttribute("aria-label", `Go to page ${item}`);
    if (item === state.page) {
      page.classList.add("is-current");
      page.setAttribute("aria-current", "page");
      page.setAttribute("aria-label", `Page ${item}, current page`);
    }
    page.addEventListener("click", () => setCatalogPage(item));
    pages.append(page);
  });
  controls.append(pages);

  const next = createElement("button", "pagination-direction");
  next.type = "button";
  next.append(createElement("span", "", "Next"), createIcon("ph-arrow-right"));
  next.disabled = state.page === totalPages;
  next.addEventListener("click", () => setCatalogPage(state.page + 1));
  controls.append(next);
  elements.pagination.replaceChildren(summary, controls);
}

function updateCatalog({ resetPage = true } = {}) {
  if (resetPage) state.page = 1;
  const papers = filteredPapers();
  const totalPages = Math.max(1, Math.ceil(papers.length / state.pageSize));
  state.page = Math.min(Math.max(1, state.page), totalPages);
  const start = (state.page - 1) * state.pageSize;
  const end = Math.min(start + state.pageSize, papers.length);
  const visible = papers.slice(start, end);
  const fragment = document.createDocumentFragment();
  visible.forEach((paper) => fragment.append(renderPaper(paper)));
  elements.paperList.replaceChildren(fragment);
  elements.resultCount.textContent = formatNumber(papers.length);
  elements.emptyState.hidden = papers.length > 0;
  renderPagination(papers.length, start + 1, end, totalPages);
  renderActiveFilters();
  updateUrl();
  elements.resultsPanel.setAttribute("aria-busy", "false");
}

function setCatalogView(view, primary = "") {
  state.view = view === "application" ? "application" : "artifact";
  state.primary = primary;
  renderFilterOptions();
  syncControls();
  updateCatalog();
}

function openCatalog(view, primary) {
  setCatalogView(view, primary);
  document.querySelector("#catalog").scrollIntoView({ behavior: "smooth" });
}

function clearFilters() {
  state.primary = "";
  state.year = "";
  state.kind = "";
  state.status = "";
  state.search = "";
  syncControls();
  updateCatalog();
}

function readUrlState() {
  const params = new URLSearchParams(location.search);
  state.view = params.get("view") === "application" ? "application" : "artifact";
  state.primary = params.get("filter") || "";
  state.year = params.get("year") || "";
  state.kind = params.get("kind") || "";
  state.status = params.get("status") || "";
  state.search = params.get("q") || "";
  state.sort = params.get("sort") === "title" ? "title" : "recent";
  const requestedPage = Number.parseInt(params.get("page") || "1", 10);
  const requestedPageSize = Number.parseInt(
    params.get("perPage") || String(DEFAULT_PAGE_SIZE),
    10,
  );
  state.page = Number.isFinite(requestedPage) && requestedPage > 0 ? requestedPage : 1;
  state.pageSize = PAGE_SIZE_OPTIONS.includes(requestedPageSize)
    ? requestedPageSize
    : DEFAULT_PAGE_SIZE;
}

function setupAxisTabs() {
  const tabs = [...document.querySelectorAll("[data-axis-tab]")];
  tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => activateAxisTab(tab.dataset.axisTab));
    tab.addEventListener("keydown", (event) => {
      if (!["ArrowLeft", "ArrowRight"].includes(event.key)) return;
      event.preventDefault();
      const direction = event.key === "ArrowRight" ? 1 : -1;
      const next = tabs[(index + direction + tabs.length) % tabs.length];
      activateAxisTab(next.dataset.axisTab);
      next.focus();
    });
  });
}

function activateAxisTab(axis) {
  document.querySelectorAll("[data-axis-tab]").forEach((tab) => {
    const selected = tab.dataset.axisTab === axis;
    tab.setAttribute("aria-selected", String(selected));
    tab.tabIndex = selected ? 0 : -1;
  });
  document.querySelector("#artifact-panel").hidden = axis !== "artifact";
  document.querySelector("#application-panel").hidden = axis !== "application";
}

function setupEvents() {
  elements.search.addEventListener("input", (event) => {
    state.search = event.target.value;
    updateCatalog();
  });
  elements.primary.addEventListener("change", (event) => {
    state.primary = event.target.value;
    updateCatalog();
  });
  elements.year.addEventListener("change", (event) => {
    state.year = event.target.value;
    updateCatalog();
  });
  elements.kind.addEventListener("change", (event) => {
    state.kind = event.target.value;
    updateCatalog();
  });
  elements.status.addEventListener("change", (event) => {
    state.status = event.target.value;
    updateCatalog();
  });
  elements.sort.addEventListener("change", (event) => {
    state.sort = event.target.value;
    updateCatalog();
  });
  elements.pageSize.addEventListener("change", (event) => {
    state.pageSize = Number.parseInt(event.target.value, 10);
    updateCatalog();
  });
  document.querySelectorAll('input[name="catalog-view"]').forEach((input) => {
    input.addEventListener("change", (event) => setCatalogView(event.target.value));
  });
  elements.clearFilters.addEventListener("click", clearFilters);
  document.querySelectorAll("[data-clear-filters]").forEach((button) => {
    button.addEventListener("click", clearFilters);
  });
  window.addEventListener("popstate", () => {
    readUrlState();
    renderFilterOptions();
    syncControls();
    updateCatalog({ resetPage: false });
  });
  document.querySelectorAll(".mobile-menu a").forEach((link) => {
    link.addEventListener("click", () => link.closest("details").removeAttribute("open"));
  });
}

function setupRevealMotion() {
  const revealElements = document.querySelectorAll(".reveal");
  if (
    window.matchMedia("(prefers-reduced-motion: reduce)").matches ||
    !("IntersectionObserver" in window)
  ) {
    revealElements.forEach((element) => element.classList.add("is-visible"));
    return;
  }
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.08, rootMargin: "0px 0px -40px" },
  );
  revealElements.forEach((element) => observer.observe(element));
}

function settleStalledCharts(message) {
  document.querySelectorAll(".chart-loading").forEach((loading) => {
    const error = document.createElement("p");
    error.className = "chart-error";
    error.textContent = message;
    loading.replaceWith(error);
  });
}

async function initialize() {
  setupRevealMotion();
  setupAxisTabs();
  window.setTimeout(
    () => settleStalledCharts("Chart loading timed out. Reload the page to try again."),
    10000,
  );
  try {
    const catalogUrl = document.body.dataset.catalogUrl || "data/catalog.json";
    const response = await fetch(catalogUrl);
    if (!response.ok) throw new Error(`Catalog request failed: ${response.status}`);
    state.catalog = await response.json();
    readUrlState();
    hydrateSummary();
    renderTaxonomyOverview();
    renderFilterOptions();
    renderYearOptions();
    setupCustomSelects();
    syncControls();
    setupEvents();
    updateCatalog({ resetPage: false });
  } catch (error) {
    console.error(error);
    settleStalledCharts(
      window.location.protocol === "file:"
        ? "Charts require the published site or a local web server."
        : "The chart data could not be loaded. Reload the page to try again.",
    );
    elements.resultsPanel.setAttribute("aria-busy", "false");
    elements.paperList.replaceChildren();
    elements.emptyState.hidden = false;
    elements.emptyState.querySelector("p").textContent =
      "The catalog could not be loaded. Please try again or use the repository README.";
  }
}

initialize();
