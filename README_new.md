# 🌅 Horizon 本地部署手册

基于 [Thysrael/Horizon](https://github.com/Thysrael/Horizon) 部署的个人 AI 新闻雷达，每日自动聚合、评分、生成三语（英/中/日）简报并推送至 Telegram。

---

## 运行环境

| 项目 | 值 |
|------|-----|
| Python | 3.14+ |
| 包管理器 | uv |
| AI Provider | Agnes AI (OpenAI 兼容) |
| AI Model | agnes-2.0-flash |
| 输出语言 | English / 中文 / 日本語 |
| 推送方式 | Telegram Bot（文件形式） |

---

## 快速运行

```bash
# 生成每日简报（默认抓取最近 24 小时）
python -m uv run horizon

# 抓取最近 48 小时
python -m uv run horizon --hours 48

# 发送到 Telegram（自动发今天的 HTML 文件）
python -m uv run python scripts/send_telegram.py

# 指定日期发送
python -m uv run python scripts/send_telegram.py 2026-06-30

# 一步到位：生成 + 推送
python -m uv run horizon && python -m uv run python scripts/send_telegram.py
```

---

## 配置文件

| 文件 | 用途 |
|------|------|
| `.env` | API Key、Telegram Token 等敏感信息 |
| `data/config.json` | 来源、AI、过滤、推送等全部配置 |
| `scripts/send_telegram.py` | Telegram 文件推送脚本 |

---

## 信息来源一览

### RSS 订阅（12 个）

**中国政治/经济/社会（多方视角）：**

| 来源 | 视角 | 分类 |
|------|------|------|
| South China Morning Post | 香港/中立偏商业 | china-news |
| Reuters China | 国际通讯社/中立客观 | china-news |
| BBC News China | 英国/西方视角 | china-news |
| The Guardian China | 英国/偏自由派 | china-news |
| Nikkei Asia China | 日本/亚洲经济视角 | china-news |
| FT China | 金融时报/经济深度 | china-economy |
| Bloomberg Markets | 美国/财经市场视角 | china-economy |

**科技/AI：**

| 来源 | 说明 | 分类 |
|------|------|------|
| Simon Willison | AI 工具/LLM 深度博客 | ai-tools |
| The Verge | 科技综合新闻 | tech-news |
| Ars Technica | 深度科技报道 | tech-news |
| TechCrunch | 创业/科技产业 | tech-news |
| MIT Technology Review | 前沿技术评论 | tech-news |

### Reddit（8 个子版块）

| 子版块 | 方向 | 最低分数 |
|--------|------|----------|
| r/China | 中国相关讨论 | 30 |
| r/geopolitics | 地缘政治 | 50 |
| r/worldnews | 世界新闻 | 200 |
| r/economics | 经济学/宏观经济 | 50 |
| r/MachineLearning | 机器学习学术 | 50 |
| r/LocalLLaMA | 本地大模型 | 30 |
| r/technology | 科技综合 | 100 |
| r/programming | 编程/开发 | 50 |

### Hacker News

- Top 30 stories，最低分数 100

### Telegram 频道

| 频道 | 状态 |
|------|------|
| @aigaboratory | ✅ 启用 |
| @OpenAINewsDaily | ✅ 启用 |

### GDELT 全球新闻事件

- 查询：`China economy OR China politics OR China trade OR China technology OR artificial intelligence`
- 最多 75 条

### Google News 搜索

- 查询：`China economy politics OR AI technology`
- 最多 50 条

### OSS Insight（GitHub 趋势）

- 时间窗口：过去 24 小时
- 语言筛选：All / Python / TypeScript / Rust
- 最少 50 stars 增长
- 最多 20 条

---

## AI 评分与过滤

| 参数 | 值 |
|------|-----|
| 评分阈值 | ≥ 6.0（满分 10） |
| 时间窗口 | 24 小时 |
| 评分标准 | 9-10 突破性 / 7-8 高价值 / 5-6 有趣 / 3-4 低优先 / 0-2 噪音 |
| 节流 | 每条间隔 2 秒 |
| 并发 | 评分 1 / 丰富 1 |

---

## Telegram 推送

通过 `scripts/send_telegram.py` 将生成的 Markdown 报告转为 HTML 文件发送到 Telegram，支持：

- 目录点击跳转到对应条目
- 美观的排版样式
- 三语文件分别发送
- 无消息长度限制

**所需环境变量（.env）：**

```env
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_CHAT_ID=your-chat-id
```

---

## 输出目录

| 路径 | 内容 |
|------|------|
| `data/summaries/` | 每日 Markdown 报告原文 |
| `docs/_posts/` | GitHub Pages 发布用副本 |

文件命名格式：`horizon-YYYY-MM-DD-{lang}.md`

---

## 未启用的来源

以下来源已配置但未启用，需要额外 API Key：

| 来源 | 要求 |
|------|------|
| Twitter | 需要 Apify Token（$5/月免费额度） |
| OpenBB | 需要对应金融数据 provider 账号 |
| GitHub | 可选，提高 rate limit 需 GitHub Token |

---

## 相关文档

- [Horizon 官方配置指南](https://github.com/Thysrael/Horizon/blob/main/docs/configuration.md)
- [Horizon GitHub 仓库](https://github.com/Thysrael/Horizon)
