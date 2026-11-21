# -*- coding: utf-8 -*-
"""批51：Britannica 新核 3 作家 3 部（埃切加赖 B369/加尔多斯 B370/品达 B371）"""
import json, pathlib

newsrc = [
{"id":"B369","title":"Jose Echegaray y Eizaguirre — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jose-Echegaray-y-Eizaguirre","type":"百科全书","verified":True,"covers":["echegaray","fengzihuaishengt"],"note":"2026-11-21 核对：1832-04-19马德里生—1916-09-04马德里卒（84岁）；1904诺贝尔文学奖（与普罗旺斯诗人弗雷德里克·米斯特拉尔分享——B362 交叉）；'was a mathematician, statesman, and the leading Spanish dramatist of the last quarter of the 19th century.'；数学教授出身、1868年入政府、1874年任财政部长并参与创办西班牙银行；第一部剧 El libro talonario (1874)——42岁才上演；此后平均'一年两部'；O locura o santidad (1877; Madman or Saint)——'he showed that honesty is condemned as madness by society'；'His early work is almost wholly Romantic'；'In all his plays his manner is melodramatic.'；后期受易卜生影响写' thesis drama'、常用讽刺反转；舞台效果'helped revolutionize Spanish theatre'"},
{"id":"B370","title":"Benito Perez Galdos — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Benito-Perez-Galdos","type":"百科全书","verified":True,"covers":["galdos","fortunata"],"note":"2026-11-21 核对：1843-05-10拉斯帕尔马斯（加那利群岛）生—1920-01-04马德里卒（76岁）；'regarded as the greatest Spanish novelist since Miguel de Cervantes'（塞万提斯之后最伟大的西班牙小说家）；'earned him comparison with Honoré de Balzac and Charles Dickens'；'perfected the Spanish realistic novel and innovatively recreated Spain's 19th-century history'；首作 La fontana de oro (1870)；Episodios nacionales（民族轶事）46部历史小说系列 (1873-1912)——写1805-1874；Doña Perfecta (1876)；La desheredada (1881)；Fortunata y Jacinta (1886-87)——'a study of two unhappily married women from different social classes'——四卷——'a paradigm of Spanish realism'——'Madrid's social spectrum through the lives of two women and a wealthy bourgeois'——被称为其杰作（masterpiece）；Nazarín (1895)；Misericordia (1897)；另有20余部戏剧"},
{"id":"B371","title":"Pindar — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Pindar","type":"百科全书","verified":True,"covers":["pindar","shenglisong"],"note":"2026-11-21 核对：约前518生于彼奥提亚Cynoscephalae——卒于前446后（约前438），阿尔戈斯（古代传说称80岁卒于彼）；'ancient Greece's greatest lyric poet and master of epinicia'（竞技凯歌大师）；竞技凯歌（epinicia）——颂皮提亚/奥林匹克/地峡/尼米亚四大赛会优胜者；古代17卷存其诗——唯竞技凯歌四卷完整传世（或因2世纪用作教科书）——共44首，按赛会分卷；风格：神话叙事、对僭妄（hubris）的道德训诫、多变格律（'no two odes alike'）、'Pindaric flights'（品达式急转）；科林娜劝其神话'少用'——'to sow with the hand and not with the whole sack'；贵族法则以荷马名言'summed up in a famous line of Homer, ever to excel and to surpass other men'；相信诗比雕像更能保存名声；fragment 76 赞雅典——该城授其特殊荣誉"},
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
{"id":"echegaray","name":"何塞·埃切加赖","foreign_name":"José Echegaray y Eizaguirre（何塞·埃切加赖·埃萨吉雷，1832-04-19—1916-09-04）","country":"西班牙","birth":1832,"death":1916,"birth_year":1832,"death_year":1916,"era":"近代",
"summary":"埃切加赖，马德里生，数学家、政治家与剧作家——'the leading Spanish dramatist of the last quarter of the 19th century'（19世纪最后25年西班牙最重要的剧作家——B369）；1904年诺贝尔文学奖（与弗雷德里克·米斯特拉尔分享——B369；B362 交叉）。数学教授出身，1868年入政府，1874年任财政部长并参与创办西班牙银行（B369）。第一部剧 El libro talonario (1874)——42岁才上演，此后平均'一年两部'（B369）。O locura o santidad（疯子还是圣徒, 1877）——'he showed that honesty is condemned as madness by society'（B369）。",
"timeline":[
 {"year":1832,"text":"4月19日生于马德里（B369）。","src":"B369"},
 {"year":1874,"text":"任财政部长、参与创办西班牙银行；第一部剧上演（B369）。","src":"B369"},
 {"year":1877,"text":"O locura o santidad——'诚实被社会判为疯狂'（B369）。","src":"B369"},
 {"year":1904,"text":"获诺贝尔文学奖（与米斯特拉尔分享）（B369）。","src":"B369"},
 {"year":1916,"text":"9月4日卒于马德里（B369）。","src":"B369"}],
"major_works":[
 {"work_id":"fengzihaishishengt","note":"1877（B369）"},
 {"title":"支票簿","note":"（B369：El libro talonario (1874)——中译名待核）"}],
"style":["情节剧式（B369：melodramatic）。",
 "浪漫主义底色与'论题剧'的转向（B369：almost wholly Romantic / thesis drama under Ibsen's influence）。",
 "讽刺反转（B369：satiric reversal）。"],
"status":"Britannica 定位埃切加赖为1904诺奖得主、19世纪末西班牙最重要剧作家、数学家与政治家（B369）。",
"sources":["B369"],"dates_source":"B369",
"pending":["中译名（《疯子还是圣徒》）待核。","'帮助革新西班牙剧场'细节（B369：helped revolutionize Spanish theatre）待核。","数学成就（'bounding solids'说）待核——B369未载。"]},
{"id":"galdos","name":"贝尼托·佩雷斯·加尔多斯","foreign_name":"Benito Pérez Galdós（贝尼托·佩雷斯·加尔多斯，1843-05-10—1920-01-04）","country":"西班牙","birth":1843,"death":1920,"birth_year":1843,"death_year":1920,"era":"近代",
"summary":"加尔多斯，加那利群岛拉斯帕尔马斯生，西班牙小说家——'regarded as the greatest Spanish novelist since Miguel de Cervantes'（塞万提斯之后最伟大的西班牙小说家——B370）；与巴尔扎克、狄更斯并提（B370）；'perfected the Spanish realistic novel and innovatively recreated Spain's 19th-century history'（B370）。Episodios nacionales（民族轶事）46部 (1873-1912)——写1805-1874（B370）。Fortunata y Jacinta（福尔图娜塔和哈辛塔, 1886-87）——四卷——'a paradigm of Spanish realism'——被称为其杰作（B370）。",
"timeline":[
 {"year":1843,"text":"5月10日生于拉斯帕尔马斯（B370）。","src":"B370"},
 {"year":1870,"text":"首作 La fontana de oro（B370）。","src":"B370"},
 {"year":1873,"text":"《民族轶事》系列开始（至1912共46部）（B370）。","src":"B370"},
 {"year":1886,"text":"Fortunata y Jacinta（1886-87四卷）——'a paradigm of Spanish realism'（B370）。","src":"B370"},
 {"year":1920,"text":"1月4日卒于马德里（B370）。","src":"B370"}],
"major_works":[
 {"work_id":"fortunata","note":"1886-87四卷（B370）"},
 {"title":"民族轶事","note":"（B370：Episodios nacionales (1873-1912)——46部）"},
 {"title":"纳萨林","note":"（B370：Nazarín (1895)）"}],
"style":["'完善了西班牙现实主义小说'（B370：perfected the Spanish realistic novel）。",
 "巴尔扎克式的系列人物（B370：comparison with Balzac——语境）。",
 "19世纪西班牙史的小说化（B370：recreated Spain's 19th-century history）。"],
"status":"Britannica 定位加尔多斯为塞万提斯之后最伟大的西班牙小说家（B370）。",
"sources":["B370"],"dates_source":"B370",
"pending":["Fortunata y Jacinta 通行译名（《福尔图娜塔和哈辛塔》）待核。","《民族轶事》46部清单待核。","诺奖未得与提名史待核（B370未载）。"]},
{"id":"pindar","name":"品达","foreign_name":"Pindar（品达，约公元前518—约公元前438）","country":"希腊","birth":None,"death":None,"birth_year":-518,"death_year":-438,"era":"古代",
"summary":"品达，约前518生于彼奥提亚Cynoscephalae，卒于约前438——'ancient Greece's greatest lyric poet and master of epinicia'（古希腊最伟大的抒情诗人、竞技凯歌大师——B371）。竞技凯歌颂四大赛会优胜者——古代17卷唯四卷（按赛会分卷、共44首）完整传世（B371）。风格：神话叙事、僭妄训诫、'no two odes alike'的多变格律与'Pindaric flights'（B371）。fragment 76 赞雅典获特殊荣誉（B371）。",
"timeline":[
 {"year":-518,"text":"约前518生于彼奥提亚Cynoscephalae（B371）。","src":"B371"},
 {"year":-462,"text":"约前462起为希耶罗等僭主作凯歌（首奥林匹克凯歌说——通说待核）。","src":"B371"},
 {"year":-446,"text":"前446后卒（约前438，阿尔戈斯——B371）。","src":"B371"}],
"major_works":[
 {"work_id":"shenglisong","note":"四卷44首（B371）"}],
"style":["竞技凯歌（epinicia）的大师（B371）。",
 "'Pindaric flights'：主题的急转（B371）。",
 "对僭妄（hubris）的道德训诫（B371）。"],
"status":"Britannica 定位品达为古希腊最伟大的抒情诗人（B371）。",
"sources":["B371"],"dates_source":"B371",
"pending":["生卒年（约前518/约前438——B371 口径）待核。","四卷篇数（44首——B371）核对。","科林娜逸事（'sow with the hand'——B371）属传闻口径待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"fengzihaishishengt","title":"疯子还是圣徒","original_title":"O locura o santidad","region":"西班牙","era":"近代","era_detail":"19世纪70年代",
"genre":"戏剧","genre_group":"戏剧","language":"西班牙语","author_id":"echegaray","author_name":"何塞·埃切加赖",
"year_display":"1877年（Britannica B369：O locura o santidad (1877; Madman or Saint)）","year_sort":1877,
"background":["Britannica（B369）：'he showed that honesty is condemned as madness by society'——诚实被社会判为疯狂。","Britannica（B369）：埃切加赖——数学家、政治家与'leading Spanish dramatist of the last quarter of the 19th century'。","Britannica（B369）：'In all his plays his manner is melodramatic.'——情节剧式。"],
"outline":["（通说待核——B369未载剧情）'诚实的疯子'：道德者被社会判为疯狂。","（通说待核）讽刺反转的结局（B369：satiric reversal 语境）。"],
"characters":[{"name":"主角（无名待核）","identity":"'诚实者'","note":"（通说待核，B369未载）"}],
"themes":["'诚实被判为疯狂'（B369）。",
 "情节剧的形式（B369：melodramatic）。",
 "论题剧的先声（B369：thesis drama——后期语境交叉）。"],
"influence":[{"text":"Britannica：1904诺奖（B369）。","source":"B369"},{"text":"Britannica：'helped revolutionize Spanish theatre'（B369）。","source":"B369"}],
"reading":{"difficulties":["'论题剧'的辩论结构。","19世纪西班牙剧坛。"],
 "editions":["《疯子还是圣徒》中译名（《是疯子还是圣人》）待核。","西班牙文原版（公有领域）。"],
 "order":"埃切加赖代表作；了解'情节剧'传统的入口。"},
"pending":["剧情细节核对（通说）。","1877年首演细节待核。","中译名两说待核。"],
"sources":["B369"],"year_source":"B369","author_source":"B369","related_works":["aimiliyajialuoti","yinmouyuaiqing","richu"],
"svg":G("《疯子还是圣徒》论题结构图",[{"title":"诚实","text":"被判为疯狂（B369）","color":"main"},{"title":"社会","text":"价值的颠倒（B369语境）","color":"antagonist"},{"title":"情节剧","text":"melodramatic（B369）","color":"gold"},{"title":"反转","text":"讽刺的结局（B369）","color":"family"}])},
{"id":"fortunata","title":"福尔图娜塔和哈辛塔","original_title":"Fortunata y Jacinta","region":"西班牙","era":"近代","era_detail":"19世纪80年代",
"genre":"长篇小说（四卷）","genre_group":"小说","language":"西班牙语","author_id":"galdos","author_name":"贝尼托·佩雷斯·加尔多斯",
"year_display":"1886-87年（Britannica B370：Fortunata y Jacinta (1886-87)——四卷——'a paradigm of Spanish realism'——masterpiece）","year_sort":1886,
"background":["Britannica（B370）：'a study of two unhappily married women from different social classes'——两个不同阶层的不幸婚姻女人的研究。","Britannica（B370）：'Madrid's social spectrum through the lives of two women and a wealthy bourgeois'——被称为其杰作（masterpiece）。","Britannica（B370）：'a paradigm of Spanish realism'（西班牙现实主义的典范）。"],
"outline":["（通说待核）福尔图娜塔（平民）与哈辛塔（资产阶级）：一夫二妻的三角。","（通说待核）马德里社会光谱：从兵营到药房。"],
"characters":[{"name":"福尔图娜塔","identity":"平民女子","note":"（B370 书名人物）"},{"name":"哈辛塔","identity":"资产阶级女子","note":"（B370 书名人物）"},{"name":"胡安·圣菲尔莫","identity":"富有的资产阶级","note":"（B370：a wealthy bourgeois——名通说待核）"}],
"themes":["'马德里社会光谱'（B370）。",
 "两个女人与一个男人的阶级镜像（B370）。",
 "现实主义的'典范'（B370：paradigm）。"],
"influence":[{"text":"Britannica：'the greatest Spanish novelist since Cervantes'（B370 作者级）。","source":"B370"},{"text":"Britannica：'a paradigm of Spanish realism'（B370）。","source":"B370"}],
"reading":{"difficulties":["四卷的体量与人物表。","1868革命前后的马德里史（通说待核）。"],
 "editions":["《福尔图娜塔和哈辛塔》中译名（《福尔图娜塔与哈辛塔》）待核。","西班牙文原版（公有领域）。"],
 "order":"加尔多斯代表作；与巴尔扎克式系列对照。"},
"pending":["胡安·圣菲尔莫人名核对（通说）。","1886-87年出版细节待核。","四卷分段核对（通说）。"],
"sources":["B370"],"year_source":"B370","author_source":"B370","related_works":["fuluosihemofang","midengmamaqi" if "midengmamaqi" in existing else "nongmin","baofali"],
"svg":G("《福尔图娜塔和哈辛塔》阶级镜像图",[{"title":"福尔图娜塔","text":"平民的妻子（B370）","color":"main"},{"title":"哈辛塔","text":"资产阶级的妻子（B370）","color":"family"},{"title":"马德里","text":"'社会光谱'（B370）","color":"gold"},{"title":"典范","text":"现实主义的标杆（B370）","color":"antagonist"}])},
{"id":"shenglisong","title":"胜利颂","original_title":"Epinicia（四卷竞技凯歌）","region":"希腊","era":"古代","era_detail":"公元前5世纪",
"genre":"合唱凯歌（四卷44首）","genre_group":"诗歌","language":"希腊语（多利安方言）","author_id":"pindar","author_name":"品达",
"year_display":"约公元前5世纪（Britannica B371：四卷竞技凯歌——44首完整传世——古代17卷唯此四卷完整）","year_sort":-470,
"background":["Britannica（B371）：'master of epinicia'——颂奥林匹克/皮提亚/地峡/尼米亚四大赛会优胜者——共44首按赛会分卷。","Britannica（B371）：风格——神话叙事、僭妄训诫、'no two odes alike'、'Pindaric flights'。","Britannica（B371）：贵族法则——荷马名言'ever to excel and to surpass other men'。"],
"outline":["（通说待核）凯歌的典型结构：赛况—神话—训诫—祝福。","（通说待核）'奥林匹亚颂'之首（为希耶罗作说——通说待核）。"],
"characters":[{"name":"优胜者","identity":"受颂者","note":"（B371：victors at the games）"},{"name":"神话人物","identity":"插入的叙事","note":"（B371：mythic narratives）"}],
"themes":["竞技凯歌的仪式（B371）。",
 "'Pindaric flights'的急转（B371）。",
 "僭妄（hubris）的训诫（B371）。"],
"influence":[{"text":"Britannica：'ancient Greece's greatest lyric poet'（B371）。","source":"B371"},{"text":"Britannica：四卷完整传世（或因2世纪教科书使用——B371）。","source":"B371"}],
"reading":{"difficulties":["多利安方言（读译本）。","'品达体'颂歌的结构。"],
 "editions":["《胜利颂》中译名（《奥林匹亚颂》等——通说待核）。","希腊语原版（公有领域）。"],
 "order":"古希腊抒情诗首选；与萨福残篇对读。"},
"pending":["44首篇数核对（B371口径）。","'首奥林匹克凯歌'细节待核。","'Pindaric flights'术语通行译名待核。"],
"sources":["B371"],"year_source":"B371","author_source":"B371","related_works":["safucanpian","shiyi","xunjiexiaoshuo"],
"svg":G("《胜利颂》凯歌结构图",[{"title":"凯歌","text":"四大赛会的优胜（B371）","color":"main"},{"title":"神话","text":"插入的叙事（B371）","color":"gold"},{"title":"急转","text":"'Pindaric flights'（B371）","color":"antagonist"},{"title":"训诫","text":"僭妄的警告（B371）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B36x/B37x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('fengzihaishishengt','echegaray'), ('fortunata','galdos'), ('shenglisong','pindar')]:
    if wid in created:
        link(aid, wid)
print('BATCH51 DONE')
