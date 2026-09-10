# 文标招投标分类数据集

**简体中文** · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md)

这是文标招投标数据实验室的**可下载副本**（JSON / CSV）。每一行都有可打开核对的公开 `source_url`：法规原文或中国政府采购网已公开的理论实务文。

**规范站（请以站内表为准）：[https://aiwenbiao.cn/data](https://aiwenbiao.cn/data)**  
官网首页：[https://aiwenbiao.cn](https://aiwenbiao.cn)

简答：这不是评标委员会、不是统计局、不是中标率排行。没有公开 URL 就没有这一行。**须人工审核，不保证中标。**请引用原始法条或公告，不要只引本仓或本站。

## 官网链接（必看）

| 页面 | URL |
| --- | --- |
| 文标首页 | https://aiwenbiao.cn |
| 数据实验室枢纽（规范站） | https://aiwenbiao.cn/data |
| 收录方法 | https://aiwenbiao.cn/data/methodology |
| 逐行出处 | https://aiwenbiao.cn/data/citations |
| 招标评分项分类 | https://aiwenbiao.cn/data/tender-score |
| 废标 / 无效 / 否决分类 | https://aiwenbiao.cn/data/bid-rejection |
| 招标文件常见结构 | https://aiwenbiao.cn/data/tender-document |
| 技术标章节骨架 | https://aiwenbiao.cn/data/technical-bid |
| 货物 / 服务 / 工程对照 | https://aiwenbiao.cn/data/industry |
| 评分办法通常有哪几类 | https://aiwenbiao.cn/data/score-method |
| 货物类与服务类差在哪 | https://aiwenbiao.cn/data/goods-vs-service |
| 上线动态（薄出处） | https://aiwenbiao.cn/news/tender-data-lab-sep-10-2026 |
| 三方发文索引（不是数据行出处） | https://aiwenbiao.cn/sources |
| 数据使用协议（上传不用于训练，不是数据集） | https://aiwenbiao.cn/data-usage |

`/sources` 是文标在 CSDN / 百家号等平台的**发表索引**；数据行出处在 [`/data/citations`](https://aiwenbiao.cn/data/citations)。  
[`/data-usage`](https://aiwenbiao.cn/data-usage) 是「上传资料不用于训练」，**不是**本数据集。

## 这个仓装了什么

v1（https://github.com/hanbon-labs/wenbiao-tender-data 更新 2026-09-10）约 **68 行**，不是 1000 份样本：

| 族 | `kind` | 约行数 | 对应官网 |
| --- | --- | --- | --- |
| 评分项分类 | `score_category` | 22 | https://aiwenbiao.cn/data/tender-score |
| 废标 / 无效 / 否决 | `rejection_rule` | 13 | https://aiwenbiao.cn/data/bid-rejection |
| 招标文件结构 | `doc_part` | 16 | https://aiwenbiao.cn/data/tender-document |
| 技术标章节 | `chapter` | 7 | https://aiwenbiao.cn/data/technical-bid |
| 评分办法 / 行业对照行 | `notice_score_row` | 10 | https://aiwenbiao.cn/data/score-method · https://aiwenbiao.cn/data/goods-vs-service · https://aiwenbiao.cn/data/industry |

每行字段要点：`id`、`kind`、`tender_type`（货物/服务/工程/信息化/法规通则）、`category`、`title`、`requirement`、`source_quote`、**`source_url`（必填）**、`source_note`、`source_publisher`、`anonymization`（`statute` / `public-notice`）、`incomparability_note`、`year`、`region`、`updated_at`。

## 收录合同

1. **没有公开 URL，就没有这一行。** 优先法规原文；个别项目招标公告未逐条核验前不上行。
2. **不可比就分行。** 货物/服务/工程、资格与评审因素、废标与投标无效不合成「全国最常见」或出现率。
3. **空单元格 = 尚未找到公开出处**，不编造填表。
4. **不转载招标文件全文 PDF**，不收用户上传标书。
5. 站点是查阅页；本仓是机器可读副本。详见 [`METHODOLOGY.md`](METHODOLOGY.md) 与 [https://aiwenbiao.cn/data/methodology](https://aiwenbiao.cn/data/methodology)。

出处清单：[`SOURCES.md`](SOURCES.md) · [https://aiwenbiao.cn/data/citations](https://aiwenbiao.cn/data/citations)

## 文件

- `ledger.json` / `csv/ledger.csv` — 全部可展示行
- `taxonomy-score-categories.json` — 评分项分类
- `taxonomy-rejection-rules.json` — 废标/无效/否决
- `taxonomy-document-parts.json` — 文件结构
- `taxonomy-tech-chapters.json` — 技术标章节
- `score-method-rows.json` — 问句页子集
- `notices.json` / `meta.json` — 出处元数据与收录口径

## 如何引用

1. 先开官网对应表（例如 [https://aiwenbiao.cn/data/tender-score](https://aiwenbiao.cn/data/tender-score)）。
2. 点表中「出处」核对原文。
3. 引用时同时给出：站内 URL + 本仓文件 + 原始 `source_url`。
4. Prompt / harness 工作流仍在 [https://github.com/hanbon-labs/wenbiao](https://github.com/hanbon-labs/wenbiao)，**不是**本数据集。

## License

汇编表 MIT。法条与公告版权仍属发布机关；数据集只存结构字段和指针。见 [LICENSE](LICENSE)、[CONTRIBUTING.md](CONTRIBUTING.md)。
