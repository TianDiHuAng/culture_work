# -*- coding: utf-8 -*-
"""流水线批次5：Britannica 新核 6 作家 7 部（海鸥复用契诃夫页）"""
import json, pathlib

new_src = [
{"id":"B272","title":"Eugene ONeill — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Eugene-ONeill","type":"百科全书","verified":True,"covers":["ONeill","manchangdeheian"],"note":"2026-11-20 核对：1888-10-16纽约—1953-11-27波士顿；1936诺奖；四项普利策戏剧奖（Beyond the Horizon/Anna Christie/Strange Interlude/Long Day's Journey into Night）；'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'；《送冰的人来了》(1946)——'Considered by many to be ONeill's finest work'（页面问答）"},
{"id":"B273","title":"O. Henry — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/O-Henry","type":"百科全书","verified":True,"covers":["ohenry","ouhengliduanpianxuan"],"note":"2026-11-20 核对：1862-09-11 Greensboro—1910-06-05纽约（47岁）；'From December 1903 to January 1906 he produced a story a week for the New York Sunday World magazine'；The Four Million (1906) 含'The Gift of the Magi'；1898年入哥伦布监狱（5年减为3年）、狱中医院夜班药剂师写作；'His stories often had surprise endings, a device that became identified with his name'；'expressed the effect of coincidence on character through humour, grim or ironic'"},
{"id":"B274","title":"Henry Fielding — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Henry-Fielding","type":"百科全书","verified":True,"covers":["fielding","tangmuqiongsi"],"note":"2026-11-20 核对：1707-04-22 Sharpham Park生—1754-10-08里斯本卒；'Tom Jones……a famous comic novel……published in 1749'；'Fielding, deemed the father of the English novel by Sir Walter Scott, established a tradition of realism'；前言自述'a comic Epic-Poem in Prose'；Joseph Andrews (1742)；Shamela戏仿（1741）；协助创立鲍街 runners"},
{"id":"B275","title":"Andre Gide — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Andre-Gide","type":"百科全书","verified":True,"covers":["gide","weibizaozhe"],"note":"2026-11-20 核对：1869-11-22巴黎—1951-02-19巴黎（81岁）；1947诺贝尔奖；'Gide called his next work, Les Faux-Monnayeurs (1926; The Counterfeiters), his only novel'——'the most complex and intricately constructed of his works'；L'Immoraliste (1902) 等为创作盛期"},
{"id":"B276","title":"Romain Rolland — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Romain-Rolland","type":"百科全书","verified":True,"covers":["rolland","yuehankelisituofu"],"note":"2026-11-20 核对：1866-01-29 Clamecy生—1944-12-30 Vézelay卒；1915诺贝尔奖（'For this and for his pamphlet Au-dessus de la mêlée'）；'Rolland's masterpiece, Jean-Christophe...is a prime example of the roman fleuve (novel cycle) in France'；Jean-Christophe 10卷（1904–12）刊于 Les Cahiers de la Quinzaine；'Vie de Beethoven (1903)'传记——贝多芬'was for Rolland the universal musician above all the others'"},
{"id":"B277","title":"Rudyard Kipling — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Rudyard-Kipling","type":"百科全书","verified":True,"covers":["kipling","jim"],"note":"2026-11-20 核对：1865-12-30孟买生—1936-01-18伦敦卒（70岁）；1907诺贝尔奖——'the first Englishman to be so honoured'；'Kim (1901), about an Irish orphan in India, is a classic'；'The Jungle Book (1894) and The Second Jungle Book (1895) are stylistically superb collections of stories'；1882—1889年回印度做记者七年"},
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
"ONeill": {
  "id": "ONeill", "name": "尤金·奥尼尔", "foreign_name": "Eugene ONeill（尤金·格莱斯顿·奥尼尔，1888-10-16—1953-11-27）",
  "country": "美国", "birth": 1888, "death": 1953, "birth_year": 1888, "death_year": 1953, "era": "现当代",
  "summary": "奥尼尔，纽约人，美国最重要的剧作家——'a foremost American dramatist who won the 1936 Nobel Prize in Literature and is widely credited with elevating American theatre into a serious literary medium'（被广泛认为使美国戏剧成为严肃文学媒介——Britannica）。四项普利策戏剧奖（Beyond the Horizon、Anna Christie、Strange Interlude、Long Day's Journey into Night——B272）；'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'（身后1956年上演的杰作《进入黑夜的漫长旅程》——B272）。",
  "timeline": [
    {"year": 1888, "text": "10月16日生于纽约（Britannica：Born October 16, 1888, New York City）。", "src": "B272"},
    {"year": 1920, "text": "《天边外》获首个普利策戏剧奖（Britannica：Beyond the Horizon……first of four Pulitzer prizes）。", "src": "B272"},
    {"year": 1936, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1936）。", "src": "B272"},
    {"year": 1956, "text": "《进入黑夜的漫长旅程》身后上演（Britannica：produced posthumously 1956）。", "src": "B272"},
    {"year": 1953, "text": "11月27日卒于波士顿（Britannica：died November 27, 1953, Boston）。", "src": "B272"}],
  "major_works": [
    {"work_id": "manchangdeheian", "note": "戏剧（Britannica：masterpiece，身后1956）"},
    {"title": "送冰的人来了", "note": "（Britannica：The Iceman Cometh (1946)）"},
    {"title": "天边外、安娜·克里斯蒂", "note": "（Britannica：普利策作品）"}],
  "style": [
    "'以家庭悲剧与希腊悲剧'为源（Britannica：drew heavily on family tragedy and Greek tragedy）。",
    "使美国戏剧成为严肃文学媒介（B272：elevating American theatre）。",
    "自传性：《进入黑夜的漫长旅程》写自家毒瘾与病（通说待核）。"],
  "status": "Britannica 定位奥尼尔为美国最重要的剧作家、1936年诺奖得主、四项普利策戏剧奖（B272）。",
  "sources": ["B272"], "dates_source": "B272",
  "pending": ["《进入黑夜的漫长旅程》写作年份（1939—41说）与身后1956年上演核对。", "四项普利策年份逐项核对。", "自传性（家庭成员对应）待核。"]
},
"ohenry": {
  "id": "ohenry", "name": "欧·亨利", "foreign_name": "O. Henry（欧·亨利，本名威廉·西德尼·波特，1862-09-11—1910-06-05）",
  "country": "美国", "birth": 1862, "death": 1910, "birth_year": 1862, "death_year": 1910, "era": "近代",
  "summary": "欧·亨利，本名威廉·西德尼·波特（Britannica），美国短篇小说家——以温暖幽默地写日常生活特别是纽约小人物著称（Britannica 语境：warm, humorous tales about everyday life, especially in New York City）。1903年12月至1906年1月'produced a story a week for the New York Sunday World magazine'（每周一篇——B273）；The Four Million (1906) 收'widely popular'的《麦琪的礼物》（B273）；1898年入俄亥俄州监狱（刑期五年减为三年），狱中医院夜班药剂师写作（B273）。'His stories often had surprise endings, a device that became identified with his name'（'欧·亨利式结尾'——B273）。",
  "timeline": [
    {"year": 1862, "text": "9月11日生于北卡罗来纳州格林斯伯勒（Britannica）。", "src": "B273"},
    {"year": 1898, "text": "入哥伦布监狱（刑期缩短为三年），狱中写作（B273）。", "src": "B273"},
    {"year": 1903, "text": "12月起为《纽约世界报》周日杂志每周一篇（至1906年1月）（B273）。", "src": "B273"},
    {"year": 1906, "text": "《四百万》出版，含《麦琪的礼物》（B273）。", "src": "B273"},
    {"year": 1910, "text": "6月5日卒于纽约（B273）。", "src": "B273"}],
  "major_works": [
    {"work_id": "ouhengliduanpianxuan", "note": "短篇选（B273：The Four Million 1906）"},
    {"title": "最后一片叶子、警察与赞美诗", "note": "（通说待核）"},
    {"title": "白菜与皇帝", "note": "（通说待核）"}],
  "style": [
    "'欧·亨利式结尾'：surprise endings（B273）。",
    "'幽默、严峻或反讽的巧合'（B273：effect of coincidence on character through humour）。",
    "纽约小人物的温暖书写（B273 语境）。"],
  "status": "Britannica 定位欧·亨利为美国短篇名家、'欧·亨利式结尾'的命名来源；'当此风过时也使其失去批评界的青睐'（B273：cost him critical favour）。",
  "sources": ["B273"], "dates_source": "B273",
  "pending": ["本名 William Sydney Porter（B273 已载 pen name of William Sydney Porter）核对。", "《麦琪的礼物》1905年首发（《纽约世界报》说）待核。", "'欧·亨利式结尾'中文术语出处待核。"]
},
"fielding": {
  "id": "fielding", "name": "亨利·菲尔丁", "foreign_name": "Henry Fielding（亨利·菲尔丁，1707-04-22—1754-10-08）",
  "country": "英国", "birth": 1707, "death": 1754, "birth_year": 1707, "death_year": 1754, "era": "近代",
  "summary": "菲尔丁，英国小说家、剧作家与讽刺作家——与理查森并称英国小说的奠基者（Britannica：alongside Samuel Richardson, is regarded as a founder of the English novel）；司各特称之为'英国小说之父'（Britannica：deemed the 'father of the English novel' by Sir Walter Scott, established a tradition of realism）。1737年《许可法》终结其剧作生涯后改任律师、记者与治安官，协助创立鲍街 runners（Britannica）。《汤姆·琼斯》（1749）——'a famous comic novel'，前言自述'a comic Epic-Poem in Prose'（散文体滑稽史诗——B274）。",
  "timeline": [
    {"year": 1707, "text": "4月22日生于萨默塞特郡（Britannica：Born April 22, 1707, Sharpham Park, Somerset）。", "src": "B274"},
    {"year": 1742, "text": "《约瑟夫·安德鲁斯》匿名出版（Britannica：published anonymously in 1742）。", "src": "B274"},
    {"year": 1749, "text": "《汤姆·琼斯》出版（Britannica：published in 1749）。", "src": "B274"},
    {"year": 1754, "text": "10月8日卒于里斯本（Britannica：Died Oct. 8, 1754, Lisbon）。", "src": "B274"}],
  "major_works": [
    {"work_id": "tangmuqiongsi", "note": "长篇（Britannica：1749）"},
    {"title": "约瑟夫·安德鲁斯", "note": "（Britannica：1742）"},
    {"title": "大伟人江奈生·魏尔德", "note": "（通说待核）"}],
  "style": [
    "'散文体滑稽史诗'（B274：a comic Epic-Poem in Prose——前言自述）。",
    "现实主义的奠基传统（B274：tradition of realism）。",
    "讽刺与治安官实务的双面（B274 语境：magistrate，Bow Street Runners）。"],
  "status": "Britannica 定位菲尔丁为英国小说奠基者之一、被司各特称'英国小说之父'（B274）。",
  "sources": ["B274"], "dates_source": "B274",
  "pending": ["《汤姆·琼斯》十八卷结构核对。", "《莎米拉》1741年匿名出版（B274 已载）核对。", "鲍街 runners 创立年份待核。"]
},
"gide": {
  "id": "gide", "name": "安德烈·纪德", "foreign_name": "André Gide（安德烈·纪德，1869-11-22—1951-02-19）",
  "country": "法国", "birth": 1869, "death": 1951, "birth_year": 1869, "death_year": 1951, "era": "现当代",
  "summary": "纪德，巴黎人，法国作家、人文主义者与道德家（Britannica：a French writer, humanist, and moralist）——其 récits 与小说'probed individual freedom and moral ambiguity'（探察个人自由与道德含混——Britannica）。1947年获诺贝尔文学奖（Britannica）。《伪币制造者》（1926）——'Gide called his next work, Les Faux-Monnayeurs (1926; The Counterfeiters), his only novel'（自称为其唯一的长篇小说——B275）；'the most complex and intricately constructed of his works'（B275）。《背德者》（1902）为其创作盛期之作（B275）。",
  "timeline": [
    {"year": 1869, "text": "11月22日生于巴黎（Britannica：Born November 22, 1869, Paris）。", "src": "B275"},
    {"year": 1902, "text": "《背德者》出版（Britannica：L'Immoraliste (1902)）。", "src": "B275"},
    {"year": 1926, "text": "《伪币制造者》出版（Britannica：Les Faux-Monnayeurs (1926)）。", "src": "B275"},
    {"year": 1947, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1947）。", "src": "B275"},
    {"year": 1951, "text": "2月19日卒于巴黎（Britannica：Died February 19, 1951, Paris）。", "src": "B275"}],
  "major_works": [
    {"work_id": "weibizaozhe", "note": "长篇（Britannica：1926，唯一小说）"},
    {"title": "背德者、窄门", "note": "（Britannica：L'Immoraliste (1902)，Strait Is the Gate）"},
    {"title": "田园交响曲", "note": "（Britannica：The Pastoral Symphony）"}],
  "style": [
    "'探察个人自由与道德含混'（B275：probed individual freedom and moral ambiguity）。",
    "'最复杂、结构最精巧'的作品（《伪币制造者》——B275）。",
    "不连续场景（B275：told through discontinuous scenes）。"],
  "status": "Britannica 定位纪德为法国作家与道德家、1947年诺奖得主；自认《伪币制造者》为其唯一'novel'（B275）。",
  "sources": ["B275"], "dates_source": "B275",
  "pending": ["《伪币制造者》'小说中的小说'嵌套结构待核。", "《背德者》1902年出版细节核对。", "《人间食粮》（1897）待核。"]
},
"rolland": {
  "id": "rolland", "name": "罗曼·罗兰", "foreign_name": "Romain Rolland（罗曼·罗兰，1866-01-29—1944-12-30）",
  "country": "法国", "birth": 1866, "death": 1944, "birth_year": 1866, "death_year": 1944, "era": "现当代",
  "summary": "罗兰，法国小说家、剧作家与散文家——致力于和平主义、反法西斯主义与艺术天才研究（Britannica：committed to pacifism, anti-fascism, and the study of artistic genius）。'Rolland's masterpiece, Jean-Christophe... is a prime example of the roman fleuve (novel cycle) in France'（大河小说在法国的典范——B276）；10卷（1904—12）。1915年获诺贝尔文学奖——'For this and for his pamphlet Au-dessus de la mêlée (1915...)'（连同反战小册子《超然于纷争之上》——B276）。贝多芬传记（1903）——贝多芬'was for Rolland the universal musician above all the others'（B276）。",
  "timeline": [
    {"year": 1866, "text": "1月29日生于克拉姆西（Britannica：Born Jan. 29, 1866, Clamecy, France）。", "src": "B276"},
    {"year": 1904, "text": "《约翰·克利斯朵夫》开始出版（1904—12，10卷）（B276）。", "src": "B276"},
    {"year": 1915, "text": "获诺贝尔文学奖（B276：Nobel Prize 1915）。", "src": "B276"},
    {"year": 1944, "text": "12月30日卒于韦兹莱（B276：died Dec. 30, 1944, Vézelay）。", "src": "B276"}],
  "major_works": [
    {"work_id": "yuehankelisituofu", "note": "十卷大河小说（B276：masterpiece）"},
    {"title": "贝多芬传、米开朗琪罗传、托尔斯泰传", "note": "（B276：Vie de Beethoven (1903) 等传记系列）"},
    {"title": "欣悦的灵魂", "note": "（B276：L'Âme-enchantée 1922–33）"}],
  "style": [
    "'大河小说'（roman fleuve）的法国典范（B276）。",
    "英雄传记系列：'passion for the heroic'（B276）。",
    "和平主义与反法西斯（B276：committed to pacifism, anti-fascism）。"],
  "status": "Britannica 定位罗兰为1915年诺奖得主、《约翰·克利斯朵夫》作者与《贝多芬传》等英雄传记的写作者（B276）。",
  "sources": ["B276"], "dates_source": "B276",
  "pending": ["十卷分期（1904—1912）核对。", "傅雷译本（4册说）待核。", "《超然于纷争之上》1915年细节核对。"]
},
"kipling": {
  "id": "kipling", "name": "鲁德亚德·吉卜林", "foreign_name": "Rudyard Kipling（鲁德亚德·吉卜林，1865-12-30—1936-01-18）",
  "country": "英国", "birth": 1865, "death": 1936, "birth_year": 1865, "death_year": 1936, "era": "近代",
  "summary": "吉卜林，生于孟买的英国短篇家、诗人与小说家——'best known for celebrating British imperialism, writing about British soldiers in India, and creating children's tales such as The Jungle Book'（以歌颂英帝国、写印度英军与《丛林之书》等儿童故事著称——Britannica）。1907年获诺贝尔文学奖——'the first English writer to receive the Nobel Prize'（首位获诺奖的英国作家——Britannica）。'Kim (1901), about an Irish orphan in India, is a classic'（《吉姆》经典——B277）；'The Jungle Book (1894) and The Second Jungle Book (1895) are stylistically superb collections of stories'（B277）。",
  "timeline": [
    {"year": 1865, "text": "12月30日生于孟买（Britannica：Born December 30, 1865, Bombay）。", "src": "B277"},
    {"year": 1882, "text": "回印度做记者七年（Britannica：returned to India in 1882……worked for seven years as a journalist）。", "src": "B277"},
    {"year": 1901, "text": "《吉姆》出版（B277：Kim (1901)）。", "src": "B277"},
    {"year": 1907, "text": "获诺贝尔文学奖（B277：Nobel Prize 1907）。", "src": "B277"},
    {"year": 1936, "text": "1月18日卒于伦敦（B277：Died January 18, 1936, London）。", "src": "B277"}],
  "major_works": [
    {"work_id": "jim", "note": "长篇（B277：1901，classic）"},
    {"title": "丛林之书（一、二）", "note": "（B277：1894/1895，'stylistically superb'）"},
    {"title": "山里的平凡故事", "note": "（B277：Plain Tales from the Hills 1888）"}],
  "style": [
    "'stylistically superb'的丛林故事（B277）。",
    "帝国书写与争议（Britannica 语境：celebrating British imperialism）。",
    "'讲故事'的才能与'平衡 cohesive 长篇'的不稳定（B277：excelled at telling a story but was inconsistent in producing balanced, cohesive novels）。"],
  "status": "Britannica 定位吉卜林为1907年诺奖得主（首位英国获奖者）；《吉姆》为经典（B277）；其帝国立场引发后世争议（通说待核）。",
  "sources": ["B277"], "dates_source": "B277",
  "pending": ["《吉姆》故事细节（西藏喇嘛/大游戏）待核。", "帝国立场争议（后殖民批评）待核。", "《丛林之书》篇目待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

G = G2

works = {
"manchangdeheian": {
  "id":"manchangdeheian","title":"进入黑夜的漫长旅程","original_title":"Long Day's Journey into Night","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"自传性戏剧","genre_group":"戏剧","language":"英语","author_id":"ONeill","author_name":"尤金·奥尼尔",
  "year_display":"身后1956年上演（Britannica：His masterpiece, Long Day's Journey into Night (produced posthumously 1956)）","year_sort":1956,
  "background":["Britannica（B272）：'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'——杰作；'drew heavily on family tragedy and Greek tragedy'。","四项普利策戏剧奖之一（B272：four Pulitzer prizes in drama——含本作）。"],
  "outline":["蒂龙一家的一天：吗啡、酗酒与病——'过去'如何纠缠当下（通说待核）。"],
  "characters":[{"name":"詹姆斯·蒂龙","identity":"父亲","note":"吝啬演员（通说待核）"},{"name":"玛丽","identity":"母亲","note":"吗啡成瘾（通说待核）"},{"name":"埃德蒙","identity":"小儿子","note":"作者化身（通说待核）"}],
  "themes":["家庭的毒瘾与宽恕（通说待核）。",
   "'希腊悲剧'的家庭版（B272 语境）。",
   "自传性（通说待核——奥尼尔家庭）。"],
  "influence":[{"text":"Britannica：'His masterpiece'（B272）。","source":"B272"},
   {"text":"Britannica：四项普利策戏剧奖之一（B272）。","source":"B272"}],
  "reading":{"difficulties":["自传对应（奥尼尔家族）。","长独白的节奏。"],
   "editions":["《进入黑夜的漫长旅程》（人民文学出版社/湖南文艺出版社版本，通说待核）。","英文原版（Yale）。"],
   "order":"奥尼尔收官之作。"},
  "pending":["身后1956年（Yale University Press出版/百老汇演出说）核对。","蒂龙一家对应（奥尼尔父兄）待核。","四项普利策年份逐项核对。"],
  "sources":["B272"],"year_source":"B272","author_source":"B272","related_works":["leiyu","richu","yingtaoyuan"],
  "svg":G("《漫长旅程》家庭结构图",[{"title":"父亲","text":"吝啬与悔恨","color":"antagonist"},{"title":"母亲","text":"吗啡的回归","color":"main"},{"title":"埃德蒙","text":"作者的化身","color":"gold"},{"title":"雾","text":"过去的纠缠","color":"family"}])
},
"ouhengliduanpianxuan": {
  "id":"ouhengliduanpianxuan","title":"欧·亨利短篇小说选","original_title":"The Four Million 等","region":"美国","era":"近代","era_detail":"20世纪初",
  "genre":"短篇小说集","genre_group":"小说","language":"英语","author_id":"ohenry","author_name":"欧·亨利（O. Henry）",
  "year_display":"1906年（Britannica：The Four Million (1906)——含《麦琪的礼物》）","year_sort":1906,
  "background":["Britannica（B273）：'From December 1903 to January 1906 he produced a story a week for the New York Sunday World magazine'；'Both The Four Million (1906) and The Trimmed Lamp (1907) explored the lives of the multitude of New York'——'the former contained the widely popular story The Gift of the Magi'。","风格（B273）：'His stories often had surprise endings, a device that became identified with his name'；'expressed the effect of coincidence on character through humour, grim or ironic'。"],
  "outline":["名篇谱系（B273+通说）：《麦琪的礼物》《最后一片叶子》《警察与赞美诗》等。"],
  "characters":[{"name":"小人物们","identity":"纽约多众","note":"'the multitude of New York'（B273）"}],
  "themes":["'欧·亨利式结尾'（B273）。",
   "巧合对性格的作用（B273：effect of coincidence on character）。",
   "小人物的温暖（B273 语境）。"],
  "influence":[{"text":"Britannica：'surprise endings, a device that became identified with his name'（B273）。","source":"B273"},
   {"text":"Britannica：每周一篇的生产力（B273）。","source":"B273"}],
  "reading":{"difficulties":["'欧·亨利式结尾'的预期管理。","1900年代纽约俚语。"],
   "editions":["《欧·亨利短篇小说选》（人民文学出版社王永年译本，通说待核）。","英文原版（公有领域）。"],
   "order":"先《麦琪的礼物》→《最后一片叶子》。"},
  "pending":["《麦琪的礼物》首发日期核对。","《最后一片叶子》篇名（The Last Leaf）核对。","王永年译本信息待核。"],
  "sources":["B273"],"year_source":"B273","author_source":"B273","related_works":["mauposangxuan","kafuxuan","qikefuxuan"],
  "svg":G("欧·亨利结尾图",[{"title":"麦琪的礼物","text":"互赠的牺牲","color":"main"},{"title":"最后一片叶子","text":"常春藤的奇迹（通说）","color":"gold"},{"title":"巧合","text":" grim 或 ironic（B273）","color":"antagonist"},{"title":"结尾","text":"欧·亨利式反转","color":"family"}])
},
"tangmuqiongsi": {
  "id":"tangmuqiongsi","title":"汤姆·琼斯","original_title":"The History of Tom Jones, a Foundling","region":"英国","era":"近代","era_detail":"18世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"fielding","author_name":"亨利·菲尔丁",
  "year_display":"1749年出版（Britannica：Tom Jones……is a famous comic novel by Henry Fielding published in 1749）","year_sort":1749,
  "background":["Britannica（B274）：'a famous comic novel'；'Fielding's detailed planning and structure made Tom Jones a literary masterpiece'（精心的规划与结构使其成为文学杰作——B274）。","前言自述（B274）：'a comic Epic-Poem in Prose'（散文体滑稽史诗）。","司各特（B274）：'father of the English novel'。"],
  "outline":["弃儿汤姆的流浪与身世之谜：从乡绅家到伦敦的十八卷（通说待核）。","索菲娅的出走与团圆（通说待核）。"],
  "characters":[{"name":"汤姆·琼斯","identity":"弃儿","note":"热情的浪子"},{"name":"索菲娅","identity":"乡绅之女","note":"（通说待核）"},{"name":"布利非","identity":"伪君子表弟","note":"（通说待核）"}],
  "themes":["'散文体滑稽史诗'（B274：comic Epic-Poem in Prose——前言自述）。",
   "结构与规划的典范（B274：detailed planning and structure）。",
   "人性的全光谱（通说）。"],
  "influence":[{"text":"Britannica：'literary masterpiece'；'father of the English novel'（B274）。","source":"B274"},
   {"text":"作者页：菲尔丁现实主义传统（B274）。","source":"B274"}],
  "reading":{"difficulties":["十八卷结构。","18世纪英语叙事口吻。"],
   "editions":["《汤姆·琼斯》（人民文学出版社黄乔生译本？——通说待核）。","英文原版（公有领域）。"],
   "order":"英国18世纪小说首选（与《鲁滨逊》并列）。"},
  "pending":["1749年2月出版核对。","汤姆/索菲娅/布利非人名核对。","黄乔生译本信息待核。"],
  "sources":["B274"],"year_source":"B274","author_source":"B274","related_works":["lubinxun","aoman","lianaizhong"],
  "svg":G("《汤姆·琼斯》史诗结构图",[{"title":"弃儿","text":"身世之谜","color":"family"},{"title":"伦敦","text":"十八卷的流浪","color":"main"},{"title":"滑稽史诗","text":"自述的文类（B274）","color":"gold"},{"title":"团圆","text":"身世的揭晓","color":"plain"}])
},
"weibizaozhe": {
  "id":"weibizaozhe","title":"伪币制造者","original_title":"Les Faux-Monnayeurs（The Counterfeiters）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"gide","author_name":"安德烈·纪德",
  "year_display":"1926年（Britannica：Les Faux-Monnayeurs (1926; The Counterfeiters)——'his only novel'）","year_sort":1926,
  "background":["Britannica（B275）：'Gide called his next work, Les Faux-Monnayeurs (1926; The Counterfeiters), his only novel'；'the most complex and intricately constructed of his works'（其最复杂、结构最精巧之作——B275）；'told through discontinuous scenes'（不连续场景）。","作者：1947年诺奖（B275）。"],
  "outline":["中学生 bernard？——不：贝尔纳与奥利维埃：'伪币'（假币与假情）的巴黎（通说待核）。","'小说中的小说'：爱德华的日记（通说待核）。"],
  "characters":[{"name":"爱德华","identity":"作家","note":"日记体嵌套（通说待核）"},{"name":"贝尔纳","identity":"中学生","note":"（通说待核）"}],
  "themes":["'伪币'：假与真的哲学（通说待核）。",
   "不连续场景（B275）。",
   "'唯一小说'的自认（B275）。"],
  "influence":[{"text":"Britannica：'the most complex and intricately constructed of his works'（B275）。","source":"B275"},
   {"text":"Britannica：1947年诺奖（B275 作者级）。","source":"B275"}],
  "reading":{"difficulties":["嵌套结构。","多人物。"],
   "editions":["《伪币制造者》（人民文学出版社/上海译文版本，通说待核）。","法文原版（Gallimard）。"],
   "order":"先《背德者》《窄门》后本作。"},
  "pending":["1926年出版（Gallimard/NRF说）核对。","爱德华/贝尔纳人名核对。","'唯一小说'的自称与评论界立场待核。"],
  "sources":["B275"],"year_source":"B275","author_source":"B275","related_works":["xianzhi","duoluo","qingzhong"],
  "svg":G("《伪币制造者》嵌套结构图",[{"title":"伪币","text":"假与真","color":"main"},{"title":"爱德华日记","text":"小说中的小说（通说）","color":"gold"},{"title":"不连续场景","text":"B275 方法","color":"family"},{"title":"少年们","text":"堕落的诱惑","color":"antagonist"}])
},
"yuehankelisituofu": {
  "id":"yuehankelisituofu","title":"约翰·克利斯朵夫","original_title":"Jean-Christophe","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"十卷大河小说","genre_group":"小说","language":"法语","author_id":"rolland","author_name":"罗曼·罗兰",
  "year_display":"1904—1912年十卷（Britannica：Jean-Christophe, 10 vol. (1904–12)——'a prime example of the roman fleuve'）","year_sort":1908,
  "background":["Britannica（B276）：'Rolland's masterpiece, Jean-Christophe... is a prime example of the roman fleuve（novel cycle）in France'；10卷刊于 Les Cahiers de la Quinzaine（B276）。","题材（通说待核）：德国血统的音乐家约翰·克利斯朵夫·克拉夫特的一生——以贝多芬为原型（B276：Vie de Beethoven 语境）。"],
  "outline":["音乐家的一生：德国—巴黎—瑞士—意大利（通说待核）。","'音乐'与'生活'的同构（通说待核）。"],
  "characters":[{"name":"约翰·克利斯朵夫·克拉夫特","identity":"音乐家","note":"以贝多芬为原型（通说待核）"},{"name":"奥里维","identity":"法国友人","note":"（通说待核）"}],
  "themes":["'大河小说'（B276：roman fleuve）。",
   "英雄与音乐（B276：贝多芬传记语境）。",
   "法德文化的桥（通说待核）。"],
  "influence":[{"text":"Britannica：'masterpiece'；'prime example of the roman fleuve'（B276）。","source":"B276"},
   {"text":"Britannica：1915年诺奖（B276 作者级）。","source":"B276"}],
  "reading":{"difficulties":["十卷体量。","音乐结构章节。"],
   "editions":["《约翰·克利斯朵夫》（人民文学出版社傅雷译本四册，通说待核）。","法文原版（公有领域）。"],
   "order":"傅雷译本为中文世界经典。"},
  "pending":["十卷分卷与四册（傅雷）对应核对。","克拉夫特人名核对。","傅雷译本（1930—40年代）信息待核。"],
  "sources":["B276"],"year_source":"B276","author_source":"B276","related_works":["beican","jian","renshijian"],
  "svg":G("《约翰·克利斯朵夫》大河结构图",[{"title":"诞生","text":"莱茵河畔","color":"family"},{"title":"音乐","text":"一生的乐章","color":"main"},{"title":"巴黎","text":"文化的战场","color":"antagonist"},{"title":"大河","text":"roman fleuve（B276）","color":"gold"}])
},
"jim": {
  "id":"jim","title":"吉姆","original_title":"Kim","region":"英国","era":"近代","era_detail":"19世纪末",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"kipling","author_name":"鲁德亚德·吉卜林",
  "year_display":"1901年（Britannica：Kim (1901), about an Irish orphan in India, is a classic）","year_sort":1901,
  "background":["Britannica（B277）：'Kim (1901), about an Irish orphan in India, is a classic'（写爱尔兰孤儿在印度的经典）。","吉卜林1907年诺奖——'the first English writer to receive the Nobel Prize'（B277）。","题材（通说待核）：孤儿吉姆与西藏喇嘛的'大游戏'（Great Game）间谍之旅。"],
  "outline":["吉姆与喇嘛的寻找之河：从拉合尔到喜马拉雅（通说待核）。"],
  "characters":[{"name":"吉姆","identity":"孤儿","note":"（通说待核）"},{"name":"喇嘛","identity":"西藏僧人","note":"寻找圣河（通说待核）"}],
  "themes":["'大游戏'：英俄在中亚的谍战（通说待核）。",
   "印度全景（通说）。",
   "寻找与身份（通说待核）。"],
  "influence":[{"text":"Britannica：'is a classic'（B277）。","source":"B277"},
   {"text":"Britannica：1907诺奖——首位英国获奖者（B277）。","source":"B277"}],
  "reading":{"difficulties":["'大游戏'史。","印度地名与宗教。"],
   "editions":["《吉姆》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"吉卜林代表作。"},
  "pending":["1901年出版（Macmillan说）核对。","吉姆/喇嘛人名核对。","'大游戏'（Great Game）术语核对。"],
  "sources":["B277"],"year_source":"B277","author_source":"B277","related_works":["hakebei","shijiemori","yidudewunv"],
  "svg":G("《吉姆》大游戏结构图",[{"title":"拉合尔","text":"出发的炮台","color":"family"},{"title":"寻找圣河","text":"喇嘛的祈愿","color":"main"},{"title":"大游戏","text":"中亚的谍战（通说）","color":"antagonist"},{"title":"经典","text":"B277 定位","color":"gold"}])
},
"haiou": {
  "id":"haiou","title":"海鸥","original_title":"Чайка（The Seagull）","region":"俄国","era":"近代","era_detail":"19世纪末",
  "genre":"四幕喜剧","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
  "year_display":"1896年首演（通说待核；作者页 B270 存目：'Notable Works'——The Seagull；1898年莫斯科艺术剧院成功说通说待核）","year_sort":1896,
  "background":["作者页（B270）：契诃夫 major works 存目含'The Seagull'（B270 作者页定位）。","契诃夫原则（B270）：'Chekhov's gun'与'what is left unsaid seems much more important than what is said'。","1898年莫斯科艺术剧院复排成功（Britannica 相关问答提及——通说待核）。"],
  "outline":["尼娜与特里波列夫：新戏剧的失败与'海鸥'的射杀（通说待核）。","两年后：尼娜的重来与特里波列夫的自尽（通说待核）。"],
  "characters":[{"name":"尼娜","identity":"少女演员","note":"海鸥的化身（通说待核）"},{"name":"特里波列夫","identity":"青年作家","note":"（通说待核）"},{"name":"阿尔卡基娜","identity":"名演员","note":"母亲（通说待核）"}],
  "themes":["新形式的失败与坚持（通说待核）。",
   "海鸥的象征：射杀与重生（通说待核）。",
   "'潜台词'的戏剧（B270 语境）。"],
  "influence":[{"text":"作者页：契诃夫 Notable Works 存目（B270）。","source":"B270"},
   {"text":"作者页：'Chekhov's gun'与未说出之重（B270）。","source":"B270"}],
  "reading":{"difficulties":["'潜台词'的表演法。","莫斯科艺术剧院史。"],
   "editions":["《海鸥》（人民文学出版社《契诃夫戏剧集》，通说待核）。","俄文原版（公有领域）。"],
   "order":"契诃夫戏剧四部之首。"},
  "pending":["1896年彼得堡首演失败说核对。","1898年莫斯科艺术剧院复排说核对。","尼娜/特里波列夫人名核对。"],
  "sources":["B270"],"year_source":"B270","author_source":"B270","related_works":["yingtaoyuan","leiyu","beijingren"],
  "svg":G("《海鸥》射杀结构图",[{"title":"射杀的海鸥","text":"创作的隐喻（通说）","color":"main"},{"title":"尼娜","text":"两年的重来","color":"gold"},{"title":"特里波列夫","text":"失败的作家","color":"antagonist"},{"title":"新形式","text":"戏剧的寻找","color":"family"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
