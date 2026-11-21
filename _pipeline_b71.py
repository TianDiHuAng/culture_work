# -*- coding: utf-8 -*-
"""批71：Britannica 新核 2 作家 3 部（济慈 B395 颂歌1819/雪莱 B396 解放了的普罗米修斯+阿多尼）"""
import json, pathlib

newsrc = [
{"id":"B395","title":"John Keats — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/John-Keats","type":"百科全书","verified":True,"covers":["keats","songge1819"],"note":"2026-11-21 核对：1795-10-31伦敦生—1821-02-23罗马（教皇国）卒（25岁）——'died of tuberculosis in Rome in 1821 at the age of 25'；1819颂歌——'On Indolence'/'On a Grecian Urn'/'To Psyche'/'To a Nightingale'/'On Melancholy'/'To Autumn'——全部写于1819年——'all his greatest poetry came that single year'；'On First Looking into Chapman's Homer'——1816商籁；Poems——首书1817年3月；Endymion——1818——四个1000行部分；1819年：'Lamia'/'The Eve of St. Agnes'/伟大颂歌/'the two unfinished versions of an epic on Hyperion'；The Fall of Hyperion（Notable Works）；注：'negative capability'一词仅在外链标题出现、正文未定义（不采为引文）；'Beauty is truth, truth beauty'仅见于问答标题（不采为引文）"},
{"id":"B396","title":"Percy Bysshe Shelley — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Percy-Bysshe-Shelley","type":"百科全书","verified":True,"covers":["shelley","jiefangpu"],"note":"2026-11-21 核对：1792-08-04英国苏塞克斯Field Place生（近Horsham）—1822-07-08意大利托斯卡纳Livorno海面卒（29岁）——'when his boat sank during a stormy return voyage from Leghorn…to Lerici'（与Edward Williams同溺）；Prometheus Unbound（解放了的普罗米修斯）——1819年秋完成于佛罗伦萨、约1820年出版——'inverts the plot of a lost play by Aeschylus'（颠倒埃斯库罗斯佚剧的情节）——'supple blank verse with a variety of complex lyric measures'——'the keystone of Shelley's poetic achievement'（雪莱诗歌成就的基石）；Ode to the West Wind (1819)——与《解放了的普罗米修斯》同刊——志在使其词语成为'an unextinguished hearth'的'Ashes and sparks'；Adonais——'in Spenserian stanzas'悼济慈（1821）——引文'The One remains, the many change and pass;'/'Life, like a dome of many-coloured glass,'；'Poets are the unacknowledged legislators of the world.'——《诗辨》(A Defence of Poetry, 1821作/1840刊)；The Necessity of Atheism (1811)——被牛津开除；Queen Mab (1813)——首部大诗；'Ozymandias' (1818)；The Cenci (1819)；'To a Skylark'/'The Cloud'（约1820与《解放》同刊）"},
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
{"id":"keats","name":"约翰·济慈","foreign_name":"John Keats（约翰·济慈，1795-10-31—1821-02-23）","country":"英国","birth":1795,"death":1821,"birth_year":1795,"death_year":1821,"era":"近代",
"summary":"济慈，伦敦生，英国浪漫主义诗人——'died of tuberculosis in Rome in 1821 at the age of 25'（25岁死于肺结核——B395）。1819年颂歌——'On a Grecian Urn'/'To a Nightingale'/'To Autumn'等——'all his greatest poetry came that single year'（所有最伟大的诗都出自这一年——B395）。'On First Looking into Chapman's Homer'——1816商籁（B395）；Endymion——1818——四个1000行部分（B395）；1819年另有'Lamia'/'The Eve of St. Agnes'与未完成的许佩里翁史诗两稿（B395）。",
"timeline":[
 {"year":1795,"text":"10月31日生于伦敦（B395）。","src":"B395"},
 {"year":1816,"text":"'On First Looking into Chapman's Homer'——商籁（B395）。","src":"B395"},
 {"year":1818,"text":"Endymion——四个1000行部分（B395）。","src":"B395"},
 {"year":1819,"text":"1819颂歌年——'all his greatest poetry came that single year'（B395）。","src":"B395"},
 {"year":1821,"text":"2月23日卒于罗马，25岁（B395）。","src":"B395"}],
"major_works":[
 {"work_id":"songge1819","note":"1819（B395）"},
 {"title":"恩底弥翁","note":"（B395：Endymion (1818)——中译名待核）"},
 {"title":"许佩里翁的陨落","note":"（B395：The Fall of Hyperion——Notable Works——中译名待核）"}],
"style":["1819'颂歌年'的奇迹（B395）。",
 "'超越自然之美'走向'人类心灵的痛苦与挣扎'（B395 转述）。",
 "'简洁、直接、如画'措辞的浪漫派对应（无——B395未载风格语，不采）。（风格待核）"],
"status":"Britannica 定位济慈为英国浪漫主义诗人、1819年的奇迹（B395）。",
"sources":["B395"],"dates_source":"B395",
"pending":["'negative capability'术语——B395 正文未载（不采）。","'Beauty is truth'——仅问答标题（不采为引文）。","六颂歌清单核对（B395已载六题）。"]},
{"id":"shelley","name":"珀西·比希·雪莱","foreign_name":"Percy Bysshe Shelley（珀西·比希·雪莱，1792-08-04—1822-07-08）","country":"英国","birth":1792,"death":1822,"birth_year":1792,"death_year":1822,"era":"近代",
"summary":"雪莱，英国苏塞克斯Field Place生，浪漫主义诗人——1822年7月8日于意大利托斯卡纳海面覆舟溺亡，29岁（B396）。Prometheus Unbound（解放了的普罗米修斯）——1819年秋完成于佛罗伦萨——'inverts the plot of a lost play by Aeschylus'——'the keystone of Shelley's poetic achievement'（雪莱诗歌成就的基石——B396）。Ode to the West Wind（西风颂, 1819）——志在使其词语成为'an unextinguished hearth'的'Ashes and sparks'（B396）。Adonais——'in Spenserian stanzas'悼济慈（B396）。'Poets are the unacknowledged legislators of the world.'——《诗辨》（B396）。The Necessity of Atheism (1811)——被牛津开除（B396）。",
"timeline":[
 {"year":1792,"text":"8月4日生于苏塞克斯Field Place（B396）。","src":"B396"},
 {"year":1811,"text":"The Necessity of Atheism——被牛津开除（B396）。","src":"B396"},
 {"year":1819,"text":"《解放了的普罗米修斯》完成（佛罗伦萨秋）；《西风颂》（B396）。","src":"B396"},
 {"year":1821,"text":"Adonais——悼济慈；《诗辨》（B396）。","src":"B396"},
 {"year":1822,"text":"7月8日海难溺亡，29岁（B396）。","src":"B396"}],
"major_works":[
 {"work_id":"jiefangpu","note":"1819作/约1820刊（B396）"},
 {"work_id":"adonisi","note":"1821（B396）"},
 {"title":"西风颂","note":"（B396：Ode to the West Wind (1819)）"}],
"style":["'柔韧素体诗与繁复抒情格律'的混合（B396：supple blank verse...complex lyric measures）。",
 "'未熄的炉膛'之'灰烬与火星'（B396：Ashes and sparks）。",
 "'诗人是世间未被承认的立法者'（B396：《诗辨》引文）。"],
"status":"Britannica 定位雪莱为浪漫主义诗人、《解放了的普罗米修斯》为其'成就基石'（B396）。",
"sources":["B396"],"dates_source":"B396",
"pending":["《解放了的普罗米修斯》通行译名待核。","Adonais 引文两句（B396已载）完整核对。","玛丽·雪莱《弗兰克斯坦》1818（B396交叉）细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"songge1819","title":"1819年颂歌","original_title":"The Great Odes (1819)","region":"英国","era":"近代","era_detail":"19世纪10年代末",
"genre":"颂歌组","genre_group":"诗歌","language":"英语","author_id":"keats","author_name":"约翰·济慈",
"year_display":"1819年（Britannica B395：六颂歌——'On a Grecian Urn'/'To a Nightingale'/'To Autumn'等——'all his greatest poetry came that single year'）","year_sort":1819,
"background":["Britannica（B395）：1819颂歌——'On Indolence'/'On a Grecian Urn'/'To Psyche'/'To a Nightingale'/'On Melancholy'/'To Autumn'——'all his greatest poetry came that single year'。","Britannica（B395）：济慈——'died of tuberculosis in Rome in 1821 at the age of 25'。","题材（通说待核）：夜莺的古瓶与'秋'——感官的'颂'体。"],
"outline":["（通说待核）六颂的'感官'序列：听（夜莺）—看（古瓶）—触（秋）。","（通说待核）'负性能力'说（negative capability——B395正文未载，不采）。"],
"characters":[{"name":"抒情'我'","identity":"颂者","note":"（B395 语境）"}],
"themes":["'所有最伟大的诗都出自这一年'（B395）。",
 "颂歌体的感官化（通说待核）。",
 "'人类心灵的痛苦与挣扎'（B395 转述：the agony and strife of human hearts）。"],
"influence":[{"text":"Britannica：'all his greatest poetry came that single year'（B395）。","source":"B395"},{"text":"Britannica：六颂歌清单（B395）。","source":"B395"}],
"reading":{"difficulties":["颂歌体（ode stanza）。","1819年的传记语境（弟弟之死说——通说待核）。"],
 "editions":["《1819年颂歌》中译名（《济慈颂歌》）待核。","英文原版（公有领域）。"],
 "order":"济慈首选；与《恩底弥翁》对读。"},
"pending":["六颂歌清单核对（B395已载六题）。","'负性能力'术语——B395正文未载（不采）。","《希腊古瓮颂》细节待核（通说）。"],
"sources":["B395"],"year_source":"B395","author_source":"B395","related_works":["zuizhou","caihuaji","xuboliweng"],
"svg":G("《1819年颂歌》感官结构图",[{"title":"颂歌年","text":"'奇迹的一年'（B395）","color":"gold"},{"title":"夜莺","text":"听的颂（通说）","color":"main"},{"title":"古瓮","text":"看的颂（通说）","color":"family"},{"title":"秋","text":"触的颂（通说）","color":"antagonist"}])},
{"id":"jiefangpu","title":"解放了的普罗米修斯","original_title":"Prometheus Unbound","region":"英国","era":"近代","era_detail":"19世纪10年代末",
"genre":"抒情剧","genre_group":"戏剧","language":"英语","author_id":"shelley","author_name":"珀西·比希·雪莱",
"year_display":"1819年秋完成于佛罗伦萨、约1820年出版（Britannica B396——'the keystone of Shelley's poetic achievement'）","year_sort":1820,
"background":["Britannica（B396）：'inverts the plot of a lost play by Aeschylus'（颠倒埃斯库罗斯佚剧的情节——普罗米修斯与朱庇特和解改为推翻）。","Britannica（B396）：'supple blank verse with a variety of complex lyric measures'——'the keystone of Shelley's poetic achievement'。","Britannica（B396）：雪莱——1822年海难溺亡，29岁。"],
"outline":["（通说待核——B396未载剧情）被缚的普罗米修斯拒绝和解：朱庇特的倾覆与'爱'的解放。","（通说待核）阿特拉斯女与亚洲的'革命'晨曲（通说待核）。"],
"characters":[{"name":"普罗米修斯","identity":"被缚的泰坦","note":"（B396 书名人物）"},{"name":"朱庇特","identity":"暴君","note":"（通说待核）"}],
"themes":["'颠倒埃斯库罗斯'——和解改为推翻（B396：inverts the plot）。",
 "'雪莱诗歌成就的基石'（B396：keystone）。",
 "素体诗与抒情格律的混合（B396）。"],
"influence":[{"text":"Britannica：'the keystone of Shelley's poetic achievement'（B396）。","source":"B396"},{"text":"Britannica：《西风颂》同刊（B396 交叉）。","source":"B396"}],
"reading":{"difficulties":["抒情剧的'合唱'结构。","希腊神话原型（埃斯库罗斯佚剧——B396）。"],
 "editions":["《解放了的普罗米修斯》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"雪莱代表作；与《西风颂》《阿多尼》对读。"},
"pending":["四幕结构核对（通说）。","约1820年出版细节待核。","'推翻'结局与埃斯库罗斯原剧对照待核（B396已载inverts）。"],
"sources":["B396"],"year_source":"B396","author_source":"B396","related_works":["baofuodepuluo" if "baofuodepuluo" in existing else "leiyu","adonisi","xuboliweng"],
"svg":G("《解放了的普罗米修斯》基石结构图",[{"title":"普罗米修斯","text":"拒绝和解（B396：inverts）","color":"main"},{"title":"基石","text":"'诗歌成就的基石'（B396）","color":"gold"},{"title":"朱庇特","text":"倾覆的暴君（通说）","color":"antagonist"},{"title":"解放","text":"爱的黎明（通说）","color":"family"}])},
{"id":"adonisi","title":"阿多尼","original_title":"Adonais","region":"英国","era":"近代","era_detail":"19世纪20年代初",
"genre":"牧歌挽诗","genre_group":"诗歌","language":"英语","author_id":"shelley","author_name":"珀西·比希·雪莱",
"year_display":"1821年（Britannica B396：Adonais——'in Spenserian stanzas'悼济慈）","year_sort":1821,
"background":["Britannica（B396）：Adonais——'in Spenserian stanzas'悼济慈（1821）——引文'The One remains, the many change and pass;'/'Life, like a dome of many-coloured glass,'。","Britannica（B396）：雪莱——1822年海难——本作为其卒前一年之作。","题材（通说待核）：'阿多尼'（Adonis 原型）——济慈的'青春'之死。"],
"outline":["（通说待核）牧歌挽诗：'一'恒存而'多'流变（B396：'The One remains, the many change and pass;'）。","（通说待核）'彩色玻璃穹顶'般的生命（B396：'Life, like a dome of many-coloured glass,'）。"],
"characters":[{"name":"阿多尼","identity":"悼亡对象（济慈）","note":"（B396 书名人物——悼济慈）"}],
"themes":["'一'恒存与'多'流变（B396 引文）。",
 "'彩色玻璃穹顶'的生命（B396 引文）。",
 "斯宾塞体的挽歌（B396：Spenserian stanzas）。"],
"influence":[{"text":"Britannica：'in Spenserian stanzas'悼济慈（B396）。","source":"B396"},{"text":"Britannica：两句引文（B396 已载）。","source":"B396"}],
"reading":{"difficulties":["斯宾塞体九行节。","'阿多尼'神话原型（通说待核）。"],
 "editions":["《阿多尼》中译名（《阿多奈斯》）待核。","英文原版（公有领域）。"],
 "order":"雪莱挽歌首选；与《解放了的普罗米修斯》对读。"},
"pending":["引文两句完整核对（B396已载节选）。","1821年出版细节待核。","'济慈之死'背景核对（B395交叉：1821-02-23罗马肺结核）。"],
"sources":["B396"],"year_source":"B396","author_source":"B396","related_works":["jiefangpu","songge1819","diyuzhiji"],
"svg":G("《阿多尼》挽歌结构图",[{"title":"一","text":"'恒存'的哲学（B396引文）","color":"gold"},{"title":"多","text":"'流变'的世界（B396引文）","color":"antagonist"},{"title":"阿多尼","text":"悼济慈（B396）","color":"main"},{"title":"穹顶","text":"'彩色玻璃'的生命（B396引文）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B39x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('songge1819','keats'), ('jiefangpu','shelley'), ('adonisi','shelley')]:
    if wid in created:
        link(aid, wid)
print('BATCH71 DONE')
