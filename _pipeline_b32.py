# -*- coding: utf-8 -*-
"""批32：Britannica 新核 3 作家 4 部（怀特沃斯/汉姆生饥饿+大地的成长/拉克斯内斯独立的人们 B359-B361）"""
import json, pathlib

newsrc = [
{"id":"B359","title":"Patrick White — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Patrick-White","type":"百科全书","verified":True,"covers":["white","vosi"],"note":"2026-11-21 核对：1912-05-28伦敦生—1990-09-30悉尼卒（78岁）；1973诺贝尔文学奖；'White saw Australia as a country in a highly volatile process of growth and self-definition'；'His style is dense with myth, symbol, and allegory.'；'His deepest concern is for mans sense of isolation and his search for meaning.'；Voss (1957)、Riders in the Chariot (1961)、The Tree of Man (1955)——反映其'conception of Australia'——'individual, critical, poetic imagination'；Happy Valley (1939)——'showed the influence of D.H. Lawrence and Thomas Hardy'；The Solid Mandala (1966)；The Twyborn Affair (1979)；Flaws in the Glass (1981)自传；The Hanging Garden (2012死后)——'the friendship between a boy and girl in Sydney during World War II'"},
{"id":"B360","title":"Knut Hamsun — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Knut-Hamsun","type":"百科全书","verified":True,"covers":["hamsun","jihe"],"note":"2026-11-21 核对：1859-08-04挪威Lom生—1952-02-19Grimstad附近卒（92岁）；1920诺贝尔文学奖；Sult（饥饿, 1890）——'the story of a starving young writer in Norway'——半自传——'marked a clear departure from the social realism of the typical Norwegian novel of the period'——'Its refreshing viewpoint and impulsive, lyrical style had an electrifying effect on European writers.'；Mysterier (1892)；Pan (1894)——'asocial heroes'——'either was indifferent to or took an irreverent view of progress'；Victoria (1898)；Markens grøde（大地的成长, 1917）——'expresses a back-to-nature philosophy'；Paa gjengrodde stier (1949)——'in part memoir, in part self-defense'（90岁写）；二战支持德军占领挪威——战后以叛国罪拘禁、因年龄撤诉、判经济合作罚重款——'collaboration with the Nazis seriously damaged his reputation'，死后复兴；风格影响'Gorky, Thomas Mann, and Isaac Bashevis Singer'——'acknowledged him as a master'"},
{"id":"B361","title":"Halldor Laxness — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Halldor-Laxness","type":"百科全书","verified":True,"covers":["laxness","dulidemen"],"note":"2026-11-21 核对：原名 Halldór Kiljan Gudjónsson；1902-04-23雷克雅未克生—1998-02-08雷克雅未克近郊卒（95岁）；1955诺贝尔文学奖——瑞典学院'with having renewed the great narrative art of Iceland'（更新了冰岛伟大的叙事艺术）；'the most creative Icelandic writer of the 20th century'；Vefarinn mikli frá Kasmír (1927)首部重要长篇；Salka Valka (1931-32)——'deals with the plight of working people in an Icelandic fishing village'；Sjálfstætt fólk（独立的人们, 1934-35）——'the story of an impoverished farmer and his struggle to retain his economic independence'；Heimsljós (1937-40)四卷——'the struggles of a peasant poet'；Íslandsklukkan (1943-46)三部曲；Brekkukotsannáll (1957; The Fish Can Sing)；Paradísarheimt (1960)；1950年代后'more lyrical and introspective'"},
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
wid_ji = next(w for w in ['jihe','jielu','ji_e_hunger'] if w not in existing)
def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

rel_vo = [rid('xueseziwuxian'), rid('meiyougexingderen'), rid('renshu' if 'renshu' in existing else 'fushide')]
rel_ji = [rid('zenodeyishi'), rid('jihe' if wid_ji=='jihe' else None), rid('chengbao')]
rel_ji = [c for c in dict.fromkeys(rel_ji) if c in existing] or ['leiyu']
rel_dd = [rid('nongmin'), rid('qieelvxing'), rid('peideluobalamo')]
rel_du = [rid('nongmin'), rid('peideluobalamo'), rid('qieelvxing')]
print('wid_ji:', wid_ji, 'rel:', rel_vo, rel_ji, rel_dd, rel_du)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"white","name":"帕特里克·怀特","foreign_name":"Patrick White（帕特里克·怀特，1912-05-28—1990-09-30）","country":"澳大利亚","birth":1912,"death":1990,"birth_year":1912,"death_year":1990,"era":"现当代",
"summary":"怀特，伦敦生（澳大利亚作家），1973年诺贝尔文学奖（B359）——首位澳籍得主（'首位'提法B359未载——待核）。'White saw Australia as a country in a highly volatile process of growth and self-definition'（B359）；'His style is dense with myth, symbol, and allegory.'（B359）；'His deepest concern is for mans sense of isolation and his search for meaning.'（B359）。Voss (1957)、Riders in the Chariot (1961)、The Tree of Man (1955)——反映其'conception of Australia'——'individual, critical, poetic imagination'（B359）。处女作 Happy Valley (1939)——'showed the influence of D.H. Lawrence and Thomas Hardy'（B359）。",
"timeline":[
 {"year":1912,"text":"5月28日生于伦敦（B359）。","src":"B359"},
 {"year":1939,"text":"Happy Valley——处女作（B359）。","src":"B359"},
 {"year":1955,"text":"The Tree of Man（人树）（B359）。","src":"B359"},
 {"year":1957,"text":"Voss（沃斯）（B359）。","src":"B359"},
 {"year":1973,"text":"获诺贝尔文学奖（B359）。","src":"B359"},
 {"year":1990,"text":"9月30日卒于悉尼（B359）。","src":"B359"}],
"major_works":[
 {"work_id":"vosi","note":"1957（B359）"},
 {"title":"人树","note":"（B359：The Tree of Man (1955)——中译名待核）"},
 {"title":"战车上的乘客","note":"（B359：Riders in the Chariot (1961)——中译名待核）"}],
"style":["'神话、象征与寓言'的密织风格（B359）。",
 "'孤离感与意义追寻'的深层关切（B359）。",
 "澳大利亚的自我定义（B359：growth and self-definition）。"],
"status":"Britannica 定位怀特为1973年诺奖得主、澳大利亚民族想象的核心书写者（B359）。",
"sources":["B359"],"dates_source":"B359",
"pending":["'首位澳大利亚诺奖得主'提法待核（B359未载）。","Voss 剧情（探险家穿越内陆说）待核（B359未载）。","中译名（《沃斯》）待核。"]},
{"id":"hamsun","name":"克努特·汉姆生","foreign_name":"Knut Hamsun（克努特·汉姆生，1859-08-04—1952-02-19）","country":"挪威","birth":1859,"death":1952,"birth_year":1859,"death_year":1952,"era":"近代",
"summary":"汉姆生，挪威Lom生——1920年诺贝尔文学奖（B360）。Sult（饥饿, 1890）——半自传——'the story of a starving young writer in Norway'——'marked a clear departure from the social realism of the typical Norwegian novel of the period'——'Its refreshing viewpoint and impulsive, lyrical style had an electrifying effect on European writers.'（B360）。Pan (1894)——'asocial heroes'（B360）；Markens grøde（大地的成长, 1917）——'expresses a back-to-nature philosophy'（B360）。风格影响'Gorky, Thomas Mann, and Isaac Bashevis Singer'——'acknowledged him as a master'（B360）。二战支持德军占领挪威——战后以叛国罪拘禁、因年龄撤诉、判经济合作罚重款——'collaboration with the Nazis seriously damaged his reputation'（B360）。",
"timeline":[
 {"year":1859,"text":"8月4日生于挪威Lom（B360）。","src":"B360"},
 {"year":1890,"text":"Sult（饥饿）——欧洲文坛的电击效应（B360）。","src":"B360"},
 {"year":1917,"text":"Markens grøde（大地的成长）（B360）。","src":"B360"},
 {"year":1920,"text":"获诺贝尔文学奖（B360）。","src":"B360"},
 {"year":1945,"text":"战后因亲纳粹被拘禁；1952-02-19卒于Grimstad附近（B360：imprisoned as a traitor...age撤诉；卒年92岁）。","src":"B360"}],
"major_works":[
 {"work_id":"jihe","note":"1890（B360）"},
 {"work_id":"dadidechengzhang","note":"1917（B360）"},
 {"title":"潘","note":"（B360：Pan (1894)）"}],
"style":["'冲动而抒情'的风格（B360：impulsive, lyrical style）。",
 "'asocial heroes'的反英雄（B360）。",
 "归自然的哲学（B360：back-to-nature）。"],
"status":"Britannica 定位汉姆生为1920诺奖得主、影响高尔基/托马斯·曼/辛格的'大师'（B360）——并载其纳粹合作的污点（B360）。",
"sources":["B360"],"dates_source":"B360",
"pending":["'欧洲作家的电击效应'具体影响对象待核（B360仅载高尔基/曼/辛格承认）。","拘禁与罚金细节待核（B360口径）。","中译名（《饥饿》）待核。"]},
{"id":"laxness","name":"哈尔多尔·拉克斯内斯","foreign_name":"Halldór Laxness（哈尔多尔·拉克斯内斯，原名 Halldór Kiljan Gudjónsson，1902-04-23—1998-02-08）","country":"冰岛","birth":1902,"death":1998,"birth_year":1902,"death_year":1998,"era":"现当代",
"summary":"拉克斯内斯，雷克雅未克生，冰岛小说家——1955年诺贝尔文学奖（B361）——瑞典学院'with having renewed the great narrative art of Iceland'（更新了冰岛伟大的叙事艺术——B361）；'the most creative Icelandic writer of the 20th century'（B361）。Sjálfstætt fólk（独立的人们, 1934-35）——'the story of an impoverished farmer and his struggle to retain his economic independence'（B361）；Salka Valka (1931-32)——'deals with the plight of working people in an Icelandic fishing village'（B361）；Heimsljós (1937-40) 四卷（B361）；Íslandsklukkan（冰岛之钟, 1943-46）三部曲（B361）。1950年代后'more lyrical and introspective'（B361）。",
"timeline":[
 {"year":1902,"text":"4月23日生于雷克雅未克（B361）。","src":"B361"},
 {"year":1934,"text":"Sjálfstætt fólk（独立的人们, 1934-35）（B361）。","src":"B361"},
 {"year":1955,"text":"获诺贝尔文学奖（B361）。","src":"B361"},
 {"year":1998,"text":"2月8日卒于雷克雅未克近郊（B361）。","src":"B361"}],
"major_works":[
 {"work_id":"dulidemen","note":"1934-35（B361）"},
 {"title":"冰岛之钟","note":"（B361：Íslandsklukkan (1943-46)——三部曲）"},
 {"title":"会唱歌的鱼","note":"（B361：Brekkukotsannáll (1957; The Fish Can Sing)——中译名待核）"}],
"style":["'更新了冰岛伟大的叙事艺术'（B361：诺奖引语）。",
 "穷苦渔村与农庄的现实主义（B361）。",
 "晚期的抒情与内省（B361：more lyrical and introspective）。"],
"status":"Britannica 定位拉克斯内斯为'20世纪冰岛最具创造力的作家'、1955诺奖得主（B361）。",
"sources":["B361"],"dates_source":"B361",
"pending":["Sjálfstætt fólk 通行译名（《独立的人们》）待核。","'冰岛之钟'三部曲卷名待核。","1955诺奖授奖词全文待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"vosi","title":"沃斯","original_title":"Voss","region":"澳大利亚","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"white","author_name":"帕特里克·怀特",
"year_display":"1957年（Britannica B359：Voss (1957)——与《人树》《战车上的乘客》并列为'conception of Australia'之作）","year_sort":1957,
"background":["Britannica（B359）：Voss、Riders in the Chariot、The Tree of Man——怀特'conception of Australia'的反映——'individual, critical, poetic imagination'。","Britannica（B359）：'White saw Australia as a country in a highly volatile process of growth and self-definition'。","Britannica（B359）：'His style is dense with myth, symbol, and allegory.'；'His deepest concern is for mans sense of isolation and his search for meaning.'"],
"outline":["（通说待核——B359未载剧情）探险家沃斯率队穿越澳大利亚内陆的幻觉之旅。","（通说待核）内陆荒野与书信中的灵魂对话。"],
"characters":[{"name":"沃斯","identity":"探险家","note":"（B359 书名人物——细节通说待核）"},{"name":"劳拉","identity":"书信对方","note":"（通说待核，B359未载）"}],
"themes":["澳大利亚的自我定义（B359）。",
 "孤离感与意义追寻（B359：mans sense of isolation and his search for meaning）。",
 "神话、象征与寓言（B359：dense with myth, symbol, and allegory）。"],
"influence":[{"text":"Britannica：1973年诺贝尔文学奖（B359）。","source":"B359"},{"text":"Britannica：'individual, critical, poetic imagination'（B359）。","source":"B359"}],
"reading":{"difficulties":["神话—象征的密织文体（B359）。","19世纪殖民探险史（通说待核）。"],
 "editions":["《沃斯》中译本（人民文学/译林等——通说待核）。","英文原版。"],
 "order":"怀特首选；后接《人树》。"},
"pending":["沃斯/劳拉人名核对（B359未载细节）。","剧情概要核对（探险家穿越内陆说——通说）。","1957年出版（Viking说）待核。"],
"sources":["B359"],"year_source":"B359","author_source":"B359","related_works":rel_vo,
"svg":G("《沃斯》内陆之旅图",[{"title":"探险队","text":"穿越内陆（通说）","color":"main"},{"title":"荒野","text":"民族的自我定义（B359）","color":"gold"},{"title":"孤离","text":"'意义追寻'（B359）","color":"family"},{"title":"书信","text":"灵魂的对话（通说）","color":"antagonist"}])},
{"id":wid_ji,"title":"饥饿","original_title":"Sult","region":"挪威","era":"近代","era_detail":"19世纪80年代末",
"genre":"长篇小说","genre_group":"小说","language":"挪威语","author_id":"hamsun","author_name":"克努特·汉姆生",
"year_display":"1890年（Britannica B360：Sult (Hunger, 1890)——半自传）","year_sort":1890,
"background":["Britannica（B360）：'the story of a starving young writer in Norway'——半自传。","Britannica（B360）：'marked a clear departure from the social realism of the typical Norwegian novel of the period'——与当时挪威小说的社会现实主义决裂。","Britannica（B360）：'Its refreshing viewpoint and impulsive, lyrical style had an electrifying effect on European writers.'"],
"outline":["饥饿中的年轻作家在城市街头流浪：身体与理智的滑坡（B360：story of a starving young writer in Norway；城市名克里斯蒂安尼亚说通说待核）。","冲动而抒情的第一人称独白（B360：impulsive, lyrical style）。"],
"characters":[{"name":"无名作家","identity":"'我'","note":"（B360：starving young writer——半自传）"}],
"themes":["饥饿的身体政治（B360）。",
 "'我'的冲动与自我欺骗（B360：impulsive style 语境）。",
 "与社会现实主义的决裂（B360）。"],
"influence":[{"text":"Britannica：'had an electrifying effect on European writers'（B360）。","source":"B360"},{"text":"Britannica：高尔基、托马斯·曼、辛格'acknowledged him as a master'（B360）。","source":"B360"}],
"reading":{"difficulties":["饥饿中的心理谵妄。","19世纪90年代奥斯陆（克里斯蒂安尼亚）背景（通说待核）。"],
 "editions":["《饥饿》中译本（人民文学/上海译文等——通说待核）。","挪威文原版。"],
 "order":"汉姆生首选；后接《大地的成长》。"},
"pending":["城市名（克里斯蒂安尼亚说）核对（B360未载）。","1890年出版（Nielsen & Lydvo说）待核。","半自传细节核对（B360口径）。"],
"sources":["B360"],"year_source":"B360","author_source":"B360","related_works":rel_ji,
"svg":G("《饥饿》身体滑坡图",[{"title":"'我'","text":"饥饿的作家（B360）","color":"main"},{"title":"街头","text":"城市的流浪（通说）","color":"family"},{"title":"谵妄","text":"冲动的独白（B360）","color":"gold"},{"title":"现实主义","text":"被决裂的传统（B360）","color":"antagonist"}])},
{"id":"dadidechengzhang","title":"大地的成长","original_title":"Markens grøde","region":"挪威","era":"近代","era_detail":"20世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"挪威语","author_id":"hamsun","author_name":"克努特·汉姆生",
"year_display":"1917年（Britannica B360：Markens grøde (Growth of the Soil, 1917)）","year_sort":1917,
"background":["Britannica（B360）：'expresses a back-to-nature philosophy'（表达'归自然'的哲学）。","Britannica（B360）：本作发表三年后（1920）获诺贝尔文学奖（'Won the Nobel Prize for Literature in 1920'——B360 语境）。","题材（通说待核）：拓荒者艾萨克在荒原开垦——土地与生育的史诗。"],
"outline":["（通说待核——B360未载剧情）拓荒者与荒原：开垦、婚姻与生育。","（通说待核）现代性的侵入：矿线与金钱。"],
"characters":[{"name":"艾萨克","identity":"拓荒者","note":"（通说待核，B360未载）"},{"name":"英格尔","identity":"妻子","note":"（通说待核，B360未载）"}],
"themes":["'归自然'哲学（B360：back-to-nature）。",
 "土地与生育的史诗（通说待核）。",
 "对进步的'漠然或不敬'（B360：indifferent to or took an irreverent view of progress——Pan 语境延伸）。"],
"influence":[{"text":"Britannica：1920年诺贝尔文学奖（B360）。","source":"B360"},{"text":"Britannica：'back-to-nature philosophy'（B360）。","source":"B360"}],
"reading":{"difficulties":["挪威荒原农耕社会。","与《饥饿》的文风对比。"],
 "editions":["《大地的成长》中译本（人民文学等——通说待核）。","挪威文原版。"],
 "order":"汉姆生进阶；与《饥饿》对读。"},
"pending":["艾萨克/英格尔人名核对（B360未载）。","剧情细节核对（通说）。","1920诺奖授奖理由与本作的关系待核。"],
"sources":["B360"],"year_source":"B360","author_source":"B360","related_works":rel_dd,
"svg":G("《大地的成长》垦荒图",[{"title":"荒原","text":"归自然（B360）","color":"gold"},{"title":"拓荒者","text":"开垦与生育（通说）","color":"main"},{"title":"现代性","text":"'不敬'的进步（B360）","color":"antagonist"},{"title":"大地","text":"生育的史诗（通说）","color":"family"}])},
{"id":"dulidemen","title":"独立的人们","original_title":"Sjálfstætt fólk","region":"冰岛","era":"现当代","era_detail":"20世纪30年代",
"genre":"长篇小说（两部）","genre_group":"小说","language":"冰岛语","author_id":"laxness","author_name":"哈尔多尔·拉克斯内斯",
"year_display":"1934-35年（Britannica B361：Sjálfstætt fólk (Independent People, 1934-35)）","year_sort":1934,
"background":["Britannica（B361）：'the story of an impoverished farmer and his struggle to retain his economic independence'（一个赤贫农夫与其保持经济独立的斗争）。","Britannica（B361）：拉克斯内斯——1955诺奖——瑞典学院'with having renewed the great narrative art of Iceland'；'the most creative Icelandic writer of the 20th century'。","Britannica（B361）：同期 Salka Valka (1931-32)——'deals with the plight of working people in an Icelandic fishing village'。"],
"outline":["赤贫农夫的'独立'之战：羊、债与家庭（B361：struggle to retain his economic independence；人名通说待核）。","'独立'的代价：孤傲与失去（通说待核）。"],
"characters":[{"name":"比约尔图·科勒克","identity":"农夫","note":"（通说待核，B361未载）"}],
"themes":["经济独立的执念（B361）。",
 "冰岛农庄的生存史诗（B361 语境）。",
 "孤傲的悲剧（通说待核）。"],
"influence":[{"text":"Britannica：1955诺奖——'renewed the great narrative art of Iceland'（B361）。","source":"B361"},{"text":"Britannica：'the most creative Icelandic writer of the 20th century'（B361）。","source":"B361"}],
"reading":{"difficulties":["冰岛农庄经济与氏族记忆。","'独立'的反讽结构（通说待核）。"],
 "editions":["《独立的人们》中译本（人民文学等——通说待核）。","冰岛文原版。"],
 "order":"拉克斯内斯首选；后接《冰岛之钟》。"},
"pending":["农夫名（比约尔图·科勒克说）核对（B361未载）。","两部结构（'独立之诗'与'财产之诗'说）待核。","1934-35出版细节待核。"],
"sources":["B361"],"year_source":"B361","author_source":"B361","related_works":rel_du,
"svg":G("《独立的人们》荒原独立图",[{"title":"农夫","text":"'独立'之战（B361）","color":"main"},{"title":"荒原","text":"冰岛的生存（B361语境）","color":"family"},{"title":"债","text":"独立的代价（通说）","color":"antagonist"},{"title":"叙事艺术","text":"'更新'的诺奖辞（B361）","color":"gold"}])},
]
for w in works:
    if w['id'] in existing:
        print('skip existing', w['id'])
for w in works:
    if w['id'] in existing:
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("white","vosi"),("hamsun",wid_ji),("hamsun","dadidechengzhang"),("laxness","dulidemen")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B35x/B36x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH32 DONE')
