# BLOCKERS — 连续失败记录（规则：同一问题连续失败3次记录并跳过）

## B-01 Britannica「Shen Congwen」页面无法通过 WebFetch 提取（2026-11-17）
- 现象：`https://www.britannica.com/biography/Shen-Congwen` 三次尝试失败（两次"completed but extraction model returned no text"，一次猜测变体 URL 404）。
- 处理：改用英文维基百科 Shen_Congwen 条目（web_reader 通道）核对，成功。
- 影响：无（已获等价权威来源）。

## B-02 GitHub 推送（2026-11-18）—— 已解决
- 现象：HTTPS 直连 github.com/api.github.com 被网络重置/超时（Connection reset / timeout）；本地无代理端口可用；gh CLI 未安装。
- 解决：发现 `~/.ssh/id_ed25519` 已配置且 `ssh.github.com:443` 可达（`ssh -T -p 443 git@ssh.github.com` 认证成功 Hi TianDiHuAng）；将 remote 改为 SSH（`git@github.com:TianDiHuAng/culture_work.git`）后 push 成功。
- 教训：国内网络下 GitHub 推送优先试 `ssh.github.com:443`；HTTPS 通道仅作只读备用。

## 备注
- zh.wikipedia.org / en.wikipedia.org：本地 DNS 污染 + 直连超时，WebFetch/curl 均不可达；改走 web_reader MCP（服务器侧抓取）或 Britannica。
- baike.baidu.com：403（UA 伪装无效），放弃。
- zgbk.com（中国大百科）：SPA 前端、正文 JS 渲染，无法静态抓取，放弃。
- ctext.org：连接超时，放弃。
- gutenberg.org：WebFetch 503，放弃。
- guoxue.com：TLS 握手失败，放弃。
