# BLOCKERS — 连续失败记录（规则：同一问题连续失败3次记录并跳过）

## B-01 Britannica「Shen Congwen」页面无法通过 WebFetch 提取（2026-11-17）
- 现象：`https://www.britannica.com/biography/Shen-Congwen` 三次尝试失败（两次"completed but extraction model returned no text"，一次猜测变体 URL 404）。
- 处理：改用英文维基百科 Shen_Congwen 条目（web_reader 通道）核对，成功。
- 影响：无（已获等价权威来源）。

## 备注
- zh.wikipedia.org / en.wikipedia.org：本地 DNS 污染 + 直连超时，WebFetch/curl 均不可达；改走 web_reader MCP（服务器侧抓取）或 Britannica。
- baike.baidu.com：403（UA 伪装无效），放弃。
- zgbk.com（中国大百科）：SPA 前端、正文 JS 渲染，无法静态抓取，放弃。
- ctext.org：连接超时，放弃。
- gutenberg.org：WebFetch 503，放弃。
- guoxue.com：TLS 握手失败，放弃。
