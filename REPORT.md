# REPORT — 中外文学名著导读库（第一版交付报告）

完成日期：2026-11-18　　工作目录：`D:\AI\project\culture`　　Git 提交数：46

---

## 一、成果总览

| 项目 | 数量 | 说明 |
|---|---|---|
| 作品页 | **60 部** | 中国 30 / 外国 30，每页固定 8 节结构 |
| 作家页 | **55 篇** | 生卒年、生平年谱、代表作、风格、文学史地位（诗经无名氏与两部选集编者不设页，见 DECISIONS.md D04） |
| SVG 配图 | **60 张** | 人物关系图 33 张（graph/ring）+ 主题·结构图 27 张（grid/flow），脚本生成、程序化防出界 |
| 来源库 | **100 条** | `sources.json`，其中 **99 条 verified=true**（全部经实际打开页面核对），要求 ≥80 |
| 静态站点 | 9 类页面 | 首页、作品总览（筛选）、作家索引、时间线、关于 + 60 作品页 + 55 作家页；纯 HTML/CSS/原生 JS，可 file:// 离线打开 |
| 校验工具 | 3 个脚本 | `tools/check.py`（全库校验）、`build.py`（站点生成）、`svggen.py`（SVG 生成） |
| 决策与阻塞记录 | 2 份 | `DECISIONS.md`（10 项保守决策）、`BLOCKERS.md`（通道限制与失败记录） |

### 收录分布
- **时代**：古代 25 · 近代 16 · 现当代 19
- **体裁**：小说 34 · 诗歌 8 · 戏剧 8 · 故事集 6 · 散文 4
- **国别（14 个/地区）**：中国 30、法国 6、英国 4、美国 4、古希腊 4、俄国 3、意大利 2，西班牙/德国/奥地利/爱尔兰/挪威/日本/哥伦比亚各 1

---

## 二、各阶段执行摘要

### 阶段0 初始化
建立目录骨架（data/works、data/authors、assets/svg、tools、site）与 `works_list.md` 入选清单（60 部中外各 30）、`DECISIONS.md`、`PROGRESS.md`；git init。

### 阶段1 来源库（100 条 / 99 verified）
- **网络环境诊断**：本机网络存在 DNS 污染——WebFetch/curl 直连维基百科全部超时；百度百科 403；中国大百科（zgbk）为 JS 渲染 SPA；ctext/gutenberg/guoxue 超时或握手失败。诊断过程与放弃原因记录于 `BLOCKERS.md`。
- **最终通道矩阵**（并记入 BLOCKERS.md 备注）：
  - Encyclopaedia Britannica（WebFetch 可达，成海外条目主力）；
  - 英文维基百科（web_reader MCP 服务器侧抓取，Britannica 缺条目时使用：汤显祖、老舍等）；
  - 中文官方源（WebFetch 可达）：央视网、求是、人民网党史频道、中国作家网（中国作协）、中国新闻网、新华网、书格古籍库（港中文藏本影印）；
  - WebSearch（服务端）用于定位 URL 与交叉确认。
- 每条来源均实际打开页面并记录核对要点（`note` 字段注明核对日期与页面确认内容）；仅 1 条（Britannica 艾青页，三次提取失败）标记 verified=false，改用英文维基+人民网补证。
- 覆盖：外国 30 部作品 + 28 位作家全部来自 Britannica/诺贝尔官网等权威条目；中国部分 Britannica 有条目的用 Britannica，无条目的（唐诗三百首、宋词三百首、平凡的世界、白鹿原、活着、边城、艾青诗选等）用中文官方源补齐。

### 阶段2 校验与生成工具
- `tools/check.py` 校验项（全部实现并每次提交前运行）：
  1. **必填字段**：works 25 项、authors 14 项字段强制；era/genre_group 枚举；
  2. **日期合法**：year_sort 整数且 [-3000, 2026]；birth_year/death_year 合法、death≥birth；
  3. **每条事实有来源**：sources、year_source、author_source、dates_source 必须存在且 verified=true；influence 每条带 verified 来源；timeline 条目带来源；
  4. **无重复**：work id/书名去重、author id/姓名去重、source id 去重；
  5. **内部链接**：所有页面 href/src 目标存在；总览与时间线收录全部作品；
  6. **SVG 不出界**：解析 viewBox 与全部坐标属性、polygon 点、文本按 text-anchor 估算宽度（中文 1em/英文 0.62em）；
  7. 补充：相关作品引用有效性、作者页双向引用、待核实字段存在。
- `tools/svggen.py`：5 种版式（graph/ring/grid/flow/tree）从规格生成 SVG，内置 Bounds 逐元素检查，从构造上杜绝出界；check.py 再独立复核生成文件。
- 阶段期间即以《红楼梦》样例跑通“写数据 → build → check → commit”管线，并修复了链接前缀、text-anchor 宽度估算、两轮依赖校验三个真实问题。

### 阶段3 内容生产（60 部逐部提交，45 次内容提交）
- 顺序：中国按时代（先秦→明清→近现代）→ 外国按时代（古希腊→20世纪）；每部作品页 + 对应作家页 + SVG 一次提交。
- 全部内容遵循硬性规则：
  - **不编造**：所有成书年份、生卒年、人物、情节均以已核来源为锚；查不到的（初版月份、篇目细数、名言出处、原型考订等）写入各页“八、待核实”，60 部作品页与 55 篇作家页均设“待核实”栏；
  - **引文克制**：正文只转述观点并注明是谁的评价（Britannica 撰稿人、具体评论家、媒体名）；直接引文仅限公有领域古籍/原文名句（如《浮士德》《哈姆雷特》《老人与海》），且标注“原文/意译、逐字核对待完成”；
  - **情节概括**：只写到读者需要的程度（每部 3 段左右脉络），无逐章复述；
  - **争议并列**：《哈克贝利·费恩》的种族语言之争与 2011 年洁本、《白鹿原》茅奖修订风波、《十日谈》“粗俗”批评、《红楼梦》后 40 回三说、《骆驼祥子》死亡两说、《堂吉诃德》伪续事件、《莫言》2024 被诉事件等均列各方说法；
  - **版权**：未搬用任何现代译本文字；推荐版本只列书目信息。

### 阶段4 聚合与报告
- `tools/build.py` 生成：`index.html`（统计与入口）、`works.html`（作品总览：国别/时代/体裁/搜索四维筛选，原生 JS，禁 JS 退化为完整列表）、`authors.html`（作家索引：按国别分组、生卒与代表作直链）、`timeline.html`（60 个坐标的时间线，中外分色）、`about.html`（收录原则与来源说明）、全部作品/作家页。
- 抽查验证：页面 8 节编号完整、来源外链与 SVG 相对路径正确、面包屑导航一致。
- 本报告即为阶段4 交付物。

---

## 三、质量与合规声明

1. **可复现**：任何人在本仓库执行 `python tools/build.py && python tools/check.py` 即可重建站点并全量校验；check 以 exit code 报告失败。
2. **来源可溯**：每页底部列“本页主要来源”；正文关键事实（年代、生卒、评价）行内标注来源 ID；点击可跳转到已核对的原文页面。
3. **诚实边界**：全库共留下约 300 条“待核实”事项（各页第八节/作家页对应栏），涵盖：古代作品断代争议、初版细节、译本信息、轶事出处、原型考订等。这些事项**不冒充已证实事实**，等待后续版本逐条补充来源。
4. **单人署名**：内容为 AI 辅助整理（知识库 + 已核网络来源），站点“关于”页有说明；不冒充专家学术成果。

---

## 四、已知限制

- **来源语言偏科**：外国部分几乎全部依赖 Britannica/英文维基；中国现当代部分依赖国内官方媒体。未能使用学术期刊（本机不可达），“评价”多为百科级而非专题论文级。
- **两条来源 verified=false**（Britannica 艾青页等）：未在正文引用，仅存档。
- **少数页面的深层数据**（如《诗经》风雅颂细数、《论语》章数、各选集逐篇目录）在已核来源中不存在，按规则移入待核实而非臆填。
- **SVG 为示意图**：人物关系图做了简化取舍，非学术考据图；站点已注明。

---

## 五、如何浏览与构建

```bash
# 浏览：直接用浏览器打开 site/index.html（无需服务器）
# 重建：
python tools/build.py      # data/*.json + sources.json -> site/
python tools/check.py      # 全库校验（错误则 exit 1）
# 追加来源：
python tools/appendsrc.py <<'EOF'
{"id":"B101","title":"...","url":"...","verified":true,"note":"已打开核对..."}
EOF
python - <<'PYEOF'   # 重建 sources.json（去重排序）
import json, pathlib
lines = pathlib.Path("_sources_raw.jsonl").read_text(encoding="utf-8").splitlines()
seen, out = set(), []
for line in lines:
    line = line.strip()
    if not line: continue
    obj = json.loads(line)
    if obj["id"] in seen: continue
    seen.add(obj["id"]); out.append(obj)
out.sort(key=lambda o: o["id"])
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
PYEOF
```

---

## 六、后续展望（呼应“广泛搜集有点名气的作者的作品”）

第一版以“公认经典 + 来源可核”为保守标准。后续扩充建议（已在 DECISIONS.md D01 预留）：

1. **补充名单**（《追忆似水年华》《金瓶梅》等已讨论未入选者）；
2. **同一作家加收**：鲁迅《彷徨》《野草》、雨果《九三年》、托尔斯泰《安娜·卡列尼娜》、契诃夫戏剧、卡夫卡《审判》、川端《伊豆的舞女》、莫言《生死疲劳》等（作家页已就位，加作品页即可）；
3. **待核实清零**：逐条为约 300 项待核实补来源（可复用本项目的通道矩阵）；
4. **多语言/学术来源**：接入可达的学术数据库，提升“影响与评论”一节的引用层级；
5. **站内搜索**：目前为总览页过滤，后续可加全文索引（如 lunr.js 的本地方案）。

---

**状态：ALL 四阶段完成。PROGRESS.md 已写 ALL_DONE。**
