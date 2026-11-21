# -*- coding: utf-8 -*-
"""批77：Britannica 新核 2 作家 4 部（杰克·伦敦 B407×2/保罗·奥斯特 B408 纽约三部曲）"""
import json, pathlib

newsrc = [
{"id":"B407","title":"Jack London — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jack-London","type":"百科全书","verified":True,"covers":["jackson","yexingdehuhuan"],"note":"2026-11-21 核对：原名 John Griffith Chaney；1876-01-12旧金山生—1916-11-22加州Glen Ellen卒（40岁）；The Call of the Wild（野性的呼唤, 1903）——Buck（圣伯纳/苏格兰牧羊犬混血）雪橇犬之旅——'often considered to be Jack London's masterpiece'——最广为阅读；White Fang（白牙, 1906）——'dramatized in turn atavism, adaptability, and the appeal of the wilderness'；Martin Eden（马丁·伊登, 1909）——自传小说——乐观与活力'best conveyed in his autobiographical novel Martin Eden'；The Iron Heel（铁蹄, 1908）——'a fantasy of the future that is a terrifying anticipation of fascism'；'To Build a Fire' (1908)——'masterly depiction of humankind's inability to overcome nature'；The Sea-Wolf (1904)——'Nietzschean superman hero, Humphrey Van Weyden'；The Son of the Wolf (1900)首部书；离开加州大学伯克利一年——'to seek a fortune in the Klondike gold rush'——空手而归改行写作；1894年'became a militant socialist'——'maintained his socialist beliefs almost to the end of his life'；图书馆自学达尔文/马克思/尼采；17年写'约50本'——'the highest-paid writer in the United States at that time'；20世纪译最多的美国作家之一；二战后俄国风行"},
{"id":"B408","title":"Paul Auster — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Paul-Auster","type":"百科全书","verified":True,"covers":["auster","niuyuesanbuqu"],"note":"2026-11-21 核对：1947-02-03新泽西Newark生—2024-04-30布鲁克林卒（77岁）；'gained renown for a series of experimental detective stories published collectively as The New York Trilogy (1987)'——实验侦探小说系列：City of Glass (1985)——犯罪小说家被卷入谜案承担多重身份；Ghosts (1986)——私家侦探Blue受雇于White调查Black；The Locked Room (1986)——作家研究失踪作者渐取其身份；'often concerned with the search for identity and personal meaning'（常关注身份与个人意义的追寻）；The Invention of Solitude (1982)——'both a memoir about the death of his father and a meditation on the act of writing'（父亡回忆+写作冥想）；4 3 2 1 (2017)——七年首部长篇——主角 Archie Ferguson 'experiences four alternate lives'；Moon Palace (1989)、Leviathan (1992)、The Book of Illusions (2002)、Smoke 剧本 (1995)"},
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
{"id":"jackson","name":"杰克·伦敦","foreign_name":"Jack London（杰克·伦敦，原名 John Griffith Chaney，1876-01-12—1916-11-22）","country":"美国","birth":1876,"death":1916,"birth_year":1876,"death_year":1916,"era":"近代",
"summary":"伦敦，旧金山生（原名 John Griffith Chaney），美国作家——The Call of the Wild（野性的呼唤, 1903）——'often considered to be Jack London's masterpiece'（常被认为其杰作——B407）——最广为阅读。Martin Eden（马丁·伊登, 1909）——自传小说（B407）。The Iron Heel（铁蹄, 1908）——'a fantasy of the future that is a terrifying anticipation of fascism'（对法西斯主义的可怖预言——B407）。'To Build a Fire' (1908)——'masterly depiction of humankind's inability to overcome nature'（B407）。1894年'became a militant socialist'——'maintained his socialist beliefs almost to the end of his life'（B407）。17年写约50本书——'the highest-paid writer in the United States at that time'（B407）。",
"timeline":[
 {"year":1876,"text":"1月12日生于旧金山（B407）。","src":"B407"},
 {"year":1897,"text":"赴克朗代克淘金——空手而归改行写作（B407：left UC Berkeley after one year to seek a fortune in the Klondike gold rush）。","src":"B407"},
 {"year":1903,"text":"《野性的呼唤》——常被认为其杰作（B407）。","src":"B407"},
 {"year":1909,"text":"《马丁·伊登》——自传小说（B407）。","src":"B407"},
 {"year":1916,"text":"11月22日卒于加州Glen Ellen（B407）。","src":"B407"}],
"major_works":[
 {"work_id":"yexingdehuhuan","note":"1903（B407）"},
 {"work_id":"madingyideng","note":"1909（B407）"},
 {"title":"铁蹄","note":"（B407：The Iron Heel (1908)）"}],
"style":["克朗代克淘金的北方书写（B407：Klondike gold rush）。",
 "'是法西斯主义可怖预言'的未来幻想（B407：The Iron Heel）。",
 "'人类无法战胜自然'的描写（B407：To Build a Fire）。"],
"status":"Britannica 定位伦敦为《野性的呼唤》作者、当时美国稿酬最高的作家（B407）。",
"sources":["B407"],"dates_source":"B407",
"pending":["《野性的呼唤》通行译名待核。","'最高稿酬'口径核对（B407：highest-paid writer at that time）。","社会主义活动细节（B407）待核。"]},
{"id":"auster","name":"保罗·奥斯特","foreign_name":"Paul Auster（保罗·奥斯特，1947-02-03—2024-04-30）","country":"美国","birth":1947,"death":2024,"birth_year":1947,"death_year":2024,"era":"现当代",
"summary":"奥斯特，新泽西Newark生，美国作家——2024年4月30日卒于布鲁克林（77岁）（B408）。'gained renown for a series of experimental detective stories published collectively as The New York Trilogy (1987)'（实验侦探小说系列《纽约三部曲》——B408）：City of Glass (1985)——犯罪小说家被卷入谜案承担多重身份；Ghosts (1986)——私家侦探 Blue 受雇于 White 调查 Black；The Locked Room (1986)——作家研究失踪作者渐取其身份（B408）。'often concerned with the search for identity and personal meaning'（常关注身份与个人意义的追寻——B408）。The Invention of Solitude (1982)——'both a memoir about the death of his father and a meditation on the act of writing'（B408）。4 3 2 1 (2017)——主角 Archie Ferguson 'experiences four alternate lives'（B408）。",
"timeline":[
 {"year":1947,"text":"2月3日生于新泽西Newark（B408）。","src":"B408"},
 {"year":1982,"text":"The Invention of Solitude——父亡回忆+写作冥想（B408）。","src":"B408"},
 {"year":1987,"text":"《纽约三部曲》合集出版（B408）。","src":"B408"},
 {"year":2017,"text":"4 3 2 1——七年首部长篇（B408）。","src":"B408"},
 {"year":2024,"text":"4月30日卒于布鲁克林（B408）。","src":"B408"}],
"major_works":[
 {"work_id":"niuyuesanbuqu","note":"1987（B408）"},
 {"title":"孤独及其所创造的","note":"（B408：The Invention of Solitude (1982)——中译名待核）"},
 {"title":"4 3 2 1","note":"（B408：2017——四种平行人生）"}],
"style":["'实验侦探小说'（B408：experimental detective stories）。",
 "'身份与个人意义的追寻'（B408：search for identity and personal meaning）。",
 "玻璃城的'多重身份'（B408：City of Glass 语境）。"],
"status":"Britannica 定位奥斯特为《纽约三部曲》作者、2024年卒（B408）。",
"sources":["B408"],"dates_source":"B408",
"pending":["《纽约三部曲》通行译名待核。","'烟'（Smoke 1995——B408）剧本细节待核。","与妻子 Siri Hustvedt 合著说待核（B408未载——不采）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"yexingdehuhuan","title":"野性的呼唤","original_title":"The Call of the Wild","region":"美国","era":"近代","era_detail":"20世纪初",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"jackson","author_name":"杰克·伦敦",
"year_display":"1903年（Britannica B407：The Call of the Wild (1903)——'often considered to be Jack London's masterpiece'）","year_sort":1903,
"background":["Britannica（B407）：Buck——圣伯纳/苏格兰牧羊犬混血雪橇犬之旅——'often considered to be Jack London's masterpiece'——最广为阅读。","Britannica（B407）：伦敦——克朗代克淘金（'to seek a fortune in the Klondike gold rush'）——空手而归改行写作。","Britannica（B407）：伦敦——1894年'became a militant socialist'。"],
"outline":["（通说待核——B407未载剧情）巴克被偷卖至北方：雪橇犬的'野性呼唤'。","（通说待核）桑顿的爱与荒野的最终回归。"],
"characters":[{"name":"巴克（Buck）","identity":"混血雪橇犬","note":"（B407：a St. Bernard/Scotch collie mix）"},{"name":"约翰·桑顿","identity":"最后的主人","note":"（通说待核）"}],
"themes":["'野性的呼唤'：文明的褪去（书名语境——通说待核）。",
 "克朗代克的北方（B407：Klondike gold rush）。",
 "自然主义与'适者生存'（通说待核）。"],
"influence":[{"text":"Britannica：'often considered to be Jack London's masterpiece'（B407）。","source":"B407"},{"text":"Britannica：'most widely read work'（B407）。","source":"B407"}],
"reading":{"difficulties":["动物视点的叙述。","淘金热的北方环境。"],
 "editions":["《野性的呼唤》中译本（人民文学等——通说待核）。","英文原版（公有领域状态待核）。"],
 "order":"伦敦首选；与《白牙》《马丁·伊登》对读。"},
"pending":["巴克血统核对（B407已载混血）。","1903年出版（Macmillan说）待核。","'野性'回归结尾细节待核。"],
"sources":["B407"],"year_source":"B407","author_source":"B407","related_works":["maodeyaolan","dulidemen","nongmin"],
"svg":G("《野性的呼唤》野性回归图",[{"title":"巴克","text":"雪橇犬的旅程（B407）","color":"main"},{"title":"野性","text":"'呼唤'的归宿（书名）","color":"gold"},{"title":"克朗代克","text":"淘金的北方（B407）","color":"antagonist"},{"title":"爱","text":"最后的文明（通说）","color":"family"}])},
{"id":"madingyideng","title":"马丁·伊登","original_title":"Martin Eden","region":"美国","era":"近代","era_detail":"20世纪初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"jackson","author_name":"杰克·伦敦",
"year_display":"1909年（Britannica B407：Martin Eden (1909)——autobiographical novel——'best conveyed in his autobiographical novel Martin Eden'）","year_sort":1909,
"background":["Britannica（B407）：Martin Eden——autobiographical novel——其乐观与活力的'best conveyed'（自传小说）。","Britannica（B407）：伦敦——1894年'became a militant socialist'——'maintained his socialist beliefs almost to the end of his life'。","题材（通说待核）：水手马丁的成名与幻灭——'尼采式超人'与社会主义的拉扯。"],
"outline":["（通说待核）马丁的写作苦斗与露丝的'文明'世界。","（通说待核）成名后的'虚空'与海的告别。"],
"characters":[{"name":"马丁·伊登","identity":"水手/作家","note":"（B407 书名人物）"},{"name":"露丝","identity":"上流少女","note":"（通说待核）"}],
"themes":["'自传小说'（B407：autobiographical novel）。",
 "成名与幻灭（通说待核）。",
 "社会主义与个人主义的拉扯（B407 语境）。"],
"influence":[{"text":"Britannica：'best conveyed in his autobiographical novel Martin Eden'（B407）。","source":"B407"},{"text":"Britannica：'the highest-paid writer in the United States at that time'（B407 交叉）。","source":"B407"}],
"reading":{"difficulties":["'超人'与社会主义的双声。","自传对应（伦敦经历——通说待核）。"],
 "editions":["《马丁·伊登》中译本（人民文学等——通说待核）。","英文原版（公有领域状态待核）。"],
 "order":"伦敦自传篇；与《野性的呼唤》对读。"},
"pending":["马丁/露丝人名核对（通说）。","1909年出版细节待核。","'尼采式超人'说法待核（通说）。"],
"sources":["B407"],"year_source":"B407","author_source":"B407","related_works":["yexingdehuhuan","meiguobuqu","daolian"],
"svg":G("《马丁·伊登》成名幻灭图",[{"title":"马丁","text":"水手的写作（B407）","color":"main"},{"title":"成名","text":"迟到的荣耀（通说）","color":"gold"},{"title":"幻灭","text":"海中的告别（通说）","color":"antagonist"},{"title":"自传","text":"伦敦的镜像（B407）","color":"family"}])},
{"id":"niuyuesanbuqu","title":"纽约三部曲","original_title":"The New York Trilogy","region":"美国","era":"现当代","era_detail":"20世纪80年代",
"genre":"实验小说（三部曲）","genre_group":"小说","language":"英语","author_id":"auster","author_name":"保罗·奥斯特",
"year_display":"1987年（Britannica B408：The New York Trilogy (1987)——'experimental detective stories'）","year_sort":1987,
"background":["Britannica（B408）：'gained renown for a series of experimental detective stories published collectively as The New York Trilogy (1987)'。","Britannica（B408）：City of Glass (1985)——犯罪小说家被卷入谜案承担多重身份；Ghosts (1986)——Blue 受雇于 White 调查 Black；The Locked Room (1986)——作家研究失踪作者渐取其身份。","Britannica（B408）：'often concerned with the search for identity and personal meaning'。"],
"outline":["《玻璃城》：作家奎因'成为'侦探（B408：takes on multiple identities）。","《幽灵》：Blue 调查 Black 的自我镜像（B383 式——B408）。","《锁闭的房间》：研究者'成为'失踪者（B408）。"],
"characters":[{"name":"奎因","identity":"玻璃城的作家","note":"（B408：City of Glass——通说待核）"},{"name":"Blue/Black/White","identity":"幽灵的名字","note":"（B408：Ghosts——B408已载）"}],
"themes":["'身份与个人意义的追寻'（B408：search for identity and personal meaning）。",
 "'实验侦探小说'（B408）。",
 "'多重身份'的承担（B408：City of Glass）。"],
"influence":[{"text":"Britannica：'gained renown for...'（B408）。","source":"B408"},{"text":"Britannica：'The Invention of Solitude'（B408 交叉）。","source":"B408"}],
"reading":{"difficulties":["侦探类型的解构。","'身份'的哲学追问。"],
 "editions":["《纽约三部曲》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"奥斯特首选；后接《孤独及其所创造的》。"},
"pending":["奎因/Blue/Black人名核对（B408已载 Ghosts 三名）。","三部合集1987年（Sun & Moon说）待核。","'玻璃城'细节待核。"],
"sources":["B408"],"year_source":"B408","author_source":"B408","related_works":["wuhhaotuchang","moluoyi","meiguobuqu"],
"svg":G("《纽约三部曲》身份追寻图",[{"title":"玻璃城","text":"多重身份（B408）","color":"main"},{"title":"幽灵","text":"Blue 与 Black（B408）","color":"gold"},{"title":"锁闭的房间","text":"成为失踪者（B408）","color":"family"},{"title":"追寻","text":"'身份与意义'（B408）","color":"antagonist"}])},
{"id":"dizudelang","title":"铁蹄","original_title":"The Iron Heel","region":"美国","era":"近代","era_detail":"20世纪初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"jackson","author_name":"杰克·伦敦",
"year_display":"1908年（Britannica B407：The Iron Heel (1908)——'a fantasy of the future that is a terrifying anticipation of fascism'）","year_sort":1908,
"background":["Britannica（B407）：The Iron Heel——'a fantasy of the future that is a terrifying anticipation of fascism'（对未来幻想——法西斯主义的可怖预言）。","Britannica（B407）：伦敦——1894年'became a militant socialist'——'maintained his socialist beliefs almost to the end of his life'。","题材（通说待核）：寡头'铁蹄'与工人起义——手稿残卷的框形叙事。"],
"outline":["（通说待核）'铁蹄'寡头政权的镇压与芝加哥暴动。","（通说待核）'手稿'在'七百年后'被释读的框架。"],
"characters":[{"name":"欧内斯特·埃弗哈德","identity":"社会主义者","note":"（通说待核）"},{"name":"艾薇丝","identity":"妻子/记录者","note":"（通说待核）"}],
"themes":["'法西斯主义的可怖预言'（B407）。",
 "寡头政治的幻象（书名语境——通说待核）。",
 "'手稿残卷'的框架（通说待核）。"],
"influence":[{"text":"Britannica：'a terrifying anticipation of fascism'（B407）。","source":"B407"},{"text":"Britannica：'militant socialist'（B407 交叉）。","source":"B407"}],
"reading":{"difficulties":["未来史框架。","1900年代美国劳工运动。"],
 "editions":["《铁蹄》中译本（人民文学等——通说待核）。","英文原版（公有领域状态待核）。"],
 "order":"伦敦政治篇；与《马丁·伊登》对读。"},
"pending":["埃弗哈德/艾薇丝人名核对（通说）。","1908年出版细节待核。","'手稿'框架细节待核。"],
"sources":["B407"],"year_source":"B407","author_source":"B407","related_works":["madingyideng","yexingdehuhuan","meiguobuqu"],
"svg":G("《铁蹄》预言结构图",[{"title":"铁蹄","text":"寡头的镇压（书名）","color":"antagonist"},{"title":"预言","text":"'法西斯主义的可怖预言'（B407）","color":"gold"},{"title":"手稿","text":"七百年后的释读（通说）","color":"family"},{"title":"起义","text":"芝加哥的暴动（通说）","color":"main"}])},
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

for wid, aid in [('yexingdehuhuan','jackson'), ('madingyideng','jackson'), ('niuyuesanbuqu','auster'), ('dizudelang','jackson')]:
    if wid in created:
        link(aid, wid)
print('BATCH77 DONE')
