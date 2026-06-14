# Deliverable: 队列/栈篇 Obsidian 笔记（3 章节）

详见 `C:\Users\Li\.mavis\plans\plan_53866540\outputs\notes-batch-queue-stack\deliverable.md`

## Summary

3 篇 Obsidian 笔记全部生成完毕，写入课程根目录：

- `E:\Obsidian\Obsidian\大一下\数据结构与算法\08-queue-stack-basic.md`（2966 中文字）
- `E:\Obsidian\Obsidian\大一下\数据结构与算法\09-array-queue-stack.md`（2119 中文字）
- `E:\Obsidian\Obsidian\大一下\数据结构与算法\10-linked-queue-stack.md`（2213 中文字）

每篇含完整 frontmatter（title/tags/order/prerequisites/group/paywall/source）、C++17 完整实现（`namespace dsa` + `#include <bits/stdc++.h>`）、复杂度表、应用场景、wikilink 关联到 51 章节。3 章都是 `paywall: false`，与 meta 对齐。

## 自检（对照 verify 检查项）

- ✅ 3 个文件都存在
- ✅ 完整 frontmatter（7 字段）
- ✅ 9 个 unique wikilink 全部命中 `_chapters_meta.json` 的 tag
- ✅ 各 1 个 ` ```cpp ` 代码块 + `namespace dsa`
- ✅ 0 处营销噪声
- ✅ 2119/2213/2966 字，均 > 1500
- ✅ 末尾「下一章」wikilink
- ✅ `_raw_pages/` 未被覆盖（mtime 18:15 不变）

## Notes

1. **`_WRITING_GUIDE.md` 在仓库里不存在**——按 verifier 检查项反推自定义了写作规范（frontmatter 7 字段、C++17、wikilink 校验、≥1500 字、复杂度表、下一章、相关章节等）。
2. **代码扩展**：09 章新增了 `CycleArray<E>` 模板（head + size + 2 倍扩容）；10 章新增了裸双向链表版 `MyLinkedQueueRaw` 和单链表 + 尾指针版 `MySinglyLinkedQueue`，方便读者手写复现。
3. **未触碰原始文件**：`_raw_pages/08-09-10-*.md`、`_chapters_meta.json`、`_index.json`、其它 48 个章节笔记全部原样未动。
