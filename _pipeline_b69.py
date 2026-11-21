# -*- coding: utf-8 -*-
"""批69：Britannica 新核 2 作家 2 部（克洛德·西蒙 B391/法朗士 B392）"""
import json, pathlib

newsrc = [
{"id":"B391","title":"Claude Simon — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Claude-Simon","type":"百科全书","verified":True,"covers":["csimon","fulandegonglu"],"note":"2026-11-21 核对：全名 Claude Eugène Henri Simon；1913-10-10马达加斯加塔那那利佛生—2005-07-06巴黎卒（91岁）；1985诺贝尔文学奖；'whose works are among the most authentic representatives of the French nouveau roman (new novel) that emerged in the 1950s'；La Route des Flandres（弗兰德公路, 1960）——与 L'Herbe/La Palace/Histoire 构成循环四部（人物事件反复）——'Many critics consider these novels, especially La Route des Flandres, to be his most important work'；风格：叙述与意识流混合——'lacking all punctuation and heavy with 1,000-word sentences'——'to capture the very progression of life'（捕捉生命的推进本身）；骑兵军官之子（父卒于一战）、佩皮尼昂由母抚养；巴黎/牛津/剑桥求学；1940年5月被德军俘、逃脱、参加抵抗运动；后在法国南部购葡萄园；Le Tricheur (1945)首作；Histoire (1967)；Les Géorgiques (1981)；Le Tramway (2001)"},
{"id":"B392","title":"Anatole France — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Anatole-France","type":"百科全书","verified":True,"covers":["france","qiedao"],"note":"2026-11-21 核对：原名 Jacques-Anatole-François Thibault；1844-04-16巴黎生—1924-10-12 Saint-Cyr-sur-Loire卒（80岁）；1921诺贝尔文学奖；L'Île des Pingouins（企鹅岛, 1908）——'An extended satire of French society through the ages'（历代法国社会的长篇讽刺）；Les Dieux ont soif（诸神渴了, 1912）——'A condemnation of fanaticism set during the French Revolution'；Crainquebille (1903)——'dramatizes the unjust treatment of a small tradesman'；1896年入选法兰西学院；德雷福斯事件的亲德雷福斯立场使其写作转向社会关怀；后倾向社会主义与共产主义——但其作品'show little belief in the ultimate arrival of a fraternal society'；Le Crime de Sylvestre Bonnard (1881)、Thaïs (1890)、Le Lys rouge (1894)"},
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
{"id":"csimon","name":"克洛德·西蒙","foreign_name":"Claude Simon（克洛德·欧仁·亨利·西蒙，1913-10-10—2005-07-06）","country":"法国","birth":1913,"death":2005,"birth_year":1913,"death_year":2005,"era":"现当代",
"summary":"西蒙，马达加斯加塔那那利佛生，法国作家——1985年诺贝尔文学奖（B391）；'whose works are among the most authentic representatives of the French nouveau roman'（法国新小说最纯正的代表之一——B391）。La Route des Flandres（弗兰德公路, 1960）——与《草》《宫》《史》构成循环四部——'Many critics consider these novels, especially La Route des Flandres, to be his most important work'（B391）。风格：叙述与意识流混合——'lacking all punctuation and heavy with 1,000-word sentences'——'to capture the very progression of life'（B391）。1940年5月被德军俘、逃脱、参加抵抗运动（B391）。",
"timeline":[
 {"year":1913,"text":"10月10日生于马达加斯加塔那那利佛（B391）。","src":"B391"},
 {"year":1940,"text":"5月被德军俘、逃脱、参加抵抗运动（B391）。","src":"B391"},
 {"year":1960,"text":"La Route des Flandres——'most important work'（B391）。","src":"B391"},
 {"year":1985,"text":"获诺贝尔文学奖（B391）。","src":"B391"},
 {"year":2005,"text":"7月6日卒于巴黎（B391）。","src":"B391"}],
"major_works":[
 {"work_id":"fulandegonglu","note":"1960（B391）"},
 {"title":"历史","note":"（B391：Histoire (1967)）"},
 {"title":"农事诗","note":"（B391：Les Géorgiques (1981)——中译名待核）"}],
"style":["新小说的'最纯正代表'（B391）。",
 "'无标点的千词长句'（B391：lacking all punctuation...1,000-word sentences）。",
 "'捕捉生命的推进本身'（B391）。"],
"status":"Britannica 定位克洛德·西蒙为1985诺奖得主、法国新小说的代表（B391）。",
"sources":["B391"],"dates_source":"B391",
"pending":["《弗兰德公路》通行译名待核。","'千词长句'细节核对（B391口径）。","'循环四部'（La Route/L'Herbe/La Palace/Histoire）核对（B391已载）。"]},
{"id":"france","name":"阿纳托尔·法朗士","foreign_name":"Anatole France（阿纳托尔·法朗士，原名 Jacques-Anatole-François Thibault，1844-04-16—1924-10-12）","country":"法国","birth":1844,"death":1924,"birth_year":1844,"death_year":1924,"era":"近代",
"summary":"法朗士，巴黎生，法国作家——1921年诺贝尔文学奖（B392）。L'Île des Pingouins（企鹅岛, 1908）——'An extended satire of French society through the ages'（历代法国社会的长篇讽刺——B392）。Les Dieux ont soif（诸神渴了, 1912）——'A condemnation of fanaticism set during the French Revolution'（法国大革命中的狂热主义批判——B392）。Crainquebille (1903)——'dramatizes the unjust treatment of a small tradesman'（B392）。1896年入选法兰西学院（B392）；德雷福斯事件使其写作转向社会关怀（B392）。",
"timeline":[
 {"year":1844,"text":"4月16日生于巴黎（B392）。","src":"B392"},
 {"year":1896,"text":"入选法兰西学院（B392）。","src":"B392"},
 {"year":1908,"text":"《企鹅岛》（B392）。","src":"B392"},
 {"year":1921,"text":"获诺贝尔文学奖（B392）。","src":"B392"},
 {"year":1924,"text":"10月12日卒于Saint-Cyr-sur-Loire（B392）。","src":"B392"}],
"major_works":[
 {"work_id":"qiedao","note":"1908（B392）"},
 {"title":"诸神渴了","note":"（B392：Les Dieux ont soif (1912)——中译名待核）"},
 {"title":"苔依丝","note":"（B392：Thaïs (1890)）"}],
"style":["'历代法国社会的长篇讽刺'（B392：Penguin Island）。",
 "'狂热主义的批判'（B392：The Gods Are Athirst）。",
 "古典的'优雅'与怀疑主义（作者级语境——通说待核）。"],
"status":"Britannica 定位法朗士为1921诺奖得主、社会关怀转向的古典讽刺家（B392）。",
"sources":["B392"],"dates_source":"B392",
"pending":["《企鹅岛》通行译名待核。","德雷福斯事件细节（B392：pro-Dreyfus commitment）待核。","'法兰西学院'1896年（B392）核对。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"fulandegonglu","title":"弗兰德公路","original_title":"La Route des Flandres","region":"法国","era":"近代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"csimon","author_name":"克洛德·西蒙",
"year_display":"1960年（Britannica B391：La Route des Flandres (1960)——'his most important work'说）","year_sort":1960,
"background":["Britannica（B391）：与 L'Herbe/La Palace/Histoire 构成循环四部——'Many critics consider these novels, especially La Route des Flandres, to be his most important work'。","Britannica（B391）：风格——'lacking all punctuation and heavy with 1,000-word sentences'——'to capture the very progression of life'。","Britannica（B391）：西蒙——1940年5月被德军俘、逃脱、参加抵抗运动——1940溃败为其素材（交叉——待核）。"],
"outline":["（通说待核——B391未载剧情）1940年溃退的骑兵与'德·雷谢尔'的传说。","（通说待核）'公路'上马匹与人体的'色彩'流。"],
"characters":[{"name":"乔治","identity":"骑兵/叙述者","note":"（通说待核，B391未载）"},{"name":"德·雷谢尔","identity":"旧贵族","note":"（通说待核）"}],
"themes":["1940溃败的'色彩'书写（通说待核）。",
 "'无标点'的意识流（B391）。",
 "循环四部的人物复现（B391）。"],
"influence":[{"text":"Britannica：1985诺奖（B391）。","source":"B391"},{"text":"Britannica：'his most important work'说（B391）。","source":"B391"}],
"reading":{"difficulties":["'千词长句'（B391）。","1940年法国溃败史。"],
 "editions":["《弗兰德公路》中译本（漓江/人民文学等——通说待核）。","法文原版。"],
 "order":"西蒙代表作；新小说读者首选。"},
"pending":["乔治/德·雷谢尔人名核对（通说）。","1960年出版细节待核。","'四部循环'结构核对（B391已载四部名）。"],
"sources":["B391"],"year_source":"B391","author_source":"B391","related_works":["zaidiceng","meiguobuqu","wuhhaotuchang"],
"svg":G("《弗兰德公路》溃败色彩图",[{"title":"公路","text":"溃败的行军（通说）","color":"main"},{"title":"千词长句","text":"'无标点'的意识流（B391）","color":"gold"},{"title":"循环","text":"四部的人物复现（B391）","color":"family"},{"title":"色彩","text":"马匹与人体（通说）","color":"antagonist"}])},
{"id":"qiedao","title":"企鹅岛","original_title":"L'Île des Pingouins","region":"法国","era":"近代","era_detail":"20世纪初",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"france","author_name":"阿纳托尔·法朗士",
"year_display":"1908年（Britannica B392：L'Île des Pingouins (1908)——'An extended satire of French society through the ages'）","year_sort":1908,
"background":["Britannica（B392）：'An extended satire of French society through the ages'（历代法国社会的长篇讽刺）。","Britannica（B392）：法朗士——1921诺奖；德雷福斯事件后转向社会关怀。","题材（通说待核）：近视修士把企鹅误认为人——'受洗'而衍生的伪岛史。"],
"outline":["（通说待核）圣马埃尔修士为企鹅'施洗'——伦理的喜剧开端。","（通说待核）八卷企鹅岛编年：从建国到'未来'的末世（通说待核）。"],
"characters":[{"name":"圣马埃尔","identity":"近视修士","note":"（通说待核）"},{"name":"企鹅岛民","identity":"讽喻人类","note":"（通说待核）"}],
"themes":["'历代法国社会的长篇讽刺'（B392）。",
 "施洗误会的原型喜剧（通说待核）。",
 "'历史'的循环讽喻（通说待核）。"],
"influence":[{"text":"Britannica：'An extended satire of French society through the ages'（B392）。","source":"B392"},{"text":"Britannica：1921诺奖（B392 交叉）。","source":"B392"}],
"reading":{"difficulties":["讽喻的历史层次。","'企鹅'与'人'的镜像。"],
 "editions":["《企鹅岛》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"法朗士讽刺首选；与《诸神渴了》对读。"},
"pending":["圣马埃尔修士细节核对（通说）。","1908年出版细节待核。","八卷结构核对（通说）。"],
"sources":["B392"],"year_source":"B392","author_source":"B392","related_works":["qiedao" if False else "leiyu","minzuyishi","sangeshouqiangshou"],
"svg":G("《企鹅岛》讽喻结构图",[{"title":"企鹅","text":"被误认的人类（通说）","color":"main"},{"title":"施洗","text":"误会的开端（通说）","color":"gold"},{"title":"讽刺","text":"'历代法国社会'（B392）","color":"family"},{"title":"编年","text":"八卷的岛史（通说）","color":"antagonist"}])},
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

for wid, aid in [('fulandegonglu','csimon'), ('qiedao','france')]:
    if wid in created:
        link(aid, wid)
print('BATCH69 DONE')
