# -*- coding: utf-8 -*-
"""流水线批次10：Britannica 新核 2 作家 2 部 + 零成本直写 4 部"""
import json, pathlib

new_src = [
{"id":"B293","title":"Daniel Defoe — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Daniel-Defoe","type":"百科全书","verified":True,"covers":["defoe","moerflandes"],"note":"2026-11-21 核对：1660年伦敦生—1731-04-24伦敦卒（71岁）；'Defoe was 59 when he published his first novel, Robinson Crusoe, which brought him lasting fame'；'Daniel Defoe is best known as the writer of the novels Robinson Crusoe (1719) and Moll Flanders (1722)'；Review 杂志'undoubtedly had a considerable influence on the development of later essay periodicals'（如 The Tatler 与 The Spectator）；'英国小说之父'说法见于关联问答标题（正文未直接载——待核）"},
{"id":"B294","title":"Robert Louis Stevenson — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Robert-Louis-Stevenson","type":"百科全书","verified":True,"covers":["stevenson","huashenboshi"],"note":"2026-11-21 核对：1850-11-13爱丁堡生—1894-12-03萨摩亚瓦伊利马卒（44岁）；'best known for his novels Treasure Island (1881), Kidnapped (1886)'（页面Quick Facts 作1881——通行1883年说待核）；化身博士相关仅见链接与问答、正文未载——1886年说通说待核；'a writer of originality and power who produced brilliant adventure stories with subtle moral overtones'；1875年获苏格兰律师资格、1880年与范妮·奥斯本结婚、晚年居萨摩亚"},
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

authors = {
"defoe": {
  "id": "defoe", "name": "丹尼尔·笛福", "foreign_name": "Daniel Defoe（丹尼尔·笛福，1660—1731-04-24）",
  "country": "英国", "birth": 1660, "death": 1731, "birth_year": 1660, "death_year": 1731, "era": "近代",
  "summary": "笛福，伦敦人，英国小说家、小册子作者与记者——经商与政治写作之后，'Defoe was 59 when he published his first novel, Robinson Crusoe, which brought him lasting fame'（59岁出版首部小说《鲁滨逊漂流记》并获持久声名——Britannica B293）；'best known as the writer of the novels Robinson Crusoe (1719) and Moll Flanders (1722)'（B293）。其《评论》杂志'undoubtedly had a considerable influence on the development of later essay periodicals'（对后世随笔期刊影响重大——B293）。关联问答称其为'英国小说之父'（B293 页面问答标题——正文未直接载，待核）。",
  "timeline": [
    {"year": 1660, "text": "生于伦敦（B293：Born 1660, London, England）。", "src": "B293"},
    {"year": 1719, "text": "59岁出版首部小说《鲁滨逊漂流记》（B293）。", "src": "B293"},
    {"year": 1722, "text": "《摩尔·弗兰德斯》出版（B293：Moll Flanders (1722)）。", "src": "B293"},
    {"year": 1731, "text": "4月24日卒于伦敦（B293：Died April 24, 1731, London）。", "src": "B293"}],
  "major_works": [
    {"work_id": "moerflandes", "note": "长篇（B293：1722）"},
    {"title": "鲁滨逊漂流记", "note": "（B293：1719——本库另条 lubinxun）"},
    {"title": "瘟疫年纪事", "note": "（通说待核）"}],
  "style": [
    "第一人称的'拟真'叙述（通说待核——伪自传体）。",
    "《评论》对随笔期刊的奠基（B293）。",
    "小册子与新闻写作的现实感（B293 语境：pamphleteer and journalist）。"],
  "status": "Britannica 定位笛福为英国小说家、小册子作者与记者（《鲁滨逊漂流记》《摩尔·弗兰德斯》作者）；'英国小说之父'之说见于关联问答（B293——待核）。",
  "sources": ["B293"], "dates_source": "B293",
  "pending": ["生年1660（具体日期不详）核对。", "'英国小说之父'正文的直接表述待核。", "《瘟疫年纪事》1722年待核。"]
},
"stevenson": {
  "id": "stevenson", "name": "罗伯特·路易斯·史蒂文森", "foreign_name": "Robert Louis Stevenson（罗伯特·路易斯·史蒂文森，1850-11-13—1894-12-03）",
  "country": "英国", "birth": 1850, "death": 1894, "birth_year": 1850, "death_year": 1894, "era": "近代",
  "summary": "史蒂文森，爱丁堡人，苏格兰散文家、诗人与小说、游记作家——'a writer of originality and power who produced brilliant adventure stories with subtle moral overtones'（以原创与力量写出带微妙道德意味的精彩冒险故事——Britannica B294）。'best known for his novels Treasure Island (1881), Kidnapped (1886)'（《金银岛》《绑架》——B294 Quick Facts；金银岛通行1883年说待核）。放弃法律改从文学，晚年居萨摩亚（B294）。",
  "timeline": [
    {"year": 1850, "text": "11月13日生于爱丁堡（B294：Born November 13, 1850, Edinburgh, Scotland）。", "src": "B294"},
    {"year": 1875, "text": "获苏格兰律师资格（B294：Called to the Scottish bar July 1875）。", "src": "B294"},
    {"year": 1880, "text": "与范妮·奥斯本结婚（B294：married Fanny Osbourne early 1880）。", "src": "B294"},
    {"year": 1886, "text": "《化身博士》出版（通说待核；B294 Quick Facts 载 Kidnapped (1886)）。", "src": "B294"},
    {"year": 1894, "text": "12月3日卒于萨摩亚瓦伊利马（B294：Died December 3, 1894, Vailima, Samoa）。", "src": "B294"}],
  "major_works": [
    {"work_id": "huashenboshi", "note": "中篇（1886年说——通说待核）"},
    {"title": "金银岛、绑架", "note": "（B294：Treasure Island、Kidnapped (1886)）"},
    {"title": "儿童诗园", "note": "（通说待核）"}],
  "style": [
    "'原创与力量'的冒险故事、'微妙的道德意味'（B294）。",
    "善恶双重人格的心理分化（《化身博士》——通说待核）。",
    "游记与冒险的交织（B294 语境：fiction and travel writer）。"],
  "status": "Britannica 定位史蒂文森为苏格兰散文家、诗人与小说/游记作家（'原创与力量'——B294）；44岁早逝于萨摩亚（B294）。",
  "sources": ["B294"], "dates_source": "B294",
  "pending": ["《金银岛》1883年（书刊年份）与 Britannica 页 1881 说核对。", "《化身博士》1886年出版细节核对。", "萨摩亚晚年（'Vailima'居所）待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"taileisi": {
  "id":"taileisi","title":"苔蕾丝·德斯盖鲁","original_title":"Thérèse Desqueyroux","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"mauriac","author_name":"弗朗索瓦·莫里亚克",
  "year_display":"1927年（作者页 B289 口径：Thérèse Desqueyroux published 1927）","year_sort":1927,
  "background":["作者页（B289）：莫里亚克 major_works 载'苔蕾丝·德斯盖鲁'（B289 作者页定位，详见 aidewangmo 条核对）。","Britannica（B289）：'whose heroine is driven to attempt the murder of her husband to escape her suffocating life'（女主人公为逃离窒息生活而试图谋杀丈夫——B289）。"],
  "outline":["苔蕾丝毒害丈夫伯纳德未遂——家族的'庇护'与无罪释放（通说待核）。","结尾：'自由'的荒凉（通说待核）。"],
  "characters":[{"name":"苔蕾丝","identity":"妻子","note":"投毒者（B289）"},{"name":"伯纳德","identity":"丈夫","note":"（通说待核）"}],
  "themes":["窒息的婚姻与谋杀（B289）。",
   "'自由'的荒凉（通说待核）。",
   "天主教罪恶观（B289 作者级语境）。"],
  "influence":[{"text":"Britannica：'whose heroine is driven to attempt the murder of her husband'（B289）。","source":"B289"},
   {"text":"Britannica：1952年诺奖（B289 作者级）。","source":"B289"}],
  "reading":{"difficulties":["心理剧的封闭结构。","波尔多资产阶级语境。"],
   "editions":["《苔蕾丝·德斯盖鲁》（广西师范大学出版社，通说待核）。","法文原版（公有领域渐近）。"],
   "order":"先《爱的荒漠》后本作。"},
  "pending":["1927年出版（Grasset说）核对。","苔蕾丝/伯纳德人名核对。","1950年电影改编待核。"],
  "sources":["B289"],"year_source":"B289","author_source":"B289","related_works":["aidewangmo","lianqingdezhongjie","ouyeni"],
  "svg":G2("《苔蕾丝》窒息结构图",[{"title":"投毒","text":"逃离的未遂","color":"antagonist"},{"title":"家族","text":"无罪的庇护","color":"family"},{"title":"苔蕾丝","text":"窒息的妻子","color":"main"},{"title":"自由","text":"荒凉的出路","color":"gold"}])
},
"zhongjiedeganjue": {
  "id":"zhongjiedeganjue","title":"终结的感觉","original_title":"The Sense of an Ending","region":"英国","era":"现当代","era_detail":"21世纪",
  "genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"barnes","author_name":"朱利安·巴恩斯",
  "year_display":"2011年（Britannica：2011年布克奖——'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'）","year_sort":2011,
  "background":["作者页（B290）：巴恩斯 major_works 载'终结的感觉'（B290 作者页定位，详见 fuloubaideyingwu 条核对）。","Britannica（B290）：'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'（以不可靠叙述者探察记忆与衰老——B290）。"],
  "outline":["退休律师托尼的回忆被一封遗嘱与一封信改写（通说待核）。","'不可靠的记忆'：自我辩护的崩塌（通说待核）。"],
  "characters":[{"name":"托尼","identity":"退休律师","note":"不可靠叙述者（B290）"},{"name":"维罗妮卡","identity":"前女友","note":"（通说待核）"}],
  "themes":["记忆的不可靠（B290）。",
   "衰老与清算（B290：memory and aging）。",
   "'终结的感觉'：历史的追索（书名通说待核）。"],
  "influence":[{"text":"Britannica：2011年布克奖——不可靠叙述者探察记忆与衰老（B290）。","source":"B290"},
   {"text":"Britannica：2017年电影改编（B290 语境）。","source":"B290"}],
  "reading":{"difficulties":["上下两部（第一/第二部分）结构。","不可靠叙述的细节。"],
   "editions":["《终结的感觉》（译林出版社，通说待核）。","英文原版。"],
   "order":"先《福楼拜的鹦鹉》后本作。"},
  "pending":["2011年出版（Jonathan Cape说）核对。","托尼/维罗妮卡人名核对。","2017年电影（Ritesh Batra说）待核。"],
  "sources":["B290"],"year_source":"B290","author_source":"B290","related_works":["fuloubaideyingwu","banshengyuan","changri"],
  "svg":G2("《终结的感觉》记忆结构图",[{"title":"遗嘱","text":"改写的开始","color":"antagonist"},{"title":"记忆","text":"不可靠的自辩（B290）","color":"main"},{"title":"维罗妮卡","text":"真相的持有者","color":"gold"},{"title":"衰老","text":"清算的晚年","color":"family"}])
},
"huixue": {
  "id":"huixue","title":"慧血","original_title":"Wise Blood","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"oconnor","author_name":"弗兰纳里·奥康纳",
  "year_display":"1952年（作者页 B291 口径：Wise Blood (1952)）","year_sort":1952,
  "background":["作者页（B291）：奥康纳 major_works 载'Wise Blood (1952)'（B291 作者页定位，详见 haorennanxun 条核对）。","题材（通说待核）：退伍兵黑兹尔·莫茨的'无教会'布道——拒绝基督却离不开基督。"],
  "outline":["黑兹尔创立'无基督之教'——荒诞布道与最后的自毁（通说待核）。"],
  "characters":[{"name":"黑兹尔·莫茨","identity":"退伍兵","note":"（通说待核）"},{"name":"伊诺克","identity":"青年","note":"（通说待核）"}],
  "themes":["'无教会'的悖论：拒绝即证明（通说待核）。",
   "南方哥特（B291：master of the Southern gothic——作者级）。",
   "瞎眼与忏悔（通说待核）。"],
  "influence":[{"text":"作者页：奥康纳首部长篇（B291 作者页口径）。","source":"B291"},
   {"text":"作者页：南方哥特大师（B291 作者级定位）。","source":"B291"}],
  "reading":{"difficulties":["'无教会'的宗教戏仿。","哥特细节。"],
   "editions":["《慧血》（新星出版社《慧血：奥康纳作品集》，通说待核）。","英文原版。"],
   "order":"先《好人难寻》后本作。"},
  "pending":["1952年出版（Harcourt, Brace说）核对。","黑兹尔·莫茨人名核对。","1969年电影改编待核。"],
  "sources":["B291"],"year_source":"B291","author_source":"B291","related_works":["haorennanxun","juwairen","bianxingji"],
  "svg":G2("《慧血》悖论结构图",[{"title":"无教会","text":"拒绝的布道","color":"main"},{"title":"黑兹尔","text":"瞎眼的忏悔（通说）","color":"antagonist"},{"title":"慧血","text":"书名的反讽","color":"gold"},{"title":"南方","text":"哥特的荒原","color":"family"}])
},
"atuopaozhe": {
  "id":"atuopaozhe","title":"啊，拓荒者！","original_title":"O Pioneers!","region":"美国","era":"近代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"cather","author_name":"薇拉·凯瑟",
  "year_display":"1913年（作者页 B292 口径：O Pioneers! (1913)）","year_sort":1913,
  "background":["作者页（B292）：凯瑟 major_works 载'O Pioneers! (1913)'（B292 作者页定位，详见 wodeandongnia 条核对）。","Britannica（B292）：'With O Pioneers! (1913) and My Ántonia (1918)'——边疆精神与勇气的主题（通说待核）。"],
  "outline":["亚历山德拉继承内布拉斯加农场——坚守土地而致富（通说待核）。"," EMIL？——不：艾米与玛丽亚的悲剧线（通说待核）。"],
  "characters":[{"name":"亚历山德拉","identity":"农场主","note":"（通说待核）"},{"name":"艾米","identity":"恋人","note":"（通说待核）"}],
  "themes":["拓荒者的坚守与土地（B292 语境：frontier spirit and courage）。",
   "'精神与道德价值高于物质主义'（B292 作者级）。",
   "地域主义（B292：unique regionalism——作者级）。"],
  "influence":[{"text":"Britannica：'With O Pioneers! (1913) and My Ántonia (1918)'——边疆主题的代表（B292）。","source":"B292"},
   {"text":"Britannica：1922年《我们中的一个》获普利策奖（B292 作者级）。","source":"B292"}],
  "reading":{"difficulties":["移民垦荒史。","北欧裔移民名。"],
   "editions":["《啊，拓荒者！》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"凯瑟平原小说之首。"},
  "pending":["1913年出版（Houghton Mifflin说）核对。","亚历山德拉/艾米人名核对。","书名出自惠特曼诗（通说待核）。"],
  "sources":["B292"],"year_source":"B292","author_source":"B292","related_works":["wodeandongnia","fenwangyu","huozhe"],
  "svg":G2("《拓荒者》坚守结构图",[{"title":"亚历山德拉","text":"守土的女主","color":"main"},{"title":"垦荒","text":"草原的麦田","color":"gold"},{"title":"悲剧","text":"艾米与玛丽亚","color":"antagonist"},{"title":"拓荒者","text":"书名出自惠特曼（待核）","color":"family"}])
},
"moerflandes": {
  "id":"moerflandes","title":"摩尔·弗兰德斯","original_title":"Moll Flanders","region":"英国","era":"近代","era_detail":"18世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"defoe","author_name":"丹尼尔·笛福",
  "year_display":"1722年（Britannica：Moll Flanders (1722)——B293）","year_sort":1722,
  "background":["Britannica（B293）：'Daniel Defoe is best known as the writer of the novels Robinson Crusoe (1719) and Moll Flanders (1722).'（B293）。","题材（通说待核）：新门监狱出生的摩尔——12年妓女、12年窃贼、8年弗吉尼亚流放的'悔罪'自述。"],
  "outline":["摩尔的自述：从出生（新门监狱）到弗吉尼亚的种植园（通说待核）。","'悔罪'与利益的悖论（通说待核）。"],
  "characters":[{"name":"摩尔·弗兰德斯","identity":"叙述者","note":"（通说待核）"}],
  "themes":["女性生存的'经济'书写（通说待核）。",
   "'悔罪体'与利益的悖论（通说待核）。",
   "18世纪伦敦底层（通说）。"],
  "influence":[{"text":"Britannica：笛福 best known 作品之一（B293）。","source":"B293"},
   {"text":"作者页：笛福'英国小说之父'关联问答（B293——待核）。","source":"B293"}],
  "reading":{"difficulties":["18世纪货币与刑律。","伪自传的语气。"],
   "editions":["《摩尔·弗兰德斯》（人民文学出版社，通说待核）。","英文原版（公有领域）。"],
   "order":"笛福双璧之二。"},
  "pending":["1722年出版细节核对。","摩尔12年妓女/12年窃贼/8年殖民地说核对。","'悔罪'结构待核。"],
  "sources":["B293"],"year_source":"B293","author_source":"B293","related_works":["lubinxun","tangmuqiongsi","jialimeimei"],
  "svg":G2("《摩尔·弗兰德斯》自述结构图",[{"title":"新门监狱","text":"出生之地","color":"antagonist"},{"title":"摩尔","text":"女性的生存","color":"main"},{"title":"弗吉尼亚","text":"流放与'新生'","color":"family"},{"title":"悔罪","text":"利益的悖论（通说）","color":"gold"}])
},
"huashenboshi": {
  "id":"huashenboshi","title":"化身博士","original_title":"The Strange Case of Dr Jekyll and Mr Hyde","region":"英国","era":"近代","era_detail":"19世纪",
  "genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"stevenson","author_name":"罗伯特·路易斯·史蒂文森",
  "year_display":"1886年（通说待核；Britannica B294 Quick Facts 载 Kidnapped (1886)——本篇正文未载）","year_sort":1886,
  "background":["作者页（B294）：史蒂文森'a writer of originality and power who produced brilliant adventure stories with subtle moral overtones'（B294 作者页定位）。","题材（通说待核）：杰基尔博士的药剂与海德先生的恶——人格分裂的哥特寓言。"],
  "outline":["律师厄特森追查：杰基尔与海德的药剂秘密（通说待核）。","'人并非其一，而是二者'（通说待核——杰基尔自白）。"],
  "characters":[{"name":"杰基尔/海德","identity":"博士与恶人","note":"一人两面（通说待核）"},{"name":"厄特森","identity":"律师","note":"追查者（通说待核）"}],
  "themes":["人格的双重性（通说）。",
   "'化身'：科学的越界（通说待核）。",
   "维多利亚的伪善（通说待核）。"],
  "influence":[{"text":"作者页：史蒂文森'原创与力量'（B294 作者页口径）。","source":"B294"},
   {"text":"'Jekyll and Hyde'进入英语（通说待核）。","source":"B294"}],
  "reading":{"difficulties":["多重叙述（厄特森/拉尼翁/自白）。","维多利亚哥特语境。"],
   "editions":["《化身博士》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"史蒂文森代表作之一。"},
  "pending":["1886年出版（Longmans, Green说）核对。","杰基尔/海德/厄特森人名核对。","'Jekyll and Hyde'英语习语待核。"],
  "sources":["B294"],"year_source":"B294","author_source":"B294","related_works":["daolian","weite","bianxingji"],
  "svg":G2("《化身博士》双重人格图",[{"title":"杰基尔","text":"体面的博士","color":"family"},{"title":"海德","text":"释放的恶","color":"antagonist"},{"title":"药剂","text":"科学的越界","color":"gold"},{"title":"双重","text":"'人并非其一'（通说）","color":"main"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
