# -*- coding: utf-8 -*-
"""批81：Britannica 新核 2 作家 2 部（马拉美 B412 骰子一掷/魏尔伦 B413 无词的浪漫曲）"""
import json, pathlib

newsrc = [
{"id":"B412","title":"Stephane Mallarme — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Stephane-Mallarme","type":"百科全书","verified":True,"covers":["mallarme","touziyizhi"],"note":"2026-11-21 核对：1842-03-18巴黎生—1898-09-09法国Valvins卒（56岁）；L'Après-midi d'un faune（牧神午后）——1865年起写——'inspired Claude Debussy to compose his celebrated Prélude a quarter of a century later'（启德彪西《牧神午后前奏曲》）；Hérodiade——1864年起写；周二沙龙——'A series of celebrated Tuesday evening meetings at his tiny flat in Paris were attended by well-known writers, painters, and musicians of the time'；1868年断言虚无中'lie the essences of perfect forms'——诗人成为'a veritable God, creating something from nothing'——求'l'absente de tous bouquets'（一切花束中缺席的花）；Grand Oeuvre / Le Livre（大作品/书）——从未完成（唯预备笔记存）；Un Coup de dés jamais n'abolira le hasard（骰子一掷永不取消偶然, 1897）；Divagations (1897)；Sonnets to Méry Laurent (1884-90)"},
{"id":"B413","title":"Paul Verlaine — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Verlaine-Paul","type":"百科全书","verified":True,"covers":["verlaine","wucidelangmanqu"],"note":"2026-11-21 核对：1844-03-30梅斯生—1896-01-08巴黎卒（51岁，'Eugénie Krantz's lodgings'）；'first associated with the Parnassians and later known as a leader of the Symbolists'——与马拉美、波德莱尔构成'the so-called Decadents'；Poèmes saturniens（忧郁诗篇, 1866）——首卷——'virtuoso imitations of Baudelaire and Leconte de Lisle'+表妹 Élisa 资助出版；Romances sans paroles（无词的浪漫曲, 1874）——部分写于伦敦——开篇几页'attain a pure musicality rarely surpassed in French literature'（法国文学中罕有的纯净音乐性）——主题多为风景、悔恨或对分居妻子的攻击；1873-07-10布鲁塞尔左轮枪伤兰波——Mons 监两年——1874夏'sincere return to Roman Catholicism'；La Bonne Chanson——订婚诗（1870年8月娶 Mathilde Mauté——'his long hoped-for saviour from erring ways'）；1872年7月弃妻与幼子 Georges；Sagesse (1880年10月——诗多作于1873-78)；'Art poétique'——1882年被青年象征派采纳（约1874年狱中作）；1886年助刊兰波《彩画集》；'rhyme...seemed to him an unavoidable necessity in French verse'"},
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
{"id":"mallarme","name":"斯特凡·马拉美","foreign_name":"Stéphane Mallarmé（斯特凡·马拉美，1842-03-18—1898-09-09）","country":"法国","birth":1842,"death":1898,"birth_year":1842,"death_year":1898,"era":"近代",
"summary":"马拉美，巴黎生，法国诗人——1898年卒于 Valvins，56岁（B412）。L'Après-midi d'un faune（牧神午后）——1865年起写——'inspired Claude Debussy to compose his celebrated Prélude a quarter of a century later'（B412）。Hérodiade——1864年起写（B412）。周二沙龙——'A series of celebrated Tuesday evening meetings at his tiny flat in Paris were attended by well-known writers, painters, and musicians of the time'（B412）。1868年断言虚无中'lie the essences of perfect forms'——诗人成为'a veritable God, creating something from nothing'——求'l'absente de tous bouquets'（B412）。Un Coup de dés（骰子一掷, 1897）；Grand Oeuvre / Le Livre——从未完成（B412）。",
"timeline":[
 {"year":1842,"text":"3月18日生于巴黎（B412）。","src":"B412"},
 {"year":1864,"text":"Hérodiade 起笔（B412）。","src":"B412"},
 {"year":1865,"text":"L'Après-midi d'un faune 起笔（B412）。","src":"B412"},
 {"year":1897,"text":"Un Coup de dés（骰子一掷）与 Divagations（B412）。","src":"B412"},
 {"year":1898,"text":"9月9日卒于 Valvins（B412）。","src":"B412"}],
"major_works":[
 {"work_id":"touziyizhi","note":"1897（B412）"},
 {"title":"牧神午后","note":"（B412：L'Après-midi d'un faune——启德彪西前奏曲）"},
 {"title":"希罗底亚德","note":"（B412：Hérodiade——中译名待核）"}],
"style":["'虚无中的完美形式'（B412：essences of perfect forms）。",
 "'创造无中生有'的诗人-神（B412：a veritable God）。",
 "'一切花束中缺席的花'（B412：l'absente de tous bouquets）。"],
"status":"Britannica 定位马拉美为象征派的'纯诗'宗师、周二沙龙的主人（B412）。",
"sources":["B412"],"dates_source":"B412",
"pending":["《骰子一掷》通行译名（《骰子一掷永远取消不了偶然》）待核。","'大作品/书'（Grand Oeuvre/Le Livre）细节待核（B412：never completed）。","周二沙龙成员清单待核。"]},
{"id":"verlaine","name":"保尔·魏尔伦","foreign_name":"Paul Verlaine（保尔·魏尔伦，1844-03-30—1896-01-08）","country":"法国","birth":1844,"death":1896,"birth_year":1844,"death_year":1896,"era":"近代",
"summary":"魏尔伦，梅斯生，法国诗人——'first associated with the Parnassians and later known as a leader of the Symbolists'（帕尔纳斯派出身、象征派领袖——B413）——与马拉美、波德莱尔构成'the so-called Decadents'（B413）。Poèmes saturniens（忧郁诗篇, 1866）——首卷——'virtuoso imitations of Baudelaire and Leconte de Lisle'（B413）。Romances sans paroles（无词的浪漫曲, 1874）——部分写于伦敦——开篇几页'attain a pure musicality rarely surpassed in French literature'（B413）。1873年7月10日在布鲁塞尔左轮枪伤兰波——Mons 监两年——1874夏'sincere return to Roman Catholicism'（B413）。'Art poétique'——1882年被青年象征派采纳（B413）。",
"timeline":[
 {"year":1844,"text":"3月30日生于梅斯（B413）。","src":"B413"},
 {"year":1866,"text":"Poèmes saturniens——首卷（B413）。","src":"B413"},
 {"year":1873,"text":"7月10日枪伤兰波——Mons 监两年（B413）。","src":"B413"},
 {"year":1874,"text":"Romances sans paroles——'纯净音乐性'（B413）。","src":"B413"},
 {"year":1896,"text":"1月8日卒于巴黎（B413）。","src":"B413"}],
"major_works":[
 {"work_id":"wucidelangmanqu","note":"1874（B413）"},
 {"title":"忧郁诗篇","note":"（B413：Poèmes saturniens (1866)——中译名待核）"},
 {"title":"智慧集","note":"（B413：Sagesse (1880)——中译名待核）"}],
"style":["象征派领袖（B413：a leader of the Symbolists）。",
 "'法国文学中罕有的纯净音乐性'（B413：pure musicality rarely surpassed）。",
 "'韵是法语诗不可避免的必需'（B413：rhyme...unavoidable necessity）。"],
"status":"Britannica 定位魏尔伦为象征派领袖、'颓废者'之一、现代'词音乐'的开启者（B413 搜索口径——initiator of modern word-music）。",
"sources":["B413"],"dates_source":"B413",
"pending":["《无词的浪漫曲》通行译名（《无言的浪漫曲》）待核。","枪伤兰波细节（B413已载1873-07-10）核对。","'Art poétique'通行译名（《诗艺》）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"touziyizhi","title":"骰子一掷","original_title":"Un Coup de dés jamais n'abolira le hasard","region":"法国","era":"近代","era_detail":"19世纪90年代",
"genre":"长诗（视觉诗）","genre_group":"诗歌","language":"法语","author_id":"mallarme","author_name":"斯特凡·马拉美",
"year_display":"1897年（Britannica B412：Un Coup de dés jamais n'abolira le hasard (1897)）","year_sort":1897,
"background":["Britannica（B412）：Un Coup de dés jamais n'abolira le hasard（骰子一掷永不取消偶然）——1897年。","Britannica（B412）：马拉美——'虚无中的完美形式'——诗人'a veritable God, creating something from nothing'；Grand Oeuvre / Le Livre——从未完成。","题材（通说待核）：版式'排布'的诗——'骰子一掷'与'偶然'的海。"],
"outline":["（通说待核——B412未载诗节）'骰子一掷永不取消偶然'的版式实验。","（通说待核）'船'与'深渊'的意象。"],
"characters":[{"name":"版式之'我'","identity":"实验诗人","note":"（B412 语境）"}],
"themes":["'偶然'与'必然'（书名语境——通说待核）。",
 "版式：诗即图像（先于 Calligrammes 的实验——通说待核）。",
 "'书'的未完成（B412：Grand Oeuvre / Le Livre）。"],
"influence":[{"text":"Britannica：Un Coup de dés (1897)（B412）。","source":"B412"},{"text":"Britannica：'Grand Oeuvre / Le Livre never completed'（B412）。","source":"B412"}],
"reading":{"difficulties":["版式的读法（页面的'空白'）。","'偶然'的哲学。"],
 "editions":["《骰子一掷》中译名（《骰子一掷永远取消不了偶然》）待核。","法文原版（公有领域状态待核）。"],
 "order":"马拉美收官之作；与《牧神午后》对读。"},
"pending":["版式细节核对（双页跨页说——通说）。","1897年发表（Cosmopolis说）待核。","'船'意象细节待核。"],
"sources":["B412"],"year_source":"B412","author_source":"B412","related_works":["chunjiuji","tianzhenyujiy","wucidelangmanqu"],
"svg":G("《骰子一掷》版式结构图",[{"title":"骰子","text":"'一掷'的偶然（书名）","color":"gold"},{"title":"版式","text":"诗即图像（通说）","color":"main"},{"title":"虚无","text":"'完美形式'（B412）","color":"antagonist"},{"title":"书","text":"未完成的 Grand Oeuvre（B412）","color":"family"}])},
{"id":"wucidelangmanqu","title":"无词的浪漫曲","original_title":"Romances sans paroles","region":"法国","era":"近代","era_detail":"19世纪70年代",
"genre":"诗集","genre_group":"诗歌","language":"法语","author_id":"verlaine","author_name":"保尔·魏尔伦",
"year_display":"1874年（Britannica B413：Romances sans paroles (1874)——部分写于伦敦——'attain a pure musicality rarely surpassed in French literature'）","year_sort":1874,
"background":["Britannica（B413）：Romances sans paroles——部分写于伦敦——开篇几页'attain a pure musicality rarely surpassed in French literature'（法国文学中罕有的纯净音乐性）——主题多为风景、悔恨或对分居妻子的攻击。","Britannica（B413）：魏尔伦——'a leader of the Symbolists'——与马拉美、波德莱尔构成'the so-called Decadents'。","Britannica（B413）：1873年7月10日枪伤兰波——Mons 监两年——1874夏'信仰回归'。"],
"outline":["（通说待核——B413未载篇目）'月光'《andelier》? ——（篇名通说待核：《月光》《泪落在我心》说待核）。","（通说待核）'罗曼司'：风景、悔恨与流亡的伦敦。"],
"characters":[{"name":"抒情'我'","identity":"流亡的歌者","note":"（B413 语境）"}],
"themes":["'纯净音乐性'（B413：pure musicality rarely surpassed）。",
 "风景、悔恨与婚姻的攻击（B413：subjects were mostly landscape, regret...）。",
 "'无词'：音乐先于语义（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：'a leader of the Symbolists'（B413）。","source":"B413"},{"text":"Britannica：'attain a pure musicality rarely surpassed in French literature'（B413）。","source":"B413"}],
"reading":{"difficulties":["'音乐先于意义'的读法。","1872-73的流亡伦敦背景（B413：partly written in London）。"],
 "editions":["《无词的浪漫曲》中译名（《无言的情歌》）待核。","法文原版（公有领域）。"],
 "order":"魏尔伦代表作；与《忧郁诗篇》对读。"},
"pending":["篇目（《月光》《泪落在我心》说——通说）核对。","1874年出版（London说）待核。","'音乐性'评价核对（B413已载）。"],
"sources":["B413"],"year_source":"B413","author_source":"B413","related_works":["wucidelangmanqu" if False else "leiyu","diyuzhiji","songge1819"],
"svg":G("《无词的浪漫曲》音乐结构图",[{"title":"无词","text":"音乐先于语义（书名）","color":"gold"},{"title":"纯净音乐性","text":"'罕有的'（B413）","color":"main"},{"title":"伦敦","text":"流亡的风景（B413）","color":"family"},{"title":"悔恨","text":"对妻的攻击（B413）","color":"antagonist"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B41x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('touziyizhi','mallarme'), ('wucidelangmanqu','verlaine')]:
    if wid in created:
        link(aid, wid)
print('BATCH81 DONE')
