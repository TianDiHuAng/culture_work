# -*- coding: utf-8 -*-
"""批67：Britannica 新核 2 作家 2 部（拉格克维斯特 B387/迪内森 B388）"""
import json, pathlib

newsrc = [
{"id":"B387","title":"Par Lagerkvist — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Par-Lagerkvist","type":"百科全书","verified":True,"covers":["lagerkvist","balabasi"],"note":"2026-11-21 核对：全名 Pär Fabian Lagerkvist；1891-05-23瑞典韦克舍生—1974-07-11斯德哥尔摩卒（83岁）；1951诺贝尔文学奖；Dvärgen（侏儒, 1944）——'not until his novel Dvärgen (1944; The Dwarf) appeared that he had unqualified success with Swedish critics'——'became his first best-seller'；Barabbas（巴拉巴斯, 1950）——'With Barabbas (1950) he achieved world recognition'；Ordkonst och bildkonst (1913)——宣言；Ångest（苦闷, 1916）——一战悲观；Bödeln（刽子手, 1933）——'a protest against brutality'；Mannen utan själ (1936)——反法西斯；Låt människan leva (1949)——'stage oratorio'；Evening Land=Aftonland (1975)——W.H.奥登参与英译（66首）；'The influence of his early years remained strong despite his introduction to modern scientific ideas.'"},
{"id":"B388","title":"Isak Dinesen — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Isak-Dinesen","type":"百科全书","verified":True,"covers":["dinesen","zouchufeizhou"],"note":"2026-11-21 核对：原名 Karen Christence Dinesen，男爵夫人 Blixen-Finecke（另用笔名 Pierre Andrézel）；1885-04-17丹麦Rungsted生—1962-09-07Rungsted卒（77岁）；（B388 页未提诺奖——不采）；Seven Gothic Tales (1934；丹麦题 Syv fantastiske fortællinger)——'highly polished narratives in the Romantic tradition'——'incorporate the themes of eros and dreams'；Out of Africa（走出非洲, 1937；Den afrikanske farm）——肯尼亚岁月非虚构回忆——'a poetic reminiscence of her triumphs and her sorrows on the loss of her farm'——'an almost mystical love of Africa and its people'；1914嫁表兄男爵、1921离异后'continued to operate the plantation for 10 years'——'mismanagement, drought, and the falling price of coffee forced her return to Denmark'；先英文后丹麦文重写；Winter's Tales (1942)；Denys Finch Hatton（英国猎人伴侣）卒"},
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
{"id":"lagerkvist","name":"帕尔·拉格克维斯特","foreign_name":"Pär Fabian Lagerkvist（帕尔·法比安·拉格克维斯特，1891-05-23—1974-07-11）","country":"瑞典","birth":1891,"death":1974,"birth_year":1891,"death_year":1974,"era":"近代",
"summary":"拉格克维斯特，瑞典韦克舍生，作家——1951年诺贝尔文学奖（B387）。Dvärgen（侏儒, 1944）——'became his first best-seller'（首部畅销书——B387）；Barabbas（巴拉巴斯, 1950）——'With Barabbas (1950) he achieved world recognition'（B387）。Ångest（苦闷, 1916）——一战悲观（B387）；Bödeln（刽子手, 1933）——'a protest against brutality'（B387）。'The influence of his early years remained strong despite his introduction to modern scientific ideas.'（B387）。",
"timeline":[
 {"year":1891,"text":"5月23日生于瑞典韦克舍（B387）。","src":"B387"},
 {"year":1916,"text":"Ångest（苦闷）——一战悲观（B387）。","src":"B387"},
 {"year":1944,"text":"Dvärgen（侏儒）——首部畅销书（B387）。","src":"B387"},
 {"year":1951,"text":"获诺贝尔文学奖（B387）。","src":"B387"},
 {"year":1974,"text":"7月11日卒于斯德哥尔摩（B387）。","src":"B387"}],
"major_works":[
 {"work_id":"balabasi","note":"1950（B387）"},
 {"title":"侏儒","note":"（B387：Dvärgen (1944)——中译名待核）"},
 {"title":"刽子手","note":"（B387：Bödeln (1933)——中译名待核）"}],
"style":["'善恶'寓意的宗教书写（B387：Barabbas/Dvärgen 语境）。",
 "一战的悲观与暴力的抗议（B387：Ångest/Bödeln）。",
 "'早期影响始终强烈'（B387 引文）。"],
"status":"Britannica 定位拉格克维斯特为1951诺奖得主、《巴拉巴斯》使其世界闻名（B387）。",
"sources":["B387"],"dates_source":"B387",
"pending":["《巴拉巴斯》通行译名（《巴拉巴》）待核。","《侏儒》剧情细节待核（B387未载）。","'stage oratorio'（Låt människan leva 1949）细节待核。"]},
{"id":"dinesen","name":"伊萨克·迪内森","foreign_name":"Isak Dinesen（伊萨克·迪内森，原名 Karen Christence Dinesen，男爵夫人 Blixen-Finecke，1885-04-17—1962-09-07）","country":"丹麦","birth":1885,"death":1962,"birth_year":1885,"death_year":1962,"era":"近代",
"summary":"迪内森（男爵夫人布利克森），丹麦Rungsted生——Seven Gothic Tales（七篇哥特故事, 1934）——'highly polished narratives in the Romantic tradition'——'incorporate the themes of eros and dreams'（B388）。Out of Africa（走出非洲, 1937）——肯尼亚岁月的非虚构回忆——'a poetic reminiscence of her triumphs and her sorrows on the loss of her farm'——'an almost mystical love of Africa and its people'（B388）。1914年嫁表兄男爵、经营咖啡庄园、1921年离异后'continued to operate the plantation for 10 years'——'mismanagement, drought, and the falling price of coffee forced her return to Denmark'（B388）。先英文后丹麦文重写（B388）。",
"timeline":[
 {"year":1885,"text":"4月17日生于丹麦Rungsted（B388）。","src":"B388"},
 {"year":1914,"text":"嫁表兄男爵赴肯尼亚经营咖啡庄园（B388）。","src":"B388"},
 {"year":1934,"text":"Seven Gothic Tales——'浪漫传统的打磨叙事'（B388）。","src":"B388"},
 {"year":1937,"text":"Out of Africa（走出非洲）（B388）。","src":"B388"},
 {"year":1962,"text":"9月7日卒于Rungsted（B388）。","src":"B388"}],
"major_works":[
 {"work_id":"zouchufeizhou","note":"1937（B388）"},
 {"title":"七篇哥特故事","note":"（B388：Seven Gothic Tales (1934)——中译名待核）"},
 {"title":"冬天的故事集","note":"（B388：Winter's Tales (1942)——中译名待核）"}],
"style":["'浪漫传统的打磨叙事'（B388：highly polished narratives）。",
 "'eros 与梦'的主题（B388）。",
 "'对非洲及其人民近乎神秘的爱'（B388）。"],
"status":"Britannica 定位迪内森为《走出非洲》作者、哥特故事与回忆录的双栖作家（B388）。",
"sources":["B388"],"dates_source":"B388",
"pending":["诺奖与否——B388 页未提（不采）。","《走出非洲》1985年电影说待核（通说）。","Denys Finch Hatton 卒年（1931说）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"balabasi","title":"巴拉巴斯","original_title":"Barabbas","region":"瑞典","era":"近代","era_detail":"20世纪50年代初",
"genre":"长篇小说","genre_group":"小说","language":"瑞典语","author_id":"lagerkvist","author_name":"帕尔·拉格克维斯特",
"year_display":"1950年（Britannica B387：Barabbas (1950)——'With Barabbas (1950) he achieved world recognition'）","year_sort":1950,
"background":["Britannica（B387）：'With Barabbas (1950) he achieved world recognition'（由此世界闻名）。","Britannica（B387）：拉格克维斯特——1951诺奖。","题材（通说待核）：被释放的强盗巴拉巴斯——目睹基督之死后的黑暗求索。"],
"outline":["（通说待核）巴拉巴斯被释放：'代他'而死者的追随。","（通说待核）黑暗中'信'与'不信'的摇摆。"],
"characters":[{"name":"巴拉巴斯","identity":"被释放的强盗","note":"（B387 书名人物）"}],
"themes":["'黑暗中'的信仰求索（通说待核）。",
 "'代他'的救赎反讽（书名语境——通说待核）。",
 "一战的悲观底色（B387：Ångest 语系）。"],
"influence":[{"text":"Britannica：'achieved world recognition'（B387）。","source":"B387"},{"text":"Britannica：1951诺奖（B387 交叉）。","source":"B387"}],
"reading":{"difficulties":["宗教寓意的解读。","'强盗'视点的福音对照。"],
 "editions":["《巴拉巴斯》中译名（《巴拉巴》）待核。","瑞典文原版。"],
 "order":"拉格克维斯特首选；与《侏儒》对读。"},
"pending":["巴拉巴斯人名核对（B387书名）。","1950年出版细节待核。","1961年电影改编说待核（通说）。"],
"sources":["B387"],"year_source":"B387","author_source":"B387","related_works":["balabasi" if False else "derinahe","dulidemen","ezhihua"],
"svg":G("《巴拉巴斯》黑暗求索图",[{"title":"巴拉巴斯","text":"被释放的强盗（B387）","color":"main"},{"title":"黑暗","text":"信仰的求索（通说）","color":"gold"},{"title":"十字架","text":"'代他'的反讽（通说）","color":"family"},{"title":"1950","text":"世界闻名之年（B387）","color":"antagonist"}])},
{"id":"zouchufeizhou","title":"走出非洲","original_title":"Out of Africa","region":"丹麦","era":"近代","era_detail":"20世纪30年代",
"genre":"回忆录","genre_group":"散文","language":"英语（丹麦文重写）","author_id":"dinesen","author_name":"伊萨克·迪内森",
"year_display":"1937年（Britannica B388：Out of Africa (1937; Den afrikanske farm)）","year_sort":1937,
"background":["Britannica（B388）：肯尼亚岁月的非虚构回忆——'a poetic reminiscence of her triumphs and her sorrows on the loss of her farm'——'an almost mystical love of Africa and its people'。","Britannica（B388）：1914年嫁表兄男爵、经营咖啡庄园、1921年离异后'continued to operate the plantation for 10 years'——'mismanagement, drought, and the falling price of coffee forced her return to Denmark'。","Britannica（B388）：'She initially wrote first in English and then rewrote her books in Danish'。"],
"outline":["（通说待核）庄园的岁月：土著、猎游与'文明'的边界。","（通说待核）庄园的失去与'走出非洲'的告别。"],
"characters":[{"name":"男爵夫人（'我'）","identity":"庄园主","note":"（B388 语境）"},{"name":"丹尼斯·芬奇·哈顿","identity":"猎人伴侣","note":"（B388：Denys Finch Hatton——通说待核）"}],
"themes":["'近乎神秘的非洲之爱'（B388：an almost mystical love）。",
 "庄园的失去（B388：the loss of her farm）。",
 "'诗意回忆'的非虚构（B388：poetic reminiscence）。"],
"influence":[{"text":"Britannica：'poetic reminiscence'（B388）。","source":"B388"},{"text":"Britannica：'almost mystical love of Africa'（B388）。","source":"B388"}],
"reading":{"difficulties":["回忆录与自传的边界。","肯尼亚殖民史（通说待核）。"],
 "editions":["《走出非洲》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"迪内森代表作；与《七篇哥特故事》对读。"},
"pending":["丹尼斯·芬奇·哈顿卒年（1931说）待核。","1937年出版细节待核。","1985年电影改编说待核（通说）。"],
"sources":["B388"],"year_source":"B388","author_source":"B388","related_works":["gushiji","luomansailuo","xiaoyindejiti"],
"svg":G("《走出非洲》庄园回忆图",[{"title":"非洲","text":"'神秘的爱'（B388）","color":"gold"},{"title":"庄园","text":"咖啡的岁月（通说）","color":"main"},{"title":"失去","text":"'triumphs and sorrows'（B388）","color":"antagonist"},{"title":"走出","text":"告别的诗（书名）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B38x/B39x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('balabasi','lagerkvist'), ('zouchufeizhou','dinesen')]:
    if wid in created:
        link(aid, wid)
print('BATCH67 DONE')
