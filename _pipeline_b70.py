# -*- coding: utf-8 -*-
"""批70：Britannica 新核 2 作家 2 部（萨克雷 B393/斯威夫特 B394）"""
import json, pathlib

newsrc = [
{"id":"B393","title":"William Makepeace Thackeray — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/William-Makepeace-Thackeray","type":"百科全书","verified":True,"covers":["thackeray","minglichang"],"note":"2026-11-21 核对：1811-07-18加尔各答生（东印度公司行政官之子）—1863-12-24伦敦卒（52岁）；'an English novelist whose reputation rests chiefly on Vanity Fair'；Vanity Fair 连载1847-48——副题'A Novel Without a Hero'（无英雄的小说）——'satirizes the foolishness and selfishness of people chasing after vanities'；两个对照女性：Amelia Sedley 与'ambitious adventuress'Becky Sharp（'the novel's central character'）——与 Rawdon Crawley 结婚上升；Amelia 嫁 George Osborne（死于滑铁卢）后嫁 Captain William Dobbin；'Thackeray was considered a rival to Dickens'；价值在'narrative skill, subtle characterization, descriptive power'；1832继承£20,000——'He soon lost his fortune, however, through gambling and unlucky speculations and investments.'；The Luck of Barry Lyndon (1844)——首部全长作品；The Book of Snobs (1848)；Henry Esmond (1852)；1860年创办并主编 The Cornhill Magazine；笔名 Fitz-Boodle/Michael Angelo Titmarsh 等"},
{"id":"B394","title":"Jonathan Swift — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jonathan-Swift","type":"百科全书","verified":True,"covers":["swift","geliefu"],"note":"2026-11-21 核对：1667-11-30都柏林生—1745-10-19都柏林卒；'Anglo-Irish author who was the foremost prose satirist in the English language'（英语最伟大的散文讽刺家）；A Tale of a Tub (1704)——匿名散文讽刺；Gulliver's Travels (1726)——'a parody of a travel narrative' mocking English customs and politics（戏仿游记体，讽刺英国习俗与政治）；'A Modest Proposal' (1729)——讽刺短论批判英格兰对爱尔兰的剥削——'suggests living conditions in Ireland could be improved by butchering the children of poor Irish citizens and selling them as food'；Quick Facts 引文——'Satire is a sort of glass, wherein beholders do generally discover everybody's face but their own.'（讽刺是一面镜子，观看者通常从中看见所有人的脸却不见自己）；笔名 Isaac Bickerstaff；Journal to Stella；Bickerstaff 小册子 (1708-09)"},
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
{"id":"thackeray","name":"威廉·梅克比斯·萨克雷","foreign_name":"William Makepeace Thackeray（威廉·梅克比斯·萨克雷，1811-07-18—1863-12-24）","country":"英国","birth":1811,"death":1863,"birth_year":1811,"death_year":1863,"era":"近代",
"summary":"萨克雷，加尔各答生（东印度公司行政官之子），英国小说家——'an English novelist whose reputation rests chiefly on Vanity Fair'（声誉主要建立在《名利场》上——B393）。Vanity Fair（名利场）连载1847-48——副题'A Novel Without a Hero'（无英雄的小说）——'satirizes the foolishness and selfishness of people chasing after vanities'（B393）。两个对照女性：Amelia Sedley 与'ambitious adventuress'Becky Sharp——'the novel's central character'（B393）。'Thackeray was considered a rival to Dickens'（被视为狄更斯的对手——B393）。价值在'narrative skill, subtle characterization, descriptive power'（B393）。",
"timeline":[
 {"year":1811,"text":"7月18日生于加尔各答（B393）。","src":"B393"},
 {"year":1832,"text":"继承£20,000——旋因赌博与投机而失（B393：'He soon lost his fortune...'）。","src":"B393"},
 {"year":1847,"text":"《名利场》连载（1847-48）（B393）。","src":"B393"},
 {"year":1860,"text":"创办并主编 The Cornhill Magazine（B393）。","src":"B393"},
 {"year":1863,"text":"12月24日卒于伦敦（B393）。","src":"B393"}],
"major_works":[
 {"work_id":"minglichang","note":"1847-48连载（B393）"},
 {"title":"巴里·林登的命运","note":"（B393：The Luck of Barry Lyndon (1844)——首部全长作品——中译名待核）"},
 {"title":"势利者集","note":"（B393：The Book of Snobs (1848)——中译名待核）"}],
"style":["'无英雄的小说'（B393：A Novel Without a Hero）。",
 "'追逐虚荣者的愚蠢与自私'的讽刺（B393）。",
 "'叙事技巧、细微的人物刻画、描写力'（B393）。"],
"status":"Britannica 定位萨克雷为《名利场》作者、狄更斯的'对手'（B393）。",
"sources":["B393"],"dates_source":"B393",
"pending":["《名利场》通行译名待核。","Becky Sharp 全名（Rebecca——通说）待核。","与狄更斯'对手'说的出处核对（B393口径）。"]},
{"id":"swift","name":"乔纳森·斯威夫特","foreign_name":"Jonathan Swift（乔纳森·斯威夫特，1667-11-30—1745-10-19）","country":"爱尔兰","birth":1667,"death":1745,"birth_year":1667,"death_year":1745,"era":"近代",
"summary":"斯威夫特，都柏林生，英裔爱尔兰作家——'the foremost prose satirist in the English language'（英语最伟大的散文讽刺家——B394）。A Tale of a Tub（一只桶的故事, 1704）——匿名散文讽刺（B394）；Gulliver's Travels（格列佛游记, 1726）——'a parody of a travel narrative' mocking English customs and politics（B394）；'A Modest Proposal'（一个温和的建议, 1729）——讽刺短论批判英格兰对爱尔兰的剥削——'suggests living conditions in Ireland could be improved by butchering the children of poor Irish citizens and selling them as food'（B394）。引文——'Satire is a sort of glass, wherein beholders do generally discover everybody's face but their own.'（B394 Quick Facts）。",
"timeline":[
 {"year":1667,"text":"11月30日生于都柏林（B394）。","src":"B394"},
 {"year":1704,"text":"A Tale of a Tub——匿名出版（B394）。","src":"B394"},
 {"year":1726,"text":"《格列佛游记》（B394）。","src":"B394"},
 {"year":1729,"text":"'A Modest Proposal'——讽刺短论（B394）。","src":"B394"},
 {"year":1745,"text":"10月19日卒于都柏林（B394）。","src":"B394"}],
"major_works":[
 {"work_id":"geliefu","note":"1726（B394）"},
 {"title":"一只桶的故事","note":"（B394：A Tale of a Tub (1704)——中译名待核）"},
 {"title":"一个温和的建议","note":"（B394：A Modest Proposal (1729)——中译名待核）"}],
"style":["'英语最伟大的散文讽刺家'（B394）。",
 "'戏仿游记体'（B394：a parody of a travel narrative）。",
 "'讽刺是一面镜子'（B394 Quick Facts 引文）。"],
"status":"Britannica 定位斯威夫特为英语最伟大的散文讽刺家（B394）。",
"sources":["B394"],"dates_source":"B394",
"pending":["《格列佛游记》通行译名待核。","四卷（小人国/大人国/飞岛/慧骃国）细节核对（B394未载——通说）。","'Isaac Bickerstaff'笔名细节（B394已载）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"minglichang","title":"名利场","original_title":"Vanity Fair","region":"英国","era":"近代","era_detail":"19世纪40年代",
"genre":"长篇小说（连载）","genre_group":"小说","language":"英语","author_id":"thackeray","author_name":"威廉·梅克比斯·萨克雷",
"year_display":"1847-48年（Britannica B393：Vanity Fair 连载——副题'A Novel Without a Hero'）","year_sort":1847,
"background":["Britannica（B393）：副题'A Novel Without a Hero'（无英雄的小说）——'satirizes the foolishness and selfishness of people chasing after vanities'。","Britannica（B393）：两个对照女性——Amelia Sedley 与'ambitious adventuress'Becky Sharp（'the novel's central character'）；Amelia 嫁 George Osborne（死于滑铁卢）后嫁 Captain William Dobbin。","Britannica（B393）：'Thackeray was considered a rival to Dickens'——价值在'narrative skill, subtle characterization, descriptive power'。"],
"outline":["（通说待核——B393未载全剧情）贝基·夏普的'攀登'与爱米丽亚的温顺。","（通说待核）滑铁卢与'名利场'的散场。"],
"characters":[{"name":"贝基·夏普","identity":"'野心勃勃的冒险女'","note":"（B393：Becky Sharp——'the novel's central character'）"},{"name":"爱米丽亚·塞德利","identity":"对照女性","note":"（B393：Amelia Sedley）"}],
"themes":["'无英雄的小说'（B393：A Novel Without a Hero）。",
 "'追逐虚荣者的愚蠢与自私'（B393）。",
 "滑铁卢时代的英国社会（B393：Napoleonic period in England）。"],
"influence":[{"text":"Britannica：'an English novelist whose reputation rests chiefly on Vanity Fair'（B393）。","source":"B393"},{"text":"Britannica：'considered a rival to Dickens'（B393）。","source":"B393"}],
"reading":{"difficulties":["双女主的对照结构。","摄政时期英国社会。"],
 "editions":["《名利场》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"萨克雷代表作；与《狄更斯》对读。"},
"pending":["贝基/爱米丽亚全名核对（B393载Becky Sharp/Amelia Sedley）。","1847-48连载刊（Punch说）待核。","'无英雄'副题核对（B393已载）。"],
"sources":["B393"],"year_source":"B393","author_source":"B393","related_works":["aimaa","kasiteqiaoshizhang","ouyanigelangtai"],
"svg":G("《名利场》虚荣结构图",[{"title":"名利场","text":"'无英雄'的场（B393）","color":"gold"},{"title":"贝基","text":"野心的攀登（B393）","color":"main"},{"title":"爱米丽亚","text":"温顺的对照（B393）","color":"family"},{"title":"滑铁卢","text":"时代的转折（B393）","color":"antagonist"}])},
{"id":"geliefu","title":"格列佛游记","original_title":"Gulliver's Travels","region":"爱尔兰","era":"近代","era_detail":"18世纪20年代",
"genre":"长篇小说（游记讽刺）","genre_group":"小说","language":"英语","author_id":"swift","author_name":"乔纳森·斯威夫特",
"year_display":"1726年（Britannica B394：Gulliver's Travels (1726)——'a parody of a travel narrative' mocking English customs and politics）","year_sort":1726,
"background":["Britannica（B394）：'a parody of a travel narrative'——戏仿游记体，讽刺英国习俗与政治。","Britannica（B394）：斯威夫特——'the foremost prose satirist in the English language'。","Britannica（B394）Quick Facts 引文：'Satire is a sort of glass, wherein beholders do generally discover everybody's face but their own.'（讽刺是一面镜子……）。"],
"outline":["（通说待核——B394未载四卷细节）小人国/大人国/飞岛/慧骃国的四段旅程。","（通说待核）'慧骃'（理性马）与'耶胡'（野胡）的对照。"],
"characters":[{"name":"格列佛","identity":"外科医生/航海者","note":"（B394 书名人物）"},{"name":"慧骃（Houyhnhnms）","identity":"理性的马","note":"（通说待核）"}],
"themes":["'戏仿游记体'（B394）。",
 "讽刺英国习俗与政治（B394：mocking English customs and politics）。",
 "'讽刺是一面镜子'（B394 引文）。"],
"influence":[{"text":"Britannica：'the foremost prose satirist in the English language'（B394 作者级）。","source":"B394"},{"text":"Britannica：'a parody of a travel narrative'（B394）。","source":"B394"}],
"reading":{"difficulties":["四卷的讽喻层次。","'耶胡'的人性讽刺（通说待核）。"],
 "editions":["《格列佛游记》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"斯威夫特首选；与《一只桶的故事》对读。"},
"pending":["四卷细节核对（通说——B394未载）。","1726年出版（Motte说）待核。","'慧骃国'细节待核。"],
"sources":["B394"],"year_source":"B394","author_source":"B394","related_works":["qiedao","biande" if "biande" in existing else "leiyu","shiqishoushi"],
"svg":G("《格列佛游记》四国讽刺图",[{"title":"游记体","text":"戏仿的框架（B394）","color":"gold"},{"title":"四国","text":"小人/大人/飞岛/慧骃（通说）","color":"main"},{"title":"镜子","text":"'讽刺的镜'（B394引文）","color":"antagonist"},{"title":"英国","text":"被讽刺的对象（B394）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B39x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('minglichang','thackeray'), ('geliefu','swift')]:
    if wid in created:
        link(aid, wid)
print('BATCH70 DONE')
