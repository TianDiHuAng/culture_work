# -*- coding: utf-8 -*-
"""流水线批20：Britannica 新核 4 作家 4 部 + 零成本直写 4 部"""
import json, pathlib

new_src = [
{"id":"B315","title":"Eugene ONeill — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Eugene-ONeill","type":"百科全书","verified":True,"covers":["ONeill","manchangdeheian"],"note":"2026-11-21 核对：1888-10-16纽约生—1953-11-27波士顿卒（65岁）；1936诺奖；四项普利策戏剧奖（Beyond the Horizon/Anna Christie/Strange Interlude/Long Day's Journey into Night）；'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'；The Iceman Cometh (1946)——'Considered by many to be ONeill's finest work'（页面问答）"},
{"id":"B316","title":"Graham Greene — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Graham-Greene","type":"百科全书","verified":True,"covers":["greene","lianqingdezhongjie"],"note":"2026-11-21 核对：1904-10-02 Berkhamsted生—1991-04-03瑞士沃韦卒（86岁）；'one of the most widely read British novelists of the 20th century'；'Many of his best-known works, including The Power and the Glory (1940) and The End of the Affair (1951), center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'；End of the Affair——'narrated by an agnostic in love with a woman who forsakes him because of a religious conviction'（电影1955/1999）"},
{"id":"B317","title":"Richard Wright — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Richard-Wright","type":"百科全书","verified":True,"covers":["wright","tuyuzhizideneizi"],"note":"2026-11-21 核对：1908-09-04密西西比州Adams County种植园生—1960-11-28巴黎卒；Native Son (1940)——'a disturbing and brutally honest novel'；Black Boy (1945)——自传；'the first African American writer to gain a large white readership'"},
{"id":"B317","title":"Franz Kafka — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Franz-Kafka","type":"百科全书","verified":True,"covers":["kafka","chengbao"],"note":"2026-11-21 核对：1883-07-03布拉格生—1924-06-03 Kierling疗养院卒（40岁）；'a German-language writer of visionary fiction'；The Trial (1925)——'posthumously published'；The Castle (1926)——'posthumously published, unfinished'；'Kafkas stories and novels have proved so provocative that they have become nothing less than cultural icons'；Max Brod——'his literary executor'，'disobeyed Kafkas instructions to burn the manuscripts'"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new_src:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

authors = {
"wright": {
  "id": "wright", "name": "理查德·赖特", "foreign_name": "Richard Wright（理查德·赖特，1908-09-04—1960-11-28）",
  "country": "美国", "birth": 1908, "death": 1960, "birth_year": 1908, "death_year": 1960, "era": "现当代",
  "summary": "赖特，密西西比州种植园生，美国黑人作家——'the first African American writer to gain a large white readership'（首位获得大量白人读者的非裔美国作家——B317）；Native Son (1940)——'a disturbing and brutally honest novel'；Black Boy (1945)——自传（B317）。",
  "timeline": [
    {"year": 1908, "text": "9月4日生于密西西比州（B317：Born September 4, 1908, Mississippi种植园）。", "src": "B317"},
    {"year": 1940, "text": "Native Son 出版（B317：1940）。", "src": "B317"},
    {"year": 1960, "text": "11月28日卒于巴黎（B317：died November 28, 1960, Paris）。", "src": "B317"}],
  "major_works": [
    {"work_id": "tuyuzhizideneizi", "note": "长篇（B317：Native Son 1940）"},
    {"title": "黑孩子", "note": "（B317：Black Boy (1945)——自传）"}],
  "style": [
    "'disturbing and brutally honest'（B317）。",
    "种族主义的暴力书写（通说待核）。",
    "自然主义与存在主义（通说待核）。"],
  "status": "Britannica 定位赖特为'首位获得大量白人读者的非裔美国作家'（B317）。",
  "sources": ["B317"], "dates_source": "B317",
  "pending": ["Native Son 1940年出版（Harper & Brothers说）核对。","Bigger Thomas人名核对。","'土生子'中译名待核。"]
},
"stevenson": {
  "id": "stevenson", "name": "罗伯特·路易斯·史蒂文森", "foreign_name": "Robert Louis Stevenson（罗伯特·路易斯·史蒂文森，1850-11-13—1894-12-03）",
  "country": "英国", "birth": 1850, "death": 1894, "birth_year": 1850, "death_year": 1894, "era": "近代",
  "summary": "史蒂文森，爱丁堡人，苏格兰散文家、诗人与小说、游记作家——'a writer of originality and power who produced brilliant adventure stories with subtle moral overtones'（B294）。'best known for his novels Treasure Island (1881), Kidnapped (1886)'（B294 Quick Facts——金银岛通行1883年说待核）。放弃法律改从文学，晚年居萨摩亚（B294）。",
  "timeline": [
    {"year": 1850, "text": "11月13日生于爱丁堡（B294）。", "src": "B294"},
    {"year": 1875, "text": "获苏格兰律师资格（B294）。", "src": "B294"},
    {"year": 1894, "text": "12月3日卒于萨摩亚（B294）。", "src": "B294"}],
  "major_works": [
    {"work_id": "huashenboshi", "note": "中篇（1886年说——通说待核）"},
    {"title": "金银岛", "note": "（B294 Quick Facts 载 1881——通行1883说待核）"},
    {"title": "绑架", "note": "（B294：Kidnapped (1886)）"}],
  "style": [
    "'原创与力量'的冒险故事、'微妙的道德意味'（B294）。",
    "善恶双重人格的心理分化（《化身博士》——通说待核）。",
    "游记与冒险的交织（B294 语境）。"],
  "status": "Britannica 定位史蒂文森为苏格兰散文家、诗人与小说/游记作家（B294）。",
  "sources": ["B294"], "dates_source": "B294",
  "pending": ["《化身博士》1886年出版细节核对。","《金银岛》1883年（书刊年份）与 Britannica 页 1881 说核对。","萨摩亚晚年待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"tuyuzhizideneizi": {
  "id":"tuyuzhizideneizi","title":"土生子","original_title":"Native Son","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"wright","author_name":"理查德·赖特",
  "year_display":"1940年（作者页 B317 口径：Native Son 1940）","year_sort":1940,
  "background":["作者页（B317）：'the first African American writer to gain a large white readership'——本作为其成名作。","题材（通说待核）：芝加哥黑人青年比格·托马斯的犯罪与审判——种族主义的暴力循环。"],
  "outline":["误杀→藏尸→逃亡→审判（通说待核）。"],
  "characters":[{"name":"比格·托马斯","identity":"黑人青年","note":"（通说待核）"}],
  "themes":["种族主义与暴力（通说待核）。",
   "恐惧的循环（通说待核）。",
   "自然主义与社会抗议（通说待核）。"],
  "influence":[{"text":"Britannica：'the first African American writer to gain a large white readership'（B317）。","source":"B317"},
   {"text":"作者页：'disturbing and brutally honest'（B317）。","source":"B317"}],
  "reading":{"difficulties":["种族主义语境。","暴力描写。"],
   "editions":["《土生子》（人民文学出版社/上海译文版本，通说待核）。","英文原版。"],
   "order":"赖特首选。"},
  "pending":["1940年出版（Harper & Brothers说）核对。","比格·托马斯人名核对。","书名'Native Son'中译（土生子/ native son）待核。"],
  "sources":["B317"],"year_source":"B317","author_source":"B317","related_works":["kanbujian3","chonger","zise"],
  "svg":G2("《土生子》暴力结构图",[{"title":"比格·托马斯","text":"黑人的愤怒","color":"main"},{"title":"误杀","text":"恐惧的循环","color":"antagonist"},{"title":"审判","text":"社会的共谋","color":"gold"},{"title":"土生子","text":"书名的隐喻","color":"family"}])
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
