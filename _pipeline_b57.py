# -*- coding: utf-8 -*-
"""批57：Britannica 新核卡彭铁尔 B373（这个世界的王国）+ 零成本2部（爱/蜜蜂的生活）+ 过期条目清理"""
import json, pathlib

newsrc = [
{"id":"B373","title":"Alejo Carpentier y Valmont — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Alejo-Carpentier-y-Valmont","type":"百科全书","verified":True,"covers":["carpentier","zhegeshijiedewanguo"],"note":"2026-11-21 核对：1904-12-26洛桑生（法父俄母）——'Carpentier claimed throughout his life that he was Cuban-born'——1980-04-24巴黎卒（75岁）；El reino de este mundo（这个世界的王国, 1949）——第二部长篇——'the first to enjoy wide acclaim'——'is about the Haitian revolution'——序言'expounds on magic realism, which he defines as the representation of marvelous American reality'（神奇的现实）；The Lost Steps（消隐的阶梯, 1953）——'his best-known work'——奥里诺科丛林寻'时间起源'；Explosion in a Cathedral (1962)——法国大革命冲击加勒比——引发诺奖呼声（未遂）；Cervantes Prize 1977；音乐学家：Music in Cuba (1946)；1928年逃马查多独裁至巴黎；1959返哈瓦那、60年代中期起任驻巴黎外交官；¡Ecue-Yamba-O! (1933)；Journey Back to the Source (1944)"},
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

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"carpentier","name":"阿莱霍·卡彭铁尔","foreign_name":"Alejo Carpentier（阿莱霍·卡彭铁尔，1904-12-26—1980-04-24）","country":"古巴","birth":1904,"death":1980,"birth_year":1904,"death_year":1980,"era":"近代",
"summary":"卡彭铁尔，生于洛桑（法父俄母）——'Carpentier claimed throughout his life that he was Cuban-born'（一生自称古巴生——B373）——1980年卒于巴黎。El reino de este mundo（这个世界的王国, 1949）——'the first to enjoy wide acclaim'——写海地革命——其序言'expounds on magic realism...the representation of \"marvelous American reality\"'（神奇的现实——魔幻现实主义的经典表述——B373）。The Lost Steps（消隐的阶梯, 1953）——'his best-known work'（B373）。音乐学家：Music in Cuba (1946)（B373）。1977年塞万提斯奖（B373）。",
"timeline":[
 {"year":1904,"text":"12月26日生于洛桑，襁褓中抵哈瓦那（B373）。","src":"B373"},
 {"year":1928,"text":"逃马查多独裁至巴黎（B373）。","src":"B373"},
 {"year":1949,"text":"El reino de este mundo——魔幻现实主义序言（B373）。","src":"B373"},
 {"year":1953,"text":"The Lost Steps——'best-known work'（B373）。","src":"B373"},
 {"year":1980,"text":"4月24日卒于巴黎（B373）。","src":"B373"}],
"major_works":[
 {"work_id":"zhegeshijiedewanguo","note":"1949（B373）"},
 {"title":"消隐的阶梯","note":"（B373：The Lost Steps (1953)——'his best-known work'）"},
 {"title":"大教堂里的爆炸","note":"（B370式列举：Explosion in a Cathedral (1962)——中译名待核）"}],
"style":["'神奇的现实'（B373：marvelous American reality）。",
 "音乐学家的史前史方法（B373：Music in Cuba 交叉）。",
 "巴洛克句法（'barroco'说——通说待核）。"],
"status":"Britannica 定位卡彭铁尔为魔幻现实主义概念的阐述者、拉美先锋（B373；B053 交叉：马尔克斯承之）。",
"sources":["B373"],"dates_source":"B373",
"pending":["生地（洛桑）与'自称古巴生'的矛盾口径核对（B373）。","《消隐的阶梯》通行译名待核。","'巴洛克'风格说法待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"zhegeshijiedewanguo","title":"这个世界的王国","original_title":"El reino de este mundo","region":"古巴","era":"近代","era_detail":"20世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"carpentier","author_name":"阿莱霍·卡彭铁尔",
"year_display":"1949年（Britannica B373：El reino de este mundo (1949)——'the first to enjoy wide acclaim'）","year_sort":1949,
"background":["Britannica（B373）：'is about the Haitian revolution'——海地革命史。","Britannica（B373）：其序言'expounds on magic realism, which he defines as the representation of \"marvelous American reality\"'——魔幻现实主义的经典表述。","Britannica（B373）：卡彭铁尔——音乐学家与作家（B053 交叉：马尔克斯承之）。"],
"outline":["（通说待核）海地革命（1750-1820——B373 交叉口径）：黑奴蒂-诺埃尔的见证。","（通说待核）'人变兽'的神奇现实：马坎达尔的神迹与烧毁。"],
"characters":[{"name":"蒂-诺埃尔","identity":"黑奴/见证者","note":"（通说待核）"},{"name":"马坎达尔","identity":"起义领袖","note":"（通说待核）"}],
"themes":["'神奇的美国现实'（B373：marvelous American reality）。",
 "海地革命的暴力循环（B373：Haitian revolution）。",
 "'信者见神迹'的叙事伦理（通说待核）。"],
"influence":[{"text":"Britannica：魔幻现实主义序言（B373）。","source":"B373"},{"text":"Britannica：马尔克斯等拉美作家的先声（B053 交叉）。","source":"B053"}],
"reading":{"difficulties":["海地革命史（杜桑等——通说待核）。","'神奇现实'与'魔幻'的术语。"],
 "editions":["《这个世界的王国》中译名（《人间王国》）待核。","西班牙文原版。"],
 "order":"魔幻现实主义源头首选；与《百年孤独》对读。"},
"pending":["蒂-诺埃尔/马坎达尔人名核对（通说）。","1949年出版细节待核。","'1750-1820'年代口径核对（B373 交叉）。"],
"sources":["B373"],"year_source":"B373","author_source":"B373","related_works":["peideluobalamo","gmx" if False else "bainian" if "bainian" in existing else "leiyu","nongmin"],
"svg":G("《这个世界的王国》神奇现实图",[{"title":"神奇现实","text":"'marvelous American reality'（B373）","color":"gold"},{"title":"海地革命","text":"黑奴的世纪（B373）","color":"main"},{"title":"神迹","text":"信者的叙事（通说）","color":"family"},{"title":"白人","text":"碾压的秩序（通说）","color":"antagonist"}])},
# 零成本
{"id":"ai1963","title":"爱","original_title":"Un amore","region":"意大利","era":"近代","era_detail":"20世纪60年代",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"buzzati","author_name":"迪诺·布扎蒂",
"year_display":"1963年（Britannica B351：Un amore (1963)——中译名待核）","year_sort":1963,
"background":["Britannica（B351）：Un amore (1963)——'a novel about a middle-aged man and a devious young woman'。","Britannica（B351）：布扎蒂——'detached sense of irony and humor'。","题材（通说待核）：中年建筑师与米兰妓女拉伊达——痴迷与观察。"],
"outline":["（通说待核）中年男子的痴恋：'观察'与占有。","（通说待核）米兰的夜色与'爱'的账目。"],
"characters":[{"name":"乔瓦尼","identity":"中年建筑师","note":"（通说待核，B351未载）"},{"name":"拉伊达","identity":"年轻女子","note":"（通说待核，B351：a devious young woman）"}],
"themes":["痴迷的观察者（B351：middle-aged man and a devious young woman）。",
 "'爱'的商品化（通说待核）。",
 "米兰都市（B351 语境）。"],
"influence":[{"text":"Britannica：Un amore (1963)（B351）。","source":"B351"},{"text":"Britannica：'detached sense of irony'（B351）。","source":"B351"}],
"reading":{"difficulties":["'痴恋'的心理。","1960年代米兰都市史。"],
 "editions":["《爱》中译名（《爱情》）待核。","意大利文原版。"],
 "order":"布扎蒂'爱'篇；与《鞑靼人沙漠》对读。"},
"pending":["乔瓦尼/拉伊达人名核对（B351未载人名）。","1963年出版细节待核。","'建筑'职业细节待核。"],
"sources":["B351"],"year_source":"B351","author_source":"B351","related_works":["datatarenshamo","liushipian","mengya"],
"svg":G("《爱》痴迷结构图",[{"title":"痴迷","text":"中年的凝视（通说）","color":"main"},{"title":"拉伊达","text":"'狡黠的年轻女子'（B351）","color":"antagonist"},{"title":"米兰","text":"都市的夜（通说）","color":"family"},{"title":"反讽","text":"疏离的目光（B351）","color":"gold"}])},
{"id":"mifengdeshenghuo","title":"蜜蜂的生活","original_title":"La Vie des abeilles","region":"比利时","era":"近代","era_detail":"20世纪初",
"genre":"散文集（自然随笔）","genre_group":"散文","language":"法语","author_id":"maeterlinck","author_name":"莫里斯·梅特林克",
"year_display":"1901年（Britannica B372：La Vie des abeilles (1901)）","year_sort":1901,
"background":["Britannica（B372）：La Vie des abeilles——梅特林克作品列表（与 Le Trésor des humbles 1896 并列）。","Britannica（B372）：梅特林克——1911诺奖；象征主义戏剧家。","题材（通说待核）：蜂巢的'哲学'——蜂王、雄蜂与工蜂的乌托邦观察。"],
"outline":["（通说待核）蜂巢的观察：分蜂、蜂王的诞生与屠杀。","（通说待核）'蜜蜂的生活'作为人类社会的镜。"],
"characters":[{"name":"蜂王","identity":"巢的君主","note":"（通说待核）"}],
"themes":["蜂巢的'共和国'（通说待核）。",
 "自然随笔的科学诗（B372 语系）。",
 "'命运'的哲学（作者页语境）。"],
"influence":[{"text":"Britannica：La Vie des abeilles (1901)（B372）。","source":"B372"},{"text":"Britannica：1911诺奖（B372 交叉）。","source":"B372"}],
"reading":{"difficulties":["养蜂学的术语。","'拟人'的限度。"],
 "editions":["《蜜蜂的生活》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"梅特林克散文首选；与《青鸟》对读。"},
"pending":["篇目结构核对（通说）。","1901年出版细节待核。","'拟人化'限度待核。"],
"sources":["B372"],"year_source":"B372","author_source":"B372","related_works":["qingniao","peiliyasi","jichengzhe"],
"svg":G("《蜜蜂的生活》蜂巢哲学图",[{"title":"蜂巢","text":"共和国的镜（通说）","color":"gold"},{"title":"蜂王","text":"屠杀与诞生的循环（通说）","color":"main"},{"title":"自然","text":"科学诗（B372语系）","color":"family"},{"title":"命运","text":"哲学的底色（作者页语境）","color":"antagonist"}])},
]
created = []
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    created.append(w['id'])
    print('work', w['id'])

def link(aid, wid, kw=None):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        done = False
        if kw:
            for i, m in enumerate(j['major_works']):
                if m.get('title') and kw in m['title']:
                    j['major_works'][i] = {"work_id": wid, "note": m['note']}
                    done = True; break
        if not done:
            j['major_works'].append({"work_id": wid, "note": "（批57）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('zhegeshijiedewanguo','carpentier','这个世界的王国'),('ai1963','buzzati','爱'),('mifengdeshenghuo','maeterlinck','蜜蜂的生活')]:
    if wid in created:
        link(aid, wid, kw)

# 过期条目清理：aeschylus 俄瑞斯忒亚三部曲（已有 eruosteya）
found_er = None
for p2 in pathlib.Path('data/works').glob('*.json'):
    j2 = json.loads(p2.read_text(encoding='utf-8'))
    if j2['title'] == '俄瑞斯忒亚':
        found_er = p2.stem
if found_er:
    p = pathlib.Path('data/authors/aeschylus.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    for i, m in enumerate(j['major_works']):
        if m.get('title') and '俄瑞斯忒亚' in m['title'] and not m.get('work_id'):
            j['major_works'][i] = {"work_id": found_er, "note": m['note'] + '（复用已有作品页）'}
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('stale fixed aeschylus ->', found_er)
print('BATCH57 DONE')
