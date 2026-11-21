# -*- coding: utf-8 -*-
"""批78：Britannica 新核梅勒 B409×2（裸者与死者/刽子手之歌）"""
import json, pathlib

newsrc = [
{"id":"B409","title":"Norman Mailer — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Norman-Mailer","type":"百科全书","verified":True,"covers":["mailer","luzhezhezhe"],"note":"2026-11-21 核对：1923-01-31新泽西Long Branch生—2007-11-10纽约卒（84岁）；The Naked and the Dead（裸者与死者, 1948）——索邦求学期间写——'hailed immediately as one of the finest American novels to come out of World War II'（立即被誉为二战最佳美国小说之一）——'follows a platoon of 13 American soldiers stationed on the Japanese-held island of Anopopei in the Pacific'；The Executioner's Song (1979)——'Pulitzer Prize-winning novel based on the life of convicted murderer Gary Gilmore'；Advertisements for Myself (1959)——'a collection of unfinished stories, parts of novels, essays, reviews, notebook entries, or ideas for fiction'——出版时'was generally dismissed as a one-book author'；'New Journalism'——'combines the imaginative subjectivity of literature with the more objective qualities of journalism'（新新闻主义：文学的想象主观性+新闻的客观性）；The Armies of the Night (1968)——普利策+全国图书奖；哈佛1943航空工程；1944-46太平洋服役；1969竞选纽约市长未果"},
]
raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in newsrc:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
srcs = json.load(open('sources.json', encoding='utf-8'))
have = {s['id'] for s in srcs}
srcs.extend(s for s in newsrc if s['id'] not in have)
pathlib.Path('sources.json').write_text(json.dumps(srcs, ensure_ascii=False, indent=1), encoding='utf-8')
print('sources:', len(srcs))

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"mailer","name":"诺曼·梅勒","foreign_name":"Norman Mailer（诺曼·梅勒，1923-01-31—2007-11-10）","country":"美国","birth":1923,"death":2007,"birth_year":1923,"death_year":2007,"era":"现当代",
"summary":"梅勒，新泽西Long Branch生，美国作家——'New Journalism'——'combines the imaginative subjectivity of literature with the more objective qualities of journalism'（新新闻主义：文学的想象主观性+新闻的客观性——B409）。The Naked and the Dead（裸者与死者, 1948）——索邦求学期间写——'hailed immediately as one of the finest American novels to come out of World War II'（B409）——'follows a platoon of 13 American soldiers stationed on the Japanese-held island of Anopopei in the Pacific'（B409）。The Executioner's Song (1979)——'Pulitzer Prize-winning novel based on the life of convicted murderer Gary Gilmore'（B409）。The Armies of the Night (1968)——普利策+全国图书奖（B409）。",
"timeline":[
 {"year":1923,"text":"1月31日生于新泽西Long Branch（B409）。","src":"B409"},
 {"year":1948,"text":"《裸者与死者》——'二战最佳美国小说之一'（B409）。","src":"B409"},
 {"year":1968,"text":"The Armies of the Night——普利策+全国图书奖（B409）。","src":"B409"},
 {"year":1979,"text":"《刽子手之歌》——普利策奖（B409）。","src":"B409"},
 {"year":2007,"text":"11月10日卒于纽约（B409）。","src":"B409"}],
"major_works":[
 {"work_id":"luzhezhezhe","note":"1948（B409）"},
 {"work_id":"guizishouzhige","note":"1979普利策奖（B409）"},
 {"title":"夜幕下的大军","note":"（B409：The Armies of the Night (1968)——中译名待核）"}],
"style":["'新新闻主义'（B409：New Journalism——'imaginative subjectivity of literature...objective qualities of journalism'）。",
 "二战太平洋战场的群体肖像（B409：a platoon of 13 American soldiers）。",
 "'真人真事'的非虚构小说（B409：Gary Gilmore）。"],
"status":"Britannica 定位梅勒为'新新闻主义'代表、两获普利策奖（B409）。",
"sources":["B409"],"dates_source":"B409",
"pending":["《裸者与死者》通行译名（《裸者与死者》）待核。","Anopopei 岛（虚构）核对。","1969年纽约市长竞选（B409已载）细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"luzhezhezhe","title":"裸者与死者","original_title":"The Naked and the Dead","region":"美国","era":"现当代","era_detail":"20世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mailer","author_name":"诺曼·梅勒",
"year_display":"1948年（Britannica B409：The Naked and the Dead (1948)——'hailed immediately as one of the finest American novels to come out of World War II'）","year_sort":1948,
"background":["Britannica（B409）：'hailed immediately as one of the finest American novels to come out of World War II'（立即被誉为二战最佳美国小说之一）——索邦求学期间写。","Britannica（B409）：'follows a platoon of 13 American soldiers stationed on the Japanese-held island of Anopopei in the Pacific'（太平洋日占虚构岛 Anopopei 上的13人排）。","Britannica（B409）：梅勒——哈佛1943航空工程、1944-46太平洋服役。"],
"outline":["（通说待核——B409未载剧情）安诺波佩岛登陆战：卡明斯将军与赫恩中尉的权力角斗。","（通说待核）'箱子'式的排级群像与飞行员的'时间机器'插入。"],
"characters":[{"name":"卡明斯将军","identity":"师指挥官","note":"（通说待核，B409未载）"},{"name":"赫恩","identity":"中尉","note":"（通说待核）"}],
"themes":["'二战最佳美国小说之一'（B409）。",
 "军阶与权力的政治（通说待核）。",
 "13人排的群像（B409：a platoon of 13 American soldiers）。"],
"influence":[{"text":"Britannica：'hailed immediately as one of the finest American novels to come out of World War II'（B409）。","source":"B409"},{"text":"Britannica：梅勒'新新闻主义'（B409 交叉）。","source":"B409"}],
"reading":{"difficulties":["群像的插章结构（'时间机器'——通说待核）。","太平洋战场史。"],
 "editions":["《裸者与死者》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"梅勒首作；与《刽子手之歌》对读。"},
"pending":["卡明斯/赫恩人名核对（通说）。","1948年出版（Holt说）待核。","'时间机器'插章细节待核。"],
"sources":["B409"],"year_source":"B409","author_source":"B409","related_works":["sangeshibing","wuhhaotuchang","sanzimei"],
"svg":G("《裸者与死者》群像结构图",[{"title":"13人排","text":"太平洋的岛屿（B409）","color":"main"},{"title":"权力","text":"将军与中尉（通说）","color":"antagonist"},{"title":"裸者","text":"战争剥夺的一切（书名）","color":"gold"},{"title":"死者","text":"群岛的代价（通说）","color":"family"}])},
{"id":"guizishouzhige","title":"刽子手之歌","original_title":"The Executioner's Song","region":"美国","era":"现当代","era_detail":"20世纪70年代末",
"genre":"非虚构小说","genre_group":"小说","language":"英语","author_id":"mailer","author_name":"诺曼·梅勒",
"year_display":"1979年（Britannica B409：The Executioner's Song (1979)——'Pulitzer Prize-winning novel based on the life of convicted murderer Gary Gilmore'）","year_sort":1979,
"background":["Britannica（B409）：'Pulitzer Prize-winning novel based on the life of convicted murderer Gary Gilmore'（基于杀人犯加里·吉尔摩生平的普利策奖小说）。","Britannica（B409）：'New Journalism'——'combines the imaginative subjectivity of literature with the more objective qualities of journalism'。","题材（通说待核）：吉尔摩要求的死刑执行——'行刑者之歌'的西部叙事。"],
"outline":["（通说待核）吉尔摩出狱、杀人、自请死刑——'西部的声音'。","（通说待核）执行前夜的媒体与宗教。"],
"characters":[{"name":"加里·吉尔摩","identity":"死刑犯","note":"（B409：convicted murderer Gary Gilmore）"},{"name":"妮可","identity":"恋人","note":"（通说待核）"}],
"themes":["'行刑者之歌'：死刑的仪式（书名语境——通说待核）。",
 "'新新闻主义'的实录（B409）。",
 "西部与暴力的神话（通说待核）。"],
"influence":[{"text":"Britannica：'Pulitzer Prize-winning'（B409）。","source":"B409"},{"text":"Britannica：'New Journalism'（B409 作者级）。","source":"B409"}],
"reading":{"difficulties":["'非虚构小说'的实录性。","1976-77年犹他州死刑案（通说待核）。"],
 "editions":["《刽子手之歌》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"梅勒非虚构篇；与《裸者与死者》对读。"},
"pending":["吉尔摩案细节核对（1976年杀人/1977年1月行刑说——通说）。","1979年出版（Little, Brown说）待核。","'西部之声'结构待核。"],
"sources":["B409"],"year_source":"B409","author_source":"B409","related_works":["luzhezhezhe","katarinabulum","wuhhaotuchang"],
"svg":G("《刽子手之歌》行刑结构图",[{"title":"吉尔摩","text":"自请死刑（B409语境）","color":"main"},{"title":"行刑者","text":"'之歌'的仪式（书名）","color":"gold"},{"title":"新新闻","text":"实录的文学（B409）","color":"family"},{"title":"西部","text":"暴力的神话（通说）","color":"antagonist"}])},
]
created = []
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    created.append(w['id'])
    print('work', w['id'])

def link(aid, wid):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B409 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('luzhezhezhe','mailer'), ('guizishouzhige','mailer')]:
    if wid in created:
        link(aid, wid)
print('BATCH78 DONE')
