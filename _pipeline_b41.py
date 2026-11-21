# -*- coding: utf-8 -*-
"""批41：Britannica 新核 2 作家 2 部（弗·米斯特拉尔/蒙森 B362-B363）"""
import json, pathlib

newsrc = [
{"id":"B362","title":"Frederic Mistral — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Frederic-Mistral","type":"百科全书","verified":True,"covers":["fmistral","mileiyi"],"note":"2026-11-21 核对：1830-09-08法国Maillane生—1914-03-25 Maillane卒（83岁）；1904诺贝尔文学奖（与埃切加赖分享——'for his contributions in literature and philology'）；领导19世纪奥克语（普罗旺斯语）复兴；1854年与友人创 Félibrige（'an association for the maintenance of the Provençal language and customs'）；20年编普罗旺斯语词典 Lou Tresor dóu Félibrige 两卷 (1878)；用诺奖奖金在阿尔勒建普罗旺斯民族志博物馆；'he is considered one of the greatest poets of France'；四首长篇叙事诗：Mirèio (1859)、Calendau (1867)、Nerto (1884)、Lou Pouèmo dóu Rose (1897)；悲剧 La Reino Jano (1890)；抒情诗两卷 Lis Isclo d'or (1876)、Lis Oulivado (1912)；回忆录 Moun espelido (1906)——'his best-known work'；'his claim to greatness rests on his first and last long poems'——两首12歌史诗；Mirèio——富农场主之女爱上穷编篮匠之子被父母阻挠、死于 Les Saintes-Maries-de-la-Mer 教堂——'skillfully combines narration, dialogue, description, and lyricism'——古诺1863年歌剧 Mireille；Lou Pouèmo dóu Rose——罗讷河航程、荷兰王子与摆渡人之女的爱情因汽船撞沉驳船而双双溺亡——'less musical and more dense in style than Mirèio...as full of life and colour'"},
{"id":"B363","title":"Theodor Mommsen — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Theodor-Mommsen","type":"百科全书","verified":True,"covers":["mommsen","luomashi"],"note":"2026-11-21 核对：1817-11-30石勒苏益格Garding生—1903-11-01柏林近郊夏洛滕堡卒（86岁差4周）；1902诺贝尔文学奖；'famous for his masterpiece, Römische Geschichte (The History of Rome)'；前三卷1854-56年出版（至塔普苏斯战役46 BC）；因萨克斯起义1849失去莱比锡教职；1852苏黎世、1854布雷斯劳、1858柏林（普鲁士科学院）；Corpus Inscriptionum Latinarum（拉丁铭文集成，1863年起）——'essential in complementing the one-sidedly literary tradition'；第五卷(1885)——帝国行省史——'No one but Mommsen could have depicted this period in so authoritative a manner'；Römisches Staatsrecht 三卷(1871-88)——'if he were to be remembered by anything, it would be by this work'；Römisches Strafrecht (1899)；'he was an artist...he used the means of poetry and enjoyed exercising his poetic talent'；Liederbuch dreier Friends (1843)与弟及施托姆合著；对恺撒的推崇与'caesarism'之讥；1873-79普鲁士邦议员、1881-84帝国议员；16子女；歌德为终生理想"},
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
{"id":"fmistral","name":"弗雷德里克·米斯特拉尔","foreign_name":"Frédéric Mistral（弗雷德里克·米斯特拉尔，1830-09-08—1914-03-25）","country":"法国","birth":1830,"death":1914,"birth_year":1830,"death_year":1914,"era":"近代",
"summary":"米斯特拉尔，法国Maillane生，普罗旺斯语诗人——1904年诺贝尔文学奖（与埃切加赖分享——'for his contributions in literature and philology'——B362）。领导19世纪奥克语复兴：1854年创 Félibrige——'an association for the maintenance of the Provençal language and customs'（B362）；20年编普罗旺斯语大词典 Lou Tresor dóu Félibrige (1878)（B362）。Mirèio（米蕾伊, 1859）——富农场主之女与穷编篮匠之子的爱情悲剧——'skillfully combines narration, dialogue, description, and lyricism'（B362）；Lou Pouèmo dóu Rose（罗讷河之歌, 1897）——两首12歌史诗为其伟大之凭（B362）。'considered one of the greatest poets of France'（B362）。",
"timeline":[
 {"year":1830,"text":"9月8日生于法国Maillane（B362）。","src":"B362"},
 {"year":1854,"text":"与友人创立 Félibrige（B362）。","src":"B362"},
 {"year":1859,"text":"Mirèio（米蕾伊）——成名史诗（B362）。","src":"B362"},
 {"year":1904,"text":"获诺贝尔文学奖（与埃切加赖分享）（B362）。","src":"B362"},
 {"year":1914,"text":"3月25日卒于Maillane（B362）。","src":"B362"}],
"major_works":[
 {"work_id":"mileiyi","note":"1859（B362）"},
 {"title":"罗讷河之歌","note":"（B362：Lou Pouèmo dóu Rose (1897)——中译名待核）"},
 {"title":"米斯特拉尔回忆录","note":"（B362：Moun espelido (1906)——'his best-known work'）"}],
"style":["奥克语（普罗旺斯语）的复兴书写（B362）。",
 "'springy, musical quality'的独创诗节（B362）。",
 "乡土史诗：把家乡倾入诗中（B362：poured his love for the countryside）。"],
"status":"Britannica 定位米斯特拉尔为1904诺奖得主、奥克语复兴的领袖、法国最伟大的诗人之一（B362）。",
"sources":["B362"],"dates_source":"B362",
"pending":["Mirèio 通行译名（《米蕾伊》/《米瑞伊》）待核。","与加·米斯特拉尔（Gabriela）无亲属关系——笔名借用说的关系待核。","Félibrige 后续史待核。"]},
{"id":"mommsen","name":"特奥多尔·蒙森","foreign_name":"Theodor Mommsen（特奥多尔·蒙森，1817-11-30—1903-11-01）","country":"德国","birth":1817,"death":1903,"birth_year":1817,"death_year":1903,"era":"近代",
"summary":"蒙森，石勒苏益格Garding生，德国历史学家——1902年诺贝尔文学奖（B363）。Römische Geschichte（罗马史）前三卷1854-56年出版——'embodied the new historical method applied to the history of Rome'（B363）；第五卷(1885)写帝国行省史——'No one but Mommsen could have depicted this period in so authoritative a manner'（B363）。主持拉丁铭文集成 Corpus Inscriptionum Latinarum (1863年起)（B363）。'he was an artist...he used the means of poetry and enjoyed exercising his poetic talent'（B363）。Römisches Staatsrecht 三卷 (1871-88)——'if he were to be remembered by anything, it would be by this work'（B363）。",
"timeline":[
 {"year":1817,"text":"11月30日生于石勒苏益格Garding（B363）。","src":"B363"},
 {"year":1854,"text":"《罗马史》前三卷出版（1854-56）（B363）。","src":"B363"},
 {"year":1858,"text":"入普鲁士科学院、柏林大学任教（B363）。","src":"B363"},
 {"year":1885,"text":"《罗马史》第五卷——帝国行省史（B363）。","src":"B363"},
 {"year":1902,"text":"获诺贝尔文学奖（B363）。","src":"B363"},
 {"year":1903,"text":"11月1日卒于夏洛滕堡（B363）。","src":"B363"}],
"major_works":[
 {"work_id":"luomashi","note":"1854-56/1885（B363）"},
 {"title":"罗马公法","note":"（B363：Römisches Staatsrecht (1871-88)三卷——中译名待核）"},
 {"title":"拉丁铭文集成","note":"（B363：Corpus Inscriptionum Latinarum，1863年起——主持）"}],
"style":["'把古代人从奥林匹斯山请下人间'（B363：come down to earth——转述）。",
 "19世纪政治社会学词汇写古代（B363）。",
 "艺术家式的历史文体（B363：he was an artist...means of poetry）。"],
"status":"Britannica 定位蒙森为1902诺奖得主、《罗马史》为其杰作、铭文学宗师（B363）。",
"sources":["B363"],"dates_source":"B363",
"pending":["《罗马史》通行译本（商务印书馆李稼年译本说）待核。","'caesarism'之讥细节待核。","诺奖授奖理由（史学家的文学奖）细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"mileiyi","title":"米蕾伊","original_title":"Mirèio","region":"法国","era":"近代","era_detail":"19世纪50年代末",
"genre":"长篇叙事诗（12歌）","genre_group":"诗歌","language":"奥克语（普罗旺斯语）","author_id":"fmistral","author_name":"弗雷德里克·米斯特拉尔",
"year_display":"1859年（Britannica B362：Mirèio (1859)——'his claim to greatness rests on his first and last long poems'）","year_sort":1859,
"background":["Britannica（B362）：Mirèio——富农场主之女爱上穷编篮匠之子，被父母阻挠——'ends with her death in the Church of Les Saintes-Maries-de-la-Mer'。","Britannica（B362）：'skillfully combines narration, dialogue, description, and lyricism'——'springy, musical quality of its highly individual stanzaic form'。","Britannica（B362）：以法文题《Mireille》启发了古诺的歌剧（1863）。"],
"outline":["米蕾伊与樊尚的爱情受阻（B362：love...thwarted by her parents；人名通说待核）。","圣马利海岸教堂的朝圣与死亡（B362：ends with her death in the Church of Les Saintes-Maries-de-la-Mer）。"],
"characters":[{"name":"米蕾伊","identity":"农场主之女","note":"（B362 书名人物）"},{"name":"樊尚","identity":"编篮匠之子","note":"（B362：a poor basketmaker's son——名通说待核）"}],
"themes":["乡土史诗（B362：set in the poet's own time and district）。",
 "爱情与门第（B362：thwarted by her parents）。",
 "普罗旺斯风物的百科（B362：poured his love for the countryside）。"],
"influence":[{"text":"Britannica：古诺歌剧 Mireille (1863)（B362）。","source":"B362"},{"text":"Britannica：1904诺奖（B362 交叉）。","source":"B362"}],
"reading":{"difficulties":["奥克语文本（读译本）。","普罗旺斯民俗与圣马利朝圣。"],
 "editions":["《米蕾伊》中译名（《米瑞伊》）待核。","奥克语原版（公有领域）。"],
 "order":"米斯特拉尔首选；与《罗讷河之歌》对读。"},
"pending":["人名（米蕾伊/樊尚——樊尚说待核）核对。","1859年出版细节待核。","12歌结构核对（B362：full-scale epics in 12 cantos）。"],
"sources":["B362"],"year_source":"B362","author_source":"B362","related_works":["xinnuofusuobaken","mengya","chengfaji"],
"svg":G("《米蕾伊》乡土史诗图",[{"title":"米蕾伊","text":"农场主之女（B362）","color":"main"},{"title":"樊尚","text":"编篮匠之子（B362）","color":"gold"},{"title":"门第","text":"父母的阻挠（B362）","color":"antagonist"},{"title":"圣马利","text":"朝圣与死亡（B362）","color":"family"}])},
{"id":"luomashi","title":"罗马史","original_title":"Römische Geschichte","region":"德国","era":"近代","era_detail":"19世纪50-80年代",
"genre":"史学著作","genre_group":"散文","language":"德语","author_id":"mommsen","author_name":"特奥多尔·蒙森",
"year_display":"1854-56/1885年（Britannica B363：前三卷1854-56——第五卷1885）","year_sort":1854,
"background":["Britannica（B363）：'famous for his masterpiece, Römische Geschichte (The History of Rome)'——前三卷1854-56——第五卷(1885)帝国行省史——'No one but Mommsen could have depicted this period in so authoritative a manner'。","Britannica（B363）：'embodied the new historical method'——批判地审视传统、拒绝启蒙派对古典时代的理想化。","Britannica（B363）：'he used the means of poetry and enjoyed exercising his poetic talent'——蒙森的文体艺术。"],
"outline":["共和国史（前三卷，至塔普苏斯战役46 BC——B363）。","帝国行省史（第五卷，1885——B363）；第四卷（皇帝史）未写——'he felt that he would not be capable of writing it in the same brilliant style'（B363）。"],
"characters":[{"name":"恺撒","identity":"被推崇的独裁者","note":"（B363：glorification of the dictator Caesar）"},{"name":"西塞罗/庞培","identity":"被贬低的对手","note":"（B363：disparagement）"}],
"themes":["新史学方法（B363：critical examination of traditions）。",
 "'去神话化'的罗马史（B363：demythologizing Roman history）。",
 "对恺撒的推崇与自由主义的张力（B363）。"],
"influence":[{"text":"Britannica：1902年诺贝尔文学奖（B363）。","source":"B363"},{"text":"Britannica：铭文集成作为学术丰碑（B363 交叉）。","source":"B363"}],
"reading":{"difficulties":["罗马共和政治制度。","19世纪史学方法的语境。"],
 "editions":["《罗马史》中译本（商务印书馆等——通说待核）。","德文原版（公有领域）。"],
 "order":"史学类首选之一；配合《罗马十二帝王传》等古典著作阅读。"},
"pending":["中译本细节核对。","第四卷未写的细节（B363已载）。","'squirearchy and the cloth'译法待核。"],
"sources":["B363"],"year_source":"B363","author_source":"B363","related_works":["yemanli","fushide","luoting"],
"svg":G("《罗马史》新史学结构图",[{"title":"罗马共和国","text":"前三卷的舞台（B363）","color":"main"},{"title":"铭文","text":"非文学史料（B363）","color":"gold"},{"title":"恺撒","text":"推崇与争议（B363）","color":"antagonist"},{"title":"文体","text":"'诗的手段'（B363）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B36x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('mileiyi','fmistral'), ('luomashi','mommsen')]:
    if wid in created:
        link(aid, wid)
print('BATCH41 DONE')
