# WenBiao Chinese tender classification dataset

[简体中文](README.md) · [繁體中文](README.zh-Hant.md) · **English** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md)

Downloadable JSON/CSV copy of the WenBiao tender **classification ledger**. Every row has a public `source_url` you can open: a statute page or a China Government Procurement Network article.

**Canonical site: [https://aiwenbiao.cn/data](https://aiwenbiao.cn/data)**  
Product home: [https://aiwenbiao.cn](https://aiwenbiao.cn)

This is not an evaluation committee, not a statistics office, and not a win-rate ranking. **No public URL means no row.** Drafts need human review; winning a bid is not guaranteed. Cite the original statute or notice, not only this repo or the site.

## Official website pages

| Page | URL |
| --- | --- |
| WenBiao home | https://aiwenbiao.cn |
| Data lab hub (canonical) | https://aiwenbiao.cn/data |
| How rows are included | https://aiwenbiao.cn/data/methodology |
| Line-by-line sources | https://aiwenbiao.cn/data/citations |
| Tender score-item taxonomy | https://aiwenbiao.cn/data/tender-score |
| Rejection / invalid-bid / veto classes | https://aiwenbiao.cn/data/bid-rejection |
| Common tender-document parts | https://aiwenbiao.cn/data/tender-document |
| Technical-bid chapter skeleton | https://aiwenbiao.cn/data/technical-bid |
| Goods / services / works contrast | https://aiwenbiao.cn/data/industry |
| Usual types of scoring methods | https://aiwenbiao.cn/data/score-method |
| Goods vs services scoring | https://aiwenbiao.cn/data/goods-vs-service |
| Launch note (thin stub) | https://aiwenbiao.cn/news/tender-data-lab-sep-10-2026 |
| Third-party publications index (not row citations) | https://aiwenbiao.cn/sources |
| Upload-not-used-for-training policy (not this dataset) | https://aiwenbiao.cn/data-usage |

`/sources` lists WenBiao posts on CSDN and similar sites. Row-level citations live at [`/data/citations`](https://aiwenbiao.cn/data/citations).  
[`/data-usage`](https://aiwenbiao.cn/data-usage) is the upload/training policy, **not** this dataset.

## What is inside

v1 (updated 2026-09-10) has about **68 rows**, not a 1,000-document sample:

| Family | `kind` | Rows | Official page |
| --- | --- | --- | --- |
| Score-item classes | `score_category` | 22 | https://aiwenbiao.cn/data/tender-score |
| Rejection / invalid / veto | `rejection_rule` | 13 | https://aiwenbiao.cn/data/bid-rejection |
| Tender-document parts | `doc_part` | 16 | https://aiwenbiao.cn/data/tender-document |
| Technical-bid chapters | `chapter` | 7 | https://aiwenbiao.cn/data/technical-bid |
| Method / industry rows | `notice_score_row` | 10 | https://aiwenbiao.cn/data/score-method |

Required field: **`source_url`**. Empty cells mean no public source yet.

## Inclusion rules

See [`METHODOLOGY.md`](METHODOLOGY.md) and [https://aiwenbiao.cn/data/methodology](https://aiwenbiao.cn/data/methodology). Source list: [`SOURCES.md`](SOURCES.md).

Prompt/harness repo (not this dataset): [https://github.com/hanbon-labs/wenbiao](https://github.com/hanbon-labs/wenbiao)

## License

Compilation: MIT. Statute and notice copyright stays with the publishers. Pointers and short quotes only. See [LICENSE](LICENSE).
