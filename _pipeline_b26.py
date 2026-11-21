# -*- coding: utf-8 -*-
"""批26：Britannica 新核 3 作家 3 部（莱蒙特/加·米斯特拉尔/布勒东 B342-B344）"""
import json, pathlib

newsrc = [
{"id":"B342","title":"Wladyslaw Reymont — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Wladyslaw-Reymont","type":"百科全书","verified":True,"covers":["reymont","nongmin"],"note":"2026-11-21 核对：1867-05-07波兰Kobiele Wielkie（俄属波兰）生—1925-12-05华沙卒（58岁）；1924诺贝尔文学奖；Chłopi（农民）1904-09四卷——'a chronicle of peasant life during the four seasons of a year'——'Written almost entirely in peasant dialect'——'won for Reymont the Nobel Prize'（1973年拍成电影）；Ziemia obiecana (1899; The Promised Land)——罗兹纺织厂主（1974年电影）；Komediantka (1896; The Comedienne)、Fermenty (1897)；Wampir (1911)——唯灵论趣味；Rok 1794 三卷 (1913-18)——波兰被瓜分初期；早期农村短篇'the strong influence of Naturalism'"},
{"id":"B343","title":"Gabriela Mistral — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Gabriela-Mistral","type":"百科全书","verified":True,"covers":["gmistral","huangliang"],"note":"2026-11-21 核对：原名 Lucila Godoy Alcayaga；1889-04-07智利Vicuña生—1957-01-10纽约州Hempstead卒（67岁）；1945诺贝尔文学奖——'the first Latin American to win the Nobel Prize for Literature'；Desolación (1922)——早期作品集，含'Dolor'——'detailing the aftermath of a love affair that was ended by the suicide'；Ternura (1924, 1945扩)、Tala (1938; 'Destruction')、Lagar (1954; 'The Wine Press')——'evidence a broader interest'；主题'love of children and of the downtrodden remained her principal themes'；风格'warmth of feeling and emotional power'；15岁任小学教师、后为教授/教育者/文化部长/外交官（马德里/里斯本/热那亚/尼斯）；1914年以'Sonetos de la muerte'（死亡十四行诗）获智利奖而成名；笔名取自 D'Annunzio 与 Frédéric Mistral；英译者 Langston Hughes (1957)、Doris Dana (1957)、Ursula K. Le Guin (2003)"},
{"id":"B344","title":"Andre Breton — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Andre-Breton","type":"百科全书","verified":True,"covers":["breton","najia"],"note":"2026-11-21 核对：1896-02-18法国Tinchebray生—1966-09-28巴黎卒（70岁）；'chief promoter and one of the founders of the Surrealist movement'；1919与阿拉贡、苏波创办 Littérature；与苏波合著 Les Champs magnétiques (1920)——'the first example of the Surrealist technique of automatic writing'；1924宣言定义超现实主义——'pure psychic automatism, by which it is intended to express…the real process of thought'——'the dictation of thought, free from any control by the reason'——超现实主义'aimed to eliminate the distinction between dream and reality, reason and madness'；Nadja (1928)——'merged everyday occurrences with psychological aberrations'；L'Immaculée Conception (1930, 与艾吕雅)——'attempted to convey a verbal impression of different types of mental disorder'；医学出身、读过弗洛伊德（1921会面）；1930第二宣言；1935年与共产党决裂但保留马克思主义立场；二战流亡美国、1942耶鲁超现实主义展+第三宣言；1946返法；L'Amour fou (1937; Mad Love)、Les Vases communicants (1932)"},
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
def find_work(aid, prefer=None):
    got = [p.stem for p in pathlib.Path('data/works').glob('*.json') if json.load(open(p, encoding='utf-8'))['author_id'] == aid]
    for pref in prefer or []:
        if pref in got: return pref
    return got[0] if got else None

def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

wid_nongmin = next(w for w in ['nongmin','chlopi','nongmin_reymont'] if w not in existing)
rel_rey = [rid(find_work('milosz'), find_work('mickiewicz'), 'sienkiewicz'), rid(find_work('sienkiewicz')), 'qieelvxing']
rel_rey = list(dict.fromkeys(rel_rey))[:3]
rel_nadja = [rid('diyuzhiji'), rid('toutougeonv'), rid('kanbujian3')]
rel_mis = [rid(find_work('neruda', []), 'diyuzhiji'), rid('diyuzhiji'), rid('ezhihua')]
print('wid:', wid_nongmin, 'rel:', rel_rey, rel_nadja, rel_mis)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"reymont","name":"弗拉迪斯拉夫·莱蒙特","foreign_name":"Władysław Reymont（弗拉迪斯拉夫·莱蒙特，1867-05-07—1925-12-05）","country":"波兰","birth":1867,"death":1925,"birth_year":1867,"death_year":1925,"era":"近代",
"summary":"莱蒙特，俄属波兰Kobiele Wielkie生，波兰小说家——1924年诺贝尔文学奖（B342）。Chłopi（农民, 1904-09）四卷——'a chronicle of peasant life during the four seasons of a year'（四季农事编年——B342）——'Written almost entirely in peasant dialect'（几乎全用农民方言写成——B342）——'won for Reymont the Nobel Prize'（B342）。Ziemia obiecana（福地, 1899）——罗兹纺织工业城（B342）；Rok 1794 三卷（1913-18）——波兰被瓜分初期（B342）。早期农村短篇受自然主义强影响（B342）。",
"timeline":[
 {"year":1867,"text":"5月7日生于俄属波兰Kobiele Wielkie（B342）。","src":"B342"},
 {"year":1899,"text":"Ziemia obiecana（福地）——罗兹纺织厂主的生活（B342）。","src":"B342"},
 {"year":1904,"text":"《农民》四卷（1904-09）开始出版（B342）。","src":"B342"},
 {"year":1924,"text":"获诺贝尔文学奖（B342：'won for Reymont the Nobel Prize'）。","src":"B342"},
 {"year":1925,"text":"12月5日卒于华沙（B342）。","src":"B342"}],
"major_works":[
 {"work_id":wid_nongmin,"note":"1904-09四卷（B342）"},
 {"title":"福地","note":"（B342：Ziemia obiecana, 1899）"},
 {"title":"1794年","note":"（B342：Rok 1794, 1913-18三卷）"}],
"style":["农民方言的编年体（B342：peasant dialect / chronicle）。",
 "自然主义的农村书写（B342：早期短篇 the strong influence of Naturalism）。",
 "工业城市的批判（《福地》——B342 语境）。"],
"status":"Britannica 定位莱蒙特为1924年诺奖得主、《农民》为其获奖之作（B342）。",
"sources":["B342"],"dates_source":"B342",
"pending":["《农民》四卷书名（秋冬卷次）核对。","《福地》通行中译名（《福地》/《应许之地》）待核。","1924诺奖授奖理由细节待核。"]},
{"id":"gmistral","name":"加夫列拉·米斯特拉尔","foreign_name":"Gabriela Mistral（加夫列拉·米斯特拉尔，原名 Lucila Godoy Alcayaga，1889-04-07—1957-01-10）","country":"智利","birth":1889,"death":1957,"birth_year":1889,"death_year":1957,"era":"现当代",
"summary":"米斯特拉尔，原名 Lucila Godoy Alcayaga，智利Vicuña生，诗人、教师与外交官——1945年诺贝尔文学奖——'the first Latin American to win the Nobel Prize for Literature'（首位获诺奖的拉美作家——B343）。Desolación（荒凉, 1922）——早期作品集，含'Dolor'——'detailing the aftermath of a love affair that was ended by the suicide'（B343）；Tala（塔拉, 1938）、Lagar（压榨, 1954）——'evidence a broader interest'（B343）。主题：'love of children and of the downtrodden remained her principal themes'（对孩子的爱与对底层者的爱——B343）；风格：'warmth of feeling and emotional power'（B343）。15岁任小学教师，后为教授、教育者、文化部长与外交官（B343）。1914年以'Sonetos de la muerte'成名（B343）。",
"timeline":[
 {"year":1889,"text":"4月7日生于智利Vicuña（B343）。","src":"B343"},
 {"year":1914,"text":"以'Sonetos de la muerte'（死亡十四行诗）获智利奖，成名（B343）。","src":"B343"},
 {"year":1922,"text":"Desolación（荒凉）——早期作品集（B343）。","src":"B343"},
 {"year":1945,"text":"获诺贝尔文学奖——首位拉美得主（B343）。","src":"B343"},
 {"year":1957,"text":"1月10日卒于纽约州Hempstead（B343）。","src":"B343"}],
"major_works":[
 {"work_id":"huangliang","note":"1922（B343）"},
 {"title":"塔拉","note":"（B343：Tala, 1938——'Destruction'）"},
 {"title":"母性的诗","note":"（B343：Ternura (1924, 1945扩；'Tenderness')——中译名待核）"}],
"style":["'warmth of feeling and emotional power'（B343）。",
 "死亡十四行诗的挽歌体（B343：'Sonetos de la muerte'）。",
 "儿童与底层者的主题（B343）。"],
"status":"Britannica 定位米斯特拉尔为首位拉美诺奖得主、教师出身的诗人外交官（B343）。",
"sources":["B343"],"dates_source":"B343",
"pending":["卒地（纽约州Hempstead——一说长岛）待核。","Ternura/Lagar 通行中译名待核。","笔名取自 D'Annunzio 与 Frédéric Mistral 之说仅 B343 口径。"]},
{"id":"breton","name":"安德烈·布勒东","foreign_name":"André Breton（安德烈·布勒东，1896-02-18—1966-09-28）","country":"法国","birth":1896,"death":1966,"birth_year":1896,"death_year":1966,"era":"现当代",
"summary":"布勒东，法国Tinchebray生，诗人与理论家——'chief promoter and one of the founders of the Surrealist movement'（超现实主义运动的主要推动者与创始人之一——B344）。1924年宣言定义超现实主义：'pure psychic automatism, by which it is intended to express…the real process of thought'、'the dictation of thought, free from any control by the reason'——超现实主义'aimed to eliminate the distinction between dream and reality, reason and madness'（B344）。与苏波合著 Les Champs magnétiques（磁场, 1920）——'the first example of the Surrealist technique of automatic writing'（B344）。Nadja（娜佳, 1928）——'merged everyday occurrences with psychological aberrations'（B344）。医学出身、读弗洛伊德（1921年会面）；1935年与共产党决裂；二战流亡美国，1946年返法（B344）。",
"timeline":[
 {"year":1896,"text":"2月18日生于法国Tinchebray（B344）。","src":"B344"},
 {"year":1919,"text":"与阿拉贡、苏波创办 Littérature 杂志（B344）。","src":"B344"},
 {"year":1924,"text":"《超现实主义宣言》——运动的正式定义（B344）。","src":"B344"},
 {"year":1928,"text":"Nadja（娜佳）出版（B344）。","src":"B344"},
 {"year":1942,"text":"流亡美国期间组织耶鲁超现实主义展并发表第三宣言（B344）。","src":"B344"},
 {"year":1966,"text":"9月28日卒于巴黎（B344）。","src":"B344"}],
"major_works":[
 {"work_id":"najia","note":"1928（B344）"},
 {"title":"磁场","note":"（B344：Les Champs magnétiques, 1920——与苏波合著）"},
 {"title":"疯狂的爱","note":"（B344：L'Amour fou (1937; Mad Love)——中译名待核）"}],
"style":["自动写作（B344：automatic writing）。",
 "梦与现实边界的消除（B344）。",
 "宣言体的理论写作（B344：1924/1930两宣言）。"],
"status":"Britannica 定位布勒东为超现实主义运动的首席推动者（B344）。",
"sources":["B344"],"dates_source":"B344",
"pending":["Nadja 中译名（《娜佳》/《娜嘉》）待核。","1921年弗洛伊德会面细节（维也纳说）待核。","宣言通行译本细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"najia","title":"娜佳","original_title":"Nadja","region":"法国","era":"现当代","era_detail":"20世纪20年代",
"genre":"小说（自传性散文）","genre_group":"小说","language":"法语","author_id":"breton","author_name":"安德烈·布勒东",
"year_display":"1928年（Britannica B344：Nadja (1928)）","year_sort":1928,
"background":["Britannica（B344）：Nadja——'merged everyday occurrences with psychological aberrations'（把日常事件与心理异象熔为一体）。","Britannica（B344）：布勒东为超现实主义'chief promoter and one of the founders'；1924宣言定义'pure psychic automatism'。","题材（通说待核）：'我'与神秘女子娜佳在巴黎街头相遇——疯癫与诗意的边界。"],
"outline":["巴黎街头的日常相遇与'心理异象'的交织（B344：everyday occurrences...psychological aberrations）。","娜佳其人（原型说通说待核）：谵妄中的'自由精灵'（通说待核）。"],
"characters":[{"name":"'我'","identity":"叙述者","note":"（B344 自传性语境）"},{"name":"娜佳","identity":"神秘女子","note":"（B344 书名人物）"}],
"themes":["梦与现实的边界消除（B344：eliminate the distinction between dream and reality）。","自动写作的叙事化（B344：automatic writing）。","谵妄与诗意（B344：psychological aberrations 语境）。"],
"influence":[{"text":"Britannica：超现实主义运动的核心文本之一（B344 定位）。","source":"B344"},{"text":"Britannica：'merged everyday occurrences with psychological aberrations'（B344）。","source":"B344"}],
"reading":{"difficulties":["超现实主义术语（自动写作/客体）。","1920年代巴黎的先锋派圈层。"],
 "editions":["《娜佳》中译名（《娜佳》/《娜嘉》）——通说待核。","法文原版。"],
 "order":"布勒东首选；配合《超现实主义宣言》阅读。"},
"pending":["娜佳原型（Jacquina Roque说/其他）待核。","1928年初版与1963年修订版差异待核。","人物照片插入的'档案性'细节待核。"],
"sources":["B344"],"year_source":"B344","author_source":"B344","related_works":rel_nadja,
"svg":G("《娜佳》谵妄结构图",[{"title":"娜佳","text":"'自由精灵'（通说）","color":"main"},{"title":"巴黎街头","text":"日常与异象（B344）","color":"gold"},{"title":"自动写作","text":"超现实主义方法（B344）","color":"family"},{"title":"谵妄","text":"疯癫与诗意（通说）","color":"antagonist"}])},
{"id":wid_nongmin,"title":"农民","original_title":"Chłopi","region":"波兰","era":"近代","era_detail":"20世纪初",
"genre":"长篇小说（四卷）","genre_group":"小说","language":"波兰语","author_id":"reymont","author_name":"弗拉迪斯拉夫·莱蒙特",
"year_display":"1904-09年（Britannica B342：Chłopi 四卷出版——'won for Reymont the Nobel Prize'）","year_sort":1904,
"background":["Britannica（B342）：Chłopi（农民, 1904-09）四卷——'a chronicle of peasant life during the four seasons of a year'（一年四季农民生活的编年）。","Britannica（B342）：'Written almost entirely in peasant dialect'——几乎全用农民方言写成。","Britannica（B342）：'won for Reymont the Nobel Prize'——1924年诺奖之获奖作。"],
"outline":["四季结构：秋、冬、春、夏的村庄编年（卷次对应通说待核——B342未载卷名）。","热乌雷莫村：土地、婚姻与教堂的政治（村名与情节通说待核）。"],
"characters":[{"name":"安蒂克","identity":"青年农民","note":"（通说待核，B342未载）"},{"name":"波瑞娜","identity":"安蒂克之妻","note":"（通说待核，B342未载）"}],
"themes":["四季农事的编年体（B342）。","方言书写的农民史诗（B342：peasant dialect）。","土地与婚姻的政治（通说待核）。"],
"influence":[{"text":"Britannica：'won for Reymont the Nobel Prize'（B342）。","source":"B342"},{"text":"Britannica：1973年拍成电影（B342：filmed 1973）。","source":"B342"}],
"reading":{"difficulties":["方言译本的失落感。","波兰乡村的教会与家族结构。"],
 "editions":["《农民》中译本（人民文学等——通说待核）。","波兰文原版。"],
 "order":"波兰小说首选；可后接《福地》。"},
"pending":["四季卷名（秋/冬/春/夏）核对（B342未载卷次名）。","安蒂克/波瑞娜人名核对（B342未载）。","热乌雷莫村名待核。"],
"sources":["B342"],"year_source":"B342","author_source":"B342","related_works":rel_rey,
"svg":G("《农民》四季结构图",[{"title":"四季","text":"农事编年（B342）","color":"family"},{"title":"方言","text":"农民的语言（B342）","color":"gold"},{"title":"土地","text":"村庄的政治（通说）","color":"antagonist"},{"title":"诺奖","text":"1924（B342）","color":"main"}])},
{"id":"huangliang","title":"荒凉","original_title":"Desolación","region":"智利","era":"现当代","era_detail":"20世纪20年代",
"genre":"诗集","genre_group":"诗歌","language":"西班牙语","author_id":"gmistral","author_name":"加夫列拉·米斯特拉尔",
"year_display":"1922年（Britannica B343：Desolación (1922)——早期作品集）","year_sort":1922,
"background":["Britannica（B343）：Desolación——'A collection of her early works'，含'Dolor'——'detailing the aftermath of a love affair that was ended by the suicide'。","Britannica（B343）：米斯特拉尔主题——'love of children and of the downtrodden remained her principal themes'；风格——'warmth of feeling and emotional power'。","Britannica（B343）：1914年以'Sonetos de la muerte'（死亡十四行诗）获智利奖而成名——本集收录其成名期作品。"],
"outline":["死亡十四行诗：'Sonetos de la muerte'的挽歌体（B343：成名作——篇目收录通说待核）。","'Dolor'：因自杀而终结的爱恋及其余波（B343）。","教师之诗：对儿童与底层者的爱（B343）。"],
"characters":[{"name":"抒情'我'","identity":"教师/诗人","note":"（B343 教师出身的自传语境）"}],
"themes":["对孩子的爱（B343：love of children）。","对底层者的爱（B343：the downtrodden）。","死亡与哀悼（B343：'Sonetos de la muerte'/'Dolor' 语境）。"],
"influence":[{"text":"Britannica：1945年诺奖——首位拉美得主（B343）。","source":"B343"},{"text":"Britannica：英译者含 Langston Hughes、Ursula K. Le Guin（B343）。","source":"B343"}],
"reading":{"difficulties":["西班牙语美洲诗歌的宗教语调。","智利北部乡村背景。"],
 "editions":["《荒凉》中译本（人民文学等——通说待核）。","西班牙文原版。"],
 "order":"米斯特拉尔首选；后接《塔拉》(1938)。"},
"pending":["'Dolor'篇目细节核对。","1922年出版（ Instituto de las Españas，纽约说）待核。","'自杀'事件的传记细节待核（B343未载姓名）。"],
"sources":["B343"],"year_source":"B343","author_source":"B343","related_works":rel_mis,
"svg":G("《荒凉》挽歌结构图",[{"title":"死亡十四行","text":"成名的挽歌体（B343）","color":"main"},{"title":"Dolor","text":"爱之殇（B343）","color":"antagonist"},{"title":"儿童","text":"教师的主题（B343）","color":"gold"},{"title":"荒凉","text":"情感的暖与痛（B343）","color":"family"}])},
]
for w in works:
    assert w['id'] not in existing, f'dup {w["id"]}'
for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("reymont",wid_nongmin),("gmistral","huangliang"),("breton","najia")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B34x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH26 DONE')
