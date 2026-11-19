# -*- coding: utf-8 -*-
"""v5批3：古典戏剧补强 9部+8作家页+12来源"""
import json, pathlib

new_src = [
{"id":"B234","title":"Aeschylus — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Aeschylus-Greek-dramatist","type":"百科全书","verified":True,"covers":["aeschylus","puluomixiusibang"],"note":"2026-11-20 核对：c.525/524 BC—456/455 BC Gela；'adding a second actor'；'Father of Tragedy'；'wrote approximately 90 plays'仅存7部完整悲剧；13次首奖；《被缚的普罗米修斯》作者归属存在学术争论（页面问答提出）"},
{"id":"B235","title":"Prometheus Bound (play by Aeschylus) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Prometheus-Bound-play-by-Aeschylus","type":"百科全书","verified":True,"covers":["puluomixiusibang"],"note":"2026-11-20 核对：'has saved humanity with his gift of fire'；'For this act Zeus has ordered that he be chained to a remote crag'；来客：Oceanus/俄刻阿尼得斯歌队/Io/Hermes；'the dating of which is uncertain'"},
{"id":"B236","title":"Euripides — Encyclopaedia Britannica 与 Medea (play by Euripides) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Euripides","type":"百科全书","verified":True,"covers":["euripides","meidiya"],"note":"2026-11-20 核对：c.484 BC Athens—406 Macedonia；最后一位古典雅典大悲剧家；'Nineteen plays are extant, if one of disputed authorship is included'（92部归名）；《美狄亚》431 BCE上演；'Medea determines that she will punish Jason by murdering not only her own sons but also the Corinthian princess'"},
{"id":"B237","title":"Ovid — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ovid-Roman-poet","type":"百科全书","verified":True,"covers":["ovid","bianxingji_ovid"],"note":"2026-11-20 核对：43 BCE 3月20日 Sulmo—17 CE Tomis；8 CE 被奥古斯都流放黑海 Tomis；'Ovid specifies two, his Ars amatoria and an offense'、'insisting that it was an indiscretion (error), not a crime (scelus)'；'Ovid gave many Greek legends their definitive forms for subsequent generations'"},
{"id":"B238","title":"Metamorphoses (poem by Ovid) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Metamorphoses-poem-by-Ovid","type":"百科全书","verified":True,"covers":["bianxingji_ovid"],"note":"2026-11-20 核对：15卷、约8 CE拉丁六音步史诗；'noted for its wit, rhetorical brilliance, and narrative and descriptive qualities'；从创世到'死亡与成神的凯撒'；以'激情'为统一主题"},
{"id":"B239","title":"Voltaire — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Voltaire","type":"百科全书","verified":True,"covers":["voltaire","laoshiren"],"note":"2026-11-20 核对：1694-11-21巴黎—1778-05-30巴黎；'central figure of the Enlightenment'；'the satirical novel Candide (1759)'；《哲学书简》(1734)'a landmark in the history of thought'（莱布尼茨乐观主义讽刺目标该页未载——待核）"},
{"id":"B240","title":"Moliere — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Moliere-French-dramatist","type":"百科全书","verified":True,"covers":["moliere","weijunzi"],"note":"2026-11-20 核对：1622-01-15受洗巴黎—1673-02-17巴黎；'widely regarded as the finest writer of comedy in the French language'；1658年卢浮宫为路易十四演出；'They were met with public outcry and were suppressed by the Roman Catholic Church'；1673年台上倒塌当日去世"},
{"id":"B241","title":"Tartuffe — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Tartuffe","type":"百科全书","verified":True,"covers":["weijunzi"],"note":"2026-11-20 核对：五幕喜剧'produced in 1664 and published in French in 1669'（Le Tartuffe; ou, l'imposteur）；'Elmire, Orgon's wife, sees through Tartuffe's wicked hypocrisy and exposes him'"},
{"id":"B242","title":"Epic of Gilgamesh — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Epic-of-Gilgamesh","type":"百科全书","verified":True,"covers":["jierjiamieshishi"],"note":"2026-11-20 核对：'often cited as the earliest significant work of surviving literature'；最完整文本为尼尼微亚述巴尼拔图书馆出土的'12 incomplete Akkadian-language tablets'；恩奇都之死→寻乌特纳皮什提姆（'survivor of the Babylonian Flood'）→青春草被蛇夺走→接受必死"},
{"id":"B243","title":"Jaroslav Hasek — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jaroslav-Hasek","type":"百科全书","verified":True,"covers":["hasek","haobingshuaike"],"note":"2026-11-20 核对：1883-04-30布拉格—1923-01-03 Lipnice；'The Good Soldier Schweik reflects the pacifist, antimilitary sentiments of post-World War I Europe'；'forever colliding with the clumsy, dehumanized military bureaucracy'；计划六卷仅成三卷、第四卷由 Karel Vaněk 续成"},
{"id":"C027","title":"《晚明文化与昆曲盛世》（光明日报）","author":"光明日报","year":"2014-01-20","url":"https://epaper.gmw.cn/gmrb/html/2014-01/20/nw.D110000gmrb_20140120_1-16.htm","type":"官方媒体","verified":True,"covers":["hongsheng","changshengdian"],"note":"2026-11-20 核对：'《长生殿》写成于康熙二十七年（1688）'；《桃花扇》成于康熙三十八年（1699）；'这两部戏曲，都在康熙年间写成'；'都遭到了很大的政治压迫，难以摆脱以古讽今的指责'"},
{"id":"C028","title":"《兴亡一系桃花扇》（光明日报）","author":"光明日报（黄敏学）","year":"2014-12-03","url":"https://epaper.gmw.cn/gmrb/html/2014-12/03/nw.D110000gmrb_20141203_2-12.htm","type":"官方媒体","verified":True,"covers":["kongshangren","taohuashan"],"note":"2026-11-20 核对：'《桃花扇》乃明清传奇压卷之作'；'穷二十余年之心力，三易其稿'；'康熙三十八年六月，《桃花扇》终于脱稿'；'王公荐绅，莫不借钞，时有纸贵之誉'；康熙看后不悦、次年遣返原籍；'借离合之情，写兴亡之感'；'南朝兴亡，遂系之桃花扇底'；复社名士侯方域与秦淮歌伎李香君；结尾'入道'虚构"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new_src:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
raw = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for s in raw:
    seen[s["id"]] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources:", len(out))

# ---------- authors ----------
authors = {
"hongsheng": {
  "id": "hongsheng", "name": "洪昇", "foreign_name": "Hong Sheng（洪昇，1645—1704，生卒通说待核）",
  "country": "中国", "birth": 1645, "death": 1704, "birth_year": 1645, "death_year": 1704, "era": "古代",
  "summary": "洪昇，清初戏曲家，杭州人（通说）。传奇《长生殿》'写成于康熙二十七年（1688）'（光明日报 C027）；'这两部戏曲，都在康熙年间写成'且'都遭到了很大的政治压迫，难以摆脱以古讽今的指责'（C027——与《桃花扇》并提）。与孔尚任并称'南洪北孔'（通说待核）。",
  "timeline": [
    {"year": 1645, "text": "生于杭州（1645年说——通说待核）。", "src": "C027"},
    {"year": 1688, "text": "《长生殿》写成于康熙二十七年（光明日报 C027）。", "src": "C027"},
    {"year": 1704, "text": "卒（1704年曹寅江宁观演《长生殿》返程落水说——通说待核）。", "src": "C027"}],
  "major_works": [
    {"work_id": "changshengdian", "note": "传奇（C027：康熙二十七年写成）"},
    {"title": "四婵娟", "note": "杂剧（通说待核）"}],
  "style": [
    "以情写史：帝妃之恋与兴亡之叹（通说）。",
    "曲词典雅、音律谨严（通说待核）。",
    "遭政治压迫的清初剧坛境遇（C027）。"],
  "status": "《长生殿》为清初传奇代表作之一（C027）；'南洪北孔'并称（通说待核）。",
  "sources": ["C027"], "dates_source": "C027",
  "pending": ["生卒年（1645—1704）与钱塘（杭州）籍贯核对。", "长生殿案（1689年佟皇后丧期演出被革国子监监生说）待核。", "'南洪北孔'称谓出处待核。"]
},
"kongshangren": {
  "id": "kongshangren", "name": "孔尚任", "foreign_name": "Kong Shangren（孔尚任，1648—1718，生卒通说待核）",
  "country": "中国", "birth": 1648, "death": 1718, "birth_year": 1648, "death_year": 1718, "era": "古代",
  "summary": "孔尚任，清初戏曲家（孔子后裔说——通说待核）。传奇《桃花扇》'乃明清传奇压卷之作'，孔尚任'穷二十余年之心力，三易其稿'；'康熙三十八年六月，《桃花扇》终于脱稿'，'王公荐绅，莫不借钞，时有纸贵之誉'（光明日报 C028）；康熙帝看后不悦，次年将其遣返原籍（C028）。全剧'借离合之情，写兴亡之感'（C028）。",
  "timeline": [
    {"year": 1648, "text": "生于（1648年说——通说待核；孔子六十四代孙说待核）。", "src": "C028"},
    {"year": 1699, "text": "康熙三十八年六月《桃花扇》脱稿（光明日报 C028）。", "src": "C028"},
    {"year": 1700, "text": "康熙看后不悦，次年（1700年）找理由将其遣返原籍（C028）。", "src": "C028"},
    {"year": 1718, "text": "卒（1718年说——通说待核）。", "src": "C028"}],
  "major_works": [
    {"work_id": "taohuashan", "note": "传奇（C028：康熙三十八年脱稿）"},
    {"title": "小忽雷（与顾彩合撰）", "note": "（通说待核）"},
    {"title": "湖海集", "note": "诗集（通说待核）"}],
  "style": [
    "历史剧的真实观：'朝政得失，文人聚散'皆确考时地（通说待核——《桃花扇凡例》）。",
    "'借离合之情，写兴亡之感'（C028）。",
    "以道具（扇）贯穿兴亡（C028：'南朝兴亡，遂系之桃花扇底'）。"],
  "status": "《桃花扇》为'明清传奇压卷之作'（光明日报 C028）；其因剧获罪遣返的经历为清初文字环境之注脚（C028）。",
  "sources": ["C028"], "dates_source": "C028",
  "pending": ["生卒年与孔子后裔身份核对。", "《桃花扇》四十四出出目核对。", "1690年出仕国子监博士经历待核。"]
},
"aeschylus": {
  "id": "aeschylus", "name": "埃斯库罗斯", "foreign_name": "Aeschylus（埃斯库罗斯，约公元前525/524—前456/455）",
  "country": "古希腊", "birth": -525, "death": -456, "birth_year": -525, "death_year": -456, "era": "古代",
  "summary": "埃斯库罗斯，雅典悲剧家——'the first great Athenian tragedian'（第一位伟大的雅典悲剧家——Britannica），通过引入第二名演员改造了希腊戏剧，被称为'悲剧之父'（Britannica：Father of Tragedy）。'wrote approximately 90 plays'（约90部），今仅存7部完整悲剧（Britannica）；13次狄俄尼索斯戏剧节首奖（Britannica）。唯一存世完整三联剧《俄瑞斯忒亚》（458 BC，Britannica）。《被缚的普罗米修斯》虽归其名下，但'Why is the authorship of Prometheus Bound debated by scholars?'（作者归属存在学术争论——Britannica 页面问答）。",
  "timeline": [
    {"year": -525, "text": "生于（约前525/524——Britannica：Born 525/524 bc）。", "src": "B234"},
    {"year": -499, "text": "首次参加狄俄尼索斯戏剧节（Britannica：First competed at the Dionysia in 499 bc）。", "src": "B234"},
    {"year": -484, "text": "首获戏剧节冠军（Britannica：first victory in the spring of 484 bc）。", "src": "B234"},
    {"year": -458, "text": "《俄瑞斯忒亚》上演（Britannica：Oresteia produced in 458）。", "src": "B234"},
    {"year": -456, "text": "卒于西西里杰拉（Britannica：died 456/455 bc, Gela, Sicily）。", "src": "B234"}],
  "major_works": [
    {"work_id": "puluomixiusibang", "note": "悲剧（Britannica 语境；作者归属有争论）"},
    {"title": "俄瑞斯忒亚三部曲", "note": "（Britannica：458 BC）"},
    {"title": "七将攻忒拜、乞援人", "note": "（Britannica 存目）"}],
  "style": [
    "引入第二名演员：对话戏剧的开创（Britannica：adding a second actor）。",
    "'the most theological of the Greek tragedians'（Britannica 转引——其普罗米修斯被比于《约伯记》）。",
    "宏大而庄严的合唱与意象（通说）。"],
  "status": "Britannica 定位埃斯库罗斯为希腊悲剧之父；《俄瑞斯忒亚》为唯一存世完整三联剧（Britannica）。",
  "sources": ["B234", "B235"], "dates_source": "B234",
  "pending": ["《被缚的普罗米修斯》作者归属争论细节（学界主流观点）待核。", "恩提梅乌斯？——不：普罗米修斯三部曲（被缚/被释/带火者）散佚情况待核。", "悲剧节三剧一羊人剧规则（Britannica 已载）展开核对。"]
},
"euripides": {
  "id": "euripides", "name": "欧里庇得斯", "foreign_name": "Euripides（欧里庇得斯，约公元前484—前406）",
  "country": "古希腊", "birth": -484, "death": -406, "birth_year": -484, "death_year": -406, "era": "古代",
  "summary": "欧里庇得斯，雅典三大悲剧家的最后一位（Britannica：the last of classical Athens' three great tragic dramatists），以心理写实与对传统神话宗教的怀疑著称（Britannica）。生前比赛屡败、身后成为希腊化时代最受欢迎的悲剧家（Britannica 语境）。'Nineteen plays are extant'（含存疑者一部——Britannica），古代归于其名下者92部。《美狄亚》431 BCE 上演（Britannica）。",
  "timeline": [
    {"year": -484, "text": "约生于雅典（Britannica：Born c. 484 bc, Athens）。", "src": "B236"},
    {"year": -455, "text": "首次参加戏剧节（Britannica：first competed 455）。", "src": "B236"},
    {"year": -441, "text": "首获戏剧节冠军（Britannica：first victory 441）。", "src": "B236"},
    {"year": -431, "text": "《美狄亚》上演（Britannica：431 BCE）。", "src": "B236"},
    {"year": -406, "text": "卒于马其顿（Britannica：died 406, Macedonia）。", "src": "B236"}],
  "major_works": [
    {"work_id": "meidiya", "note": "悲剧（Britannica：431 BCE）"},
    {"title": "酒神的伴侣、特洛伊妇女", "note": "（通说待核）"},
    {"title": "伊菲革涅亚在奥利斯", "note": "（通说待核）"}],
  "style": [
    "心理写实：激情与疯狂的内在戏剧（Britannica 语境：psychological realism）。",
    "对神话与宗教的怀疑立场（Britannica：skeptical, questioning stance）。",
    "修辞与辩术的舞台化（通说）。"],
  "status": "Britannica 定位欧里庇得斯为三大悲剧家之末、希腊化时代最受欢迎者；存世悲剧19部（含存疑1部）。",
  "sources": ["B236"], "dates_source": "B236",
  "pending": ["美狄亚身份（科尔基斯公主）与复仇情节逐句核对。", "'机械降神'结局（太阳车）细节待核。", "马其顿晚年（阿卡劳斯宫廷）待核。"]
},
"ovid": {
  "id": "ovid", "name": "奥维德", "foreign_name": "Ovid（Publius Ovidius Naso，公元前43年3月20日—公元17年）",
  "country": "古罗马", "birth": -43, "death": 17, "birth_year": -43, "death_year": 17, "era": "古代",
  "summary": "奥维德（普布利乌斯·奥维德乌斯·纳索），奥古斯都时代罗马诗人（Britannica），《变形记》'fixed many Greek myths in their lasting literary forms'（使许多希腊神话定型于持久的文学形式——Britannica）。公元8年被奥古斯都流放黑海之滨的托米斯，终身未归（Britannica）；流放原因：'Ovid specifies two, his Ars amatoria and an offense'——坚称那是'indiscretion (error), not a crime (scelus)'（过失而非罪行——Britannica）。",
  "timeline": [
    {"year": -43, "text": "3月20日生于苏尔莫（Britannica：Born March 20, 43 bce, Sulmo）。", "src": "B237"},
    {"year": 8, "text": "被奥古斯都流放至黑海托米斯（Britannica：Exiled 8 ce, banished by Augustus to Tomis）。", "src": "B237"},
    {"year": 17, "text": "卒于托米斯（Britannica：Died 17 ce, Tomis）。", "src": "B237"}],
  "major_works": [
    {"work_id": "bianxingji_ovid", "note": "史诗（Britannica：15卷，约8 CE）"},
    {"title": "爱经（Ars amatoria）", "note": "（Britannica：流放原因之一）"},
    {"title": "哀歌集（Tristia）、黑海书简", "note": "（Britannica：流放期作品）"}],
  "style": [
    "'wit, rhetorical brilliance, and narrative and descriptive qualities'（Britannica 对《变形记》的评语）。",
    "神话的定型者：'Ovid gave many Greek legends their definitive forms for subsequent generations'（Britannica）。",
    "以'激情'为统一主题（Britannica：passion, not transformation, as the essential unifying theme）。"],
  "status": "Britannica 定位奥维德为奥古斯都时代诗人；'His verse had immense influence both by its imaginative interpretations of Classical myth and as an example of supreme technical accomplishment'（B237）。",
  "sources": ["B237", "B238"], "dates_source": "B237",
  "pending": ["流放具体原因（carmen et error 的史学界推测）待核。", "《变形记》与但丁/莎士比亚的接受史待核。", "《岁时记》待核。"]
},
"moliere": {
  "id": "moliere", "name": "莫里哀", "foreign_name": "Molière（莫里哀，本名让-巴蒂斯特·波克兰，1622-01-15受洗—1673-02-17）",
  "country": "法国", "birth": 1622, "death": 1673, "birth_year": 1622, "death_year": 1673, "era": "近代",
  "summary": "莫里哀，巴黎人，本名让-巴蒂斯特·波克兰（Britannica：born Jean-Baptiste Poquelin），法国演员与剧作家——'widely regarded as the finest writer of comedy in the French language'（公认法语喜剧最伟大的作家——Britannica）。1658年在卢浮宫为路易十四演出获王室青睐（Britannica）。'Many of his plays contained scandalous material. They were met with public outcry and were suppressed by the Roman Catholic Church.'（Britannica）。1673年2月17日舞台倒塌当日去世（Britannica：Collapsed onstage February 17, 1673——当日去世为通说待核）。",
  "timeline": [
    {"year": 1622, "text": "1月15日受洗于巴黎（Britannica：Baptized January 15, 1622, Paris）。", "src": "B240"},
    {"year": 1644, "text": "首次见于'莫里哀'艺名（Britannica：Stage name first documented June 28, 1644）。", "src": "B240"},
    {"year": 1658, "text": "10月24日在卢浮宫为路易十四演出（Britannica：Louvre performance October 24, 1658）。", "src": "B240"},
    {"year": 1664, "text": "《伪君子》首演（Britannica：produced in 1664——B241）。", "src": "B241"},
    {"year": 1673, "text": "2月17日台上倒塌当日去世（Britannica 语境+通说待核）。", "src": "B240"}],
  "major_works": [
    {"work_id": "weijunzi", "note": "喜剧（Britannica：1664/1669）"},
    {"title": "吝啬鬼、愤世嫉俗", "note": "（Britannica 语境：Le Misanthrope 等）"},
    {"title": "无病呻吟", "note": "（通说待核）"}],
  "style": [
    "性格喜剧：以单一性格缺陷推动全剧（通说）。",
    "利用即兴喜剧传统与芭蕾插曲（通说待核）。",
    "以笑声攻击伪善与教条（Britannica：suppressed by the Roman Catholic Church 语境）。"],
  "status": "Britannica 定位莫里哀为法语喜剧最伟大作家；《伪君子》为遭遇教会压制的代表作（B240/B241）。",
  "sources": ["B240", "B241"], "dates_source": "B240",
  "pending": ["《伪君子》五版禁演与1670年解禁年表核对。", "效仿西班牙剧团的13年外省巡演细节待核。", "法兰西喜剧院'莫里哀之家'传统（通说）待核。"]
},
"voltaire": {
  "id": "voltaire", "name": "伏尔泰", "foreign_name": "Voltaire（伏尔泰，本名弗朗索瓦-马利·阿鲁埃，1694-11-21—1778-05-30）",
  "country": "法国", "birth": 1694, "death": 1778, "birth_year": 1694, "death_year": 1778, "era": "近代",
  "summary": "伏尔泰，本名弗朗索瓦-马利·阿鲁埃（Britannica：pen name of François-Marie Arouet），法国作家与哲学家——'a central figure of the Enlightenment'（启蒙运动的中心人物——Britannica），其作品'attacked church authority, championed reason and religious tolerance, and influenced the French and American revolutions'（攻击教会权威、倡导理性与宗教宽容、影响法美革命——Britannica）。讽刺小说《老实人》1759年出版（Britannica：the satirical novel Candide (1759)）。《哲学书简》（1734）'was a landmark in the history of thought'（B239）。",
  "timeline": [
    {"year": 1694, "text": "11月21日生于巴黎（Britannica：Born November 21, 1694, Paris）。", "src": "B239"},
    {"year": 1734, "text": "《哲学书简》出版（Britannica：Lettres philosophiques (1734)）。", "src": "B239"},
    {"year": 1759, "text": "《老实人》出版（Britannica：Candide (1759)）。", "src": "B239"},
    {"year": 1778, "text": "5月30日卒于巴黎（Britannica：Died May 30, 1778, Paris）。", "src": "B239"}],
  "major_works": [
    {"work_id": "laoshiren", "note": "哲理小说（Britannica：1759）"},
    {"title": "哲学书简", "note": "（Britannica：1734）"},
    {"title": "路易十四时代、亨利亚特", "note": "史学与史诗（通说待核）"}],
  "style": [
    "反讽的启蒙论战文体（Britannica：attacked church authority 语境）。",
    "哲理小说：以荒诞旅程检验'乐观主义'（通说待核——莱布尼茨目标说）。",
    "史家笔法与戏剧并行（通说）。"],
  "status": "Britannica 定位伏尔泰为启蒙运动中心人物、法美革命的思想影响者；《老实人》为其最著名的讽刺小说（B239）。",
  "sources": ["B239"], "dates_source": "B239",
  "pending": ["'必须耕耘我们的园地'结尾句原文核对。", "《老实人》讽刺莱布尼茨式乐观主义的学界共识出处待核。", "里斯本地震（1755）进入小说的对应待核。"]
},
"hasek": {
  "id": "hasek", "name": "雅罗斯拉夫·哈谢克", "foreign_name": "Jaroslav Hašek（雅罗斯拉夫·哈谢克，1883-04-30—1923-01-03）",
  "country": "捷克", "birth": 1883, "death": 1923, "birth_year": 1883, "death_year": 1923, "era": "现当代",
  "summary": "哈谢克，布拉格人，捷克作家（Britannica），以讽刺小说《好兵帅克》传世。一战返回新建立的捷克斯洛伐克后专心写作（Britannica：devoted himself to writing），1921—23年出版《好兵帅克》，39岁早逝、小说未完成（Britannica：leaving it unfinished at his early death）。'The Good Soldier Schweik reflects the pacifist, antimilitary sentiments of post-World War I Europe'（B243）；帅克'invariably incompetent, and guileless, is forever colliding with the clumsy, dehumanized military bureaucracy'（B243）。原计划六卷、仅成三卷，第四卷由卡雷尔·瓦内克续成（Britannica）。",
  "timeline": [
    {"year": 1883, "text": "4月30日生于布拉格（Britannica：Born April 30, 1883, Prague）。", "src": "B243"},
    {"year": 1921, "text": "《好兵帅克》开始出版（1921—23）（Britannica：published 1921–23）。", "src": "B243"},
    {"year": 1923, "text": "1月3日卒于利普尼采（Britannica：died Jan. 3, 1923, Lipnice nad Sázavou）。", "src": "B243"}],
  "major_works": [
    {"work_id": "haobingshuaike", "note": "讽刺小说（Britannica：1921—23）"},
    {"title": "好兵帅克前传短篇", "note": "（通说待核）"}],
  "style": [
    "天真的反讽：帅克的'乖顺'即对抗（Britannica：naïveté is the main vehicle for Hašek's mockery of authority）。",
    "反军国主义与和平主义（Britannica：pacifist, antimilitary sentiments）。",
    "布拉格酒馆幽默与卡雷尔·瓦内克续稿公案（通说待核）。"],
  "status": "Britannica 定位哈谢克为以《好兵帅克》传世的捷克讽刺作家；未完成的六卷计划（成三卷+第四卷由他人续成）为其文学史公案（B243）。",
  "sources": ["B243"], "dates_source": "B243",
  "pending": ["帅克人物原型（弗里格尔犬贩说）待核。", "雷纳译本与哈谢克 anarchist 经历待核。", "捷克原版插图（约瑟夫·拉达）待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

# ---------- works ----------
works = {
"changshengdian": {
  "id":"changshengdian","title":"长生殿","original_title":"长生殿（传奇，二卷五十出）","region":"中国","era":"古代","era_detail":"清（康熙）",
  "genre":"传奇（戏曲）","genre_group":"戏剧","language":"汉语（曲牌体）","author_id":"hongsheng","author_name":"洪昇",
  "year_display":"写成于康熙二十七年（1688）（光明日报 C027）","year_sort":1688,
  "background":["光明日报（C027）：'《长生殿》写成于康熙二十七年（1688）'；与《桃花扇》一样'都遭到了很大的政治压迫，难以摆脱以古讽今的指责'。","题材：唐明皇与杨贵妃的帝妃爱情（通说；取材《长恨歌》系——通说待核）。"],
  "outline":["定情→霓裳羽衣→马嵬之变→冥追→雨梦——以情亡国、以情复生（出目通说待核）。","后半以仙界重圆收束（通说待核）。"],
  "characters":[{"name":"李隆基（唐明皇）","identity":"皇帝","note":"帝妃恋（通说）"},{"name":"杨玉环","identity":"贵妃","note":"马嵬之殇（通说）"},{"name":"李龟年等","identity":"乐工","note":"兴亡见证（通说待核）"}],
  "themes":["'逞情'与'勤政'的矛盾（通说待核——作者自序语）。",
   "兴亡之感的戏曲化（C027：以古讽今的指责）。",
   "昆曲音乐的集大成（通说待核）。"],
  "influence":[{"text":"光明日报：'《长生殿》写成于康熙二十七年（1688）'，与《桃花扇》同为康熙年间遭受政治压迫的名剧（C027）。","source":"C027"},
   {"text":"与《桃花扇》并称清初剧坛双璧、'南洪北孔'（通说待核）。","source":"C027"}],
  "reading":{"difficulties":["曲牌体唱词的格律。","天宝掌故的注释。"],
   "editions":["《长生殿》（人民文学出版社，通说待核）。"],
   "order":"先读《定情》《絮阁》《埋玉》《雨梦》四出（通说）。"},
  "pending":["五十出出目核对。","长生殿案（1689年丧期演出革监生说）待核。","取材《长恨歌》《梧桐雨》的谱系核对。"],
  "sources":["C027"],"year_source":"C027","author_source":"C027","related_works":["mudanting","doueyuan","xixiangji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《长生殿》帝妃情节结构图",
    "cards":[{"title":"定情","text":"七月长生殿","color":"family"},{"title":"霓裳羽衣","text":"盛世之音","color":"gold"},{"title":"埋玉","text":"马嵬之变","color":"antagonist"},{"title":"重圆","text":"仙界团圆","color":"main"}]}
},
"taohuashan": {
  "id":"taohuashan","title":"桃花扇","original_title":"桃花扇（传奇，四十四出）","region":"中国","era":"古代","era_detail":"清（康熙）",
  "genre":"传奇（戏曲）","genre_group":"戏剧","language":"汉语（曲牌体）","author_id":"kongshangren","author_name":"孔尚任",
  "year_display":"康熙三十八年（1699）六月脱稿（光明日报 C028）","year_sort":1699,
  "background":["光明日报（C028）：'《桃花扇》乃明清传奇压卷之作'；孔尚任'穷二十余年之心力，三易其稿'；脱稿后'王公荐绅，莫不借钞，时有纸贵之誉'；康熙看后不悦、次年将其遣返原籍。","主旨：'借离合之情，写兴亡之感'（C028）；'南朝兴亡，遂系之桃花扇底'（C028）。"],
  "outline":["复社名士侯方域与秦淮歌伎李香君的悲欢离合，置于复社文人与马士英、阮大铖等阉党余孽的冲突中（C028）。","结局虚构'入道'：侯李面对残破江山'修真学道'，宣告王朝历史的终结（C028）。"],
  "characters":[{"name":"侯方域","identity":"复社名士","note":"离合线（C028）"},{"name":"李香君","identity":"秦淮歌伎","note":"却奁·骂筵（通说待核）"},{"name":"阮大铖","identity":"阉党余孽","note":"反派（C028）"}],
  "themes":["兴亡之感压倒离合之情（C028）。",
   "历史剧的真实原则（通说待核——凡例语）。",
   "扇为兴亡之证（C028）。"],
  "influence":[{"text":"光明日报：明清传奇压卷之作；'借离合之情，写兴亡之感'（C028）。","source":"C028"},
   {"text":"2006年青春版昆剧《1699·桃花扇》首演（C028 语境）。","source":"C028"}],
  "reading":{"difficulties":["南明史事（弘光朝）注释。","四十余出出目与人物。"],
   "editions":["《桃花扇》（人民文学出版社，通说待核）。"],
   "order":"先读《却奁》《骂筵》《余韵》（通说）。"},
  "pending":["四十四出出目核对。","孔尚任生卒（1648—1718）与孔子后裔身份待核。","《余韵》出苏柳生等人物核对。"],
  "sources":["C028"],"year_source":"C028","author_source":"C028","related_works":["changshengdian","mudanting","doueyuan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《桃花扇》离合兴亡结构图",
    "cards":[{"title":"却奁","text":"拒绝阉党之资","color":"main"},{"title":"骂筵","text":"香君之烈","color":"antagonist"},{"title":"入道","text":"王朝的终结（C028）","color":"gold"},{"title":"桃花扇底","text":"南朝兴亡","color":"family"}]}
},
"puluomixiusibang": {
  "id":"puluomixiusibang","title":"被缚的普罗米修斯","original_title":"Promētheus Desmōtēs（Prometheus Bound）","region":"古希腊","era":"古代","era_detail":"古典时代",
  "genre":"悲剧","genre_group":"戏剧","language":"古希腊语","author_id":"aeschylus","author_name":"埃斯库罗斯（作者归属有争论——Britannica）",
  "year_display":"创作年代不确定（Britannica：the dating of which is uncertain）","year_sort":-450,
  "background":["Britannica：普罗米修斯'has saved humanity with his gift of fire'（以火赠人类）；'For this act Zeus has ordered that he be chained to a remote crag'（因此被缚于荒崖——Britannica）。","作者归属：Britannica 页面问答提出'Why is the authorship of Prometheus Bound debated by scholars?'（B234）。"],
  "outline":["权势与暴力神将普罗米修斯钉上高加索悬崖——赫菲斯托斯执行（通说）。","来客：俄刻阿诺斯、俄刻阿尼得斯歌队、伊奥、赫尔墨斯（Britannica：visited by Oceanus, a chorus of Oceanus's daughters, Io, and Hermes）。","结尾：普罗米修斯拒泄预言、与赫尔墨斯对峙坠入深渊（通说待核）。"],
  "characters":[{"name":"普罗米修斯","identity":"提坦神","note":"人类的恩人（Britannica）"},{"name":"宙斯（僭主）","identity":"新王","note":"压迫者（Britannica 语境）"},{"name":"伊奥","identity":"受宙斯迫害者","note":"受害者互证（通说）"}],
  "themes":["反抗僭主的正义（通说）。",
   "知识即痛苦的预言（通说待核）。",
   "技术文明的恩人神话（通说）。"],
  "influence":[{"text":"Britannica：希腊悲剧中被缚赠火者的经典舞台（B235 语境）。","source":"B235"},
   {"text":"浪漫主义以降的'普罗米修斯'再造（雪莱《解放了的普罗米修斯》——通说待核）。","source":"B235"}],
  "reading":{"difficulties":["古希腊神系谱。","作者归属争论——阅读时以'埃斯库罗斯名下'看待。"],
   "editions":["《罗念生全集》悲剧卷（上海人民出版社，通说待核）。","英文译本（公有领域）。"],
   "order":"可与《约伯记》对读（Britannica 曾以之相比——通说待核）。"},
  "pending":["作者归属争论的主流观点核对。","三部曲散佚（被释的普罗米修斯说）待核。","上演年代（前460年代说）待核。"],
  "sources":["B235","B234"],"year_source":"B235","author_source":"B234","related_works":["oedipus","meidiya","shenqu"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《被缚的普罗米修斯》结构图",
    "cards":[{"title":"赠火","text":"拯救人类（Britannica）","color":"main"},{"title":"钉崖","text":"宙斯的惩罚","color":"antagonist"},{"title":"伊奥","text":"受害者的互证","color":"family"},{"title":"坠渊","text":"拒绝泄密的结局","color":"gold"}]}
},
"meidiya": {
  "id":"meidiya","title":"美狄亚","original_title":"Μήδεια（Medea）","region":"古希腊","era":"古代","era_detail":"古典时代",
  "genre":"悲剧","genre_group":"戏剧","language":"古希腊语","author_id":"euripides","author_name":"欧里庇得斯",
  "year_display":"公元前431年上演（Britannica：431 BCE）","year_sort":-431,
  "background":["Britannica：'a tragedy exploring injustice and revenge'（探不公与复仇的悲剧）；'Medea determines that she will punish Jason by murdering not only her own sons but also the Corinthian princess'（杀子以罚负心——Britannica）。","作者：三大悲剧家最后一位、以心理写实著称（B236）。"],
  "outline":["伊阿宋另娶科林斯公主；美狄亚被放逐（通说）。","假意和解：赠毒袍——公主与国王之死（通说待核）。","杀子复仇，驾日车离去（Britannica 语境+通说）。"],
  "characters":[{"name":"美狄亚","identity":"科尔基斯公主","note":"复仇者（Britannica）"},{"name":"伊阿宋","identity":"阿尔戈英雄","note":"负心者（通说）"}],
  "themes":["不公与复仇的悲剧（Britannica：exploring injustice and revenge）。",
   "异乡人（barbarian）的身份暴力（通说待核）。",
   "母性与复仇的悖论（通说）。"],
  "influence":[{"text":"Britannica：欧里庇得斯最著名的作品之一（one of his most famous works）。","source":"B236"},
   {"text":"女性复仇叙事的原型：后世文学与影视的母题（通说待核）。","source":"B236"}],
  "reading":{"difficulties":["希腊神话前史（金羊毛）注释。","申辩辞的长篇修辞。"],
   "editions":["《罗念生全集》悲剧卷（通说待核）。","英文译本（公有领域）。"],
   "order":"对照《被缚的普罗米修斯》：两种反抗。"},
  "pending":["毒袍与日车结局细节核对。","克瑞翁/格劳刻人名核对。","科林斯上演未获首奖说待核。"],
  "sources":["B236"],"year_source":"B236","author_source":"B236","related_works":["oedipus","puluomixiusibang","leiyu"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《美狄亚》复仇结构图",
    "cards":[{"title":"被弃","text":"异乡的背叛","color":"family"},{"title":"毒袍","text":"假意和解","color":"antagonist"},{"title":"杀子","text":"最深的惩罚（Britannica）","color":"main"},{"title":"日车","text":"逃逸与遗留","color":"gold"}]}
},
"bianxingji_ovid": {
  "id":"bianxingji_ovid","title":"变形记（奥维德）","original_title":"Metamorphoses","region":"古罗马","era":"古代","era_detail":"奥古斯都时代",
  "genre":"叙事史诗","genre_group":"诗歌","language":"拉丁语","author_id":"ovid","author_name":"奥维德（Publius Ovidius Naso）",
  "year_display":"约公元8年成书（Britannica：poem in 15 books, written in Latin about 8 ce）","year_sort":8,
  "background":["Britannica：'a collection of mythological and legendary stories, told in chronological order from the creation'（从创世起按时序讲述的神话传说集）；15卷六音步史诗（B238）。","主题（Britannica）：'passion, not transformation, as the essential unifying theme'——统一主题是激情而非变形本身（B238）。"],
  "outline":["从创世的混沌到'死亡与成神的凯撒'——'the death and deification of Julius Caesar'为最终变形（B238）。","著名变形：达佛涅、那喀索斯、俄耳甫斯等（篇目通说待核）。"],
  "characters":[{"name":"诸神与英雄","identity":"群像","note":"变形的多棱镜"}],
  "themes":["激情作为统一主题（Britannica）。",
   "神话的权威定型：'Ovid gave many Greek legends their definitive forms for subsequent generations'（B237）。",
   "wit 与修辞的华丽（B238：noted for its wit, rhetorical brilliance）。"],
  "influence":[{"text":"Britannica：'His verse had immense influence both by its imaginative interpretations of Classical myth and as an example of supreme technical accomplishment'（B237）。","source":"B237"},
   {"text":"中世纪以降欧洲文学的'奥维德传统'（通说待核）。","source":"B237"}],
  "reading":{"difficulties":["15卷的连续性——按神话谱系而非情节。","拉丁文格律（中译依赖转译）。"],
   "editions":["杨周翰译本？（《变形记》中译本信息待核）。","英文译本（Melville/Mandre 公有领域部分）。"],
   "order":"先读卷一（创世—洪水）与卷十五（凯撒成神）首尾。"},
  "pending":["中译本信息核对。","达佛涅等名篇出处卷次核对。","凯撒成神与奥古斯都颂诗的政治性待核。"],
  "sources":["B238","B237"],"year_source":"B238","author_source":"B237","related_works":["aeneid","shenqu","yisuo"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《变形记》15卷时间轴",
    "cards":[{"title":"创世","text":"混沌→秩序","color":"family"},{"title":"诸神时代","text":"激情的变形","color":"main"},{"title":"英雄时代","text":"俄耳甫斯等","color":"gold"},{"title":"凯撒成神","text":"最后的变形","color":"plain"}]}
},
"weijunzi": {
  "id":"weijunzi","title":"伪君子","original_title":"Le Tartuffe; ou, l'imposteur（Tartuffe）","region":"法国","era":"近代","era_detail":"路易十四时代",
  "genre":"五幕喜剧","genre_group":"戏剧","language":"法语","author_id":"moliere","author_name":"莫里哀（Molière）",
  "year_display":"1664年首演、1669年出版（Britannica：produced in 1664 and published in French in 1669）","year_sort":1669,
  "background":["Britannica：五幕喜剧，又名'The Imposter'（骗子）；达尔杜弗——'a pious-seeming fraud'（貌似虔诚的骗子）几乎毁掉富商奥尔恭一家；'Elmire, Orgon's wife, sees through Tartuffe's wicked hypocrisy and exposes him'（妻子艾耳密尔识破伪善——Britannica）。","压制（Britannica B240）：'They were met with public outcry and were suppressed by the Roman Catholic Church.'（该剧遭遇教会压制——通说待核：1664—1669禁演年表）。"],
  "outline":["奥尔恭迷上'虔诚'的达尔杜弗，逐子赠产（通说）。","桌下窃听：艾耳密尔设局让丈夫亲见（Britannica：sees through……and exposes him）。","圣旨解围：国王的英明收束（通说待核——尾声对王权的颂词）。"],
  "characters":[{"name":"达尔杜弗","identity":"伪信士","note":"伪善的化身（Britannica）"},{"name":"奥尔恭","identity":"富商家长","note":"被蒙蔽者"},{"name":"艾耳密尔","identity":"奥尔恭之妻","note":"识破者（Britannica）"},{"name":"道丽娜","identity":"女仆","note":"最清醒的人（通说）"}],
  "themes":["宗教伪善的喜剧解剖（Britannica 语境）。",
   "父权与家庭财产的荒诞（通说）。",
   "仆人的智慧：道丽娜（通说）。"],
  "influence":[{"text":"Britannica：莫里哀'widely regarded as the finest writer of comedy in the French language'（B240）。","source":"B240"},
   {"text":"'Tartuffe'成为语言中的伪善代名词（通说待核）。","source":"B241"}],
  "reading":{"difficulties":["亚历山大体诗行（中译需看韵文/散文版本）。","1660年代法国宗教政治背景。"],
   "editions":["李健吾译本（上海译文出版社，通说待核）。","法文原版（公有领域）。"],
   "order":"一次读完（五幕紧凑）；对照《悭吝人》。"},
  "pending":["1664—1669禁演年表核对。","李健吾译本信息核对。","结尾颂王权一幕的解读争议待核。"],
  "sources":["B241","B240"],"year_source":"B241","author_source":"B240","related_works":["luerwang","rulin","aoman"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《伪君子》骗局结构图",
    "cards":[{"title":"入宅","text":"虔士的表演","color":"family"},{"title":"赠产","text":"奥尔恭的痴迷","color":"antagonist"},{"title":"桌下窃听","text":"艾耳密尔识破（Britannica）","color":"main"},{"title":"圣旨","text":"解围（通说）","color":"gold"}]}
},
"laoshiren": {
  "id":"laoshiren","title":"老实人","original_title":"Candide, ou l'Optimisme（Candide）","region":"法国","era":"近代","era_detail":"启蒙时代",
  "genre":"哲理小说","genre_group":"小说","language":"法语","author_id":"voltaire","author_name":"伏尔泰（Voltaire）",
  "year_display":"1759年出版（Britannica：the satirical novel Candide (1759)）","year_sort":1759,
  "background":["Britannica：伏尔泰为'central figure of the Enlightenment'，《老实人》为其讽刺小说（B239）。","讽刺目标：'乐观主义'（莱布尼茨式'一切皆善'说——通说待核；Britannica 该页未载目标）。"],
  "outline":["憨第德（Candide）被逐出城堡：从战场、地震、宗教裁判到黄金国——一路荒诞（通说）。","庞格罗斯师的'一切皆善'不断被现实打脸（通说待核）。","结尾：'必须耕耘我们的园地'（名句通说待核——il faut cultiver notre jardin）。"],
  "characters":[{"name":"憨第德（Candide）","identity":"青年","note":"天真的旅人"},{"name":"庞格罗斯","identity":"哲学教师","note":"乐观主义化身（通说）"},{"name":"居内贡","identity":"城堡小姐","note":"爱慕对象（通说）"}],
  "themes":["对盲目乐观主义的清算（通说待核）。",
   "灾难的目录：战争、地震、宗教裁判（通说）。",
   "退出玄谈、耕耘园地（名句待核）。"],
  "influence":[{"text":"Britannica：伏尔泰'attacked church authority, championed reason and religious tolerance, and influenced the French and American revolutions'（B239）——《老实人》为其通俗化载体。","source":"B239"},
   {"text":"哲理小说文体的典范（通说）。","source":"B239"}],
  "reading":{"difficulties":["章回式的快节奏讽刺——辨明史实影射。","1755里斯本地震等事件背景（通说）。"],
   "editions":["傅雷译本（人民文学出版社，通说待核）。","法文原版（公有领域）。"],
   "order":"对照《格列佛游记》：两种启蒙讽刺。"},
  "pending":["'耕耘园地'结尾原文核对。","莱布尼茨乐观主义目标说出处待核。","1759年匿名初版（日内瓦说）待核。"],
  "sources":["B239"],"year_source":"B239","author_source":"B239","related_works":["geliefo","meilixinshijie","gulage"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《老实人》荒诞旅程图",
    "cards":[{"title":"逐出城堡","text":"天真的开始","color":"family"},{"title":"战争与地震","text":"'一切皆善'的破产","color":"antagonist"},{"title":"黄金国","text":"乌托邦的一瞥","color":"gold"},{"title":"耕耘园地","text":"结尾（名句待核）","color":"main"}]}
},
"jierjiamieshishi": {
  "id":"jierjiamieshishi","title":"吉尔伽美什史诗","original_title":"Epic of Gilgamesh（阿卡德语版）","region":"美索不达米亚","era":"古代","era_detail":"美索不达米亚（最完整文本约公元前7世纪）",
  "genre":"史诗","genre_group":"诗歌","language":"阿卡德语","author_id":None,"author_name":"美索不达米亚多代文人层累而成（作者不可考）",
  "year_display":"'often cited as the earliest significant work of surviving literature'（Britannica）；最完整文本为尼尼微出土12块阿卡德语残板（Britannica）","year_sort":-650,
  "background":["Britannica：'an ancient Mesopotamian poem in Akkadian about Gilgamesh, a part-divine king of Uruk who quests for immortality after his friend Enkidu dies'（半神乌鲁克王在挚友死后寻求永生——B242）；'often cited as the earliest significant work of surviving literature'（常被引为存世文学中最早的重要作品——B242）。","文本（B242）：最完整者为尼尼微亚述巴尼拔图书馆出土的'12 incomplete Akkadian-language tablets'（12块残板）。"],
  "outline":["为驯服暴君，神造恩奇都；二人搏斗后结为挚友，共诛天牛（B242 转述）。","恩奇都之死→吉尔伽美什寻乌特纳皮什提姆（'survivor of the Babylonian Flood'——B242）求永生（B242）。","得青春草又被蛇夺走——接受必死（B242）。","洪水故事与《创世记》的平行（通说待核）。"],
  "characters":[{"name":"吉尔伽美什","identity":"乌鲁克王","note":"三分之二神性（通说）"},{"name":"恩奇都","identity":"神造野人","note":"挚友（B242）"},{"name":"乌特纳皮什提姆","identity":"洪水幸存者","note":"永生的见证者（B242）"}],
  "themes":["死亡与友谊：接受必死的教育（B242）。",
   "洪水母题的最早文本之一（通说待核）。",
   "城邦记忆的刻写（泥板——通说）。"],
  "influence":[{"text":"Britannica：'often cited as the earliest significant work of surviving literature'（B242）。","source":"B242"},
   {"text":"对后世洪水叙事与英雄史诗的原型意义（通说待核）。","source":"B242"}],
  "reading":{"difficulties":["残板缺文与译本差异。","美索不达米亚神名系统。"],
   "editions":["《吉尔伽美什》（译林出版社/商务印书馆版本，通说待核）。","英译（Andrew George 版，通说待核）。"],
   "order":"先读第1—8块板（友谊与死亡）→ 洪水板 → 第11—12块板。"},
  "pending":["十二块板内容分配核对。","古巴比伦旧版（约前18世纪说）与苏美尔五首独立诗歌的谱系待核。","中译本信息核对。"],
  "sources":["B242"],"year_source":"B242","author_source":"B242","related_works":["shiji","iliad","odyssey"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《吉尔伽美什》寻索结构图",
    "cards":[{"title":"搏斗结友","text":"恩奇都（B242）","color":"family"},{"title":"天牛","text":"共诛的僭越","color":"gold"},{"title":"寻永生","text":"洪水见证者","color":"main"},{"title":"蛇夺草","text":"接受必死","color":"antagonist"}]}
},
"haobingshuaike": {
  "id":"haobingshuaike","title":"好兵帅克","original_title":"Osudy dobrého vojáka Švejka za světové války（The Good Soldier Švejk）","region":"捷克","era":"现当代","era_detail":"20世纪（一战后）",
  "genre":"讽刺小说","genre_group":"小说","language":"捷克语","author_id":"hasek","author_name":"雅罗斯拉夫·哈谢克",
  "year_display":"1921—1923年出版（Britannica：published 1921–23）","year_sort":1921,
  "background":["Britannica：'The Good Soldier Schweik reflects the pacifist, antimilitary sentiments of post-World War I Europe'（反映一战后欧洲的反战与反军国情绪——B243）。","帅克'invariably incompetent, and guileless, is forever colliding with the clumsy, dehumanized military bureaucracy'——其天真'is the main vehicle for Hašek's mockery of authority'（B243）。","未完成：原计划六卷、仅成三卷，第四卷由卡雷尔·瓦内克续成（B243）。"],
  "outline":["帅克以'白痴式忠诚'应征入伍：征兵局、随军神父、火车、前线（通说）。","每一步都与笨拙而无人性的军事官僚机构相撞（Britannica：forever colliding with……）。"],
  "characters":[{"name":"帅克","identity":"好兵","note":"天真反讽的主角（B243）"},{"name":"杜布中尉","identity":"军官","note":"官僚机器的代表（通说待核）"}],
  "themes":["反战与反军国主义（Britannica：pacifist, antimilitary sentiments）。",
   "以天真瓦解权威（Britannica：mockery of authority）。",
   "奥匈帝国官僚的荒诞（Britannica：clumsy, dehumanized military bureaucracy）。"],
  "influence":[{"text":"Britannica：一战后欧洲反战文学的代表作之一（语境）。","source":"B243"},
   {"text":"'帅克式'人物成为捷克民族性格的漫画符号（通说待核）。","source":"B243"}],
  "reading":{"difficulties":["奥匈军制与捷克语双关。","未完成结构——阅读时注意续稿。"],
   "editions":["萧乾译本（人民文学出版社，通说待核）。","捷克原版插图（拉达画本——通说待核）。"],
   "order":"对照《动物农场》《五号屠场》：反战的两种笑法。"},
  "pending":["人物名（杜布/卡茨）核对。","哈谢克的无政府主义经历待核。","六卷计划细节核对。"],
  "sources":["B243"],"year_source":"B243","author_source":"B243","related_works":["bianxingji","wuhao","sihunling"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《好兵帅克》撞机结构图",
    "cards":[{"title":"征兵局","text":"体检的闹剧","color":"family"},{"title":"随军神父","text":"酒馆的战争","color":"gold"},{"title":"开赴前线","text":"官僚机器（Britannica）","color":"antagonist"},{"title":"天真","text":"帅克的武器","color":"main"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
