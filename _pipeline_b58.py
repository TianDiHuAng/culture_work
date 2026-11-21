# -*- coding: utf-8 -*-
"""批58：Britannica 新核帕韦泽 B374×2（月亮与篝火/生活的职业）"""
import json, pathlib

newsrc = [
{"id":"B374","title":"Cesare Pavese — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Cesare-Pavese","type":"百科全书","verified":True,"covers":["pavese","yueliangyuhuoyan"],"note":"2026-11-21 核对：1908-09-09意大利Santo Stefano Belbo生—1950-08-27都灵卒（41岁，自杀——'Shortly after receiving the Strega Prize for it, Pavese committed suicide in a hotel room.'）；La luna e i falò（月亮与篝火, 1950）——'a bleak, yet compassionate story of a hero who tries to find himself by visiting the place in which he grew up'——'the novel considered his best'；Einaudi出版社创始人之一与终身编辑；主编反法西斯评论 La Cultura；1935年因反法西斯入狱；1943-45与游击队同驻皮埃蒙特；译斯坦贝克/海明威/福克纳/梅尔维尔（含《白鲸》）；Lavorare stanca (1936)——首部抒情诗集（1935出狱后）；Paesi tuoi (1941)——首部中篇；Il compagno (1947)；La bella estate (1949)——斯特雷加奖；Dialoghi con Leucò (1947)；Il mestiere di vivere, diario 1935-1950 (1952)——日记；Verrà la morte e avrà i tuoi occhi (1951)——身后情诗；1957年设 Pavese Prize"},
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
{"id":"pavese","name":"切萨雷·帕韦泽","foreign_name":"Cesare Pavese（切萨雷·帕韦泽，1908-09-09—1950-08-27）","country":"意大利","birth":1908,"death":1950,"birth_year":1908,"death_year":1950,"era":"近代",
"summary":"帕韦泽，意大利Santo Stefano Belbo生，小说家、诗人、翻译家——Einaudi出版社创始人之一与终身编辑（B374）。La luna e i falò（月亮与篝火, 1950）——'a bleak, yet compassionate story of a hero who tries to find himself by visiting the place in which he grew up'——'the novel considered his best'（B374）。1935年因反法西斯入狱；1943-45年与游击队同驻皮埃蒙特（B374）；译斯坦贝克、海明威、福克纳、梅尔维尔（含《白鲸》）（B374）。获斯特雷加奖后不久——1950年8月27日在旅馆房间自杀（B374）。",
"timeline":[
 {"year":1908,"text":"9月9日生于Santo Stefano Belbo（B374）。","src":"B374"},
 {"year":1935,"text":"因反法西斯活动入狱（B374）。","src":"B374"},
 {"year":1943,"text":"与游击队同驻皮埃蒙特（1943-45）（B374）。","src":"B374"},
 {"year":1950,"text":"《月亮与篝火》出版；获斯特雷加奖后不久自杀（B374）。","src":"B374"}],
"major_works":[
 {"work_id":"yueliangyuhuoyan","note":"1950（B374）"},
 {"title":"生活的职业","note":"（B374：Il mestiere di vivere (1952)——日记 1935-50）"},
 {"title":"艰难之活","note":"（B374：Lavorare stanca (1936)——首部诗集——中译名待核）"}],
"style":["'苍凉而悲悯'的乡愁叙事（B374：bleak, yet compassionate）。",
 "新现实主义与神话的对位（通说待核）。",
 "翻译家的美语化文体（B374：翻译史清单）。"],
"status":"Britannica 定位帕韦泽为 Einaudi 奠基编辑、《月亮与篝火》为其最佳（B374）。",
"sources":["B374"],"dates_source":"B374",
"pending":["'斯特雷加奖'（La bella estate 1949——B374）细节待核。","自杀细节（旅馆房间——B374）口径待核。","《月亮与篝火》通行译名待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"yueliangyuhuoyan","title":"月亮与篝火","original_title":"La luna e i falò","region":"意大利","era":"近代","era_detail":"20世纪50年代初",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"pavese","author_name":"切萨雷·帕韦泽",
"year_display":"1950年（Britannica B374：La luna e i falò (1950)——'the novel considered his best'）","year_sort":1950,
"background":["Britannica（B374）：'a bleak, yet compassionate story of a hero who tries to find himself by visiting the place in which he grew up'——主角重返生长之地寻找自己。","Britannica（B374）：'the novel considered his best'（被认为其最佳）。","Britannica（B374）：帕韦泽——1943-45与游击队同驻皮埃蒙特——本作的'返乡'背景。"],
"outline":["（通说待核）'鳗鱼'回到山谷：寻找'自己生长的地方'（B374：visiting the place in which he grew up）。","（通说待核）法西斯岁月的毁灭与乡愁的幻灭。"],
"characters":[{"name":"'鳗鱼'","identity":"归乡者","note":"（通说待核，B374未载人名）"},{"name":"尼托","identity":"旧友","note":"（通说待核）"}],
"themes":["'还乡'的幻灭（B374：bleak, yet compassionate）。",
 "战争对乡村的摧毁（通说待核）。",
 "'山谷'的神话化（通说待核）。"],
"influence":[{"text":"Britannica：'the novel considered his best'（B374）。","source":"B374"},{"text":"Britannica：帕韦泽的游击队经历（B374 交叉）。","source":"B374"}],
"reading":{"difficulties":["'鳗鱼'的绰号叙事。","朗格山谷的地理（通说待核）。"],
 "editions":["《月亮与篝火》中译本（人民文学等——通说待核）。","意大利文原版。"],
 "order":"帕韦泽首选；与《生活的职业》对读。"},
"pending":["'鳗鱼'/尼托人名核对（通说）。","1950年出版（Einaudi说）待核。","'山谷'地名细节待核。"],
"sources":["B374"],"year_source":"B374","author_source":"B374","related_works":["bao","lengmoederen","nongmin"],
"svg":G("《月亮与篝火》还乡结构图",[{"title":"还乡","text":"'寻找自己'（B374）","color":"main"},{"title":"山谷","text":"生长的地方（B374）","color":"gold"},{"title":"战争","text":"毁灭的岁月（通说）","color":"antagonist"},{"title":"篝火","text":"焚烧的乡愁（书名意象）","color":"family"}])},
{"id":"shenghuodezhiye","title":"生活的职业","original_title":"Il mestiere di vivere","region":"意大利","era":"近代","era_detail":"20世纪30-50年代",
"genre":"日记","genre_group":"散文","language":"意大利语","author_id":"pavese","author_name":"切萨雷·帕韦泽",
"year_display":"1952年（Britannica B374：Il mestiere di vivere, diario 1935-1950 (1952)——日记）","year_sort":1952,
"background":["Britannica（B374）：Il mestiere di vivere, diario 1935-1950 (1952)——1935-1950年的日记。","Britannica（B374）：帕韦泽——1950年自杀——日记为其内心档案。","题材（通说待核）：'生活的职业'——写作、政治与绝望的日课。"],
"outline":["（通说待核）十五年的日记：从狱中到自杀前夜。","（通说待核）'著名的句子'（不采为引文——细节通说待核）。"],
"characters":[{"name":"帕韦泽","identity":"日记者","note":"（B374 语境）"}],
"themes":["'生活的职业'（书名语境——通说待核）。",
 "写作与政治的自省（B374 语境）。",
 "绝望的日课（通说待核）。"],
"influence":[{"text":"Britannica：Il mestiere di vivere (1952)（B374）。","source":"B374"},{"text":"Britannica：1950年自杀（B374 交叉）。","source":"B374"}],
"reading":{"difficulties":["日记的碎片性。","'句子'与生活的互文。"],
 "editions":["《生活的职业》中译本（人民文学等——通说待核）。","意大利文原版。"],
 "order":"帕韦泽内心档案；与《月亮与篝火》对读。"},
"pending":["日记起讫（1935-1950——B374）核对。","1952年出版（Einaudi说）待核。","'著名句子'细节待核（不采为引文）。"],
"sources":["B374"],"year_source":"B374","author_source":"B374","related_works":["yueliangyuhuoyan","zenodeyishi","lu"],
"svg":G("《生活的职业》日记结构图",[{"title":"日记","text":"十五年的日课（B374）","color":"main"},{"title":"职业","text":"'生活'的技艺（书名）","color":"gold"},{"title":"绝望","text":"自杀前夜（B374交叉）","color":"antagonist"},{"title":"写作","text":"内心的档案（通说）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B374 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('yueliangyuhuoyan','pavese'), ('shenghuodezhiye','pavese')]:
    if wid in created:
        link(aid, wid)
print('BATCH58 DONE')
