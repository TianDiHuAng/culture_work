# -*- coding: utf-8 -*-
"""批75：Britannica 新核 2 作家 2 部（阿波利奈尔 B403 醇酒集/科莱特 B404 吉吉）"""
import json, pathlib

newsrc = [
{"id":"B403","title":"Guillaume Apollinaire — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Guillaume-Apollinaire","type":"百科全书","verified":True,"covers":["apollinaire","chunjiuji"],"note":"2026-11-21 核对：1880-08-26罗马生（波兰移民之女与意大利军官之子——'he kept his origins secret'）—1918-11-09巴黎卒（38岁）——'Weakened by war wounds, he died of Spanish influenza'（西班牙流感）；Alcools（醇酒集, 1913）——'his poetic masterpiece, always without punctuation'（始终无标点）——混亚历山大体/规则诗节/短无韵行；Calligrammes（图像诗, 1918）——'dominated by images of war'——诗即图像（版式排布）；Les Mamelles de Tirésias（剧，1917年上演；普朗克歌剧1947）——'believed to be the first use of the term' surrealiste——'he can be considered a forebear of Surrealism'——求'惊讶'via'unusual verbal associations'；'took part in all the avant-garde movements'；'helped to direct poetry into unexplored channels'；'Chanson du mal-aimé'——失恋英文女子所启；1914入伍、中尉、1916头部重伤；与毕加索/弗拉曼克/德朗/杜菲为友；把卢梭绘画与非洲雕塑引荐给同代"},
{"id":"B404","title":"Colette — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Colette","type":"百科全书","verified":True,"covers":["colette","jiji"],"note":"2026-11-21 核对：全名 Sidonie-Gabrielle Colette；1873-01-28法国Saint-Sauveur-en-Puisaye生—1954-08-03巴黎卒（81岁）；'an outstanding French writer of the first half of the 20th century'；'the pains and pleasures of love'——写'everything that germinates, blossoms, or flies'；Claudine 四部（1900-1903）以夫名 Willy 出版——'Locking her in a room to encourage her to focus on the task at hand, Willy forced her to write'；Chéri（谢利, 1920）——青年与年长女子的私情；La Fin de Chéri (1926)；Le Blé en herbe (1923)；La Vagabonde (1910)；Sido (1930)；Gigi（吉吉, 1944）——被两老姐妹养大成'交际花'的女孩——改编舞台与电影——1958年音乐电影（Maurice Chevalier/Louis Jourdan/Leslie Caron）；'the annalist of female existence'（女性存在的编年史家）；1945入龚古尔学院；'She ended her days, a legendary figure surrounded by her beloved cats'"},
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
{"id":"apollinaire","name":"纪尧姆·阿波利奈尔","foreign_name":"Guillaume Apollinaire（纪尧姆·阿波利奈尔，1880-08-26—1918-11-09）","country":"法国","birth":1880,"death":1918,"birth_year":1880,"death_year":1918,"era":"近代",
"summary":"阿波利奈尔，罗马生（波兰移民之女与意大利军官之子——'he kept his origins secret'），法国诗人——1918年11月9日卒于巴黎，38岁——'Weakened by war wounds, he died of Spanish influenza'（战伤削弱后死于西班牙流感——B403）。Alcools（醇酒集, 1913）——'his poetic masterpiece, always without punctuation'（始终无标点——B403）；Calligrammes（图像诗, 1918）——诗即图像（版式排布）——'dominated by images of war'（B403）。剧《蒂雷西亚的乳房》——'believed to be the first use of the term' surrealist——'he can be considered a forebear of Surrealism'（超现实主义的先祖——B403）。'took part in all the avant-garde movements'、'helped to direct poetry into unexplored channels'（B403）。",
"timeline":[
 {"year":1880,"text":"8月26日生于罗马（B403）。","src":"B403"},
 {"year":1913,"text":"Alcools（醇酒集）——'无标点'杰作（B403）。","src":"B403"},
 {"year":1917,"text":"《蒂雷西亚的乳房》——首用 surrealiste 一词（B403）。","src":"B403"},
 {"year":1918,"text":"Calligrammes（图像诗）；11月9日卒于巴黎（西班牙流感）（B403）。","src":"B403"}],
"major_works":[
 {"work_id":"chunjiuji","note":"1913（B403）"},
 {"work_id":"tuxiangshi","note":"1918（B403：Calligrammes）"},
 {"title":"被杀害的诗人","note":"（B403：Le Poète assassiné (1916)——中译名待核）"}],
"style":["'始终无标点'的诗歌（B403：always without punctuation）。",
 "图像诗：诗即图像（B403：Calligrammes）。",
 "'不同寻常的词语组合'求'惊讶'（B403：unusual verbal associations）。"],
"status":"Britannica 定位阿波利奈尔为超现实主义的先祖、先锋运动的全参与者（B403）。",
"sources":["B403"],"dates_source":"B403",
"pending":["Alcools 通行译名（《醇酒集》/《烧酒集》）待核。","《米拉波桥》未见于 B403（不采其细节）。","'surrealiste'首用说核对（B381口径'believed to be the first use'）。"]},
{"id":"colette","name":"西多妮-加布里埃尔·科莱特","foreign_name":"Sidonie-Gabrielle Colette（西多妮-加布里埃尔·科莱特，1873-01-28—1954-08-03）","country":"法国","birth":1873,"death":1954,"birth_year":1873,"death_year":1954,"era":"近代",
"summary":"科莱特，法国Saint-Sauveur-en-Puisaye生——'an outstanding French writer of the first half of the 20th century'（20世纪上半叶杰出的法国作家——B404）；'the pains and pleasures of love'——写'everything that germinates, blossoms, or flies'（一切'发芽、开花或飞翔'之物——B404）。Claudine 四部（1900-1903）以夫名 Willy 出版——'Locking her in a room..., Willy forced her to write'（B404）。Chéri（谢利, 1920）、Gigi（吉吉, 1944）——改编舞台与电影、1958年音乐电影（B404）。'the annalist of female existence'（女性存在的编年史家——B404）；1945年入龚古尔学院（B404）。",
"timeline":[
 {"year":1873,"text":"1月28日生于法国Saint-Sauveur-en-Puisaye（B404）。","src":"B404"},
 {"year":1900,"text":"Claudine 系列（1900-03）以夫名 Willy 出版（B404）。","src":"B404"},
 {"year":1920,"text":"Chéri（谢利）（B404）。","src":"B404"},
 {"year":1944,"text":"Gigi（吉吉）（B404）。","src":"B404"},
 {"year":1954,"text":"8月3日卒于巴黎（B404）。","src":"B404"}],
"major_works":[
 {"work_id":"jiji","note":"1944（B404）"},
 {"title":"谢利","note":"（B404：Chéri (1920)）"},
 {"title":"青苗","note":"（B404：Le Blé en herbe (1923)——中译名待核）"}],
"style":["'女性存在的编年史家'（B404：the annalist of female existence）。",
 "'爱的痛苦与欢愉'（B404：the pains and pleasures of love）。",
 "'发芽、开花或飞翔'的一切（B404）。"],
"status":"Britannica 定位科莱特为20世纪上半叶杰出法国作家、龚古尔学院成员（B404）。",
"sources":["B404"],"dates_source":"B404",
"pending":["Gigi 通行译名（《吉吉》）待核。","Claudine 四部归属（夫名 Willy——B404口径）细节待核。","1958年电影（米高梅说）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"chunjiuji","title":"醇酒集","original_title":"Alcools","region":"法国","era":"近代","era_detail":"20世纪10年代",
"genre":"诗集","genre_group":"诗歌","language":"法语","author_id":"apollinaire","author_name":"纪尧姆·阿波利奈尔",
"year_display":"1913年（Britannica B403：Alcools (1913)——'his poetic masterpiece, always without punctuation'）","year_sort":1913,
"background":["Britannica（B403）：Alcools——'his poetic masterpiece, always without punctuation'（其诗歌杰作、始终无标点）——混亚历山大体/规则诗节/短无韵行。","Britannica（B403）：阿波利奈尔——'helped to direct poetry into unexplored channels'——'took part in all the avant-garde movements'。","Britannica（B403）：'Chanson du mal-aimé'——失恋英文女子所启（本集内名篇——B403 提及）。"],
"outline":["（通说待核——B403未载篇目）'米拉波桥'等篇（篇目通说待核——B403未载）。","（通说待核）'无标点'的抒情流。"],
"characters":[{"name":"抒情'我'","identity":"现代歌者","note":"（B403 语境）"}],
"themes":["'始终无标点'（B403：always without punctuation）。",
 "古典格律与现代短行的混编（B403：alexandrines...short unrhymed lines）。",
 "'未探之诗路'（B403：unexplored channels）。"],
"influence":[{"text":"Britannica：'his poetic masterpiece'（B403）。","source":"B403"},{"text":"Britannica：'helped to direct poetry into unexplored channels'（B403）。","source":"B403"}],
"reading":{"difficulties":["无标点的语流。","象征主义与立体派的交叉（B403 语境）。"],
 "editions":["《醇酒集》中译名（《烧酒集》）待核。","法文原版（公有领域状态待核）。"],
 "order":"阿波利奈尔首选；后接《图像诗》。"},
"pending":["篇目（《米拉波桥》——B403未载）核对（通说）。","1913年出版细节待核。","中译名两说待核。"],
"sources":["B403"],"year_source":"B403","author_source":"B403","related_works":["diyuzhiji","tuxiangshi" if "tuxiangshi" in existing else "leiyu","balideyouyu"],
"svg":G("《醇酒集》无标点结构图",[{"title":"无标点","text":"'始终无标点'（B403）","color":"gold"},{"title":"醇酒","text":"醉意的诗行（书名）","color":"main"},{"title":"混编","text":"古典与短行（B403）","color":"family"},{"title":"先锋","text":"运动的全参与者（B403）","color":"antagonist"}])},
{"id":"jiji","title":"吉吉","original_title":"Gigi","region":"法国","era":"近代","era_detail":"20世纪40年代",
"genre":"中篇小说","genre_group":"小说","language":"法语","author_id":"colette","author_name":"西多妮-加布里埃尔·科莱特",
"year_display":"1944年（Britannica B404：Gigi (1944)——改编舞台与电影——1958年音乐电影）","year_sort":1944,
"background":["Britannica（B404）：Gigi——girl raised by two elderly sisters to become a courtesan（被两老姐妹养大成'交际花'的女孩）——改编舞台与电影——1958年音乐电影（Maurice Chevalier/Louis Jourdan/Leslie Caron）。","Britannica（B404）：科莱特——'the annalist of female existence'——'the pains and pleasures of love'。","题材（通说待核）：吉吉拒绝'职业'——'我要嫁给他'的颠倒。"],
"outline":["（通说待核——B404未载剧情）吉吉与加斯顿：'规矩'的反叛。","（通说待核）外婆阿莉西娅与姨们的'职业'训练。"],
"characters":[{"name":"吉吉","identity":"少女","note":"（B404 书名人物）"},{"name":"加斯顿","identity":"富商","note":"（通说待核）"}],
"themes":["'交际花'制度与拒绝（通说待核）。",
 "'女性存在的编年史'（B404：the annalist of female existence）。",
 "婚姻 vs '职业'（通说待核）。"],
"influence":[{"text":"Britannica：1958年音乐电影（B404）。","source":"B404"},{"text":"Britannica：'an outstanding French writer of the first half of the 20th century'（B404）。","source":"B404"}],
"reading":{"difficulties":["'美好年代'巴黎背景（通说待核）。","'轻'语体的反抗。"],
 "editions":["《吉吉》中译本（人民文学等——通说待核）。","法文原版。"],
 "order":"科莱特晚期首选；与《谢利》对读。"},
"pending":["吉吉/加斯顿人名核对（通说）。","1944年出版细节待核。","1958年音乐电影核对（B404已载主演）。"],
"sources":["B404"],"year_source":"B404","author_source":"B404","related_works":["difannidezaocan","jueshi","minglichang"],
"svg":G("《吉吉》反叛结构图",[{"title":"吉吉","text":"拒绝'职业'（通说）","color":"main"},{"title":"两姨","text":"'职业'的教练（通说）","color":"antagonist"},{"title":"加斯顿","text":"富商的爱（通说）","color":"gold"},{"title":"婚姻","text":"颠倒的结局（通说）","color":"family"}])},
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

for wid, aid in [('chunjiuji','apollinaire'), ('jiji','colette')]:
    if wid in created:
        link(aid, wid)
print('BATCH75 DONE')
