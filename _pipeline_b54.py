# -*- coding: utf-8 -*-
"""批54：零成本 3 部（我的大学/念珠/菲亚美达的哀歌）——突破700"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
{"id":"wodedaxue","title":"我的大学","original_title":"Мои университеты","region":"俄国","era":"近代","era_detail":"20世纪20年代",
"genre":"自传小说","genre_group":"小说","language":"俄语","author_id":"gorky","author_name":"马克西姆·高尔基",
"year_display":"作者页注记：Britannica——自传三部曲（年份通说待核——1923说）","year_sort":1923,
"background":["作者页注记：童年/在人间/我的大学——'自传三部曲（Britannica：one of the finest autobiographies in Russian literature）'。","Britannica：高尔基——俄国作家（作者页语境）。","题材（通说待核）：喀山的'大学'——贫民窟与面包房的'人民大学'。"],
"outline":["（通说待核）喀山岁月：革命小组与面包房。","（通说待核）'我的大学'：没有围墙的大学。"],
"characters":[{"name":"阿列克谢","identity":"青年","note":"（通说待核）"},{"name":"革命者","identity":"思想的朋友","note":"（通说待核）"}],
"themes":["'社会大学'的完成（书名语境——通说待核）。",
 "自传三部曲之三（B注记）。",
 "革命思想的萌芽（通说待核）。"],
"influence":[{"text":"Britannica：'one of the finest autobiographies in Russian literature'（作者页注记）。","source":src_of('gorky')},{"text":"Britannica：三部曲（作者页注记）。","source":src_of('gorky')}],
"reading":{"difficulties":["三部曲的顺序。","喀山革命小组语境。"],
 "editions":["《我的大学》中译本（人民文学等——通说待核）。","俄文原版（公有领域状态待核）。"],
 "order":"三部曲之三；承接《在人间》。"},
"pending":["1923年出版细节待核。","'革命小组'细节待核。","三部曲年份口径核对。"],
"sources":[src_of('gorky')],"year_source":src_of('gorky'),"author_source":src_of('gorky'),"related_works":["tongnian","zaihuang","zaidiceng"],
"svg":G("《我的大学》无墙大学图",[{"title":"喀山","text":"'大学'的课堂（通说）","color":"main"},{"title":"面包房","text":"劳动的学院（通说）","color":"gold"},{"title":"思想","text":"革命的萌芽（通说）","color":"family"},{"title":"三部曲","text":"B注记的位置","color":"antagonist"}])},
{"id":"nianzhu","title":"念珠","original_title":"Чётки（Rosary）","region":"俄国","era":"近代","era_detail":"20世纪10年代",
"genre":"诗集","genre_group":"诗歌","language":"俄语","author_id":"akhmatova","author_name":"安娜·阿赫玛托娃",
"year_display":"1914年（作者页注记：Britannica——黄昏（1912）、念珠 (1914)——早期）","year_sort":1914,
"background":["作者页注记：黄昏 (1912)、念珠 (1914)——'早期（Britannica）'。","Britannica：阿赫玛托娃——俄国女诗人（作者页语境）。","题材（通说待核）：爱情短诗的第二部集——'念珠'的祈祷意象。"],
"outline":["（通说待核）'念珠'：爱情祷告的珠串。","（通说待核）阿克梅派的短诗技艺（流派说通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"女诗人","note":"（通说待核）"}],
"themes":["爱情短诗（B注记语境）。",
 "'念珠'的祈祷意象（书名——通说待核）。",
 "阿克梅派（流派说待核）。"],
"influence":[{"text":"Britannica：念珠 (1914)——早期（作者页注记）。","source":src_of('akhmatova')},{"text":"Britannica：《安魂曲》为代表作（作者页交叉）。","source":src_of('akhmatova')}],
"reading":{"difficulties":["阿克梅派语境（待核）。","短诗的格律。"],
 "editions":["《念珠》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"阿赫玛托娃早期；与《黄昏》《安魂曲》对读。"},
"pending":["1914年出版细节待核。","'阿克梅派'归属核对（通说）。","篇目核对（Britannica未载）。"],
"sources":[src_of('akhmatova')],"year_source":src_of('akhmatova'),"author_source":src_of('akhmatova'),"related_works":["anhusiqu" if "anhusiqu" in existing else "leiyu","ezhihua","huangliang"],
"svg":G("《念珠》祈祷结构图",[{"title":"念珠","text":"爱情的祷告（书名）","color":"gold"},{"title":"短诗","text":"早期的技艺（B注记）","color":"main"},{"title":"阿克梅","text":"流派的坐标（通说）","color":"family"},{"title":"黄昏","text":"前作的延续（B注记）","color":"antagonist"}])},
{"id":"feiyameida","title":"菲亚美达的哀歌","original_title":"Elegia di Madonna Fiammetta","region":"意大利","era":"古代","era_detail":"14世纪40年代",
"genre":"散文爱情独白","genre_group":"散文","language":"意大利语（俗语）","author_id":"boccaccio","author_name":"乔万尼·薄伽丘",
"year_display":"作者页注记：Britannica 列举——菲亚美达的哀歌（俗语作品——年份通说待核）","year_sort":1343,
"background":["作者页注记：菲亚美达的哀歌、科尔巴乔——'俗语作品（Britannica 列举）'。","Britannica：薄伽丘——《十日谈》作者（作者页交叉）。","题材（通说待核）：菲亚美达被帕姆皮诺抛弃的独白——'原型心理小说'说。"],
"outline":["（通说待核）被弃女子的九日独白。","（通说待核）'疯狂'与'理智'的争辩。"],
"characters":[{"name":"菲亚美达","identity":"独白者","note":"（B注记：Madonna Fiammetta）"},{"name":"帕姆皮诺","identity":"负心人","note":"（通说待核）"}],
"themes":["被弃女性的内心（通说待核）。",
 "'俗语作品'（B注记）。",
 "《十日谈》人物的重用（通说待核）。"],
"influence":[{"text":"Britannica：'俗语作品'（作者页注记）。","source":src_of('boccaccio')},{"text":"Britannica：《十日谈》为代表作（作者页交叉）。","source":src_of('boccaccio')}],
"reading":{"difficulties":["早期意大利语。","'独白'的文体源流。"],
 "editions":["《菲亚美达的哀歌》中译名（《菲亚美达的哀歌/疯女哀歌》）待核。","意大利文原版（公有领域）。"],
 "order":"薄伽丘俗语作品；与《十日谈》《名女传》对读。"},
"pending":["1343-44年写作年份待核。","菲亚美达/帕姆皮诺人名核对（通说）。","'心理小说原型'评价待核。"],
"sources":[src_of('boccaccio')],"year_source":src_of('boccaccio'),"author_source":src_of('boccaccio'),"related_works":["shiritan","mingnuzhuan","ezhihua"],
"svg":G("《菲亚美达的哀歌》独白结构图",[{"title":"菲亚美达","text":"被弃的独白（通说）","color":"main"},{"title":"疯狂","text":"理智的争辩（通说）","color":"antagonist"},{"title":"俗语","text":"意大利语的写作（B注记）","color":"gold"},{"title":"哀歌","text":"女性的声音（通说）","color":"family"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批54）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('wodedaxue','gorky','我的大学'),('nianzhu','akhmatova','念珠'),('feiyameida','boccaccio','菲亚美达')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH54 DONE')
