# -*- coding: utf-8 -*-
"""批76：Britannica 新核 2 作家 3 部（瓦雷里 B405×2/韦尔蒂 B406）+ 零成本 热内《女仆》(B400)"""
import json, pathlib

newsrc = [
{"id":"B405","title":"Paul Valery — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Paul-Valery","type":"百科全书","verified":True,"covers":["valery","haibinmuyuan"],"note":"2026-11-21 核对：全名 Ambroise-Paul-Toussaint-Jules Valéry；1871-10-30法国塞特生—1945-07-20巴黎卒（73岁，国葬）；La Jeune Parque（年轻的命运女神, 1917）——'His greatest poem is considered La Jeune Parque'——三女神中最年轻者的意识觉醒——黎明的海边在'永葆宁谧的不朽'与'拥抱人世'之间犹疑——历时五年完成；Le Cimetière marin（海滨墓园, 1920，收入 Charmes (1922)）——塞特墓地（今葬于此）——'broods by the sea at noon on Being and Not-Being, on the living and the dead'（正午在海上沉思存在与不存在、生者与死者）；Monsieur Teste（泰斯特先生, 1896）——'an almost disembodied intellect who knows but two values, the possible and the impossible'（几乎脱离肉体的智性——只知可能与不可能两值）；纯诗——'free of message'探语言的音乐本质；'rise at dawn each day, meditate for several hours on scientific method, consciousness, and the nature of language'（每天黎明即起、默想数小时）；笔记'later to be published as the famous Cahiers'；1925法兰西学院；1937法兰西公学院诗学教授；La Soirée avec Monsieur Teste (1896)；'La Crise de l'esprit' (1919)"},
{"id":"B406","title":"Eudora Welty — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Eudora-Welty","type":"百科全书","verified":True,"covers":["welty","leguanzhe"],"note":"2026-11-21 核对：1909-04-13密西西比州杰克逊生—2001-07-23杰克逊卒（92岁）；美国短篇作家；'Why I Live at the P.O.'——'a comic monologue about a young woman escaping her eccentric family'（页面问答口径）——A Curtain of Green (1941, 扩1979)中'两篇被选集最多'之一；The Optimist's Daughter (1972)——'won a Pulitzer Prize'（普利策奖）；Delta Wedding (1946)——首部长篇；A Curtain of Green (1941)；The Robber Bridegroom (1942)；The Golden Apples (1949)；The Ponder Heart (1954)；Losing Battles (1970)；One Writer's Beginnings (1984)——哈佛讲座自传；普利策奖+1980总统自由勋章；'Welty's first short story was published in 1936'；摄影是终生爱好"},
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

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"valery","name":"保尔·瓦雷里","foreign_name":"Paul Valéry（保尔·瓦雷里，全名 Ambroise-Paul-Toussaint-Jules Valéry，1871-10-30—1945-07-20）","country":"法国","birth":1871,"death":1945,"birth_year":1871,"death_year":1945,"era":"近代",
"summary":"瓦雷里，法国塞特生，诗人——La Jeune Parque（年轻的命运女神, 1917）——'His greatest poem is considered La Jeune Parque'（被认为其最伟大的诗——B405）——三女神中最年轻者的意识觉醒、黎明海边的犹疑——历时五年完成（B405）。Le Cimetière marin（海滨墓园, 1920，收入 Charmes (1922)）——'broods by the sea at noon on Being and Not-Being, on the living and the dead'（正午在海上沉思存在与不存在——B405）——塞特墓地（今葬于此）。Monsieur Teste（泰斯特先生, 1896）——'an almost disembodied intellect who knows but two values, the possible and the impossible'（B405）。纯诗——'free of message'探语言的音乐本质（B405）。'rise at dawn each day, meditate for several hours'（B405）。1925法兰西学院、1937法兰西公学院诗学教授、国葬（B405）。",
"timeline":[
 {"year":1871,"text":"10月30日生于法国塞特（B405）。","src":"B405"},
 {"year":1896,"text":"La Soirée avec Monsieur Teste（与泰斯特先生夜谈）（B405）。","src":"B405"},
 {"year":1917,"text":"La Jeune Parque——五年写就的'最伟大之诗'（B405）。","src":"B405"},
 {"year":1925,"text":"入选法兰西学院（B405）。","src":"B405"},
 {"year":1945,"text":"7月20日卒于巴黎——国葬（B405）。","src":"B405"}],
"major_works":[
 {"work_id":"haibinmuyuan","note":"1920（B405，收入 Charmes 1922）"},
 {"work_id":"mingyunvshen","note":"1917（B405）"},
 {"title":"泰斯特先生","note":"（B405：Monsieur Teste (1896)——中译名待核）"}],
"style":["'纯诗'：'free of message'探语言的音乐本质（B405）。",
 "'黎明即起、默想数小时'的智性生活（B405）。",
 "《海滨墓园》的正午沉思（B405：Being and Not-Being）。"],
"status":"Britannica 定位瓦雷里为'纯诗'理论家与实践者、La Jeune Parque 为其最伟大之诗（B405）。",
"sources":["B405"],"dates_source":"B405",
"pending":["《海滨墓园》通行译名待核。","La Jeune Parque 通行译名（《年轻的命运女神》）待核。","《 Cahiers 》笔记（B405：famous Cahiers）出版细节待核。"]},
{"id":"welty","name":"尤多拉·韦尔蒂","foreign_name":"Eudora Welty（尤多拉·韦尔蒂，1909-04-13—2001-07-23）","country":"美国","birth":1909,"death":2001,"birth_year":1909,"death_year":2001,"era":"现当代",
"summary":"韦尔蒂，密西西比州杰克逊生（卒于同地，92岁），美国短篇作家（B406）。'Why I Live at the P.O.'——'a comic monologue about a young woman escaping her eccentric family'（页面问答口径）——A Curtain of Green (1941)中'两篇被选集最多'之一（B406）。The Optimist's Daughter (1972)——'won a Pulitzer Prize'（普利策奖——B406）。Delta Wedding (1946)——首部长篇（B406）。普利策奖+1980总统自由勋章（B406）；'Welty's first short story was published in 1936'（B406）；摄影是终生爱好（B406）。",
"timeline":[
 {"year":1909,"text":"4月13日生于密西西比州杰克逊（B406）。","src":"B406"},
 {"year":1936,"text":"首篇短篇发表（B406）。","src":"B406"},
 {"year":1941,"text":"A Curtain of Green——短篇集（B406）。","src":"B406"},
 {"year":1972,"text":"《乐观者的女儿》——普利策奖（B406）。","src":"B406"},
 {"year":2001,"text":"7月23日卒于杰克逊（B406）。","src":"B406"}],
"major_works":[
 {"work_id":"leguanzhe","note":"1972普利策奖（B406）"},
 {"title":"绿幕","note":"（B406：A Curtain of Green (1941)——中译名待核）"},
 {"title":"德尔塔婚礼","note":"（B406：Delta Wedding (1946)——首部长篇——中译名待核）"}],
"style":["密西西比小镇的'喜剧独白'（B406：Why I Live at the P.O.——页面问答口径）。",
 "'短篇作家'的集中营式观察（B406：American short-story writer）。",
 "摄影的终生爱好（B406：photography remained a lifelong interest）。"],
"status":"Britannica 定位韦尔蒂为美国短篇作家、普利策奖得主（B406）。",
"sources":["B406"],"dates_source":"B406",
"pending":["《乐观者的女儿》通行译名待核。","'Why I Live at the P.O.'描述（页面问答口径）核对。","1980总统自由勋章（B406已载）核对。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

S_GE = src_of('genet')
works = [
{"id":"haibinmuyuan","title":"海滨墓园","original_title":"Le Cimetière marin","region":"法国","era":"近代","era_detail":"20世纪20年代",
"genre":"长诗","genre_group":"诗歌","language":"法语","author_id":"valery","author_name":"保尔·瓦雷里",
"year_display":"1920年（Britannica B405：Le Cimetière marin (1920)——收入 Charmes (1922)）","year_sort":1920,
"background":["Britannica（B405）：'broods by the sea at noon on Being and Not-Being, on the living and the dead'（正午在海上沉思存在与不存在、生者与死者）。","Britannica（B405）：塞特墓地——瓦雷里今葬于此（B405）。","Britannica（B405）：瓦雷里——'纯诗'——'free of message'探语言的音乐本质。"],
"outline":["（通说待核——B405未载诗节）'正午'的静止与风的'完整'。","（通说待核）'起风了！……必须试着活下去'（不采为引文）。"],
"characters":[{"name":"冥想者'我'","identity":"墓园的沉思者","note":"（B405 语境）"}],
"themes":["'存在与不存在、生者与死者'（B405：Being and Not-Being...）。",
 "'纯诗'的巅峰实践（B405：free of message）。",
 "塞特的自传地（B405：今葬于此）。"],
"influence":[{"text":"Britannica：收入 Charmes (1922)（B405）。","source":"B405"},{"text":"Britannica：1925法兰西学院、国葬（B405 交叉）。","source":"B405"}],
"reading":{"difficulties":["十节的正午'静'结构（通说待核）。","'纯诗'的音乐性。"],
 "editions":["《海滨墓园》中译本（人民文学/卞之琳译本说——通说待核）。","法文原版（公有领域状态待核）。"],
 "order":"瓦雷里首选；与《年轻的命运女神》对读。"},
"pending":["诗节结构与'风'转折核对（通说）。","1920年发表（《南方手册》说）待核。","卞之琳译本细节待核。"],
"sources":["B405"],"year_source":"B405","author_source":"B405","related_works":["mingyunvshen","diyuzhiji","wuguigu"],
"svg":G("《海滨墓园》正午沉思图",[{"title":"正午","text":"'存在与不存在'（B405）","color":"gold"},{"title":"墓园","text":"塞特的自传地（B405）","color":"main"},{"title":"风","text":"'必须活着'的转折（通说）","color":"family"},{"title":"纯诗","text":"语言的音乐（B405）","color":"antagonist"}])},
{"id":"mingyunvshen","title":"年轻的命运女神","original_title":"La Jeune Parque","region":"法国","era":"近代","era_detail":"20世纪10年代末",
"genre":"长诗","genre_group":"诗歌","language":"法语","author_id":"valery","author_name":"保尔·瓦雷里",
"year_display":"1917年（Britannica B405：La Jeune Parque (1917; The Young Fate)——'His greatest poem is considered La Jeune Parque'）","year_sort":1917,
"background":["Britannica（B405）：'His greatest poem is considered La Jeune Parque (1917; The Young Fate)'——三女神中最年轻者的意识觉醒——黎明的海边在'永葆宁谧的不朽'与'拥抱人世'之间犹疑——历时五年完成。","Britannica（B405）：瓦雷里——'rise at dawn each day, meditate for several hours on scientific method, consciousness, and the nature of language'。","题材（通说待核）：512行的'意识'独白（行数通说待核）。"],
"outline":["（通说待核）黎明海边的女神：不朽与人世之间的犹疑（B405：hesitates by the sea at dawn）。","（通说待核）'意识'觉醒的自白（B405：consciousness awakening）。"],
"characters":[{"name":"年轻的命运女神","identity":"犹疑者","note":"（B405 书名人物——the youngest of the three Fates）"}],
"themes":["'意识在沉思欲望与行动意志之间的张力'（B405：the tension within the human consciousness...）。",
 "'历时五年'（B405）。",
 "'古典形式'的现代智性（B405：always classical in form）。"],
"influence":[{"text":"Britannica：'His greatest poem is considered La Jeune Parque'（B405）。","source":"B405"},{"text":"Britannica：'variations on the theme of the tension...'（B405）。","source":"B405"}],
"reading":{"difficulties":["512行的'意识'独白（行数通说待核）。","'命运女神'神话底本。"],
 "editions":["《年轻的命运女神》中译名（《命运女神》）待核。","法文原版（公有领域状态待核）。"],
 "order":"瓦雷里进阶；先读《海滨墓园》。"},
"pending":["行数（512行说）核对（通说）。","1917年出版（NRF说）待核。","'五年完成'核对（B405已载）。"],
"sources":["B405"],"year_source":"B405","author_source":"B405","related_works":["haibinmuyuan","xuboliweng","ezhihua"],
"svg":G("《年轻的命运女神》犹疑结构图",[{"title":"女神","text":"黎明的犹疑（B405）","color":"main"},{"title":"不朽","text":"宁谧的诱惑（B405）","color":"family"},{"title":"人世","text":"拥抱的冲动（B405）","color":"gold"},{"title":"意识","text":"张力的变奏（B405）","color":"antagonist"}])},
{"id":"leguanzhe","title":"乐观者的女儿","original_title":"The Optimist's Daughter","region":"美国","era":"现当代","era_detail":"20世纪70年代初",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"welty","author_name":"尤多拉·韦尔蒂",
"year_display":"1972年（Britannica B406：The Optimist's Daughter (1972)——'won a Pulitzer Prize'）","year_sort":1972,
"background":["Britannica（B406）：The Optimist's Daughter——'won a Pulitzer Prize'（普利策奖）。","Britannica（B406）：韦尔蒂——密西西比州杰克逊——'American short-story writer'；1980总统自由勋章。","题材（通说待核）：'乐观者'法官之死的归乡——继母与故友的和解。"],
"outline":["（通说待核）贝基·麦凯尔瓦法官之死与劳雷尔的返乡。","（通说待核）'乐观者'：父亲的绰号与女儿的成长。"],
"characters":[{"name":"劳雷尔","identity":"设计师/女儿","note":"（通说待核，B406未载）"},{"name":"法官麦凯尔瓦","identity":"'乐观者'父亲","note":"（通说待核）"}],
"themes":["'乐观者'与丧亲（书名语境——通说待核）。",
 "密西西比小镇（B406：Jackson 语境）。",
 "'亲子的纽带、爱与悲伤'（页面问答口径——通说待核）。"],
"influence":[{"text":"Britannica：'won a Pulitzer Prize'（B406）。","source":"B406"},{"text":"Britannica：1980总统自由勋章（B406 交叉）。","source":"B406"}],
"reading":{"difficulties":["南方方言的幽默。","'丧亲'的心理层次。"],
 "editions":["《乐观者的女儿》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"韦尔蒂长篇首选；与《绿幕》对读。"},
"pending":["劳雷尔人名核对（通说）。","1972年出版细节待核。","'普利策奖'（B406已载）核对。"],
"sources":["B406"],"year_source":"B406","author_source":"B406","related_works":["leguanzhe" if False else "leiyu","hunlidechengyuan","xinshigudeLieshou"],
"svg":G("《乐观者的女儿》丧亲结构图",[{"title":"父亲","text":"'乐观者'的死（通说）","color":"antagonist"},{"title":"劳雷尔","text":"返乡的女儿（通说）","color":"main"},{"title":"继母","text":"荒唐的房东（通说）","color":"gold"},{"title":"普利策","text":"1972（B406）","color":"family"}])},
{"id":"nvpu","title":"女仆","original_title":"Les Bonnes","region":"法国","era":"近代","era_detail":"20世纪40年代",
"genre":"戏剧","genre_group":"戏剧","language":"法语","author_id":"genet","author_name":"让·热内",
"year_display":"1947年（Britannica B400：Les Bonnes (1947)——'Theatre of Hatred'）","year_sort":1947,
"background":["Britannica（B400）：Les Bonnes (1947)——作品列表；'This Theatre of Hatred attempts to wrest the maximum dramatic power from a social or political situation'（'憎恨的剧场'——从社会或政治情境中榨取最大的戏剧力量）。","Britannica（B400）：热内——'a French criminal and social outcast turned writer'。","题材（通说待核）：两女仆扮演'夫人'的仪式戏——克莱尔与索朗日的谋杀排演（原型帕潘姐妹案——通说待核）。"],
"outline":["（通说待核）'夫人'与'女仆'的角色互换仪式。","（通说待核）'茶'与毒药的谋杀排演。"],
"characters":[{"name":"克莱尔/索朗日","identity":"两女仆","note":"（通说待核，B400未载）"},{"name":"夫人","identity":"被扮演者","note":"（通说待核）"}],
"themes":["'憎恨的剧场'（B400：Theatre of Hatred）。",
 "角色互换的仪式（通说待核）。",
 "仆与主的戏中戏（通说待核）。"],
"influence":[{"text":"Britannica：'Theatre of Hatred'（B400）。","source":"B400"},{"text":"Britannica：'criminal and social outcast turned writer'（B400 作者级）。","source":"B400"}],
"reading":{"difficulties":["'仪式戏'的结构。","帕潘姐妹案原型（通说待核）。"],
 "editions":["《女仆》中译本（人民文学《热内戏剧集》等——通说待核）。","法文原版。"],
 "order":"热内戏剧首选；与《鲜花圣母》对读。"},
"pending":["克莱尔/索朗日人名核对（通说）。","1947年首演细节待核。","帕潘姐妹案原型待核。"],
"sources":["B400"],"year_source":"B400","author_source":"B400","related_works":["xianhuashengmu","yuwanghaojieche","leiyu"],
"svg":G("《女仆》仪式戏结构图",[{"title":"互换","text":"夫人的扮演（通说）","color":"main"},{"title":"憎恨","text":"'憎恨的剧场'（B400）","color":"gold"},{"title":"毒茶","text":"排演的谋杀（通说）","color":"antagonist"},{"title":"仪式","text":"夜夜的重复（通说）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B40x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('haibinmuyuan','valery'), ('mingyunvshen','valery'), ('leguanzhe','welty'), ('nvpu','genet')]:
    if wid in created:
        link(aid, wid)
print('BATCH76 DONE')
