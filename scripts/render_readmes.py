# -*- coding: utf-8 -*-
"""Render data-first multilingual READMEs. Run from repo root."""
from __future__ import annotations

import json
from collections import Counter
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
    "data": "https://aiwenbiao.cn/data",
    "tender_score": "https://aiwenbiao.cn/data/tender-score",
    "bid_rejection": "https://aiwenbiao.cn/data/bid-rejection",
    "tender_document": "https://aiwenbiao.cn/data/tender-document",
    "technical_bid": "https://aiwenbiao.cn/data/technical-bid",
    "industry": "https://aiwenbiao.cn/data/industry",
    "score_method": "https://aiwenbiao.cn/data/score-method",
    "goods": "https://aiwenbiao.cn/data/goods-vs-service",
}

KIND_META = [
    ("score_category", "\u8bc4\u5206\u9879\u5206\u7c7b", SITE["tender_score"]),
    ("rejection_rule", "\u5e9f\u6807 / \u65e0\u6548 / \u5426\u51b3", SITE["bid_rejection"]),
    ("doc_part", "\u62db\u6807\u6587\u4ef6\u7ed3\u6784", SITE["tender_document"]),
    ("chapter", "\u6280\u672f\u6807\u7ae0\u8282", SITE["technical_bid"]),
    ("notice_score_row", "\u8bc4\u5206\u529e\u6cd5 / \u884c\u4e1a\u5bf9\u7167", SITE["score_method"]),
]


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
    if "README" in name:
        assert b"aiwenbiao.cn/data" in raw
        assert not raw.startswith(b"\xef\xbb\xbf")


def load_ledger() -> list[dict]:
    return json.loads((ROOT / "ledger.json").read_text(encoding="utf-8"))


def inventory_table(rows: list[dict]) -> str:
    counts = Counter(r["kind"] for r in rows)
    lines = [
        "| \u65cf | `kind` | \u884c\u6570 | \u5b98\u7f51 |",
        "| --- | --- | ---: | --- |",
    ]
    for kind, label, url in KIND_META:
        lines.append(f"| {label} | `{kind}` | {counts[kind]} | {url} |")
    lines.append(f"| **\u5408\u8ba1** | | **{len(rows)}** | {SITE['data']} |")
    return "\n".join(lines)


def field_table() -> str:
    fields = [
        ("id", "\u884c\u53f7"),
        ("kind", "\u65cf"),
        ("tender_type", "\u8d27\u7269 / \u670d\u52a1 / \u5de5\u7a0b / \u4fe1\u606f\u5316 / \u6cd5\u89c4\u901a\u5219"),
        ("category", "\u5206\u90e8"),
        ("title", "\u540d\u79f0"),
        ("requirement", "\u8bf4\u660e"),
        ("source_quote", "\u539f\u6587\u6458\u5f55"),
        ("source_url", "\u516c\u5f00\u51fa\u5904\uff08\u5fc5\u586b\uff09"),
        ("source_note", "\u6761\u53f7\u6216\u6587\u7ae0\u540d"),
        ("source_publisher", "\u53d1\u5e03\u65b9"),
        ("anonymization", "`statute` / `public-notice`"),
        ("incomparability_note", "\u4e0d\u53ef\u6bd4\u8bf4\u660e"),
        ("year", "\u5e74\u4efd"),
        ("region", "\u5730\u57df"),
        ("updated_at", "\u66f4\u65b0\u65e5"),
    ]
    lines = ["| \u5b57\u6bb5 | \u542b\u4e49 |", "| --- | --- |"]
    for name, meaning in fields:
        lines.append(f"| `{name}` | {meaning} |")
    return "\n".join(lines)


def sample_table(rows: list[dict]) -> str:
    by_kind: dict[str, list[dict]] = {}
    for row in rows:
        by_kind.setdefault(row["kind"], []).append(row)
    picked: list[dict] = []
    for kind, _label, _url in KIND_META:
        group = sorted(
            by_kind.get(kind, []),
            key=lambda r: (-int(r.get("year") or 0), r["id"]),
        )
        picked.extend(group[:2])
    lines = [
        "| \u540d\u79f0 | `kind` | \u5206\u90e8 | \u51fa\u5904 |",
        "| --- | --- | --- | --- |",
    ]
    for row in picked:
        title = row["title"].replace("|", "/")
        note = row["source_note"].replace("|", "/")
        url = row["source_url"]
        lines.append(
            f"| {title} | `{row['kind']}` | {row['category']} | [{note}]({url}) |"
        )
    return "\n".join(lines)


def files_block() -> str:
    return """- `ledger.json` / `csv/ledger.csv` \u2014 \u5168\u90e8\u53ef\u5c55\u793a\u884c
- `taxonomy-score-categories.json` \u2014 \u8bc4\u5206\u9879
- `taxonomy-rejection-rules.json` \u2014 \u5e9f\u6807/\u65e0\u6548/\u5426\u51b3
- `taxonomy-document-parts.json` \u2014 \u62db\u6807\u6587\u4ef6\u7ed3\u6784
- `taxonomy-tech-chapters.json` \u2014 \u6280\u672f\u6807\u7ae0\u8282
- `score-method-rows.json` \u2014 \u8bc4\u5206\u529e\u6cd5/\u884c\u4e1a\u5bf9\u7167
- `notices.json` / `meta.json` \u2014 \u51fa\u5904\u5143\u6570\u636e
- [`SOURCES.md`](SOURCES.md) \u2014 \u51fa\u5904\u6e05\u5355
- [`METHODOLOGY.md`](METHODOLOGY.md) \u2014 \u6536\u5f55\u53e3\u5f84"""


def main() -> None:
    rows = load_ledger()
    inventory = inventory_table(rows)
    fields = field_table()
    sample = sample_table(rows)
    files = files_block()
    data = SITE["data"]
    goods = SITE["goods"]
    industry = SITE["industry"]

    dump(
        "README.md",
        f"""# \u6587\u6807\u62db\u6295\u6807\u5206\u7c7b\u6570\u636e\u96c6

{lang_bar("zh")}

\u6709\u516c\u5f00 `source_url` \u7684\u62db\u6295\u6807\u5206\u7c7b\u53f0\u8d26\uff08JSON / CSV\uff09\u3002v2 **{len(rows)} \u884c**\uff0c2026-09-10\u3002

\u89c4\u8303\u7ad9\uff1a[{data}]({data})

## \u6570\u636e\u6784\u6210

{inventory}

\u8bc4\u5206\u529e\u6cd5/\u884c\u4e1a\u5bf9\u7167\u884c\u8fd8\u5728 [{SITE["goods"]}]({goods}) \u4e0e [{SITE["industry"]}]({industry})\u3002

## \u5b57\u6bb5

{fields}

## \u6837\u4f8b

{sample}

\u5168\u8868\u89c1 `ledger.json`\u3002

## \u6587\u4ef6

{files}

## License

\u6c47\u7f16\u8868 MIT\u3002\u6cd5\u6761\u4e0e\u516c\u544a\u7248\u6743\u4ecd\u5c5e\u53d1\u5e03\u673a\u5173\uff1b\u6570\u636e\u96c6\u53ea\u5b58\u7ed3\u6784\u5b57\u6bb5\u548c\u6307\u9488\u3002
""",
    )

    dump(
        "README.en.md",
        f"""# WenBiao Chinese tender classification dataset

{lang_bar("en")}

Classification ledger with a public `source_url` on every row (JSON / CSV). v2 **{len(rows)} rows**, 2026-09-10.

Canonical site: [{data}]({data})

## Contents

{inventory}

Method/industry rows also appear on [{SITE["goods"]}]({goods}) and [{SITE["industry"]}]({industry}).

## Fields

{fields}

## Sample

{sample}

Full table: `ledger.json`.

## Files

{files}

## License

Compilation: MIT. Statute and notice copyright stays with the publishers.
""",
    )

    others = {
        "zh-Hant": (
            "README.zh-Hant.md",
            "\u6587\u6a19\u62db\u6295\u6a19\u5206\u985e\u6578\u64da\u96c6",
            f"\u6bcf\u5217\u90fd\u6709\u516c\u958b `source_url` \u7684\u5206\u985e\u81fa\u5e33\uff08JSON / CSV\uff09\u3002v2 **{len(rows)} \u5217**\u3002",
            "\u898f\u7bc4\u7ad9",
            "\u6578\u64da\u69cb\u6210",
            "\u6b04\u4f4d",
            "\u6a23\u4f8b",
            "\u6a94\u6848",
        ),
        "ja": (
            "README.ja.md",
            "WenBiao \u4e2d\u56fd\u5165\u672d\u5206\u985e\u30c7\u30fc\u30bf\u30bb\u30c3\u30c8",
            f"\u5404\u884c\u306b\u516c\u958b `source_url` \u304c\u3042\u308b\u5206\u985e\u53f0\u5e33\uff08JSON / CSV\uff09\u3002v2 **{len(rows)} \u884c**\u3002",
            "\u6b63\u898f\u30b5\u30a4\u30c8",
            "\u30c7\u30fc\u30bf\u69cb\u6210",
            "\u30d5\u30a3\u30fc\u30eb\u30c9",
            "\u30b5\u30f3\u30d7\u30eb",
            "\u30d5\u30a1\u30a4\u30eb",
        ),
        "ko": (
            "README.ko.md",
            "WenBiao \uc785\ucc30 \ubd84\ub958 \ub370\uc774\ud130\uc14b",
            f"\ud589\ub9c8\ub2e4 \uacf5\uac1c `source_url` \uc774 \uc788\ub294 \ubd84\ub958 \uc6d0\uc7a5(JSON / CSV). v2 **{len(rows)} \ud589**.",
            "\uc815\uaddc \uc0ac\uc774\ud2b8",
            "\ub370\uc774\ud130 \uad6c\uc131",
            "\ud544\ub4dc",
            "\uc0d8\ud50c",
            "\ud30c\uc77c",
        ),
        "es": (
            "README.es.md",
            "Conjunto de clasificaci\u00f3n de licitaciones WenBiao",
            f"Libro mayor con `source_url` p\u00fablico en cada fila (JSON / CSV). v2 **{len(rows)} filas**.",
            "Sitio can\u00f3nico",
            "Contenido",
            "Campos",
            "Muestra",
            "Archivos",
        ),
        "fr": (
            "README.fr.md",
            "Jeu de donn\u00e9es de classification d'appels d'offres WenBiao",
            f"Registre avec un `source_url` public sur chaque ligne (JSON / CSV). v2 **{len(rows)} lignes**.",
            "Site canonique",
            "Contenu",
            "Champs",
            "Exemples",
            "Fichiers",
        ),
        "de": (
            "README.de.md",
            "WenBiao-Klassifikationsdatensatz f\u00fcr Ausschreibungen",
            f"Ledger mit \u00f6ffentlicher `source_url` in jeder Zeile (JSON / CSV). v2 **{len(rows)} Zeilen**.",
            "Kanonische Seite",
            "Inhalt",
            "Felder",
            "Beispiele",
            "Dateien",
        ),
        "pt": (
            "README.pt.md",
            "Conjunto de classifica\u00e7\u00e3o de licita\u00e7\u00f5es WenBiao",
            f"Livro-raz\u00e3o com `source_url` p\u00fablico em cada linha (JSON / CSV). v2 **{len(rows)} linhas**.",
            "Site can\u00f4nico",
            "Conte\u00fado",
            "Campos",
            "Amostra",
            "Arquivos",
        ),
        "ru": (
            "README.ru.md",
            "\u041d\u0430\u0431\u043e\u0440 \u043a\u043b\u0430\u0441\u0441\u0438\u0444\u0438\u043a\u0430\u0446\u0438\u0438 \u0442\u0435\u043d\u0434\u0435\u0440\u043e\u0432 WenBiao",
            f"\u0420\u0435\u0435\u0441\u0442\u0440 \u0441 \u043f\u0443\u0431\u043b\u0438\u0447\u043d\u044b\u043c `source_url` \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435 (JSON / CSV). v2 **{len(rows)} \u0441\u0442\u0440\u043e\u043a**.",
            "\u041a\u0430\u043d\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u0430\u0439\u0442",
            "\u0421\u043e\u0441\u0442\u0430\u0432",
            "\u041f\u043e\u043b\u044f",
            "\u041f\u0440\u0438\u043c\u0435\u0440\u044b",
            "\u0424\u0430\u0439\u043b\u044b",
        ),
        "ar": (
            "README.ar.md",
            "\u0645\u062c\u0645\u0648\u0639\u0629 \u062a\u0635\u0646\u064a\u0641 \u0627\u0644\u0645\u0646\u0627\u0642\u0635\u0627\u062a WenBiao",
            f"\u0633\u062c\u0644 \u0628\u0647 `source_url` \u0639\u0627\u0645 \u0641\u064a \u0643\u0644 \u0635\u0641 (JSON / CSV). v2 **{len(rows)} \u0635\u0641\u064b\u0627**.",
            "\u0627\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0631\u0633\u0645\u064a",
            "\u0627\u0644\u0645\u062d\u062a\u0648\u0649",
            "\u0627\u0644\u062d\u0642\u0648\u0644",
            "\u0639\u064a\u0646\u0627\u062a",
            "\u0627\u0644\u0645\u0644\u0641\u0627\u062a",
        ),
        "vi": (
            "README.vi.md",
            "T\u1eadp d\u1eef li\u1ec7u ph\u00e2n lo\u1ea1i \u0111\u1ea5u th\u1ea7u WenBiao",
            f"S\u1ed5 c\u00e1i c\u00f3 `source_url` c\u00f4ng khai m\u1ed7i d\u00f2ng (JSON / CSV). v2 **{len(rows)} d\u00f2ng**.",
            "Trang chu\u1ea9n",
            "Th\u00e0nh ph\u1ea7n",
            "Tr\u01b0\u1eddng",
            "M\u1eabu",
            "T\u1ec7p",
        ),
        "id": (
            "README.id.md",
            "Dataset klasifikasi tender WenBiao",
            f"Buku besar dengan `source_url` publik di setiap baris (JSON / CSV). v2 **{len(rows)} baris**.",
            "Situs kanonis",
            "Isi",
            "Bidang",
            "Contoh",
            "Berkas",
        ),
        "th": (
            "README.th.md",
            "\u0e0a\u0e38\u0e14\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e1b\u0e23\u0e30\u0e40\u0e20\u0e17\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e30\u0e21\u0e39\u0e25 WenBiao",
            f"\u0e41\u0e15\u0e48\u0e25\u0e30\u0e41\u0e16\u0e27\u0e17\u0e35\u0e48\u0e17\u0e38\u0e01\u0e41\u0e16\u0e27\u0e21\u0e35 `source_url` \u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e30 (JSON / CSV). v2 **{len(rows)} \u0e41\u0e16\u0e27**.",
            "\u0e40\u0e27\u0e47\u0e1a\u0e16\u0e32\u0e19",
            "\u0e42\u0e04\u0e23\u0e07\u0e2a\u0e23\u0e49\u0e32\u0e07",
            "\u0e1f\u0e35\u0e25\u0e14\u0e4c",
            "\u0e15\u0e31\u0e27\u0e2d\u0e22\u0e48\u0e32\u0e07",
            "\u0e44\u0e1f\u0e25\u0e4c",
        ),
        "it": (
            "README.it.md",
            "Dataset di classificazione gare WenBiao",
            f"Registro con `source_url` pubblico su ogni riga (JSON / CSV). v2 **{len(rows)} righe**.",
            "Sito canonico",
            "Contenuto",
            "Campi",
            "Esempi",
            "File",
        ),
        "hi": (
            "README.hi.md",
            "WenBiao \u091f\u0947\u0902\u0921\u0930 \u0935\u0930\u094d\u0917\u0940\u0915\u0930\u0923 \u0921\u0947\u091f\u093e\u0938\u0947\u091f",
            f"\u0939\u0930 \u092a\u0902\u0915\u094d\u0924\u093f \u092a\u0930 \u0938\u093e\u0930\u094d\u0935\u091c\u0928\u093f\u0915 `source_url` (JSON / CSV). v2 **{len(rows)} \u092a\u0902\u0915\u094d\u0924\u093f\u092f\u093e\u0901**.",
            "\u0915\u0948\u0928\u094b\u0928\u093f\u0915\u0932 \u0938\u093e\u0907\u091f",
            "\u0938\u093e\u092e\u0917\u094d\u0930\u0940",
            "\u0915\u094d\u0937\u0947\u0924\u094d\u0930",
            "\u0928\u092e\u0942\u0928\u093e",
            "\u092b\u093c\u093e\u0877\u0932",
        ),
    }
    # fix accidental hi files label if wrong - I'll use simple Hindi "??????"
    others["hi"] = (
        "README.hi.md",
        "WenBiao \u091f\u0947\u0902\u0921\u0930 \u0935\u0930\u094d\u0917\u0940\u0915\u0930\u0923 \u0921\u0947\u091f\u093e\u0938\u0947\u091f",
        f"\u0939\u0930 \u092a\u0902\u0915\u094d\u0924\u093f \u092a\u0930 \u0938\u093e\u0930\u094d\u0935\u091c\u0928\u093f\u0915 `source_url` (JSON / CSV). v2 **{len(rows)} \u092a\u0902\u0915\u094d\u0924\u093f\u092f\u093e\u0901**.",
        "\u0915\u0948\u0928\u094b\u0928\u093f\u0915\u0932 \u0938\u093e\u0907\u091f",
        "\u0938\u093e\u092e\u0917\u094d\u0930\u0940",
        "\u0915\u094d\u0937\u0947\u0924\u094d\u0930",
        "\u0928\u092e\u0942\u0928\u093e",
        "\u092b\u093c\u093e\u0907\u0932\u0947\u0902",
    )

    for code, spec in others.items():
        fn, title, lede, canon_l, c_h, f_h, s_h, file_h = spec
        dump(
            fn,
            f"""# {title}

{lang_bar(code)}

{lede}

**{canon_l}:** [{data}]({data})

## {c_h}

{inventory}

## {f_h}

{fields}

## {s_h}

{sample}

## {file_h}

{files}

## License

MIT
""",
        )

    dump(
        "METHODOLOGY.md",
        f"""# Methodology

Canonical site: {data}

## Inclusion

Only rows with a public `source_url`. No URL means no row.

## Incomparability

Goods / services / works / IT, qualification vs scoring, and rejection vs invalid bid stay on separate rows. No invented national frequency.

## Coverage (v1)

{len(rows)} rows. Statutes and CCGP public articles first; single-project notices after line-by-line check.

See {data}
""",
    )

    contributing = """# \u8d21\u732e

\u8865\u5e26\u516c\u5f00 `source_url` \u7684\u5206\u7c7b\u884c\u3002\u89c4\u8303\u7ad9\uff1ahttps://aiwenbiao.cn/data

## \u53ef\u4ee5

- \u80fd\u6253\u5f00\u6838\u5bf9\u7684\u6cd5\u89c4\u6216\u653f\u91c7/\u62db\u6807\u516c\u5171\u670d\u52a1\u5e73\u53f0\u516c\u544a
- \u7a7a\u5355\u5143\u683c = \u5c1a\u65e0\u516c\u5f00\u51fa\u5904

## \u4e0d\u8981

- \u62db\u6807\u5168\u6587 PDF\u3001\u626b\u63cf\u4ef6\u3001\u7528\u6237\u4e0a\u4f20\u6807\u4e66
- \u7f16\u9020\u767e\u5206\u6bd4\u6216\u300c1000 \u4efd\u300d
- \u58f0\u79f0\u4fdd\u8bc1\u4e2d\u6807
"""
    dump("CONTRIBUTING.md", contributing)
    print("wrote", len(list(ROOT.glob("README*.md"))), "readmes", "rows", len(rows))


if __name__ == "__main__":
    main()
