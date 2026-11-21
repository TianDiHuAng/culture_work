# -*- coding: utf-8 -*-
"""批62：Britannica 新核达里奥·福 B383×2（一个无政府主义者的意外死亡/滑稽神秘剧）"""
import json, pathlib

newsrc = [
{"id":"B383","title":"Dario Fo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Dario-Fo","type":"百科全书","verified":True,"covers":["dariofo","yigewuzhengfuzhisi"],"note":"2026-11-21 核对：1926-03-24意大利Leggiuno-Sangiano生—2016-10-13米兰卒（90岁）；1997诺贝尔文学奖；Mistero Buffo（滑稽神秘剧, 1973）——'solo tour de force'——'based on medieval mystery plays but so topical that the shows changed with each audience'；Morte accidentale di un anarchico（一个无政府主义者的意外死亡, 1970）——最受欢迎剧作之列；先锋剧作家/导演/哑剧演员——遭'government censure as a theatrical caricaturist with a flair for social agitation'——'often blasphemous and scatological but rooted in the tradition of commedia dell'arte'混以'unofficial leftism'；giullare（中世纪游吟艺人）传统——Lu santo jullàre Françesco (1999; Francis, the Holy Jester)；妻 Franca Rame（演员）——合作自首场卡巴莱至1962年电视秀 Canzonissima 并合著多剧；创团 La Comune (1970)——'they began to tour factories, parks, and gymnasiums'；We Can't Pay? We Won't Pay! (1974)、The Pope and the Witch (1989)；80余剧；小说 The Pope's Daughter (2014)、There Is a Mad King in Denmark (2015)"},
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
{"id":"dariofo","name":"达里奥·福","foreign_name":"Dario Fo（达里奥·福，1926-03-24—2016-10-13）","country":"意大利","birth":1926,"death":2016,"birth_year":1926,"death_year":2016,"era":"现当代",
"summary":"达里奥·福，意大利Leggiuno-Sangiano生，剧作家、导演与哑剧演员——1997年诺贝尔文学奖（B383）。Mistero Buffo（滑稽神秘剧, 1973）——'solo tour de force'——'based on medieval mystery plays but so topical that the shows changed with each audience'（B383）。Morte accidentale di un anarchico（一个无政府主义者的意外死亡, 1970）——最受欢迎剧作之列（B383）。遭'government censure as a theatrical caricaturist with a flair for social agitation'（B383）——'often blasphemous and scatological but rooted in the tradition of commedia dell'arte'混以'unofficial leftism'（B383）。妻 Franca Rame 合作；创团 La Comune (1970)——'they began to tour factories, parks, and gymnasiums'（B383）。80余剧（B383）。",
"timeline":[
 {"year":1926,"text":"3月24日生于意大利Leggiuno-Sangiano（B383）。","src":"B383"},
 {"year":1970,"text":"《一个无政府主义者的意外死亡》——最受欢迎剧作之列（B383）。","src":"B383"},
 {"year":1970,"text":"创 La Comune 剧团——巡演工厂、公园与体育馆（B383）。","src":"B383"},
 {"year":1997,"text":"获诺贝尔文学奖（B383）。","src":"B383"},
 {"year":2016,"text":"10月13日卒于米兰（B383）。","src":"B383"}],
"major_works":[
 {"work_id":"yigewuzhengfuzhisi","note":"1970（B383）"},
 {"work_id":"huajishenmiju","note":"1973（B383）"},
 {"title":"我们不能付钱？我们不付！","note":"（B383：We Can't Pay? We Won't Pay! (1974)——中译名待核）"}],
"style":["'中世纪神秘剧'的现代滑稽化（B383：Mistero Buffo）。",
 "commedia dell'arte 传统+'非官方左翼'（B383）。",
 "giullare（游吟艺人）传统的复兴（B383：Lu santo jullàre Françesco）。"],
"status":"Britannica 定位达里奥·福为1997诺奖得主、遭政府审查的'社会鼓动型'戏剧讽刺家（B383）。",
"sources":["B383"],"dates_source":"B383",
"pending":["《滑稽神秘剧》通行译名（《滑稽神秘剧》）待核。","与 Franca Rame 合作剧清单待核。","'80余剧'总数口径待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"yigewuzhengfuzhisi","title":"一个无政府主义者的意外死亡","original_title":"Morte accidentale di un anarchico","region":"意大利","era":"现当代","era_detail":"20世纪70年代初",
"genre":"戏剧","genre_group":"戏剧","language":"意大利语","author_id":"dariofo","author_name":"达里奥·福",
"year_display":"1970年（Britannica B383：Morte accidentale di un anarchico (1970)——最受欢迎剧作之列）","year_sort":1970,
"background":["Britannica（B383）：最受欢迎剧作之列（'listed among his most popular plays'）。","Britannica（B383）：福——遭'government censure as a theatrical caricaturist with a flair for social agitation'。","题材（通说待核）：1969年米兰炸案与'坠楼'的无政府主义者皮内利——疯子警探的'调查'（真相取材于真实案件说通说待核）。"],
"outline":["（通说待核）'疯子'冒充法官重审'意外死亡'案。","（通说待核）警方的谎言与'第N次坠楼'。"],
"characters":[{"name":"疯子（Il Matto）","identity":"假法官","note":"（通说待核，B383未载）"},{"name":"警长","identity":"体制的口舌","note":"（通说待核）"}],
"themes":["'意外死亡'的官方叙事（书名语境——通说待核）。",
 "闹剧的抗议（B383：social agitation）。",
 "commedia dell'arte 的当代变身（B383）。"],
"influence":[{"text":"Britannica：'listed among his most popular plays'（B383）。","source":"B383"},{"text":"Britannica：1997诺奖（B383 交叉）。","source":"B383"}],
"reading":{"difficulties":["真实案件底本（皮内利案说——通说待核）。","闹剧节奏与即兴。"],
 "editions":["《一个无政府主义者的意外死亡》中译本（人民文学等——通说待核）。","意大利文原版。"],
 "order":"达里奥·福首选；与《滑稽神秘剧》对读。"},
"pending":["皮内利案（1969 Piazza Fontana案说）细节待核。","1970年首演细节待核。","'疯子'角色细节待核。"],
"sources":["B383"],"year_source":"B383","author_source":"B383","related_works":["xiniu","toutougeonv","richu"],
"svg":G("《一个无政府主义者的意外死亡》闹剧调查图",[{"title":"疯子","text":"假法官的重审（通说）","color":"main"},{"title":"坠楼","text":"'意外'的官方叙事（书名）","color":"antagonist"},{"title":"闹剧","text":"抗议的形态（B383）","color":"gold"},{"title":"米兰","text":"1969年的案件（通说）","color":"family"}])},
{"id":"huajishenmiju","title":"滑稽神秘剧","original_title":"Mistero Buffo","region":"意大利","era":"现当代","era_detail":"20世纪70年代",
"genre":"独角戏（系列）","genre_group":"戏剧","language":"意大利语（方言）","author_id":"dariofo","author_name":"达里奥·福",
"year_display":"1973年（Britannica B383：Mistero Buffo (1973)——'solo tour de force'）","year_sort":1973,
"background":["Britannica（B383）：'solo tour de force'——'based on medieval mystery plays but so topical that the shows changed with each audience'（基于中世纪神秘剧，但如此切合时事以致随观众而变）。","Britannica（B383）：福——giullare（中世纪游吟艺人）传统的复兴者（Lu santo jullàre Françesco 1999 交叉）。","题材（通说待核）：福的独白戏仿：圣母的'方言诉苦'与穷人的福音。"],
"outline":["（通说待核）福音故事的方言戏仿：'松子圣母'等段落（段名通说待核）。","（通说待核）'随观众而变'的即兴（B383）。"],
"characters":[{"name":"游吟艺人（福）","identity":"独角讲述者","note":"（B383：solo tour de force）"}],
"themes":["'中世纪神秘剧'的现代滑稽（B383）。",
 "方言的政治（通说待核）。",
 "穷人的福音（通说待核）。"],
"influence":[{"text":"Britannica：'solo tour de force'（B383）。","source":"B383"},{"text":"Britannica：1997诺奖（B383 交叉）。","source":"B383"}],
"reading":{"difficulties":["方言独白的语感。","'神秘剧'的中世纪底本。"],
 "editions":["《滑稽神秘剧》中译本（人民文学等——通说待核）。","意大利文原版。"],
 "order":"达里奥·福独角戏首选；与《意外死亡》对读。"},
"pending":["段落名（《松子圣母》说——通说）核对。","1973年首演细节待核。","'即兴'的版本差异待核（B383：changed with each audience）。"],
"sources":["B383"],"year_source":"B383","author_source":"B383","related_works":["yigewuzhengfuzhisi","toutougeonv","xiniu"],
"svg":G("《滑稽神秘剧》方言戏仿图",[{"title":"神秘剧","text":"中世纪的底本（B383）","color":"family"},{"title":"方言","text":"穷人的福音（通说）","color":"main"},{"title":"独角","text":"'tour de force'（B383）","color":"gold"},{"title":"时事","text":"随观众而变（B383）","color":"antagonist"}])},
]
created = []
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    created.append(w['id'])
    print('work', w['id'])

def link(aid, wid, kw=None):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        done = False
        if kw:
            for i, m in enumerate(j['major_works']):
                if m.get('title') and kw in m['title']:
                    j['major_works'][i] = {"work_id": wid, "note": m['note']}
                    done = True; break
        if not done:
            j['major_works'].append({"work_id": wid, "note": "（B383 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('yigewuzhengfuzhisi','dariofo','无政府主义者的意外死亡'),('huajishenmiju','dariofo','滑稽神秘剧')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH62 DONE')
