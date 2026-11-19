# -*- coding: utf-8 -*-
"""v9：黄泥街（残雪）+ 4部复用直写 + 1来源"""
import json, pathlib

new_src = [
{"id":"B266","title":"Can Xue — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Can-Xue","type":"百科全书","verified":True,"covers":["canxue","huangnijie"],"note":"2026-11-20 核对：残雪（本名邓小华）1953年生于湖南长沙；中篇《黄泥街》（Huang ni jie）1987年——'concerns a strange event in a decrepit factory town'、'comical and surreal elements as well as extremely graphic descriptions of the filth'；'Can's fiction is noted for its experimentalism'；'surreal, fantastical, and absurdist elements and nonlinear plots'；苏珊·桑塔格'had named her as a likely future contender for the Nobel Prize for Literature'；'one of the most unique and challenging avant-garde authors in contemporary literature'；两次入围国际布克奖"},
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
"canxue": {
  "id": "canxue", "name": "残雪", "foreign_name": "Can Xue（残雪，本名邓小华说——Britannica 口径，1953— ）",
  "country": "中国", "birth": 1953, "death": None, "birth_year": 1953, "death_year": None, "era": "现当代",
  "summary": "残雪（Britannica：pen name of Deng Xiaohua——本名邓小华），1953年生于湖南长沙，中国先锋作家——'celebrated for experimental fiction blending surreal, absurd, and fantastical elements'（以混合超现实、荒诞与奇幻元素的实验小说著称——Britannica）。中篇《黄泥街》（1987）——'concerns a strange event in a decrepit factory town'，有'comical and surreal elements as well as extremely graphic descriptions of the filth'（B266）。'Can's fiction is noted for its experimentalism'（B266）；苏珊·桑塔格'had named her as a likely future contender for the Nobel Prize for Literature'（B266）。",
  "timeline": [
    {"year": 1953, "text": "生于湖南长沙（Britannica：Born 1953 in Changsha, Hunan province）。", "src": "B266"},
    {"year": 1987, "text": "中篇《黄泥街》出版（Britannica：Yellow Mud Street was published in 1987）。", "src": "B266"},
    {"year": 2019, "text": "两次入围国际布克奖（Britannica：Twice nominated for the International Booker Prize——年份待核）。", "src": "B266"}],
  "major_works": [
    {"work_id": "huangnijie", "note": "中篇（Britannica：1987）"},
    {"title": "五香街、最后的情人", "note": "（Britannica：Five Spice Street (2002), The Last Lover (2005)）"},
    {"title": "边疆、新世纪爱情故事", "note": "（Britannica：Frontier (2008), Love in the New Millennium (2013)）"}],
  "style": [
    "'experimentalism'（Britannica：experimentalism 著称）。",
    "'surreal, fantastical, and absurdist elements and nonlinear plots'（B266）。",
    "'极富个性与挑战性的先锋作家'（B266：one of the most unique and challenging avant-garde authors）。"],
  "status": "Britannica 定位残雪为当代文学'最独特、最具挑战性的先锋作家'之一（B266）；桑塔格视其为可能的诺奖竞争者（B266）。",
  "sources": ["B266"], "dates_source": "B266",
  "pending": ["本名邓小华与'残雪'笔名来源（'残雪'自解待核）。", "两次国际布克奖入围年份核对。", "《山上的小屋》短篇与其代表作地位待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"heitaohuanghou": {
  "id":"heitaohuanghou","title":"黑桃皇后","original_title":"Пиковая дама（The Queen of Spades）","region":"俄国","era":"近代","era_detail":"19世纪",
  "genre":"短篇小说","genre_group":"小说","language":"俄语","author_id":"pushkin","author_name":"亚历山大·普希金",
  "year_display":"1834年（通说待核；作者页 B143 口径：major_works 载'黑桃皇后、上尉的女儿'）","year_sort":1834,
  "background":["作者页（B143）：普希金 major_works 载'黑桃皇后、上尉的女儿'（B143 作者页定位，详见 aonijin 条核对）。","普希金为俄国文学之父（作者页定位）。"],
  "outline":["赌徒赫尔曼以'三张牌'秘术赌命——丽莎维塔与老伯爵夫人的悲剧（通说待核）。","结尾：赫尔曼疯于'黑桃皇后'（通说待核）。"],
  "characters":[{"name":"赫尔曼","identity":"军官","note":"赌徒（通说待核）"},{"name":"伯爵夫人","identity":"老妇","note":"秘术的持有者（通说待核）"}],
  "themes":["赌与贪的神秘主义（通说）。",
   "圣彼得堡的幽灵（通说）。",
   "散文体的紧凑（通说）。"],
  "influence":[{"text":"作者页：普希金后期名篇（B143 作者页口径）。","source":"B143"},
   {"text":"柴可夫斯基同名歌剧（1890——通说待核）。","source":"B143"}],
  "reading":{"difficulties":["俄国牌戏与称谓。","神秘主义调子。"],
   "editions":["《黑桃皇后》（人民文学出版社《普希金全集》，通说待核）。","英文原版（公有领域）。"],
   "order":"先《叶甫盖尼·奥涅金》后本作。"},
  "pending":["1834年（《读者文库》说）核对。","赫尔曼/丽莎维塔人名核对。","歌剧1890年核对。"],
  "sources":["B143"],"year_source":"B143","author_source":"B143","related_works":["aonijin","waitao","shangweidenv'er"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《黑桃皇后》赌局结构图",
    "cards":[{"title":"三张牌","text":"秘术的诱惑","color":"gold"},{"title":"赫尔曼","text":"理性的赌徒","color":"main"},{"title":"伯爵夫人","text":"鬼魂的秘密","color":"antagonist"},{"title":"疯","text":"黑桃的诅咒","color":"plain"}]}
},
"shangweidenv'er": {
  "id":"shangweidenv'er","title":"上尉的女儿","original_title":"Капитанская дочка（The Captain's Daughter）","region":"俄国","era":"近代","era_detail":"19世纪",
  "genre":"中篇小说","genre_group":"小说","language":"俄语","author_id":"pushkin","author_name":"亚历山大·普希金",
  "year_display":"1836年（通说待核；作者页 B143 口径：major_works 载'上尉的女儿'）","year_sort":1836,
  "background":["作者页（B143）：普希金 major_works 载'上尉的女儿'——历史小说（B143 作者页定位，详见 aonijin 条核对）。","题材（通说待核）：普加乔夫起义（1773—75）——历史与虚构的结合。"],
  "outline":["格里尼奥夫与玛莎在普加乔夫起义中的遭遇——普加乔夫的'赦免'（通说待核）。"],
  "characters":[{"name":"格里尼奥夫","identity":"军官","note":"叙述者（通说待核）"},{"name":"普加乔夫","identity":"起义领袖","note":"历史的虚构（通说待核）"}],
  "themes":["历史小说的典范（通说）。",
   "起义领袖的复杂面孔（通说）。",
   "宽容与忠诚（通说待核）。"],
  "influence":[{"text":"作者页：普希金散文代表作（B143 作者页口径）。","source":"B143"},
   {"text":"俄国历史小说的开端之一（通说待核）。","source":"B143"}],
  "reading":{"difficulties":["普加乔夫起义史实。","哥萨克词汇。"],
   "editions":["《上尉的女儿》（人民文学出版社，通说待核）。","英文原版（公有领域）。"],
   "order":"先《奥涅金》《黑桃皇后》后本作。"},
  "pending":["1836年（《现代人》刊出说）核对。","格里尼奥夫/玛莎人名核对。","普加乔夫史实与虚构边界待核。"],
  "sources":["B143"],"year_source":"B143","author_source":"B143","related_works":["aonijin","heitaohuanghou","shangweidenv'er"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《上尉的女儿》历史结构图",
    "cards":[{"title":"起义","text":"普加乔夫（通说）","color":"antagonist"},{"title":"赦免","text":"兔皮外套的恩义","color":"main"},{"title":"爱情","text":"上尉的女儿","color":"gold"},{"title":"历史","text":"虚构的证词","color":"plain"}]}
},
"dubolinen": {
  "id":"dubolinen","title":"都柏林人","original_title":"Dubliners","region":"爱尔兰","era":"现当代","era_detail":"20世纪初",
  "genre":"短篇小说集","genre_group":"小说","language":"英语","author_id":"joyce","author_name":"詹姆斯·乔伊斯",
  "year_display":"1914年出版（作者页 B093 口径：都柏林人（1914））","year_sort":1914,
  "background":["作者页（B093）：乔伊斯 major_works 载'都柏林人（1914）'（B093 作者页定位，详见 youlisisi 条核对）。","'瘫痪'（paralysis）主题：乔伊斯自述（通说待核——致出版商信）。"],
  "outline":["十五篇（篇数通说）：童年—青春期—成年—公共生活的四个阶段（结构通说待核）。","末篇《死者》：白雪中的'雪落所有的生者与死者'（名句通说待核）。"],
  "characters":[{"name":"加布里埃尔","identity":"《死者》主角","note":"雪夜的自省（通说待核）"},{"name":"伊芙琳","identity":"少女","note":"《伊芙琳》的抉择（通说待核）"}],
  "themes":["都柏林的'瘫痪'（通说待核）。",
   "顿悟（epiphany）技法（通说待核）。",
   "逃离与滞留（通说）。"],
  "influence":[{"text":"作者页：乔伊斯成名前的重要作品（B093 作者页口径）。","source":"B093"},
   {"text":"现代短篇小说的经典（通说待核）。","source":"B093"}],
  "reading":{"difficulties":["爱尔兰语词与政治背景。","顿悟的识别。"],
   "editions":["《都柏林人》（上海译文出版社王逢振译本，通说待核）。","英文原版（公有领域）。"],
   "order":"先《都柏林人》后《尤利西斯》。"},
  "pending":["十五篇篇目核对。","1914年（Grant Richards说，出版波折）核对。","'瘫痪'自述信出处待核。"],
  "sources":["B093"],"year_source":"B093","author_source":"B093","related_works":["youlisisi","xinishixuan","jimuye"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《都柏林人》四阶段结构图",
    "cards":[{"title":"童年","text":"《阿拉比》等","color":"family"},{"title":"青春期","text":"《伊芙琳》等","color":"main"},{"title":"成年","text":"《死者》前的群像","color":"gold"},{"title":"死者","text":"雪落生者与死者（名句待核）","color":"plain"}]}
},
"suixianglu": {
  "id":"suixianglu","title":"随想录","original_title":"随想录（散文集五卷）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"散文集","genre_group":"散文","language":"汉语（白话）","author_id":"bajin","author_name":"巴金",
  "year_display":"1978—1986年（作者页 B079 口径：随想录（1978—86））","year_sort":1982,
  "background":["作者页（B079）：巴金 major_works 载'随想录（1978—86）'（B079 作者页定位，详见 jia 条核对）。","意义（通说待核）：晚年巴金的自我清算——'讲真话'与反思'文革'的散文总集。"],
  "outline":["五卷：《随想录》《探索集》《真话集》《病中集》《无题集》（卷名通说待核）。","《怀念萧珊》：悼亡妻之文（通说待核）。"],
  "characters":[{"name":"巴金","identity":"散文作者","note":"讲真话的老人"}],
  "themes":["讲真话（通说待核——其核心口号）。",
   "反思'文革'的忏悔（通说）。",
   "'生命的开花'（通说待核）。"],
  "influence":[{"text":"作者页：巴金晚年散文总集（B079 作者页口径）。","source":"B079"},
   {"text":"新时期散文的精神标杆（通说待核）。","source":"B079"}],
  "reading":{"difficulties":["'文革'记忆的沉重。","平淡文体的力量。"],
   "editions":["《随想录》（人民文学出版社/三联书店版本，通说待核）。"],
   "order":"先《家》后本作：巴金的两端。"},
  "pending":["五卷卷名核对。","《怀念萧珊》篇核对。","'讲真话的大书'评价出处待核。"],
  "sources":["B079"],"year_source":"B079","author_source":"B079","related_works":["jia","hanye","woyuditan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《随想录》五卷结构图",
    "cards":[{"title":"随想录","text":"起笔1978","color":"family"},{"title":"真话集","text":"讲真话","color":"main"},{"title":"病中集","text":"衰病的写作","color":"gold"},{"title":"无题集","text":"最后的反思","color":"plain"}]}
},
"huangnijie": {
  "id":"huangnijie","title":"黄泥街","original_title":"黄泥街（中篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"中篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"canxue","author_name":"残雪",
  "year_display":"1987年出版（Britannica：Yellow Mud Street was published in 1987）","year_sort":1987,
  "background":["Britannica（B266）：'concerns a strange event in a decrepit factory town'——写破败工厂小镇的奇异事件；'comical and surreal elements as well as extremely graphic descriptions of the filth'（滑稽超现实的元素与对污秽的极端直露的描写——B266）。","'Can's fiction is noted for its experimentalism'（B266）；苏珊·桑塔格视其为可能的诺奖竞争者（B266）。"],
  "outline":["黄泥街的'黄泥'世界：粪便、太阳与王子——梦魇中的街道史（情节通说待核）。"],
  "characters":[{"name":"王子光","identity":"幻影人物","note":"（通说待核）"},{"name":"齐国　……不：齐婆等","identity":"街民","note":"（通说待核）"}],
  "themes":["污秽与超现实（B266）。",
   "梦魇叙事（B266：nonlinear plots）。",
   "实验主义的汉语（B266：experimentalism）。"],
  "influence":[{"text":"Britannica：残雪实验小说的代表（B266）。","source":"B266"},
   {"text":"先锋文学的最极端样本（通说待核）。","source":"B266"}],
  "reading":{"difficulties":["污秽意象的承受力。","非线性的梦魇逻辑。"],
   "editions":["《黄泥街》（湖南文艺出版社，通说待核）。"],
   "order":"先锋文学的进阶阅读——先读卡夫卡。"},
  "pending":["情节细节（王子光/齐婆）核对。","1987年刊出（《中国》杂志说）待核。","'先锋五虎'并称说待核。"],
  "sources":["B266"],"year_source":"B266","author_source":"B266","related_works":["bianxingji","huangyezhentan","xiaobaozhuang"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《黄泥街》梦魇结构图",
    "cards":[{"title":"黄泥街","text":"污秽的街道（B266）","color":"antagonist"},{"title":"王子光","text":"幻影的来访","color":"gold"},{"title":"街民","text":"梦魇的合唱","color":"family"},{"title":"实验","text":"超现实与非线性（B266）","color":"main"}]}
},
"he'an": {
  "id":"he'an","title":"河岸","original_title":"河岸（长篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"sutong","author_name":"苏童",
  "year_display":"出版年份待核（中国作家网 C015：'《米》《我的帝王生涯》《河岸》等长篇'——2009年说通说待核）","year_sort":2009,
  "background":["中国作家网（C015）：'《米》《我的帝王生涯》《河岸》等长篇'——本作为苏童长篇代表作（C015 官方口径）。","题材（通说待核）：'空脚天'？——不：船上的少年库文轩与'烈属'身份的崩塌（情节通说待核）。"],
  "outline":["河流上的生活：岸上/船上的两界（通说待核）。","身份的政治与青春的溃败（通说待核）。"],
  "characters":[{"name":"库文轩","identity":"父亲","note":"'烈属'身份（通说待核）"},{"name":"库东亮","identity":"少年","note":"叙述者（通说待核）"}],
  "themes":["岸与船：身份的两界（通说）。",
   "历史身份的崩塌（通说待核）。",
   "香椿树街之外的河流书写（通说）。"],
  "influence":[{"text":"中国作家网：列入苏童长篇代表作（C015）。","source":"C015"},
   {"text":"第三届红楼梦奖决审团奖（通说待核——C022 搜索口径）。","source":"C015"}],
  "reading":{"difficulties":["历史政治背景。","河流意象的贯穿。"],
   "editions":["《河岸》（人民文学出版社，通说待核）。"],
   "order":"先《米》后本作。"},
  "pending":["2009年人民文学出版社初版核对。","库文轩/库东亮人名核对。","红楼梦奖（决审团奖）核对。"],
  "sources":["C015"],"year_source":"C015","author_source":"C015","related_works":["mi","huangqueji","heiansenlin"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《河岸》两界结构图",
    "cards":[{"title":"岸","text":"身份与政治","color":"antagonist"},{"title":"船","text":"流放的家","color":"main"},{"title":"库东亮","text":"少年视角","color":"family"},{"title":"河流","text":"漂泊的母亲河","color":"gold"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
