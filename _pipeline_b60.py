# -*- coding: utf-8 -*-
"""批60：Britannica 新核 3 作家 3 部（鲁西迪 B378/凯尔泰斯 B379/埃尔诺 B380）"""
import json, pathlib

newsrc = [
{"id":"B378","title":"Salman Rushdie — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Salman-Rushdie","type":"百科全书","verified":True,"covers":["rushdie","wuzhizi"],"note":"2026-11-21 核对：1947-06-19孟买生；Midnight's Children（午夜之子, 1981）——'a fable about modern India'——布克奖(1981)+Booker of Bookers(1993)+Best of the Booker(2008)；The Satanic Verses (1988)——1988-10-05印度禁运——1989年霍梅尼'issued a fatwa (legal opinion) against Rushdie'并悬赏——隐居约十年——1998年伊朗'would no longer seek to enforce its fatwa'——日译者1991被杀、意译者被刺、挪威出版商1993被枪击；2022年8月在纽约州Chautauqua遇袭失去一眼——袭击者 Hadi Matar 被判谋杀未遂25年（2026年7月又判恐怖主义相关罪名）；2007封爵；2016美国公民；作品序列 Grimus (1975)、Shame (1983)、Haroun (1990)、The Moor's Last Sigh (1995)、Joseph Anton (2012)、Quichotte (2019)、Victory City (2023)、Knife (2024)、The Eleventh Hour (2025)"},
{"id":"B379","title":"Imre Kertesz — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Imre-Kertesz","type":"百科全书","verified":True,"covers":["kertesz","wumingyundesheng"],"note":"2026-11-21 核对：1929-11-09布达佩斯生—2016-03-31布达佩斯卒（86岁）；2002诺贝尔文学奖；14岁被逐奥斯维辛后布痕瓦尔德——'from which he was liberated in May 1945'；Sorstalanság（无命运的一生/无命运者, 1975年出版，60年代中期完成）——叙述者'confronts the inexplicable horror of human degradation not with outrage or resistance but with seemingly incomprehensible complacency and detachment'——1990年德译本后更受关注——译成10余种语言——2005年自改编电影；Kaddish for a Child Not Born (1990)；Fiasco (1988)；Liquidation (2003)；Dossier K. (2006回忆录)；记者1951年被共产党政权解雇——靠翻译尼采/弗洛伊德/霍夫曼斯塔尔/施尼茨勒/维特根斯坦为生"},
{"id":"B380","title":"Annie Ernaux — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Annie-Ernaux","type":"百科全书","verified":True,"covers":["ernaux","suiyue"],"note":"2026-11-21 核对：1940-09-01法国Lillebonne生（原名 Annie Duchesne，工人家庭）；2022诺贝尔文学奖——瑞典学院赞其'courage and clinical acuity'揭示'the roots, estrangements and collective restraints of personal memory'；'lightly fictionalized memoirs, which are written in spare, detached prose'（轻度虚构的自传、简洁疏离的散文）——'revealing the artifice of her own genre'；Les Armoires vides (Cleaned Out, 1974)；La Femme gelée (1981)；La Place (A Man's Place, 1983)——父亲——勒诺多奖；Une Femme (1987)——母亲阿尔茨海默；Passion simple (1991)；Les Années（岁月, 2008）——'her masterpiece'——'a personal and collective history of postwar France'——获杜拉斯奖与莫里亚克奖——英译2019入围布克——2025年伦敦西区舞台改编；Mémoire de fille (2016)；2000年从教职退休；Happening (2021)威尼斯金狮"},
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
{"id":"rushdie","name":"萨尔曼·鲁西迪","foreign_name":"Salman Rushdie（萨尔曼·鲁西迪，1947-06-19—）","country":"英国","birth":1947,"death":None,"birth_year":1947,"death_year":None,"era":"现当代",
"summary":"鲁西迪，孟买生（英籍印度裔），小说家——Midnight's Children（午夜之子, 1981）——'a fable about modern India'（关于现代印度的寓言——B378）——布克奖(1981)、Booker of Bookers(1993)、Best of the Booker(2008)（B378）。The Satanic Verses（撒旦诗篇, 1988）——1989年霍梅尼'issued a fatwa'并悬赏——隐居约十年——1998年伊朗不再执行（B378）——日译者1991被杀、意译者被刺、挪威出版商被枪击（B378）。2022年8月在纽约州遇袭失去一眼（B378）。2007年封爵（B378）。",
"timeline":[
 {"year":1947,"text":"6月19日生于孟买（B378）。","src":"B378"},
 {"year":1981,"text":"《午夜之子》——布克奖（B378）。","src":"B378"},
 {"year":1989,"text":"霍梅尼对《撒旦诗篇》发布法特瓦——隐居约十年（B378）。","src":"B378"},
 {"year":2007,"text":"获封爵士（B378）。","src":"B378"},
 {"year":2022,"text":"8月在纽约州遇袭失去一眼；袭击者被判罪（B378）。","src":"B378"}],
"major_works":[
 {"work_id":"wuzhizi","note":"1981（B378）"},
 {"title":"撒旦诗篇","note":"（B378：The Satanic Verses (1988)）"},
 {"title":"羞耻","note":"（B378：Shame (1983)）"}],
"style":["'关于现代印度的寓言'（B378）。",
 "魔幻现实主义与英语的重铸（B378 语境——通说待核）。",
 "'历史'与'想象'的争辩（B378 语境）。"],
"status":"Britannica 定位鲁西迪为布克奖三度加冕的作家、法特瓦事件的当事人（B378）。",
"sources":["B378"],"dates_source":"B378",
"pending":["《午夜之子》通行译名待核。","'Booker of Bookers'评奖细节（B378已载）待核。","2022年袭击案的司法后续（2026年7月恐怖主义罪名——B378口径）核对。"]},
{"id":"kertesz","name":"凯尔泰斯·伊姆雷","foreign_name":"Imre Kertész（凯尔泰斯·伊姆雷，1929-11-09—2016-03-31）","country":"匈牙利","birth":1929,"death":2016,"birth_year":1929,"death_year":2016,"era":"现当代",
"summary":"凯尔泰斯，布达佩斯生，匈牙利小说家——2002年诺贝尔文学奖（B379）。14岁被逐奥斯维辛、后布痕瓦尔德——1945年5月获释（B379）。Sorstalanság（无命运的一生, 1975年出版）——叙述者'confronts the inexplicable horror of human degradation not with outrage or resistance but with seemingly incomprehensible complacency and detachment'（以'麻木与超然'面对人的贬抑——B379）——1990年德译本后广受关注、译成10余种语言、2005年自改编电影（B379）。靠翻译尼采、弗洛伊德等为生（B379）。",
"timeline":[
 {"year":1929,"text":"11月9日生于布达佩斯（B379）。","src":"B379"},
 {"year":1944,"text":"14岁被逐奥斯维辛、布痕瓦尔德（B379）。","src":"B379"},
 {"year":1975,"text":"《无命运的一生》出版（B379）。","src":"B379"},
 {"year":2002,"text":"获诺贝尔文学奖（B379）。","src":"B379"},
 {"year":2016,"text":"3月31日卒于布达佩斯（B379）。","src":"B379"}],
"major_works":[
 {"work_id":"wumingyundesheng","note":"1975（B379）"},
 {"title":"给未出生孩子的挽歌","note":"（B379：Kaddish for a Child Not Born (1990)——中译名待核）"},
 {"title":"惨败","note":"（B379：Fiasco (1988)——中译名待核）"}],
"style":["'麻木与超然'的集中营叙事（B379：complacency and detachment）。",
 "'无命运'：对命运的拒绝命名（书名语境——通说待核）。",
 "翻译家式的精确（B379：Nietzsche/Freud 等）。"],
"status":"Britannica 定位凯尔泰斯为2002诺奖得主、大屠杀文学的'疏离'书写者（B379）。",
"sources":["B379"],"dates_source":"B379",
"pending":["《无命运的一生》通行译名（《无命运者》/《无命运的人生》）待核。","'1960年代中期完成'（B379）细节待核。","2005年电影改编（导演说法）待核。"]},
{"id":"ernaux","name":"安妮·埃尔诺","foreign_name":"Annie Ernaux（安妮·埃尔诺，原名 Annie Duchesne，1940-09-01—）","country":"法国","birth":1940,"death":None,"birth_year":1940,"death_year":None,"era":"现当代",
"summary":"埃尔诺，法国Lillebonne生（工人家庭），作家——2022年诺贝尔文学奖——瑞典学院赞其'courage and clinical acuity'揭示'the roots, estrangements and collective restraints of personal memory'（个人记忆的根源、疏离与集体规训——B380）。'lightly fictionalized memoirs...written in spare, detached prose'（轻度虚构的自传、简洁疏离的散文——B380）——'revealing the artifice of her own genre'（揭示自身文类的造作——B380）。Les Années（岁月, 2008）——'her masterpiece'——'a personal and collective history of postwar France'（战后法国的个人与集体史——B380）——获杜拉斯奖与莫里亚克奖（B380）。La Place (1983)——勒诺多奖（B380）。",
"timeline":[
 {"year":1940,"text":"9月1日生于Lillebonne（B380）。","src":"B380"},
 {"year":1974,"text":"Les Armoires vides——首作（B380）。","src":"B380"},
 {"year":1983,"text":"La Place——勒诺多奖（B380）。","src":"B380"},
 {"year":2008,"text":"《岁月》——'her masterpiece'（B380）。","src":"B380"},
 {"year":2022,"text":"获诺贝尔文学奖（B380）。","src":"B380"}],
"major_works":[
 {"work_id":"suiyue","note":"2008（B380）"},
 {"title":"一个男人的位置","note":"（B380：La Place (1983)——中译名待核）"},
 {"title":"一个女人的故事","note":"（B380：Une Femme (1987)）"}],
"style":["'简洁疏离的散文'（B380：spare, detached prose）。",
 "'轻度虚构的自传'与'文类的造作'（B380）。",
 "'个人记忆的集体规训'（B380：collective restraints）。"],
"status":"Britannica 定位埃尔诺为2022诺奖得主、《岁月》为其杰作（B380）。",
"sources":["B380"],"dates_source":"B380",
"pending":["《岁月》通行译名（《悠悠岁月》）待核。","2025年伦敦西区舞台改编（Eline Arbo——B380）待核。","'自'fiction'术语归属（与杜布拉夫卡之辩）待核——B380未载。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"wuzhizi","title":"午夜之子","original_title":"Midnight's Children","region":"印度","era":"现当代","era_detail":"20世纪80年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"rushdie","author_name":"萨尔曼·鲁西迪",
"year_display":"1981年（Britannica B378：Midnight's Children (1981)——布克奖+Booker of Bookers(1993)+Best of the Booker(2008)）","year_sort":1981,
"background":["Britannica（B378）：'a fable about modern India'——关于现代印度的寓言——'a critical and popular hit'。","Britannica（B378）：布克奖(1981)、Booker of Bookers(1993)、Best of the Booker(2008)。","题材（通说待核）：1947年8月15日午夜出生的千名'午夜之子'——萨里姆的电报鼻与独立印度。"],
"outline":["（通说待核）萨里姆·西奈与'午夜之子大会'（MCC——通说待核）。","（通说待核）'腌菜罐'的叙事：历史与个人互为腌制。"],
"characters":[{"name":"萨里姆·西奈","identity":"午夜之子","note":"（通说待核，B378未载）"},{"name":"湿婆（Shiva）","identity":"另一个午夜之子","note":"（通说待核）"}],
"themes":["'关于现代印度的寓言'（B378）。",
 "独立与个人的绑定（通说待核）。",
 "魔幻现实主义的英语变体（B378 语境——通说待核）。"],
"influence":[{"text":"Britannica：布克奖三度加冕（B378）。","source":"B378"},{"text":"Britannica：'a critical and popular hit'（B378）。","source":"B378"}],
"reading":{"difficulties":["印度史年表（1919-1977——通说待核）。","'腌菜'叙事框架。"],
 "editions":["《午夜之子》中译本（北京燕山/译林等——通说待核）。","英文原版。"],
 "order":"鲁西迪首选；与《百年孤独》对读。"},
"pending":["萨里姆/湿婆人名核对（通说）。","1981年出版（Jonathan Cape说）待核。","'1001个午夜之子'细节待核。"],
"sources":["B378"],"year_source":"B378","author_source":"B378","related_works":["bainian" if "bainian" in existing else "leiyu","zhegeshijiedewanguo","gududemigong"],
"svg":G("《午夜之子》寓言结构图",[{"title":"午夜","text":"独立的时刻（B378）","color":"gold"},{"title":"千名之子","text":"国家的孩子（通说）","color":"main"},{"title":"腌菜罐","text":"历史的防腐（通说）","color":"family"},{"title":"寓言","text":"'现代印度'（B378）","color":"antagonist"}])},
{"id":"wumingyundesheng","title":"无命运的一生","original_title":"Sorstalanság","region":"匈牙利","era":"近代","era_detail":"20世纪70年代",
"genre":"长篇小说","genre_group":"小说","language":"匈牙利语","author_id":"kertesz","author_name":"凯尔泰斯·伊姆雷",
"year_display":"1975年（Britannica B379：Sorstalanság (1975)——60年代中期完成）","year_sort":1975,
"background":["Britannica（B379）：叙述者'confronts the inexplicable horror of human degradation not with outrage or resistance but with seemingly incomprehensible complacency and detachment'。","Britannica（B379）：1990年德译本后更受关注——译成10余种语言——2005年自改编电影。","Britannica（B379）：凯尔泰斯——14岁被逐奥斯维辛、布痕瓦尔德——1945年5月获释。"],
"outline":["（通说待核）科维什·久尔吉的奥斯维辛-布痕瓦尔德：'步骤'式的适应。","（通说待核）'无命运'：没有选择的选择。"],
"characters":[{"name":"科维什·久尔吉","identity":"15岁被逐者","note":"（通说待核，B379未载）"}],
"themes":["'麻木与超然'（B379：complacency and detachment）。",
 "'无命运'：拒绝悲剧的姿态（书名语境——通说待核）。",
 "人的贬抑的'不可理解'（B379：inexplicable horror）。"],
"influence":[{"text":"Britannica：2002诺奖（B379）。","source":"B379"},{"text":"Britannica：'translated into more than 10 languages'（B379）。","source":"B379"}],
"reading":{"difficulties":["'疏离'叙述的伦理。","奥斯维辛-布痕瓦尔德史。"],
 "editions":["《无命运的一生》中译本（人民文学等——通说待核）。","匈牙利文原版。"],
 "order":"凯尔泰斯首选；后接《给未出生孩子的挽歌》。"},
"pending":["科维什·久尔吉人名核对（通说）。","1975年出版（Szépirodalmi说）待核。","'下一步'（Légszomj）等细节待核。"],
"sources":["B379"],"year_source":"B379","author_source":"B379","related_works":["chanye" if "chanye" in existing else "leiyu","moluoyi","wumingyundesheng" if False else "tuyuzhizideneizi"],
"svg":G("《无命运的一生》疏离结构图",[{"title":"无命运","text":"拒绝悲剧的命名（书名）","color":"gold"},{"title":"久尔吉","text":"'麻木'的见证（B379）","color":"main"},{"title":"奥斯维辛","text":"贬抑的不可解（B379）","color":"antagonist"},{"title":"步骤","text":"适应的逻辑（通说）","color":"family"}])},
{"id":"suiyue","title":"岁月","original_title":"Les Années","region":"法国","era":"现当代","era_detail":"21世纪初",
"genre":"自传性叙事","genre_group":"散文","language":"法语","author_id":"ernaux","author_name":"安妮·埃尔诺",
"year_display":"2008年（Britannica B380：Les Années (2008)——'her masterpiece'——'a personal and collective history of postwar France'）","year_sort":2008,
"background":["Britannica（B380）：'her masterpiece'——'a personal and collective history of postwar France'（战后法国的个人与集体史）——获杜拉斯奖与莫里亚克奖——英译2019入围布克。","Britannica（B380）：埃尔诺——'lightly fictionalized memoirs...written in spare, detached prose'——'revealing the artifice of her own genre'。","Britannica（B380）：2022诺奖——'courage and clinical acuity'。"],
"outline":["（通说待核）'无人称'的岁月档案：照片、歌曲、广告与事件。","（通说待核）'拯救关于某物曾经存在的记忆'（不采为引文）。"],
"characters":[{"name":"'她'（无人称）","identity":"记忆的主体","note":"（通说待核）"}],
"themes":["'个人与集体的战后法国史'（B380）。",
 "'无人称自传'（通说待核）。",
 "'文类的造作'的自我揭示（B380：artifice of her own genre）。"],
"influence":[{"text":"Britannica：2022诺奖——'courage and clinical acuity'（B380）。","source":"B380"},{"text":"Britannica：'her masterpiece'（B380）。","source":"B380"}],
"reading":{"difficulties":["'无人称'的代词实验。","法国消费社会年表。"],
 "editions":["《岁月》中译名（《悠悠岁月》）待核。","法文原版。"],
 "order":"埃尔诺集大成之作；与《一个男人的位置》对读。"},
"pending":["'无人称自传'说法待核。","2008年出版（Gallimard说）待核。","2025年伦敦西区舞台改编（B380）待核。"],
"sources":["B380"],"year_source":"B380","author_source":"B380","related_works":["suiyue" if False else "leiyu","zenodeyishi","gududemigong"],
"svg":G("《岁月》无人称结构图",[{"title":"无人称","text":"记忆的语法（通说）","color":"main"},{"title":"岁月","text":"战后法国（B380）","color":"gold"},{"title":"照片","text":"时代的底片（通说）","color":"family"},{"title":"造作","text":"文类的自觉（B380）","color":"antagonist"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B37x/B38x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('wuzhizi','rushdie'), ('wumingyundesheng','kertesz'), ('suiyue','ernaux')]:
    if wid in created:
        link(aid, wid)
print('BATCH60 DONE')
