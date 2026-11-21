# -*- coding: utf-8 -*-
"""批28：Britannica 新核 2 作家 3 部（莫拉维亚x2/兰佩杜萨 B348-B349）+ 贝克特《莫洛伊》零成本（B094）"""
import json, pathlib

newsrc = [
{"id":"B348","title":"Alberto Moravia — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Alberto-Moravia","type":"百科全书","verified":True,"covers":["moravia","lengmoederen"],"note":"2026-11-21 核对：原名 Alberto Pincherle；1907-11-28罗马生—1990-09-26罗马卒（82岁）；'Italian journalist, short-story writer, and novelist known for his fictional portrayals of social alienation'；'He was a major figure in 20th-century Italian literature.'；Gli indifferenti (1929)——'a scathingly realistic study of the moral corruption of a middle-class mother and two of her children'；Agostino (1944; Two Adolescents)；La Romana (1947; The Woman of Rome)；La disubbidienza (1948)；Il conformista (1951; The Conformist)——'themes of isolation and alienation'；La ciociara (1957; Two Women)——'tells of an adaptation to post-World War II Italian life'；La noia (1960; The Empty Canvas)——'a painter unable to find meaning either in love or work'；Racconti romani (1954)、Nuovi racconti romani (1959)；妻为小说家 Elsa Morante；多部改编为电影"},
{"id":"B349","title":"Giuseppe Tomasi di Lampedusa — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Giuseppe-Tomasi-di-Lampedusa","type":"百科全书","verified":True,"covers":["lampedusa","bao"],"note":"2026-11-21 核对：1896-12-23巴勒莫（西西里）生—1957-07-23罗马卒（60岁）；帕尔马公爵与兰佩杜萨亲王，生于西西里贵族之家；一战炮兵军官，被俘关押于匈牙利后逃脱、徒步返意；精神崩溃断送外交前程，此后'an intensely private life of intellectual activity'；Il gattopardo（豹, 1958年死后出版）——'only completed novel'——'rejected by publishers during his lifetime, brought him world acclaim with its posthumous publication'——'one of the most striking in 20th-century Italian literature'——心理研究：萨利纳亲王堂·法布里奇奥目睹1860年代权力从波旁贵族移向新意大利王国与自由资产阶级，侄子投机革命并攀上新兴阶层；Racconti (1961死后)——含未完成长篇首章与自传短篇，部分译为 Two Stories and a Memory (1962)；The Siren, and Selected Writings (1995)——补论文"},
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
def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

rel_len = [rid('shuncongzhe'), rid('yigewushiwan'), rid('wuhao')]
rel_shun = [rid('lengmoederen'), rid('bao'), rid('xiniu')]
rel_bao = [rid('shuncongzhe'), rid('lengmoederen'), rid('qieelvxing')]
rel_mol = [rid('dengdaigou'), rid('chengbao'), rid('bianxingji')]
print('rel:', rel_len, rel_shun, rel_bao, rel_mol)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"moravia","name":"阿尔贝托·莫拉维亚","foreign_name":"Alberto Moravia（阿尔贝托·莫拉维亚，原名 Alberto Pincherle，1907-11-28—1990-09-26）","country":"意大利","birth":1907,"death":1990,"birth_year":1907,"death_year":1990,"era":"现当代",
"summary":"莫拉维亚，原名 Alberto Pincherle，罗马生，意大利小说家——'known for his fictional portrayals of social alienation'（以社会疏离的虚构书写著称——B348）；'He was a major figure in 20th-century Italian literature.'（B348）。Gli indifferenti（冷漠的人, 1929）——'a scathingly realistic study of the moral corruption of a middle-class mother and two of her children'（B348）；Il conformista（顺从者, 1951）——'themes of isolation and alienation'（B348）；La ciociara（两个女人/乔恰里亚女人, 1957）——'tells of an adaptation to post-World War II Italian life'（B348）；La noia（烦闷, 1960）——'a painter unable to find meaning either in love or work'（B348）。妻为小说家 Elsa Morante；多部改编为电影（B348）。",
"timeline":[
 {"year":1907,"text":"11月28日生于罗马（B348）。","src":"B348"},
 {"year":1929,"text":"处女作 Gli indifferenti——中产道德败坏的现实主义研究（B348）。","src":"B348"},
 {"year":1951,"text":"Il conformista（顺从者）——疏离与异化的主题（B348）。","src":"B348"},
 {"year":1957,"text":"La ciociara（两个女人）——战后意大利的适应（B348）。","src":"B348"},
 {"year":1990,"text":"9月26日卒于罗马（B348）。","src":"B348"}],
"major_works":[
 {"work_id":"lengmoederen","note":"1929（B348）"},
 {"work_id":"shuncongzhe","note":"1951（B348）"},
 {"title":"两个女人","note":"（B348：La ciociara (1957)——中译名两说待核）"}],
"style":["社会疏离的虚构书写（B348：social alienation）。",
 "'辛辣的现实主义'（B348：scathingly realistic）。",
 "中产阶级的道德解剖（B348）。"],
"status":"Britannica 定位莫拉维亚为20世纪意大利文学主要人物（B348）。",
"sources":["B348"],"dates_source":"B348",
"pending":["Gli indifferenti 通行译名（《冷漠的人》）待核。","与 Elsa Morante 的婚姻年份待核。","电影改编清单待核。"]},
{"id":"lampedusa","name":"朱塞佩·托马西·迪·兰佩杜萨","foreign_name":"Giuseppe Tomasi di Lampedusa（朱塞佩·托马西·迪·兰佩杜萨，帕尔马公爵、兰佩杜萨亲王，1896-12-23—1957-07-23）","country":"意大利","birth":1896,"death":1957,"birth_year":1896,"death_year":1957,"era":"现当代",
"summary":"兰佩杜萨，巴勒莫（西西里）生——帕尔马公爵、兰佩杜萨亲王，西西里贵族之家（B349）。一战炮兵军官，被俘关押匈牙利后逃脱、徒步返意（B349）；精神崩溃断送外交前程，此后'an intensely private life of intellectual activity'（B349）。Il gattopardo（豹）为其'only completed novel'——'rejected by publishers during his lifetime, brought him world acclaim with its posthumous publication'（生前被拒、死后1958年出版而举世闻名——B349）——'one of the most striking in 20th-century Italian literature'（B349）。死后另出 Racconti (1961)——含未完成长篇首章与自传短篇（B349）。",
"timeline":[
 {"year":1896,"text":"12月23日生于巴勒莫（西西里贵族之家——B349）。","src":"B349"},
 {"year":1915,"text":"一战服役为炮兵军官，被俘匈牙利、逃脱徒步返意（年份通说待核——B349未载服役年）。","src":"B349"},
 {"year":1957,"text":"7月23日卒于罗马；生前书稿被拒（B349）。","src":"B349"},
 {"year":1958,"text":"《豹》死后出版，举世闻名（B349）。","src":"B349"}],
"major_works":[
 {"work_id":"bao","note":"1958死后出版（B349）"},
 {"title":"故事集","note":"（B349：Racconti (1961死后)）"}],
"style":["贵族的挽歌视角（B349：心理研究 Don Fabrizio）。",
 "'one of the most striking in 20th-century Italian literature'（B349）。",
 " intensely private 的智性生活（B349）。"],
"status":"Britannica 定位兰佩杜萨为死后成名的西西里贵族作家，《豹》为其唯一完成的长篇（B349）。",
"sources":["B349"],"dates_source":"B349",
"pending":["一战服役年份核对（B349未载）。","《豹》出版商（Giulio Einaudi 拒稿说）待核。","Racconti 篇目细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"lengmoederen","title":"冷漠的人","original_title":"Gli indifferenti","region":"意大利","era":"现当代","era_detail":"20世纪20年代末",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"moravia","author_name":"阿尔贝托·莫拉维亚",
"year_display":"1929年（Britannica B348：Gli indifferenti (1929; Time of Indifference)）","year_sort":1929,
"background":["Britannica（B348）：'a scathingly realistic study of the moral corruption of a middle-class mother and two of her children'——对一个中产母亲与其两个孩子的道德败坏的辛辣现实主义研究。","Britannica（B348）：莫拉维亚——'known for his fictional portrayals of social alienation'。","题材（通说待核）：丧夫的中产母亲与情人周旋，子女的'冷漠'与家庭的溃散。"],
"outline":["中产母亲与两个孩子：情人的操纵与家庭的道德溃散（B348：moral corruption of a middle-class mother and two of her children；情节通说待核）。","'冷漠'作为道德瘫痪的形式（通说待核）。"],
"characters":[{"name":"玛利亚格拉齐亚","identity":"母亲","note":"（通说待核，B348未载）"},{"name":"米凯莱/卡拉","identity":"子女","note":"（通说待核，B348未载）"}],
"themes":["社会疏离（B348：social alienation）。",
 "中产的道德败坏（B348：moral corruption）。",
 "'冷漠'——行动能力的瘫痪（通说待核）。"],
"influence":[{"text":"Britannica：'He was a major figure in 20th-century Italian literature.'（B348）。","source":"B348"},{"text":"Britannica：处女作即确立其现实主义路数（B348 定位）。","source":"B348"}],
"reading":{"difficulties":["法西斯前夕的意大利中产社会（时代背景通说待核）。","'冷漠'的心理剖析。"],
 "editions":["《冷漠的人》中译本（人民文学/上海译文等——通说待核）。","意大利文原版。"],
 "order":"莫拉维亚首选；后接《顺从者》。"},
"pending":["玛利亚格拉齐亚/米凯莱/卡拉人名核对（B348未载）。","1929年出版（Alpes说）待核。","中译名两说（《冷漠的人》/《冷漠者们》）待核。"],
"sources":["B348"],"year_source":"B348","author_source":"B348","related_works":rel_len,
"svg":G("《冷漠的人》道德溃散图",[{"title":"母亲","text":"被操纵的中产（通说）","color":"family"},{"title":"子女","text":"'冷漠'的瘫痪（通说）","color":"main"},{"title":"情人","text":"道德败坏的推手（B348语境）","color":"antagonist"},{"title":"疏离","text":"社会异化（B348）","color":"gold"}])},
{"id":"shuncongzhe","title":"顺从者","original_title":"Il conformista","region":"意大利","era":"现当代","era_detail":"20世纪50年代初",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"moravia","author_name":"阿尔贝托·莫拉维亚",
"year_display":"1951年（Britannica B348：Il conformista (1951; The Conformist)）","year_sort":1951,
"background":["Britannica（B348）：Il conformista——处理'themes of isolation and alienation'（隔离与异化的主题）。","Britannica（B348）：莫拉维亚多部作品改编为电影。","题材（通说待核）：法西斯时期，一个渴望'正常'的青年接受密探任务——顺从作为逃避。"],
"outline":["'顺从者'加入体制：密探任务与内心的空洞（情节通说待核——B348未载）。","隔夜时刻的选择与崩溃（通说待核）。"],
"characters":[{"name":"马尔切洛","identity":"'顺从者'","note":"（通说待核，B348未载）"}],
"themes":["顺从即异化（B348：isolation and alienation）。",
 "法西斯时代的中产心理（通说待核）。",
 "'正常'渴望的恐怖（通说待核）。"],
"influence":[{"text":"Britannica：'themes of isolation and alienation'（B348）。","source":"B348"},{"text":"Britannica：莫拉维亚为20世纪意大利文学主要人物（B348）。","source":"B348"}],
"reading":{"difficulties":["法西斯语境（1930年代罗马——通说待核）。","心理—政治小说的双层。"],
 "editions":["《顺从者》中译本（人民文学/上海译文等——通说待核）。","意大利文原版。"],
 "order":"莫拉维亚进阶；可后接《烦闷》。"},
"pending":["马尔切洛人名与剧情细节核对（B348未载）。","1970年贝尔托鲁奇电影说待核（B348仅称'多部改编'）。","1951年出版细节待核。"],
"sources":["B348"],"year_source":"B348","author_source":"B348","related_works":rel_shun,
"svg":G("《顺从者》顺从结构图",[{"title":"'顺从者'","text":"异化的执行者（B348语境）","color":"main"},{"title":"体制","text":"法西斯的引力（通说）","color":"antagonist"},{"title":"疏离","text":"isolation and alienation（B348）","color":"gold"},{"title":"'正常'","text":"空洞的渴望（通说）","color":"family"}])},
{"id":"bao","title":"豹","original_title":"Il Gattopardo","region":"意大利","era":"现当代","era_detail":"20世纪50年代（死后出版）",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"lampedusa","author_name":"朱塞佩·托马西·迪·兰佩杜萨",
"year_display":"1958年死后出版（Britannica B349：Il gattopardo (1958, posthumous)——'only completed novel'）","year_sort":1958,
"background":["Britannica（B349）：Il gattopardo——'rejected by publishers during his lifetime, brought him world acclaim with its posthumous publication'（生前被拒、死后出版举世闻名）——'one of the most striking in 20th-century Italian literature'。","Britannica（B349）：'a psychological study of Don Fabrizio, prince of Salina'——萨利纳亲王目睹1860年代权力从波旁贵族移向新意大利王国与自由资产阶级。","Britannica（B349）：侄子投机革命并'攀上新兴阶层'（joins the revolution opportunistically and marries into the rising class）。"],
"outline":["萨利纳亲王堂·法布里奇奥的心理研究：贵族的黄昏（B349：psychological study of Don Fabrizio）。","侄子的投机与'新兴阶层'的婚姻（B349）。","1860年代：加里波第与新意大利王国（时代背景通说待核）。"],
"characters":[{"name":"堂·法布里奇奥","identity":"萨利纳亲王","note":"（B349：Don Fabrizio, prince of Salina）"},{"name":"侄子","identity":"投机者","note":"（B349：nephew——名字通说待核）"}],
"themes":["贵族的挽歌（B349：心理研究）。",
 "权力的转移：波旁→意大利王国→自由资产阶级（B349）。",
 "投机的胜利与'豹'的终结（B349 侄子线）。"],
"influence":[{"text":"Britannica：'one of the most striking in 20th-century Italian literature'（B349）。","source":"B349"},{"text":"Britannica：'only completed novel'——死后出版的传奇（B349）。","source":"B349"}],
"reading":{"difficulties":["1860年代意大利统一史（加里波第远征西西里——通说待核）。","西西里贵族的世界。"],
 "editions":["《豹》中译本（人民文学/译林等——通说待核）。","意大利文原版。"],
 "order":"兰佩杜萨唯一长篇；与《故事集》(1961)对读。"},
"pending":["侄子名（唐克雷迪说）核对（B349未载）。","1958年出版商（Feltrinelli说）待核。","1963年维斯孔蒂电影说待核。","西西里舞会开篇细节待核。"],
"sources":["B349"],"year_source":"B349","author_source":"B349","related_works":rel_bao,
"svg":G("《豹》权力转移图",[{"title":"堂·法布里奇奥","text":"贵族的黄昏（B349）","color":"main"},{"title":"侄子","text":"投机的新兴阶层（B349）","color":"antagonist"},{"title":"1860年代","text":"波旁→意大利王国（B349）","color":"gold"},{"title":"豹","text":"濒危的物种（B349意象）","color":"family"}])},
{"id":"moluoyi","title":"莫洛伊","original_title":"Molloy","region":"爱尔兰","era":"现当代","era_detail":"20世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"beckett","author_name":"萨缪尔·贝克特",
"year_display":"写成于1947-50年（作者页 B094：莫洛伊三部曲 1947—50——出版年待核）","year_sort":1947,
"background":["作者页（B094）：贝克特——英法双语写作、1969诺奖；'莫洛伊三部曲（1947—50）'——法语小说三部曲（B094 注记）。","作者页（B094）：贝克特'his most celebrated play'为《等待戈多》(1953)——小说三部曲与戏剧并置。","题材（通说待核）：莫洛伊寻找母亲/主人公寻找自我的旅程——'寻找'的解构。"],
"outline":["莫洛伊的旅程：寻找母亲（通说待核——B094未载细节）。","莫兰寻找莫洛伊的镜像任务（第二部结构通说待核）。"],
"characters":[{"name":"莫洛伊","identity":"流浪者","note":"（B094 书名人物）"},{"name":"莫兰","identity":"侦探/镜像","note":"（通说待核，B094未载）"}],
"themes":["'寻找'的自我消解（通说待核）。",
 "语言与记忆的贫困化（通说待核——B094 语境：荒诞派）。",
 "法语写作的自我转换（B094：英法双语写作）。"],
"influence":[{"text":"作者页：莫洛伊三部曲——贝克特小说代表作（B094 注记）。","source":"B094"},{"text":"作者页：1969诺奖；荒诞派戏剧代表（B094）。","source":"B094"}],
"reading":{"difficulties":["贝克特式的重复与消解。","三部曲的阅读顺序（莫洛伊→马龙之死→不可名状者——通说待核）。"],
 "editions":["《莫洛伊》中译本（湖南文艺《贝克特选集》等——通说待核）。","法文原版。"],
 "order":"贝克特小说首选；与《等待戈多》对读。"},
"pending":["出版年（1951年巴黎法文版说）待核。","莫兰人名与三部曲结构核对（B094未载细节）。","1958年英文译本（Beckett自译说）待核。"],
"sources":["B094"],"year_source":"B094","author_source":"B094","related_works":rel_mol,
"svg":G("《莫洛伊》寻找结构图",[{"title":"莫洛伊","text":"寻找母亲（通说）","color":"main"},{"title":"莫兰","text":"镜像任务（通说）","color":"family"},{"title":"寻找","text":"自我的消解（通说）","color":"gold"},{"title":"法语","text":"双语写作的转换（B094）","color":"antagonist"}])},
]
for w in works:
    assert w['id'] not in existing, f'dup {w["id"]}'
for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

# 贝克特作者页挂 moluoyi
p = pathlib.Path('data/authors/beckett.json')
j = json.loads(p.read_text(encoding='utf-8'))
if not any(m.get('work_id') == 'moluoyi' for m in j['major_works']):
    j['major_works'].append({"work_id": "moluoyi", "note": "莫洛伊三部曲之一（B094）"})
p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH28 DONE')
