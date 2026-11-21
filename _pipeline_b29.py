# -*- coding: utf-8 -*-
"""批29：Britannica 新核 3 作家 4 部（鲁尔福/伯尔x2/布扎蒂 B350-B352）"""
import json, pathlib

newsrc = [
{"id":"B350","title":"Heinrich Boll — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Heinrich-Boll","type":"百科全书","verified":True,"covers":["boll","xiaochou"],"note":"2026-11-21 核对：1917-12-21科隆生—1985-07-16科隆近郊Bornheim-Merten卒（67岁）；1972诺贝尔文学奖（1967毕希纳奖）；The Train Was on Time (1949)——'the grimness and despair of soldiers' lives'；Billiards at Half-Past Nine (1959)——'his most complex novel'（内心独白+闪回）；The Clown (1963)——主角'deteriorates through drinking from being a well-paid entertainer to a begging street musician'——批判社会伪善；Group Portrait with Lady (1971)——最长篇——'a panorama of German life'；The Lost Honour of Katharina Blum (1974)——'attacked modern journalistic ethics'；一战役6年（1938劳役+6年德军列兵/下士，俄线等）——受伤、逃离、被俘——'the frightful fate of being a soldier and having to wish that the war might be lost.'；罗马天主教和平主义者；'rubble literature'（废墟文学）；'the eras leading humanist interpreter of Germanys WWII experience'；The Silent Angel 写于1950、1992死后出版"},
{"id":"B351","title":"Dino Buzzati — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Dino-Buzzati","type":"百科全书","verified":True,"covers":["buzzati","datatarenshamo"],"note":"2026-11-21 核对：1906-10-16贝卢诺生—1972-01-28罗马卒（65岁）；1928年入米兰晚邮报——'He stayed with the newspaper for the rest of his life'；二战随意大利海军在非洲当随军记者；学法律未执业；Il deserto dei Tartari（鞑靼人沙漠, 1940，亦译 The Stronghold）——'generally considered Buzzatis finest'——边哨士兵'poised in expectancy for an enemy who never comes and unable to go forward or retreat'（等待永不来的敌人，不能前进也不能撤退）；早期山岳小说'introduced the Kafkaesque surrealism, symbolism, and absurdity'；'a modern Kafkaesque horror story'（Un caso clinico 1953）；'uniquely devastating skill and detached sense of irony and humor'；Sessanta racconti (1958)六十篇；Un amore (1963)；Il grande ritratto (1960)科幻"},
{"id":"B352","title":"Juan Rulfo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Juan-Rulfo","type":"百科全书","verified":True,"covers":["rulfo","peideluobalamo"],"note":"2026-11-21 核对：全名 Juan Nepomuceno Carlos Pérez Rulfo Vizcaíno；1917-05-16生（Apulco?——页面有研究者注记，生地存疑）—1986-01-07墨西哥城卒（68岁）；El llano en llamas（平原上的火焰, 1953）短篇集——多篇首发于 Pan 杂志；Pedro Páramo（佩德罗·巴拉莫, 1955）——'the physical and moral disintegration of a laconic cacique (boss)'——'set in a mythical hell on earth inhabited by the dead, who are haunted by their past transgressions'（死者居住的尘世地狱）；'considered one of the finest novelists and short-story creators in 20th-century Latin America'；'often seen as the last of the novelists of the Mexican Revolution'；短篇'depict the violence of the rural environment and the moral stagnation of its people'；技巧'stream of consciousness, flashbacks, and shifting points of view'；'an avowed follower of the American novelist William Faulkner'；影响马尔克斯等魔幻现实主义作家——'did not theorize about it'；童年目睹1926-29基督战争尾声；家产尽失；在墨西哥城做过橡胶公司与电影编剧；后任国立土著研究所编辑部主任"},
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
def find_work(aid, prefer=None):
    got = [p.stem for p in pathlib.Path('data/works').glob('*.json') if json.load(open(p, encoding='utf-8'))['author_id'] == aid]
    for pref in prefer or []:
        if pref in got: return pref
    return got[0] if got else None

def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

rel_pp = [rid(find_work('garciamarquez', ['bainianduguo']), 'ershishou'), rid(find_work('faulkner', []), 'xuanhuayusaodong'), rid('huoluan')]
rel_pp = list(dict.fromkeys(rel_pp))[:3]
rel_xc = [rid('katarinabulum'), rid('xueseziwuxian'), rid('zenodeyishi')]
rel_kb = [rid('xiaochou'), rid('xinshigudeLieshou'), rid('bao')]
rel_tt = [rid('chengbao'), rid('dengdaigou'), rid('moluoyi')]
print('rel:', rel_pp, rel_xc, rel_kb, rel_tt)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"rulfo","name":"胡安·鲁尔福","foreign_name":"Juan Rulfo（胡安·鲁尔福，全名 Juan Nepomuceno Carlos Pérez Rulfo Vizcaíno，1917-05-16—1986-01-07）","country":"墨西哥","birth":1917,"death":1986,"birth_year":1917,"death_year":1986,"era":"现当代",
"summary":"鲁尔福，墨西哥生（生地页面存疑——B352 研究者注记），墨西哥小说家——'considered one of the finest novelists and short-story creators in 20th-century Latin America'（B352）；'often seen as the last of the novelists of the Mexican Revolution'（常被视为墨西哥革命最后一位小说家——B352）。El llano en llamas（平原上的火焰, 1953）——短篇'depict the violence of the rural environment and the moral stagnation of its people'（B352）。Pedro Páramo（佩德罗·巴拉莫, 1955）——'the physical and moral disintegration of a laconic cacique (boss)'——'set in a mythical hell on earth inhabited by the dead'（B352）。技巧：'stream of consciousness, flashbacks, and shifting points of view'（B352）；'an avowed follower of the American novelist William Faulkner'（B352）；影响马尔克斯等魔幻现实主义作家——'did not theorize about it'（B352）。",
"timeline":[
 {"year":1917,"text":"5月16日生于墨西哥（生地存疑——B352 研究者注记）。","src":"B352"},
 {"year":1953,"text":"El llano en llamas（平原上的火焰）——短篇集（B352）。","src":"B352"},
 {"year":1955,"text":"Pedro Páramo（佩德罗·巴拉莫）（B352）。","src":"B352"},
 {"year":1986,"text":"1月7日卒于墨西哥城（B352）。","src":"B352"}],
"major_works":[
 {"work_id":"peideluobalamo","note":"1955（B352）"},
 {"title":"平原上的火焰","note":"（B352：El llano en llamas (1953)——中译名待核）"}],
"style":["'意识流、闪回与视点漂移'（B352）。",
 "福克纳的自觉追随者（B352）。",
 "乡村暴力的凝视（B352：violence of the rural environment）。"],
"status":"Britannica 定位鲁尔福为20世纪拉美最优秀的小说家/短篇家之一、魔幻现实主义的先声（B352）。",
"sources":["B352"],"dates_source":"B352",
"pending":["生地核对（Apulco? / San Gabriel说——B352 存疑注记）。","Comala 镇名核对（B352未载——通说）。","1955年出版史细节待核。"]},
{"id":"boll","name":"海因里希·伯尔","foreign_name":"Heinrich Böll（海因里希·伯尔，1917-12-21—1985-07-16）","country":"德国","birth":1917,"death":1985,"birth_year":1917,"death_year":1985,"era":"现当代",
"summary":"伯尔，科隆生，德国小说家——1972年诺贝尔文学奖（B350）。六年德军服役（列兵/下士，俄线等）——'the frightful fate of being a soldier and having to wish that the war might be lost.'（B350）。The Clown（小丑, 1963）——主角'deteriorates through drinking from being a well-paid entertainer to a begging street musician'——批判社会伪善（B350）；The Lost Honour of Katharina Blum（1974）——'attacked modern journalistic ethics'（B350）；Group Portrait with Lady (1971)——'a panorama of German life'（B350）。罗马天主教和平主义者；'rubble literature'（废墟文学）代表；'the eras leading humanist interpreter of Germanys WWII experience'（B350）。",
"timeline":[
 {"year":1917,"text":"12月21日生于科隆（B350）。","src":"B350"},
 {"year":1938,"text":"服强制劳役，此后六年德军服役——受伤、逃离、被俘（B350）。","src":"B350"},
 {"year":1949,"text":"The Train Was on Time——士兵生活的阴郁（B350）。","src":"B350"},
 {"year":1972,"text":"获诺贝尔文学奖（B350）。","src":"B350"},
 {"year":1985,"text":"7月16日卒于科隆近郊Bornheim-Merten（B350）。","src":"B350"}],
"major_works":[
 {"work_id":"xiaochou","note":"1963（B350）"},
 {"work_id":"katarinabulum","note":"1974（B350）"},
 {"title":"女士及众生相","note":"（B350：Group Portrait with Lady (1971)——中译名待核）"}],
"style":["'废墟文学'（B350：rubble literature）。",
 "简朴的散文与锋利的讽刺（B350：austere prose and sharp satire）。",
 "个人责任与和平主义（B350：Roman Catholic pacifist）。"],
"status":"Britannica 定位伯尔为1972诺奖得主、德国二战经验的'首要人文主义者'（B350）。",
"sources":["B350"],"dates_source":"B350",
"pending":["The Clown 通行译名（《小丑之见》/《小丑》）待核。","Katharina Blum 通行译名待核。","'废墟文学'提法出处（47年聚会说）待核。"]},
{"id":"buzzati","name":"迪诺·布扎蒂","foreign_name":"Dino Buzzati（迪诺·布扎蒂，1906-10-16—1972-01-28）","country":"意大利","birth":1906,"death":1972,"birth_year":1906,"death_year":1972,"era":"现当代",
"summary":"布扎蒂，贝卢诺生，意大利小说家、记者——1928年入米兰晚邮报，'He stayed with the newspaper for the rest of his life'（B351）；二战随意大利海军在非洲任随军记者（B351）。Il deserto dei Tartari（鞑靼人沙漠, 1940）——'generally considered Buzzatis finest'（B351）——边哨士兵'poised in expectancy for an enemy who never comes and unable to go forward or retreat'（等待永不来的敌人，不能前进亦不能撤退——B351）。早期山岳小说'introduced the Kafkaesque surrealism, symbolism, and absurdity'（B351）；其写作有'uniquely devastating skill and detached sense of irony and humor'（B351）。",
"timeline":[
 {"year":1906,"text":"10月16日生于贝卢诺（B351）。","src":"B351"},
 {"year":1928,"text":"入米兰晚邮报，终身未离（B351）。","src":"B351"},
 {"year":1940,"text":"Il deserto dei Tartari（鞑靼人沙漠）——其最佳（B351）。","src":"B351"},
 {"year":1972,"text":"1月28日卒于罗马（B351）。","src":"B351"}],
"major_works":[
 {"work_id":"datatarenshamo","note":"1940（B351）"},
 {"title":"六十篇","note":"（B351：Sessanta racconti (1958)——中译名待核）"},
 {"title":"爱","note":"（B351：Un amore (1963)——中译名待核）"}],
"style":["卡夫卡式的超现实与荒诞（B351：Kafkaesque surrealism, symbolism, and absurdity）。",
 "疏离的反讽与幽默（B351：detached sense of irony）。",
 "'等待'的主题（B351：expectancy for an enemy who never comes）。"],
"status":"Britannica 定位布扎蒂为晚邮报终身记者、《鞑靼人沙漠》为其最佳（B351）。",
"sources":["B351"],"dates_source":"B351",
"pending":["《鞑靼人沙漠》通行译名两说（/《鞑靼人草原》）待核。","堡名（Bastiani说）待核（B351未载）。","德罗戈人名待核（B351未载）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"peideluobalamo","title":"佩德罗·巴拉莫","original_title":"Pedro Páramo","region":"墨西哥","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"rulfo","author_name":"胡安·鲁尔福",
"year_display":"1955年（Britannica B352：Pedro Páramo (1955)）","year_sort":1955,
"background":["Britannica（B352）：'the physical and moral disintegration of a laconic cacique (boss)'——一个寡言'考迪略'（头领）的肉体与道德解体。","Britannica（B352）：'set in a mythical hell on earth inhabited by the dead, who are haunted by their past transgressions'——死者居住的尘世地狱，亡魂被其生前罪愆纠缠。","Britannica（B352）：鲁尔福——'an avowed follower of the American novelist William Faulkner'；影响马尔克斯等魔幻现实主义作家。"],
"outline":["亡魂的村庄：'我'寻父而入死者的尘世地狱（B352：mythical hell on earth inhabited by the dead——村名 Comala 通说待核）。","佩德罗·巴拉莫的解体：从考迪略到废墟（B352：physical and moral disintegration）。"],
"characters":[{"name":"佩德罗·巴拉莫","identity":"考迪略/头领","note":"（B352：laconic cacique）"},{"name":"胡安·普雷西亚多","identity":"寻父之子","note":"（通说待核，B352未载）"}],
"themes":["死者的地狱：记忆与罪愆（B352）。",
 "考迪略的解体（B352）。",
 "'意识流、闪回与视点漂移'（B352：techniques）。"],
"influence":[{"text":"Britannica：影响马尔克斯等魔幻现实主义作家（B352）。","source":"B352"},{"text":"Britannica：'often seen as the last of the novelists of the Mexican Revolution'（B352）。","source":"B352"}],
"reading":{"difficulties":["亡魂对话的叙事混乱（有意为之）。","墨西哥革命与基督战争背景（B352 语境）。"],
 "editions":["《佩德罗·巴拉莫》中译本（人民文学/译林等——通说待核）。","西班牙文原版。"],
 "order":"鲁尔福首选；后接《平原上的火焰》(1953)。"},
"pending":["Comala 镇名核对（B352未载）。","胡安·普雷西亚多人名核对（B352未载）。","'魔幻现实主义先声'的学术定位待核。"],
"sources":["B352"],"year_source":"B352","author_source":"B352","related_works":rel_pp,
"svg":G("《佩德罗·巴拉莫》亡灵结构图",[{"title":"尘世地狱","text":"死者的村庄（B352）","color":"antagonist"},{"title":"佩德罗·巴拉莫","text":"考迪略的解体（B352）","color":"main"},{"title":"寻父","text":"生者入亡魂之地（通说）","color":"gold"},{"title":"罪愆","text":"纠缠的记忆（B352）","color":"family"}])},
{"id":"xiaochou","title":"小丑之见","original_title":"Ansichten eines Clowns","region":"德国","era":"现当代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"boll","author_name":"海因里希·伯尔",
"year_display":"1963年（Britannica B350：The Clown (Ansichten eines Clowns, 1963)）","year_sort":1963,
"background":["Britannica（B350）：The Clown——主角'deteriorates through drinking from being a well-paid entertainer to a begging street musician'（借酒沉沦：从高薪滑稽演员到街头卖艺乞丐）。","Britannica（B350）：本作'critiques societal hypocrisy'（批判社会伪善）。","Britannica（B350）：伯尔——'the eras leading humanist interpreter of Germanys WWII experience'；罗马天主教和平主义者。"],
"outline":["小丑汉斯的自述：一日之间从舞台到街头（B350：deteriorates through drinking；人物名与一日结构通说待核）。","天主教中产社会的伪善：婚姻、教义与金钱（B350：critiques societal hypocrisy）。"],
"characters":[{"name":"汉斯·施尼尔","identity":"小丑","note":"（通说待核，B350未载）"}],
"themes":["社会伪善的批判（B350）。",
 "沉沦与尊严（B350：deteriorates through drinking）。",
 "天主教中产的婚姻伦理（通说待核）。"],
"influence":[{"text":"Britannica：伯尔1972年诺奖——'the eras leading humanist interpreter of Germanys WWII experience'（B350）。","source":"B350"},{"text":"Britannica：'austere prose and sharp satire'（B350）。","source":"B350"}],
"reading":{"difficulties":["西德天主教社会背景。","'一日结构'的自述形式（通说待核）。"],
 "editions":["《小丑之见》中译本（人民文学/上海译文等——通说待核）。","德文原版。"],
 "order":"伯尔首选；后接《丧失名誉的卡塔琳娜·布鲁姆》。"},
"pending":["汉斯·施尼尔等人名核对（B350未载）。","'一日结构'说法待核。","1963年出版（Kiepenheuer & Witsch说）待核。"],
"sources":["B350"],"year_source":"B350","author_source":"B350","related_works":rel_xc,
"svg":G("《小丑之见》沉沦结构图",[{"title":"小丑","text":"从舞台到街头（B350）","color":"main"},{"title":"伪善","text":"社会的靶心（B350）","color":"antagonist"},{"title":"天主教","text":"和平主义者的目光（B350）","color":"gold"},{"title":"沉沦","text":"借酒的滑落（B350）","color":"family"}])},
{"id":"katarinabulum","title":"丧失名誉的卡塔琳娜·布鲁姆","original_title":"Die verlorene Ehre der Katharina Blum","region":"德国","era":"现当代","era_detail":"20世纪70年代",
"genre":"中篇小说","genre_group":"小说","language":"德语","author_id":"boll","author_name":"海因里希·伯尔",
"year_display":"1974年（Britannica B350：The Lost Honour of Katharina Blum (1974)）","year_sort":1974,
"background":["Britannica（B350）：'attacked modern journalistic ethics'（抨击现代新闻伦理）与德国价值观。","Britannica（B350）：伯尔——'personal responsibility'的反复主题；1972诺奖。","题材（通说待核）：无辜女子被小报摧毁——'名誉'的媒体绞杀。"],
"outline":["'新闻自由'如何毁灭一个普通人：报道、审讯与名誉的丧失（B350：attacked modern journalistic ethics；情节通说待核）。","暴力与媒体的共谋（通说待核）。"],
"characters":[{"name":"卡塔琳娜·布鲁姆","identity":"女管家","note":"（B350 书名人物）"},{"name":"托特格斯","identity":"记者","note":"（通说待核，B350未载）"}],
"themes":["新闻伦理的批判（B350）。",
 "'名誉'的社会机制（B350 书名）。",
 "个人责任（B350：recurring focus on personal responsibility）。"],
"influence":[{"text":"Britannica：'attacked modern journalistic ethics'（B350）。","source":"B350"},{"text":"Britannica：1977年电影改编说待核（B348式'多部改编'未载本作——不采）。","source":"B350"}],
"reading":{"difficulties":["1970年代西德恐怖主义背景（巴德尔-迈因霍夫说待核）。","新闻文体拼贴（通说待核）。"],
 "editions":["《丧失名誉的卡塔琳娜·布鲁姆》中译本（人民文学等——通说待核）。","德文原版。"],
 "order":"伯尔进阶；与《小丑之见》对读。"},
"pending":["托特格斯人名核对（B350未载）。","1977年施隆多夫电影说待核。","'新闻拼贴'文体细节待核。"],
"sources":["B350"],"year_source":"B350","author_source":"B350","related_works":rel_kb,
"svg":G("《卡塔琳娜·布鲁姆》名誉绞杀图",[{"title":"卡塔琳娜","text":"被摧毁的普通人（B350）","color":"main"},{"title":"小报","text":"新闻伦理的靶子（B350）","color":"antagonist"},{"title":"名誉","text":"社会的绞索（B350）","color":"gold"},{"title":"审讯","text":"体制的共谋（通说）","color":"family"}])},
{"id":"datatarenshamo","title":"鞑靼人沙漠","original_title":"Il deserto dei Tartari","region":"意大利","era":"现当代","era_detail":"20世纪30年代末",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"buzzati","author_name":"迪诺·布扎蒂",
"year_display":"1940年（Britannica B351：Il deserto dei Tartari (1940；亦译 The Stronghold)——'generally considered Buzzatis finest'）","year_sort":1940,
"background":["Britannica（B351）：'generally considered Buzzatis finest'——边哨士兵'poised in expectancy for an enemy who never comes and unable to go forward or retreat'（等待永不来的敌人，不能前进亦不能撤退）。","Britannica（B351）：布扎蒂早期山岳小说'introduced the Kafkaesque surrealism, symbolism, and absurdity'；受卡夫卡影响而有其'own ironic, detached humor'。","Britannica（B351）：布扎蒂——晚邮报终身记者。"],
"outline":["边疆要塞的等待：士兵们终身守候从不来的'鞑靼人'（B351：expectancy for an enemy who never comes；堡名与人物名通说待核）。","'不能前进亦不能撤退'：一生的消耗（B351）。"],
"characters":[{"name":"德罗戈","identity":"新兵","note":"（通说待核，B351未载）"},{"name":"堡","identity":"要塞","note":"（B351：frontier post——名待核）"}],
"themes":["等待的荒诞（B351）。",
 "'不能前进亦不能撤退'的存在困境（B351）。",
 "卡夫卡式荒诞的意大利化（B351：Kafkaesque surrealism）。"],
"influence":[{"text":"Britannica：'generally considered Buzzatis finest'（B351）。","source":"B351"},{"text":"Britannica：'detached sense of irony and humor'（B351）。","source":"B351"}],
"reading":{"difficulties":["'等待'的时间感（一生与一日的交错）。","与《城堡》《等待戈多》的互文。"],
 "editions":["《鞑靼人沙漠》中译本（人民文学/上海译文等——通说待核）。","意大利文原版。"],
 "order":"布扎蒂首选；可与《城堡》《等待戈多》对读。"},
"pending":["德罗戈人名核对（B351未载）。","堡名（Bastiani说）待核。","1976年电影改编说待核。"],
"sources":["B351"],"year_source":"B351","author_source":"B351","related_works":rel_tt,
"svg":G("《鞑靼人沙漠》等待结构图",[{"title":"要塞","text":"边哨的一生（B351）","color":"family"},{"title":"鞑靼人","text":"从不来的敌人（B351）","color":"antagonist"},{"title":"等待","text":"'不能进亦不能退'（B351）","color":"main"},{"title":"荒诞","text":"卡夫卡式的荒原（B351）","color":"gold"}])},
]
for w in works:
    if w['id'] in existing:
        print('skip existing', w['id'])
for w in works:
    if w['id'] in existing:
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("rulfo","peideluobalamo"),("boll","xiaochou"),("boll","katarinabulum"),("buzzati","datatarenshamo")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B35x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH29 DONE')
