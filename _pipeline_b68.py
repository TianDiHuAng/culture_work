# -*- coding: utf-8 -*-
"""批68：Britannica 新核 2 作家 3 部（莱辛 B389 金色笔记/冯内古特 B390 五号屠场+猫的摇篮）"""
import json, pathlib

newsrc = [
{"id":"B389","title":"Doris Lessing — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Doris-Lessing","type":"百科全书","verified":True,"covers":["lessing","jinsanbiji"],"note":"2026-11-21 核对：原名 Doris May Tayler；1919-10-22波斯Kermānshāh生（今伊朗）—2013-11-17伦敦卒（94岁）；2007诺贝尔文学奖；The Golden Notebook（金色笔记, 1962）——'a woman writer attempts to come to terms with the life of her times through her art'——'one of the most complex and the most widely read of her novels'；The Grass Is Singing (1950)——白人农夫/妻/非洲仆人（罗德西亚）；Children of Violence 五部曲 (1952-69)——Martha Quest；The Memoirs of a Survivor (1975)——'prophetic fantasy that explores psychological and social breakdown'；Canopus in Argos: Archives 五部科幻 (1979-83)；The Good Terrorist (1985)；The Fifth Child (1988)恐怖故事；Time Bites (2004)随笔——'from women's issues and politics to Sufism'；'In her early adult years she was an active communist'；主题——'people involved in the social and political upheavals of the 20th century'；自传 Under My Skin (1994)/Walking in the Shade (1997)"},
{"id":"B390","title":"Kurt Vonnegut — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Kurt-Vonnegut","type":"百科全书","verified":True,"covers":["vonnegut","wuhhaotuchang"],"note":"2026-11-21 核对：1922-11-11印第安纳波利斯生—2007-04-11纽约卒（84岁）；二战被德军俘——1945年2月德累斯顿大轰炸幸存（屠宰场Schlachthof Fünf）；Slaughterhouse-Five（五号屠场, 1969，电影1972）——副题 The Children's Crusade——'Explicitly draw[s] on his Dresden experience, Vonnegut crafted an absurdist nonlinear narrative in which the bombing raid serves as a symbol of the cruelty and destructiveness of war through the centuries'——获 National Book Award for fiction（页面口径）——评论界'a modern-day classic'；Billy Pilgrim（页面问答口径：突出部战役被俘、德累斯顿幸存、被特拉法马多星人掳走、最终被枪杀）；Cat's Cradle（猫的摇篮, 1963）——加勒比岛民'practice a religion consisting of harmless trivialities'+物质'eventually destroys all life on Earth'——以此作为论文获芝加哥大学人类学硕士(1963)；'use of black humor and postmodern techniques'——'morbid elements with comical ones'——'fatalistic worldview'但怀抱人文主义信念；Player Piano (1952)首作；Kilgore Trout——作者化身，首现于 God Bless You, Mr. Rosewater (1965)；1984年自杀未遂；1973美国艺术与科学院"},
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
{"id":"lessing","name":"多丽丝·莱辛","foreign_name":"Doris Lessing（多丽丝·莱辛，原名 Doris May Tayler，1919-10-22—2013-11-17）","country":"英国","birth":1919,"death":2013,"birth_year":1919,"death_year":2013,"era":"现当代",
"summary":"莱辛，波斯Kermānshāh生（今伊朗），英国作家——2007年诺贝尔文学奖（B389）。The Golden Notebook（金色笔记, 1962）——'a woman writer attempts to come to terms with the life of her times through her art'——'one of the most complex and the most widely read of her novels'（B389）。The Grass Is Singing (1950)——白人农夫、妻子与非洲仆人（罗德西亚）（B389）；Children of Violence 五部曲 (1952-69)（B389）。'In her early adult years she was an active communist'（B389）；Time Bites (2004)——'from women's issues and politics to Sufism'（B389）。",
"timeline":[
 {"year":1919,"text":"10月22日生于波斯Kermānshāh（B389）。","src":"B389"},
 {"year":1950,"text":"The Grass Is Singing——首作（B389）。","src":"B389"},
 {"year":1962,"text":"《金色笔记》（B389）。","src":"B389"},
 {"year":2007,"text":"获诺贝尔文学奖（B389）。","src":"B389"},
 {"year":2013,"text":"11月17日卒于伦敦（B389）。","src":"B389"}],
"major_works":[
 {"work_id":"jinsanbiji","note":"1962（B389）"},
 {"title":"野草在歌唱","note":"（B389：The Grass Is Singing (1950)——中译名待核）"},
 {"title":"暴力的孩子们","note":"（B389：Children of Violence (1952-69)五部曲）"}],
"style":["'20世纪社会政治动荡中人'的书写（B389：social and political upheavals）。",
 "女性主义与苏菲派的并置（B389：Time Bites）。",
 "四笔记的'裂缝'结构（书名语境——通说待核）。"],
"status":"Britannica 定位莱辛为2007诺奖得主、《金色笔记》为其最复杂最广读者（B389）。",
"sources":["B389"],"dates_source":"B389",
"pending":["《金色笔记》通行译名待核。","四笔记（黑红黄蓝）结构细节待核（通说）。","'积极共产主义者'年段（B389）细节待核。"]},
{"id":"vonnegut","name":"库尔特·冯内古特","foreign_name":"Kurt Vonnegut（库尔特·冯内古特，1922-11-11—2007-04-11）","country":"美国","birth":1922,"death":2007,"birth_year":1922,"death_year":2007,"era":"现当代",
"summary":"冯内古特，印第安纳波利斯生，美国作家——二战被德军俘、1945年2月德累斯顿大轰炸幸存（B390）。Slaughterhouse-Five（五号屠场, 1969，电影1972）——副题《儿童十字军》——'Explicitly draw[s] on his Dresden experience, Vonnegut crafted an absurdist nonlinear narrative in which the bombing raid serves as a symbol of the cruelty and destructiveness of war through the centuries'（B390）——获 National Book Award for fiction（页面口径）——'a modern-day classic'（B390）。Cat's Cradle（猫的摇篮, 1963）——以此论文获芝加哥大学人类学硕士（1963）（B390）。'use of black humor and postmodern techniques'——'morbid elements with comical ones'——'fatalistic worldview'但怀抱人文主义信念（B390）。",
"timeline":[
 {"year":1922,"text":"11月11日生于印第安纳波利斯（B390）。","src":"B390"},
 {"year":1945,"text":"2月德累斯顿大轰炸幸存（战俘——B390）。","src":"B390"},
 {"year":1963,"text":"Cat's Cradle——获人类学硕士学位的论文（B390）。","src":"B390"},
 {"year":1969,"text":"《五号屠场》—— National Book Award for fiction（页面口径）——'a modern-day classic'（B390）。","src":"B390"},
 {"year":2007,"text":"4月11日卒于纽约（B390）。","src":"B390"}],
"major_works":[
 {"work_id":"wuhhaotuchang","note":"1969（B390）"},
 {"work_id":"maodeyaolan","note":"1963（B390）"},
 {"title":"自动钢琴", "note":"（B390：Player Piano (1952)——首作——中译名待核）"}],
"style":["'黑色幽默与后现代技巧'（B390：black humor and postmodern techniques）。",
 "'病态与滑稽并置'（B390：morbid elements with comical ones）。",
 "'宿命论世界观'中的人文主义信念（B390：fatalistic worldview...humanist beliefs）。"],
"status":"Britannica 定位冯内古特为黑色幽默代表、《五号屠场》为其'现代经典'（B390）。",
"sources":["B390"],"dates_source":"B390",
"pending":["《五号屠场》通行译名（《第五号屠场》）待核。","'National Book Award'口径核对（页面口径——通行说法为最佳畅销榜）。","'So it goes'短语——B390 页未载（不采为引文）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"jinsanbiji","title":"金色笔记","original_title":"The Golden Notebook","region":"英国","era":"现当代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"lessing","author_name":"多丽丝·莱辛",
"year_display":"1962年（Britannica B389：The Golden Notebook (1962)——'one of the most complex and the most widely read of her novels'）","year_sort":1962,
"background":["Britannica（B389）：'a woman writer attempts to come to terms with the life of her times through her art'（一位女作家试图通过艺术与她时代的生活和解）。","Britannica（B389）：'one of the most complex and the most widely read of her novels'。","题材（通说待核）：作家安娜的四本笔记（黑红黄蓝）与'金色笔记'的合流。"],
"outline":["（通说待核）四笔记：写作/政治/爱情/心理的分裂与整合。","（通说待核）'自由女性'的框架短篇。"],
"characters":[{"name":"安娜·伍尔夫","identity":"作家","note":"（通说待核，B389未载）"},{"name":"莫莉","identity":"朋友","note":"（通说待核）"}],
"themes":["'与她时代的生活和解'（B389）。",
 "四笔记的分裂与'金色'合流（书名语境——通说待核）。",
 "60年代女性与政治（B389：active communist 交叉）。"],
"influence":[{"text":"Britannica：'one of the most complex and the most widely read'（B389）。","source":"B389"},{"text":"Britannica：2007诺奖（B389 交叉）。","source":"B389"}],
"reading":{"difficulties":["四笔记的交替结构。","60年代左翼语境。"],
 "editions":["《金色笔记》中译本（译林等——通说待核）。","英文原版。"],
 "order":"莱辛代表作；与《野草在歌唱》对读。"},
"pending":["安娜·伍尔夫名核对（通说）。","1962年出版细节待核。","四笔记颜色结构核对（通说）。"],
"sources":["B389"],"year_source":"B389","author_source":"B389","related_works":["suiyue","gududemigong","mangcike"],
"svg":G("《金色笔记》分裂结构图",[{"title":"四笔记","text":"黑红黄蓝的分裂（通说）","color":"gold"},{"title":"金色","text":"合流的尝试（书名）","color":"main"},{"title":"和解","text":"'与她时代的生活'（B389）","color":"antagonist"},{"title":"自由女性","text":"框架短篇（通说）","color":"family"}])},
{"id":"wuhhaotuchang","title":"五号屠场","original_title":"Slaughterhouse-Five","region":"美国","era":"现当代","era_detail":"20世纪60年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"vonnegut","author_name":"库尔特·冯内古特",
"year_display":"1969年（Britannica B390：Slaughterhouse-Five (1969; film 1972)——副题 The Children's Crusade）","year_sort":1969,
"background":["Britannica（B390）：'Explicitly draw[s] on his Dresden experience, Vonnegut crafted an absurdist nonlinear narrative in which the bombing raid serves as a symbol of the cruelty and destructiveness of war through the centuries'（以德累斯顿经验构造荒诞非线性叙事——轰炸作为战争残酷的世纪象征）。","Britannica（B390）：获 National Book Award for fiction（页面口径）——评论界'a modern-day classic'。","Britannica（B390）：Billy Pilgrim（页面问答口径：突出部战役被俘、德累斯顿幸存、被特拉法马多星人掳走、最终被枪杀）。"],
"outline":["（通说待核）毕利·皮尔格林的'时间旅行'：战俘、 德累斯顿与特拉法马多星。","（通说待核）'如此如此'的死亡清单（'So it goes'——B390 页未载，不采为引文）。"],
"characters":[{"name":"毕利·皮尔格林","identity":"战俘/时间旅人","note":"（B390 页面问答口径：Billy Pilgrim）"},{"name":"特拉法马多星人","identity":"外星劫持者","note":"（B390 页面问答口径）"}],
"themes":["德累斯顿轰炸作为'战争残酷的世纪象征'（B390）。",
 "荒诞的非线性叙事（B390：absurdist nonlinear narrative）。",
 "'黑色幽默'（B390：black humor）。"],
"influence":[{"text":"Britannica：'a modern-day classic'（B390）。","source":"B390"},{"text":"Britannica：National Book Award for fiction（页面口径）。","source":"B390"}],
"reading":{"difficulties":["非线性时间。","德累斯顿轰炸史（1945年2月——B390）。"],
 "editions":["《五号屠场》中译本（译林等——通说待核）。","英文原版。"],
 "order":"冯内古特代表作；与《猫的摇篮》对读。"},
"pending":["毕利·皮尔格林人名核对（B390 页面问答口径）。","1969年出版（Delacorte说）待核。","'So it goes'短语——B390 页未载（不采为引文——通说核对）。"],
"sources":["B390"],"year_source":"B390","author_source":"B390","related_works":["maodeyaolan","sangeshibing","meiguobuqu"],
"svg":G("《五号屠场》非线性结构图",[{"title":"时间旅行","text":"非线性叙事（B390）","color":"gold"},{"title":"德累斯顿","text":"轰炸的象征（B390）","color":"antagonist"},{"title":"毕利","text":"战俘的'解放'（通说）","color":"main"},{"title":"黑色幽默","text":"病态与滑稽（B390）","color":"family"}])},
{"id":"maodeyaolan","title":"猫的摇篮","original_title":"Cat's Cradle","region":"美国","era":"现当代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"vonnegut","author_name":"库尔特·冯内古特",
"year_display":"1963年（Britannica B390：Cat's Cradle (1963)——以此论文获芝加哥大学人类学硕士（1963））","year_sort":1963,
"background":["Britannica（B390）：Caribbean islanders practicing 'a religion consisting of harmless trivialities' encounter a substance that 'eventually destroys all life on Earth'。","Britannica（B390）：冯内古特把它作为论文提交——芝加哥大学授予人类学硕士（1963）。","题材（通说待核）：'冰-9'与博克农教——末日发明的讽刺。"],
"outline":["（通说待核）'冰-9'的发明与加勒比岛国博克农教。","（通说待核）世界终结的'猫的摇篮'游戏。"],
"characters":[{"name":"霍尼克博士","identity":"'冰-9'发明者","note":"（通说待核，B390未载）"},{"name":"博克农","identity":"宗教创始人","note":"（通说待核）"}],
"themes":["'无害琐碎的宗教'（B390：harmless trivialities）。",
 "'冰-9'：毁灭的发明（B390：destroys all life on Earth）。",
 "科学家的天真（通说待核）。"],
"influence":[{"text":"Britannica：人类学硕士论文（1963——B390）。","source":"B390"},{"text":"Britannica：'black humor'（B390 交叉）。","source":"B390"}],
"reading":{"difficulties":["'博克农'教义。","'冰-9'的物理寓言。"],
 "editions":["《猫的摇篮》中译本（译林等——通说待核）。","英文原版。"],
 "order":"冯内古特入门首选；后接《五号屠场》。"},
"pending":["霍尼克/博克农人名核对（通说）。","1963年出版（Holt, Rinehart说）待核。","'冰-9'细节待核。"],
"sources":["B390"],"year_source":"B390","author_source":"B390","related_works":["wuhhaotuchang","toutougeonv","huoluan"],
"svg":G("《猫的摇篮》末日发明图",[{"title":"冰-9","text":"毁灭的发明（B390）","color":"antagonist"},{"title":"博克农","text":"'无害琐碎'的宗教（B390）","color":"gold"},{"title":"摇篮","text":"猫线的游戏（书名）","color":"main"},{"title":"末日","text":"世界的终结（通说）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B38x/B39x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('jinsanbiji','lessing'), ('wuhhaotuchang','vonnegut'), ('maodeyaolan','vonnegut')]:
    if wid in created:
        link(aid, wid)
print('BATCH68 DONE')
