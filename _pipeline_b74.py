# -*- coding: utf-8 -*-
"""批74：Britannica 新核 2 作家 3 部（希梅内斯 B401 小银和我/巴别尔 B402 骑兵军+敖德萨故事）"""
import json, pathlib

newsrc = [
{"id":"B401","title":"Juan Ramon Jimenez — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Juan-Ramon-Jimenez","type":"百科全书","verified":True,"covers":["jrjimenez","xiaoyinhewo"],"note":"2026-11-21 核对：1881-12-24西班牙Moguer生—1958-05-29波多黎各圣胡安卒（76岁）；1956诺贝尔文学奖；Platero y yo（小银和我, 1917）——'the story of a man and his donkey'——经英译在美国流行；'la poesía desnuda'（裸体诗）——1917日记 Diario de un poeta recién casado（1948年重刊为 Diario de un poeta y mar）——'remove all extraneous elements and write freer, purer verse without formal metres'（去掉一切多余要素、写更自由纯粹的无格律诗）；前两部诗集因'by their excessive sentiment that he destroyed every copy he could find'（过度感伤而销毁能找到的每一本）；妻 Zenobia Camprubí（合译《海上悲剧》等——1920 Riders to the Sea 译本）；Animal de fondo (1947)"},
{"id":"B402","title":"Isaac Babel — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Isaac-Babel","type":"百科全书","verified":True,"covers":["babel","qibingjun"],"note":"2026-11-21 核对：1894-06-30敖德萨生（乌克兰，俄帝国）—1940-01-27莫斯科被处决（1月26日判——'He was executed at 1:30 am the following day'）；1939-05-15被捕（间谍与反苏罪）——酷刑下签供词后翻供——1954年平反——被没收的私人档案'disappeared without a trace'；Konarmiya（骑兵军, 1926初版/1931修订/1933增订）——苏波战争(1919-20)——1920春以 Kiril Lyutov 笔名加入布琼尼第一骑兵军（YugROSTA记者）——叙述者 Lyutov 'ostensibly autobiographical'——'probes the clash between revolutionary ideals and brutal violence'；首篇1923年敖德萨报——开篇'Crossing the Zbruch'、结篇'Rebbe's Son'；布琼尼1924/1928公开抨击；Tales of Odessa（敖德萨故事, 1931）——敖德萨犹太黑社会——首篇'The King' 1921-06-23 Moryak 刊——Benya Krik——'a mock Jewish messiah'——Rabelaisian 故事兼'闯入'俄国文学的寓言——叙述者'with spectacles on his nose and autumn in his heart'——1927电影 Benya Krik 被禁一年；'Story of My Dovecote' (1926)；剧本 Zakat (1927)——唯一成功的舞台剧；Mariya (1935)生前未上演；与爱森斯坦合作 Bezhin Meadow (1936-37被禁)；'aphoristic precision, combined with the metaphoric extravagance of Modernist poetry'；'the genre of literary silence'（1934作家代表大会）——'The Party and the state have given us everything'（审查的讽刺）；犹太人'not so much the victims of rapid change but resourceful characters'；高尔基期刊 Letopis 1916初登；影响 Philip Roth/Grace Paley"},
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
{"id":"jrjimenez","name":"胡安·拉蒙·希梅内斯","foreign_name":"Juan Ramón Jiménez（胡安·拉蒙·希梅内斯，1881-12-24—1958-05-29）","country":"西班牙","birth":1881,"death":1958,"birth_year":1881,"death_year":1958,"era":"近代",
"summary":"希梅内斯，西班牙Moguer生，诗人——1956年诺贝尔文学奖（B401）。Platero y yo（小银和我, 1917）——'the story of a man and his donkey'（一个人与他的驴的故事——B401）——经英译在美国流行。'la poesía desnuda'（裸体诗）——1917年日记《一个新婚诗人的日记》（1948年重刊为《诗人与海》）——'remove all extraneous elements and write freer, purer verse without formal metres'（去掉一切多余要素、写更自由纯粹的无格律诗——B401）。前两部诗集因过度感伤而销毁能找到的每一本（B401）。妻 Zenobia Camprubí（B401）。",
"timeline":[
 {"year":1881,"text":"12月24日生于西班牙Moguer（B401）。","src":"B401"},
 {"year":1917,"text":"《小银和我》与《一个新婚诗人的日记》同年（B401）。","src":"B401"},
 {"year":1956,"text":"获诺贝尔文学奖（B401）。","src":"B401"},
 {"year":1958,"text":"5月29日卒于波多黎各圣胡安（B401）。","src":"B401"}],
"major_works":[
 {"work_id":"xiaoyinhewo","note":"1917（B401）"},
 {"title":"一个新婚诗人的日记","note":"（B401：Diario de un poeta recién casado (1917)——中译名待核）"},
 {"title":"底层的动物","note":"（B401：Animal de fondo (1947)——中译名待核）"}],
"style":["'裸体诗'：'去掉一切多余要素'（B401：la poesía desnuda）。",
 "'人与驴'的散文诗（B401：Platero y yo）。",
 "销毁早期感伤之作（B401）。"],
"status":"Britannica 定位希梅内斯为1956诺奖得主、'裸体诗'理论家（B401）。",
"sources":["B401"],"dates_source":"B401",
"pending":["《小银和我》通行译名（《小银和我》/《普拉特罗与我》）待核。","与塞诺比娅合译细节（B401：Riders to the Sea 1920）待核。","'裸体诗'与洛尔卡一代的关系待核。"]},
{"id":"babel","name":"伊萨克·巴别尔","foreign_name":"Isaac Babel（伊萨克·巴别尔，1894-06-30—1940-01-27）","country":"苏联","birth":1894,"death":1940,"birth_year":1894,"death_year":1940,"era":"近代",
"summary":"巴别尔，敖德萨生，苏联作家——1940年1月27日凌晨1:30被处决（B402：1月26日判——次日1:30行刑）；1939年5月15日被捕（间谍与反苏罪）——酷刑下签供词后翻供——1954年平反——被没收的私人档案'disappeared without a trace'（B402）。Konarmiya（骑兵军, 1926）——苏波战争——1920春以 Kiril Lyutov 笔名入布琼尼第一骑兵军——'probes the clash between revolutionary ideals and brutal violence'（B402）。Tales of Odessa（敖德萨故事, 1931）——Benya Krik——'a mock Jewish messiah'（B402）。'aphoristic precision, combined with the metaphoric extravagance of Modernist poetry'（格言式的精确+现代主义诗的隐喻铺张——B402）；'the genre of literary silence'（'沉默的文学'——1934作家代表大会——B402）。",
"timeline":[
 {"year":1894,"text":"6月30日生于敖德萨（B402）。","src":"B402"},
 {"year":1920,"text":"以笔名 Lyutov 加入布琼尼第一骑兵军（B402）。","src":"B402"},
 {"year":1926,"text":"《骑兵军》初版（B402）。","src":"B402"},
 {"year":1939,"text":"5月15日被捕（B402）。","src":"B402"},
 {"year":1940,"text":"1月27日凌晨1:30被处决；1954年平反（B402）。","src":"B402"}],
"major_works":[
 {"work_id":"qibingjun","note":"1926（B402）"},
 {"work_id":"aodesagushi","note":"1931（B402）"},
 {"title":"日落","note":"（B402：Zakat (1927)——唯一成功的舞台剧——中译名待核）"}],
"style":["'格言式的精确+现代主义诗的隐喻铺张'（B402）。",
 "'沉默的文学'（B402：the genre of literary silence）。",
 "犹太人'机智角色'而非单纯受害者（B402：resourceful characters）。"],
"status":"Britannica 定位巴别尔为被处决的天才短篇家、'沉默的文学'的提出者（B402）。",
"sources":["B402"],"dates_source":"B402",
"pending":["《骑兵军》通行译名（《红色骑兵军》）待核。","处决细节核对（B402：1:30 am）。","影响 Philip Roth/Grace Paley（B402口径）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"xiaoyinhewo","title":"小银和我","original_title":"Platero y yo","region":"西班牙","era":"近代","era_detail":"20世纪10年代",
"genre":"散文诗集","genre_group":"诗歌","language":"西班牙语","author_id":"jrjimenez","author_name":"胡安·拉蒙·希梅内斯",
"year_display":"1917年（Britannica B401：Platero y yo (1917)——'the story of a man and his donkey'）","year_sort":1917,
"background":["Britannica（B401）：'the story of a man and his donkey'（一个人与他的驴的故事）——经英译在美国流行。","Britannica（B401）：希梅内斯——1956诺奖；'la poesía desnuda'（裸体诗）。","题材（通说待核）：与小银（驴）的莫格尔对话——140余章的散文诗。"],
"outline":["（通说待核）'小银'（Platero）：柔软的小驴与莫格尔的风物。","（通说待核）'孩子们……不要给小银面包'（不采为引文——首段细节通说待核）。"],
"characters":[{"name":"小银（Platero）","identity":"驴","note":"（B401 书名人物）"},{"name":"'我'","identity":"诗人","note":"（B401 语境）"}],
"themes":["'人与驴'的对话（B401）。",
 "'裸体诗'的散文实践（B401：la poesía desnuda）。",
 "莫格尔的风物志（通说待核）。"],
"influence":[{"text":"Britannica：'the story of a man and his donkey'（B401）。","source":"B401"},{"text":"Britannica：1956诺奖（B401 交叉）。","source":"B401"}],
"reading":{"difficulties":["散文诗的节奏。","安达卢西亚小镇风物。"],
 "editions":["《小银和我》中译本（人民文学等——通说待核）。","西班牙文原版（公有领域状态待核）。"],
 "order":"希梅内斯首选；与《一个新婚诗人的日记》对读。"},
"pending":["章数（138章说）核对（通说）。","1917年出版细节待核。","'小银'译名两说（《普特拉塞洛》）待核。"],
"sources":["B401"],"year_source":"B401","author_source":"B401","related_works":["jipusaiyaoqu","xiaoyinhewo" if False else "leiyu","wuguigu"],
"svg":G("《小银和我》对话结构图",[{"title":"小银","text":"柔软的驴（B401）","color":"main"},{"title":"莫格尔","text":"小镇的风物（通说）","color":"family"},{"title":"裸体诗","text":"'去掉多余要素'（B401）","color":"gold"},{"title":"对话","text":"人与驴（B401）","color":"antagonist"}])},
{"id":"qibingjun","title":"骑兵军","original_title":"Конармия（Red Cavalry）","region":"俄国","era":"近代","era_detail":"20世纪20年代",
"genre":"短篇集（骑兵军日记）","genre_group":"故事集","language":"俄语","author_id":"babel","author_name":"伊萨克·巴别尔",
"year_display":"1926年（Britannica B402：Konarmiya——first published 1926，revised 1931，enlarged 1933）","year_sort":1926,
"background":["Britannica（B402）：'probes the clash between revolutionary ideals and brutal violence'（探究革命理想与残酷暴力的冲突）。","Britannica（B402）：1920春以 Kiril Lyutov 笔名加入布琼尼第一骑兵军（YugROSTA 记者）；叙述者 Lyutov——'ostensibly autobiographical'。","Britannica（B402）：布琼尼1924/1928公开抨击——开篇'Crossing the Zbruch'、结篇'Rebbe's Son'。"],
"outline":["（通说待核——B402未载篇目细节）'渡过兹布鲁奇河'的战地日记式短篇。","（通说待核）犹太城镇与哥萨克骑兵的相撞。"],
"characters":[{"name":"柳托夫","identity":"记者/叙述者","note":"（B402：Lyutov——'ostensibly autobiographical'）"},{"name":"布琼尼","identity":"骑兵军军长","note":"（B402：Semyon Budenny——1924/1928抨击）"}],
"themes":["'革命理想与残酷暴力的冲突'（B402）。",
 "'表面上自传'的叙述者（B402：ostensibly autobiographical）。",
 "犹太'经师'与哥萨克'刀'（通说待核）。"],
"influence":[{"text":"Britannica：'aphoristic precision...metaphoric extravagance'（B402）。","source":"B402"},{"text":"Britannica：影响 Philip Roth/Grace Paley（B402）。","source":"B402"}],
"reading":{"difficulties":["日记体的短篇连缀。","苏波战争史（1919-20——B402）。"],
 "editions":["《骑兵军》中译本（人民文学/浙江文艺等——通说待核）。","俄文原版。"],
 "order":"巴别尔首选；与《敖德萨故事》对读。"},
"pending":["篇目（《渡过兹布鲁奇河》/《拉比之子》——B402已载首末篇）核对。","1926年出版细节待核。","布琼尼抨击细节待核（B402口径）。"],
"sources":["B402"],"year_source":"B402","author_source":"B402","related_works":["aodesagushi","moyan","gushiji" if False else "nongmin"],
"svg":G("《骑兵军》冲突结构图",[{"title":"理想","text":"革命的誓言（B402）","color":"gold"},{"title":"暴力","text":"'残酷的暴力'（B402）","color":"antagonist"},{"title":"柳托夫","text":"'表面自传'（B402）","color":"main"},{"title":"犹太镇","text":"刀锋下的经师（通说）","color":"family"}])},
{"id":"aodesagushi","title":"敖德萨故事","original_title":"Одесские рассказы（Tales of Odessa）","region":"俄国","era":"近代","era_detail":"20世纪20-30年代",
"genre":"短篇集","genre_group":"故事集","language":"俄语","author_id":"babel","author_name":"伊萨克·巴别尔",
"year_display":"1931年（Britannica B402：Tales of Odessa (1931)——敖德萨犹太黑社会——首篇'The King' 1921-06-23 Moryak 刊）","year_sort":1931,
"background":["Britannica（B402）：Tales of Odessa——敖德萨犹太黑社会——Benya Krik——'a mock Jewish messiah'（犹太假弥赛亚）——Rabelaisian 故事兼'闯入'俄国文学的寓言。","Britannica（B402）：叙述者'with spectacles on his nose and autumn in his heart'（鼻子上架着眼镜、心里装着秋天）。","Britannica（B402）：1927年电影 Benya Krik——巴别尔出售剧本——自认失败——被禁一年。"],
"outline":["（通说待核——B402未载篇目细节）'王'别尼亚·克里克的敖德萨黑帮故事。","（通说待核）'如何在大敖德萨成为老者'等篇（篇名通说待核）。"],
"characters":[{"name":"别尼亚·克里克","identity":"'犹太假弥赛亚'/黑帮王","note":"（B402：Benya Krik——'a mock Jewish messiah'）"},{"name":"眼镜少年","identity":"叙述者","note":"（B402：with spectacles on his nose and autumn in his heart）"}],
"themes":["'犹太假弥赛亚'的黑帮史诗（B402）。",
 "'Rabelaisian'的夸张喜剧（B402：Rabelaisian stories）。",
 "'闯入'俄国文学的寓言（B402：allegory of Babel muscling in）。"],
"influence":[{"text":"Britannica：'a mock Jewish messiah'（B402）。","source":"B402"},{"text":"Britannica：1927年电影被禁一年（B402）。","source":"B402"}],
"reading":{"difficulties":["敖德萨犹太黑话。","'Rabelaisian'的夸张。"],
 "editions":["《敖德萨故事》中译本（人民文学等——通说待核）。","俄文原版。"],
 "order":"巴别尔第二篇；与《骑兵军》对读。"},
"pending":["别尼亚·克里克人名核对（B402已载）。","1931年出版细节待核。","1927年电影禁映细节待核（B402口径）。"],
"sources":["B402"],"year_source":"B402","author_source":"B402","related_works":["qibingjun","gushiji" if "gushiji" in existing else "leiyu","moyan"],
"svg":G("《敖德萨故事》黑帮史诗图",[{"title":"别尼亚·克里克","text":"'犹太假弥赛亚'（B402）","color":"main"},{"title":"敖德萨","text":"黑社会的城市（B402）","color":"gold"},{"title":"眼镜与秋天","text":"叙述者的自嘲（B402）","color":"family"},{"title":"Rabelaisian","text":"夸张的喜剧（B402）","color":"antagonist"}])},
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

for wid, aid in [('xiaoyinhewo','jrjimenez'), ('qibingjun','babel'), ('aodesagushi','babel')]:
    if wid in created:
        link(aid, wid)
print('BATCH74 DONE')
