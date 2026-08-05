---
layout: default
title: "Horizon Summary: 2026-08-05 (ZH)"
date: 2026-08-05
lang: zh
---

> 从 182 条内容中筛选出 35 条重要资讯。

---

1. [Keyv 及相关 npm 包遭 Shai-Hulud 供应链攻击](#item-1) ⭐️ 8.0/10
2. [德州因需求激增暂停数据中心电网连接](#item-2) ⭐️ 8.0/10
3. [黑客利用 Coldcard 漏洞窃取超 1.3 亿美元加密货币](#item-3) ⭐️ 8.0/10
4. [慕尼黑市政府资助 libexpat XML 解析库 6 个月休假项目](#item-4) ⭐️ 7.0/10
5. [Mistral 发布 Shieldstral：用于多模态内容审核的开源 3B 模型](#item-5) ⭐️ 7.0/10
6. [用于生成多样化肤色的简单算法与色彩空间](#item-6) ⭐️ 7.0/10
7. [DeepSeek V4 Flash 成功运行于单卡 AMD MI300X](#item-7) ⭐️ 7.0/10
8. [感谢 FedEx，这就是我们不断遭遇网络钓鱼的原因](#item-8) ⭐️ 7.0/10
9. [美国 AI 领袖青睐中国开源模型，挑战安全论调](#item-9) ⭐️ 7.0/10
10. [美国强制劳动关税压力下智利向中国靠拢](#item-10) ⭐️ 7.0/10
11. [特朗普政府拟禁止中国数据中心设备进口](#item-11) ⭐️ 7.0/10
12. [PipeNetwork/minimax-h3-mlx](#item-12) ⭐️ 7.0/10
13. [AMD 数据中心收入因 AI 需求激增 107%](#item-13) ⭐️ 7.0/10
14. [SpaceX AI 部门收入达 26 亿美元](#item-14) ⭐️ 7.0/10
15. [Telegram CEO 称勒索者植入儿童色情内容致应用被下架](#item-15) ⭐️ 7.0/10
16. [Anthropic 与 AI 云初创公司 Volta 签署 100 亿美元协议](#item-16) ⭐️ 7.0/10
17. [英伟达开放安全 AI 联盟已推出安全提案](#item-17) ⭐️ 7.0/10
18. [Waymo 取消达拉斯 Robotaxi 服务等待名单](#item-18) ⭐️ 7.0/10
19. [Spotify 与 Merlin 合作扩展 AI 音乐混音工具](#item-19) ⭐️ 7.0/10
20. [苹果称更多前员工可能将机密数据带往 OpenAI](#item-20) ⭐️ 7.0/10
21. [Hugging Face CEO：中国领跑开源权重 AI 竞赛](#item-21) ⭐️ 7.0/10
22. [中国成立世界人工智能合作组织](#item-22) ⭐️ 7.0/10
23. [Gwern 放弃匿名写作，推出 Guardian Angel AI 项目](#item-23) ⭐️ 6.0/10
24. [Oxide Computer 完成 4.45 亿美元 D 轮融资](#item-24) ⭐️ 6.0/10
25. [中国 MiniMax 因版权问题限制海外访问 H3 视频模型](#item-25) ⭐️ 6.0/10
26. [中国初创公司涉嫌操纵机器人基准测试超越英伟达](#item-26) ⭐️ 6.0/10
27. [中国芯片设备商 AMEC 利润近翻四倍，需求激增](#item-27) ⭐️ 6.0/10
28. [AI 奠基优化算法之父 Nesterov 荣获应用数学顶级奖项](#item-28) ⭐️ 6.0/10
29. [LLM 0.32 新增推理轨迹、OpenAI Responses API 及服务端工具](#item-29) ⭐️ 6.0/10
30. [宽带拨款恢复，但种族标准被法官裁定违宪](#item-30) ⭐️ 6.0/10
31. [EFF 警告 Android 应用可能通过第三方 SDK 共享用户位置数据](#item-31) ⭐️ 6.0/10
32. [开源权重 AI 模型逼近前沿性能，安全差距依然存在](#item-32) ⭐️ 6.0/10
33. [下载：美国机器人限制与 ICE 的 DNA 采集扩张](#item-33) ⭐️ 6.0/10
34. [世界银行：发展中国家从 AI 获益更多、损失更少](#item-34) ⭐️ 6.0/10
35. [美国竞逐廉价 AI 替代中国方案](#item-35) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Keyv 及相关 npm 包遭 Shai-Hulud 供应链攻击](https://www.aikido.dev/blog/keyv-and-friends-compromised-in-npm-supply-chain-attack) ⭐️ 8.0/10

广泛使用的 Keyv npm 包及多个相关包在活跃的 Shai-Hulud 供应链攻击中被劫持，该攻击已通过利用预安装钩子传播至约 600 个 npm 包。 此次攻击凸显了 npm 依赖系统的脆弱性，因为带有预安装钩子的被劫持包可在安装时自动执行恶意代码，可能影响数千个下游项目并泄露敏感凭证。 Shai-Hulud 蠕虫通过被劫持包添加的预安装钩子传播，在 npm install 期间执行恶意负载。检测工具如 Packj 通过分析代码行为（如生成 shell 或使用 SSH 密钥）来识别被劫持状态，开发者建议使用 devcontainers 隔离依赖安装。

hackernews · cimi_ · 8月4日 11:01 · [社区讨论](https://news.ycombinator.com/item?id=49166874)

**背景**: npm 是 JavaScript 的默认包管理器，开发者在此发布和安装开源包。供应链攻击发生在恶意代码被注入受信任的包中，通常通过劫持维护者账户或仿冒包名实现。预安装钩子是包安装前自动运行的脚本，可能被利用来执行任意代码。Shai-Hulud 蠕虫是近期利用这些钩子在 npm 生态系统中传播的活动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.codeant.ai/blogs/shai-hulud-npm-supply-chain-attack">Shai - Hulud npm Supply Chain Attack</a></li>
<li><a href="https://www.linkedin.com/posts/tobyvandegrift_shai-hulud-post-mortem-a-call-to-action-activity-7417833048756502529-Lhnv">Shai - hulud : Warning on npm Supply - Chain Attack | LinkedIn</a></li>

</ul>
</details>

**社区讨论**: 社区情绪担忧，开发者呼吁暂停新增预安装钩子并指出 npm 依赖系统的固有漏洞。多位贡献者推荐缓解策略，如使用 devcontainers 进行隔离，以及利用 Packj 等工具通过行为分析检测被劫持的包。

**标签**: `#supply-chain-security`, `#npm`, `#cybersecurity`, `#open-source`, `#dependency-management`

---

<a id="item-2"></a>
## [德州因需求激增暂停数据中心电网连接](https://arstechnica.com/ai/2026/08/texas-halts-data-center-connections-to-power-grid-amid-overwhelming-demand/) ⭐️ 8.0/10

德州因需求激增已暂停新的数据中心电网连接申请，这与州长此前将德州定位为 AI“中心”的说法相矛盾。ERCOT 电网互联队列现已包含超过 1,800 个项目，代表超过 474 吉瓦的连接请求。 这标志着 AI 扩张与能源电网容量交叉领域的重要政策和基础设施发展，对该行业的数据中心增长和 AI 基础设施规划具有重大影响。 474 吉瓦的互联队列代表德州创纪录峰值电力需求的五倍多，其中约 90%的请求来自数据中心。在许多地区，互联等待时间现已超过五年。

rss · Ars Technica · 8月4日 20:34

**背景**: ERCOT（德州电力可靠性委员会）管理德州大部分地区的电网，处理寻求电网接入的新设施互联请求。新 AI 数据中心发展的最大限制因素已不再是土地或资本，而是电网电力接入，在许多地区互联等待时间已超过五年。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/08/texas-halts-data-center-connections-to-power-grid-amid-overwhelming-demand/">Texas halts data center connections to power grid amid overwhelming demand - Ars Technica</a></li>
<li><a href="https://www.utilitydive.com/news/ercots-large-load-queue-jumped-almost-300-last-year-official/808820/">ERCOT’s large load queue jumped almost 300% last year | Utility Dive</a></li>
<li><a href="https://www.hanwhadatacenters.com/blog/data-center-grid-limitations-the-power-bottleneck/">Data Center Grid Limitations: The Power Bottleneck</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#energy policy`, `#data centers`, `#Texas`, `#power grid`

---

<a id="item-3"></a>
## [黑客利用 Coldcard 漏洞窃取超 1.3 亿美元加密货币](https://techcrunch.com/2026/08/04/hackers-steal-over-130-million-by-exploiting-bug-in-offline-hardware-wallets/) ⭐️ 8.0/10

Coldcard 硬件钱包的固件漏洞削弱了用于种子生成的随机数生成器，黑客利用该漏洞窃取了超过 1.3 亿美元的比特币。 此次漏洞意义重大，因为 Coldcard 是一款以安全著称的热门硬件钱包，该漏洞表明固件漏洞可能危及离线设备，削弱了用户对加密货币安全解决方案的信任。 该漏洞影响五个 Coldcard 型号，攻击者可通过利用固件中受损的随机数生成器来重建受害者的私钥，而无需物理接触设备。

rss · TechCrunch · 8月4日 16:27

**背景**: 硬件钱包是旨在离线存储加密货币私钥的物理设备，提供安全的'冷'存储解决方案。它们在内部生成和签署交易，使私钥与联网设备隔离。Coldcard 是该领域知名的品牌，以其安全功能著称。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/coldcard-hardware-wallet-rng-flaw-bitcoin-theft/">Coldcard Hardware Wallet RNG Flaw Linked to $88.6 Million Bitcoin Theft</a></li>
<li><a href="https://www.techtimes.com/articles/322392/20260731/coldcard-hardware-wallet-hacked-via-firmware-bug-that-bypassed-rng-five-years.htm">Coldcard Hardware Wallet Hacked via Firmware Bug That Bypassed RNG for ...</a></li>
<li><a href="https://thehackernews.com/2026/08/coldcard-hardware-wallet-flaw-linked-to.html">Coldcard Hardware Wallet Flaw Linked to $70 Million Bitcoin Theft in 41 ...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#cryptocurrency`, `#hardware-wallets`, `#vulnerability`

---

<a id="item-4"></a>
## [慕尼黑市政府资助 libexpat XML 解析库 6 个月休假项目](https://blog.hartwork.org/posts/libexpat-city-of-munich-open-source-sabbatical/) ⭐️ 7.0/10

慕尼黑市政府通过其开源休假计划，资助 libexpat（一款广泛使用的 C 语言 XML 解析库）长达 6 个月的开源开发工作。该计划不仅面向市政府员工，也向外部软件开发者开放。 这代表了一种有趣的开源可持续性模式，即市政府直接资助关键基础设施库维护者的休假开发。此举可能激励其他市政机构和组织采用类似计划，以支持重要的开源项目。 开源休假计划允许具备专业资格的开发者在限定时间内专注于改进开源项目。libexpat 是一款由 James Clark 于 1997 年发起的流式 C 语言 XML 解析库，被众多应用、库和硬件项目所使用。

hackernews · spyc · 8月4日 23:18 · [社区讨论](https://news.ycombinator.com/item?id=49176606)

**背景**: libexpat 是全球部署最广泛的 XML 解析库之一，采用 C 语言编写，以速度和流式处理能力著称。开源休假计划是一种让开发者暂时离开日常工作、全职投入改进开源项目的机制，Ruby/Rails 等公司及各类社区倡议曾探索过这一模式。慕尼黑此前曾推行 LiMux 项目，将公共行政系统迁移至 Linux，但后来被放弃。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://libexpat.github.io/">Welcome to Expat! · Expat XML parser</a></li>
<li><a href="https://github.com/libexpat/libexpat">GitHub - libexpat / libexpat : :herb: Fast streaming XML parser written...</a></li>

</ul>
</details>

**社区讨论**: 社区评论提到了慕尼黑在 LiMux Linux 迁移项目上的历史，并对休假计划向外部开发者开放表示赞赏。部分讨论还涉及了 libxml2 维护者更替的相关话题，而其他评论则偏离到了与 Google 和 XSLT 相关的边缘话题。

**标签**: `#open source`, `#libexpat`, `#government funding`, `#sustainability`, `#XML`

---

<a id="item-5"></a>
## [Mistral 发布 Shieldstral：用于多模态内容审核的开源 3B 模型](https://mistral.ai/news/shieldstral/) ⭐️ 7.0/10

Mistral 发布了 Shieldstral，这是一个 30 亿参数的开源多模态模型，专为内容审核设计，支持基于提示的策略定制，允许开发者通过自然语言指令定制审核规则。 这一发布解决了 AI 驱动平台对可扩展、灵活内容审核的关键需求，提供了一个开源权重解决方案，减少了对封闭专有模型的依赖，并使开发者能够以更低的成本和更高的透明度实施自定义策略执行。 该模型为 30 亿参数、开源权重、多模态，支持基于提示的策略定制，其中审核规则以自然语言提示形式编码；它已在 Hugging Face 上提供，针对图像分享和社交平台等用例。

hackernews · riadsila · 8月4日 16:36 · [社区讨论](https://news.ycombinator.com/item?id=49171268)

**背景**: 开源权重 AI 模型为开发者提供了访问模型权重的途径，使其能够集成到自定义项目中，并与 ChatGPT 等封闭模型相比提高了透明度。基于提示的策略定制（或称“策略即提示”）涉及将内容审核指南直接编码为大型语言模型中的自然语言提示，允许在不重新训练的情况下灵活调整规则。随着平台寻求成本效益高、适应性强的审核解决方案，这种方法正日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/mit-csail_what-are-open-weights-ai-models-why-are-activity-7358606381521747969-k_Hd">What are open - weights AI models and why do they matter? | LinkedIn</a></li>
<li><a href="https://arxiv.org/html/2502.18695v1">Policy-as-Prompt: Rethinking Content Moderation in the Age of Large Language Models</a></li>

</ul>
</details>

**社区讨论**: 社区讨论突出显示了对模型处理标准审核风格之外任意规则集能力的 curiosity，对现实世界边缘案例的怀疑，以及对 Mistral 专注于针对特定用例的小型微调模型的策略的认可。

**标签**: `#AI/ML`, `#Content Moderation`, `#Open Weights`, `#Mistral`, `#Multimodal Models`

---

<a id="item-6"></a>
## [用于生成多样化肤色的简单算法与色彩空间](https://toneyalexander.github.io/inclusive-color-space/) ⭐️ 7.0/10

一位开发者创建了一个自定义色彩空间和程序化生成算法，使数字艺术和游戏开发中更容易选择合理且多样化的肤色。该工具包含基于 JavaScript 的颜色选择器和一个 Python 程序化生成算法，通过在球体内均匀采样来生成逼真的肤色。 这解决了数字艺术和游戏开发中的一个重要包容性问题，创作者常常难以准确表现多样化的肤色。这种方法可以帮助开发者和艺术家在各种媒体中创建更真实、更具代表性的数字角色。 该算法使用自定义色彩空间，在球体内均匀采样可产生随机肤色，在较低半径值时保持真实感。该方法论承认局限性并包含未来工作部分，作者表示方法可能有些粗糙但结果很有帮助。

hackernews · automatoney · 8月4日 15:16 · [社区讨论](https://news.ycombinator.com/item?id=49170165)

**背景**: 色彩空间是基于坐标系统组织的三维模型，每个维度代表不同的颜色属性，如色相、饱和度或亮度。肤色表现在计算机图形学中一直是个长期挑战，现有方法如 Pantone 肤色色系和数据驱动分析将肤色映射到 Oklab 等感知色彩空间中，通常呈现独特的月牙形分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://toneyalexander.github.io/inclusive-color-space/">What Colors Are We? Constructing A Color Space For Skin Tones</a></li>
<li><a href="https://news.lavx.hu/article/new-color-space-aims-to-make-digital-skin-tone-representation-more-inclusive">New Color Space Aims to Make Digital Skin Tone ... | LavX News</a></li>
<li><a href="https://en.wikipedia.org/wiki/Color_space">Color space - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞这项工作很出色，认为函数拟合方法很巧妙，有人建议 PCA 可以简化选择器。其他人指出缺少对 Pantone 肤色色系等现有工作的引用，并分享了相关研究，还有一位评论者提到将肤色图像饱和度调至 100%会产生橙色结果——这是某些人脸识别器使用的原理。

**标签**: `#color-science`, `#game-development`, `#inclusivity`, `#procedural-generation`, `#digital-art`

---

<a id="item-7"></a>
## [DeepSeek V4 Flash 成功运行于单卡 AMD MI300X](https://github.com/ryanzhou/deepseek-v4-flash-mi300x) ⭐️ 7.0/10

DeepSeek V4 Flash 已成功部署在单张 AMD MI300X GPU 上，在保留完整推理权重的情况下实现了每秒 150+ 个 token 的速度，但上下文窗口从 100 万缩减至 25.6 万 token。 这一成果证明了大规模混合专家模型可以在单张 AMD 数据中心 GPU 上实用运行，提供了更便捷的部署方案，并增强了 AMD 在与 NVIDIA 的 AI 推理市场竞争中的地位。 2840 亿参数的 DeepSeek V4 Flash 模型采用原生 MXFP4 量化，在 MI300X 的 192GB HBM 上以每秒 150+ token 的速度运行，上下文窗口为 25.6 万而非完整的 100 万。

hackernews · zhoutong · 8月4日 10:00 · [社区讨论](https://news.ycombinator.com/item?id=49166386)

**背景**: DeepSeek V4 Flash 是一个效率优化的混合专家（MoE）语言模型，拥有 2840 亿总参数，但每个 token 仅激活 130 亿参数，支持 100 万 token 的上下文窗口。AMD Instinct MI300X 是一款数据中心 GPU，配备 192GB HBM 内存，旨在与 NVIDIA 的产品在 AI 推理工作负载中竞争。上下文窗口是指模型在单次请求中能够处理的最大 token 数量，以 token 而非单词或字符为单位衡量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V 4 Flash - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://flopper.io/compare/amd-mi300x-192gb-vs-nvidia-b200-sxm-192gb">AMD Instinct MI 300 X vs NVIDIA B200 - GPU Comparison | Flopper.io</a></li>
<li><a href="https://www.morphllm.com/llm-context-window">What Is an LLM Context Window ? The Developer's Guide (2026)</a></li>

</ul>
</details>

**社区讨论**: 社区指出 MI300X 通常以 8 卡机箱形式出售，价格约 25 万欧元，而非单卡销售，并提及 MI350P 作为 144GB 显存的 PCIe 卡替代方案。有人讨论了 DwarfStar 和 DoubleWord AI 的 2xMI300X 部署等 prior work，也有人称赞了以缩减上下文窗口换取单卡可用性的实用权衡。

**标签**: `#AI/ML`, `#LLM inference`, `#GPU hardware`, `#model optimization`, `#DeepSeek`

---

<a id="item-8"></a>
## [感谢 FedEx，这就是我们不断遭遇网络钓鱼的原因](https://www.troyhunt.com/thanks-fedex-this-is-why-we-keep-getting-phished/) ⭐️ 7.0/10

安全研究员 Troy Hunt 分析了合法公司的做法（如 FedEx 从个人邮箱发送带有 PDF 附件的普通邮件）如何模糊了真实邮件与恶意邮件之间的界限，从而加剧了网络钓鱼问题。 这一分析揭示了一个系统性问题：组织因采用使用户难以区分合法通信与诈骗邮件的邮件实践，无意中助长了网络钓鱼，影响了各行业的网络安全意识工作。 文章讨论了域名欺骗技术和社交工程攻击手段，社区成员分享了多个真实案例，包括可疑的海关通知、使用欺骗性子域名（如 c.gle）的云端存储诈骗邮件，以及泛滥的.xyz 等新型通用顶级域名给钓鱼检测带来的困难。

hackernews · stymaar · 8月4日 21:09 · [社区讨论](https://news.ycombinator.com/item?id=49175192)

**背景**: 网络钓鱼是一种网络攻击技术，诈骗者伪装成可信实体以窃取登录凭证或财务数据等敏感信息。域名欺骗涉及创建模仿合法组织的虚假网站或电子邮件地址，使用户难以识别恶意通信。SPF、DKIM 和 DMARC 等邮件认证协议有助于验证发件人身份，但许多组织仍依赖非正式的邮件实践，削弱了这些安全措施的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.island.io/phishing/browser-extension-security-defending-against-domain-spoofing">Phishing attacks: Defending against domain spoofing</a></li>
<li><a href="https://www.crowdstrike.com/en-us/cybersecurity-101/social-engineering/spoofing-attack/">What is Spoofing ? Spoofing Attacks Defined | CrowdStrike</a></li>
<li><a href="https://www.getresponse.com/blog/email-authentication">How to Authenticate Your Emails : SPF , DKIM , DMARC , and BIMI</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了多个真实网络钓鱼案例，包括 FedEx 从个人邮箱发送带有 PDF 附件的海关通知，以及使用欺骗性子域名 c.gle 的 Google 存储诈骗。大家普遍认为，由于令人困惑的邮件实践和.xyz 等冷门顶级域名的泛滥，非技术用户正面临越来越大的风险。

**标签**: `#cybersecurity`, `#phishing`, `#social-engineering`, `#security-awareness`

---

<a id="item-9"></a>
## [美国 AI 领袖青睐中国开源模型，挑战安全论调](https://www.scmp.com/news/us/article/3362974/us-ai-leaders-turn-chinese-open-weight-models-challenging-closed-source-safety-claims?utm_source=rss_feed) ⭐️ 7.0/10

包括吴恩达在内的美国知名 AI 人物公开表示，中国开源模型比闭源模型更安全，直接挑战了 Anthropic 长期以来的安全论调。这一转变反映出业界对 Kimi K3 和 GLM-5.2 等中国模型的依赖日益增加，这些模型正缩小与美国前沿系统的性能差距。 这一发展挑战了 Anthropic 等公司推广的闭源安全论调，可能影响围绕开放与专有模型的 AI 政策辩论。它标志着业界在评估 AI 安全方面的潜在重新定位，对监管和开源运动具有深远影响。 据 AI 安全非营利组织 SaferAI 报告，中国开源模型 GLM-5.2 在能力上现已落后于 GPT-5.5 和 Claude Opus 4.7 等美国前沿模型仅数月之遥。这些模型在 OpenRouter 等平台上占据了大部分 API 流量，230 多家公司签署了排除 Anthropic 的开源 AI 宣言。

rss · South China Morning Post · 8月4日 16:08

**背景**: 开源 AI 模型允许公众检查和修改模型权重，与底层架构专有的闭源系统形成对比。开放与闭源 AI 的辩论核心在于，透明度是通过社区审查提高安全性，还是因不受限制的使用而带来风险。中国 AI 实验室近期发布了接近前沿水平的开源模型，在生产环境中日益受到青睐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scmp.com/tech/tech-war/article/3361142/why-chinas-open-weight-ai-model-kimi-k3-sparking-anxiety-silicon-valley">Why China ’s open - weight AI model Kimi K3 is sparking anxiety in...</a></li>
<li><a href="https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/">Open - weight AI models are catching up to the frontier. | TechCrunch</a></li>
<li><a href="https://shaam.blog/articles/anthropic-left-out-open-weight-ai-letter-2026">Anthropic Left Out as 230+ Companies Sign the Open - Weight AI ...</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Open Source AI`, `#AI Policy`, `#Chinese AI`, `#Open-Weight Models`

---

<a id="item-10"></a>
## [美国强制劳动关税压力下智利向中国靠拢](https://www.scmp.com/news/china/diplomacy/article/3362614/cuban-spy-base-allegations-new-trump-tariffs-7-latin-america-relations-reads?utm_source=rss_feed) ⭐️ 7.0/10

智利总统何塞·安东尼奥·卡斯蒂略在拉莫内达宫与中国驻圣地亚哥大使牛庆宝进行了超过一小时的会晤，这是双方首次会面。这一外交举动发生在美国对智利出口商品征收强制劳动关税的第二天。 智利向中国靠拢的外交转向表明，随着各国在美国关税压力升级之际寻求多元化贸易伙伴关系，拉丁美洲正在发生战略调整。这一举动反映了美在中地缘政治竞争已延伸至西半球，可能重塑区域贸易格局。 美国强制劳动关税源于 2021 年通过的《维吾尔强迫劳动预防法》，该法禁止进口来自中国新疆地区的商品，除非企业能证明这些商品未使用强迫劳动制造。美国贸易代表贾米森·格里尔表示，贸易伙伴应采取类似的强制劳动进口禁令。

rss · South China Morning Post · 8月4日 14:00

**背景**: 《维吾尔强迫劳动预防法》于 2021 年颁布，确立了可反驳的推定，即所有在中国新疆地区生产的商品均使用强迫劳动制造，实际上禁止其进口到美国，除非进口商能提供明确令人信服的证据予以反驳。智利和中国自 2005 年以来一直保持着双边自由贸易协定，两国贸易团体签署的谅解备忘录进一步巩固了水果贸易合作。美国已有近一个世纪的强制劳动进口禁令，最近已将执法范围扩大到中国以外的更多国家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.adn.com/nation-world/2026/07/26/a-forced-labor-crackdown-or-an-end-run-around-congress-dissecting-trumps-new-tariffs/">A forced - labor crackdown or an end-run around Congress?</a></li>
<li><a href="https://www.timeslive.co.za/news/world/2026-07-24-trump-imposes-double-digit-tariffs-on-dozens-of-countries/">Trump imposes double-digit tariffs on dozens of countries</a></li>
<li><a href="https://www.scmp.com/economy/china-economy/article/3094425/china-chile-mou-deepens-trade-ties-beijing-looks-cement">China - Chile MOU deepens trade ties as Beijing looks to cement...</a></li>

</ul>
</details>

**标签**: `#Latin America`, `#US-China relations`, `#trade policy`, `#geopolitics`, `#Chile`

---

<a id="item-11"></a>
## [特朗普政府拟禁止中国数据中心设备进口](https://www.theguardian.com/technology/2026/aug/04/fcc-ban-china-datacenter-devices) ⭐️ 7.0/10

据报道，特朗普政府的联邦通信委员会（FCC）正在起草一项措施，禁止美国进口中国新型光学收发器——这是光纤数据中心网络中的关键组件。据路透社报道，官员们希望今年内公布该措施。 这项拟议中的禁令可能大幅重塑 AI 基础设施供应链，标志着中美科技紧张关系的重大升级。它直接影响 AI 发展的数据中心硬件采购，可能迫使美国公司寻找替代供应商或增加国内生产。 光学收发器将电信号转换为光信号，用于数据中心内光纤电缆的高速数据传输。该禁令专门针对中国设备的新型号，而非现有库存，并聚焦于 AI 计算基础设施所需的关键组件。

rss · The Guardian China · 8月4日 17:21

**背景**: 光学收发器是数据中心中通过光纤电缆以光速传输数据的关键网络组件。它们对 AI 基础设施尤为重要，因为在大型计算集群中，海量数据必须在 GPU 和服务器之间快速传输。由于具有竞争力的制造成本和规模，中国已成为这些组件的主要供应商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://geneo.app/query-reports/fiber-optic-transceivers-data-centers">Fiber Optic Transceivers for Data Centers Guide | Geneo</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#US-China Tech Policy`, `#Datacenter Hardware`, `#Semiconductors`, `#FCC Regulation`

---

<a id="item-12"></a>
## [PipeNetwork/minimax-h3-mlx](https://simonwillison.net/2026/Aug/4/minimax-h3-mlx/#atom-everything) ⭐️ 7.0/10

Simon Willison 分享了一个 Python 包，将 MiniMax 全新的全模态生成模型移植到 MLX，支持在 Apple Silicon 硬件上进行文本、图像、音频和视频生成。

rss · Simon Willison · 8月4日 19:10

**标签**: `#MLX`, `#Apple Silicon`, `#Multimodal AI`, `#Open Source Models`, `#Video Generation`

---

<a id="item-13"></a>
## [AMD 数据中心收入因 AI 需求激增 107%](https://www.theverge.com/tech/975381/amd-q2-2026-earnings-ai-gaming-ryzen) ⭐️ 7.0/10

AMD 在 2026 年第二季度数据中心收入达 67 亿美元，同比增长 107%，从 32 亿美元跃升，主要受 AI 算力需求激增推动。随着公司 AI 驱动的数据中心业务加速，游戏业务增长相对放缓。 这一财报结果凸显了 AMD 向 AI 基础设施的成功转型，在蓬勃发展的数据中心 GPU 市场直接与英伟达竞争。同比增长 107%表明 AMD 的 Instinct AI 加速器在企业端获得强劲采用，并重塑了半导体收入格局。 数据中心收入从 2026 年第一季度的 58 亿美元环比增长，CEO 苏姿丰在财报电话会上讨论了这一增长。游戏业务相对放缓与数据中心繁荣形成对比，反映出需求向 AI 工作负载转移。

rss · The Verge · 8月4日 20:57

**背景**: AMD 的数据中心业务包括 AI 加速器（Instinct 系列）、服务器 CPU（EPYC）以及服务构建 AI 基础设施的云提供商和企业的自适应计算产品。半导体行业在 AI 芯片领域竞争激烈，英伟达占据市场主导地位，但 AMD 通过更具竞争力的定价和软件生态改进正在提升市场份额。

**标签**: `#AMD`, `#AI`, `#earnings`, `#data center`, `#semiconductors`

---

<a id="item-14"></a>
## [SpaceX AI 部门收入达 26 亿美元](https://www.theverge.com/science/975335/spacex-made-more-money-as-a-neocloud) ⭐️ 7.0/10

SpaceX 的 AI 部门收入达 26 亿美元，是前一年的三倍以上，主要来自与 Anthropic 和 Google 的算力协议。随着公司准备上市，AI 已成为其最大收入来源。 这标志着 SpaceX 在传统航天业务之外实现了重大多元化，使其成为 AI 基础设施市场的主要参与者，与 CoreWeave 等竞争对手同台竞技。这表明太空公司正在利用其大规模数据中心投资来满足蓬勃发展的 AI 算力需求。 SpaceX 的 AI 部门包括位于孟菲斯的 Colossus 超级计算机，提供超过 300 兆瓦的算力和 22 万块以上 NVIDIA GPU。公司分为三个业务板块：航天、AI 和连接（Starlink），AI 协议分别于 2025 年 5 月和 6 月签署。

rss · The Verge · 8月4日 20:47

**背景**: 新云（Neocloud）是一代专注于高性能 AI 算力的云基础设施提供商，通常围绕专用 GPU 集群构建。SpaceX 在数据中心基础设施上投入巨资，包括孟菲斯的 Colossus 设施，以满足日益增长的 AI 训练和推理需求。公司的传统收入主要来自火箭发射和 Starlink 卫星互联网服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/science/975335/spacex-made-more-money-as-a-neocloud">SpaceX made more revenue as an AI company than... | The Verge</a></li>
<li><a href="https://techcrunch.com/2026/08/04/spacex-doubles-revenues-on-anthropic-and-google-compute-deals-starlink-growth/">SpaceX doubles revenue on Anthropic and Google compute deals ...</a></li>

</ul>
</details>

**标签**: `#AI Infrastructure`, `#SpaceX`, `#Cloud Computing`, `#Industry News`, `#Revenue`

---

<a id="item-15"></a>
## [Telegram CEO 称勒索者植入儿童色情内容致应用被下架](https://www.theverge.com/tech/975300/telegram-app-store-takedown-extortion-pavel-durov) ⭐️ 7.0/10

Telegram CEO Pavel Durov 声称勒索者在公共聊天中植入了儿童性虐待材料(CSAM)，导致应用被暂时从苹果 App Store 下架。Durov 表示苹果在联系公司之前就移除了 Telegram，这造成了系统性风险。 此事件凸显了 App Store 内容审核政策的漏洞，引发了对自动化下架流程的质疑。它还展示了恶意行为者如何利用平台安全机制进行勒索。 Durov 表示苹果在联系他们之前就移除了 Telegram，他认为这是一个潜在的系统性风险。事件发生在周一晚上，据称在公共聊天中植入了 CSAM 以触发 App Store 政策违规。

rss · The Verge · 8月4日 19:11

**背景**: CSAM（儿童性虐待材料）是非法内容，会触发各大平台的立即下架。苹果已实施 CSAM 检测系统，特别是针对 iCloud Photos，以识别和报告此类材料。移动应用开发者必须拥有应用内报告机制和指定的儿童安全官员以符合平台政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://9to5mac.com/guides/csam/">CSAM : Apple's efforts to detect Child Sexual Abuse Materials - 9to5Mac</a></li>
<li><a href="https://www.kaspersky.com/blog/what-is-apple-csam-detection/41502/">Apple plans to use CSAM Detection to monitor... | Kaspersky official blog</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#App Store`, `#Content Moderation`, `#Cybersecurity`, `#Platform Policy`

---

<a id="item-16"></a>
## [Anthropic 与 AI 云初创公司 Volta 签署 100 亿美元协议](https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/) ⭐️ 7.0/10

Anthropic 据报道与 AI 云初创公司 Volta 签署了 100 亿美元的云合作伙伴关系协议，延续了其近期的云合作热潮。据彭博社报道，该协议为期六年。 该协议凸显了 AI 云基础设施的激烈竞争，并强调了为领先 AI 开发商确保长期计算能力的重要性。它标志着 AI 基础设施和云交易的重大转变。 Volta 由 Ricard Boada 和 Sofia Gumuzio 于今年早些时候创立，获得 Nvidia 和 Dell 支持，估值 24 亿美元，协议为期六年。

rss · TechCrunch · 8月4日 19:48

**背景**: AI 公司正越来越多地确保长期云合作伙伴关系，以扩展其模型并满足不断增长的计算需求。Volta 是一家从隐身模式走出的 AI 原生云初创公司，专注于为 AI 工作负载提供高性能云基础设施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/04/anthropic-signs-10-billion-deal-with-ai-cloud-startup-volta/">Anthropic signs $10B deal with AI cloud startup Volta | TechCrunch</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-04/nvidia-dell-back-ai-cloud-startup-volta-at-2-4-billion-value">Nvidia, Dell Back AI Cloud Startup Volta at $2.4 Billion... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cloud Infrastructure`, `#Business Deals`, `#Anthropic`

---

<a id="item-17"></a>
## [英伟达开放安全 AI 联盟已推出安全提案](https://techcrunch.com/2026/08/04/nvidia-doesnt-mess-around-a-week-after-open-ai-industry-group-formed-its-already-showing-progress/) ⭐️ 7.0/10

英伟达新成立的开放安全 AI 联盟在成立仅一周后，便已发布了针对 AI 智能体威胁的防御提案，目前已有超过 120 家成员公司参与。英伟达正在贡献开源模型、模型权重、数据以及其新的 NOOA（英伟达实验室面向对象智能体）项目，以加速网络安全工具的开发。 这一倡议意义重大，因为 AI 智能体正日益嵌入企业应用程序，带来了未经授权数据访问、提示注入攻击和敏感信息泄露等新安全风险。120 多家公司迅速组成联盟，表明业界对开源 AI 安全解决方案的推动势头强劲。 该联盟由 Adobe、CrowdStrike、Hugging Face 和戴尔科技共同创立，是在包括 OpenAI 在内的多家公司签署公开信、倡导开放 AI 模型权重之后成立的。英伟达的 NOOA 项目现已作为开源贡献发布，旨在帮助开发智能体测试框架研究和新的网络安全技术。

rss · TechCrunch · 8月4日 19:28

**背景**: AI 智能体安全是一个新兴领域，主要关注两个方面：保护组织内部部署的自主 AI 智能体，以及利用 AI 智能体提升安全运营效率。最近的高调事件，如 Hugging Face 网络攻击事件，凸显了 AI 系统的脆弱性以及行业协作应对的必要性。推动开放 AI 模型权重的举措旨在促进更广泛的审查和改进 AI 安全机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/open-secure-ai-alliance/">Industry Leaders Join Open Secure AI Alliance for AI ... | NVIDIA Blog</a></li>
<li><a href="https://mezha.net/eng/bukvy/31886e42_nvidia_forms_open/">Nvidia forms Open Secure AI Alliance to share AI safety... - #Mezha</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Industry Alliances`, `#Nvidia`, `#AI Agents`, `#Tech Policy`

---

<a id="item-18"></a>
## [Waymo 取消达拉斯 Robotaxi 服务等待名单](https://techcrunch.com/2026/08/04/waymo-opens-up-robotaxi-service-in-dallas-to-everyone/) ⭐️ 7.0/10

Waymo 已取消达拉斯 Robotaxi 服务的等待名单，允许该市任何人无需提前注册即可预约乘车。这是该公司在美国、英国和欧洲扩大自动驾驶车辆运营的最新一步。 达拉斯是美国前五大的大都市区之一，具有极低密度、高度蔓延和公共交通选择有限的特点——使其成为自动驾驶车辆部署的战略要地。取消等待名单表明 Waymo 已达到足够的运营成熟度和安全信心，能够在具有挑战性的城市环境中大规模服务公众。 达拉斯-沃斯堡以汽车依赖型文化和有限的公共交通而闻名，这使得无人驾驶叫车服务的引入成为一个值得注意的转变。Waymo 进入达拉斯是在旧金山、洛杉矶和其他城市推出服务之后的进一步扩展，该公司正继续向英国和欧洲等国际市场推进。

rss · TechCrunch · 8月4日 17:31

**背景**: Waymo 是 Alphabet Inc.的子公司，是自动驾驶技术的主要开发商之一，运营着全球最先进的 Robotaxi 服务之一。该公司正从其最初的凤凰城试点逐步扩展到美国其他主要城市以及国际市场。Robotaxi 服务采用 L4 级自动驾驶技术，意味着车辆在特定地理区域内可在特定条件下无需人类干预即可运行。

**社区讨论**: 社区情绪总体积极但关注点各异。一些用户称赞 Waymo 在道路上的安全性和可预测性，一位洛杉矶国际机场附近的居民表示其引发的交通事故远少于人类驾驶员。其他人则对机器人出租车收入是否会离开本地社区提出经济担忧，而一位商业地产专业人士则独特地提出，无人驾驶汽车可通过降低交通成本成为有效的可负担住房政策。

**标签**: `#autonomous vehicles`, `#robotaxi`, `#Waymo`, `#self-driving`, `#transportation`

---

<a id="item-19"></a>
## [Spotify 与 Merlin 合作扩展 AI 音乐混音工具](https://techcrunch.com/2026/08/04/spotify-adds-merlin-to-its-ai-music-remix-and-covers-effort/) ⭐️ 7.0/10

Spotify 已与 Merlin 合作，后者代表超过 30,000 家独立厂牌，以扩展其即将推出的 AI 驱动混音和翻唱产品。这一合作建立在与环球音乐集团 (UMG) 现有合作的基础上，并为 AI 生成音乐引入了有偿、自愿参与的框架。 这一发展具有重要意义，因为它将 Spotify 的 AI 音乐计划扩展到独立厂牌，确保艺术家自愿参与、获得署名，并为 AI 生成的翻唱和混音作品获得报酬。它解决了 AI 音乐时代艺术家权利和公平报酬方面的日益关注的担忧，可能为该行业树立先例。 这款付费工具将允许粉丝为参与艺术家的音乐创建 AI 生成的翻唱和混音，同时确保艺术家自愿参与、获得署名和报酬。Merlin 的参与将超过 30,000 家独立厂牌和发行商纳入该框架，与 UMG 一起。

rss · TechCrunch · 8月4日 15:50

**背景**: Merlin 是一家数字音乐发行和授权平台，代表全球的独立厂牌和发行商，帮助他们将音乐投放到流媒体服务。AI 驱动的翻唱和混音使用生成式 AI 创建现有歌曲的新版本，引发了关于版权和艺术家同意的疑问。音乐行业一直在努力如何为 AI 生成的内容补偿艺术家，大型厂牌如 UMG 正在探索自愿授权模式。Spotify 与 UMG 和 Merlin 的合作表明，正在向更全面、基于同意的 AI 音乐方法迈进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://music.loop.fans/blog/merlin-music-distribution">Merlin Music Distribution : A Comprehensive Guide for... | Loop Fans</a></li>
<li><a href="https://toxigon.com/merlin-music-distribution">The Magic of Merlin Music Distribution : Empowering - Toxigon</a></li>

</ul>
</details>

**标签**: `#AI Music`, `#Spotify`, `#Music Industry`, `#AI Remix`, `#Independent Labels`

---

<a id="item-20"></a>
## [苹果称更多前员工可能将机密数据带往 OpenAI](https://techcrunch.com/2026/08/04/apple-says-more-ex-employees-may-have-taken-confidential-data-to-openai/) ⭐️ 7.0/10

苹果对 OpenAI 的贸易秘密调查已扩大，新的法庭文件指控更多前员工可能保留或访问了机密信息。 这场两家领先 AI 公司之间的法律纠纷凸显了在竞争激烈的 AI 竞赛中保护知识产权的重要性，可能影响科技公司如何处理员工离职和数据安全。 这些指控源于苹果持续进行的贸易秘密调查中的新法庭文件，表明前员工潜在的数据保留范围可能超出早期声称。

rss · TechCrunch · 8月4日 14:03

**背景**: 贸易秘密是提供竞争优势的机密商业信息，例如算法、源代码或专有流程。在 AI 行业，快速创新驱动竞争，保护此类秘密至关重要。苹果和 OpenAI 都是 AI 领域的主要参与者，苹果正在开发自己的 AI 模型，而 OpenAI 则以 ChatGPT 等产品领先。

**标签**: `#AI`, `#Legal`, `#Trade Secrets`, `#Apple`, `#OpenAI`

---

<a id="item-21"></a>
## [Hugging Face CEO：中国领跑开源权重 AI 竞赛](https://www.reddit.com/r/China/comments/1vewj4b/hugging_face_ceo_says_china_is_winning_the_ai/) ⭐️ 7.0/10

Hugging Face CEO Clement Delangue 声称中国正在主导开源权重 AI 模型竞赛，并可能在 2026-2027 年达到前沿水平，他将此归功于中国的开放协作文化。他还透露，在一次 AI 驱动的安全漏洞事件中，Hugging Face 在美方前沿模型拒绝协助后，使用了来自 ZAi 的中国开源模型 GLM-5.2 来帮助解决问题。 这位主要 AI 平台 CEO 的评论凸显了全球 AI 竞争中格局的变化，尤其是在开源权重模型与封闭专有系统之间的对比。这也凸显了对 AI 驱动网络安全威胁日益增长的担忧，以及开源模型在应对这些威胁中的实际作用。 Delangue 将中国的开放协作文化与美国实验室'各自为政'的做法进行对比，并指出微软、Palantir 和英伟达等科技巨头正在游说反对限制开源权重模型。尽管如此，Hugging Face 仍与 OpenAI 保持着'健康的合作关系'，称该前沿实验室为'好伙伴'。

reddit · r/China · /u/GetOutOfTheWhey · 8月4日 01:37

**背景**: 开源权重 AI 模型会公开其模型权重（训练参数），允许任何人下载、检查并在此基础上构建——但与完全开源的模型不同，训练数据和代码通常不会共享。前沿级模型指的是目前可用的最先进的 AI 系统，通常是在推理、编码和知识任务基准测试中处于顶尖水平的模型。开源权重模型与封闭模型之间的区别对企业 AI 采用、数据治理和供应商锁定风险具有重要影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude-academy.com/open-source-vs-closed-ai-models">Open - Source vs Closed AI Models : The Real... | Claude Academy</a></li>
<li><a href="https://epoch.ai/blog/open-models-report/">Open vs . closed AI : How behind are open models ? | Epoch AI</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区对此话题的讨论质量中等，反映了对中国开源模型进展的地缘政治影响的关注。评论者既参与了 GLM-5.2 漏洞修复轶事的意义讨论，也参与了关于开放与封闭 AI 生态系统的更广泛辩论。

**标签**: `#AI`, `#Open Models`, `#China`, `#Cybersecurity`, `#Hugging Face`

---

<a id="item-22"></a>
## [中国成立世界人工智能合作组织](https://news.google.com/rss/articles/CBMilwFBVV95cUxQeG9Ja0JGZ3dfSmJWUU83aWFja19ISktORDZab2JxTjZ4RXd2d3YyenRwUFo2NGNxQ2ZuRE12bzdGQmNBZlZwUlVyRFlCbXA4bnhCb05sVnQtbUx4QWFoeHJpNGFDVVl3UDRiSlNsS1FqVGx0M3ZYai1RUDg0VG1HMjVUYkVJZVpscHI0SXBDTTRPblE1cnVJ?oc=5) ⭐️ 7.0/10

中国已提议成立世界人工智能合作组织，这是在 2025 年世界人工智能大会上的提议之后，作为塑造全球人工智能治理更广泛努力的一部分。 这一倡议代表了在影响全球人工智能治理框架方面的重要地缘政治举措，可能会改变国际人工智能标准制定中的权力平衡，并为现有的西方主导监管方法提供替代方案。 该提议包括一项配套的'人人共享的人工智能能力建设行动计划'，该计划概述了五项愿景和十项行动，旨在解决全球南方国家的愿望，但具体的运营细节和会员标准仍不清楚。

google_news · logos-pres.md · 8月4日 17:17

**背景**: 人工智能治理是指指导人工智能系统开发和部署的框架、政策和标准。目前，主要方法包括欧盟人工智能法案、中国的国内法规和美国监管环境，但不存在单一的全球标准。联合国教科文组织等国际机构曾试图制定伦理准则，例如其 2021 年《人工智能伦理建议书》，但全面的全球治理仍然遥不可及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Artificial_Intelligence_Cooperation_Organization">World Artificial Intelligence Cooperation Organization - Wikipedia</a></li>
<li><a href="https://en.people.cn/n3/2026/0625/c90000-20470973.html">Clued-in | AI for good: Major countries should shoulder their...</a></li>
<li><a href="https://thinktank.pk/2025/07/27/ai-for-all-can-a-new-global-body-bridge-the-digital-divide/">AI for All: Can a New Global Body Bridge the... -THINK TANK JOURNAL</a></li>

</ul>
</details>

**标签**: `#AI Governance`, `#Geopolitics`, `#AI Policy`, `#China`, `#International Cooperation`

---

<a id="item-23"></a>
## [Gwern 放弃匿名写作，推出 Guardian Angel AI 项目](https://twitter.com/gwern/status/2084739205071343837) ⭐️ 6.0/10

Gwern 宣布将退休全职匿名写作，转而推出 Guardian Angel，这是一个旨在与用户而非平台所有者对齐的 AI 聊天机器人人格项目。 这一转变凸显了人们对 AI 对齐用户利益而非企业激励的日益关注，可能影响个性化 AI 助手的开发方式。 Guardian Angel 旨在创建优先考虑用户对齐而非平台货币化的聊天机器人人格，解决当前 LLM 与用户不对齐且以广告收入为优化目标的问题。

hackernews · mattsterett · 8月4日 20:48 · [社区讨论](https://news.ycombinator.com/item?id=49174900)

**背景**: Gwern 是 AI 和理性主义社区中著名的匿名作家和研究者，以长篇论文和使用 GPT-2 进行国际象棋等项目闻名。Guardian Angel 项目源于对主要 AI 实验室构建中心化、单一思维系统的批评，这些系统服务于平台所有者而非个人用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hackernoon.com/melding-ai-with-user-centric-platforms-a-journey-through-industry-turbulence">Melding AI with User - Centric Platforms : A Journey... | HackerNoon</a></li>
<li><a href="https://blog.hubspot.com/website/user-centered-design">User - centered design: What it is and how to do it right</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：合作者赞扬 Gwern 的人性和愿景，批评者则警告不要将 LLM 框架为半神实体，部分人对他的匿名决定表示惊讶。

**标签**: `#AI`, `#LLMs`, `#AI Alignment`, `#Personal Project`, `#Tech Community`

---

<a id="item-24"></a>
## [Oxide Computer 完成 4.45 亿美元 D 轮融资](https://www.sec.gov/Archives/edgar/data/1795071/000179507126000002/xslFormDX01/primary_doc.xml) ⭐️ 6.0/10

Oxide Computer 提交了 SEC Form D 文件，进行 4.45 亿美元的 D 轮融资，自 2023 年以来持续快速融资，累计总额已超过 7 亿美元。 这笔重要融资表明投资者对 Oxide 通过机架级计算和开源硬件/软件重新思考本地基础设施的方法充满信心，可能加速替代云模型的采用。 SEC Form D 是私募配售通知文件；社区讨论既突出了对发展轨迹和 Jesse Frazelle 等知名人物的兴奋，也包含对公司是否实际交付硬件以及销售响应不佳的质疑。

hackernews · depr · 8月4日 20:13 · [社区讨论](https://news.ycombinator.com/item?id=49174407)

**背景**: Oxide Computer 构建了其所谓的 Cloud Computer，这是一种机架级系统，将整个服务器机架作为计算单元而非单个服务器。该公司强调通过硬件信任根、开源固件和密码隔离实现完全可审计的安全性，旨在取代传统虚拟化栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://oxide.computer/">Oxide Computer Company</a></li>
<li><a href="https://arctiq.com/blog/oxide-computer-rethinking-on-prem-infrastructure">Oxide Computer : Rethinking On-Prem Infrastructure</a></li>

</ul>
</details>

**社区讨论**: 社区情绪褒贬不一：一些人对该融资轨迹表示兴奋并赞扬 Jesse Frazelle 的参与，而另一些人则质疑公司是否实际交付硬件，并报告提交咨询表单后销售响应不佳。

**标签**: `#infrastructure`, `#funding`, `#cloud-computing`, `#hardware`, `#venture-capital`

---

<a id="item-25"></a>
## [中国 MiniMax 因版权问题限制海外访问 H3 视频模型](https://www.scmp.com/tech/tech-trends/article/3362951/chinas-minimax-curbs-overseas-access-new-ai-video-model-over-copyright-disputes?utm_source=rss_feed) ⭐️ 6.0/10

中国 AI 公司 MiniMax 开源了其 H3 视频模型，但因版权问题对美国和欧盟等地区的用户施加了许可限制。 这凸显了开源 AI 开发与版权合规之间日益紧张的矛盾，尤其是在生成式视频 AI 因训练数据面临法律审查的背景下。它可能影响其他 AI 公司在受监管市场开源模型的方式。 模型权重已发布给开发者，但许可证限制了特定司法管辖区的免费访问。这导致了开源格局的碎片化，同一模型在不同地区以不同方式提供。

rss · South China Morning Post · 8月4日 12:00

**背景**: 模型权重是编码 AI 模型智能的核心参数，决定了它如何处理和生成内容。开源 AI 涉及公开这些权重供公众使用，但许可限制可能限制商业应用和地理访问。H3 视频模型是 MiniMax 最新的 AI 视频生成器，提供原生 2K 输出和高运动连贯性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://apimart.ai/model/minimax-h3">MiniMax H 3 API - World-Leading AI Video Generation</a></li>
<li><a href="https://www.mend.io/blog/top-open-source-licenses-explained/">Top Open Source Licenses Explained</a></li>

</ul>
</details>

**标签**: `#AI`, `#Copyright`, `#Open Source`, `#Generative AI`, `#AI Regulation`

---

<a id="item-26"></a>
## [中国初创公司涉嫌操纵机器人基准测试超越英伟达](https://www.scmp.com/tech/tech-war/article/3362923/has-chinese-physical-ai-start-manipulated-global-ranking-beat-nvidia?utm_source=rss_feed) ⭐️ 6.0/10

今年六月，中国物理人工智能初创公司 Spirit AI 凭借 Spirit v1.6 模型在 RoboArena 全球基准测试中短暂超越英伟达，但该公司现被指控操纵排名以宣称在机器人领域全球领先。 这一争议凸显了中美在下一代人工智能开发方面的激烈竞争，并引发了对基准测试完整性的严重质疑，可能影响整个行业对物理人工智能进展的衡量和比较方式。 RoboArena 衡量人工智能系统将决策转化为物理行动的能力，包括移动物体、导航空间、使用工具和适应新环境。成立于 2024 年、总部位于杭州的 Spirit AI 在指控出现之前凭借 v1.6 模型获得了排名第一。

rss · South China Morning Post · 8月4日 10:30

**背景**: 物理人工智能是指嵌入机器人和机器中的人工智能，使其能够感知环境、对任务进行推理，并以越来越高的自主性执行物理动作，而不是遵循固定程序。与专注于语言或推理的传统人工智能基准测试不同，RoboArena 等物理人工智能基准测试检验系统通过具身行动与现实世界互动的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thenextweb.com/news/spirit-ai-beats-nvidia-roboarena-physical-ai">Spirit AI beats Nvidia on RoboArena robotics benchmark</a></li>

</ul>
</details>

**标签**: `#Physical AI`, `#Robotics`, `#Benchmarking`, `#US-China Tech Competition`, `#AI Ethics`

---

<a id="item-27"></a>
## [中国芯片设备商 AMEC 利润近翻四倍，需求激增](https://www.scmp.com/tech/tech-trends/article/3362918/chinese-chip-tool-maker-amec-says-first-half-profit-nearly-quadruple-amid-soaring-demand?utm_source=rss_feed) ⭐️ 6.0/10

中微半导体设备公司（AMEC）公布上半年初步利润至少 27 亿元人民币，同比增长 282%，主要受美国制裁下国产半导体需求激增推动。 这一利润激增表明美国出口管制反而加速了中国半导体自主化进程，AMEC 作为中国芯片设备龙头直接受益于国产替代趋势。 该未经审计的数据已向上海证券交易所提交，AMEC 是一家部分国有控股企业，于 2019 年在科创板上市，股票代码 688012。

rss · South China Morning Post · 8月4日 09:00

**背景**: 中微半导体设备公司（AMEC）是中国最大的半导体设备制造商之一，专注于刻蚀设备等芯片生产设备的制造。该公司的发展正值美国实施出口管制和制裁、限制中国获取先进半导体技术的背景下。中国将半导体自主化视为关键国家优先事项，致力于减少对美国及其盟友技术的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Advanced_Micro-Fabrication_Equipment">Advanced Micro - Fabrication Equipment - Wikipedia</a></li>
<li><a href="https://www.brookings.edu/wp-content/uploads/2024/05/20240528_ES_Sanctions_Branstetter_Final.pdf">Export controls and</a></li>
<li><a href="https://itif.org/publications/2024/08/19/how-innovative-is-china-in-semiconductors/">How Innovative Is China in Semiconductors ? | Reports... | ITIF</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#China tech`, `#earnings`, `#geopolitics`, `#manufacturing`

---

<a id="item-28"></a>
## [AI 奠基优化算法之父 Nesterov 荣获应用数学顶级奖项](https://www.scmp.com/news/china/science/article/3362465/shenzhen-based-ai-mathematician-yurii-nesterov-wins-top-prize-applied-maths?utm_source=rss_feed) ⭐️ 6.0/10

定居深圳的俄裔比利时数学家 Yurii Nesterov 因其约 40 年前推导出的加速梯度算法荣获应用数学顶级奖项，该算法如今已成为推动现代 AI 发展的核心引擎。 这一荣誉凸显了数十年前的基础数学工作如何支撑当今的 AI 革命，证明了纯优化理论对深度学习及更广泛技术生态的深远实际影响。 Nesterov 的加速梯度方法通过在标准梯度下降中引入类动量的前瞻项来改进算法，在凸和非凸优化问题中均实现了最优收敛速度，该技术现已嵌入 Adam 等训练框架中。

rss · South China Morning Post · 8月4日 09:00

**背景**: 梯度下降是一种通过沿负梯度方向迭代移动来最小化函数的基础优化算法。Nesterov 加速梯度方法于 20 世纪 80 年代提出，在经典梯度下降基础上增加了前瞻步骤以预测未来梯度，显著加快了收敛速度。这种优化技术对于训练深度神经网络至关重要，因为高效最小化损失函数是模型性能的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jlmelville.github.io/mize/articles/nesterov.html">Nesterov Accelerated Gradient and Momentum • mize</a></li>
<li><a href="https://pages.cs.wisc.edu/~yudongchen/cs726_sp23/Lecture_9_10_accelerated_GD.pdf">Lecture 9–10: Accelerated Gradient Descent</a></li>

</ul>
</details>

**标签**: `#AI`, `#mathematics`, `#optimization`, `#research`, `#foundational algorithms`

---

<a id="item-29"></a>
## [LLM 0.32 新增推理轨迹、OpenAI Responses API 及服务端工具](https://simonwillison.net/2026/Aug/4/new-release-of-llm/#atom-everything) ⭐️ 6.0/10

Simon Willison 发布了 LLM 0.32，这是该项目自启动以来最重要的更新，新增了可见的推理轨迹、OpenAI Responses API 支持、服务端工具以及重新设计的基于内容的 SQLite 日志系统。 此次更新增强了 LLM CLI 工具与现代推理模型及 OpenAI 最新 API 的协作能力，使其对构建 AI 驱动应用的开发者更加实用。 推理轨迹默认输出到标准错误，可通过 --hide-reasoning 标志屏蔽；新默认模型为 GPT-5.6 Luna，服务端工具包括 OpenAI 的 CodeInterpreter 和 WebSearch，以及 Anthropic 的 WebSearch、WebFetch、CodeExecution 和 MCP 连接器。

rss · Simon Willison · 8月4日 23:58

**背景**: 推理轨迹是先进 LLM 在生成最终答案之前产生的中间思维过程，类似于思维链提示。OpenAI Responses API 是一个专为智能体和多步工作负载设计的新接口，提供内置的网页搜索和代码执行等工具。基于内容的存储通过内容哈希而非位置来检索数据，提高了数据完整性和去重能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnllm.dev/learn/intermediate/reasoning-models">Reasoning Models: When AI Thinks Before It Answers</a></li>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content-addressable_storage">Content - addressable storage - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#CLI`, `#OpenAI`, `#Python`, `#AI Tools`

---

<a id="item-30"></a>
## [宽带拨款恢复，但种族标准被法官裁定违宪](https://arstechnica.com/tech-policy/2026/08/trump-forced-to-reinstate-broadband-grants-but-court-lets-us-scrap-race-criteria/) ⭐️ 6.0/10

在特朗普政府试图取消该计划后，数字公平法案下的 12.5 亿美元宽带拨款项目得以恢复，但联邦法官裁定该计划的种族资格标准违宪。 这一裁决影响未来联邦宽带公平项目的构建方式，可能限制政府使用种族标准来缩小农村和弱势社区数字鸿沟的能力。 数字公平法案是 2021 年基础设施法的一部分，最初预留了 27.5 亿美元——其中 6000 万美元供各州和领地制定公平互联网接入计划，25 亿美元用于实施。特朗普政府于 5 月以该法案'种族主义'为由终止了资金，但法院强制恢复了 12.5 亿美元的拨款，同时废除了种族相关条款。

rss · Ars Technica · 8月4日 21:27

**背景**: 数字公平法案作为 2021 年两党基础设施投资与就业法的一部分通过，旨在通过确保全美公平的网络接入来缩小数字鸿沟。它为各州和领地制定数字公平计划建立了框架，并提供资金以在服务不足的地区扩大宽带基础设施。种族相关标准旨在优先考虑历史上受高速互联网不平等接入影响的社区。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.news-medical.net/news/20251010/Trump-Called-Digital-Equity-Act-e28098Raciste28099-Now-Internet-Money-For-Rural-Americans-Is-Gone.aspx">Trump called Digital Equity Act ‘racist.’ Now internet money for rural...</a></li>

</ul>
</details>

**标签**: `#broadband`, `#tech policy`, `#digital equity`, `#legal`, `#government grants`

---

<a id="item-31"></a>
## [EFF 警告 Android 应用可能通过第三方 SDK 共享用户位置数据](https://techcrunch.com/2026/08/04/android-app-developers-may-be-unwittingly-sharing-their-users-location-data-with-advertisers/) ⭐️ 6.0/10

电子前沿基金会（EFF）发布新发现，警告嵌入 Android 应用中的第三方广告 SDK 可能会收集并共享用户的位置数据，即使用户仅授予了应用本身的权限。 这一发现揭示了一个重要的隐私漏洞：用户可能认为他们仅同意应用访问其位置，而开发者嵌入的第三方代码却在同时为广告目的收集这些敏感数据。 EFF 明确指出，'仅凭应用级别的位置权限不能表示对第三方广告 SDK 收集和共享位置的有意义同意'，并警告广告 SDK 不应将共享个人数据设为默认行为，尤其是对于位置这样敏感的数据。

rss · TechCrunch · 8月4日 20:26

**背景**: Android 应用经常集成第三方软件开发工具包（SDK），这些 SDK 由广告网络、分析公司和其他服务提供商提供，用于添加功能而无需从头构建。这些 SDK 在应用的权限上下文中运行，这意味着它们可以访问应用已获得权限使用的数据，即使用户并未明确知晓 SDK 的数据收集行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/08/04/android-app-developers-may-be-unwittingly-sharing-their-users-location-data-with-advertisers/">Android app developers may be unwittingly sharing their... | TechCrunch</a></li>
<li><a href="https://beforeitsnews.com/libertarian/2026/08/developers-beware-of-ad-libraries-that-betray-your-users-location-privacy-2851521.html">Developers: Beware of Ad Libraries that Betray Your Users’ Location ...</a></li>

</ul>
</details>

**社区讨论**: 搜索结果指出，EFF 的调查确定了多个广告 SDK，这些 SDK 在嵌入 Android 应用时默认公开承认收集和共享用户位置，引发了关于默认设置如何影响用户和开发者的担忧。

**标签**: `#privacy`, `#android`, `#mobile security`, `#data collection`, `#EFF`

---

<a id="item-32"></a>
## [开源权重 AI 模型逼近前沿性能，安全差距依然存在](https://techcrunch.com/2026/08/04/open-weight-ai-models-are-catching-up-to-the-frontier-the-safety-gap-remains/) ⭐️ 6.0/10

SaferAI 的一份报告发现，Z.ai 的 GLM-5.2 开源权重模型正在逼近前沿 AI 能力，但缺乏关键的安全缓解措施，这重新引发了人们对治理能否跟上模型能力发展的担忧。 这凸显了快速推进的开源权重模型与相对缓慢的安全治理之间的紧张关系，引发了人们对在日益竞争的环境中，强大 AI 系统是否可能在缺乏充分保障措施的情况下被部署的担忧。 GLM-5.2 是一个开源权重模型，意味着其训练参数可公开下载，但与完全开源模型不同的是，其训练代码和数据并未公开。该模型已接近前沿性能水平，但缺乏前沿模型通常具备的安全缓解措施。

rss · TechCrunch · 8月4日 20:05

**背景**: 开源权重模型会发布可下载的训练参数文件，任何人都可以使用，但无法获得底层训练代码或数据。前沿 AI 是指由少数组织开发的最先进 AI 系统，由于其双重用途潜力和不可预测的涌现能力，带来了独特的治理挑战。担忧在于，随着开源权重模型变得日益强大，它们可能会超越安全协议和治理框架的发展速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bota.chat/kimi-k3/open-weight-ai-models/">Open Weight vs Open Source AI Models : The Real Difference</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Open-Weight Models`, `#AI Governance`, `#LLMs`, `#AI Policy`

---

<a id="item-33"></a>
## [下载：美国机器人限制与 ICE 的 DNA 采集扩张](https://www.technologyreview.com/2026/08/04/1141098/the-download-robot-restrictions-ice-dna/) ⭐️ 6.0/10

特朗普政府已将 AI 保护主义扩展至机器人领域，对仿人机器人及相关电力电子设备实施出口限制。与此同时，ICE 已采集近一百万人的 DNA，其中包括数十万从未被定罪者，将其样本永久录入 FBI 犯罪数据库。 这些发展反映了美国政策以国家安全为由限制技术出口和扩大监控的更广泛趋势，直接影响具身 AI 硬件供应链，并对移民和拘留者提出严重的隐私问题。 出口管制将 AI 机器人保护主义扩展至流体机械和数据中心电力电子设备，建立在现有的芯片出口管制、无人机黑名单和路由器限制之上。ICE 的 DNA 采集在第二届特朗普政府期间激增，相关样本现已永久存储于联邦数据库中。

rss · MIT Technology Review · 8月4日 12:14

**背景**: AI 保护主义是指政府以国家安全为由限制 AI 相关技术和硬件进出口的政策。美国自拜登政府时期起逐步扩大此类管制，从先进半导体开始，逐渐扩展到无人机、网络设备，如今又延伸至机器人领域。ICE 的 DNA 采集项目允许移民当局从被拘留者身上采集遗传物质并录入联邦 CODIS 数据库，这一做法已面临法律挑战和公民自由争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://beyondtmrw.org/article/trump-ai-protectionism-targets-robotics">AI Robotics Protectionism : US Bans on Foreign Humanoid Robots</a></li>
<li><a href="https://www.wired.com/story/ice-dna-collection-fbi-codis/">ICE Collected Nearly 1 Million People’s DNA Last... | WIRED</a></li>

</ul>
</details>

**标签**: `#robotics`, `#AI policy`, `#export controls`, `#privacy`

---

<a id="item-34"></a>
## [世界银行：发展中国家从 AI 获益更多、损失更少](https://news.google.com/rss/articles/CBMitwFBVV95cUxOR2N4NEVIWUZvTS1IQ0FGeWZTSGU5U041NV9JWjZBVmowV2pvQVhFTDlDdDNxMEZZdDByUUpDYjJKbTRCVi05QUltQTdMZmVVZl96ckRuTWVFa0ltV3VfbHpBWnNhRktYWm9Od2JZVVItdWtNQm1sNWVaa1BMYUcwcFpaZ1psVjJ4N1RCci0zY3FqU1h4VEtGV19OaGtBOTFXVmMtZ1BIcUk4ZFRPb3h5Sy0xRjMxWVk?oc=5) ⭐️ 6.0/10

世界银行的一份报告指出，与发达国家相比，发展中国家在采用人工智能方面有望获得更多收益且损失更少。 这一分析的重要性在于它挑战了人工智能主要惠及发达经济体的常见叙事，表明发展中国家可能在生产力和经济增长方面实现跨越式发展。 该报告是一项宏观层面的政策分析，而非技术研究，侧重于经济影响而非人工智能能力或实施细节。

google_news · wsj.com · 8月4日 14:02

**背景**: 人工智能是指能够执行通常需要人类智能的任务（如学习和解决问题）的计算机系统。人工智能的经济影响是一个主要讨论话题，涉及对就业替代和生产率提升的担忧。与发达国家相比，发展中国家往往面临不同的结构性挑战与机遇。

**标签**: `#AI`, `#Economics`, `#World Bank`, `#Developing Economies`, `#Policy`

---

<a id="item-35"></a>
## [美国竞逐廉价 AI 替代中国方案](https://news.google.com/rss/articles/CBMiowFBVV95cUxNV1l1NDFOT09nMFNYX0lVNjlidGtVYmM5YWdNcU13NHlmVlZDS1YyYlVGeFdJZnd2Wk1ZenlBWUZUZ245M21tV25rMjZXTHBlWUNGU0hVX2NJb1lVMlV3a2lrazJhQTRxRVM3Z1pyazIxUDVFYWhSU0hUMHdmeDNmZUNXYk5nR2pXSFpVSmpyM3Y2bmZnOUFqdzBTTG5Qa3gxQXQw?oc=5) ⭐️ 6.0/10

《华尔街日报》报道了中美在开发廉价 AI 系统方面的竞争态势，中国正推动廉价开源权重模型，而美国企业和政策制定者正在应对。 成本决定了哪些 AI 模型会率先在全球被采用，如果中国将技术做得足够便宜，它可能成为全球默认选择，从而影响 AI 影响力的未来格局。 中国开源权重 AI 模型为美国初创企业提供了成本效益高的解决方案，但也引发了关于国家安全和 AI 蒸馏风险的激烈政策辩论。

google_news · wsj.com · 8月5日 01:01

**背景**: 开源权重 AI 模型是指其权重（学习到的参数）公开可用的机器学习系统，允许开发者以更低成本在本地运行和修改。中国一直在追求以效率为导向的 AI 战略，优先考虑成本效益高的模型而非单纯追求规模，而美国传统上更注重不惜成本地构建最强大的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://restofworld.org/2026/silicon-valley-debate-chinese-open-weight-ai-models/">Why U.S. tech and Washington are divided over Chinese AI models</a></li>
<li><a href="https://www.theweek.in/wire-updates/international/2026/02/27/how-china-is-betting-cheap-ai-will-get-the-world-hooked-on-its-tech.html">How China is betting cheap AI will get the world hooked on its tech</a></li>

</ul>
</details>

**标签**: `#AI`, `#Geopolitics`, `#Industry Analysis`, `#US-China Relations`

---