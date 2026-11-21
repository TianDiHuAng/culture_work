# -*- coding: utf-8 -*-
"""批72：Britannica 新核 2 作家 2 部（布莱克 B397/斯特恩 B398）"""
import json, pathlib

newsrc = [
{"id":"B397","title":"William Blake — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/William-Blake","type":"百科全书","verified":True,"covers":["blake","tianzhenyujiy"],"note":"2026-11-21 核对：1757-11-28伦敦生（'born over his father's modest hosiery shop at 28 Broad Street, Golden Square'）—1827-08-12伦敦卒（69岁）；Songs of Innocence (1789) 与 Songs of Experience (1794)——1794年合刊全题'Songs of Innocence and of Experience: Shewing the Two Contrary States of the Human Soul'（展示人类灵魂的两种对立状态）；'The Lamb'与'The Tyger'分别为纯真之保护与败坏的象征；彩色印刷（illuminated printing）——'etched, printed, coloured, stitched, and sold'自印自售（妻 Catherine 协助）；Milton (1804-?11)——'Jerusalem'歌词'which has become a kind of second national anthem in Britain'；Jerusalem (1804-?20)；引文'To see a World in a Grain of Sand / And a Heaven in a Wild Flower'（'Auguries of Innocence'开篇）、'really drunk with intellectual vision whenever I take a pencil or graver into my hand'（1804）；生前'generally neglected or (unjustly) dismissed as mad'——Alexander Gilchrist 1863年传记后声名复苏；妻述'he is always in Paradise'"},
{"id":"B398","title":"Laurence Sterne — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Laurence-Sterne","type":"百科全书","verified":True,"covers":["sterne","xiangdizhuan"],"note":"2026-11-21 核对：1713-11-24爱尔兰Clonmel生—1768-03-18伦敦卒（54岁）；Tristram Shandy（项狄传）——全题 The Life and Opinions of Tristram Shandy, Gentleman——九卷1759-67（前两卷自费于约克出版，1759年末）——'a novel in which story is subordinate to the free associations and digressions of its narrator'（故事从属于叙述者的自由联想与离题）；洛克心理学影响——心理小说与意识流小说的先声；斯特恩自言每句都'written under the greatest heaviness of heart'；A Sentimental Journey Through France and Italy——1768年初以'Mr. Yorick'署名——'Defies travel-book conventions; focuses on meaningful human connection'——意大利部分未完成；布道集两卷（1760）；A Political Romance (1759)——斯威夫特式讽刺被教会下令焚毁；'Now it is come'遗言；遗体曾被盗尸作解剖课——现葬于 Coxwold Shandy Hall 附近"},
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
{"id":"blake","name":"威廉·布莱克","foreign_name":"William Blake（威廉·布莱克，1757-11-28—1827-08-12）","country":"英国","birth":1757,"death":1827,"birth_year":1757,"death_year":1827,"era":"近代",
"summary":"布莱克，伦敦生（父亲袜店楼上），诗人与版画家——1827年卒，69岁（B397）。Songs of Innocence (1789) 与 Songs of Experience (1794)——1794年合刊全题'Songs of Innocence and of Experience: Shewing the Two Contrary States of the Human Soul'（展示人类灵魂的两种对立状态——B397）；'The Lamb'与'The Tyger'分别为纯真之保护与败坏的象征（B397）。彩色印刷（illuminated printing）——'etched, printed, coloured, stitched, and sold'自印自售（妻 Catherine 协助）（B397）。Milton 中'Jerusalem'歌词——'which has become a kind of second national anthem in Britain'（B397）。引文'To see a World in a Grain of Sand / And a Heaven in a Wild Flower'（B397）。生前'generally neglected or (unjustly) dismissed as mad'——Gilchrist 1863年传记后声名复苏（B397）。",
"timeline":[
 {"year":1757,"text":"11月28日生于伦敦袜店楼上（B397）。","src":"B397"},
 {"year":1789,"text":"Songs of Innocence（天真之歌）（B397）。","src":"B397"},
 {"year":1794,"text":"Songs of Experience——合刊《天真与经验之歌》（B397）。","src":"B397"},
 {"year":1827,"text":"8月12日卒于伦敦（B397）。","src":"B397"}],
"major_works":[
 {"work_id":"tianzhenyujiy","note":"1789/1794合刊（B397）"},
 {"title":"弥尔顿","note":"（B397：Milton (1804-?11)——含'Jerusalem'歌词）"},
 {"title":"耶路撒冷","note":"（B397：Jerusalem (1804-?20)）"}],
"style":["'人类灵魂的两种对立状态'（B397：Two Contrary States of the Human Soul）。",
 "彩色印刷的自印自售（B397：illuminated printing）。",
 "'一沙一世界'的箴言诗（B397 引文）。"],
"status":"Britannica 定位布莱克为诗人版画家、生前被忽视而身后复兴（B397）。",
"sources":["B397"],"dates_source":"B397",
"pending":["《天真与经验之歌》通行译名待核。","'彩色印刷法'来历（兄 Robert 说——B397 提及问答）待核。","'老虎'/'羔羊'细节核对（B397已载象征定位）。"]},
{"id":"sterne","name":"劳伦斯·斯特恩","foreign_name":"Laurence Sterne（劳伦斯·斯特恩，1713-11-24—1768-03-18）","country":"爱尔兰","birth":1713,"death":1768,"birth_year":1713,"death_year":1768,"era":"近代",
"summary":"斯特恩，爱尔兰Clonmel生，英国小说家与约克教士——1768年卒，54岁（B398）。Tristram Shandy（项狄传）——九卷1759-67（前两卷自费于约克出版）——'a novel in which story is subordinate to the free associations and digressions of its narrator'（故事从属于叙述者的自由联想与离题——B398）；洛克心理学影响——心理小说与意识流小说的先声（B398）。A Sentimental Journey（感伤旅行, 1768）——以'Mr. Yorick'署名——'Defies travel-book conventions; focuses on meaningful human connection'（B398）。遗言'Now it is come'（B398）。",
"timeline":[
 {"year":1713,"text":"11月24日生于爱尔兰Clonmel（B398）。","src":"B398"},
 {"year":1759,"text":"《项狄传》前两卷自费出版（B398）。","src":"B398"},
 {"year":1760,"text":"布道集两卷出版（B398）。","src":"B398"},
 {"year":1768,"text":"《感伤旅行》初刊（意大利部分未完成）；3月18日卒于伦敦（B398）。","src":"B398"}],
"major_works":[
 {"work_id":"xiangdizhuan","note":"1759-67九卷（B398）"},
 {"title":"感伤旅行","note":"（B398：A Sentimental Journey (1768)——中译名待核）"},
 {"title":"布道集","note":"（B398：sermons 两卷 (1760)）"}],
"style":["'故事从属于自由联想与离题'（B398）。",
 "洛克心理学与'意识流先声'（B398：forerunner of psychological and stream-of-consciousness fiction）。",
 "'每句都写于心底最沉重时'（B398：greatest heaviness of heart）。"],
"status":"Britannica 定位斯特恩为《项狄传》作者、心理与意识流小说的先声（B398）。",
"sources":["B398"],"dates_source":"B398",
"pending":["《项狄传》通行译名待核。","'盗尸解剖'轶事（B398已载）核对。","'墨迹页''黑页'等著名实验细节待核（B398未载——通说）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"tianzhenyujiy","title":"天真与经验之歌","original_title":"Songs of Innocence and of Experience","region":"英国","era":"近代","era_detail":"18世纪80-90年代",
"genre":"诗集（彩色印刷）","genre_group":"诗歌","language":"英语","author_id":"blake","author_name":"威廉·布莱克",
"year_display":"1789/1794年（Britannica B397：Songs of Innocence (1789) 与 Songs of Experience (1794)——1794年合刊全题'Shewing the Two Contrary States of the Human Soul'）","year_sort":1794,
"background":["Britannica（B397）：1794年合刊全题'Songs of Innocence and of Experience: Shewing the Two Contrary States of the Human Soul'（展示人类灵魂的两种对立状态）。","Britannica（B397）：'The Lamb'与'The Tyger'分别为纯真之保护与败坏的象征。","Britannica（B397）：彩色印刷——'etched, printed, coloured, stitched, and sold'自印自售（妻 Catherine 协助）。"],
"outline":["（通说待核）'羔羊'与'老虎'：同一造物主的两面。","（通说待核）《扫烟囱的孩子》两版本的对位。"],
"characters":[{"name":"羔羊/老虎","identity":"纯真与经验的象征","note":"（B397：symbols of innocence's protection and corruption）"}],
"themes":["'人类灵魂的两种对立状态'（B397）。",
 "羔羊/老虎的象征对位（B397）。",
 "自印自售的艺术革命（B397：illuminated printing）。"],
"influence":[{"text":"Britannica：'Shewing the Two Contrary States of the Human Soul'（B397）。","source":"B397"},{"text":"Britannica：Gilchrist 1863年传记后声名复苏（B397 交叉）。","source":"B397"}],
"reading":{"difficulties":["'彩色印刷'的图文合体。","两版的对位阅读。"],
 "editions":["《天真与经验之歌》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"布莱克首选；与《耶路撒冷》对读。"},
"pending":["《羔羊》《老虎》细节核对（B397已载象征定位）。","1789/1794年版式差异待核。","'Milton'中'Jerusalem'歌词（B397已载）核对。"],
"sources":["B397"],"year_source":"B397","author_source":"B397","related_works":["songge1819","caihuaji","xianrenji"],
"svg":G("《天真与经验之歌》对位结构图",[{"title":"天真","text":"羔羊的保护（B397）","color":"family"},{"title":"经验","text":"老虎的败坏（B397）","color":"antagonist"},{"title":"对位","text":"'两种对立状态'（B397）","color":"main"},{"title":"彩色印刷","text":"自印自售（B397）","color":"gold"}])},
{"id":"xiangdizhuan","title":"项狄传","original_title":"The Life and Opinions of Tristram Shandy, Gentleman","region":"英国","era":"近代","era_detail":"18世纪50-60年代",
"genre":"长篇小说（九卷）","genre_group":"小说","language":"英语","author_id":"sterne","author_name":"劳伦斯·斯特恩",
"year_display":"1759-67年（Britannica B398：九卷——'a novel in which story is subordinate to the free associations and digressions of its narrator'）","year_sort":1759,
"background":["Britannica（B398）：'a novel in which story is subordinate to the free associations and digressions of its narrator'（故事从属于叙述者的自由联想与离题）。","Britannica（B398）：洛克心理学影响——'forerunner of psychological and stream-of-consciousness fiction'（心理小说与意识流小说的先声）。","Britannica（B398）：前两卷自费于约克出版（1759年末）；斯特恩自言每句都'written under the greatest heaviness of heart'。"],
"outline":["（通说待核——B398未载剧情）'项狄'的出生被叙述延宕：名字、鼻子与'窗户'。","（通说待核）'墨迹页'与'黑页'的实验（通说待核——B398未载）。"],
"characters":[{"name":"特里斯特拉姆","identity":"未出生的主角","note":"（B398 书名人物）"},{"name":"托比叔叔","identity":"伤腿的叔叔","note":"（通说待核）"}],
"themes":["'故事从属于联想与离题'（B398）。",
 "'意识流小说的先声'（B398：forerunner）。",
 "'心底最沉重'的滑稽（B398 引文）。"],
"influence":[{"text":"Britannica：'forerunner of psychological and stream-of-consciousness fiction'（B398）。","source":"B398"},{"text":"Britannica：'story is subordinate to...digressions'（B398）。","source":"B398"}],
"reading":{"difficulties":["离题的结构（无'故事线'）。","十八世纪讽刺语境。"],
 "editions":["《项狄传》中译本（人民文学/上海译文等——通说待核）。","英文原版（公有领域）。"],
 "order":"斯特恩代表作；与《感伤旅行》对读。"},
"pending":["九卷年份核对（B398：1759-67）。","'墨迹页/黑页'实验核对（通说——B398未载）。","托比叔叔细节待核。"],
"sources":["B398"],"year_source":"B398","author_source":"B398","related_works":["luoting","weite","sangeshibing"],
"svg":G("《项狄传》离题结构图",[{"title":"离题","text":"'自由联想'的叙事（B398）","color":"main"},{"title":"延宕","text":"出生的被推迟（通说）","color":"gold"},{"title":"先声","text":"意识流的祖先（B398）","color":"family"},{"title":"滑稽","text":"'心底最沉重'（B398引文）","color":"antagonist"}])},
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

for wid, aid in [('tianzhenyujiy','blake'), ('xiangdizhuan','sterne')]:
    if wid in created:
        link(aid, wid)
print('BATCH72 DONE')
