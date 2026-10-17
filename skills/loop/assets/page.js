/* unknowns page base — inlined by scripts/render-page.py. Assembles the reply from [data-reply] controls. */
(() => {
  function init() {
    const box = document.getElementById("reply");
    const panel = box && box.closest(".reply");
    const fallback = box ? box.value : "";
    const all = (sel) => Array.from(document.querySelectorAll(sel));
    const quizzes = () => all(".choices[data-answer]");
    const outside = (el) => !panel || !panel.contains(el);
    // A value joins the reply only once it differs from what the page opened with.
    const initial = new Map(all("input[data-reply],textarea[data-reply],select[data-reply]").map((el) => [el, el.value]));

    function lines() {
      const out = [];
      for (const el of all("[data-reply]")) {
        if (!outside(el)) continue;
        const label = el.dataset.reply;
        if (el.matches("input[type=checkbox],input[type=radio]")) {
          if (el.checked) out.push(label);
        } else if (el.matches("button")) {
          if (el.getAttribute("aria-pressed") !== "true") continue;
          const group = el.closest(".choices[data-answer]");
          out.push(group ? label + (el.classList.contains("correct") ? " ✓" : " ✗") : label);
        } else if (el.matches("input,textarea,select")) {
          const v = el.value.trim();
          const before = initial.has(el) ? initial.get(el) : el.defaultValue;
          if (v && el.value !== before) out.push(label ? label + ": " + v : v);
        }
      }
      return out;
    }

    function score() {
      const qs = quizzes();
      if (!qs.length) return null;
      const right = qs.filter((g) => g.querySelector("button.correct[aria-pressed=true]")).length;
      const text = right + "/" + qs.length;
      all("[data-score]").forEach((el) => { el.textContent = text; });
      return qs.some((g) => g.classList.contains("done")) ? text : null;
    }

    function update() {
      const picked = lines();
      const s = score();
      if (s) picked.push((panel && panel.dataset.scoreLabel || "Score") + ": " + s);
      if (!box) return;
      if (!picked.length) { box.value = fallback; return; }
      const head = panel && panel.dataset.head, foot = panel && panel.dataset.foot;
      box.value = [head, ...picked, foot].filter(Boolean).join("\n");
    }

    function choose(btn) {
      const group = btn.closest(".choices");
      if (!group || btn.disabled) return;
      const buttons = Array.from(group.querySelectorAll("button"));
      if (group.dataset.answer !== undefined) {
        const correct = (btn.dataset.value || btn.textContent.trim()) === group.dataset.answer;
        btn.setAttribute("aria-pressed", "true");
        btn.classList.add(correct ? "correct" : "wrong");
        buttons.forEach((b) => {
          if ((b.dataset.value || b.textContent.trim()) === group.dataset.answer) b.classList.add("correct");
          b.disabled = true;
        });
        group.classList.add("done");
        (group.closest(".card") || group.parentElement).classList.add("answered");
        if (!correct && group.dataset.goto) {
          const target = document.querySelector(group.dataset.goto);
          if (target) target.scrollIntoView({ block: "start" });
        }
      } else if (group.hasAttribute("data-multi")) {
        btn.setAttribute("aria-pressed", btn.getAttribute("aria-pressed") === "true" ? "false" : "true");
      } else {
        const on = btn.getAttribute("aria-pressed") !== "true";
        buttons.forEach((b) => b.setAttribute("aria-pressed", "false"));
        btn.setAttribute("aria-pressed", on ? "true" : "false");
      }
    }

    all(".choices button").forEach((b) => { if (!b.hasAttribute("aria-pressed")) b.setAttribute("aria-pressed", "false"); });
    document.addEventListener("click", (e) => {
      const btn = e.target.closest(".choices button");
      if (btn) { choose(btn); update(); }
    });
    document.addEventListener("change", (e) => { if (outside(e.target)) update(); });
    document.addEventListener("input", (e) => { if (outside(e.target) && e.target.matches("[data-reply]")) update(); });

    const copy = document.getElementById("copy-reply");
    if (copy && box) {
      const label = copy.textContent;
      let timer;
      copy.addEventListener("click", async () => {
        let ok = true;
        try { await navigator.clipboard.writeText(box.value); }
        catch { box.select(); ok = document.execCommand("copy"); }
        if (!ok) { box.select(); return; }  // left selected for a manual copy
        copy.textContent = copy.dataset.copied || "Copied";
        clearTimeout(timer);
        timer = setTimeout(() => { copy.textContent = label; }, 1500);
      });
    }

    window.unknownsReply = update;
  }

  // Run at once when the content is already parsed (the rendered page puts this script last), so
  // window.unknownsReply exists for the page's own DOMContentLoaded handlers; wait only when placed early.
  if (document.getElementById("reply") || document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
