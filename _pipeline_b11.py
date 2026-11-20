# -*- coding: utf-8 -*-
"""流水线批次11：Britannica 新核 6 作家 7 部 + 零成本直写 3 部"""
import json, pathlib

new_src = [
{"id":"B295","title":"Francois Rabelais — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Francois-Rabelais","type":"百科全书","verified":True,"covers":["rabelais","jurenzhuan"],"note":"2026-11-20 核对：c.1483–94 Seuilly 生—probably 1553-04-09 巴黎卒；Pantagruel (1532) 以化名 Alcofribas Nasier（名字易位构词）出版——被索邦谴责为淫秽但'became a popular success'；Gargantua 首版 probably 1534；'The five novels that make up Gargantua and Pantagruel'——'published between 1532 and 1564'（第五卷作者归属有争议）；'His creative exuberance, colorful and wide-ranging vocabulary, and literary variety have gained him a lasting place in the history of 16th-century French literature'；'Rabelais used scatology aesthetically, not gratuitously'；讽刺对象：'social institutions, dogmas, educational traditions, and philosophical methodologies'"},
{"id":"B296","title":"Michel de Montaigne — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Michel-de-Montaigne","type":"百科全书","verified":True,"covers":["montaigne","mengtiansuibi"],"note":"2026-11-20 核对：1533-02-28蒙田城堡生—1592-09-23卒（59岁）；'a French writer whose Essais (Essays) established a new literary form'；第一二卷57+37章 1580年波尔多出版；1588年版首收第三卷13章；怀疑论：'a skepticism towards humanity's claims to knowledge, advocating for self-acceptance and tolerance'；essais 一词意为'the probings and testings of his mind'；名句'I am myself the matter of my book'（致读者开篇）；宗教战争（1562–98）背景；1581—85年任波尔多市长两任"},
{"id":"B297","title":"Henry James (American writer) — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Henry-James-American-writer","type":"百科全书","verified":True,"covers":["henryjames","yiweinvshidehuaxiang"],"note":"2026-11-20 核对：1843-04-15纽约生—1916-02-28伦敦卒（72岁）；1915年入英国籍；20部长篇、112个短篇、12部剧；'James ended this first phase of his career by producing his masterpiece, The Portrait of a Lady (1881)'——'a picture of Americans moving in the expatriate society of England and of Italy, this novel has no equal'；'Today he is best remembered as the author of the novel The Portrait of a Lady (1881) and the novella The Turn of the Screw (1898)'；'a key transitional figure between literary realism and Modernism'"},
{"id":"B298","title":"Saul Bellow — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Saul-Bellow","type":"百科全书","verified":True,"covers":["bellow","aojimaqi"],"note":"2026-11-20 核对：1915-06-10魁北克拉欣生（犹太裔）—2005-04-05布鲁克莱恩卒（89岁）；1976诺奖授奖词 'for the human understanding and subtle analysis of contemporary culture that are combined in his work'；The Adventures of Augie March (1953)——'A picaresque story of a poor Jewish boy from Chicago'、获1954年国家图书奖；普利策奖1976；'It is this combination of cultural sophistication and the wisdom of the streets that constitutes Bellow's greatest originality'；1976年亦获普利策奖（贺姆博尔德的礼物）"},
{"id":"B299","title":"Robert Burns — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Robert-Burns","type":"百科全书","verified":True,"covers":["burns","pengsishixuan"],"note":"2026-11-20 核对：1759-01-25苏格兰艾尔郡阿洛韦生—1796-07-21邓弗里斯卒（37岁）；'Robert Burns is considered the national poet of Scotland'；1786-07-31基尔马诺克版 Poems, Chiefly in the Scottish Dialect——含 To a Mouse、The Holy Fair 等'a handful of first-rate Scots poems'；'Tam o Shanter'（1791，mock-heroic）；'contribution to over three hundred songs'（Auld Lang Syne 等）；'Ploughman Poet'；为辑录改写300余首苏格兰民歌拒绝报酬"},
{"id":"B300","title":"Dylan Thomas — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Dylan-Thomas","type":"百科全书","verified":True,"covers":["dylanthomas","nailinxia"],"note":"2026-11-20 核对：1914-10-27威尔士斯旺西生—1953-11-09纽约卒（39岁）；'celebrated for comic exuberance and lyrical intensity'；Under Milk Wood——'evokes the lives of the inhabitants of a small Welsh town, shows Thomas's full powers as an artist in comedy'、1953年纽约诗歌中心演出、1954年BBC播出最终版；'His work, in its overtly emotional impact, its insistence on the importance of sound and rhythm……owed more to his Welsh background'；'verbal harmonies that are unique in English poetry'；18 Poems、Deaths and Entrances 为主要诗集"},
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
"rabelais": {
  "id": "rabelais", "name": "弗朗索瓦·拉伯雷", "foreign_name": "François Rabelais（弗朗索瓦·拉伯雷，约1483/94—1553）",
  "country": "法国", "birth": 1490, "death": 1553, "birth_year": 1490, "death_year": 1553, "era": "近代",
  "summary": "拉伯雷，希伊附近的法国文艺复兴医生与人文主义者——五卷滑稽杰作《巨人传》的作者（化名 Alcofribas Nasier，其名易位构词）（Britannica）。'His creative exuberance, colorful and wide-ranging vocabulary, and literary variety have gained him a lasting place in the history of 16th-century French literature'（B295）。'Rabelais used scatology aesthetically, not gratuitously'（将粪便学审美化而非随意——B295）；讽刺'social institutions, dogmas, educational traditions, and philosophical methodologies'（B295）。",
  "timeline": [
    {"year": 1490, "text": "约生于希伊附近（Britannica：Born c. 1483–94, Seuilly, near Chinon）。", "src": "B295"},
    {"year": 1532, "text": "《庞固埃》以化名出版——被索邦谴责为淫秽但成为畅销（B295：condemned by the Sorbonne……became a popular success）。", "src": "B295"},
    {"year": 1534, "text": "《高康大》首版约于是年（B295：probably published in 1534）。", "src": "B295"},
    {"year": 1552, "text": "《第四卷》全本出版（B295：full Quart livre published 1552）。", "src": "B295"},
    {"year": 1553, "text": "约1553年4月9日卒于巴黎（B295：probably April 9, 1553, Paris）。", "src": "B295"}],
  "major_works": [
    {"work_id": "jurenzhuan", "note": "五卷小说（B295：1532—1564）"},
    {"title": "第三卷", "note": "（B295：Tiers livre 1546，遭禁后逃梅斯）"},
    {"title": "第四卷、第五卷", "note": "（B295：Quart livre 1548/1552；第五卷1564，作者归属有争议）"}],
  "style": [
    "'creative exuberance, colorful and wide-ranging vocabulary'（B295）。",
    "'scatology aesthetically, not gratuitously'（B295——审美化的粗俗）。",
    "讽刺社会制度、教条、教育传统与哲学方法论（B295）。"],
  "status": "Britannica 定位拉伯雷为16世纪法国文学史上占永恒一席的文艺复兴医生与人文主义者（B295）。",
  "sources": ["B295"], "dates_source": "B295",
  "pending": ["生年（约1483—1494多说）与卒日核对。", "五卷卷名与出版年表核对。", "第五卷归属争议细节待核。"]
},
"montaigne": {
  "id": "montaigne", "name": "蒙田", "foreign_name": "Michel de Montaigne（米歇尔·德·蒙田，1533-02-28—1592-09-23）",
  "country": "法国", "birth": 1533, "death": 1592, "birth_year": 1533, "death_year": 1592, "era": "近代",
  "summary": "蒙田，蒙田城堡生，法国作家与哲学家——'whose Essais (Essays) established a new literary form'（其《随笔集》确立了新的文学形式——Britannica）。写作于法国宗教战争（1562—98）期间——'a skepticism towards humanity's claims to knowledge, advocating for self-acceptance and tolerance'（对人类知识主张的怀疑，倡导自我接纳与宽容——B296）。essais 一词意为'the probings and testings of his mind'（心灵的试探——B296）。名句（致读者开篇）：'I am myself the matter of my book'（我自己就是本书的题材——B296）。",
  "timeline": [
    {"year": 1533, "text": "2月28日生于蒙田城堡（B296：Born February 28, 1533, Château de Montaigne）。", "src": "B296"},
    {"year": 1580, "text": "第一二卷（57+37章）在波尔多出版（B296：published in Bordeaux in 1580）。", "src": "B296"},
    {"year": 1581, "text": "任波尔多市长（两任，至1585年7月——B296）。", "src": "B296"},
    {"year": 1588, "text": "第五版首收第三卷13章（B296：the first to contain the 13 chapters of Book III）。", "src": "B296"},
    {"year": 1592, "text": "9月23日卒于蒙田城堡（B296）。", "src": "B296"}],
  "major_works": [
    {"work_id": "mengtiansuibi", "note": "随笔集（B296：1580，确立新文学形式）"},
    {"title": "旅行日记", "note": "（B296：Journal de voyage published 1774）"},
    {"title": "塞朋德的认识？——不：塞朋德翻译（Sebond translation，1569）", "note": "（B296：first book 1569）"}],
  "style": [
    "'确立了新的文学形式'（B296：established a new literary form）。",
    "自我审视的怀疑论：'self-acceptance and tolerance'（B296）。",
    "随笔=心灵的试探（B296：probings and testings of his mind）。"],
  "status": "Britannica 定位蒙田为随笔形式的发明者、法国文艺复兴怀疑论的代言人（B296）。",
  "sources": ["B296"], "dates_source": "B296",
  "pending": ["《随笔集》三卷107篇说核对。", "'Que sais-je'（我知道什么）出处待核。", "名句'I am myself the matter of my book'原文核对。"]
},
"henryjames": {
  "id": "henryjames", "name": "亨利·詹姆斯", "foreign_name": "Henry James（亨利·詹姆斯，1843-04-15—1916-02-28）",
  "country": "美国", "birth": 1843, "death": 1916, "birth_year": 1843, "death_year": 1916, "era": "现当代",
  "summary": "亨利·詹姆斯，纽约人，美国小说家与批评家——1915年入英国籍（Britannica）；20部长篇、112个短篇、12部剧作（B297）；'a key transitional figure between literary realism and Modernism'（现实主义与现代主义之间的关键过渡人物——B297）。'James ended this first phase of his career by producing his masterpiece, The Portrait of a Lady (1881)'（B297）；'As a picture of Americans moving in the expatriate society of England and of Italy, this novel has no equal'（B297）。'Today he is best remembered as the author of the novel The Portrait of a Lady (1881) and the novella The Turn of the Screw (1898)'（B297）。",
  "timeline": [
    {"year": 1843, "text": "4月15日生于纽约（B297：Born April 15, 1843, New York City）。", "src": "B297"},
    {"year": 1881, "text": "《一位女士的画像》出版（B297：masterpiece，1881）。", "src": "B297"},
    {"year": 1898, "text": "《螺丝在拧紧》出版（B297：The Turn of the Screw (1898)）。", "src": "B297"},
    {"year": 1915, "text": "入英国籍（B297：Became a British subject 1915）。", "src": "B297"},
    {"year": 1916, "text": "2月28日卒于伦敦（B297：Died February 28, 1916, London）。", "src": "B297"}],
  "major_works": [
    {"work_id": "yiweinvshidehuaxiang", "note": "长篇（B297：masterpiece，1881）"},
    {"title": "螺丝在拧紧", "note": "（B297：The Turn of the Screw (1898)）"},
    {"title": "鸽翼、使节", "note": "（通说待核）"}],
  "style": [
    "'现实主义与现代主义之间的关键过渡人物'（B297）。",
    "'欧美侨民社会'的画像（B297：expatriate society of England and of Italy）。",
    "20部长篇+112短篇的多产（B297）。"],
  "status": "Britannica 定位亨利·詹姆斯为现实主义—现代主义之间的关键过渡人物（B297）；'transatlantic culture'的伟大人物（B297 语境）。",
  "sources": ["B297"], "dates_source": "B297",
  "pending": ["《一位女士的画像》1881年出版（Macmillan说）核对。","伊莎贝尔·阿切尔人名核对。","《使节》1903年说待核。"]
},
"bellow": {
  "id": "bellow", "name": "索尔·贝娄", "foreign_name": "Saul Bellow（索尔·贝娄，1915-06-10—2005-04-05）",
  "country": "美国", "birth": 1915, "death": 2005, "birth_year": 1915, "death_year": 2005, "era": "现当代",
  "summary": "贝娄，生于魁北克拉欣的犹太裔美国小说家（Britannica）——以描绘现代都市人'disaffected by society but not destroyed in spirit'（被社会疏离而精神未灭——B298）著称。'The Adventures of Augie March (1953)……won a National Book Award in 1954'（B298）；1976年获诺贝尔文学奖——授奖词 'for the human understanding and subtle analysis of contemporary culture that are combined in his work'（B298）；1976年亦获普利策奖（B298）。'It is this combination of cultural sophistication and the wisdom of the streets that constitutes Bellow's greatest originality'（文化精致与街头智慧的组合构成其最大原创性——B298）。",
  "timeline": [
    {"year": 1915, "text": "6月10日生于魁北克拉欣（B298：Born June 10, 1915, Lachine, near Montreal, Quebec, Canada）。", "src": "B298"},
    {"year": 1953, "text": "《奥吉·玛琪历险记》出版（B298：1953）。", "src": "B298"},
    {"year": 1954, "text": "获国家图书奖（B298）。", "src": "B298"},
    {"year": 1976, "text": "获诺贝尔文学奖与普利策奖（B298：Nobel Prize 1976；Pulitzer 1976）。", "src": "B298"},
    {"year": 2005, "text": "4月5日卒于马萨诸塞州布鲁克莱恩（B298）。", "src": "B298"}],
  "major_works": [
    {"work_id": "aojimaqi", "note": "长篇（B298：1953，国家图书奖）"},
    {"title": "赫尔索格、洪堡的礼物", "note": "（B298：Herzog, Humboldt's Gift）"},
    {"title": "雨王亨德森", "note": "（通说待核）"}],
  "style": [
    "'human understanding and subtle analysis of contemporary culture'（B298 授奖词）。",
    "'cultural sophistication and the wisdom of the streets'（B298）。",
    "流浪汉小说的现代转型（B298：picaresque story）。"],
  "status": "Britannica 定位贝娄为犹太裔美国小说家代表、1976年诺奖与普利策奖双料得主（B298）。",
  "sources": ["B298"], "dates_source": "B298",
  "pending": ["《奥吉·玛琪历险记》中译本信息核对。","赫尔索格人名核对。","'二次世界大战后美国文学中心'说待核。"]
},
"burns": {
  "id": "burns", "name": "罗伯特·彭斯", "foreign_name": "Robert Burns（罗伯特·彭斯，1759-01-25—1796-07-21）",
  "country": "英国", "birth": 1759, "death": 1796, "birth_year": 1759, "death_year": 1796, "era": "近代",
  "summary": "彭斯，苏格兰艾尔郡阿洛韦人，'considered the national poet of Scotland'（苏格兰国民诗人——B299）；农民之子，人称'Ploughman Poet'（犁夫诗人——B299），以苏格兰语与英语双语写歌词与歌曲；辑录改写数百首传统苏格兰歌曲且拒绝报酬（B299）。1786年7月31日基尔马诺克版 Poems, Chiefly in the Scottish Dialect（B299）——含 To a Mouse、The Holy Fair 等'a handful of first-rate Scots poems'（B299）；'Tam o' Shanter'（1791，mock-heroic——B299）；'contribution to over three hundred songs'（含 Auld Lang Syne——B299）。",
  "timeline": [
    {"year": 1759, "text": "1月25日生于阿洛韦（B299：Born January 25, 1759, Alloway, Ayrshire, Scotland）。", "src": "B299"},
    {"year": 1786, "text": "7月31日基尔马诺克版诗集出版（B299）。", "src": "B299"},
    {"year": 1791, "text": "《汤姆·奥·桑特》出版（B299：mock-heroic）。", "src": "B299"},
    {"year": 1796, "text": "7月21日卒于邓弗里斯（37岁）（B299）。", "src": "B299"}],
  "major_works": [
    {"work_id": "pengsishixuan", "note": "诗选（本库立目）"},
    {"title": "汤姆·奥·桑特", "note": "（B299：1791，mock-heroic）"},
    {"title": "致老鼠、一朵红红的玫瑰", "note": "（B299 载 To a Mouse；红玫瑰通说待核）"}],
  "style": [
    "苏格兰方言与英语双语写作（B299：Poems, Chiefly in the Scottish Dialect）。",
    "'300余首歌曲'的辑录改写、拒酬（B299）。",
    "讽刺与抒情的'犁夫诗人'（B299：Ploughman Poet）。"],
  "status": "Britannica 定位彭斯为苏格兰国民诗人（B299）；Auld Lang Syne 歌词作者（B299 语境）；'彭斯之夜'全球庆祝（通说待核）。",
  "sources": ["B299"], "dates_source": "B299",
  "pending": ["《一朵红红的玫瑰》1794年出处待核。","彭斯之夜（Burns Night，1月25日）待核。","《致虱子》等篇目待核。"]
},
"dylanthomas": {
  "id": "dylanthomas", "name": "狄兰·托马斯", "foreign_name": "Dylan Thomas（狄兰·托马斯，1914-10-27—1953-11-09）",
  "country": "英国", "birth": 1914, "death": 1953, "birth_year": 1914, "death_year": 1953, "era": "现当代",
  "summary": "狄兰·托马斯，威尔士斯旺西人，威尔士诗人与散文作家——'celebrated for comic exuberance and lyrical intensity'（以滑稽的奔放与抒情的强度著称——B300）。Under Milk Wood——'evokes the lives of the inhabitants of a small Welsh town, shows Thomas's full powers as an artist in comedy'（B300）；1953年纽约诗歌中心演出、1954年BBC播出最终版（B300）。文体：'owed more to his Welsh background than to the prevailing taste in English literature'（多于英国文学流行趣味——威尔士背景——B300）；'verbal harmonies that are unique in English poetry'（英语诗歌中独一无二的语音和谐——B300）。",
  "timeline": [
    {"year": 1914, "text": "10月27日生于威尔士斯旺西（B300：Born October 27, 1914, Swansea, Wales）。", "src": "B300"},
    {"year": 1953, "text": "Under Milk Wood 纽约诗歌中心演出；11月9日卒于纽约（39岁）（B300）。", "src": "B300"},
    {"year": 1954, "text": "最终版由BBC播出（B300）。", "src": "B300"}],
  "major_works": [
    {"work_id": "nailinxia", "note": "广播剧（B300：1953/1954）"},
    {"title": "18首诗、死亡与入场", "note": "（B300：18 Poems, Deaths and Entrances）"},
    {"title": "不要温和地走进那个良夜", "note": "（通说待核——B300 页未载）"}],
  "style": [
    "'滑稽的奔放与抒情的强度'（B300：comic exuberance and lyrical intensity）。",
    "'威尔士背景'之于英语文学（B300）。",
    "'英语诗歌中独一无二的语音和谐'（B300）。"],
  "status": "Britannica 定位狄兰·托马斯为威尔士诗人与散文作家（39岁早逝于纽约巡演——B300）。",
  "sources": ["B300"], "dates_source": "B300",
  "pending": ["'Do not go gentle'名句出处与全文核对。","Under Milk Wood 中译名（《奶树林下》/《 Under Milk Wood》）待核。","18 Poems（1934）年份核对。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G3(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"jinyindao": {
  "id":"jinyindao","title":"金银岛","original_title":"Treasure Island","region":"英国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"stevenson","author_name":"罗伯特·路易斯·史蒂文森",
  "year_display":"出版年份待核（Britannica B294 Quick Facts 作'Treasure Island (1881)'——通行1883年说待核）","year_sort":1883,
  "background":["作者页（B294）：史蒂文森 major_works 载'金银岛、绑架'（B294 作者页定位，详见 huashenboshi 条核对）。","作者（B294）：'a writer of originality and power who produced brilliant adventure stories with subtle moral overtones'。"],
  "outline":["少年吉姆获得藏宝图——'独脚厨'西尔弗的海上阴谋（通说待核）。","'独脚水手'歌谣的起源（通说待核）。"],
  "characters":[{"name":"吉姆·霍金斯","identity":"少年","note":"（通说待核）"},{"name":"朗·约翰·西尔弗","identity":"独脚厨","note":"（通说待核）"}],
  "themes":["海盗文学的原型（通说待核）。",
   "'独脚、鹦鹉、藏宝图'的母题发明（通说待核）。",
   "善恶的道德意味（B294：subtle moral overtones）。"],
  "influence":[{"text":"Britannica：'best known for his novels Treasure Island……'（B294）。","source":"B294"},
   {"text":"作者页：史蒂文森冒险经典至今广读（B294 语境）。","source":"B294"}],
  "reading":{"difficulties":["航海术语。","海盗黑话。"],
   "editions":["《金银岛》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"史蒂文森冒险首选。"},
  "pending":["1883年出版（Cassell说）与 Britannica Quick Facts 1881 差异核对。","吉姆·霍金斯/西尔弗人名核对。","'死人的箱子'章等细节待核。"],
  "sources":["B294"],"year_source":"B294","author_source":"B294","related_works":["huashenboshi","hakebei","tangmusuoyaxianji"],
  "svg":G2("《金银岛》藏宝结构图",[{"title":"藏宝图","text":"少年的发现","color":"family"},{"title":"西尔弗","text":"独脚的厨师","color":"antagonist"},{"title":"海上","text":" Hispaniola 号（通说）","color":"main"},{"title":"宝藏","text":"道德的试炼","color":"gold"}])
},
"conglinzhihue": {
  "id":"conglinzhihue","title":"丛林之书","original_title":"The Jungle Book","region":"英国","era":"近代","era_detail":"19世纪末",
  "genre":"故事集","genre_group":"故事集","language":"英语","author_id":"kipling","author_name":"鲁德亚德·吉卜林",
  "year_display":"1894年（作者页 B277 口径：The Jungle Book (1894)——'stylistically superb collections of stories'）","year_sort":1894,
  "background":["作者页（B277）：吉卜林 major_works 载'The Jungle Book (1894) and The Second Jungle Book (1895)'——'stylistically superb collections of stories'（B277 作者页定位）。","题材（通说待核）：狼群养大的毛克利——熊巴鲁、黑豹巴希拉与老虎谢利·可汗。"],
  "outline":["毛克利在丛林的成长与'法律'——与老虎谢利·可汗的对决（通说待核）。"],
  "characters":[{"name":"毛克利","identity":"狼孩","note":"（通说待核）"},{"name":"巴鲁","identity":"熊","note":"法律的老师（通说待核）"}],
  "themes":["丛林'法律'：文明与野性的边界（通说待核）。",
   "成长与身份（通说）。",
   "帝国视角下的印度丛林（通说待核）。"],
  "influence":[{"text":"Britannica：'stylistically superb collections of stories'（B277）。","source":"B277"},
   {"text":"作者页：吉卜林儿童故事代表作（B277 作者级定位）。","source":"B277"}],
  "reading":{"difficulties":["印度丛林词汇。","'法律'条文（丛林法则）的阅读。"],
   "editions":["《丛林之书》（人民文学出版社/浙江文艺出版社版本，通说待核）。","英文原版（公有领域）。"],
   "order":"吉卜林儿童文学首选。"},
  "pending":["1894年出版（Macmillan说）核对。","毛克利/巴鲁/谢利·可汗人名核对。","迪士尼改编（1967/2016）待核。"],
  "sources":["B277"],"year_source":"B277","author_source":"B277","related_works":["jim","yisuo","hakebei"],
  "svg":G2("《丛林之书》法律结构图",[{"title":"毛克利","text":"狼群的孩子","color":"main"},{"title":"巴鲁","text":"丛林法律的老师","color":"gold"},{"title":"谢利·可汗","text":"老虎的威胁","color":"antagonist"},{"title":"法律","text":"丛林与文明","color":"family"}])
},
"yuesefuandelusi": {
  "id":"yuesefuandelusi","title":"约瑟夫·安德鲁斯","original_title":"Joseph Andrews","region":"英国","era":"近代","era_detail":"18世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"fielding","author_name":"亨利·菲尔丁",
  "year_display":"1742年（Britannica：Fielding's Joseph Andrews was published anonymously in 1742）","year_sort":1742,
  "background":["Britannica（B274）：'Fielding's Joseph Andrews was published anonymously in 1742'；'He was certainly inaugurating a new genre in fiction'；前言自述'a comic Epic-Poem in Prose'（B274）。","缘起（B274 语境）：戏仿理查森《帕梅拉》——帕梅拉之弟约瑟夫的贞洁冒险（通说待核）。"],
  "outline":["约瑟夫与帕森·亚当斯的公路冒险：正直者的滑稽考验（通说待核）。"],
  "characters":[{"name":"约瑟夫","identity":"男仆","note":"（通说待核）"},{"name":"帕森·亚当斯","identity":"牧师","note":"唐吉诃德式牧师（通说待核）"}],
  "themes":["'滑稽史诗'的实践（B274：comic Epic-Poem in Prose）。",
   "对感伤主义的戏仿（B274 语境：Shamela 的姊妹）。",
   "正直的公路喜剧（通说待核）。"],
  "influence":[{"text":"Britannica：'He was certainly inaugurating a new genre in fiction'（B274）。","source":"B274"},
   {"text":"作者页：菲尔丁'英国小说之父'（B274 作者级定位）。","source":"B274"}],
  "reading":{"difficulties":["与《帕梅拉》的互文。","18世纪公路叙事。"],
   "editions":["《约瑟夫·安德鲁斯》（人民文学出版社，通说待核）。","英文原版（公有领域）。"],
   "order":"先《汤姆·琼斯》或本作（互为前奏）。"},
  "pending":["1742年2月出版（Andrew Millar说）核对。","约瑟夫/亚当斯人名核对。","《莎米拉》戏仿（1741——B274 已载）展开核对。"],
  "sources":["B274"],"year_source":"B274","author_source":"B274","related_works":["tangmuqiongsi","lubinxun","moerflandes"],
  "svg":G2("《约瑟夫·安德鲁斯》公路喜剧图",[{"title":"贞洁","text":"男性的'帕梅拉'","color":"main"},{"title":"亚当斯","text":"堂吉诃德式牧师","color":"gold"},{"title":"公路","text":"滑稽的冒险","color":"family"},{"title":"戏仿","text":"对感伤主义的反讽","color":"antagonist"}])
},
"jurenzhuan": {
  "id":"jurenzhuan","title":"巨人传","original_title":"La vie très horifique du grand Gargantua……Pantagruel（五卷）","region":"法国","era":"近代","era_detail":"文艺复兴",
  "genre":"长篇小说（五卷）","genre_group":"小说","language":"法语","author_id":"rabelais","author_name":"弗朗索瓦·拉伯雷（化名 Alcofribas Nasier）",
  "year_display":"1532—1564年出版（Britannica：The five novels……published between 1532 and 1564——B295）","year_sort":1532,
  "background":["Britannica（B295）：'The five novels that make up Gargantua and Pantagruel——although authorship of the fifth is disputed'（五卷、第五卷归属有争议）；Pantagruel (1532) 'condemned by the Sorbonne in Paris as obscene. It became a popular success'；'Rabelais used scatology aesthetically, not gratuitously'（B295）。","讽刺对象（B295）：'social institutions, dogmas, educational traditions, and philosophical methodologies'。"],
  "outline":["巨人父子：高康大与庞大固埃——'神瓶'的谒见与'rinkyhorn'（通说待核）。","巴汝奇：'cunning and witty rogue'（B295：first appears in the first novel——通说待核）。","'特来美修道院'：'做你想做的'（通说待核）。"],
  "characters":[{"name":"高康大","identity":"巨人","note":"庞固埃之父（B295）"},{"name":"庞大固埃","identity":"巨人","note":"（B295）"},{"name":"巴汝奇","identity":" companions","note":"'cunning and witty rogue'（B295）"}],
  "themes":["'审美化的粗俗'（B295：scatology aesthetically）。",
   "对制度、教条、教育传统的讽刺（B295）。",
   "人文主义的'直觉与好奇心'（B295：nobility and boundless curiosity——语境）。"],
  "influence":[{"text":"Britannica：'a lasting place in the history of 16th-century French literature'（B295）。","source":"B295"},
   {"text":"Britannica：'Rabelaisian'一词的误导——粗俗是审美的（B295）。","source":"B295"}],
  "reading":{"difficulties":["五卷顺序（庞固埃在前！）。","16世纪法语双关。"],
   "editions":["《巨人传》（人民文学出版社/上海译文出版社版本，通说待核）。","法文原版（公有领域）。"],
   "order":"先读《庞固埃》（先出版）或《高康大》（先叙事）。"},
  "pending":["五卷出版年表（1532/1534/1546/1552/1564）核对。","'特来美'修道院与'做你想做的'原文待核。","第五卷归属争议待核。"],
  "sources":["B295"],"year_source":"B295","author_source":"B295","related_works":["geliefo","tangjihede","don Quixote"] ,
  "svg":G2("《巨人传》五卷结构图",[{"title":"庞固埃","text":"1532首卷（B295）","color":"main"},{"title":"高康大","text":"巨人之父","color":"family"},{"title":"巴汝奇","text":"狡黠的浪子（B295）","color":"gold"},{"title":"神瓶","text":"'喝'的谒见（通说）","color":"plain"}])
},
"mengtiansuibi": {
  "id":"mengtiansuibi","title":"蒙田随笔集","original_title":"Essais（Essays）","region":"法国","era":"近代","era_detail":"文艺复兴",
  "genre":"随笔集（三卷107篇）","genre_group":"散文","language":"法语","author_id":"montaigne","author_name":"米歇尔·德·蒙田",
  "year_display":"1580年第一二卷（Britannica：57 and 37 chapters……published in Bordeaux in 1580）；1588年版首收第三卷13章（B296）","year_sort":1580,
  "background":["Britannica（B296）：'a French writer whose Essais (Essays) established a new literary form'（确立了新的文学形式——B296）；essais 意为'the probings and testings of his mind'（心灵的试探——B296）。","怀疑论（B296）：'a skepticism towards humanity's claims to knowledge, advocating for self-acceptance and tolerance'。","开篇名句（B296）：'I am myself the matter of my book'（我自己就是本书的题材）。"],
  "outline":["卷一（57章）/卷二（37章）1580年波尔多出版；1588年版首收第三卷13章（B296）；身后1774年《旅行日记》出版（B296）。"],
  "characters":[{"name":"蒙田","identity":"随笔作者","note":"'我自己就是本书的题材'（B296）"}],
  "themes":["随笔=心灵的试探（B296）。",
   "自我接纳与宽容的怀疑论（B296）。",
   "宗教战争中的私人城堡（B296 语境：wars of religion）。"],
  "influence":[{"text":"Britannica：'established a new literary form'（B296）。","source":"B296"},
   {"text":"Britannica：怀疑论与自我接纳、宽容的倡导（B296）。","source":"B296"}],
  "reading":{"difficulties":["篇目的长短不一。","16世纪法语引文。"],
   "editions":["《蒙田随笔全集》（人民文学出版社/上海书店出版社版本，通说待核）。","法文原版（公有领域）。"],
   "order":"先读《论友谊》《论恐惧》等名篇（通说）。"},
  "pending":["107篇总数核对。","'Que sais-je'出处待核。","培根《随笔》的对照阅读（通说）待核。"],
  "sources":["B296"],"year_source":"B296","author_source":"B296","related_works":["lunyu","zhuangzi","waerdenghu"],
  "svg":G2("《蒙田随笔》三卷结构图",[{"title":"卷一","text":"57章（B296）","color":"family"},{"title":"卷二","text":"37章","color":"main"},{"title":"卷三","text":"1588年增补（B296）","color":"gold"},{"title":"随笔","text":"心灵的试探","color":"plain"}])
},
"yiweinvshidehuaxiang": {
  "id":"yiweinvshidehuaxiang","title":"一位女士的画像","original_title":"The Portrait of a Lady","region":"美国","era":"现当代","era_detail":"19世纪末",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"henryjames","author_name":"亨利·詹姆斯",
  "year_display":"1881年（Britannica：his masterpiece, The Portrait of a Lady (1881)）","year_sort":1881,
  "background":["Britannica（B297）：'James ended this first phase of his career by producing his masterpiece, The Portrait of a Lady (1881)'——写'来自奥尔巴尼的年轻女性'带到欧洲的'狭隘的地方主义与自命'（B297）；'As a picture of Americans moving in the expatriate society of England and of Italy, this novel has no equal'（B297）。","作者（B297）：'a key transitional figure between literary realism and Modernism'。"],
  "outline":["伊莎贝尔·阿切尔继承巨款后误嫁吉尔伯特·奥斯蒙德——自由意志的悲剧（通说待核）。"],
  "characters":[{"name":"伊莎贝尔·阿切尔","identity":"美国女继承","note":"（B297）"},{"name":"吉尔伯特·奥斯蒙德","identity":"收藏家","note":"（通说待核）"}],
  "themes":["'自由意志'的悲剧：选择的重量（通说待核）。",
   "美国'天真'与欧洲'世故'的碰撞（B297 语境）。",
   "国际小说（international theme）的典范（通说待核）。"],
  "influence":[{"text":"Britannica：'his masterpiece'；'this novel has no equal'（B297）。","source":"B297"},
   {"text":"作者页：'key transitional figure between literary realism and Modernism'（B297 作者级）。","source":"B297"}],
  "reading":{"difficulties":["长句与心理视角。","国际主题（international theme）背景。"],
   "editions":["《一位女士的画像》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"亨利·詹姆斯入门首选。"},
  "pending":["1881年出版（Macmillan/Houghton Mifflin说）核对。","伊莎贝尔/奥斯蒙德人名核对。","'international theme'术语出处待核。"],
  "sources":["B297"],"year_source":"B297","author_source":"B297","related_works":["jueshi","fenwangyu","yinduzhixing"],
  "svg":G2("《女士画像》选择结构图",[{"title":"遗产","text":"自由的诱惑","color":"family"},{"title":"伊莎贝尔","text":"选择的重量","color":"main"},{"title":"奥斯蒙德","text":"艺术的空壳","color":"antagonist"},{"title":"回归","text":"最后的抉择","color":"gold"}])
},
"aojimaqi": {
  "id":"aojimaqi","title":"奥吉·玛琪历险记","original_title":"The Adventures of Augie March","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"bellow","author_name":"索尔·贝娄",
  "year_display":"1953年（Britannica：The Adventures of Augie March published 1953——'won a National Book Award in 1954'）","year_sort":1953,
  "background":["Britannica（B298）：'A picaresque story of a poor Jewish boy from Chicago, the novel tracks his progress'（芝加哥犹太穷孩子的流浪汉故事——B298）；'The novel won a National Book Award in 1954'（B298）。","作者（B298）：1976诺奖——'for the human understanding and subtle analysis of contemporary culture'；'cultural sophistication and the wisdom of the streets'构成其最大原创性（B298）。"],
  "outline":["奥吉从芝加哥底层到墨西哥、欧洲的流浪——'万物皆可尝试'的帕卡雷特（通说待核）。"],
  "characters":[{"name":"奥吉·玛琪","identity":"流浪者","note":"（通说待核）"},{"name":"劳希奶奶","identity":"房主","note":"（通说待核）"}],
  "themes":["流浪汉小说的现代转型（B298：picaresque story）。",
   "'反对屈从'的freedom（通说待核）。",
   "犹太裔美国叙事（B298 语境：Jewish American writers）。"],
  "influence":[{"text":"Britannica：'won a National Book Award in 1954'（B298）。","source":"B298"},
   {"text":"Britannica：'cultural sophistication and the wisdom of the streets……greatest originality'（B298）。","source":"B298"}],
  "reading":{"difficulties":["流浪汉体的长卷。","芝加哥犹太街景。"],
   "editions":["《奥吉·玛琪历险记》（人民文学出版社/上海译文版本，通说待核）。","英文原版。"],
   "order":"贝娄入门首选。"},
  "pending":["1953年出版（Viking Press说）核对。","奥吉·玛琪/劳希奶奶人名核对。","'拒绝屈从'（against submission）表述待核。"],
  "sources":["B298"],"year_source":"B298","author_source":"B298","related_works":["meiguoren","jueshi","嘉莉妹妹"] ,
  "svg":G2("《奥吉·玛琪》流浪结构图",[{"title":"奥吉","text":"芝加哥的犹太男孩（B298）","color":"main"},{"title":"流浪","text":"picaresque（B298）","color":"gold"},{"title":"万事皆可","text":"奥吉的信条（通说）","color":"family"},{"title":"国家图书奖","text":"1954年（B298）","color":"plain"}])
},
"pengsishixuan": {
  "id":"pengsishixuan","title":"彭斯诗选","original_title":"Poems, Chiefly in the Scottish Dialect（1786）等","region":"英国","era":"近代","era_detail":"18世纪",
  "genre":"诗选集","genre_group":"诗歌","language":"苏格兰方言/英语","author_id":"burns","author_name":"罗伯特·彭斯",
  "year_display":"1786年7月31日基尔马诺克版（Britannica：Poems, Chiefly in the Scottish Dialect appeared July 31, 1786 (Kilmarnock)）","year_sort":1786,
  "background":["Britannica（B299）：'Robert Burns is considered the national poet of Scotland'（苏格兰国民诗人）；首版含 To a Mouse、The Holy Fair 等'a handful of first-rate Scots poems'；'Tam o' Shanter'（1791）为 mock-heroic 名篇（B299）；'contribution to over three hundred songs'（含 Auld Lang Syne）；'Ploughman Poet'；为辑录改写民歌拒酬（B299）。","基尔马诺克版成功（B299）：'Simple country folk and sophisticated Edinburgh critics alike'皆赞誉。"],
  "outline":["苏格兰方言诗：致老鼠、致虱子、圣游、汤姆·奥·桑特（B299）+ 歌曲（Auld Lang Syne——通说）。"],
  "characters":[{"name":"彭斯","identity":"犁夫诗人","note":"'Ploughman Poet'（B299）"}],
  "themes":["苏格兰方言的诗性（B299）。",
   "民歌的辑录与改写（B299：over three hundred songs）。",
   "农民的讽刺与抒情（通说待核）。"],
  "influence":[{"text":"Britannica：'considered the national poet of Scotland'；Auld Lang Syne（B299）。","source":"B299"},
   {"text":"Britannica：'country folk and Edinburgh critics alike'的双重赞誉（B299）。","source":"B299"}],
  "reading":{"difficulties":["苏格兰方言的读音。","民歌曲调的对应。"],
   "editions":["《彭斯诗选》（人民文学出版社袁可嘉译本，通说待核）。","英文原版（公有领域）。"],
   "order":"先《致老鼠》《一朵红红的玫瑰》→《汤姆·奥·桑特》。"},
  "pending":["《一朵红红的玫瑰》1794年出处核对。","彭斯之夜（1月25日）待核。","袁可嘉译本信息待核。"],
  "sources":["B299"],"year_source":"B299","author_source":"B299","related_works":["xinishixuan","yijiubasi","caoyeji"],
  "svg":G2("彭斯诗歌结构图",[{"title":"致老鼠","text":"一流的苏格兰诗（B299）","color":"main"},{"title":"汤姆·奥·桑特","text":"mock-heroic（B299）","color":"gold"},{"title":"Auld Lang Syne","text":"300余首歌之一","color":"family"},{"title":"犁夫诗人","text":"国民诗人（B299）","color":"plain"}])
},
"nailinxia": {
  "id":"nailinxia","title":"奶树林下","original_title":"Under Milk Wood","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"广播剧（播音剧）","genre_group":"戏剧","language":"英语","author_id":"dylanthomas","author_name":"狄兰·托马斯",
  "year_display":"1953年纽约诗歌中心演出、1954年BBC播出（Britannica：presented at the Poetry Center in New York City in 1953, and its final version was broadcast by the BBC in 1954）","year_sort":1954,
  "background":["Britannica（B300）：'This play, which evokes the lives of the inhabitants of a small Welsh town, shows Thomas's full powers as an artist in comedy.'（威尔士小镇居民的生活——喜剧艺术的全盛）。","文体（B300 语境）：'verbal harmonies that are unique in English poetry'（英语诗歌中独一无二的语音和谐——B300）。","'His work……owed more to his Welsh background than to the prevailing taste in English literature'（B300）。"],
  "outline":["拉拉格小镇的一天：船长、织袜女与'海的呼唤'（通说待核）。"],
  "characters":[{"name":"威利船长","identity":"盲眼老船长","note":"（通说待核）"},{"name":"波利·盖特?","identity":"织袜女","note":"（通说待核）"}],
  "themes":["小镇的一天：梦与醒（通说待核）。",
   "'海的呼唤'（通说待核）。",
   "广播剧的声音艺术（通说）。"],
  "influence":[{"text":"Britannica：'shows Thomas's full powers as an artist in comedy'（B300）。","source":"B300"},
   {"text":"作者页：'verbal harmonies……unique in English poetry'（B300 作者级定位）。","source":"B300"}],
  "reading":{"difficulties":["威尔士小镇名（Llareggub——倒拼说）。","纯声音的想象。"],
   "editions":["《奶树林下》（收于狄兰·托马斯作品集，通说待核）。","英文原版（Dent）。"],
   "order":"先读诗后听剧。"},
  "pending":["小镇名 Llareggub（'bugger all'倒拼——通说待核）核对。","威利船长/波利人名核对。","BBC 1954年首播说核对（B300 已载）。"],
  "sources":["B300"],"year_source":"B300","author_source":"B300","related_works":["zhongju","dengdaigou","xinishixuan"],
  "svg":G2("《奶树林下》小镇一天图",[{"title":"拉拉格","text":"威尔士小镇（通说）","color":"family"},{"title":"威利船长","text":"盲眼的梦","color":"main"},{"title":"声音","text":"verbal harmonies（B300）","color":"gold"},{"title":"海的呼唤","text":"小镇的宿命","color":"plain"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
