# -*- coding: utf-8 -*-
"""批79：Britannica 新核 2 作家 2 部（卡赞扎基斯 B410 希腊人左巴/曼斯菲尔德 B411 园会）"""
import json, pathlib

newsrc = [
{"id":"B410","title":"Nikos Kazantzakis — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Nikos-Kazantzakis","type":"百科全书","verified":True,"covers":["kazantzakis","xilarenzuoba"],"note":"2026-11-21 核对：1883-02-18克里特Iráklion生（时属奥斯曼帝国）—1957-10-26西德弗赖堡卒（74岁）；'a Greek writer whose prolific output and wide variety of work represent a major contribution to modern Greek literature'；Zorba the Greek（Víos kai politía tou Aléxi Zormpá, 1946）——'a portrayal of a passionate lover of life and poor-man's philosopher'（热爱生活的穷苦人哲学家）；Freedom or Death（O Kapetán Mikhális, 1950）——'a depiction of Cretan Greeks' struggle against their Ottoman overlords in the 19th century'；The Greek Passion (1954)；The Last Temptation of Christ (1955)——'a revisionist psychological study of Jesus Christ'；Odíssa (1938)——33333行荷马《奥德赛》续作史诗——'expresses the full range of Kazantzákis philosophy'；Report to Greco (1961死后)；电影：Celui qui doit mourir (1958)、Zorba the Greek (1964)、The Last Temptation of Christ (1988)；雅典法学(1902-06)、巴黎随柏格森学哲学(1907-09)、1945年希腊政府部长、1947-48巴黎UNESCO、晚定居法国昂蒂布"},
{"id":"B411","title":"Katherine Mansfield — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Katherine-Mansfield","type":"百科全书","verified":True,"covers":["mansfield","yuanhui"],"note":"2026-11-21 核对：原名 Kathleen Mansfield Beauchamp（夫姓 Murry）；1888-10-14新西兰惠灵顿生—1923-01-09法国枫丹白露附近 Gurdjieff 学院卒（34岁）；Bliss (1920)——'secured her reputation and is typical of her art'；The Garden Party (1922)——含'At the Bay'/'The Voyage'/'The Stranger'/'Daughters of the Late Colonel'——后者'a subtle account of genteel frustration'；'a master of the short story whose style had many overtones of poetry'——心理冲突+契诃夫影响——'she in turn shaped the short story's development as a literary form'；In a German Pension (1911)；Prelude (1918)——新西兰家族记忆短篇系列；Journal (1927, 修订1954——Murry编)；The Dove's Nest (1923死后)、Something Childish (1924死后)；书信集 O'Sullivan/Scott 编 (1984-2008)"},
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
{"id":"kazantzakis","name":"尼科斯·卡赞扎基斯","foreign_name":"Níkos Kazantzákis（尼科斯·卡赞扎基斯，1883-02-18—1957-10-26）","country":"希腊","birth":1883,"death":1957,"birth_year":1883,"death_year":1957,"era":"近代",
"summary":"卡赞扎基斯，克里特Iráklion生（时属奥斯曼帝国），希腊作家——'a Greek writer whose prolific output and wide variety of work represent a major contribution to modern Greek literature'（B410）。Zorba the Greek（希腊人左巴, 1946）——'a portrayal of a passionate lover of life and poor-man's philosopher'（B410）；The Last Temptation of Christ (1955)——'a revisionist psychological study of Jesus Christ'（B410）；Odíssa (1938)——33333行荷马《奥德赛》续作史诗（B410）。巴黎随柏格森学哲学（1907-09）（B410）；1945年希腊政府部长（B410）。",
"timeline":[
 {"year":1883,"text":"2月18日生于克里特Iráklion（B410）。","src":"B410"},
 {"year":1938,"text":"Odíssa——33333行史诗（B410）。","src":"B410"},
 {"year":1946,"text":"Zorba the Greek（希腊人左巴）（B410）。","src":"B410"},
 {"year":1957,"text":"10月26日卒于西德弗赖堡（B410）。","src":"B410"}],
"major_works":[
 {"work_id":"xilarenzuoba","note":"1946（B410）"},
 {"title":"基督的最后诱惑","note":"（B410：The Last Temptation of Christ (1955)——中译名待核）"},
 {"title":"自由或死亡","note":"（B410：Freedom or Death (1950)——中译名待核）"}],
"style":["'热爱生活的穷苦人哲学家'（B410：Zorba——poor-man's philosopher）。",
 "'再造'的耶稣研究（B410：revisionist psychological study）。",
 "克里特的'自由或死亡'（B410：Freedom or Death）。"],
"status":"Britannica 定位卡赞扎基斯为现代希腊文学的'重大贡献者'（B410）。",
"sources":["B410"],"dates_source":"B410",
"pending":["《希腊人左巴》通行译名（《希腊人左巴》）待核。","1964年电影（米夏利斯·卡柯扬尼斯说）待核——B410仅载年份。","1955年《基督的最后诱惑》被罗马教会列禁书说待核（通说）。"]},
{"id":"mansfield","name":"凯瑟琳·曼斯菲尔德","foreign_name":"Katherine Mansfield（凯瑟琳·曼斯菲尔德，原名 Kathleen Mansfield Beauchamp，1888-10-14—1923-01-09）","country":"新西兰","birth":1888,"death":1923,"birth_year":1888,"death_year":1923,"era":"近代",
"summary":"曼斯菲尔德，新西兰惠灵顿生，短篇小说家——1923年1月9日卒于法国枫丹白露附近 Gurdjieff 学院，34岁（B411）。Bliss (1920)——'secured her reputation and is typical of her art'（B411）。The Garden Party（园会, 1922）——含'At the Bay'/'The Voyage'/'The Stranger'/'Daughters of the Late Colonel'——后者'a subtle account of genteel frustration'（B411）。'a master of the short story whose style had many overtones of poetry'——受契诃夫影响——'she in turn shaped the short story's development as a literary form'（B411）。",
"timeline":[
 {"year":1888,"text":"10月14日生于新西兰惠灵顿（B411）。","src":"B411"},
 {"year":1920,"text":"Bliss——声誉确立（B411）。","src":"B411"},
 {"year":1922,"text":"The Garden Party（园会）（B411）。","src":"B411"},
 {"year":1923,"text":"1月9日卒于法国 Gurdjieff 学院（B411）。","src":"B411"}],
"major_works":[
 {"work_id":"yuanhui","note":"1922（B411）"},
 {"title":"幸福","note":"（B411：Bliss (1920)——中译名待核）"},
 {"title":"序曲","note":"（B411：Prelude (1918)——新西兰家族记忆短篇系列）"}],
"style":["'诗意回声'的短篇风格（B411：many overtones of poetry）。",
 "心理冲突+契诃夫影响（B411）。",
 "'塑造了短篇小说文体的发展'（B411：shaped the short story's development）。"],
"status":"Britannica 定位曼斯菲尔德为短篇大师、短篇小说文体发展的塑造者（B411）。",
"sources":["B411"],"dates_source":"B411",
"pending":["《园会》通行译名（《园会》）待核。","Gurdjieff 学院细节（B411已载卒地）待核。","与契诃夫的影响关系（B411：Chekhov's influence）细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"xilarenzuoba","title":"希腊人左巴","original_title":"Víos kai politía tou Aléxi Zormpá","region":"希腊","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"希腊语","author_id":"kazantzakis","author_name":"尼科斯·卡赞扎基斯",
"year_display":"1946年（Britannica B410：Zorba the Greek (Víos kai politía tou Aléxi Zormpá, 1946)）","year_sort":1946,
"background":["Britannica（B410）：Zorba——'a portrayal of a passionate lover of life and poor-man's philosopher'（热爱生活的穷苦人哲学家）。","Britannica（B410）：卡赞扎基斯——'a major contribution to modern Greek literature'。","题材（通说待核）：'我'与左巴的克里特褐煤生意——dance 与丧子的酒馆。"],
"outline":["（通说待核——B410未载剧情）'我'的书记人生与左巴的'自由'哲学。","（通说待核）褐煤的失败与 widow 的私刑。"],
"characters":[{"name":"左巴","identity":"工人/哲学家","note":"（B410：poor-man's philosopher——名通说待核：阿列克西斯·佐尔巴）"},{"name":"'我'（书生）","identity":"雇主","note":"（通说待核）"}],
"themes":["'热爱生活的穷苦人哲学家'（B410）。",
 "书与身体（通说待核）。",
 "克里特的习俗暴力（通说待核）。"],
"influence":[{"text":"Britannica：'a major contribution to modern Greek literature'（B410）。","source":"B410"},{"text":"Britannica：1964年电影改编（B410）。","source":"B410"}],
"reading":{"difficulties":["克里特习俗（ widow 私刑——通说待核）。","'左巴舞'的节奏（通说待核）。"],
 "editions":["《希腊人左巴》中译名（《希腊人佐巴》）待核。","希腊文原版。"],
 "order":"卡赞扎基斯首选；与《基督的最后诱惑》对读。"},
"pending":["左巴全名（阿列克西斯·佐尔巴——B410书名希腊文含 Zormpá）核对。","1946年出版细节待核。","1964年电影（Anthony Quinn说）待核。"],
"sources":["B410"],"year_source":"B410","author_source":"B410","related_works":["shenglisong","xilarenzuoba" if False else "leiyu","gududemigong"],
"svg":G("《希腊人左巴》生命哲学图",[{"title":"左巴","text":"'穷苦人的哲学家'（B410）","color":"main"},{"title":"舞蹈","text":"生命的节奏（通说）","color":"gold"},{"title":"书生","text":"纸上的囚徒（通说）","color":"family"},{"title":"克里特","text":"习俗的暴力（通说）","color":"antagonist"}])},
{"id":"yuanhui","title":"园会","original_title":"The Garden Party","region":"新西兰","era":"近代","era_detail":"20世纪20年代初",
"genre":"短篇小说集","genre_group":"故事集","language":"英语","author_id":"mansfield","author_name":"凯瑟琳·曼斯菲尔德",
"year_display":"1922年（Britannica B411：The Garden Party (1922)——含'At the Bay'/'The Voyage'/'The Stranger'/'Daughters of the Late Colonel'）","year_sort":1922,
"background":["Britannica（B411）：The Garden Party——含'At the Bay'/'The Voyage'/'The Stranger'/'Daughters of the Late Colonel'——后者'a subtle account of genteel frustration'。","Britannica（B411）：曼斯菲尔德——'a master of the short story whose style had many overtones of poetry'——受契诃夫影响——'she in turn shaped the short story's development as a literary form'。","题材（通说待核）：同名篇——劳拉的花园会与死者家庭的'帽子'。"],
"outline":["（通说待核）劳拉的花园会与邻巷死者的对照。","（通说待核）'帽子'：阶级的暂停与恢复（通说待核）。"],
"characters":[{"name":"劳拉","identity":"谢里丹家小女儿","note":"（通说待核，B411未载）"},{"name":"亡者之家","identity":"邻巷穷家","note":"（通说待核）"}],
"themes":["阶级的'帽子'暂停（通说待核）。",
 "'诗意回声'的短篇（B411：many overtones of poetry）。",
 "'文雅的失意'（B411：genteel frustration——Daughters of the Late Colonel）。"],
"influence":[{"text":"Britannica：'secured her reputation and is typical of her art'（B411——Bliss 交叉）。","source":"B411"},{"text":"Britannica：'shaped the short story's development as a literary form'（B411）。","source":"B411"}],
"reading":{"difficulties":["'诗意回声'的句法。","新西兰/英国的双地书写（Prelude 交叉——B411）。"],
 "editions":["《园会》中译本（人民文学等——通说待核）。","英文原版（公有领域状态待核）。"],
 "order":"曼斯菲尔德首选；与《幸福》对读。"},
"pending":["劳拉人名核对（通说）。","1922年出版（Constable说）待核。","'Daughters of the Late Colonel'细节待核（B411已载评语）。"],
"sources":["B411"],"year_source":"B411","author_source":"B411","related_works":["yuanhui" if False else "leiyu","chunjiuji","nvpu"],
"svg":G("《园会》阶级对照图",[{"title":"花园会","text":"盛开的玫瑰（通说）","color":"gold"},{"title":"死者","text":"邻巷的哀恸（通说）","color":"antagonist"},{"title":"帽子","text":"阶级的暂停（通说）","color":"main"},{"title":"诗意","text":"'回声'的短篇（B411）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B41x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('xilarenzuoba','kazantzakis'), ('yuanhui','mansfield')]:
    if wid in created:
        link(aid, wid)
print('BATCH79 DONE')
