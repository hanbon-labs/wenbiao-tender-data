# -*- coding: utf-8 -*-
"""Render detailed multilingual READMEs. Run from repo root."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LANGS = [
    ("zh", "README.md", "\u7b80\u4f53\u4e2d\u6587"),
    ("zh-Hant", "README.zh-Hant.md", "\u7e41\u9ad4\u4e2d\u6587"),
    ("en", "README.en.md", "English"),
    ("ja", "README.ja.md", "\u65e5\u672c\u8a9e"),
    ("ko", "README.ko.md", "\ud55c\uad6d\uc5b4"),
    ("es", "README.es.md", "Espa\u00f1ol"),
    ("fr", "README.fr.md", "Fran\u00e7ais"),
    ("de", "README.de.md", "Deutsch"),
    ("pt", "README.pt.md", "Portugu\u00eas"),
    ("ru", "README.ru.md", "\u0420\u0443\u0441\u0441\u043a\u0438\u0439"),
    ("ar", "README.ar.md", "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"),
    ("vi", "README.vi.md", "Ti\u1ebfng Vi\u1ec7t"),
    ("id", "README.id.md", "Bahasa Indonesia"),
    ("th", "README.th.md", "\u0e44\u0e17\u0e22"),
    ("it", "README.it.md", "Italiano"),
    ("hi", "README.hi.md", "\u0939\u093f\u0928\u094d\u0926\u0940"),
]

SITE = {
    "home": "https://aiwenbiao.cn",
    "data": "https://aiwenbiao.cn/data",
    "methodology": "https://aiwenbiao.cn/data/methodology",
    "citations": "https://aiwenbiao.cn/data/citations",
    "tender_score": "https://aiwenbiao.cn/data/tender-score",
    "bid_rejection": "https://aiwenbiao.cn/data/bid-rejection",
    "tender_document": "https://aiwenbiao.cn/data/tender-document",
    "technical_bid": "https://aiwenbiao.cn/data/technical-bid",
    "industry": "https://aiwenbiao.cn/data/industry",
    "score_method": "https://aiwenbiao.cn/data/score-method",
    "goods": "https://aiwenbiao.cn/data/goods-vs-service",
    "sources": "https://aiwenbiao.cn/sources",
    "usage": "https://aiwenbiao.cn/data-usage",
    "news": "https://aiwenbiao.cn/news/tender-data-lab-sep-10-2026",
    "prompts": "https://github.com/hanbon-labs/wenbiao",
    "repo": "https://github.com/hanbon-labs/wenbiao-tender-data",
}


def lang_bar(current: str) -> str:
    parts = []
    for code, fn, label in LANGS:
        if code == current:
            parts.append(f"**{label}**")
        else:
            parts.append(f"[{label}]({fn})")
    return " \u00b7 ".join(parts)


def dump(name: str, text: str) -> None:
    path = ROOT / name
    path.write_bytes(text.encode("utf-8"))
    raw = path.read_bytes()
    if path.suffix == ".md" and "README" in name:
        assert b"aiwenbiao.cn/data" in raw


def official_table(headers: tuple[str, str], rows: list[tuple[str, str]]) -> str:
    h1, h2 = headers
    lines = [f"| {h1} | {h2} |", "| --- | --- |"]
    for label, url in rows:
        lines.append(f"| {label} | {url} |")
    return "\n".join(lines)


def pages(labels: dict[str, str]) -> list[tuple[str, str]]:
    return [
        (labels["home"], SITE["home"]),
        (labels["data"], SITE["data"]),
        (labels["methodology"], SITE["methodology"]),
        (labels["citations"], SITE["citations"]),
        (labels["tender_score"], SITE["tender_score"]),
        (labels["bid_rejection"], SITE["bid_rejection"]),
        (labels["tender_document"], SITE["tender_document"]),
        (labels["technical_bid"], SITE["technical_bid"]),
        (labels["industry"], SITE["industry"]),
        (labels["score_method"], SITE["score_method"]),
        (labels["goods"], SITE["goods"]),
        (labels["news"], SITE["news"]),
        (labels["sources"], SITE["sources"]),
        (labels["usage"], SITE["usage"]),
    ]


def main() -> None:
    # --- Simplified Chinese (canonical README) ---
    zh_pages = {
        "home": "\u6587\u6807\u9996\u9875",
        "data": "\u6570\u636e\u5b9e\u9a8c\u5ba4\u67a2\u7ebd\uff08\u89c4\u8303\u7ad9\uff09",
        "methodology": "\u6536\u5f55\u65b9\u6cd5",
        "citations": "\u9010\u884c\u51fa\u5904",
        "tender_score": "\u62db\u6807\u8bc4\u5206\u9879\u5206\u7c7b",
        "bid_rejection": "\u5e9f\u6807 / \u65e0\u6548 / \u5426\u51b3\u5206\u7c7b",
        "tender_document": "\u62db\u6807\u6587\u4ef6\u5e38\u89c1\u7ed3\u6784",
        "technical_bid": "\u6280\u672f\u6807\u7ae0\u8282\u9aa8\u67b6",
        "industry": "\u8d27\u7269 / \u670d\u52a1 / \u5de5\u7a0b\u5bf9\u7167",
        "score_method": "\u8bc4\u5206\u529e\u6cd5\u901a\u5e38\u6709\u54ea\u51e0\u7c7b",
        "goods": "\u8d27\u7269\u7c7b\u4e0e\u670d\u52a1\u7c7b\u5dee\u5728\u54ea",
        "news": "\u4e0a\u7ebf\u52a8\u6001\uff08\u8584\u51fa\u5904\uff09",
        "sources": "\u4e09\u65b9\u53d1\u6587\u7d22\u5f15\uff08\u4e0d\u662f\u6570\u636e\u884c\u51fa\u5904\uff09",
        "usage": "\u6570\u636e\u4f7f\u7528\u534f\u8bae\uff08\u4e0a\u4f20\u4e0d\u7528\u4e8e\u8bad\u7ec3\uff0c\u4e0d\u662f\u6570\u636e\u96c6\uff09",
    }
    dump(
        "README.md",
        f"""# \u6587\u6807\u62db\u6295\u6807\u5206\u7c7b\u6570\u636e\u96c6

{lang_bar("zh")}

\u8fd9\u662f\u6587\u6807\u62db\u6295\u6807\u6570\u636e\u5b9e\u9a8c\u5ba4\u7684**\u53ef\u4e0b\u8f7d\u526f\u672c**\uff08JSON / CSV\uff09\u3002\u6bcf\u4e00\u884c\u90fd\u6709\u53ef\u6253\u5f00\u6838\u5bf9\u7684\u516c\u5f00 `source_url`\uff1a\u6cd5\u89c4\u539f\u6587\u6216\u4e2d\u56fd\u653f\u5e9c\u91c7\u8d2d\u7f51\u5df2\u516c\u5f00\u7684\u7406\u8bba\u5b9e\u52a1\u6587\u3002

**\u89c4\u8303\u7ad9\uff08\u8bf7\u4ee5\u7ad9\u5185\u8868\u4e3a\u51c6\uff09\uff1a[{SITE["data"]}]({SITE["data"]})**  
\u5b98\u7f51\u9996\u9875\uff1a[{SITE["home"]}]({SITE["home"]})

\u7b80\u7b54\uff1a\u8fd9\u4e0d\u662f\u8bc4\u6807\u59d4\u5458\u4f1a\u3001\u4e0d\u662f\u7edf\u8ba1\u5c40\u3001\u4e0d\u662f\u4e2d\u6807\u7387\u6392\u884c\u3002\u6ca1\u6709\u516c\u5f00 URL \u5c31\u6ca1\u6709\u8fd9\u4e00\u884c\u3002**\u987b\u4eba\u5de5\u5ba1\u6838\uff0c\u4e0d\u4fdd\u8bc1\u4e2d\u6807\u3002**\u8bf7\u5f15\u7528\u539f\u59cb\u6cd5\u6761\u6216\u516c\u544a\uff0c\u4e0d\u8981\u53ea\u5f15\u672c\u4ed3\u6216\u672c\u7ad9\u3002

## \u5b98\u7f51\u94fe\u63a5\uff08\u5fc5\u770b\uff09

{official_table(("\u9875\u9762", "URL"), pages(zh_pages))}

`/sources` \u662f\u6587\u6807\u5728 CSDN / \u767e\u5bb6\u53f7\u7b49\u5e73\u53f0\u7684**\u53d1\u8868\u7d22\u5f15**\uff1b\u6570\u636e\u884c\u51fa\u5904\u5728 [`/data/citations`]({SITE["citations"]})\u3002  
[`/data-usage`]({SITE["usage"]}) \u662f\u300c\u4e0a\u4f20\u8d44\u6599\u4e0d\u7528\u4e8e\u8bad\u7ec3\u300d\uff0c**\u4e0d\u662f**\u672c\u6570\u636e\u96c6\u3002

## \u8fd9\u4e2a\u4ed3\u88c5\u4e86\u4ec0\u4e48

v1\uff08{SITE["repo"]} \u66f4\u65b0 2026-09-10\uff09\u7ea6 **68 \u884c**\uff0c\u4e0d\u662f 1000 \u4efd\u6837\u672c\uff1a

| \u65cf | `kind` | \u7ea6\u884c\u6570 | \u5bf9\u5e94\u5b98\u7f51 |
| --- | --- | --- | --- |
| \u8bc4\u5206\u9879\u5206\u7c7b | `score_category` | 22 | {SITE["tender_score"]} |
| \u5e9f\u6807 / \u65e0\u6548 / \u5426\u51b3 | `rejection_rule` | 13 | {SITE["bid_rejection"]} |
| \u62db\u6807\u6587\u4ef6\u7ed3\u6784 | `doc_part` | 16 | {SITE["tender_document"]} |
| \u6280\u672f\u6807\u7ae0\u8282 | `chapter` | 7 | {SITE["technical_bid"]} |
| \u8bc4\u5206\u529e\u6cd5 / \u884c\u4e1a\u5bf9\u7167\u884c | `notice_score_row` | 10 | {SITE["score_method"]} \u00b7 {SITE["goods"]} \u00b7 {SITE["industry"]} |

\u6bcf\u884c\u5b57\u6bb5\u8981\u70b9\uff1a`id`\u3001`kind`\u3001`tender_type`\uff08\u8d27\u7269/\u670d\u52a1/\u5de5\u7a0b/\u4fe1\u606f\u5316/\u6cd5\u89c4\u901a\u5219\uff09\u3001`category`\u3001`title`\u3001`requirement`\u3001`source_quote`\u3001**`source_url`\uff08\u5fc5\u586b\uff09**\u3001`source_note`\u3001`source_publisher`\u3001`anonymization`\uff08`statute` / `public-notice`\uff09\u3001`incomparability_note`\u3001`year`\u3001`region`\u3001`updated_at`\u3002

## \u6536\u5f55\u5408\u540c

1. **\u6ca1\u6709\u516c\u5f00 URL\uff0c\u5c31\u6ca1\u6709\u8fd9\u4e00\u884c\u3002** \u4f18\u5148\u6cd5\u89c4\u539f\u6587\uff1b\u4e2a\u522b\u9879\u76ee\u62db\u6807\u516c\u544a\u672a\u9010\u6761\u6838\u9a8c\u524d\u4e0d\u4e0a\u884c\u3002
2. **\u4e0d\u53ef\u6bd4\u5c31\u5206\u884c\u3002** \u8d27\u7269/\u670d\u52a1/\u5de5\u7a0b\u3001\u8d44\u683c\u4e0e\u8bc4\u5ba1\u56e0\u7d20\u3001\u5e9f\u6807\u4e0e\u6295\u6807\u65e0\u6548\u4e0d\u5408\u6210\u300c\u5168\u56fd\u6700\u5e38\u89c1\u300d\u6216\u51fa\u73b0\u7387\u3002
3. **\u7a7a\u5355\u5143\u683c = \u5c1a\u672a\u627e\u5230\u516c\u5f00\u51fa\u5904**\uff0c\u4e0d\u7f16\u9020\u586b\u8868\u3002
4. **\u4e0d\u8f6c\u8f7d\u62db\u6807\u6587\u4ef6\u5168\u6587 PDF**\uff0c\u4e0d\u6536\u7528\u6237\u4e0a\u4f20\u6807\u4e66\u3002
5. \u7ad9\u70b9\u662f\u67e5\u9605\u9875\uff1b\u672c\u4ed3\u662f\u673a\u5668\u53ef\u8bfb\u526f\u672c\u3002\u8be6\u89c1 [`METHODOLOGY.md`](METHODOLOGY.md) \u4e0e [{SITE["methodology"]}]({SITE["methodology"]})\u3002

\u51fa\u5904\u6e05\u5355\uff1a[`SOURCES.md`](SOURCES.md) \u00b7 [{SITE["citations"]}]({SITE["citations"]})

## \u6587\u4ef6

- `ledger.json` / `csv/ledger.csv` \u2014 \u5168\u90e8\u53ef\u5c55\u793a\u884c
- `taxonomy-score-categories.json` \u2014 \u8bc4\u5206\u9879\u5206\u7c7b
- `taxonomy-rejection-rules.json` \u2014 \u5e9f\u6807/\u65e0\u6548/\u5426\u51b3
- `taxonomy-document-parts.json` \u2014 \u6587\u4ef6\u7ed3\u6784
- `taxonomy-tech-chapters.json` \u2014 \u6280\u672f\u6807\u7ae0\u8282
- `score-method-rows.json` \u2014 \u95ee\u53e5\u9875\u5b50\u96c6
- `notices.json` / `meta.json` \u2014 \u51fa\u5904\u5143\u6570\u636e\u4e0e\u6536\u5f55\u53e3\u5f84

## \u5982\u4f55\u5f15\u7528

1. \u5148\u5f00\u5b98\u7f51\u5bf9\u5e94\u8868\uff08\u4f8b\u5982 [{SITE["tender_score"]}]({SITE["tender_score"]})\uff09\u3002
2. \u70b9\u8868\u4e2d\u300c\u51fa\u5904\u300d\u6838\u5bf9\u539f\u6587\u3002
3. \u5f15\u7528\u65f6\u540c\u65f6\u7ed9\u51fa\uff1a\u7ad9\u5185 URL + \u672c\u4ed3\u6587\u4ef6 + \u539f\u59cb `source_url`\u3002
4. Prompt / harness \u5de5\u4f5c\u6d41\u4ecd\u5728 [{SITE["prompts"]}]({SITE["prompts"]})\uff0c**\u4e0d\u662f**\u672c\u6570\u636e\u96c6\u3002

## License

\u6c47\u7f16\u8868 MIT\u3002\u6cd5\u6761\u4e0e\u516c\u544a\u7248\u6743\u4ecd\u5c5e\u53d1\u5e03\u673a\u5173\uff1b\u6570\u636e\u96c6\u53ea\u5b58\u7ed3\u6784\u5b57\u6bb5\u548c\u6307\u9488\u3002\u89c1 [LICENSE](LICENSE)\u3001[CONTRIBUTING.md](CONTRIBUTING.md)\u3002
""",
    )

    # --- English ---
    en_pages = {
        "home": "WenBiao home",
        "data": "Data lab hub (canonical)",
        "methodology": "How rows are included",
        "citations": "Line-by-line sources",
        "tender_score": "Tender score-item taxonomy",
        "bid_rejection": "Rejection / invalid-bid / veto classes",
        "tender_document": "Common tender-document parts",
        "technical_bid": "Technical-bid chapter skeleton",
        "industry": "Goods / services / works contrast",
        "score_method": "Usual types of scoring methods",
        "goods": "Goods vs services scoring",
        "news": "Launch note (thin stub)",
        "sources": "Third-party publications index (not row citations)",
        "usage": "Upload-not-used-for-training policy (not this dataset)",
    }
    dump(
        "README.en.md",
        f"""# WenBiao Chinese tender classification dataset

{lang_bar("en")}

Downloadable JSON/CSV copy of the WenBiao tender **classification ledger**. Every row has a public `source_url` you can open: a statute page or a China Government Procurement Network article.

**Canonical site: [{SITE["data"]}]({SITE["data"]})**  
Product home: [{SITE["home"]}]({SITE["home"]})

This is not an evaluation committee, not a statistics office, and not a win-rate ranking. **No public URL means no row.** Drafts need human review; winning a bid is not guaranteed. Cite the original statute or notice, not only this repo or the site.

## Official website pages

{official_table(("Page", "URL"), pages(en_pages))}

`/sources` lists WenBiao posts on CSDN and similar sites. Row-level citations live at [`/data/citations`]({SITE["citations"]}).  
[`/data-usage`]({SITE["usage"]}) is the upload/training policy, **not** this dataset.

## What is inside

v1 (updated 2026-09-10) has about **68 rows**, not a 1,000-document sample:

| Family | `kind` | Rows | Official page |
| --- | --- | --- | --- |
| Score-item classes | `score_category` | 22 | {SITE["tender_score"]} |
| Rejection / invalid / veto | `rejection_rule` | 13 | {SITE["bid_rejection"]} |
| Tender-document parts | `doc_part` | 16 | {SITE["tender_document"]} |
| Technical-bid chapters | `chapter` | 7 | {SITE["technical_bid"]} |
| Method / industry rows | `notice_score_row` | 10 | {SITE["score_method"]} |

Required field: **`source_url`**. Empty cells mean no public source yet.

## Inclusion rules

See [`METHODOLOGY.md`](METHODOLOGY.md) and [{SITE["methodology"]}]({SITE["methodology"]}). Source list: [`SOURCES.md`](SOURCES.md).

Prompt/harness repo (not this dataset): [{SITE["prompts"]}]({SITE["prompts"]})

## License

Compilation: MIT. Statute and notice copyright stays with the publishers. Pointers and short quotes only. See [LICENSE](LICENSE).
""",
    )

    # Remaining languages share the same official URL table with localized labels.
    others = {
        "zh-Hant": (
            "README.zh-Hant.md",
            "\u6587\u6a19\u62db\u6295\u6a19\u5206\u985e\u6578\u64da\u96c6",
            "\u6b64\u70ba\u6587\u6a19\u62db\u6295\u6a19\u8cc7\u6599\u5be6\u9a57\u5ba4\u7684\u53ef\u4e0b\u8f09\u526f\u672c\u3002\u6bcf\u4e00\u5217\u90fd\u6709\u53ef\u6253\u958b\u6838\u5c0d\u7684\u516c\u958b `source_url`\u3002",
            "\u898f\u7bc4\u7ad9\uff08\u8acb\u4ee5\u7ad9\u5167\u8868\u70ba\u6e96\uff09",
            "\u5b98\u7db2\u9996\u9801",
            "\u9019\u4e0d\u662f\u8a55\u6a19\u59d4\u54e1\u6703\u3001\u4e0d\u662f\u7d71\u8a08\u5c40\u3001\u4e0d\u662f\u4e2d\u6a19\u7387\u6392\u884c\u3002\u6c92\u6709\u516c\u958b URL \u5c31\u6c92\u6709\u9019\u4e00\u884c\u3002\u9808\u4eba\u5de5\u5be9\u6838\uff0c\u4e0d\u4fdd\u8b49\u4e2d\u6a19\u3002",
            "\u5b98\u7db2\u93c8\u63a5",
            {
                "home": "\u6587\u6a19\u9996\u9801",
                "data": "\u8cc7\u6599\u5be6\u9a57\u5ba4\u6a1e\u7d10",
                "methodology": "\u6536\u9304\u65b9\u6cd5",
                "citations": "\u9010\u5217\u51fa\u8655",
                "tender_score": "\u62db\u6a19\u8a55\u5206\u9805\u5206\u985e",
                "bid_rejection": "\u5ee2\u6a19\uff0f\u7121\u6548\uff0f\u5426\u6c7a",
                "tender_document": "\u62db\u6a19\u6587\u4ef6\u7d50\u69cb",
                "technical_bid": "\u6280\u8853\u6a19\u7ae0\u7bc0",
                "industry": "\u8ca8\u7269\uff0f\u670d\u52d9\u5c0d\u7167",
                "score_method": "\u8a55\u5206\u8fa6\u6cd5\u985e\u578b",
                "goods": "\u8ca8\u7269\u8207\u670d\u52d9\u5dee\u7570",
                "news": "\u4e0a\u7dda\u52d5\u614b",
                "sources": "\u4e09\u65b9\u767c\u6587\u7d22\u5f15",
                "usage": "\u4e0a\u50b3\u8cc7\u6599\u4e0d\u7528\u65bc\u8a13\u7df4",
            },
            ("\u9801\u9762", "URL"),
            "\u532f\u7de8\u8868 MIT\u3002\u6cd5\u689d\u8207\u516c\u544a\u7248\u6b0a\u4ecd\u5c6c\u767c\u4f48\u65b9\u3002",
        ),
        "ja": (
            "README.ja.md",
            "WenBiao \u4e2d\u56fd\u5165\u672d\u5206\u985e\u30c7\u30fc\u30bf\u30bb\u30c3\u30c8",
            "\u516c\u958b\u306e `source_url` \u304c\u3042\u308b\u8a55\u70b9\u9805\u76ee\u30fb\u7121\u52b9\u5165\u672d\u30fb\u5165\u672d\u66f8\u985e\u306e\u53f0\u5e33\uff08JSON/CSV\uff09\u3067\u3059\u3002",
            "\u6b63\u898f\u30b5\u30a4\u30c8",
            "\u516c\u5f0f\u30db\u30fc\u30e0",
            "\u8a55\u4fa1\u59d4\u54e1\u4f1a\u3067\u3082\u7d71\u8a08\u5c40\u3067\u3082\u53d7\u6ce8\u7387\u30e9\u30f3\u30ad\u30f3\u30b0\u3067\u3082\u3042\u308a\u307e\u305b\u3093\u3002\u516c\u958bURL\u304c\u306a\u3051\u308c\u3070\u884c\u306f\u3042\u308a\u307e\u305b\u3093\u3002\u4eba\u624b\u78ba\u8a8d\u304c\u5fc5\u8981\u3067\u3001\u53d7\u6ce8\u306f\u4fdd\u8a3c\u3057\u307e\u305b\u3093\u3002",
            "\u516c\u5f0f\u30b5\u30a4\u30c8\u30ea\u30f3\u30af",
            {
                "home": "WenBiao \u30db\u30fc\u30e0",
                "data": "\u30c7\u30fc\u30bf\u5b9f\u9a13\u5ba4\uff08\u6b63\u898f\uff09",
                "methodology": "\u53ce\u9332\u65b9\u91dd",
                "citations": "\u884c\u3054\u3068\u306e\u5178\u62e0",
                "tender_score": "\u8a55\u70b9\u9805\u76ee\u306e\u5206\u985e",
                "bid_rejection": "\u7121\u52b9\u30fb\u5426\u6c7a\u306e\u5206\u985e",
                "tender_document": "\u5165\u672d\u66f8\u306e\u69cb\u6210",
                "technical_bid": "\u6280\u8853\u63d0\u6848\u306e\u7ae0",
                "industry": "\u7269\u8ca8\u30fb\u30b5\u30fc\u30d3\u30b9\u5bfe\u7167",
                "score_method": "\u63a1\u70b9\u65b9\u6cd5\u306e\u7a2e\u985e",
                "goods": "\u7269\u8ca8\u3068\u30b5\u30fc\u30d3\u30b9\u306e\u5dee",
                "news": "\u516c\u958b\u30ce\u30fc\u30c8",
                "sources": "\u793e\u5916\u767a\u4fe1\u4e00\u89a7",
                "usage": "\u30a2\u30c3\u30d7\u30ed\u30fc\u30c9\u3092\u5b66\u7fd2\u306b\u4f7f\u308f\u306a\u3044",
            },
            ("\u30da\u30fc\u30b8", "URL"),
            "\u7de8\u7e54\u8868\u306f MIT\u3002\u6cd5\u898f\u30fb\u516c\u544a\u306e\u8457\u4f5c\u6a29\u306f\u767a\u884c\u8005\u306b\u6b8b\u308a\u307e\u3059\u3002",
        ),
        "ko": (
            "README.ko.md",
            "WenBiao \uc911\uad6d \uc785\ucc30 \ubd84\ub958 \ub370\uc774\ud130\uc14b",
            "\uacf5\uac1c `source_url`\uc774 \uc788\ub294 \ud56d\ubaa9\u00b7\ubb34\ud6a8 \uc785\ucc30\u00b7\uc785\ucc30\uc11c \uad6c\uc131 \uc7a5\ubd80(JSON/CSV)\uc785\ub2c8\ub2e4.",
            "\uc815\uaddc \uc0ac\uc774\ud2b8",
            "\uacf5\uc2dd \ud648",
            "\ud3c9\uac00\uc704\uc6d0\ud68c\ub3c4, \ud1b5\uacc4\uccad\ub3c4, \ub099\ucc30\ub960 \uc21c\uc704\ub3c4 \uc544\ub2d9\ub2c8\ub2e4. \uacf5\uac1c URL\uc774 \uc5c6\uc73c\uba74 \ud589\uc774 \uc5c6\uc2b5\ub2c8\ub2e4. \uc778\uac80\uc218\uac00 \ud544\uc694\ud558\uba70 \ub099\ucc30\ub97c \ubcf4\uc99d\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.",
            "\uacf5\uc2dd \uc0ac\uc774\ud2b8 \ub9c1\ud06c",
            {
                "home": "WenBiao \ud648",
                "data": "\ub370\uc774\ud130 \uc2e4\ud5d8\uc2e4(\uc815\uaddc)",
                "methodology": "\uc218\ub85d \ubc29\ubc95",
                "citations": "\ud589\ubcc4 \ucd9c\ucc98",
                "tender_score": "\uc810\uc218 \ud56d\ubaa9 \ubd84\ub958",
                "bid_rejection": "\ubb34\ud6a8/\uae30\uac01 \ubd84\ub958",
                "tender_document": "\uc785\ucc30\uc11c \uad6c\uc131",
                "technical_bid": "\uae30\uc220\uc81c\uc548 \uc7a5",
                "industry": "\ubb3c\ud488/\uc11c\ube44\uc2a4 \ub300\uc870",
                "score_method": "\uc810\uc218 \ubc29\ubc95 \uc720\ud615",
                "goods": "\ubb3c\ud488 vs \uc11c\ube44\uc2a4",
                "news": "\uac8c\uc2dc \ub178\ud2b8",
                "sources": "\uc678\ubd80 \uac8c\uc2dc \ubaa9\ub85d",
                "usage": "\uc5c5\ub85c\ub4dc\ub294 \ud559\uc2b5\uc5d0 \uc4f0\uc9c0 \uc54a\uc74c",
            },
            ("\ud398\uc774\uc9c0", "URL"),
            "\ud3b8\ucc2c\ud45c\ub294 MIT. \ubc95\ub839\u00b7\uacf5\uace0 \uc800\uc791\uad8c\uc740 \ubc1c\ud589\uae30\uad00\uc5d0 \uc788\uc2b5\ub2c8\ub2e4.",
        ),
        "es": (
            "README.es.md",
            "Conjunto de clasificaci\u00f3n de licitaciones (WenBiao)",
            "Copia JSON/CSV de un libro mayor de clasificaci\u00f3n. Cada fila tiene un `source_url` p\u00fablico.",
            "Sitio can\u00f3nico",
            "Inicio oficial",
            "No es un comit\u00e9 de evaluaci\u00f3n, ni una oficina estad\u00edstica, ni un ranking de adjudicaci\u00f3n. Sin URL p\u00fablica no hay fila. Se exige revisi\u00f3n humana; no se garantiza ganar.",
            "Enlaces del sitio oficial",
            {
                "home": "Inicio WenBiao",
                "data": "Laboratorio de datos (can\u00f3nico)",
                "methodology": "C\u00f3mo se incluye una fila",
                "citations": "Fuentes l\u00ednea a l\u00ednea",
                "tender_score": "Taxonom\u00eda de criterios",
                "bid_rejection": "Rechazo / nulidad",
                "tender_document": "Partes del pliego",
                "technical_bid": "Cap\u00edtulos de la oferta t\u00e9cnica",
                "industry": "Bienes / servicios",
                "score_method": "Tipos de m\u00e9todo de puntuaci\u00f3n",
                "goods": "Bienes frente a servicios",
                "news": "Nota de lanzamiento",
                "sources": "\u00cdndice de publicaciones",
                "usage": "Los env\u00edos no se usan para entrenar",
            },
            ("P\u00e1gina", "URL"),
            "Compilaci\u00f3n MIT. El copyright de leyes y avisos sigue en el emisor.",
        ),
        "fr": (
            "README.fr.md",
            "Jeu de classification des appels d\u2019offres (WenBiao)",
            "Copie JSON/CSV d\u2019un registre de classification. Chaque ligne a un `source_url` public.",
            "Site canonique",
            "Accueil officiel",
            "Ce n\u2019est ni un comit\u00e9 d\u2019\u00e9valuation, ni un institut de statistique, ni un classement de taux de gain. Pas d\u2019URL publique = pas de ligne. Relecture humaine obligatoire ; aucun gain n\u2019est garanti.",
            "Liens du site officiel",
            {
                "home": "Accueil WenBiao",
                "data": "Laboratoire de donn\u00e9es (canonique)",
                "methodology": "R\u00e8gles d\u2019inclusion",
                "citations": "Sources ligne par ligne",
                "tender_score": "Taxonomie des crit\u00e8res",
                "bid_rejection": "Rejet / nullit\u00e9",
                "tender_document": "Pi\u00e8ces du dossier",
                "technical_bid": "Chapitres de l\u2019offre technique",
                "industry": "Fournitures / services",
                "score_method": "Types de m\u00e9thodes de notation",
                "goods": "Fournitures vs services",
                "news": "Note de mise en ligne",
                "sources": "Index des publications",
                "usage": "Les d\u00e9p\u00f4ts ne servent pas \u00e0 l\u2019entra\u00eenement",
            },
            ("Page", "URL"),
            "Compilation MIT. Le droit d\u2019auteur des textes officiels reste \u00e0 l\u2019\u00e9metteur.",
        ),
        "de": (
            "README.de.md",
            "WenBiao-Klassifikationsdatensatz f\u00fcr Ausschreibungen",
            "JSON/CSV-Kopie eines Klassifikationsledgers. Jede Zeile hat eine \u00f6ffentliche `source_url`.",
            "Kanonische Website",
            "Offizielle Startseite",
            "Kein Bewertungsausschuss, kein Statistikamt, keine Zuschlagsquote. Ohne \u00f6ffentliche URL gibt es keine Zeile. Menschliche Pr\u00fcfung ist Pflicht; Zuschlag wird nicht garantiert.",
            "Offizielle Website-Links",
            {
                "home": "WenBiao-Startseite",
                "data": "Datenlabor (kanonisch)",
                "methodology": "Aufnahmevertrag",
                "citations": "Quellen je Zeile",
                "tender_score": "Bewertungskriterien",
                "bid_rejection": "Ausschluss / Ung\u00fcltigkeit",
                "tender_document": "Bestandteile der Unterlage",
                "technical_bid": "Kapitel des technischen Angebots",
                "industry": "Lieferungen / Dienstleistungen",
                "score_method": "Arten von Bewertungsmethoden",
                "goods": "Lieferungen vs. Dienstleistungen",
                "news": "Ver\u00f6ffentlichungshinweis",
                "sources": "Publikationsindex",
                "usage": "Uploads werden nicht trainiert",
            },
            ("Seite", "URL"),
            "Zusammenstellung MIT. Urheberrecht an Gesetzen und Bekanntmachungen bleibt beim Herausgeber.",
        ),
        "pt": (
            "README.pt.md",
            "Conjunto de classifica\u00e7\u00e3o de licita\u00e7\u00f5es (WenBiao)",
            "C\u00f3pia JSON/CSV de um livro-raz\u00e3o de classifica\u00e7\u00e3o. Cada linha tem um `source_url` p\u00fablico.",
            "S\u00edtio can\u00f3nico",
            "In\u00edcio oficial",
            "N\u00e3o \u00e9 comiss\u00e3o de avalia\u00e7\u00e3o, instituto de estat\u00edstica nem ranking de adjudica\u00e7\u00e3o. Sem URL p\u00fablica n\u00e3o h\u00e1 linha. \u00c9 obrigat\u00f3ria revis\u00e3o humana; n\u00e3o se garante vencer.",
            "Liga\u00e7\u00f5es do s\u00edtio oficial",
            {
                "home": "In\u00edcio WenBiao",
                "data": "Laborat\u00f3rio de dados (can\u00f3nico)",
                "methodology": "Como se inclui uma linha",
                "citations": "Fontes linha a linha",
                "tender_score": "Taxonomia de crit\u00e9rios",
                "bid_rejection": "Rejei\u00e7\u00e3o / nulidade",
                "tender_document": "Partes do edital",
                "technical_bid": "Cap\u00edtulos da proposta t\u00e9cnica",
                "industry": "Bens / servi\u00e7os",
                "score_method": "Tipos de m\u00e9todo de pontua\u00e7\u00e3o",
                "goods": "Bens versus servi\u00e7os",
                "news": "Nota de lan\u00e7amento",
                "sources": "\u00cdndice de publica\u00e7\u00f5es",
                "usage": "Envios n\u00e3o s\u00e3o usados para treino",
            },
            ("P\u00e1gina", "URL"),
            "Compila\u00e7\u00e3o MIT. Os direitos das leis e avisos permanecem no emissor.",
        ),
        "ru": (
            "README.ru.md",
            "\u041d\u0430\u0431\u043e\u0440 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u0442\u0435\u043d\u0434\u0435\u0440\u043e\u0432 WenBiao",
            "JSON/CSV-\u043a\u043e\u043f\u0438\u044f \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u043e\u043d\u043d\u043e\u0433\u043e \u0440\u0435\u0435\u0441\u0442\u0440\u0430. \u0423 \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0438 \u0435\u0441\u0442\u044c \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u0439 `source_url`.",
            "\u041a\u0430\u043d\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0430\u0439\u0442",
            "\u041e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u0430\u044f \u0433\u043b\u0430\u0432\u043d\u0430\u044f",
            "\u042d\u0442\u043e \u043d\u0435 \u043e\u0446\u0435\u043d\u043e\u0447\u043d\u0430\u044f \u043a\u043e\u043c\u0438\u0441\u0441\u0438\u044f, \u043d\u0435 \u0441\u0442\u0430\u0442\u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438 \u043d\u0435 \u0440\u0435\u0439\u0442\u0438\u043d\u0433 \u043f\u043e\u0431\u0435\u0434. \u041d\u0435\u0442 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u043e\u0433\u043e URL \u2014 \u043d\u0435\u0442 \u0441\u0442\u0440\u043e\u043a\u0438. \u041d\u0443\u0436\u043d\u0430 \u0440\u0443\u0447\u043d\u0430\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430; \u043f\u043e\u0431\u0435\u0434\u0430 \u043d\u0435 \u0433\u0430\u0440\u0430\u043d\u0442\u0438\u0440\u0443\u0435\u0442\u0441\u044f.",
            "\u0421\u0441\u044b\u043b\u043a\u0438 \u043e\u0444\u0438\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0441\u0430\u0439\u0442\u0430",
            {
                "home": "\u0413\u043b\u0430\u0432\u043d\u0430\u044f WenBiao",
                "data": "\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445",
                "methodology": "\u041a\u0430\u043a \u0432\u043a\u043b\u044e\u0447\u0430\u044e\u0442 \u0441\u0442\u0440\u043e\u043a\u0443",
                "citations": "\u0418\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438 \u043f\u043e \u0441\u0442\u0440\u043e\u043a\u0430\u043c",
                "tender_score": "\u041a\u043b\u0430\u0441\u0441\u044b \u043a\u0440\u0438\u0442\u0435\u0440\u0438\u0435\u0432",
                "bid_rejection": "\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0438\u0435 / \u043d\u0435\u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c",
                "tender_document": "\u0421\u043e\u0441\u0442\u0430\u0432 \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u0430\u0446\u0438\u0438",
                "technical_bid": "\u0413\u043b\u0430\u0432\u044b \u0442\u0435\u0445\u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f",
                "industry": "\u0422\u043e\u0432\u0430\u0440\u044b / \u0443\u0441\u043b\u0443\u0433\u0438",
                "score_method": "\u0422\u0438\u043f\u044b \u043c\u0435\u0442\u043e\u0434\u043e\u0432 \u043e\u0446\u0435\u043d\u043a\u0438",
                "goods": "\u0422\u043e\u0432\u0430\u0440\u044b \u043f\u0440\u043e\u0442\u0438\u0432 \u0443\u0441\u043b\u0443\u0433",
                "news": "\u0417\u0430\u043c\u0435\u0442\u043a\u0430 \u043e \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0438",
                "sources": "\u0418\u043d\u0434\u0435\u043a\u0441 \u043f\u0443\u0431\u043b\u0438\u043a\u0430\u0446\u0438\u0439",
                "usage": "\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u043d\u0435 \u0438\u0434\u0443\u0442 \u0432 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435",
            },
            ("\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430", "URL"),
            "\u0421\u0432\u043e\u0434\u043a\u0430 MIT. \u0410\u0432\u0442\u043e\u0440\u0441\u043a\u043e\u0435 \u043f\u0440\u0430\u0432\u043e \u043d\u0430 \u0437\u0430\u043a\u043e\u043d\u044b \u0438 \u0438\u0437\u0432\u0435\u0449\u0435\u043d\u0438\u044f \u043e\u0441\u0442\u0430\u0451\u0442\u0441\u044f \u0443 \u0438\u0437\u0434\u0430\u0442\u0435\u043b\u044f.",
        ),
        "ar": (
            "README.ar.md",
            "\u0645\u062c\u0645\u0648\u0639\u0629 \u062a\u0635\u0646\u064a\u0641 \u0627\u0644\u0645\u0646\u0627\u0642\u0635\u0627\u062a (WenBiao)",
            "\u0646\u0633\u062e\u0629 JSON/CSV \u0645\u0646 \u0633\u062c\u0644 \u062a\u0635\u0646\u064a\u0641. \u0644\u0643\u0644 \u0635\u0641 \u0631\u0627\u0628\u0637 `source_url` \u0639\u0627\u0645.",
            "\u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0631\u0633\u0645\u064a",
            "\u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",
            "\u0644\u064a\u0633\u062a \u0644\u062c\u0646\u0629 \u062a\u0642\u064a\u064a\u0645 \u0648\u0644\u0627 \u062c\u0647\u0627\u0632 \u0625\u062d\u0635\u0627\u0621 \u0648\u0644\u0627 \u062a\u0631\u062a\u064a\u0628 \u0641\u0648\u0632. \u0628\u0644\u0627 URL \u0639\u0627\u0645 \u0644\u0627 \u064a\u0648\u062c\u062f \u0635\u0641. \u0627\u0644\u0645\u0631\u0627\u062c\u0639\u0629 \u0627\u0644\u0628\u0634\u0631\u064a\u0629 \u0648\u0627\u062c\u0628\u0629\u061b \u0644\u0627 \u0636\u0645\u0627\u0646 \u0644\u0644\u0641\u0648\u0632.",
            "\u0631\u0648\u0627\u0628\u0637 \u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0631\u0633\u0645\u064a",
            {
                "home": "\u0627\u0644\u0631\u0626\u064a\u0633\u064a\u0629",
                "data": "\u0645\u062e\u062a\u0628\u0631 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a",
                "methodology": "\u0642\u0648\u0627\u0639\u062f \u0627\u0644\u0625\u062f\u0631\u0627\u062c",
                "citations": "\u0627\u0644\u0645\u0635\u0627\u062f\u0631",
                "tender_score": "\u062a\u0635\u0646\u064a\u0641 \u0645\u0639\u0627\u064a\u064a\u0631 \u0627\u0644\u062a\u0642\u064a\u064a\u0645",
                "bid_rejection": "\u0627\u0644\u0631\u0641\u0636 / \u0627\u0644\u0628\u0637\u0644\u0627\u0646",
                "tender_document": "\u0623\u062c\u0632\u0627\u0621 \u0648\u062b\u064a\u0642\u0629 \u0627\u0644\u0639\u0637\u0627\u0621",
                "technical_bid": "\u0641\u0635\u0648\u0644 \u0627\u0644\u0639\u0631\u0636 \u0627\u0644\u062a\u0642\u0646\u064a",
                "industry": "\u0633\u0644\u0639 / \u062e\u062f\u0645\u0627\u062a",
                "score_method": "\u0623\u0646\u0648\u0627\u0639 \u0637\u0631\u0642 \u0627\u0644\u062a\u0642\u064a\u064a\u0645",
                "goods": "\u0627\u0644\u0633\u0644\u0639 \u0645\u0642\u0627\u0628\u0644 \u0627\u0644\u062e\u062f\u0645\u0627\u062a",
                "news": "\u0645\u0644\u0627\u062d\u0638\u0629 \u0627\u0644\u0625\u0637\u0644\u0627\u0642",
                "sources": "\u0641\u0647\u0631\u0633 \u0627\u0644\u0645\u0646\u0634\u0648\u0631\u0627\u062a",
                "usage": "\u0627\u0644\u0631\u0641\u0639 \u0644\u0627 \u064a\u064f\u0633\u062a\u062e\u062f\u0645 \u0644\u0644\u062a\u062f\u0631\u064a\u0628",
            },
            ("\u0627\u0644\u0635\u0641\u062d\u0629", "URL"),
            "\u0627\u0644\u062c\u062f\u0648\u0644\u0629 MIT. \u062d\u0642\u0648\u0642 \u0627\u0644\u0646\u0635\u0648\u0635 \u0627\u0644\u0631\u0633\u0645\u064a\u0629 \u062a\u0628\u0642\u0649 \u0644\u062f\u0649 \u0627\u0644\u0646\u0627\u0634\u0631.",
        ),
        "vi": (
            "README.vi.md",
            "B\u1ed9 d\u1eef li\u1ec7u ph\u00e2n lo\u1ea1i \u0111\u1ea5u th\u1ea7u WenBiao",
            "B\u1ea3n sao JSON/CSV c\u1ee7a s\u1ed5 c\u00e1i ph\u00e2n lo\u1ea1i. M\u1ed7i d\u00f2ng c\u00f3 `source_url` c\u00f4ng khai.",
            "Trang chu\u1ea9n",
            "Trang ch\u1ee7 ch\u00ednh th\u1ee9c",
            "Kh\u00f4ng ph\u1ea3i h\u1ed9i \u0111\u1ed3ng ch\u1ea5m, c\u1ee5c th\u1ed1ng k\u00ea hay b\u1ea3ng x\u1ebfp h\u1ea1ng t\u1ef7 l\u1ec7 tr\u00fang. Kh\u00f4ng c\u00f3 URL c\u00f4ng khai th\u00ec kh\u00f4ng c\u00f3 d\u00f2ng. B\u1eaft bu\u1ed9c r\u00e0 so\u00e1t th\u1ee7 c\u00f4ng; kh\u00f4ng b\u1ea3o \u0111\u1ea3m tr\u00fang th\u1ea7u.",
            "Li\u00ean k\u1ebft website ch\u00ednh th\u1ee9c",
            {
                "home": "Trang ch\u1ee7 WenBiao",
                "data": "Ph\u00f2ng th\u00ed nghi\u1ec7m d\u1eef li\u1ec7u",
                "methodology": "C\u00e1ch \u0111\u01b0a v\u00e0o s\u1ed5",
                "citations": "Ngu\u1ed3n t\u1eebng d\u00f2ng",
                "tender_score": "Ph\u00e2n lo\u1ea1i ti\u00eau ch\u00ed",
                "bid_rejection": "Lo\u1ea1i / v\u00f4 hi\u1ec7u",
                "tender_document": "C\u1ea5u ph\u1ea7n h\u1ed3 s\u01a1",
                "technical_bid": "Ch\u01b0\u01a1ng h\u1ed3 s\u01a1 k\u1ef9 thu\u1eadt",
                "industry": "H\u00e0ng h\u00f3a / d\u1ecbch v\u1ee5",
                "score_method": "C\u00e1c lo\u1ea1i ph\u01b0\u01a1ng ph\u00e1p ch\u1ea5m",
                "goods": "H\u00e0ng h\u00f3a so v\u1edbi d\u1ecbch v\u1ee5",
                "news": "Ghi ch\u00fa ra m\u1eaft",
                "sources": "M\u1ee5c b\u00e0i \u0111\u0103ng ngo\u00e0i",
                "usage": "T\u1ea3i l\u00ean kh\u00f4ng d\u00f9ng \u0111\u1ec3 hu\u1ea5n luy\u1ec7n",
            },
            ("Trang", "URL"),
            "B\u1ea3ng t\u1ed5ng h\u1ee3p MIT. B\u1ea3n quy\u1ec1n v\u0103n b\u1ea3n ph\u00e1p lu\u1eadt thu\u1ed9c c\u01a1 quan ban h\u00e0nh.",
        ),
        "id": (
            "README.id.md",
            "Dataset klasifikasi tender WenBiao",
            "Salinan JSON/CSV dari buku besar klasifikasi. Setiap baris punya `source_url` publik.",
            "Situs kanonik",
            "Beranda resmi",
            "Bukan panitia penilaian, biro statistik, atau peringkat kemenangan. Tanpa URL publik tidak ada baris. Wajib tinjauan manusia; kemenangan tidak dijamin.",
            "Tautan situs resmi",
            {
                "home": "Beranda WenBiao",
                "data": "Laboratorium data",
                "methodology": "Aturan pemasukan",
                "citations": "Sumber per baris",
                "tender_score": "Taksonomi kriteria",
                "bid_rejection": "Penolakan / batal",
                "tender_document": "Bagian dokumen tender",
                "technical_bid": "Bab penawaran teknis",
                "industry": "Barang / jasa",
                "score_method": "Jenis metode skor",
                "goods": "Barang vs jasa",
                "news": "Catatan rilis",
                "sources": "Indeks publikasi",
                "usage": "Unggahan tidak untuk pelatihan",
            },
            ("Halaman", "URL"),
            "Kompilasi MIT. Hak cipta undang-undang tetap pada penerbit.",
        ),
        "th": (
            "README.th.md",
            "WenBiao tender classification dataset",
            "JSON/CSV copy. Every row has a public source_url.",
            "Canonical site",
            "Official home",
            "Not an evaluation board, statistics office, or win-rate ranking. No public URL means no row. Human review required; winning is not guaranteed.",
            "Official website links",
            {
                "home": "WenBiao home",
                "data": "Data lab (canonical)",
                "methodology": "Inclusion rules",
                "citations": "Line sources",
                "tender_score": "Score-item classes",
                "bid_rejection": "Rejection classes",
                "tender_document": "Document parts",
                "technical_bid": "Technical chapters",
                "industry": "Goods / services",
                "score_method": "Scoring methods",
                "goods": "Goods vs services",
                "news": "Launch note",
                "sources": "Publication index",
                "usage": "Uploads not used for training",
            },
            ("Page", "URL"),
            "Compilation MIT. Statute copyright stays with the publisher.",
        ),
        "it": (
            "README.it.md",
            "Dataset di classificazione gare WenBiao",
            "Copia JSON/CSV di un registro di classificazione. Ogni riga ha un `source_url` pubblico.",
            "Sito canonico",
            "Home ufficiale",
            "Non e una commissione di valutazione, un istituto di statistica o una classifica di aggiudicazione. Senza URL pubblica non c'e riga. Serve revisione umana; la vittoria non e garantita.",
            "Link del sito ufficiale",
            {
                "home": "Home WenBiao",
                "data": "Laboratorio dati (canonico)",
                "methodology": "Regole di inclusione",
                "citations": "Fonti riga per riga",
                "tender_score": "Tassonomia dei criteri",
                "bid_rejection": "Esclusione / nullita",
                "tender_document": "Parti del bando",
                "technical_bid": "Capitoli dell'offerta tecnica",
                "industry": "Forniture / servizi",
                "score_method": "Tipi di metodo di punteggio",
                "goods": "Forniture vs servizi",
                "news": "Nota di pubblicazione",
                "sources": "Indice pubblicazioni",
                "usage": "Gli upload non addestrano modelli",
            },
            ("Pagina", "URL"),
            "Compilazione MIT. Il copyright di leggi e avvisi resta all'emittente.",
        ),
        "hi": (
            "README.hi.md",
            "WenBiao tender classification dataset",
            "JSON/CSV copy of a classification ledger. Every row has a public `source_url`.",
            "Canonical site",
            "Official home",
            "Yah evaluation committee, statistics office ya win-rate ranking nahi hai. Public URL na ho to row nahi. Human review zaroori hai; jeet ki guarantee nahi.",
            "Official website links",
            {
                "home": "WenBiao home",
                "data": "Data lab (canonical)",
                "methodology": "Inclusion rules",
                "citations": "Line sources",
                "tender_score": "Score-item classes",
                "bid_rejection": "Rejection classes",
                "tender_document": "Document parts",
                "technical_bid": "Technical chapters",
                "industry": "Goods / services",
                "score_method": "Scoring methods",
                "goods": "Goods vs services",
                "news": "Launch note",
                "sources": "Publication index",
                "usage": "Uploads not used for training",
            },
            ("Page", "URL"),
            "Compilation MIT. Statute copyright stays with the publisher.",
        ),
    }

    for code, spec in others.items():
        fn, title, lede, canon_l, home_l, warn, links_h, labels, headers, lic = spec
        dump(
            fn,
            f"""# {title}

{lang_bar(code)}

{lede}

**{canon_l}: [{SITE["data"]}]({SITE["data"]})**  
{home_l}: [{SITE["home"]}]({SITE["home"]})

{warn}

## {links_h}

{official_table(headers, pages(labels))}

- Methodology: [{SITE["methodology"]}]({SITE["methodology"]}) \u00b7 [`METHODOLOGY.md`](METHODOLOGY.md)
- Citations: [{SITE["citations"]}]({SITE["citations"]}) \u00b7 [`SOURCES.md`](SOURCES.md)
- Prompt repo (not this dataset): [{SITE["prompts"]}]({SITE["prompts"]})

## License

{lic}
""",
        )

    method = f"""# Methodology

Canonical site: {SITE["data"]}
Official inclusion page: {SITE["methodology"]}
Citations: {SITE["citations"]}

## Inclusion

Only rows that point to a public `source_url`: statutes, administrative regulations, Ministry of Finance rules, and China Government Procurement Network theory/practice articles.

No public URL means no row. Prefer the official statute page. Individual project notices are not added until each line is checked.

## Incomparability

Goods / services / works / IT, qualification vs scoring factors, and rejection vs invalid bid are separate rows. Do not invent a national "most common" list or an appearance rate.

## Coverage (v1)

Statutes and CCGP public articles are thicker. Single-project notices are thinner and will be added after verification.

## Not this dataset

- Not an evaluation basis
- Not a win-rate ranking
- Not a 1,000-document sample
- Does not republish full tender PDFs
- [`/data-usage`]({SITE["usage"]}) is the upload/training policy, not this ledger
- [`/sources`]({SITE["sources"]}) is the third-party publication index, not row citations

See also: {SITE["tender_score"]}, {SITE["bid_rejection"]}, {SITE["tender_document"]}, {SITE["technical_bid"]}
"""
    dump("METHODOLOGY.md", method)
    print("wrote", len(list(ROOT.glob("README*.md"))), "readmes")


if __name__ == "__main__":
    main()
