# -*- coding: utf-8 -*-
"""实地验证：labuladong 一个章节页面的多语言 tab 结构"""
import json
from playwright.sync_api import sync_playwright

URL = "https://labuladong.online/zh/algo/data-structure-basic/array-basic/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        locale='zh-CN',
    )
    page = ctx.new_page()
    page.goto(URL, timeout=30000, wait_until='domcontentloaded')
    page.wait_for_load_state('networkidle', timeout=15000)
    page.wait_for_timeout(1500)

    # 1. 查看所有 tab 标签（可能 class="tab" / role="tab" / 包含 C++/Go 字样的 button/li）
    info = page.evaluate("""() => {
        const tabs = document.querySelectorAll('[role="tab"], .tab, .code-tab, [class*="tab"], [class*="Tab"]');
        const tabTexts = Array.from(tabs).map(t => (t.innerText||'').trim()).filter(t => t && t.length < 20);
        // 找所有 pre/code 块的数量
        const codes = document.querySelectorAll('pre');
        const codeCount = codes.length;
        // 找所有按钮文字
        const buttons = document.querySelectorAll('button, [role="button"]');
        const btnTexts = Array.from(buttons).map(b => (b.innerText||'').trim()).filter(t => t && t.length < 20);
        return {tabCount: tabs.length, tabTexts, codeCount, btnCount: buttons.length, btnTexts: btnTexts.slice(0,50)};
    }""")
    print("TABS INFO:")
    print(json.dumps(info, ensure_ascii=False, indent=2))

    # 2. 试着点击 "C++" tab
    print("\n--- 尝试点击 C++ tab ---")
    clicked = page.evaluate("""() => {
        const candidates = Array.from(document.querySelectorAll('button, [role="tab"], .tab, [class*="tab"], [class*="Tab"]'));
        for (const el of candidates) {
            const t = (el.innerText||'').trim();
            if (t === 'C++' || t === 'cpp' || t === 'C/C++') {
                el.click();
                return {found: true, text: t, tag: el.tagName, className: el.className};
            }
        }
        return {found: false};
    }""")
    print("CLICK RESULT:", clicked)
    if clicked.get('found'):
        page.wait_for_timeout(800)
        # 抓切换后的所有 pre 块
        codes = page.evaluate("""() => {
            return Array.from(document.querySelectorAll('pre')).map((p, i) => ({
                idx: i,
                lang: p.className,
                text: p.innerText
            }));
        }""")
        print(f"\n所有 pre 块数量: {len(codes)}")
        for c in codes[:8]:
            print(f"--- pre #{c['idx']} class={c['lang']!r} ---")
            print(c['text'][:300])
            print()

    browser.close()