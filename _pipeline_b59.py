# -*- coding: utf-8 -*-
"""批59：Britannica 新核 3 作家 3 部（库切 B375/安德里奇 B376/特朗斯特罗默 B377）"""
import json, pathlib

newsrc = [
{"id":"B375","title":"J.M. Coetzee — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/J-M-Coetzee","type":"百科全书","verified":True,"covers":["coetzee","mikesaierke"],"note":"2026-11-21 核对：1940-02-09南非开普敦生（在世）；2003诺贝尔文学奖；Life & Times of Michael K (1983)——布克奖——'concerns the dilemma of a simple man beset by conditions he can neither comprehend nor control during a civil war in a future South Africa'；Disgrace (1999)——布克奖——'making Coetzee the first author to win the Booker Prize twice'——后种族隔离南非背景——'caused an outcry in South Africa'——此后移居澳大利亚（2006入籍）；Waiting for the Barbarians (1980)——'set in some undefined borderland, is an examination of the ramifications of colonization'；Dusklands (1974)首作；Foe (1986)——重写笛福《鲁滨逊》；自传三部曲 Boyhood (1997)/Youth (2002)/Summertime (2009)；Elizabeth Costello (2003)"},
{"id":"B376","title":"Ivo Andric — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ivo-Andric","type":"百科全书","verified":True,"covers":["andric","derinahe"],"note":"2026-11-21 核对：1892-10-10波斯尼亚Travnik附近Dolac生—1975-03-13贝尔格莱德卒（82岁）；1961诺贝尔文学奖；Na Drini ćuprija（德里纳河上的桥, 1945）——'constructs four centuries of Bosnian history'（建构四个世纪的波斯尼亚史）——维舍格勒奥斯曼桥；诺奖委员会称其以'epic force'处理材料；Ex Ponto (1918)——'a contemplative, lyrical prose work written during his internment by Austro-Hungarian authorities'（一战奥匈拘禁期写）；Travnička hronika（特拉夫尼克纪事, 1945）——拿破仑时代法/奥/奥斯曼三领事视角；'His works are written soberly, in language of great beauty and purity.'"},
{"id":"B377","title":"Tomas Transtromer — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Tomas-Transtromer","type":"百科全书","verified":True,"covers":["transtromer","shiqishoushi"],"note":"2026-11-21 核对：1931-04-15斯德哥尔摩生—2015-03-26斯德哥尔摩卒（83岁）；2011诺贝尔文学奖；1990 Neustadt奖；'noted for his spare but resonant language, particularly his unusual metaphors—more transformative than substitutive'；其隐喻'have been associated with a literary surrealism. His verse was at once revelatory and mysterious.'；17 dikter（十七首诗, 1954）——'showed the influence of Modernism in its spare language and startling imagery, and it met with critical acclaim'；后期'a more-personal style, with plainer diction'；评论家——'Tranströmer's poems are acoustically perfect chambers...'；'poetic observations of nature combine richness of meaning with the utmost simplicity of style'；Östersjöar（波罗的海, 1974）——波罗的海海岸；'the most widely translated Scandinavian poet in the English-speaking world'（20世纪后期）；1990中风'robbed him almost entirely of the ability to speak'——仍持续出版；与Robert Bly的友谊传播其影响；心理学家/社工"},
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
{"id":"coetzee","name":"J.M.库切","foreign_name":"J.M. Coetzee（约翰·马克斯韦尔·库切，1940-02-09—）","country":"南非","birth":1940,"death":None,"birth_year":1940,"death_year":None,"era":"现当代",
"summary":"库切，开普敦生，南非小说家——2003年诺贝尔文学奖（B375）。Life & Times of Michael K（迈克尔·K的生活和时代, 1983）——布克奖——'concerns the dilemma of a simple man beset by conditions he can neither comprehend nor control during a civil war in a future South Africa'（B375）。Disgrace（耻, 1999）——再获布克奖——'making Coetzee the first author to win the Booker Prize twice'（首位两获布克——B375）——后种族隔离背景——'caused an outcry in South Africa'——此后移居澳大利亚（B375）。Waiting for the Barbarians（等待野蛮人, 1980）——'an examination of the ramifications of colonization'（B375）。",
"timeline":[
 {"year":1940,"text":"2月9日生于开普敦（B375）。","src":"B375"},
 {"year":1980,"text":"Waiting for the Barbarians——殖民后果的审视（B375）。","src":"B375"},
 {"year":1983,"text":"《迈克尔·K的生活和时代》——布克奖（B375）。","src":"B375"},
 {"year":1999,"text":"《耻》——两获布克的第一人（B375）。","src":"B375"},
 {"year":2003,"text":"获诺贝尔文学奖（B375）。","src":"B375"}],
"major_works":[
 {"work_id":"mikesaierke","note":"1983布克奖（B375）"},
 {"title":"耻","note":"（B375：Disgrace (1999)——布克奖）"},
 {"title":"等待野蛮人","note":"（B375：Waiting for the Barbarians (1980)）"}],
"style":["寓言化的政治书写（B375：undefined borderland）。",
 "'简单人'的困境（B375：a simple man beset...）。",
 "殖民的后果学（B375：ramifications of colonization）。"],
"status":"Britannica 定位库切为2003诺奖得主、首位两获布克奖的作家（B375）。",
"sources":["B375"],"dates_source":"B375",
"pending":["《迈克尔·K的生活和时代》通行译名待核。","'移居澳大利亚'细节（2006入籍——B375）待核。","Disgrace 通行译名（《耻》）待核。"]},
{"id":"andric","name":"伊沃·安德里奇","foreign_name":"Ivo Andrić（伊沃·安德里奇，1892-10-10—1975-03-13）","country":"南斯拉夫","birth":1892,"death":1975,"birth_year":1892,"death_year":1975,"era":"近代",
"summary":"安德里奇，波斯尼亚特拉夫尼克附近Dolac生，南斯拉夫作家——1961年诺贝尔文学奖（B376）。Na Drini ćuprija（德里纳河上的桥, 1945）——'constructs four centuries of Bosnian history'（建构四个世纪的波斯尼亚史——B376）——维舍格勒的奥斯曼大桥；诺奖委员会称其以'epic force'处理材料（B376）。'His works are written soberly, in language of great beauty and purity.'（B376）。Ex Ponto (1918)——一战奥匈拘禁期的沉思散文（B376）。",
"timeline":[
 {"year":1892,"text":"10月10日生于波斯尼亚Dolac（B376）。","src":"B376"},
 {"year":1918,"text":"Ex Ponto——拘禁期的沉思散文（B376）。","src":"B376"},
 {"year":1945,"text":"《德里纳河上的桥》《特拉夫尼克纪事》同年出版（B376）。","src":"B376"},
 {"year":1961,"text":"获诺贝尔文学奖（B376）。","src":"B376"},
 {"year":1975,"text":"3月13日卒于贝尔格莱德（B376）。","src":"B376"}],
"major_works":[
 {"work_id":"derinahe","note":"1945（B376）"},
 {"title":"特拉夫尼克纪事","note":"（B376：Travnička hronika (1945)——中译名待核）"},
 {"title":"埃克斯蓬托","note":"（B376：Ex Ponto (1918)——中译名待核）"}],
"style":["'清醒而优美纯净的语言'（B376：soberly...great beauty and purity）。",
 "'史诗力量'（B376：epic force——诺奖委员会）。",
 "桥作为历史的脊柱（书名语境——通说待核）。"],
"status":"Britannica 定位安德里奇为1961诺奖得主、波斯尼亚史的史诗建构者（B376）。",
"sources":["B376"],"dates_source":"B376",
"pending":["德里纳河桥年代（1571建桥说）待核。","'四个世纪'起讫核对（通说）。","外交官生涯细节待核（B376未载）。"]},
{"id":"transtromer","name":"托马斯·特朗斯特罗默","foreign_name":"Tomas Tranströmer（托马斯·特朗斯特罗默，1931-04-15—2015-03-26）","country":"瑞典","birth":1931,"death":2015,"birth_year":1931,"death_year":2015,"era":"现当代",
"summary":"特朗斯特罗默，斯德哥尔摩生，瑞典诗人——2011年诺贝尔文学奖（B377）；1990 Neustadt奖（B377）。'noted for his spare but resonant language, particularly his unusual metaphors—more transformative than substitutive'（简洁而共鸣的语言、'转变性'隐喻——B377）；其隐喻'have been associated with a literary surrealism'（B377）。17 dikter（十七首诗, 1954）——'showed the influence of Modernism in its spare language and startling imagery'（B377）。Östersjöar（波罗的海, 1974）（B377）。'the most widely translated Scandinavian poet in the English-speaking world'（B377）。1990年中风'robbed him almost entirely of the ability to speak'——仍持续出版（B377）。",
"timeline":[
 {"year":1931,"text":"4月15日生于斯德哥尔摩（B377）。","src":"B377"},
 {"year":1954,"text":"17 dikter（十七首诗）——现代主义、好评（B377）。","src":"B377"},
 {"year":1974,"text":"Östersjöar（波罗的海）（B377）。","src":"B377"},
 {"year":1990,"text":"中风——几乎完全失去说话能力；仍持续出版（B377）。","src":"B377"},
 {"year":2011,"text":"获诺贝尔文学奖（B377）。","src":"B377"},
 {"year":2015,"text":"3月26日卒于斯德哥尔摩（B377）。","src":"B377"}],
"major_works":[
 {"work_id":"shiqishoushi","note":"1954（B377）"},
 {"title":"波罗的海","note":"（B377：Östersjöar (1974; Baltics)）"},
 {"title":"悲伤的贡多拉","note":"（B377：Sorgegondolen (1996)——受李斯特启发）"}],
"style":["'简洁而共鸣'的语言（B377：spare but resonant）。",
 "'转变性而非替代性'的隐喻（B377）。",
 "'声学上完美的房间'（B377 评论家引语）。"],
"status":"Britannica 定位特朗斯特罗默为2011诺奖得主、英语世界译介最广的斯堪的纳维亚诗人（B377）。",
"sources":["B377"],"dates_source":"B377",
"pending":["《十七首诗》通行译名待核。","心理学家职业细节（B377已载）待核。","与Robert Bly的交往细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"mikesaierke","title":"迈克尔·K的生活和时代","original_title":"Life & Times of Michael K","region":"南非","era":"现当代","era_detail":"20世纪80年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"coetzee","author_name":"J.M.库切",
"year_display":"1983年（Britannica B375：Life & Times of Michael K (1983)——布克奖）","year_sort":1983,
"background":["Britannica（B375）：'concerns the dilemma of a simple man beset by conditions he can neither comprehend nor control during a civil war in a future South Africa'——未来南非内战中一个'简单人'的困境。","Britannica（B375）：布克奖（1983）。","Britannica（B375）：库切——2003诺奖；'an examination of the ramifications of colonization'（等待野蛮人——交叉）。"],
"outline":["（通说待核——B375未载剧情）迈克尔·K携病母返乡：内战中的'园丁'。","（通说待核）营地与逃逸：'不吃他们的饭'的抵抗。"],
"characters":[{"name":"迈克尔·K","identity":"园丁/兔唇","note":"（B375 书名人物）"},{"name":"医疗官","identity":"追问他的人","note":"（通说待核）"}],
"themes":["'简单人'的困境（B375）。",
 "内战寓言（B375：a civil war in a future South Africa）。",
 "土地与种子（通说待核）。"],
"influence":[{"text":"Britannica：1983布克奖（B375）。","source":"B375"},{"text":"Britannica：2003诺奖（B375 交叉）。","source":"B375"}],
"reading":{"difficulties":["寓言化叙事。","南非内战假设（通说待核）。"],
 "editions":["《迈克尔·K的生活和时代》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"库切布克奖之作；与《耻》对读。"},
"pending":["迈克尔·K全名核对（通说：Michael Kosis）。","1983年出版（Ravan说）待核。","'营地'细节待核。"],
"sources":["B375"],"year_source":"B375","author_source":"B375","related_works":["yu","moluoyi","nongmin"],
"svg":G("《迈克尔·K》寓言结构图",[{"title":"迈克尔·K","text":"'简单人'的困境（B375）","color":"main"},{"title":"内战","text":"未来南非（B375）","color":"antagonist"},{"title":"种子","text":"园丁的执念（通说）","color":"gold"},{"title":"营地","text":"收容的逻辑（通说）","color":"family"}])},
{"id":"derinahe","title":"德里纳河上的桥","original_title":"Na Drini ćuprija","region":"南斯拉夫","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"塞尔维亚-克罗地亚语","author_id":"andric","author_name":"伊沃·安德里奇",
"year_display":"1945年（Britannica B376：Na Drini ćuprija (1945)——'constructs four centuries of Bosnian history'）","year_sort":1945,
"background":["Britannica（B376）：'constructs four centuries of Bosnian history'——以维舍格勒奥斯曼大桥串起的事件与个人故事，并置历史叙事与民间传说。","Britannica（B376）：诺奖委员会——'epic force'（史诗力量）。","Britannica（B376）：'His works are written soberly, in language of great beauty and purity.'"],
"outline":["（通说待核——B376未载细节）大桥的四百年：从奥斯曼建造到一战炸毁。","（通说待核）'桥头堡'上的弑兄与婚礼。"],
"characters":[{"name":"阿勃迪帕夏","identity":"建桥者","note":"（通说待核）"},{"name":"桥","identity":"历史的脊柱","note":"（书名人物——通说待核）"}],
"themes":["'四个世纪的波斯尼亚史'（B376）。",
 "桥与'血税'的传说（通说待核）。",
 "'史诗力量'（B376：诺奖委员会）。"],
"influence":[{"text":"Britannica：1961诺奖——'epic force'（B376）。","source":"B376"},{"text":"Britannica：'language of great beauty and purity'（B376）。","source":"B376"}],
"reading":{"difficulties":["奥斯曼-奥匈史。","多世纪编年的群像。"],
 "editions":["《德里纳河上的桥》中译本（人民文学等——通说待核）。","塞尔维亚-克罗地亚语原版。"],
 "order":"安德里奇首选；与《特拉夫尼克纪事》对读。"},
"pending":["建桥年代与帕夏名核对（通说）。","'四个世纪'起讫核对。","1945年出版细节待核。"],
"sources":["B376"],"year_source":"B376","author_source":"B376","related_works":["xianrenji","dulidemen","fuyuzi"],
"svg":G("《德里纳河上的桥》四百年结构图",[{"title":"桥","text":"历史的脊柱（书名）","color":"gold"},{"title":"四百年","text":"波斯尼亚史（B376）","color":"main"},{"title":"奥斯曼","text":"建桥的帝国（通说）","color":"antagonist"},{"title":"传说","text":"民间叙事（B376）","color":"family"}])},
{"id":"shiqishoushi","title":"十七首诗","original_title":"17 dikter","region":"瑞典","era":"近代","era_detail":"20世纪50年代",
"genre":"诗集","genre_group":"诗歌","language":"瑞典语","author_id":"transtromer","author_name":"托马斯·特朗斯特罗默",
"year_display":"1954年（Britannica B377：17 dikter (1954; Seventeen Poems)——'showed the influence of Modernism in its spare language and startling imagery'）","year_sort":1954,
"background":["Britannica（B377）：17 dikter——'showed the influence of Modernism in its spare language and startling imagery, and it met with critical acclaim'。","Britannica（B377）：'noted for his spare but resonant language...unusual metaphors—more transformative than substitutive'。","Britannica（B377）：'the most widely translated Scandinavian poet in the English-speaking world'（20世纪后期）。"],
"outline":["（通说待核——B377未载篇目）现代主义式的'简洁语言与惊人意象'。","（通说待核）'诗是内在的房间'（评论家语——B377：acoustically perfect chambers）。"],
"characters":[{"name":"抒情'我'","identity":"心理学家诗人","note":"（B377 语境）"}],
"themes":["'转变性'的隐喻（B377：more transformative than substitutive）。",
 "'文学超现实主义'的关联（B377）。",
 "自然的观察：'意义的丰富与风格的至简'（B377）。"],
"influence":[{"text":"Britannica：2011诺奖（B377）。","source":"B377"},{"text":"Britannica：'critically acclaimed'（B377）。","source":"B377"}],
"reading":{"difficulties":["隐喻的'转变性'。","瑞典语原文（读译本）。"],
 "editions":["《十七首诗》中译名（《诗十七首》）待核。","瑞典文原版（公有领域状态待核）。"],
 "order":"特朗斯特罗默首选；后接《波罗的海》。"},
"pending":["篇目（《序曲》等）核对（B377未载）。","1954年出版细节待核。","'acoustically perfect chambers'评论出处核对。"],
"sources":["B377"],"year_source":"B377","author_source":"B377","related_works":["wuguigu","shenhualishi","ezhihua"],
"svg":G("《十七首诗》隐喻结构图",[{"title":"隐喻","text":"'转变性'（B377）","color":"gold"},{"title":"简洁","text":"共鸣的语言（B377）","color":"main"},{"title":"超现实","text":"文学的关联（B377）","color":"family"},{"title":"房间","text":"'声学上完美'（B377）","color":"antagonist"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B37x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('mikesaierke','coetzee'), ('derinahe','andric'), ('shiqishoushi','transtromer')]:
    if wid in created:
        link(aid, wid)
print('BATCH59 DONE')
