# WenBiao-Klassifikationsdatensatz für Ausschreibungen

[简体中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · **Deutsch** · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md)

Ledger mit öffentlicher `source_url` in jeder Zeile (JSON / CSV). v1 **68 Zeilen**.

**Kanonische Seite:** [https://aiwenbiao.cn/data](https://aiwenbiao.cn/data)

## Inhalt

| 族 | `kind` | 行数 | 官网 |
| --- | --- | ---: | --- |
| 评分项分类 | `score_category` | 22 | https://aiwenbiao.cn/data/tender-score |
| 废标 / 无效 / 否决 | `rejection_rule` | 13 | https://aiwenbiao.cn/data/bid-rejection |
| 招标文件结构 | `doc_part` | 16 | https://aiwenbiao.cn/data/tender-document |
| 技术标章节 | `chapter` | 7 | https://aiwenbiao.cn/data/technical-bid |
| 评分办法 / 行业对照 | `notice_score_row` | 10 | https://aiwenbiao.cn/data/score-method |
| **合计** | | **68** | https://aiwenbiao.cn/data |

## Felder

| 字段 | 含义 |
| --- | --- |
| `id` | 行号 |
| `kind` | 族 |
| `tender_type` | 货物 / 服务 / 工程 / 信息化 / 法规通则 |
| `category` | 分部 |
| `title` | 名称 |
| `requirement` | 说明 |
| `source_quote` | 原文摘录 |
| `source_url` | 公开出处（必填） |
| `source_note` | 条号或文章名 |
| `source_publisher` | 发布方 |
| `anonymization` | `statute` / `public-notice` |
| `incomparability_note` | 不可比说明 |
| `year` | 年份 |
| `region` | 地域 |
| `updated_at` | 更新日 |

## Beispiele

| 名称 | `kind` | 分部 | 出处 |
| --- | --- | --- | --- |
| 投标报价 | `score_category` | 价格 | [财政部令第87号第五十五条](https://www.ccgp.gov.cn/zcfg/mofgz/201707/t20170718_8541199.shtml) |
| 技术或者服务水平 | `score_category` | 技术 | [财政部令第87号第五十五条](https://www.ccgp.gov.cn/zcfg/mofgz/201707/t20170718_8541199.shtml) |
| 废标：实质响应供应商不足三家 | `rejection_rule` | 符合性 | [政府采购法第三十六条](https://www.ccgp.gov.cn/zcfg/gjfg/201310/t20131029_3587339.htm) |
| 废标：影响采购公正的违法违规 | `rejection_rule` | 符合性 | [政府采购法第三十六条](https://www.ccgp.gov.cn/zcfg/gjfg/201310/t20131029_3587339.htm) |
| 投标邀请 | `doc_part` | 其他 | [财政部令第87号第二十条](https://www.ccgp.gov.cn/zcfg/mofgz/201707/t20170718_8541199.shtml) |
| 投标人须知（密封、签署、盖章） | `doc_part` | 其他 | [财政部令第87号第二十条](https://www.ccgp.gov.cn/zcfg/mofgz/201707/t20170718_8541199.shtml) |
| 编制依据与需求理解 | `chapter` | 技术 | [财政部令第87号第二十条](https://www.ccgp.gov.cn/zcfg/mofgz/201707/t20170718_8541199.shtml) |
| 总体技术方案 / 方案设计 | `chapter` | 技术 | [中国政府采购网理论实务，2020-09-15](https://www.ccgp.gov.cn/llsw/202009/t20200915_15070380.htm) |
| 评标方法分为最低评标价法和综合评分法 | `notice_score_row` | 其他 | [政府采购法实施条例第三十四条](https://www.ccgp.gov.cn/zcfg/mof/201502/t20150227_5029424.shtml) |
| 最低评标价法 | `notice_score_row` | 价格 | [政府采购法实施条例第三十四条](https://www.ccgp.gov.cn/zcfg/mof/201502/t20150227_5029424.shtml) |

## Dateien

- `ledger.json` / `csv/ledger.csv` — 全部 68 行
- `taxonomy-score-categories.json` — 评分项 22
- `taxonomy-rejection-rules.json` — 废标/无效/否决 13
- `taxonomy-document-parts.json` — 招标文件结构 16
- `taxonomy-tech-chapters.json` — 技术标章节 7
- `score-method-rows.json` — 评分办法/行业对照 10
- `notices.json` / `meta.json` — 出处元数据
- [`SOURCES.md`](SOURCES.md) — 出处清单
- [`METHODOLOGY.md`](METHODOLOGY.md) — 收录口径

## License

MIT
