# -*- coding: utf-8 -*-
"""流水线批次17：象征主义与白银时代 4 部 + 4 作家页 + 4 来源"""
import json, pathlib

new_src = [
{"id":"B309","title":"Charles Baudelaire — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Charles-Baudelaire","type":"百科全书","verified":True,"covers":["baudelaire","ezhihua"],"note":"2026-11-21 核对：1821-04-09巴黎生—1867-08-31巴黎卒（46岁）；Les Fleurs du mal (1857)——'perhaps the most important and influential poetry collection published in Europe in the 19th century'；'In 1857, authorities charged thirteen poems from this collection with offenses against religion and public morality'——'six poems were censored due to obscenity, leading to a fine'；'The collection consists of poems arranged into six sections'；'correspondances'——Symbolist leaders'regarded themselves as his followers'；Petits poèmes en prose (1868)——'the most successful and innovative early experiment in prose poetry of the time'；Les Fleurs du mal——'the fullest expression of French Romantic poetry'"},
{"id":"B310","title":"Arthur Rimbaud — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Arthur-Rimbaud","type":"百科全书","verified":True,"covers":["rimbaud","diyuzhiji"],"note":"2026-11-21 核对：1854-10-20 Charleville生—1891-11-10马赛卒（37岁）；Une Saison en enfer (1873)——'Consisting of nine fragments of prose and verse'——examining 'Rimbauds search for experience and his relationship with Verlaine'；Illuminations——'A collection of 40 prose poems and two free-verse poems, believed to have been written between 1872 and 1874'；'Many 20th-century poets were influenced by the Dionysian power of his verse and his liberation of language from the constraints of form'；'one of the first modern poets to shatter the constraints of traditional metric forms'；'a founding father of modernism'（Legacy 语境）"},
{"id":"B311","title":"Marina Ivanovna Tsvetayeva — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Marina-Ivanovna-Tsvetayeva","type":"百科全书","verified":True,"covers":["tsvetaeva","cweitayeva"],"note":"2026-11-21 核对：1892-10-08（儒历9-26）莫斯科生—1941-08-31 Yelabuga卒（48岁，自杀）；'regarded as one of the finest Russian-language poets of the 20th century'；'distinctive for its staccato rhythms, originality, and directness'；主要作品：Vecherny albom (1910)、Lebediny stan（1917—21写/1957慕尼黑出版）、Posle Rossii (1928)、Moy Pushkin (1937)、Stikhi k Chekhii (1938–39)；'She committed suicide in 1941'"},
{"id":"B312","title":"Osip Emilyevich Mandelshtam — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Osip-Emilyevich-Mandelshtam","type":"百科全书","verified":True,"covers":["mandelshtam","shitou"],"note":"2026-11-21 核对：1891-01-03（儒历1-15）华沙生—1938-12-27海参崴附近Vtoraya Rechka中转营卒；Acmeism——'rejected the vague mysticism of Russian Symbolism and demanded clarity and concreteness'；Kamen (Stone, 1913)——父亲出资出版首部诗集；题目象征阿克梅派'identification with the cultural essence of St. Petersburg'；1934年5月3日因讽刺诗被捕——'Sentenced to five years in a labour camp for anti-Soviet activity'，卒于中转营"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new_src:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
raw = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for s in raw:
    seen[s["id"]] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources:", len(out))

authors = {
"baudelaire": {
  "id": "baudelaire", "name": "夏尔·波德莱尔", "foreign_name": "Charles Baudelaire（夏尔·波德莱尔，1821-04-09—1867-08-31）",
  "country": "法国", "birth": 1821, "death": 1867, "birth_year": 1821, "death_year": 1867, "era": "近代",
  "summary": "波德莱尔，巴黎生，法国诗人、翻译家与艺术批评家——'whose reputation rests primarily on Les Fleurs du mal (1857; The Flowers of Evil) and Petits poèmes en prose (1868)'（声誉主要基于《恶之花》与《散文诗》——B309）。'perhaps the most important and influential poetry collection published in Europe in the 19th century'（《恶之花》为19世纪欧洲最重要的诗集——B309）。象征主义领袖'regarded themselves as his followers'（视自己为其追随者——B309）。",
  "timeline": [
    {"year": 1821, "text": "4月9日生于巴黎（B309：Born April 9, 1821, Paris）。", "src": "B309"},
    {"year": 1857, "text": "《恶之花》出版（B309：Les Fleurs du mal (1857)）——13首被控冒犯宗教与公德、6首被删并罚款（B309）。", "src": "B309"},
    {"year": 1868, "text": "《散文诗》（Petits poèmes en prose）身后出版（B309：1868）。", "src": "B309"},
    {"year": 1867, "text": "8月31日卒于巴黎（B309：Died August 31, 1867, Paris，46岁）。", "src": "B309"}],
  "major_works": [
    {"work_id": "ezhihua", "note": "诗集（B309：1857）"},
    {"title": "散文诗（巴黎的忧郁）", "note": "（B309：Petits poèmes en prose (1868)——'the most successful and innovative early experiment in prose poetry'）"},
    {"title": "美学珍品", "note": "艺术评论（通说待核）"}],
  "style": [
    "'correspondances'（感应/对应）——象征主义的诗学起点（B309：Symbolist leaders regarded themselves as his followers）。",
    "'the fullest expression of French Romantic poetry'（B309：《恶之花》为法国浪漫主义诗歌的最充分表达）。",
    "散文诗实验（B309：Petits poèmes en prose——'the most successful and innovative early experiment'）。"],
  "status": "Britannica 定位波德莱尔为法国诗人、《恶之花》作者——象征主义先驱（B309）。",
  "sources": ["B309"], "dates_source": "B309",
  "pending": ["1861年第二版与增补篇目核对。","'correspondances'原诗（第4篇）核对。","Gauteng？——不：戈蒂耶《恶之花》献词待核。"]
},
"rimbaud": {
  "id": "rimbaud", "name": "阿尔蒂尔·兰波", "foreign_name": "Arthur Rimbaud（阿尔蒂尔·兰波，1854-10-20—1891-11-10）",
  "country": "法国", "birth": 1854, "death": 1891, "birth_year": 1854, "death_year": 1891, "era": "近代",
  "summary": "兰波，夏尔维尔生，法国诗人与冒险家——象征主义运动的中心人物之一（Britannica 语境）；'Many 20th-century poets were influenced by the Dionysian power of his verse and his liberation of language from the constraints of form'（其诗的酒神力量与语言解放影响了20世纪许多诗人——B310）；'one of the first modern poets to shatter the constraints of traditional metric forms'（最早打破传统格律的现代诗人之一——B310）；'a founding father of modernism'（现代主义的奠基者——B310 Legacy 语境）。弃文从商于非洲（B310）。",
  "timeline": [
    {"year": 1854, "text": "10月20日生于夏尔维尔（B310：Born October 20, 1854, Charleville, France）。", "src": "B310"},
    {"year": 1871, "text": "《醉舟》写就（B310：The Drunken Boat written 1871）；与魏尔伦相识（通说待核）。", "src": "B310"},
    {"year": 1873, "text": "《地狱一季》出版（B310：Une Saison en enfer——'Consisting of nine fragments of prose and verse'）。", "src": "B310"},
    {"year": 1891, "text": "11月10日卒于马赛（B310：Died November 10, 1891, Marseille，37岁）。", "src": "B310"}],
  "major_works": [
    {"work_id": "diyuzhiji", "note": "散文诗集（B310：1873，九个片段）"},
    {"title": "彩画集（Illuminations）", "note": "（B310：40 prose poems + 2 free-verse poems，1872—74年写）"},
    {"title": "醉舟", "note": "（B310：The Drunken Boat written 1871）"}],
  "style": [
    "'Dionysian power of his verse and his liberation of language from the constraints of form'（B310）。",
    "'shatter the constraints of traditional metric forms'（B310）。",
    "'a founding father of modernism'（B310 Legacy 语境）。"],
  "status": "Britannica 定位兰波为象征主义中心人物、现代主义奠基者之一（B310）；弃文从商于非洲（B310）。",
  "sources": ["B310"], "dates_source": "B310",
  "pending": ["《地狱一季》1873年（Brussels自印说）核对。","'通灵者书信'（Lettre du voyant，1871）待核。","与魏尔伦的恋情及布鲁塞尔枪击（1873）待核。"]
},
"tsvetaeva": {
  "id": "tsvetaeva", "name": "玛丽娜·茨维塔耶娃", "foreign_name": "Marina Ivanovna Tsvetayeva（玛丽娜·伊万诺夫娜·茨维塔耶娃，1892-10-08（儒历9-26）—1941-08-31）",
  "country": "俄国", "birth": 1892, "death": 1941, "birth_year": 1892, "death_year": 1941, "era": "现当代",
  "summary": "茨维塔耶娃，莫斯科生，俄罗斯诗人——'regarded as one of the finest Russian-language poets of the 20th century'（20世纪最优秀的俄语诗人之一——B311）；'distinctive for its staccato rhythms, originality, and directness'（断续的节奏、原创性与直接性——B311）。主要作品：Vecherny albom（1910）、Lebediny stan（1917—21写/1957慕尼黑出版）、Posle Rossii (1928)、Moy Pushkin (1937)、Stikhi k Chekhii (1938–39)（B311）。'She committed suicide in 1941'（1941年自尽——B311）。",
  "timeline": [
    {"year": 1892, "text": "10月8日（儒历9-26）生于莫斯科（B311）。", "src": "B311"},
    {"year": 1910, "text": "首部诗集《黄昏纪念册》出版（B311：Vecherny albom (Evening Album, 1910)）。", "src": "B311"},
    {"year": 1928, "text": "《俄罗斯之后》出版（B311：Posle Rossii (1928)——流亡巴黎期）。", "src": "B311"},
    {"year": 1941, "text": "8月31日卒于叶拉布加（B311：Died Aug. 31, 1941, Yelabuga——自杀）。", "src": "B311"}],
  "major_works": [
    {"work_id": "cweitayeva", "note": "诗选（本库立目）"},
    {"title": "天鹅营地", "note": "（B311：Lebediny stan，1917—21写/1957慕尼黑出版）"},
    {"title": "我的普希金", "note": "（B311：Moy Pushkin (1937)——散文）"}],
  "style": [
    "'staccato rhythms, originality, and directness'（B311）。",
    "'20世纪最优秀的俄语诗人之一'（B311）。",
    "流亡与回归的悲剧（B311 语境）。"],
  "status": "Britannica 定位茨维塔耶娃为20世纪最优秀的俄语诗人之一（B311）。",
  "sources": ["B311"], "dates_source": "B311",
  "pending": ["《天鹅营地》1957年慕尼黑出版细节核对。","与里尔克的通信（《信函》1926年三通信说）待核。","1941年自杀细节（叶拉布加说）待核。"]
},
"mandelshtam": {
  "id": "mandelshtam", "name": "奥西普·曼德尔施塔姆", "foreign_name": "Osip Emilyevich Mandelshtam（奥西普·叶梅利扬诺维奇·曼德尔施塔姆，1891-01-03/15—1938-12-27）",
  "country": "俄国", "birth": 1891, "death": 1938, "birth_year": 1891, "death_year": 1938, "era": "现当代",
  "summary": "曼德尔施塔姆，华沙生（时属俄罗斯帝国），俄罗斯诗人、散文家与随笔作家——Acmeism 共创人（Britannica：co-founded the Acmeist school of poetry）；Acmeists——'rejected the vague mysticism of Russian Symbolism and demanded clarity and concreteness'（拒绝俄国象征主义的含混神秘主义，要求清晰与具体——B312）。Kamen（石头，1913）——父亲出资出版首部诗集；题目象征阿克梅派'identification with the cultural essence of St. Petersburg'（与彼得堡文化本质的认同——B312）。1934年5月3日因讽刺诗被捕——'Sentenced to five years in a labour camp for anti-Soviet activity'，1938-12-27卒于海参崴附近中转营（B312）。",
  "timeline": [
    {"year": 1891, "text": "1月3日（儒历1-15）生于华沙（B312）。", "src": "B312"},
    {"year": 1913, "text": "首部诗集《石头》出版（B312：Kamen (Stone)——父亲出资）。", "src": "B312"},
    {"year": 1934, "text": "5月3日因讽刺斯大林的诗被捕（B312：arrested in 1934 for an epigram criticizing the dictator）。", "src": "B312"},
    {"year": 1938, "text": "12月27日卒于海参崴附近中转营（B312：died in a transit camp near Vladivostok）。", "src": "B312"}],
  "major_works": [
    {"work_id": "shitou", "note": "诗集（B312：Kamen (Stone, 1913)）"},
    {"title": "哀歌、Tristia", "note": "（通说待核）"},
    {"title": "噪声的时间", "note": "散文（通说待核）"}],
  "style": [
    "Acmeism：'clarity and concreteness'（B312）。",
    "'identification with the cultural essence of St. Petersburg'（《石头》——B312）。",
    "诗歌与建筑的同构（通说待核）。"],
  "status": "Britannica 定位曼德尔施塔姆为俄国重要诗人、Acmeism 共创人（B312）；因讽刺诗被捕死于中转营（B312）。",
  "sources": ["B312"], "dates_source": "B312",
  "pending": ["《石头》篇目（亚历山大车站等）核对。","'斯大林讽刺诗'（1933年11月说）待核。","娜杰日达《希望对抗希望》回忆录待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

works = {
"ezhihua": {
  "id":"ezhihua","title":"恶之花","original_title":"Les Fleurs du mal（The Flowers of Evil）","region":"法国","era":"近代","era_detail":"19世纪",
  "genre":"诗集","genre_group":"诗歌","language":"法语","author_id":"baudelaire","author_name":"夏尔·波德莱尔",
  "year_display":"1857年出版（Britannica：Les Fleurs du mal (1857; The Flowers of Evil)）","year_sort":1857,
  "background":["Britannica（B309）：'perhaps the most important and influential poetry collection published in Europe in the 19th century'（19世纪欧洲最重要、最具影响力的诗集——B309）；'the fullest expression of French Romantic poetry'（B309）。","审查（B309）：'In 1857, authorities charged thirteen poems from this collection with offenses against religion and public morality'——'six poems were censored due to obscenity, leading to a fine'。","结构（B309）：'The collection consists of poems arranged into six sections'；波德莱尔坚持它不是'simple album'而是有'beginning and an end'。"],
  "outline":["六部分：忧郁与理想/巴黎即景/酒/恶之花/叛逆/死亡（篇目通说待核）。"],
  "characters":[{"name":"诗人","identity":"抒情主体","note":"（B309 语境）"}],
  "themes":["'correspondances'（感应）——象征主义起点（B309）。",
   "美、恶与都市（通说待核）。",
   "'忧郁'（spleen）主题（通说待核）。"],
  "influence":[{"text":"Britannica：'perhaps the most important and influential poetry collection published in Europe in the 19th century'（B309）。","source":"B309"},
   {"text":"Britannica：象征主义领袖'regarded themselves as his followers'（B309）。","source":"B309"}],
  "reading":{"difficulties":["'correspondances'的通感诗学。","1857审查史。"],
   "editions":["《恶之花》（人民文学出版社/上海译文出版社版本，通说待核）。","法文原版（公有领域）。"],
   "order":"象征主义源头（先本作后兰波）。"},
  "pending":["1861年第二版增补核对。","'远行'（Le Voyage）终篇核对。","'six poems censored'篇目核对。"],
  "sources":["B309"],"year_source":"B309","author_source":"B309","related_works":["hongyuhei","weite","lianaizhongjie"],
  "svg":G2("《恶之花》六部结构图",[{"title":"忧郁与理想","text":"第一部分（通说）","color":"main"},{"title":"巴黎即景","text":"都市的忧郁","color":"gold"},{"title":"恶之花","text":"恶中的美","color":"antagonist"},{"title":"死亡","text":"终篇之旅（通说）","color":"family"}])
},
"diyuzhiji": {
  "id":"diyuzhiji","title":"地狱一季","original_title":"Une Saison en enfer（A Season in Hell）","region":"法国","era":"近代","era_detail":"19世纪",
  "genre":"散文诗集","genre_group":"诗歌","language":"法语","author_id":"rimbaud","author_name":"阿尔蒂尔·兰波",
  "year_display":"1873年（Britannica：Une Saison en enfer——'Consisting of nine fragments of prose and verse'）","year_sort":1873,
  "background":["Britannica（B310）：'Consisting of nine fragments of prose and verse'——examining 'Rimbauds search for experience and his relationship with Verlaine'（探察兰波的求索经历及与魏尔伦的关系——B310）。","作者（B310）：'Many 20th-century poets were influenced by the Dionysian power of his verse'；'a founding father of modernism'（B310 Legacy 语境）。"],
  "outline":["九个片段：坏血统/疯狂的眩晕/疯狂的重罚/谵妄I-II/不可能/闪光/清晨（篇名通说待核）。"],
  "characters":[{"name":"兰波","identity":"自白者","note":"（B310 语境）"}],
  "themes":["'通灵者'的自白与告别（通说待核）。",
   "'理性的人们'？——不：诗的自审（通说待核）。",
   "告别文学（1873年后弃文——B310 语境）。"],
  "influence":[{"text":"Britannica：'Many 20th-century poets were influenced by the Dionysian power of his verse'（B310）。","source":"B310"},
   {"text":"Britannica：'a founding father of modernism'（B310 Legacy 语境）。","source":"B310"}],
  "reading":{"difficulties":["散文诗的自白语调。","1873年弃文背景。"],
   "editions":["《地狱一季》（人民文学出版社/上海译文版本，通说待核）。","法文原版（公有领域）。"],
   "order":"先《醉舟》后本作；再读《彩画集》。"},
  "pending":["1873年（布鲁塞尔自印说）核对。","九个片段篇名核对。","'通灵者书信'（1871年5月两封——B310 已载日期）核对。"],
  "sources":["B310"],"year_source":"B310","author_source":"B310","related_works":["ezhihua","weite","hongyuhei"],
  "svg":G2("《地狱一季》九片段图",[{"title":"坏血统","text":"家族的自白（通说）","color":"antagonist"},{"title":"谵妄","text":"疯狂的清醒","color":"main"},{"title":"闪光","text":"洞见与告别","color":"gold"},{"title":"清晨","text":"终章（通说）","color":"family"}])
},
"cweitayeva": {
  "id":"cweitayeva","title":"茨维塔耶娃诗选","original_title":"Марина Цветаева（诗选）","region":"俄国","era":"现当代","era_detail":"20世纪",
  "genre":"诗选集","genre_group":"诗歌","language":"俄语","author_id":"tsvetaeva","author_name":"玛丽娜·茨维塔耶娃",
  "year_display":"诗作于1910—1941年间；通行选本数十首","year_sort":1922,
  "background":["作者页（B311）：茨维塔耶娃'regarded as one of the finest Russian-language poets of the 20th century'（B311 作者页定位）；'distinctive for its staccato rhythms, originality, and directness'（B311）。","主要作品（B311）：Vecherny albom (1910)、Lebediny stan（1917—21写/1957出版）、Posle Rossii (1928)、Moy Pushkin (1937)、Stikhi k Chekhii (1938–39)。","'She committed suicide in 1941'（B311）。"],
  "outline":["《黄昏纪念册》(1910)、《神灯》(1912)、《从两本书》(1913)——早期三集（通说待核）。","《天鹅营地》(1917—21)、《俄罗斯之后》(1928)——流亡期（通说待核）。","《我的普希金》(1937)——散文（B311）。"],
  "characters":[{"name":"茨维塔耶娃","identity":"诗人","note":"'staccato rhythms'（B311）"}],
  "themes":["流亡与回归（B311 语境）。",
   "爱情诗（致帕斯捷尔纳克/里尔克——通说待核）。",
   "母性与女儿（通说待核）。"],
  "influence":[{"text":"Britannica：'one of the finest Russian-language poets of the 20th century'（B311）。","source":"B311"},
   {"text":"作者页：布罗茨基等后辈诗人的推崇（通说待核——B313 未载）。","source":"B313"}],
  "reading":{"difficulties":["断续节奏的朗读。","流亡三阶段（布拉格/巴黎）。"],
   "editions":["《茨维塔耶娃诗集》（人民文学出版社/广西师范大学出版社版本，通说待核）。","俄文原版。"],
   "order":"先《黄昏纪念册》后流亡期。"},
  "pending":["《黄昏纪念册》1910年出版核对。","《致布洛克的诗》《致阿赫玛托娃》组诗待核。","1941年叶拉布加自杀细节（B311 已载）核对。"],
  "sources":["B311"],"year_source":"B311","author_source":"B311","related_works":["anhunqu","nianzhu","xiaoyuyi"],
  "svg":G2("茨维塔耶娃诗歌结构图",[{"title":"黄昏纪念册","text":"1910首集（B311）","color":"family"},{"title":"天鹅营地","text":"1917—21（B311）","color":"main"},{"title":"俄罗斯之后","text":"流亡巴黎（B311）","color":"gold"},{"title":"叶拉布加","text":"1941年的终点","color":"antagonist"}])
},
"shitou": {
  "id":"shitou","title":"石头","original_title":"Камень（Kamen / Stone）","region":"俄国","era":"现当代","era_detail":"20世纪初",
  "genre":"诗集","genre_group":"诗歌","language":"俄语","author_id":"mandelshtam","author_name":"奥西普·曼德尔施塔姆",
  "year_display":"1913年（Britannica：In 1913 his father underwrote the publication of his first slim volume of verse, Kamen (Stone)）","year_sort":1913,
  "background":["Britannica（B312）：'In 1913 his father underwrote the publication of his first slim volume of verse, Kamen (Stone)'——父亲出资出版首部小诗集。","题目象征（B312）：Acmeists'identification with the cultural essence of St. Petersburg'（与彼得堡文化本质的认同——B312）。","Acmeism（B312）：'rejected the vague mysticism of Russian Symbolism and demanded clarity and concreteness'。","结局（B312）：1934年5月3日因讽刺诗被捕——'Sentenced to five years in a labour camp'，1938-12-27卒于中转营。"],
  "outline":["彼得堡的建筑与文化：海军大厦、圣索菲亚（篇目通说待核）。"],
  "characters":[{"name":"曼德尔施塔姆","identity":"诗人","note":"Acmeist（B312）"}],
  "themes":["石头：彼得堡文化的认同（B312）。",
   "建筑与诗歌的同构（通说待核）。",
   "Acmeism 的'清晰与具体'（B312：clarity and concreteness）。"],
  "influence":[{"text":"Britannica：Acmeism——'rejected the vague mysticism of Russian Symbolism'（B312）。","source":"B312"},
   {"text":"Britannica：'identification with the cultural essence of St. Petersburg'（B312）。","source":"B312"}],
  "reading":{"difficulties":["Acmeism 与 Symbolism 的对立。","彼得堡建筑史。"],
   "editions":["《石头》（Princeton University Press 英译本，通说待核）。","俄文原版。"],
   "order":"曼德尔施塔姆诗集首选。"},
  "pending":["《石头》1913年篇目（33首说）核对。","1930年《石头》增订版待核。","'Notre Dame'首篇待核。"],
  "sources":["B312"],"year_source":"B312","author_source":"B312","related_works":["anhunqu","geti","shenqu"],
  "svg":G2("《石头》Acmeism结构图",[{"title":"石头","text":"彼得堡的文化认同（B312）","color":"main"},{"title":"Acmeism","text":"'clarity and concreteness'（B312）","color":"family"},{"title":"1934被捕","text":"讽刺诗的代价（B312）","color":"antagonist"},{"title":"中转营","text":"1938年的终点","color":"gold"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
