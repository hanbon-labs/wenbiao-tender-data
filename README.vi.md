# Tập dữ liệu phân loại đấu thầu WenBiao

[简体中文](README.md) · [繁體中文](README.zh-Hant.md) · [English](README.en.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · **Tiếng Việt** · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Italiano](README.it.md) · [हिन्दी](README.hi.md)

Sổ cái có `source_url` công khai mỗi dòng (JSON / CSV). v2 **129 dòng**.

**Trang chuẩn:** [https://aiwenbiao.cn/data](https://aiwenbiao.cn/data)

## Thành phần

| 族 | `kind` | 行数 | 官网 |
| --- | --- | ---: | --- |
| 评分项分类 | `score_category` | 40 | https://aiwenbiao.cn/data/tender-score |
| 废标 / 无效 / 否决 | `rejection_rule` | 29 | https://aiwenbiao.cn/data/bid-rejection |
| 招标文件结构 | `doc_part` | 21 | https://aiwenbiao.cn/data/tender-document |
| 技术标章节 | `chapter` | 11 | https://aiwenbiao.cn/data/technical-bid |
| 评分办法 / 行业对照 | `notice_score_row` | 28 | https://aiwenbiao.cn/data/score-method |
| **合计** | | **129** | https://aiwenbiao.cn/data |

## Trường

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

## Mẫu

| 名称 | `kind` | 分部 | 出处 |
| --- | --- | --- | --- |
| 必须满足的核心要求应设为符合性条件，而不是全部拿去赋分 | `score_category` | 符合性 | [中国政府采购网理论实务，2026-03-24](https://www.ccgp.gov.cn/llsw/202603/t20260324_26305325.htm) |
| 报价分 / 技术分 / 商务分 / 政策分 | `score_category` | 其他 | [中国政府采购网理论实务，2026-03-24](https://www.ccgp.gov.cn/llsw/202603/t20260324_26305325.htm) |
| 电子标里扫描清晰度、PDF分层、电子签章位置成为新的格式争议点 | `rejection_rule` | 符合性 | [中国政府采购网理论实务，2025-05-09](https://www.ccgp.gov.cn/llsw/202505/t20250509_24565317.htm) |
| 法律法规没有对“格式性要求”给出废标定义 | `rejection_rule` | 符合性 | [中国政府采购网理论实务，2025-05-09](https://www.ccgp.gov.cn/llsw/202505/t20250509_24565317.htm) |
| 实质性条款应以醒目方式标明 | `doc_part` | 其他 | [中国政府采购网理论实务，2025-05-09](https://www.ccgp.gov.cn/llsw/202505/t20250509_24565317.htm) |
| 合作创新响应文件还应包括研发完成时间、分项报价、验收标准、知识产权 | `doc_part` | 其他 | [合作创新采购方式管理暂行办法第二十条](https://www.ccgp.gov.cn/zcfg/mof/202404/t20240426_21937284.htm) |
| 创新产品的售后服务方案 | `chapter` | 服务 | [合作创新采购方式管理暂行办法第二十条](https://www.ccgp.gov.cn/zcfg/mof/202404/t20240426_21937284.htm) |
| 研发方案 | `chapter` | 技术 | [合作创新采购方式管理暂行办法第二十条](https://www.ccgp.gov.cn/zcfg/mof/202404/t20240426_21937284.htm) |
| 技术分“不设扣分上限”会出现负分，不符合分值与指标对应 | `notice_score_row` | 技术 | [中国政府采购网理论实务，2026-03-24](https://www.ccgp.gov.cn/llsw/202603/t20260324_26305325.htm) |
| “每负偏离一项扣分，扣完为止”不符合分值与量化指标一一对应 | `notice_score_row` | 技术 | [中国政府采购网理论实务，2026-03-24](https://www.ccgp.gov.cn/llsw/202603/t20260324_26305325.htm) |

## Tệp

- `ledger.json` / `csv/ledger.csv` — 全部可展示行
- `taxonomy-score-categories.json` — 评分项
- `taxonomy-rejection-rules.json` — 废标/无效/否决
- `taxonomy-document-parts.json` — 招标文件结构
- `taxonomy-tech-chapters.json` — 技术标章节
- `score-method-rows.json` — 评分办法/行业对照
- `notices.json` / `meta.json` — 出处元数据
- [`SOURCES.md`](SOURCES.md) — 出处清单
- [`METHODOLOGY.md`](METHODOLOGY.md) — 收录口径

## License

MIT
