# -*- coding: utf-8 -*-
"""批61：Britannica 新核 2 作家 3 部（勒克莱齐奥 B381/莫迪亚诺 B382）"""
import json, pathlib

newsrc = [
{"id":"B381","title":"Jean-Marie Gustave Le Clezio — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jean-Marie-Gustave-Le-Clezio","type":"百科全书","verified":True,"covers":["leclezio","sha"],"note":"2026-11-21 核对：1940-04-13尼斯生；2008诺贝尔文学奖；Désert（沙漠, 1980）——'awarded the Grand Prix Paul Morand by the French Academy'——主角'a North African Berber separated from her past and her cultural inheritance'；'known for his intricate, seductive fiction and distinctive works of nonfiction that mediate between the past and the present'；'a compassionate and evocative portrayal of the disenfranchised and displaced in search of meaning, identity, and reintegration'；'emerged independently from contemporaries of the nouveau roman'；Le Procès-verbal (1963)——勒诺多奖；La Fièvre (1965)；Le Déluge (1966)；Onitsha (1991)——半自传（尼日利亚童年）；L'Africain (2004)——战后与父重逢回忆录；Révolutions (2003)；Alma (2017)"},
{"id":"B382","title":"Patrick Modiano — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Patrick-Modiano","type":"百科全书","verified":True,"covers":["modiano","anpujie"],"note":"2026-11-21 核对：1945-07-30法国Boulogne-Billancourt生；2014诺贝尔文学奖——瑞典学院'the art of memory with which he has evoked the most ungraspable human destinies'（以记忆的艺术唤起最难把握的人类命运）——第15位法国得主+当年国家图书馆奖；La Place de l'Étoile (1968)首作——犹太通敌者（或以其父为原型）——题名暗指黄星；Rue des boutiques obscures（暗铺街, 1978; Missing Person）——失忆者寻找自我身份的惊悚——龚古尔奖；Dora Bruder (1997; The Search Warrant)——重构失踪犹太少女的一生；'sometimes likened to Marcel Proust despite differing styles'；被占巴黎'almost functioning as a character in his books'；评论——'so spare and elliptical that the words seem only lightly attached to the page'；Ring Roads (1972)——法兰西学院大奖；与路易·马勒合写 Lacombe Lucien (1974)剧本；Un Pedigree (2005)——前21年回忆录；Souvenirs dormants (2017)；Encre sympathique (2019)"},
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
{"id":"leclezio","name":"让-马里·古斯塔夫·勒克莱齐奥","foreign_name":"Jean-Marie Gustave Le Clézio（让-马里·古斯塔夫·勒克莱齐奥，1940-04-13—）","country":"法国","birth":1940,"death":None,"birth_year":1940,"death_year":None,"era":"现当代",
"summary":"勒克莱齐奥，尼斯生，法国作家——2008年诺贝尔文学奖（B381）。Désert（沙漠, 1980）——法兰西学院保罗·莫朗大奖——主角'a North African Berber separated from her past and her cultural inheritance'（与自己的过去和文化遗产分离的北非柏柏尔女子——B381）。'known for his intricate, seductive fiction and distinctive works of nonfiction that mediate between the past and the present'（B381）；'a compassionate and evocative portrayal of the disenfranchised and displaced in search of meaning, identity, and reintegration'（B381）。Le Procès-verbal (1963)——勒诺多奖（B381）。",
"timeline":[
 {"year":1940,"text":"4月13日生于尼斯（B381）。","src":"B381"},
 {"year":1963,"text":"Le Procès-verbal——勒诺多奖（B381）。","src":"B381"},
 {"year":1980,"text":"Désert（沙漠）——保罗·莫朗大奖（B381）。","src":"B381"},
 {"year":2008,"text":"获诺贝尔文学奖（B381）。","src":"B381"}],
"major_works":[
 {"work_id":"sha","note":"1980（B381）"},
 {"title":"诉讼笔录","note":"（B381：Le Procès-verbal (1963)——中译名待核）"},
 {"title":"非洲人","note":"（B381：L'Africain (2004)——父亲重逢回忆录）"}],
"style":["'繁复而迷人'的小说与沟通古今的非虚构（B381）。",
 "'流离失所者寻找意义、身份与重新融入'的悲悯画像（B381）。",
 "'独立于新小说派'（B381：emerged independently）。"],
"status":"Britannica 定位勒克莱齐奥为2008诺奖得主、无根者与边缘者的书写者（B381）。",
"sources":["B381"],"dates_source":"B381",
"pending":["《沙漠》通行译名待核。","'尼日利亚童年'（Onitsha——B381）细节待核。","与毛里求斯家族史的关联待核。"]},
{"id":"modiano","name":"帕特里克·莫迪亚诺","foreign_name":"Patrick Modiano（帕特里克·莫迪亚诺，1945-07-30—）","country":"法国","birth":1945,"death":None,"birth_year":1945,"death_year":None,"era":"现当代",
"summary":"莫迪亚诺，法国Boulogne-Billancourt生，作家——2014年诺贝尔文学奖——瑞典学院'the art of memory with which he has evoked the most ungraspable human destinies'（以记忆的艺术唤起最难把握的人类命运——B382）。Rue des boutiques obscures（暗铺街, 1978）——失忆者寻找自我身份的惊悚——龚古尔奖（B382）。Dora Bruder（朵拉·布吕德, 1997）——重构失踪犹太少女的一生（B382）。被占巴黎'almost functioning as a character in his books'（B382）。评论——'so spare and elliptical that the words seem only lightly attached to the page'（B382）。",
"timeline":[
 {"year":1945,"text":"7月30日生于Boulogne-Billancourt（B382）。","src":"B382"},
 {"year":1968,"text":"La Place de l'Étoile——首作（B382）。","src":"B382"},
 {"year":1978,"text":"《暗铺街》——龚古尔奖（B382）。","src":"B382"},
 {"year":1997,"text":"Dora Bruder（朵拉·布吕德）（B382）。","src":"B382"},
 {"year":2014,"text":"获诺贝尔文学奖（B382）。","src":"B382"}],
"major_works":[
 {"work_id":"anpujie","note":"1978龚古尔奖（B382）"},
 {"work_id":"duolabulude","note":"1997（B382）"},
 {"title":"夜半撞车", "note":"（B382 口径外——不采）"}],
"style":["'记忆的艺术'（B382：the art of memory）。",
 "'如此简洁与省略，词似乎轻轻附着在纸页上'（B382 评论）。",
 "被占巴黎作为'书中人物'（B382）。"],
"status":"Britannica 定位莫迪亚诺为2014诺奖得主、'记忆的艺术'的实践者（B382）。",
"sources":["B382"],"dates_source":"B382",
"pending":["《暗铺街》通行译名（《暗店街》）待核。","'与普鲁斯特相比'说法（B382：sometimes likened）待核。","Lacombe Lucien 剧本细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"sha","title":"沙漠","original_title":"Désert","region":"法国","era":"现当代","era_detail":"20世纪80年代初",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"leclezio","author_name":"让-马里·古斯塔夫·勒克莱齐奥",
"year_display":"1980年（Britannica B381：Désert (1980)——法兰西学院保罗·莫朗大奖）","year_sort":1980,
"background":["Britannica（B381）：Désert——主角'a North African Berber separated from her past and her cultural inheritance'。","Britannica（B381）：'a compassionate and evocative portrayal of the disenfranchised and displaced in search of meaning, identity, and reintegration'。","Britannica（B381）：勒克莱齐奥——2008诺奖；'emerged independently from contemporaries of the nouveau roman'。"],
"outline":["（通说待核——B381未载剧情）拉拉：北非沙漠的逃婚与马赛的流亡。","（通说待核）'沙漠'的 blue men 与现代都市的对照。"],
"characters":[{"name":"拉拉","identity":"柏柏尔少女","note":"（通说待核，B381未载）"}],
"themes":["'与过去和文化遗产分离'（B381）。",
 "流离失所者的身份追寻（B381：in search of meaning, identity, and reintegration）。",
 "沙漠与都市的双声（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：保罗·莫朗大奖（B381）。","source":"B381"},{"text":"Britannica：2008诺奖（B381 交叉）。","source":"B381"}],
"reading":{"difficulties":["柏柏尔文化背景。","双线结构（通说待核）。"],
 "editions":["《沙漠》中译本（人民文学等——通说待核）。","法文原版。"],
 "order":"勒克莱齐奥代表作；与《诉讼笔录》对读。"},
"pending":["拉拉人名核对（通说）。","1980年出版细节待核。","双线（沙漠/马赛）结构待核。"],
"sources":["B381"],"year_source":"B381","author_source":"B381","related_works":["peideluobalamo","gududemigong","zhegeshijiedewanguo"],
"svg":G("《沙漠》流亡结构图",[{"title":"沙漠","text":"分离的遗产（B381）","color":"gold"},{"title":"拉拉","text":"柏柏尔的流亡（通说）","color":"main"},{"title":"马赛","text":"都市的边缘（通说）","color":"antagonist"},{"title":"悲悯","text":"'流离者'的画像（B381）","color":"family"}])},
{"id":"anpujie","title":"暗铺街","original_title":"Rue des boutiques obscures","region":"法国","era":"现当代","era_detail":"20世纪70年代末",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"modiano","author_name":"帕特里克·莫迪亚诺",
"year_display":"1978年（Britannica B382：Rue des boutiques obscures (1978; Missing Person)——龚古尔奖）","year_sort":1978,
"background":["Britannica（B382）：'a thriller in which a man with amnesia searches for his own identity'——失忆者寻找自我身份的惊悚——龚古尔奖。","Britannica（B382）：莫迪亚诺——'the art of memory'——被占巴黎'almost functioning as a character in his books'。","Britannica（B382）：评论——'so spare and elliptical that the words seem only lightly attached to the page'。"],
"outline":["（通说待核——B382未载剧情）私家侦探于特失忆：寻找'吉米·罗德里格斯'。","（通说待核）'巴黎的雪'与战时的痕迹。"],
"characters":[{"name":"于特","identity":"失忆侦探","note":"（通说待核，B382未载）"}],
"themes":["'记忆的艺术'（B382）。",
 "身份的空洞与追踪（书名语境——通说待核）。",
 "被占巴黎的幽灵（B382：almost functioning as a character）。"],
"influence":[{"text":"Britannica：龚古尔奖（B382）。","source":"B382"},{"text":"Britannica：2014诺奖（B382 交叉）。","source":"B382"}],
"reading":{"difficulties":["失忆叙事的线索。","1960年代巴黎地名。"],
 "editions":["《暗铺街》中译名（《暗店街》）待核。","法文原版。"],
 "order":"莫迪亚诺代表作；后接《朵拉·布吕德》。"},
"pending":["于特/罗德里格斯人名核对（通说）。","1978年出版细节待核。","'暗店街'译名两说待核。"],
"sources":["B382"],"year_source":"B382","author_source":"B382","related_works":["suiyue","zenodeyishi","tangjihuade"],
"svg":G("《暗铺街》失忆结构图",[{"title":"失忆","text":"自我的空洞（B382）","color":"main"},{"title":"暗铺街","text":"追寻的地址（书名）","color":"gold"},{"title":"巴黎","text":"'书中人物'（B382）","color":"antagonist"},{"title":"省略","text":"'轻轻附着'的文体（B382）","color":"family"}])},
{"id":"duolabulude","title":"朵拉·布吕德","original_title":"Dora Bruder","region":"法国","era":"现当代","era_detail":"20世纪90年代末",
"genre":"纪实文学（档案叙事）","genre_group":"散文","language":"法语","author_id":"modiano","author_name":"帕特里克·莫迪亚诺",
"year_display":"1997年（Britannica B382：Dora Bruder (1997; The Search Warrant)）","year_sort":1997,
"background":["Britannica（B382）：Dora Bruder——'An effort to reconstruct the life of a missing Jewish girl'（重构一位失踪犹太少女的一生）。","Britannica（B382）：莫迪亚诺——'the art of memory with which he has evoked the most ungraspable human destinies'（诺奖授奖词）。","题材（通说待核）：从旧报纸寻人启事出发——档案、地址与'维希'的空缺。"],
"outline":["（通说待核）1941年《巴黎晨报》寻人启事：15岁的朵拉离家。","（通说待核）档案的空缺与作者的填补。"],
"characters":[{"name":"朵拉·布吕德","identity":"失踪少女","note":"（B382 书名人物）"},{"name":"欧内斯特·布吕德","identity":"父亲","note":"（通说待核）"}],
"themes":["档案与记忆的伦理（B382：reconstruct the life）。",
 "'最难把握的人类命运'（B382 诺奖引语）。",
 "维希法国的追索（通说待核）。"],
"influence":[{"text":"Britannica：'An effort to reconstruct the life of a missing Jewish girl'（B382）。","source":"B382"},{"text":"Britannica：2014诺奖授奖词（B382）。","source":"B382"}],
"reading":{"difficulties":["档案叙事的空缺美学。","维希法国史。"],
 "editions":["《朵拉·布吕德》中译名（《失踪女子》）待核。","法文原版。"],
 "order":"莫迪亚诺非虚构篇；与《暗铺街》对读。"},
"pending":["朵拉档案细节核对（通说）。","1997年出版细节待核。","英译名 The Search Warrant（B382）核对。"],
"sources":["B382"],"year_source":"B382","author_source":"B382","related_works":["anpujie","suiyue","huoluan"],
"svg":G("《朵拉·布吕德》档案结构图",[{"title":"寻人启事","text":"1941年的线索（通说）","color":"gold"},{"title":"朵拉","text":"失踪的少女（B382）","color":"main"},{"title":"档案","text":"空缺的填补（B382语境）","color":"family"},{"title":"维希","text":"追索的年代（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（B38x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('sha','leclezio','沙漠'),('anpujie','modiano','暗铺街'),('duolabulude','modiano','朵拉·布吕德')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH61 DONE')
