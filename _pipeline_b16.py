# -*- coding: utf-8 -*-
"""流水线批16：Britannica 新核 3 作家 3 部 + 零成本直写 2 部"""
import json, pathlib

new_src = [
{"id":"B315","title":"Carson McCullers — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Carson-McCullers","type":"百科全书","verified":True,"covers":["mccalles","xinshigudeLieshou"],"note":"2026-11-21 核对：1917-02-19佐治亚州哥伦布生（原名 Lula Carson Smith）—1967-09-29纽约州卒；'The Heart Is a Lonely Hunter (1940)'——成名作；'The Member of the Wedding (1946)'；'The Ballad of the Sad Café'；'her novels……explore the spiritual isolation of misfits and outcast characters in the small towns of the South'"},
{"id":"B316","title":"Truman Capote — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Truman-Capote","type":"百科全书","verified":True,"covers":["capote","lengxue"],"note":"2026-11-21 核对：1924-09-30新奥尔良生—1984-08-25洛杉矶卒；In Cold Blood (1966)——'nonfiction novel'（非虚构小说）开创者之一，写堪萨斯一家四口被杀案；Other Voices, Other Rooms (1948) 处女作； Breakfast at Tiffany's (1958)"},
{"id":"B317","title":"Ralph Ellison — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ralph-Ellison","type":"百科全书","verified":True,"covers":["ellison","kanbujian3"],"note":"2026-11-21 核对：1914-03-01俄克拉何马城生—1994-04-16卒；Invisible Man (1952)——'the story of an unnamed Black man'；1953年 National Book Award；'Invisible Man'——'the narrator moves through a series of episodes'； '.shadow and act'——散文集 Shadow and Act (1964)"},
{"id":"B318","title":"Washington Irving — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Washington-Irving","type":"百科全书","verified":True,"covers":["ouwen","jianWenzhaji"],"note":"2026-11-21 核对：1783-04-03纽约生—1859-12-28卒；The Sketch Book (1819–20)——含'Rip Van Winkle'与'The Legend of Sleepy Hollow'；'first American author to achieve international fame'；《纽约外史》（A History of New York, 1809，Diedrich Knickerbocker 署名）"},
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
"mccalles": {
  "id": "mccalles", "name": "卡森·麦卡勒斯", "foreign_name": "Carson McCullers（卡森·麦卡勒斯，原名 Lula Carson Smith，1917-02-19—1967-09-29）",
  "country": "美国", "birth": 1917, "death": 1967, "birth_year": 1917, "death_year": 1967, "era": "现当代",
  "summary": "麦卡勒斯，佐治亚州哥伦布生（原名 Lula Carson Smith——B315），美国南方作家——'her novels……explore the spiritual isolation of misfits and outcast characters in the small towns of the South'（探索南方小镇格格不入者的精神孤独——B315）。成名作《心是孤独的猎手》（The Heart Is a Lonely Hunter，1940）；《婚礼的成员》（The Member of the Wedding，1946）；《伤心咖啡馆之歌》（The Ballad of the Sad Café）均为名篇（B315）。",
  "timeline": [
    {"year": 1917, "text": "2月19日生于佐治亚州哥伦布（B315：原名 Lula Carson Smith）。", "src": "B315"},
    {"year": 1940, "text": "《心是孤独的猎手》出版（B315：The Heart Is a Lonely Hunter (1940)）。", "src": "B315"},
    {"year": 1967, "text": "9月29日卒于纽约州（B315：died September 29, 1967, New York State）。", "src": "B315"}],
  "major_works": [
    {"work_id": "xinshigudeLieshou", "note": "长篇（B315：1940）"},
    {"title": "婚礼的成员", "note": "（B315：The Member of the Wedding (1946)）"},
    {"title": "伤心咖啡馆之歌", "note": "（B315：The Ballad of the Sad Café）"}],
  "style": [
    "'misfits and outcast characters'的精神孤独（B315）。",
    "南方小镇的世界（B315：small towns of the South）。",
    "哥特与抒情的混合（通说待核）。"],
  "status": "Britannica 定位麦卡勒斯为南方精神孤独的书写者（B315）。",
  "sources": ["B315"], "dates_source": "B315",
  "pending": ["《婚礼的成员》1960年戏剧改编说待核。","《伤心咖啡馆之歌》1951年说待核。","'哥特'标签的学术讨论待核。"]
},
"capote": {
  "id": "capote", "name": "杜鲁门·卡波特", "foreign_name": "Truman Capote（杜鲁门·卡波特，1924-09-30—1984-08-25）",
  "country": "美国", "birth": 1924, "death": 1984, "birth_year": 1924, "death_year": 1984, "era": "现当代",
  "summary": "卡波特，新奥尔良生，美国作家——'nonfiction novel'（非虚构小说）的先驱之一，In Cold Blood (1966) 写堪萨斯克拉特一家四口被杀案（B316）。处女作 Other Voices, Other Rooms (1948)；《蒂凡尼的早餐》(Breakfast at Tiffany's, 1958)（B316）。",
  "timeline": [
    {"year": 1924, "text": "9月30日生于新奥尔良（B316：Born September 30, 1924, New Orleans）。", "src": "B316"},
    {"year": 1948, "text": "处女作 Other Voices, Other Rooms 出版（B316）。", "src": "B316"},
    {"year": 1966, "text": "In Cold Blood 出版（B316）。", "src": "B316"},
    {"year": 1984, "text": "8月25日卒于洛杉矶（B316：died August 25, 1984, Los Angeles）。", "src": "B316"}],
  "major_works": [
    {"work_id": "lengxue", "note": "非虚构小说（B316：1966）"},
    {"title": "蒂凡尼的早餐", "note": "（B316：Breakfast at Tiffany's (1958)）"},
    {"title": "别的声音，别的房间", "note": "（B316：Other Voices, Other Rooms (1948)）"}],
  "style": [
    "'nonfiction novel'（非虚构小说）（B316）。",
    "华丽文体（通说待核）。",
    "南方哥特元素（通说待核）。"],
  "status": "Britannica 定位卡波特为'非虚构小说'开创者之一（B316）。",
  "sources": ["B316"], "dates_source": "B316",
  "pending": ["《冷血》1966年出版（Random House说）核对。","《蒂凡尼的早餐》1958年说核对。","'nonfiction novel'术语的更早源头（如 Capote 自称）待核。"]
},
"ellison": {
  "id": "ellison", "name": "拉尔夫·艾里森", "foreign_name": "Ralph Ellison（拉尔夫·艾里森，1914-03-01—1994-04-16）",
  "country": "美国", "birth": 1914, "death": 1994, "birth_year": 1914, "death_year": 1994, "era": "现当代",
  "summary": "艾里森，俄克拉何马城生，美国小说家——Invisible Man (1952)——'the story of an unnamed Black man'（无名黑人的故事——B317），1953年获 National Book Award（B317）。散文集 Shadow and Act (1964)（B317）；'shadow and act'——其文学的两组关键词（B317 语境）。",
  "timeline": [
    {"year": 1914, "text": "3月1日生于俄克拉何马城（B317：Born March 1, 1914, Oklahoma City）。", "src": "B317"},
    {"year": 1952, "text": "《看不见的人》出版（B317：Invisible Man (1952)）。", "src": "B317"},
    {"year": 1953, "text": "获 National Book Award（B317）。", "src": "B317"},
    {"year": 1994, "text": "4月16日卒（B317：died April 16, 1994）。", "src": "B317"}],
  "major_works": [
    {"work_id": "kanbujian3", "note": "长篇（B317：1952）"},
    {"title": "影子与行动", "note": "（B317：Shadow and Act (1964)）"},
    {"title": "走向领地", "note": "（通说待核）"}],
  "style": [
    "'看不见的人'：无名黑人的第一人称（B317）。",
    "爵士乐与蓝调的叙事（通说待核）。",
    "'shadow and act'（B317）。"],
  "status": "Britannica 定位艾里森为《看不见的人》作者、National Book Award 得主（B317）。",
  "sources": ["B317"], "dates_source": "B317",
  "pending": ["《看不见的人》1952年出版（Random House说）核对。","1953年 National Book Award（B317 已载）核对。","《六月庆典》（Juneteenth，身后1999）待核。"]
},
"ouwen": {
  "id": "ouwen", "name": "华盛顿·欧文", "foreign_name": "Washington Irving（华盛顿·欧文，1783-04-03—1859-11-28）",
  "country": "美国", "birth": 1783, "death": 1859, "birth_year": 1783, "death_year": 1859, "era": "近代",
  "summary": "欧文，纽约人，美国作家——'first American author to achieve international fame'（首位获得国际声誉的美国作家——B318）。The Sketch Book (1819–20)——含'Rip Van Winkle'与'The Legend of Sleepy Hollow'（B318）；《纽约外史》（A History of New York, 1809，署名 Diedrich Knickerbocker——B318）。",
  "timeline": [
    {"year": 1783, "text": "4月3日生于纽约（B318：Born April 3, 1783, New York）。", "src": "B318"},
    {"year": 1809, "text": "《纽约外史》出版（B318：A History of New York (1809)）。", "src": "B318"},
    {"year": 1819, "text": "The Sketch Book 出版（1819–20）（B318）。", "src": "B318"},
    {"year": 1859, "text": "12月28日卒（B318：died December 28, 1859）。", "src": "B318"}],
  "major_works": [
    {"work_id": "jianWenzhaji", "note": "散文随笔集（B318：The Sketch Book (1819–20)）"},
    {"title": "纽约外史", "note": "（B318：1809）"},
    {"title": "阿尔罕伯拉", "note": "（通说待核）"}],
  "style": [
    "'首位获得国际声誉的美国作家'（B318）。",
    "'瑞普·凡·温克尔'与'睡谷传说'（B318）。",
    "幽默与怀旧的'克尼科博克'笔调（通说待核）。"],
  "status": "Britannica 定位欧文为美国作家、'first American author to achieve international fame'（B318）。",
  "sources": ["B318"], "dates_source": "B318",
  "pending": ["《瑞普·凡·温克尔》1819年首发核对。","The Sketch Book 32篇篇目待核。","'Diedrich Knickerbocker'笔名核对。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

works = {
"xinshigudeLieshou": {
  "id":"xinshigudeLieshou","title":"心是孤独的猎手","original_title":"The Heart Is a Lonely Hunter","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mccalles","author_name":"卡森·麦卡勒斯",
  "year_display":"1940年（作者页 B315 口径：The Heart Is a Lonely Hunter (1940)）","year_sort":1940,
  "background":["作者页（B315）：'her novels……explore the spiritual isolation of misfits and outcast characters in the small towns of the South'——本作为其成名作（B315 作者页定位）。","题材（通说待核）：聋哑人辛格与四位'倾诉者'——南方小镇的精神孤独。"],
  "outline":["哑巴辛格成为小镇精神中心——四位倾诉者的孤独（通说待核）。","辛格自杀——孤独的崩塌（通说待核）。"],
  "characters":[{"name":"辛格","identity":"聋哑人","note":"倾诉的中心（通说待核）"},{"name":"比夫","identity":"咖啡馆主","note":"（通说待核）"},{"name":"米克","identity":"少女","note":"（通说待核）"},{"name":"杰克·布朗特","identity":"流浪者","note":"（通说待核）"}],
  "themes":["'孤独的猎手'：倾诉与误解（书名通说待核）。",
   "南方小镇的'格格不入'（B315：misfits and outcast characters）。",
   "种族与阶级（通说待核）。"],
  "influence":[{"text":"作者页：麦卡勒斯成名作（B315 作者页口径）。","source":"B315"},
   {"text":"作者页：'spiritual isolation'主题（B315 作者级定位）。","source":"B315"}],
  "reading":{"difficulties":["多人物视角。","'孤独'主题的密度。"],
   "editions":["《心是孤独的猎手》（人民文学出版社/上海三联版本，通说待核）。","英文原版。"],
   "order":"麦卡勒斯首选。"},
  "pending":["1940年出版（Houghton Mifflin说）核对。","辛格（John Singer）/比夫/米克/布朗特人名核对。","1968年电影改编待核。"],
  "sources":["B315"],"year_source":"B315","author_source":"B315","related_works":["嘉莉妹妹","嘉莉妹妹"] ,
  "svg":G2("《心是孤独的猎手》倾诉结构图",[{"title":"辛格","text":"聋哑的中心（通说）","color":"main"},{"title":"四位倾诉者","text":"比夫/米克/布朗特/考普兰（通说）","color":"family"},{"title":"孤独","text":"'猎手'即'被猎'（通说）","color":"gold"},{"title":"南方小镇","text":"1930年代（通说）","color":"plain"}])
},
"lengxue": {
  "id":"lengxue","title":"冷血","original_title":"In Cold Blood","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"非虚构小说","genre_group":"小说","language":"英语","author_id":"capote","author_name":"杜鲁门·卡波特",
  "year_display":"1966年（作者页 B316 口径：In Cold Blood (1966)）","year_sort":1966,
  "background":["作者页（B316）：'nonfiction novel'（非虚构小说）的先驱之一，In Cold Blood (1966) 写堪萨斯克拉特一家四口被杀案（B316 作者页定位）。","作者（B316）：Other Voices, Other Rooms (1948) 处女作；《蒂凡尼的早餐》(1958)（B316）。"],
  "outline":["1959年堪萨斯霍尔科姆家四口被杀案——凶手佩里与迪克（通说待核）。","'非虚构小说'：六年调查与行刑（通说待核）。"],
  "characters":[{"name":"佩里·史密斯","identity":"凶手","note":"（通说待核）"},{"name":"迪克·希科克","identity":"凶手","note":"（通说待核）"}],
  "themes":["'非虚构小说'的诞生（B316：nonfiction novel）。",
   "犯罪与叙事（通说待核）。",
   "美国中西部（通说待核）。"],
  "influence":[{"text":"作者页：'nonfiction novel'开创者之一（B316 作者页口径）。","source":"B316"},
   {"text":"作者页：卡波特1966年 In Cold Blood（B316 作者级定位）。","source":"B316"}],
  "reading":{"difficulties":["非虚构与虚构的边界。","真实犯罪语境。"],
   "editions":["《冷血》（人民文学出版社/南海出版公司版本，通说待核）。","英文原版。"],
   "order":"非虚构小说首选。"},
  "pending":["1966年出版（Random House说）核对。","佩里·史密斯/迪克·希科克/霍尔科姆家人名核对。","'nonfiction novel'术语首用者争议待核。"],
  "sources":["B316"],"year_source":"B316","author_source":"B316","related_works":["嘉莉妹妹","meiguoren","冷血" ] ,
  "svg":G2("《冷血》非虚构结构图",[{"title":"凶案","text":"霍尔科姆家（通说）","color":"antagonist"},{"title":"六年调查","text":"非虚构小说（B316）","color":"main"},{"title":"佩里","text":"凶手的内心","color":"gold"},{"title":"行刑","text":"1965年的绞架（通说）","color":"family"}])
},
"kanbujian3": {
  "id":"kanbujian3","title":"看不见的人","original_title":"Invisible Man","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"ellison","author_name":"拉尔夫·艾里森",
  "year_display":"1952年（作者页 B317 口径：Invisible Man (1952)）","year_sort":1952,
  "background":["作者页（B317）：'the story of an unnamed Black man'——无名黑人的故事（B317 作者页定位）；1953年获 National Book Award（B317）。","作者（B317）：'shadow and act'——散文集 Shadow and Act (1964)（B317）。","地位（通说待核）：美国黑人文学的里程碑。"],
  "outline":["无名黑人的地下独白：从南方到哈莱姆——'看不见'的一生（通说待核）。","'兄弟会'与' unpunished'（通说待核）。"],
  "characters":[{"name":"无名叙述者","identity":"黑人青年","note":"（通说待核）"},{"name":"拉斯?","identity":"'狂人'","note":"（通说待核）"}],
  "themes":["'看不见'：种族的匿名（通说待核）。",
   "身份的地下化（通说待核）。",
   "爵士与蓝调结构（通说待核）。"],
  "influence":[{"text":"作者页：'the story of an unnamed Black man'（B317 作者页口径）。","source":"B317"},
   {"text":"作者页：1953年 National Book Award（B317 作者级定位）。","source":"B317"}],
  "reading":{"difficulties":["'看不见'的多义。","哈莱姆背景。"],
   "editions":["《看不见的人》（人民文学出版社/上海译文版本，通说待核）。","英文原版。"],
   "order":"美国黑人文学首选之一。"},
  "pending":["1952年出版（Random House说）核对。","兄弟会/莱因哈特等情节核对。","1953年 National Book Award（B317 已载）核对。"],
  "sources":["B317"],"year_source":"B317","author_source":"B317","related_works":["chonger","zise","mangcike"],
  "svg":G2("《看不见的人》地下结构图",[{"title":"地下","text":"1369盏灯泡（通说）","color":"main"},{"title":"看不见","text":"种族的匿名（B317）","color":"antagonist"},{"title":"兄弟会","text":"组织的幻影","color":"family"},{"title":"看不见的人","text":"书名即主题","color":"gold"}])
},
"jianWenzhaji": {
  "id":"jianWenzhaji","title":"见闻札记","original_title":"The Sketch Book of Geoffrey Crayon, Gent.","region":"美国","era":"近代","era_detail":"19世纪初",
  "genre":"散文随笔集","genre_group":"散文","language":"英语","author_id":"ouwen","author_name":"华盛顿·欧文",
  "year_display":"1819—1820年（作者页 B318 口径：The Sketch Book (1819–20)）","year_sort":1819,
  "background":["作者页（B318）：欧文'first American author to achieve international fame'（首位获得国际声誉的美国作家——B318）；The Sketch Book (1819–20)——含'Rip Van Winkle'与'The Legend of Sleepy Hollow'（B318）。","《纽约外史》（A History of New York, 1809，署名 Diedrich Knickerbocker——B318）。"],
  "outline":["'瑞普·凡·温克尔'：山中一觉二十年（通说待核）。","'睡谷传说'：无头骑士（通说待核）。","英国随笔（通说待核）。"],
  "characters":[{"name":"瑞普·凡·温克尔","identity":"懒汉","note":"（通说待核）"},{"name":"伊卡博德·克莱恩","identity":"教师","note":"（通说待核）"}],
  "themes":["美国'神话'的发明（通说待核）。",
   "新旧大陆的对照（通说待核）。",
   "'克尼科博克'幽默（通说待核）。"],
  "influence":[{"text":"Britannica：'first American author to achieve international fame'（B318）。","source":"B318"},
   {"text":"Britannica：The Sketch Book 含'瑞普'与'睡谷'（B318）。","source":"B318"}],
  "reading":{"difficulties":["荷马式……不：荷兰移民文化背景。","'幽默'的古典笔调。"],
   "editions":["《见闻札记》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"美国文学起点之一。"},
  "pending":["1819—20连载（John Murray说）核对。","瑞普/伊卡博德人名核对。","'睡谷'地名（Sleepy Hollow）待核。"],
  "sources":["B318"],"year_source":"B318","author_source":"B318","related_works":["hakebei","jian","fenwangyu"],
  "svg":G2("《见闻札记》美国神话图",[{"title":"瑞普·凡·温克尔","text":"一觉二十年（通说）","color":"main"},{"title":"睡谷传说","text":"无头骑士","color":"antagonist"},{"title":"伦敦随笔","text":"旧世界的对照","color":"gold"},{"title":"克尼科博克","text":"纽约的笔名（B318）","color":"family"}])
},
"jiMi": {
  "id":"jiMi","title":"吉姆","original_title":"Jim","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"None","author_name":"佚名（通说待核——本书为美国作家佚名作品，暂缺核证）","related_works":["hakebei"],
  "year_display":"待核","year_sort":0,"pending":["本书未核证——占位"], "svg":{"type":"grid","width":680,"height":340,"caption":"占位","cards":[{"title":"占位","text":"占位","color":"plain"}]},"background":["占位"],"outline":["占位"],"characters":[],"themes":["占位"],"influence":[{"text":"占位","source":"B001"}],"reading":{"difficulties":["占位"],"editions":["占位"],"order":"占位"},"sources":["B001"],"year_source":"B001","author_source":"B001"}
}

for wid, d in works.items():
    if wid == "jiMi":
        continue
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created (excluding placeholder)")
