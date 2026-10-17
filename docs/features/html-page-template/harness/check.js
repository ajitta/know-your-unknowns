// Usage: node check.js file1.html ... -> JSON lines of page checks
const { chromium } = require('playwright-core');
const fs = require('fs');
const base = process.env.HOME + '/.cache/ms-playwright/chromium_headless_shell-1243';
const exe = fs.readdirSync(base).find(d => d.startsWith('chrome-'));
(async () => {
  const b = await chromium.launch({ executablePath: `${base}/${exe}/chrome-headless-shell` });
  for (const f of process.argv.slice(2)) {
    const src = fs.readFileSync(f, 'utf8');
    const r = { file: f, bytes: Buffer.byteLength(src) };
    r.dark = /prefers-color-scheme:\s*dark/.test(src);
    r.focus = /:focus-visible/.test(src);
    r.motion = /prefers-reduced-motion/.test(src);
    r.lang = /<(html|main)[^>]*\blang=/.test(src);
    r.dataReply = (src.match(/\bdata-reply\s*=/g) || []).length;
    r.remote = (src.match(/\b(?:src|poster)\s*=\s*["']?(?:https?:)?\/\/(?!fonts\.g)/gi) || []).length;
    const p = await b.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message.slice(0, 120)));
    await p.goto('file://' + require('path').resolve(f)); await p.waitForTimeout(300);
    const box = async () => p.evaluate(() => { const t = document.querySelector('#reply') || [...document.querySelectorAll('textarea')].pop(); return t ? t.value : null; });
    const before = await box();
    r.replyBox = before !== null; r.defaultReply = !!(before && before.trim().length > 10);
    // react: try up to 5 visible reply controls (data-reply first, then any checkbox/button chip)
    let acted = false;
    const cands = [...await p.$$('input[type=checkbox][data-reply], input[type=radio][data-reply], button[data-reply]'),
                   ...await p.$$('input[type=checkbox], input[type=radio], .choices button, button[aria-pressed], [role=group] button')];
    let tries = 0;
    for (const el of cands) {
      if (tries >= 5) break;
      if (!(await el.isVisible())) continue;
      tries++; acted = true;
      await el.click().catch(() => {});
      await p.waitForTimeout(150);
      if ((await box()) !== before) break;
    }
    await p.waitForTimeout(200);
    const after = await box();
    r.reacts = acted && after !== null && after !== before;
    r.copyButton = await p.evaluate(() => [...document.querySelectorAll('button')].some(x => /copy|복사/i.test(x.textContent + x.id)));
    r.jsErrors = errs;
    await p.close();
    console.log(JSON.stringify(r));
  }
  await b.close();
})();
