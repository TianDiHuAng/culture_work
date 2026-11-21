# -*- coding: utf-8 -*-
"""批42：Britannica 新核 2 作家 2 部（萨福 B364/拉伯雷 B365）"""
import json, pathlib

newsrc = [
{"id":"B364","title":"Sappho — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Sappho-Greek-poet","type":"百科全书","verified":True,"covers":["sappho","safucanpian"],"note":"2026-11-21 核对：约前610生于莱斯博斯岛—约前570卒；'Greek lyric poet greatly admired in all ages for the beauty of her writing style'；与阿尔基洛科斯、阿尔凯奥斯并列——'her ability to impress readers with a lively sense of her personality'；'Her phrasing is concise, direct, and picturesque'；爱奥利亚方言与传统+史诗词汇；主题几乎全为个人——围绕其 thiasos（女性社群）——以阿佛洛狄忒为守护神；'In the ode to Aphrodite, the poet invokes the goddess...to be her ally in persuading a girl she desires to love her'；婚礼歌（epithalamia）占重要部分；亚历山大里亚学者编九卷抒情诗集（按格律分卷）——中世纪后散佚；'Only the ode to Aphrodite, 28 lines long, is complete'——次长残篇16行；1898年起纸草发现大增残篇；兄弟 Larichus 与 Charaxus；女儿 Cleis；'leaped from the Leucadian rock'为 Phaon 事为传说；'married to Cercylas'说被多数现代学者视为传说；一生大部分在莱斯博斯米蒂利尼"},
{"id":"B365","title":"Francois Rabelais — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Francois-Rabelais","type":"百科全书","verified":True,"covers":["rabelais","jurenzhuan"],"note":"2026-11-21 核对：约1483-94生于希农附近Seuilly——卒于1553-04-09（约）巴黎；'the French writer responsible for the comic masterpiece Gargantua and Pantagruel'（1532-1564间出版）；五部小说（第五部作者存疑）——'rich use of Renaissance French'——'comedy...ranges from gross burlesque to profound satire'；医生与人文ist：1530蒙彼利埃学医、1532里主宫医院医生；1532以笔名 Alcofribas Nasier 出版 Pantagruel——被索邦斥为淫秽但'became a popular success'；巨人 Panurge 首次登场；Gargantua 约1534/1535——德廉美修道院（Abbaye de Thélème）'rejects poverty, celibacy, and obedience'；Tiers livre (1546)——'Rabelais's most profound work'——Panurge 的婚姻咨询；Quart livre (1552)——'his longest book'；索邦与巴黎高等法院多次禁书；'Rabelais used scatology aesthetically, not gratuitously'；披着人文主义保护的生涯：纪·杜·贝莱红衣主教等庇护人"},
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
{"id":"sappho","name":"萨福","foreign_name":"Sappho（萨福，约公元前610—约公元前570）","country":"希腊","birth":None,"death":None,"birth_year":-610,"death_year":-570,"era":"古代",
"summary":"萨福，约前610生于莱斯博斯岛、约前570卒——'Greek lyric poet greatly admired in all ages for the beauty of her writing style'（B364）；与阿尔基洛科斯、阿尔凯奥斯并列——'her ability to impress readers with a lively sense of her personality'（B364）；'Her phrasing is concise, direct, and picturesque'（B364）。爱奥利亚方言入诗（B364）。主题几乎全为个人——围绕其领导的女性社群 thiasos，以阿佛洛狄忒为守护神（B364）；婚礼歌（epithalamia）占重要部分（B364）。亚历山大里亚学者编九卷集，后散佚——'Only the ode to Aphrodite, 28 lines long, is complete'（B364）。",
"timeline":[
 {"year":-610,"text":"约前610生于莱斯博斯岛（B364：born c. 610, Lesbos）。","src":"B364"},
 {"year":-600,"text":"亚历山大里亚编九卷本（后世编订——B364 语境）。","src":"B364"},
 {"year":-570,"text":"约前570卒（B364：died c. 570 bce）。","src":"B364"}],
"major_works":[
 {"work_id":"safucanpian","note":"残篇（B364：九卷本散佚——仅《阿佛洛狄忒颂》28行完整）"},
 {"title":"阿佛洛狄忒颂","note":"（B364：ode to Aphrodite——唯一完整诗，28行）"}],
"style":["'简洁、直接、如画'的措辞（B364：concise, direct, and picturesque）。",
 "爱奥利亚方言与传统（B364）。",
 "'以平静追忆激情'（B364：recollected in tranquillity）。"],
"status":"Britannica 定位萨福为希腊抒情诗的巅峰、与阿尔基洛科斯/阿尔凯奥斯并列（B364）。",
"sources":["B364"],"dates_source":"B364",
"pending":["生卒年（约前610/约前570——B364 口径）细节待核。","'萨福体'（Sapphic stanza）术语待核（B364未载）。","勒卡迪亚岩跳海传说为 legend（B364 已载——不采为事实）。"]},
{"id":"rabelais","name":"弗朗索瓦·拉伯雷","foreign_name":"François Rabelais（弗朗索瓦·拉伯雷，约1483-94—1553-04-09约）","country":"法国","birth":None,"death":1553,"birth_year":1490,"death_year":1553,"era":"古代",
"summary":"拉伯雷，希农附近 Seuilly 生（约1483-94），卒于约1553年4月9日巴黎——'the French writer responsible for the comic masterpiece Gargantua and Pantagruel'（B365）。医生与人文主义者：1530年蒙彼利埃学医、1532年里昂主宫医院医生（B365）。Pantagruel (1532)——笔名 Alcofribas Nasier 出版——被索邦斥为淫秽但'became a popular success'（B365）；Gargantua (约1534/1535)——德廉美修道院'rejects poverty, celibacy, and obedience'（B365）；Tiers livre (1546)——'Rabelais's most profound work'（B365）；Quart livre (1552)——'his longest book'（B365）。'Rabelais used scatology aesthetically, not gratuitously'（B365）。",
"timeline":[
 {"year":1490,"text":"约1483-94年间生于希农附近Seuilly（B365）。","src":"B365"},
 {"year":1530,"text":"蒙彼利埃大学学医（B365）。","src":"B365"},
 {"year":1532,"text":"以笔名出版 Pantagruel——索邦斥为淫秽但畅销（B365）。","src":"B365"},
 {"year":1546,"text":"Tiers livre——'最深刻的作品'——再遭索邦斥责、逃亡梅斯（B365）。","src":"B365"},
 {"year":1553,"text":"约4月9日卒于巴黎（B365）。","src":"B365"}],
"major_works":[
 {"work_id":"jurenzhuan","note":"五部（B365：1532-1564）"},
 {"title":"第三书","note":"（B365：Tiers livre (1546)——'his most profound work'）"}],
"style":["文艺复兴法语的丰富词汇（B365：rich use of Renaissance French）。",
 "从粗野滑稽到深刻讽刺（B365：gross burlesque to profound satire）。",
 " aesthetically 的秽语书写（B365）。"],
"status":"Britannica 定位拉伯雷为《高康大与庞大固埃》的作者、16世纪法国文学史上的持久地位（B365）。",
"sources":["B365"],"dates_source":"B365",
"pending":["生年（1483-94区间）待核。","第五书作者存疑（B365：authorship disputed）。","'Rabelaisian'术语待核（B365 有载：misleading）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"safucanpian","title":"萨福诗残篇","original_title":"Fragments（九卷本散佚残篇）","region":"希腊","era":"古代","era_detail":"公元前7-6世纪",
"genre":"抒情诗（残篇）","genre_group":"诗歌","language":"希腊语（爱奥利亚方言）","author_id":"sappho","author_name":"萨福",
"year_display":"约公元前600年（Britannica B364：约前610-约前570——亚历山大里亚九卷本编订后世散佚）","year_sort":-600,
"background":["Britannica（B364）：'greatly admired in all ages for the beauty of her writing style'——措辞'concise, direct, and picturesque'。","Britannica（B364）：主题围绕其女性社群 thiasos——阿佛洛狄忒为守护神；'Only the ode to Aphrodite, 28 lines long, is complete'——次长残篇16行。","Britannica（B364）：婚礼歌（epithalamia）占 oeuvre 的重要部分；1898年起纸草发现使残篇大增。"],
"outline":["《阿佛洛狄忒颂》（唯一完整，28行）：向女神求援以说服所爱（B364）。","残篇中的婚礼歌与花环、香膏等阿佛洛狄忒仪式意象（B364：flowers, bright garlands...altars smoking with incense）。"],
"characters":[{"name":"抒情'我'","identity":"社群的引领者","note":"（B364：thiasos 语境）"},{"name":"阿佛洛狄忒","identity":"守护神","note":"（B364：tutelary divinity）"}],
"themes":["激情作为'女神所驱使的不可逃避之力'（B364：love is passion, an inescapable power）。",
 "女性社群与教育（B364：thiasos——education of young women）。",
 "回忆与乡愁（B364：nostalgia and memory）。"],
"influence":[{"text":"Britannica：'the beauty of her writing style'（B364）。","source":"B364"},{"text":"Britannica：与阿尔基洛科斯、阿尔凯奥斯并列（B364）。","source":"B364"}],
"reading":{"difficulties":["残篇的断裂性。","爱奥利亚方言（读译本）。"],
 "editions":["《萨福诗残篇》中译本（人民文学/上海三联等——通说待核）。","希腊语原版（公有领域）。"],
 "order":"希腊抒情诗首选；与《神谱》等对读。"},
"pending":["'萨福体'诗节术语待核（B364未载）。","残篇编号体系（Lobel-Page等）待核。","'九卷'编订细节待核（B364口径）。"],
"sources":["B364"],"year_source":"B364","author_source":"B364","related_works":["xuboliweng","diyuzhiji","shenhua" if "shenhua" in existing else "leiyu"],
"svg":G("萨福残篇抒情结构图",[{"title":"阿佛洛狄忒","text":"唯一完整的28行（B364）","color":"gold"},{"title":"thiasos","text":"女性社群（B364）","color":"family"},{"title":"激情","text":"女神驱使的力量（B364）","color":"main"},{"title":"残篇","text":"纸草的馈赠（B364）","color":"antagonist"}])},
{"id":"jurenzhuan","title":"巨人传","original_title":"La vie de Gargantua et de Pantagruel","region":"法国","era":"古代","era_detail":"16世纪30-60年代",
"genre":"长篇小说（五部）","genre_group":"小说","language":"法语","author_id":"rabelais","author_name":"弗朗索瓦·拉伯雷",
"year_display":"1532-64年（Britannica B365：Gargantua and Pantagruel——'published between 1532 and 1564'）","year_sort":1532,
"background":["Britannica（B365）：'the comic masterpiece'——五部小说（第五部作者存疑）——'rich use of Renaissance French'——comedy 'from gross burlesque to profound satire'。","Britannica（B365）：Pantagruel (1532)——笔名 Alcofribas Nasier——索邦斥为淫秽但'became a popular success'——巨人 Panurge 首次登场。","Britannica（B365）：Gargantua——德廉美修道院'rejects poverty, celibacy, and obedience'——Frère Jean 的形象；Tiers livre (1546)——'his most profound work'——Panurge 的婚姻咨询；Quart livre (1552)——'his longest book'。"],
"outline":["《庞大固埃》(1532)：巨人与狡黠的 Panurge（B365：mock-heroic framework——细节通说待核）。","《高康大》(约1534)：巨人的诞生/教育与比克罗肖尔战争、德廉美修道院（B365：Abbaye de Thélème）。","第三书(1546)：Panurge 婚否的咨询与'神瓶'之旅的开端（B365：most profound work）；第四书(1552)与第五书(1564，作者存疑)：'喝'的神谕（B365：oraculous advice: 'drink'）。"],
"characters":[{"name":"高康大","identity":"巨人父亲","note":"（B365：Gargantua）"},{"name":"庞大固埃","identity":"巨人儿子","note":"（B365：Pantagruel）"},{"name":"巴汝奇（Panurge）","identity":"狡黠的伙伴","note":"（B365：a cunning and witty rogue）"}],
"themes":["从粗野滑稽到深刻讽刺（B365）。",
 "人文主义教育对经院哲学的嘲笑（B365：Old-fashioned scholastic pedagogy is ridiculed）。",
 "'德廉美'：拒绝贫穷/独身/服从的理想院（B365）。"],
"influence":[{"text":"Britannica：'comic masterpiece'定位（B365）。","source":"B365"},{"text":"Britannica：'Rabelaisian'一词进入语言（B365：adjective Rabelaisian）。","source":"B365"}],
"reading":{"difficulties":["五部书的次序（庞→高→三→四→五）。","文艺复兴法语与双关语。"],
 "editions":["《巨人传》中译本（人民文学/上海译文等——通说待核）。","法文原版（公有领域）。"],
 "order":"文艺复兴小说首选；与《堂吉诃德》对读。"},
"pending":["五部书名与年份核对（B365口径）。","'神瓶'神谕的解读（'喝'=智慧？——B365）待核。","成书次序（庞大固埃先于高康大）核对。"],
"sources":["B365"],"year_source":"B365","author_source":"B365","related_works":["tangjihuade","xunjiexiaoshuo","mingnuzhuan"],
"svg":G("《巨人传》讽刺结构图",[{"title":"巨人","text":"夸张的躯体（B365）","color":"main"},{"title":"德廉美","text":"理想的修道院（B365）","color":"gold"},{"title":"索邦","text":"禁书的靶子（B365）","color":"antagonist"},{"title":"'喝'","text":"神瓶的智慧（B365）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B36x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('safucanpian','sappho'), ('jurenzhuan','rabelais')]:
    if wid in created:
        link(aid, wid)
print('BATCH42 DONE')
