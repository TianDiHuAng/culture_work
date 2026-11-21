# -*- coding: utf-8 -*-
"""批31：Britannica 新核 3 作家 3 部（塞菲里斯/埃利蒂斯/乌纳穆诺 B356-B358）"""
import json, pathlib

newsrc = [
{"id":"B356","title":"George Seferis — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/George-Seferis","type":"百科全书","verified":True,"covers":["seferis","shenhualishi"],"note":"2026-11-21 核对：原名 Giōrgios Stylianou Seferiadēs；1900-03-13士麦那（奥斯曼帝国安纳托利亚，今土耳其伊兹密尔）生—1971-09-20雅典卒（71岁）；1963诺贝尔文学奖；'the most distinguished Greek poet of the generation of the 30s'；其作'shows a deep feeling for the tragic predicament of the Greeks'；巴黎学法律后入希腊外交界——战前伦敦/阿尔巴尼亚，战时随流亡自由希腊政府；战后黎巴嫩/叙利亚/约旦/伊拉克；1957-62驻伦敦大使；作品：Strofí (1931; Turning Point)——'the poet of the future'之誉；I stérna (1932)；Mithistórima (1935; Myth-History)；Imerolóyio katastrómatos I/II/III (1940/1945/1955)；Kíkhli (1947; Thrush)长诗；Tría krifá poiímata (1966)"},
{"id":"B357","title":"Odysseus Elytis — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Odysseus-Elytis","type":"百科全书","verified":True,"covers":["elytis","zhidezansongde"],"note":"2026-11-21 核对：原名 Alepoudhelis；1911-11-02克里特Iráklion生—1996-03-18雅典卒（84岁）；1979诺贝尔文学奖（部分因其长诗被 Theodorakis 谱曲而广传）；莱斯博斯富裕家庭——青年弃姓以免与家族肥皂生意相混；雅典大学法学；受法国超现实主义影响（尤其艾吕雅）；刊于 Nea grammata——'30一代'（含1963年首位希腊诺奖得主塞菲里斯）；Prosanatolismoi (1940; Orientations)；1941年后在阿尔巴尼亚抗意作战——1945年'Heroic and Elegiac Song for the Lost Second Lieutenant of the Albanian Campaign'——'became an anthem to the cause of freedom'；希腊内战后近15年沉默；To Axion Esti (1959)——长诗——'the speaker explores the essence of his being as well as the identity of his country and people'——Theodorakis 谱曲后'became immensely popular and helped Elytis earn the Nobel Prize'；后期 Ho hēlios ho hēliatoras (1971)、Ta eterothalē (1974)、Ho mikros nautilos (1986)、The Oxopetra Elegies (1991)；英译全集 (1997)"},
{"id":"B358","title":"Miguel de Unamuno — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Miguel-de-Unamuno","type":"百科全书","verified":True,"covers":["unamuno","abeiersangchensi"],"note":"2026-11-21 核对：1864-09-29毕尔巴鄂生—1936-12-31萨拉曼卡卒（72岁）；'an early existentialist who concerned himself largely with the tension between intellect and emotion, faith and reason'；'mans hunger to live on after death is constantly denied by his reason and can only be satisfied by faith, and the resulting tension results in unceasing agony'；散文主题——'the need to preserve ones personal integrity in the face of social conformity, fanaticism, and hypocrisy'；Del sentimiento trágico de la vida en los hombres y en los pueblos (1913)——'stressed the vital role spiritual anxiety plays in driving man to live the fullest possible life'；Abel Sánchez (1917)——'his most famous novel'——'a modern re-creation of the biblical story of Cain and Abel'；San Manuel Bueno, mártir (1933)——'the story of an unbelieving priest'；En torno al casticismo (1895)；Vida de Don Quijote y Sancho (1905)——塞万提斯人物分析；Amor y pedagogía (1902)——科学育儿'ending in failure and the sons ruin'；El Cristo de Velázquez (1920)——'a superb example of modern Spanish verse'；Niebla (1914)（页面仅列名无剧情——不采）；注：'nivola'一词未见于本页"},
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

rel_shl = [rid('wuguigu'), rid('diyuzhiji'), rid('huangliang')]
rel_zdz = [rid('shenhualishi'), rid('ershisou'), rid('diyuzhiji')]
rel_abe = [rid('yigewushiwan'), rid('xinshigudeLieshou'), rid('fushide')]
print('rel:', rel_shl, rel_zdz, rel_abe)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"seferis","name":"乔治·塞菲里斯","foreign_name":"George Seferis（乔治·塞菲里斯，原名 Giōrgios Stylianou Seferiadēs，1900-03-13—1971-09-20）","country":"希腊","birth":1900,"death":1971,"birth_year":1900,"death_year":1971,"era":"现当代",
"summary":"塞菲里斯，士麦那生（今土耳其伊兹密尔），希腊诗人、散文家与外交官——1963年诺贝尔文学奖（B356）；'the most distinguished Greek poet of the generation of the 30s'（'30一代'最杰出的希腊诗人——B356）；其作'shows a deep feeling for the tragic predicament of the Greeks'（对希腊人悲剧处境的深切感受——B356）。Strofí（转折点, 1931）——获'the poet of the future'之誉（B356）；Mithistórima（神话与历史, 1935）（B356）。巴黎学法律后入外交界：战前伦敦/阿尔巴尼亚，战时随流亡政府，1957-62驻伦敦大使（B356）。",
"timeline":[
 {"year":1900,"text":"3月13日生于士麦那（B356）。","src":"B356"},
 {"year":1931,"text":"Strofí（转折点）——首部诗集（B356）。","src":"B356"},
 {"year":1935,"text":"Mithistórima（神话与历史）（B356）。","src":"B356"},
 {"year":1963,"text":"获诺贝尔文学奖（B356）。","src":"B356"},
 {"year":1971,"text":"9月20日卒于雅典（B356）。","src":"B356"}],
"major_works":[
 {"work_id":"shenhualishi","note":"1935（B356）"},
 {"title":"转折点","note":"（B356：Strofí (1931)——中译名待核）"}],
"style":["'对希腊人悲剧处境的深切感受'（B356）。",
 "神话与个人史的编织（B356：Mithistórima 书名语境）。",
 "外交官诗人的国际视野（B356 语境）。"],
"status":"Britannica 定位塞菲里斯为1963年诺奖得主、'30一代'最杰出的希腊诗人（B356）。",
"sources":["B356"],"dates_source":"B356",
"pending":["Mithistórima 通行译名（《神话与历史》）待核。","'亚辛之王'等篇目未见于 B356——不采。","1963诺奖授奖词待核。"]},
{"id":"elytis","name":"奥季修斯·埃利蒂斯","foreign_name":"Odysseus Elytis（奥季修斯·埃利蒂斯，原名 Alepoudhelis，1911-11-02—1996-03-18）","country":"希腊","birth":1911,"death":1996,"birth_year":1911,"death_year":1996,"era":"现当代",
"summary":"埃利蒂斯，克里特Iráklion生，希腊诗人——1979年诺贝尔文学奖（B357）。青年弃家族姓 Alepoudhelis——以免与家族肥皂生意相混（B357）。受法国超现实主义影响（尤其艾吕雅）；刊于 Nea grammata——'30一代'（B357）。1941年后在阿尔巴尼亚抗意作战；1945年《阿尔巴尼亚战役阵亡中尉的英雄挽歌》——'became an anthem to the cause of freedom'（B357）。To Axion Esti（1959）——长诗——'the speaker explores the essence of his being as well as the identity of his country and people'——Theodorakis 谱曲后'became immensely popular and helped Elytis earn the Nobel Prize'（B357）。",
"timeline":[
 {"year":1911,"text":"11月2日生于克里特Iráklion（B357）。","src":"B357"},
 {"year":1940,"text":"Prosanatolismoi（定向）——此前作品合集（B357）。","src":"B357"},
 {"year":1959,"text":"To Axion Esti——长诗（B357）。","src":"B357"},
 {"year":1979,"text":"获诺贝尔文学奖（B357）。","src":"B357"},
 {"year":1996,"text":"3月18日卒于雅典（B357）。","src":"B357"}],
"major_works":[
 {"work_id":"zhidezansongde","note":"1959（B357）"},
 {"title":"定向","note":"（B357：Prosanatolismoi (1940)——中译名待核）"}],
"style":["爱琴海的光与透明（书名语境——通说待核）。",
 "超现实主义与希腊民歌传统（B357 语境）。",
 "自由的颂歌（B357：anthem to the cause of freedom）。"],
"status":"Britannica 定位埃利蒂斯为1979年诺奖得主、《理所应当》(To Axion Esti)为其代表作（B357）。",
"sources":["B357"],"dates_source":"B357",
"pending":["To Axion Esti 通行译名（《理所应当》/《值得赞颂的》）待核。","'受 Theodorakis 谱曲'细节待核（B357 口径）。","内战后'15年沉默'细节待核。"]},
{"id":"unamuno","name":"米格尔·德·乌纳穆诺","foreign_name":"Miguel de Unamuno（米格尔·德·乌纳穆诺，1864-09-29—1936-12-31）","country":"西班牙","birth":1864,"death":1936,"birth_year":1864,"death_year":1936,"era":"近代",
"summary":"乌纳穆诺，毕尔巴鄂生，西班牙小说家、散文家与哲学家——'an early existentialist who concerned himself largely with the tension between intellect and emotion, faith and reason'（早期存在主义者，关心理智与情感、信仰与理性之张力——B358）。Del sentimiento trágico de la vida（生命的悲剧意识, 1913）——'stressed the vital role spiritual anxiety plays in driving man to live the fullest possible life'（B358）。Abel Sánchez (1917)——'his most famous novel'——'a modern re-creation of the biblical story of Cain and Abel'（该隐与亚伯的现代重写——B358）。San Manuel Bueno, mártir (1933)——'the story of an unbelieving priest'（不信神的教士——B358）。散文主题：'the need to preserve ones personal integrity in the face of social conformity, fanaticism, and hypocrisy'（B358）。",
"timeline":[
 {"year":1864,"text":"9月29日生于毕尔巴鄂（B358）。","src":"B358"},
 {"year":1913,"text":"Del sentimiento trágico de la vida——'生命的悲剧意识'（B358）。","src":"B358"},
 {"year":1917,"text":"Abel Sánchez——最著名的小说（B358）。","src":"B358"},
 {"year":1933,"text":"San Manuel Bueno, mártir——不信神的教士（B358）。","src":"B358"},
 {"year":1936,"text":"12月31日卒于萨拉曼卡（B358）。","src":"B358"}],
"major_works":[
 {"work_id":"abeiersangchensi","note":"1917（B358）"},
 {"title":"生命的悲剧意识","note":"（B358：1913——哲学散文）"},
 {"title":"圣曼努埃尔·布埃诺，殉道者","note":"（B358：1933——中译名待核）"}],
"style":["'基督徒的痛苦'：理性与信仰的张力（B358）。",
 "个人完整性对从众/狂热/伪善的抵抗（B358）。",
 "堂吉诃德式的民族自省（B358：Vida de Don Quijote y Sancho）。"],
"status":"Britannica 定位乌纳穆诺为早期存在主义者、'98一代'核心（'98一代'提法B358未载——待核）。",
"sources":["B358"],"dates_source":"B358",
"pending":["Abel Sánchez 通行译名待核。","'98一代'提法核对（B358未载）。","Niebla (1914) 页面仅列名——剧情不采。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"shenhualishi","title":"神话与历史","original_title":"Mithistórima","region":"希腊","era":"现当代","era_detail":"20世纪30年代",
"genre":"诗集","genre_group":"诗歌","language":"希腊语","author_id":"seferis","author_name":"乔治·塞菲里斯",
"year_display":"1935年（Britannica B356：Mithistórima (1935; Myth-History)）","year_sort":1935,
"background":["Britannica（B356）：塞菲里斯——'the most distinguished Greek poet of the generation of the 30s'——其作'shows a deep feeling for the tragic predicament of the Greeks'。","Britannica（B356）：Strofí (1931) 出版时被誉'the poet of the future'——本集为其中期代表作。","题材（通说待核）：以神话人物（奥德修斯等）折射现代希腊的流亡与离散。"],
"outline":["神话与历史的对位：古典之'神'与现代之'史'（B356 书名语境；篇目通说待核）。","流亡者的海：爱琴海的记忆政治（通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"外交官诗人","note":"（B356 语境）"}],
"themes":["希腊人的悲剧处境（B356）。",
 "神话的现代化（B356：Myth-History）。",
 "流亡与离散（通说待核）。"],
"influence":[{"text":"Britannica：1963年诺贝尔文学奖——首位希腊得主（B356；'first Greek literature Nobel laureate' 见 B357 交叉）。","source":"B356"},{"text":"Britannica：'the poet of the future'（B356——Strofí 之誉）。","source":"B356"}],
"reading":{"difficulties":["希腊神话典故。","'30一代'的语体。"],
 "editions":["《神话与历史》中译名（通说待核）。","希腊文原版。"],
 "order":"塞菲里斯进阶；先读《转折点》。"},
"pending":["具体篇目（《王亚辛》未见于B356）核对。","1935年出版细节待核。","中译名两说（《神话与历史》/《神话史》)待核。"],
"sources":["B356"],"year_source":"B356","author_source":"B356","related_works":rel_shl,
"svg":G("《神话与历史》神话对位图",[{"title":"神话","text":"古典的回声（B356）","color":"gold"},{"title":"历史","text":"现代的流亡（通说）","color":"antagonist"},{"title":"悲剧处境","text":"希腊人的感受（B356）","color":"main"},{"title":"海","text":"爱琴海的记忆（通说）","color":"family"}])},
{"id":"zhidezansongde","title":"理所应当","original_title":"To Axion Esti","region":"希腊","era":"现当代","era_detail":"20世纪50年代末",
"genre":"长诗","genre_group":"诗歌","language":"希腊语","author_id":"elytis","author_name":"奥季修斯·埃利蒂斯",
"year_display":"1959年（Britannica B357：To Axion Esti (1959)）","year_sort":1959,
"background":["Britannica（B357）：长诗——'the speaker explores the essence of his being as well as the identity of his country and people'（探索自我存在的本质与其国家、人民的身份）。","Britannica（B357）：Theodorakis 为其谱曲——'became immensely popular and helped Elytis earn the Nobel Prize'。","Britannica（B357）：埃利蒂斯——1979诺奖；受法国超现实主义（尤其艾吕雅）影响。"],
"outline":["诗体的民族自画像：诗人之'我'与希腊之'我们'（B357：essence of his being...identity of his country and people）。","赞美诗结构的借用（结构通说待核）。"],
"characters":[{"name":"言说者","identity":"诗人之'我'","note":"（B357：the speaker）"}],
"themes":["存在与民族身份的双重探索（B357）。",
 "自由的颂歌（B357：anthem to the cause of freedom——1945作语境）。",
 "诗与音乐（B357：Theodorakis 谱曲）。"],
"influence":[{"text":"Britannica：1979年诺贝尔文学奖（B357）。","source":"B357"},{"text":"Britannica：'became immensely popular'（B357）。","source":"B357"}],
"reading":{"difficulties":["东正教礼拜仪文的结构借用（通说待核）。","超现实主义语汇。"],
 "editions":["中译名（《理所应当》/《值得赞颂的》）待核。","希腊文原版。"],
 "order":"埃利蒂斯首选。"},
"pending":["中译名两说待核。","礼拜仪文结构（'圣咏'说）待核。","Theodorakis 谱曲年份待核。"],
"sources":["B357"],"year_source":"B357","author_source":"B357","related_works":rel_zdz,
"svg":G("To Axion Esti 颂歌结构图",[{"title":"之'我'","text":"存在的本质（B357）","color":"main"},{"title":"之'我们'","text":"民族的身份（B357）","color":"family"},{"title":"音乐","text":"Theodorakis 谱曲（B357）","color":"gold"},{"title":"自由","text":"颂歌的底色（B357）","color":"antagonist"}])},
{"id":"abeiersangchensi","title":"阿贝尔·桑切斯","original_title":"Abel Sánchez: una historia de pasión","region":"西班牙","era":"近代","era_detail":"20世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"unamuno","author_name":"米格尔·德·乌纳穆诺",
"year_display":"1917年（Britannica B358：Abel Sánchez (1917)——'his most famous novel'）","year_sort":1917,
"background":["Britannica（B358）：'his most famous novel'——'a modern re-creation of the biblical story of Cain and Abel'（该隐与亚伯故事的现代重写）。","Britannica（B358）：乌纳穆诺——'an early existentialist'——理智与情感、信仰与理性之张力。","题材（通说待核）：华金与阿贝尔终生的嫉妒——嫉妒作为'该隐'的现代名。"],
"outline":["一个'该隐'的现代重写：华金对阿贝尔的终生嫉妒（B358：modern re-creation of the biblical story of Cain and Abel；人名通说待核）。","嫉妒的哲学化：'该隐情结'（通说待核）。"],
"characters":[{"name":"华金","identity":"嫉妒者/'该隐'","note":"（通说待核，B358未载）"},{"name":"阿贝尔·桑切斯","identity":"被嫉妒者/'亚伯'","note":"（B358 书名人物）"}],
"themes":["嫉妒的心理学与神学（B358：Cain and Abel 语境）。",
 "信仰与理性之张力（B358）。",
 "个人完整性对伪善社会的抵抗（B358 散文主题语系）。"],
"influence":[{"text":"Britannica：'his most famous novel'（B358）。","source":"B358"},{"text":"Britannica：'a modern re-creation of the biblical story of Cain and Abel'（B358）。","source":"B358"}],
"reading":{"difficulties":["圣经原型（该隐与亚伯）。","'98一代'语境（提法待核——B358未载）。"],
 "editions":["《阿贝尔·桑切斯》中译本（人民文学等——通说待核）。","西班牙文原版。"],
 "order":"乌纳穆诺小说首选；配合《生命的悲剧意识》。"},
"pending":["华金/阿贝尔人名核对（B358未载华金）。","1917年出版细节待核。","'nivola'术语待核（B358未载——不采）。"],
"sources":["B358"],"year_source":"B358","author_source":"B358","related_works":rel_abe,
"svg":G("《阿贝尔·桑切斯》嫉妒结构图",[{"title":"华金","text":"现代'该隐'（通说）","color":"main"},{"title":"阿贝尔","text":"被嫉妒的'亚伯'（B358）","color":"antagonist"},{"title":"嫉妒","text":"终生的激情（B358书名）","color":"gold"},{"title":"理性与信仰","text":"张力的哲学（B358）","color":"family"}])},
]
for w in works:
    if w['id'] in existing:
        print('skip existing', w['id'])
for w in works:
    if w['id'] in existing:
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("seferis","shenhualishi"),("elytis","zhidezansongde"),("unamuno","abeiersangchensi")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B35x/B36x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH31 DONE')
