# -*- coding: utf-8 -*-
"""批52：Britannica 新核梅特林克 B372×2（青鸟/佩利亚斯）+ 零成本4部（叶尔玛/贝尔纳达·阿尔巴的家/萨图拉/在人间）"""
import json, pathlib

newsrc = [
{"id":"B372","title":"Maurice Maeterlinck — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Maurice-Maeterlinck","type":"百科全书","verified":True,"covers":["maeterlinck","qingniao"],"note":"2026-11-21 核对：1862-08-29根特生—1949-05-06尼斯卒（86岁）；1911诺贝尔文学奖；La Princesse Maleine (1889)首剧；L'Intruse 与 Les Aveugles (1890)一幕剧突破；Pelléas et Mélisande (1892)——'the unquestioned masterpiece of Symbolist drama'——'conveys a mood of hopeless melancholy and doom'——启德彪西1902歌剧；Monna Vanna (1902)；L'Oiseau bleu（青鸟, 1908）——'allegorical fantasy conceived as a play for children'——莫斯科艺术剧院1908首演——Tyltyl与Mytyl寻找'Blue Bird of Happiness, only to discover it in their own backyard'；Le Bourgmestre de Stilmonde (1917)；诗 Serres chaudes (1889)、Le Trésor des humbles (1896)、La Vie des abeilles (1901)；影响 Hofmannsthal/叶芝/辛格/奥尼尔——'no Belgian dramatist had greater effect on worldwide audiences'；1932年比利时国王封伯爵"},
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
{"id":"maeterlinck","name":"莫里斯·梅特林克","foreign_name":"Maurice Maeterlinck（莫里斯·梅特林克，1862-08-29—1949-05-06）","country":"比利时","birth":1862,"death":1949,"birth_year":1862,"death_year":1949,"era":"近代",
"summary":"梅特林克，根特生，比利时剧作家——1911年诺贝尔文学奖（B372）。Pelléas et Mélisande（佩利亚斯与梅丽桑德, 1892）——'the unquestioned masterpiece of Symbolist drama'（象征主义戏剧无可争议的杰作——B372）——启德彪西1902年歌剧（B372）。L'Oiseau bleu（青鸟, 1908）——'allegorical fantasy conceived as a play for children'——1908年莫斯科艺术剧院首演——Tyltyl与Mytyl寻找'幸福的青鸟，却发现它就在自家后院'（B372）。影响霍夫曼斯塔尔、叶芝、辛格与奥尼尔——'no Belgian dramatist had greater effect on worldwide audiences'（B372）。",
"timeline":[
 {"year":1862,"text":"8月29日生于根特（B372）。","src":"B372"},
 {"year":1892,"text":"Pelléas et Mélisande——象征主义戏剧杰作（B372）。","src":"B372"},
 {"year":1908,"text":"L'Oiseau bleu——莫斯科艺术剧院首演（B372）。","src":"B372"},
 {"year":1911,"text":"获诺贝尔文学奖（B372）。","src":"B372"},
 {"year":1949,"text":"5月6日卒于尼斯（B372）。","src":"B372"}],
"major_works":[
 {"work_id":"qingniao","note":"1908（B372）"},
 {"work_id":"peiliyasi","note":"1892（B372）"},
 {"title":"蜜蜂的生活","note":"（B372：La Vie des abeilles (1901)）"}],
"style":["象征主义戏剧（B372：Symbolist drama）。",
 "'无可救药的忧郁与厄运'的氛围（B372：hopeless melancholy and doom）。",
 "寓意童话剧（B372：allegorical fantasy）。"],
"status":"Britannica 定位梅特林克为1911诺奖得主、象征主义戏剧宗师、影响世界剧坛的比利时作家（B372）。",
"sources":["B372"],"dates_source":"B372",
"pending":["《青鸟》通行译名核对。","'伯爵'封号（1932——B372）细节待核。","'静止戏剧'（static drama）术语待核（B372未载）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

S_CH, S_LO, S_MO, S_GK = src_of('chikefu'), src_of('lorca'), src_of('montale'), src_of('gorky')
works = [
{"id":"qingniao","title":"青鸟","original_title":"L'Oiseau bleu","region":"比利时","era":"近代","era_detail":"20世纪初",
"genre":"寓意童话剧","genre_group":"戏剧","language":"法语","author_id":"maeterlinck","author_name":"莫里斯·梅特林克",
"year_display":"1908年（Britannica B372：L'Oiseau bleu (1908)——莫斯科艺术剧院首演）","year_sort":1908,
"background":["Britannica（B372）：'allegorical fantasy conceived as a play for children'——为儿童构思的寓意幻想剧。","Britannica（B372）：Tyltyl与Mytyl寻找'Blue Bird of Happiness, only to discover it in their own backyard'——幸福的青鸟就在自家后院。","Britannica（B372）：1908年莫斯科艺术剧院首演。"],
"outline":["（通说待核——B372未载全剧情）兄妹寻找青鸟的历程：记忆之国、夜宫、未来之国。","（通说待核）归家后发现青鸟（就在后院）。"],
"characters":[{"name":"迪迪尔（Tyltyl）","identity":"男孩","note":"（B372：Tyltyl——中译名通说待核）"},{"name":"米迪尔（Mytyl）","identity":"女孩","note":"（B372：Mytyl）"}],
"themes":["'幸福就在身边'（B372：in their own backyard）。",
 "寓意的旅行结构（B372：allegorical fantasy）。",
 "儿童的戏剧（B372：play for children）。"],
"influence":[{"text":"Britannica：莫斯科艺术剧院1908首演（B372）。","source":"B372"},{"text":"Britannica：1911诺奖（B372 交叉）。","source":"B372"}],
"reading":{"difficulties":["寓意的符号系统。","'静'的舞台美学（作者页语境——待核）。"],
 "editions":["《青鸟》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"梅特林克首选；与《佩利亚斯与梅丽桑德》对读。"},
"pending":["迪迪尔/米迪尔通行译名核对。","1908年首演细节待核。","六幕十二场结构核对（通说）。"],
"sources":["B372"],"year_source":"B372","author_source":"B372","related_works":["peiliyasi","haidenvren","xiwang" if "xiwang" in existing else "leiyu"],
"svg":G("《青鸟》寓意旅行图",[{"title":"青鸟","text":"幸福的象征（B372）","color":"gold"},{"title":"兄妹","text":"寻找的旅程（通说）","color":"main"},{"title":"后院","text":"'就在身边'（B372）","color":"family"},{"title":"夜宫","text":"寓意的站台（通说）","color":"antagonist"}])},
{"id":"peiliyasi","title":"佩利亚斯与梅丽桑德","original_title":"Pelléas et Mélisande","region":"比利时","era":"近代","era_detail":"19世纪90年代初",
"genre":"戏剧","genre_group":"戏剧","language":"法语","author_id":"maeterlinck","author_name":"莫里斯·梅特林克",
"year_display":"1892年（Britannica B372：Pelléas et Mélisande (1892)——'the unquestioned masterpiece of Symbolist drama'）","year_sort":1892,
"background":["Britannica（B372）：'the unquestioned masterpiece of Symbolist drama'（象征主义戏剧无可争议的杰作）。","Britannica（B372）：'conveys a mood of hopeless melancholy and doom'——启德彪西1902年歌剧。","题材（通说待核）：海底王国出走的梅丽桑德与两兄弟的爱情——井、发与死亡。"],
"outline":["（通说待核）梅丽桑德与戈洛、佩利亚斯的三角。","（通说待核）'发'的坠落与井底的失落。"],
"characters":[{"name":"梅丽桑德","identity":"神秘少女","note":"（B372 书名人物）"},{"name":"佩利亚斯","identity":"年轻王子","note":"（B372 书名人物）"}],
"themes":["'绝望的忧郁与厄运'（B372：hopeless melancholy and doom）。",
 "象征主义戏剧的杰作（B372）。",
 "静默与暗示（作者页语境——待核）。"],
"influence":[{"text":"Britannica：德彪西歌剧（1902）（B372）。","source":"B372"},{"text":"Britannica：影响叶芝、辛格、奥尼尔（B372 作者级）。","source":"B372"}],
"reading":{"difficulties":["象征主义的'潜文本'。","与德彪西歌剧的对读。"],
 "editions":["《佩利亚斯与梅丽桑德》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"梅特林克戏剧巅峰；与《青鸟》对读。"},
"pending":["剧情细节核对（通说）。","1892年出版/首演细节待核。","德彪西歌剧1902年首演核对。"],
"sources":["B372"],"year_source":"B372","author_source":"B372","related_works":["qingniao","xuboliweng","dengdaigou"],
"svg":G("《佩利亚斯与梅丽桑德》象征结构图",[{"title":"梅丽桑德","text":"厄运的化身（B372语境）","color":"main"},{"title":"发","text":"坠落的信物（通说）","color":"gold"},{"title":"井","text":"失落的深处（通说）","color":"family"},{"title":"象征","text":"戏剧的巅峰（B372）","color":"antagonist"}])},
# 零成本
{"id":"yeerma","title":"叶尔玛","original_title":"Yerma","region":"西班牙","era":"近代","era_detail":"20世纪30年代",
"genre":"悲剧","genre_group":"戏剧","language":"西班牙语","author_id":"lorca","author_name":"费德里科·加西亚·洛尔卡",
"year_display":"1934年（Britannica B355：Yerma (1934)）","year_sort":1934,
"background":["Britannica（B355）：Yerma (1934)——洛尔卡民间悲剧三部曲之一。","Britannica（B355）：洛尔卡——'the most important Spanish poet and playwright of the 20th century'。","题材（通说待核）：'叶尔玛'（ barren 之意）——无嗣农妇的绝望与弑夫。"],
"outline":["（通说待核）叶尔玛求子的岁月与牧场之夜。","（通说待核）'荒芜'的命名与终局的暴力。"],
"characters":[{"name":"叶尔玛","identity":"农妇","note":"（B355 书名人物）"},{"name":"胡安","identity":"丈夫","note":"（通说待核）"}],
"themes":["'荒芜'与生育（书名语境——通说待核）。",
 "农村悲剧三部曲之二（B355 三部曲语境）。",
 "女性的身体与土地（通说待核）。"],
"influence":[{"text":"Britannica：民间悲剧三部曲（B355）。","source":"B355"},{"text":"Britannica：西班牙戏剧'second Golden Age'（B355 交叉）。","source":"B355"}],
"reading":{"difficulties":["安达卢西亚农事意象。","'Yerma'词义（荒芜）。"],
 "editions":["《叶尔玛》中译本（人民文学等——通说待核）。","西班牙文原版。"],
 "order":"三部曲之二；与《血婚》《阿尔巴之家》连读。"},
"pending":["胡安人名核对（通说）。","1934年首演细节待核。","'荒芜'词义核对。"],
"sources":["B355"],"year_source":"B355","author_source":"B355","related_works":["xuehun","jipusaiyaoqu","leiyu"],
"svg":G("《叶尔玛》荒芜结构图",[{"title":"叶尔玛","text":"'荒芜'之名（书名）","color":"main"},{"title":"求子","text":"岁月的空转（通说）","color":"gold"},{"title":"牧场","text":"夜的暴力（通说）","color":"antagonist"},{"title":"土地","text":"女性的荒芜（通说）","color":"family"}])},
{"id":"beernadajia","title":"贝尔纳达·阿尔巴的家","original_title":"La casa de Bernarda Alba","region":"西班牙","era":"近代","era_detail":"20世纪30年代",
"genre":"悲剧","genre_group":"戏剧","language":"西班牙语","author_id":"lorca","author_name":"费德里科·加西亚·洛尔卡",
"year_display":"1936年（Britannica B355：La casa de Bernarda Alba (1936)）","year_sort":1936,
"background":["Britannica（B355）：La casa de Bernarda Alba (1936)——民间悲剧三部曲之三（作者卒年作品）。","Britannica（B355）：洛尔卡1936年8月被杀（作者页交叉）。","题材（通说待核）：寡母贝尔纳达的'八年守丧'——五个女儿的锁闭与反抗。"],
"outline":["（通说待核）丧服中的五姐妹与求婚者佩贝。","（通说待核）'白色的墙'：压抑的房子与最后一声枪响。"],
"characters":[{"name":"贝尔纳达·阿尔巴","identity":"寡母","note":"（B355 书名人物）"},{"name":"阿德莉亚","identity":"最幼女儿","note":"（通说待核）"}],
"themes":["'守丧'与压制（通说待核）。",
 "全女性剧（通说待核）。",
 "'纯洁'的暴政（通说待核）。"],
"influence":[{"text":"Britannica：民间悲剧三部曲之三（B355）。","source":"B355"},{"text":"Britannica：1936年被杀——未及见其上演（交叉——待核）。","source":"B355"}],
"reading":{"difficulties":["全女班的舞台。","安达卢西亚的荣誉制。"],
 "editions":["《贝尔纳达·阿尔巴的家》中译名（《阿尔巴家的女人们》两说——通说待核）。","西班牙文原版。"],
 "order":"三部曲之三；洛尔卡戏剧收官。"},
"pending":["阿德莉亚/佩贝人名核对（通说）。","1936年写作、1945年首演说待核。","'八年'守丧细节待核。"],
"sources":["B355"],"year_source":"B355","author_source":"B355","related_works":["xuehun","yeerma","yuwanghaojieche"],
"svg":G("《阿尔巴之家》压抑结构图",[{"title":"贝尔纳达","text":"'守丧'的暴政（通说）","color":"antagonist"},{"title":"五姐妹","text":"锁闭的青春（通说）","color":"main"},{"title":"白墙","text":"压抑的房子（通说）","color":"gold"},{"title":"枪声","text":"终局的爆发（通说）","color":"family"}])},
{"id":"satula","title":"萨图拉","original_title":"Satura","region":"意大利","era":"近代","era_detail":"20世纪60年代",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"montale","author_name":"埃乌杰尼奥·蒙塔莱",
"year_display":"1962年（Britannica B341：Satura (1962)）","year_sort":1962,
"background":["Britannica（B341）：Satura (1962)——蒙塔莱晚期诗集。","Britannica（B341）：蒙塔莱——1975诺奖；'progressively more introverted and obscure'。","题材（通说待核）：'萨图拉'（拉丁语'混合祭品'说——通说待核）：悼亡妻与自嘲。"],
"outline":["（通说待核）悼亡妻莫塞利的诗（与Xenia 1966并读——B341交叉）。","（通说待核）'拉丁语satura'的词源：混合的祭品。"],
"characters":[{"name":"抒情'我'","identity":"晚期的隐逸诗人","note":"（B341 语系）"}],
"themes":["悼亡与自嘲（通说待核）。",
 "'拉丁'词源的诗学（书名语境——通说待核）。",
 "'更内省'（B341：more introverted）。"],
"influence":[{"text":"Britannica：Satura (1962)（B341）。","source":"B341"},{"text":"Britannica：1975诺奖（B341 交叉）。","source":"B341"}],
"reading":{"difficulties":["晚期语体的'闲谈'化（通说待核）。","拉丁词源。"],
 "editions":["《萨图拉》中译名待核。","意大利文原版。"],
 "order":"蒙塔莱晚期；与《境遇》对读。"},
"pending":["'satura'词源说核对（通说）。","1962年出版细节待核。","悼亡诗篇目待核。"],
"sources":["B341"],"year_source":"B341","author_source":"B341","related_works":["wuguigu","jingyu","shunxijiandeyewan"],
"svg":G("《萨图拉》晚期结构图",[{"title":"萨图拉","text":"'混合祭品'（书名）","color":"gold"},{"title":"悼亡","text":"亡妻的缺席（通说）","color":"main"},{"title":"自嘲","text":"晚期的反讽（通说）","color":"antagonist"},{"title":"拉丁","text":"词源的诗学（通说）","color":"family"}])},
{"id":"zaihuang","title":"在人间","original_title":"В людях","region":"俄国","era":"近代","era_detail":"20世纪10年代",
"genre":"自传小说","genre_group":"小说","language":"俄语","author_id":"gorky","author_name":"马克西姆·高尔基",
"year_display":"作者页注记：Britannica——自传三部曲（年份通说待核——1916说）","year_sort":1916,
"background":["作者页注记：童年/在人间/我的大学——'自传三部曲（Britannica：one of the finest autobiographies in Russian literature）'。","Britannica：高尔基——俄国作家（作者页语境）。","题材（通说待核）：阿列克谢的'人间'学徒岁月：鞋店、绘图的作坊与轮船。"],
"outline":["（通说待核）'人间'：伏尔加河上的洗碗工与画坊学徒。","（通说待核）'大学'之前的'社会大学'。"],
"characters":[{"name":"阿列克谢","identity":"少年学徒","note":"（通说待核）"},{"name":"厨师（'司炉'说）","identity":"书籍的引路人","note":"（通说待核）"}],
"themes":["'社会大学'的学徒（书名语境——通说待核）。",
 "自传三部曲之二（B注记）。",
 "书籍的救赎（通说待核）。"],
"influence":[{"text":"Britannica：'one of the finest autobiographies in Russian literature'（作者页注记）。","source":S_GK},{"text":"Britannica：三部曲（作者页注记）。","source":S_GK}],
"reading":{"difficulties":["三部曲的顺序。","19世纪末俄国的底层行业。"],
 "editions":["《在人间》中译本（人民文学等——通说待核）。","俄文原版（公有领域状态待核）。"],
 "order":"三部曲之二；承接《童年》。"},
"pending":["1916年出版细节待核。","'社会大学'说法待核。","人物名核对（通说）。"],
"sources":[S_GK],"year_source":S_GK,"author_source":S_GK,"related_works":["tongnian","zaidiceng","muqin"],
"svg":G("《在人间》学徒结构图",[{"title":"人间","text":"社会的大学（书名）","color":"main"},{"title":"轮船","text":"伏尔加的劳动（通说）","color":"gold"},{"title":"书籍","text":"暗夜的救赎（通说）","color":"family"},{"title":"三部曲","text":"B注记的定位","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（批52）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('qingniao','maeterlinck','青鸟'),('peiliyasi','maeterlinck','佩利亚斯'),('yeerma','lorca','叶尔玛'),('beernadajia','lorca','贝尔纳达'),('satula','montale','萨图拉'),('zaihuang','gorky','在人间')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH52 DONE')
