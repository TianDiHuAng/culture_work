# -*- coding: utf-8 -*-
"""批48：零成本 12 部（水/白雪皇后/教师/最后时光/汤姆·奥·桑特/定向/塔拉/影子与行动/中国佬/国王死去/疯狂的爱/恩培多克勒之死）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 丁玲《水》
{"id":"shui","title":"水","original_title":"水","region":"中国","era":"近代","era_detail":"20世纪30年代初",
"genre":"短篇小说","genre_group":"小说","language":"汉语","author_id":"dingling","author_name":"丁玲",
"year_display":"1931年（作者页注记：Britannica——水 (1931)）","year_sort":1931,
"background":["作者页注记：水 (1931)——'社会主义现实主义（Britannica）'。","Britannica：丁玲——现代中国女作家（作者页语境）。","题材（通说待核）：十六省水灾的农民群像——集体化的视角转换。"],
"outline":["（通说待核）洪水中农民从个人求生到集体觉醒。","（通说待核）'水'：既是灾难也是人民之力。"],
"characters":[{"name":"农民群像","identity":"——","note":"（通说待核——无单一主角）"}],
"themes":["'社会主义现实主义'的先声（B注记）。",
 "灾难叙事的集体化（通说待核）。",
 "从个人到群像的转换（作者页语境）。"],
"influence":[{"text":"Britannica：水 (1931)（作者页注记）。","source":src_of('dingling')},{"text":"Britannica：丁玲左翼转向（作者页语境——待核）。","source":src_of('dingling')}],
"reading":{"difficulties":["1931年江淮大水史。","'群像'的无主角结构。"],
 "editions":["《水》（人民文学出版社《丁玲全集》等——通说待核）。","1931年发表（《北斗》说）待核。"],
 "order":"丁玲左翼阶段；与《莎菲女士的日记》对照。"},
"pending":["1931年发表刊物核对。","'群像'结构细节待核。","'社会主义现实主义'评价（B注记）核对。"],
"sources":[src_of('dingling')],"year_source":src_of('dingling'),"author_source":src_of('dingling'),"related_works":["shafeinushideriji","zaidiceng","nongmin"],
"svg":G("《水》洪水群像图",[{"title":"洪水","text":"灾难的浪（书名）","color":"antagonist"},{"title":"农民","text":"群像的觉醒（通说）","color":"main"},{"title":"集体","text":"从求生到组织（通说）","color":"gold"},{"title":"左翼","text":"现实的转向（B注记）","color":"family"}])},
# 2. 安徒生《白雪皇后》
{"id":"baixuehuanghou","title":"白雪皇后","original_title":"Snedronningen（The Snow Queen）","region":"丹麦","era":"近代","era_detail":"19世纪40年代",
"genre":"童话","genre_group":"故事集","language":"丹麦语","author_id":"andersen","author_name":"安徒生",
"year_display":"作者页注记：Britannica 语境——白雪皇后（发表年份通说待核——1844说）","year_sort":1844,
"background":["作者页注记：海的女儿、丑小鸭、白雪皇后——'（Britannica 语境）'。","Britannica：安徒生——童话作家（作者页语境）。","题材（通说待核）：镜子的碎片入心——格尔达雪原寻友。"],
"outline":["（通说待核）卡伊被镜片与白雪皇后带走。","（通说待核）格尔达的冬季寻友与吻的融化。"],
"characters":[{"name":"格尔达","identity":"寻友少女","note":"（通说待核）"},{"name":"卡伊","identity":"被带走男孩","note":"（通说待核）"},{"name":"白雪皇后","identity":"冰雪之宫主人","note":"（书名人物）"}],
"themes":["'理性的冰'与'心的火'（通说待核）。",
 "七段故事的旅程结构（通说待核）。",
 "善的救赎（通说待核）。"],
"influence":[{"text":"Britannica：安徒生童话序列（作者页注记）。","source":src_of('andersen')},{"text":"Britannica：安徒生为童话大师（作者页语境）。","source":src_of('andersen')}],
"reading":{"difficulties":["七个故事的结构（通说待核）。","'镜子的碎片'寓意。"],
 "editions":["《白雪皇后》（人民文学出版社《安徒生童话全集》等——通说待核）。","丹麦文原版（公有领域）。"],
 "order":"安徒生代表作；与《海的女儿》《丑小鸭》对读。"},
"pending":["1844年发表（《新童话》第二集说）待核。","七段结构核对（通说）。","'泰恩'等名词细节待核。"],
"sources":[src_of('andersen')],"year_source":src_of('andersen'),"author_source":src_of('andersen'),"related_works":["haidenvren","chouxiaoya","baimaqishi"],
"svg":G("《白雪皇后》冰火结构图",[{"title":"镜片","text":"理性的碎片（通说）","color":"antagonist"},{"title":"格尔达","text":"寻友的火（通说）","color":"main"},{"title":"雪宫","text":"冰雪的王国（书名）","color":"gold"},{"title":"吻","text":"融化的救赎（通说）","color":"family"}])},
# 3. 夏洛蒂·勃朗特《教师》
{"id":"jiaoshi","title":"教师","original_title":"The Professor","region":"英国","era":"近代","era_detail":"19世纪40-50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"charlotte-bronte","author_name":"夏洛蒂·勃朗特",
"year_display":"身后出版（作者页注记：Britannica——The Professor was published posthumously——年份通说待核——1857说）","year_sort":1857,
"background":["作者页注记：教师——'首作身后出版（Britannica：The Professor was published posthumously）'。","Britannica：夏洛蒂·勃朗特——勃朗特三姐妹（作者页语境）。","题材（通说待核）：威廉·克里姆斯沃思的 Belgian 教书生涯——第一人称男性叙述。"],
"outline":["（通说待核）威廉在布鲁塞尔的教书生涯与Angioletti? （人物细节通说待核）。","（通说待核）'教师'的独立与婚姻。"],
"characters":[{"name":"威廉·克里姆斯沃思","identity":"教师/叙述者","note":"（通说待核）"},{"name":"弗朗西丝·亨利","identity":"学生/爱人","note":"（通说待核）"}],
"themes":["自食其力的伦理（通说待核）。",
 "男性第一人称的勃朗特实验（通说待核）。",
 "布鲁塞尔经历的自传对应（作者页语境——待核）。"],
"influence":[{"text":"Britannica：'The Professor was published posthumously'（作者页注记）。","source":src_of('charlotte-bronte')},{"text":"Britannica：《简·爱》为代表作（作者页交叉）。","source":src_of('charlotte-bronte')}],
"reading":{"difficulties":["男性叙述者的语调。","'首作被拒'的出版史（通说待核）。"],
 "editions":["《教师》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"勃朗特学者向阅读；与《维莱特》对读。"},
"pending":["1857年出版（Smith Elder说）待核。","威廉·克里姆斯沃思人名核对（通说）。","与《维莱特》的互文待核。"],
"sources":[src_of('charlotte-bronte')],"year_source":src_of('charlotte-bronte'),"author_source":src_of('charlotte-bronte'),"related_works":["sheli","weilaite","jianai"],
"svg":G("《教师》首作结构图",[{"title":"教师","text":"自食其力（通说）","color":"main"},{"title":"布鲁塞尔","text":"异国的讲台（通说）","color":"family"},{"title":"身后","text":"出版的曲折（B注记）","color":"gold"},{"title":"婚姻","text":"独立的完成（通说）","color":"antagonist"}])},
# 4. 海勒《最后时光》
{"id":"zuihouguangshi","title":"最后时光","original_title":"Closing Time","region":"美国","era":"现当代","era_detail":"21世纪初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"heller","author_name":"约瑟夫·海勒",
"year_display":"作者页注记：Britannica——Closing Time（年份通说待核——1994说）","year_sort":1994,
"background":["作者页注记：最后时光——'（Britannica：Closing Time）'。","Britannica：海勒——Catch-22 作者（作者页交叉）。","题材（通说待核）：《第二十二条军规》的续篇——老兵们的'末日'聚会。"],
"outline":["（通说待核）约塞连们的老年重聚与'关闭时间'。","（通说待核）美国的黄昏与死亡的黑玩笑。"],
"characters":[{"name":"约塞连等","identity":"老兵","note":"（通说待核）"}],
"themes":["'黑色幽默'的晚年变奏（作者页语境——通说待核）。",
 "代际的终结（书名语境）。",
 "美国的自我清算（通说待核）。"],
"influence":[{"text":"Britannica：Closing Time（作者页注记）。","source":src_of('heller')},{"text":"Britannica：Catch-22 为代表作（作者页交叉）。","source":src_of('heller')}],
"reading":{"difficulties":["续篇的互文。","1990年代美国政治讽刺。"],
 "editions":["《最后时光》中译名（《关上时间》）待核。","英文原版。"],
 "order":"海勒收官之作；先读《第二十二条军规》。"},
"pending":["1994年出版细节待核。","约塞连回归细节待核。","中译名待核。"],
"sources":[src_of('heller')],"year_source":src_of('heller'),"author_source":src_of('heller'),"related_works":["di-erershierjunju" if "di-erershierjunju" in existing else "leiyu","meiguobuqu","toutougeonv"],
"svg":G("《最后时光》末日聚会图",[{"title":"重聚","text":"老兵的晚年（通说）","color":"main"},{"title":"关上时间","text":"末日的玩笑（书名）","color":"gold"},{"title":"军规","text":"续篇的互文（作者页语境）","color":"family"},{"title":"黑色幽默","text":"美国的黄昏（通说）","color":"antagonist"}])},
# 5. 彭斯《汤姆·奥·桑特》
{"id":"tangmosangte","title":"汤姆·奥·桑特","original_title":"Tam o' Shanter","region":"苏格兰","era":"近代","era_detail":"18世纪90年代初",
"genre":"长诗","genre_group":"诗歌","language":"苏格兰语","author_id":"burnsburns","author_name":"罗伯特·彭斯",
"year_display":"1791年（Britannica B299：汤姆·奥·桑特——1791，mock-heroic）","year_sort":1791,
"background":["Britannica（B299）：Tam o' Shanter——1791——mock-heroic（模仿英雄体）。","Britannica（B299）：彭斯——苏格兰民族诗人（作者页交叉）。","题材（通说待核）：汤姆酒醉夜归——教堂里巫鬼的狂欢与被追逐。"],
"outline":["（通说待核）汤姆从酒馆夜归遇鬼。","（通说待核）'剪短的尾巴'：巫婆追过桥。"],
"characters":[{"name":"汤姆","identity":"醉汉","note":"（通说待核）"},{"name":"南妮","identity":"巫婆","note":"（通说待核）"}],
"themes":["苏格兰民间鬼话（通说待核）。",
 "mock-heroic 的滑稽史诗（B299）。",
 "'故事'与'教训'的插叙（通说待核）。"],
"influence":[{"text":"Britannica：Tam o' Shanter (1791)——mock-heroic（B299）。","source":"B299"},{"text":"Britannica：彭斯诗歌地位（B299 作者页）。","source":"B299"}],
"reading":{"difficulties":["苏格兰方言。","mock-heroic 的反讽。"],
 "editions":["《汤姆·奥·桑特》中译本（人民文学等——通说待核）。","苏格兰语原版（公有领域）。"],
 "order":"彭斯叙事诗首选；与《一朵红红的玫瑰》对读。"},
"pending":["南妮人名核对（通说）。","1791年写作（致Francis Grose信说）待核。","'剪尾'细节待核。"],
"sources":["B299"],"year_source":"B299","author_source":"B299","related_works":["yiduohonghongdmeigui" if "yiduohonghongdmeigui" in existing else "diyuzhiji","xinnuofusuobaken","pochan"],
"svg":G("《汤姆·奥·桑特》鬼夜结构图",[{"title":"汤姆","text":"酒醉的夜归（通说）","color":"main"},{"title":"教堂","text":"巫鬼的狂欢（通说）","color":"antagonist"},{"title":"桥","text":"逃命的界线（通说）","color":"gold"},{"title":"mock-heroic","text":"滑稽史诗（B299）","color":"family"}])},
# 6. 埃利蒂斯《定向》
{"id":"dingxiang","title":"定向","original_title":"Prosanatolismoi（Orientations）","region":"希腊","era":"近代","era_detail":"20世纪40年代初",
"genre":"诗集","genre_group":"诗歌","language":"希腊语","author_id":"elytis","author_name":"奥季修斯·埃利蒂斯",
"year_display":"1940年（Britannica B357：Prosanatolismoi (1940; Orientations)——collection of works to that date）","year_sort":1940,
"background":["Britannica（B357）：Prosanatolismoi——'collection of works to that date'（此前作品合集）。","Britannica（B357）：埃利蒂斯——受法国超现实主义影响（尤其艾吕雅）；刊于 Nea grammata——'30一代'。","题材（通说待核）：爱琴海的'透明'与光的颂歌——成名前作合集。"],
"outline":["（通说待核）爱琴海岛屿的光与透明的意象群。","（通说待核）'东方化'（Orientations）的命名：面向东方。"],
"characters":[{"name":"抒情'我'","identity":"光之诗人","note":"（通说待核）"}],
"themes":["爱琴海的光（书名语境——通说待核）。",
 "超现实主义与希腊民歌（B357）。",
 "'30一代'的位置（B357）。"],
"influence":[{"text":"Britannica：Prosanatolismoi (1940)（B357）。","source":"B357"},{"text":"Britannica：1979诺奖（B357 交叉）。","source":"B357"}],
"reading":{"difficulties":["超现实主义语汇。","希腊海岛地理。"],
 "editions":["《定向》中译名（《方位》）待核。","希腊文原版。"],
 "order":"埃利蒂斯成名前作；后接《理所应当》。"},
"pending":["篇目核对（B357未载）。","1940年出版细节待核。","'Orientations'译名待核。"],
"sources":["B357"],"year_source":"B357","author_source":"B357","related_works":["zhidezansongde","shenhualishi","diyuzhiji"],
"svg":G("《定向》爱琴海光图",[{"title":"光","text":"爱琴海的透明（通说）","color":"gold"},{"title":"定向","text":"面向东方（书名）","color":"main"},{"title":"超现实","text":"法国的影响（B357）","color":"family"},{"title":"战争","text":"1940的阴影（通说）","color":"antagonist"}])},
# 7. 加·米斯特拉尔《塔拉》
{"id":"tala","title":"塔拉","original_title":"Tala","region":"智利","era":"近代","era_detail":"20世纪30年代末",
"genre":"诗集","genre_group":"诗歌","language":"西班牙语","author_id":"gmistral","author_name":"加夫列拉·米斯特拉尔",
"year_display":"1938年（Britannica B343：Tala (1938; 'Destruction')）","year_sort":1938,
"background":["Britannica（B343）：Tala——'Destruction'——与 Ternura、Lagar 一起'evidence a broader interest'。","Britannica（B343）：米斯特拉尔——1945诺奖——'love of children and of the downtrodden remained her principal themes'。","题材（通说待核）：《美洲》等诗——从母性之爱扩展到大陆之爱。"],
"outline":["（通说待核）'塔拉'（毁坏）的题意与美洲主题。","（通说待核）'Sol y Luna'等组诗（篇目通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"教师/诗人","note":"（B343 语境）"}],
"themes":["'更广的兴趣'（B343：a broader interest）。",
 "美洲的大陆之爱（通说待核）。",
 "爱与毁坏（书名语境）。"],
"influence":[{"text":"Britannica：'evidence a broader interest'（B343）。","source":"B343"},{"text":"Britannica：1945诺奖（B343 交叉）。","source":"B343"}],
"reading":{"difficulties":["'塔拉'词义（毁坏——B343）。","智利—墨西哥的旅程诗（通说待核）。"],
 "editions":["《塔拉》中译本（人民文学等——通说待核）。","西班牙文原版。"],
 "order":"米斯特拉尔中期；与《荒凉》对读。"},
"pending":["篇目核对（B343未载）。","1938年出版（Buenos Aires说）待核。","'美洲'主题细节待核。"],
"sources":["B343"],"year_source":"B343","author_source":"B343","related_works":["huangliang","ershisou","jipusaiyaoqu"],
"svg":G("《塔拉》美洲之爱图",[{"title":"塔拉","text":"毁坏的命名（B343）","color":"antagonist"},{"title":"美洲","text":"大陆的爱（通说）","color":"main"},{"title":" broader","text":"兴趣的扩展（B343）","color":"gold"},{"title":"母性","text":"主题的延续（B343语境）","color":"family"}])},
# 8. 艾里森《影子与行动》
{"id":"yingziyuxingdong","title":"影子与行动","original_title":"Shadow and Act","region":"美国","era":"现当代","era_detail":"20世纪60年代",
"genre":"散文集","genre_group":"散文","language":"英语","author_id":"ellison","author_name":"拉尔夫·艾里森",
"year_display":"1964年（Britannica B334：Shadow and Act (1964)）","year_sort":1964,
"background":["Britannica（B334）：Shadow and Act (1964)——散文集（与 Going to the Territory (1986) 并列）。","Britannica（B334）：艾里森——Invisible Man——1953 National Book Award。","题材（通说待核）：文学、爵士与种族的随笔——'影子'与'行动'的双义。"],
"outline":["（通说待核）论爵士、论《看不见的人》的创作与批评回应。","（通说待核）'影子与行动'：非裔美国人经验的两面。"],
"characters":[{"name":"'我'","identity":"散文家","note":"（B334 语境）"}],
"themes":["爵士乐与文学（通说待核）。",
 "对'抗议小说'标签的拒绝（通说待核）。",
 "'影子'：书名的双关（通说待核）。"],
"influence":[{"text":"Britannica：Shadow and Act (1964)（B334）。","source":"B334"},{"text":"Britannica：'first Black author to win that honor'（B334 交叉）。","source":"B334"}],
"reading":{"difficulties":["爵士术语。","1950-60年代批评语境。"],
 "editions":["《影子与行动》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"艾里森散文首选；与《看不见的人》对读。"},
"pending":["篇目核对（B334未载）。","1964年出版（Random House说）待核。","'抗议小说'论战细节待核。"],
"sources":["B334"],"year_source":"B334","author_source":"B334","related_works":["kanbujian3","xiayicijiangshiliehuo","tuyuzhizideneizi"],
"svg":G("《影子与行动》双关结构图",[{"title":"影子","text":"看不见的人（书名）","color":"main"},{"title":"行动","text":"爵士的即兴（通说）","color":"gold"},{"title":"随笔","text":"批评的阵地（B334）","color":"family"},{"title":"标签","text":"'抗议小说'之辩（通说）","color":"antagonist"}])},
# 9. 汤婷婷《中国佬》
{"id":"zhongguolao","title":"中国佬","original_title":"China Men","region":"美国","era":"现当代","era_detail":"20世纪70年代末",
"genre":"长篇小说（混合文体）","genre_group":"小说","language":"英语","author_id":"kingston","author_name":"汤亭亭",
"year_display":"1980年（作者页注记：Britannica——中国佬 (1980)——美国图书奖）","year_sort":1980,
"background":["作者页注记：中国佬 (1980)——'美国图书奖（Britannica）'。","Britannica：汤婷婷——华裔美国作家（作者页语境——待核）。","题材（通说待核）：华裔移民男性四代——神话、历史与家族的编织。"],
"outline":["（通说待核）从'曾祖父'到'父亲'：内华达筑路与洗衣馆。","（通说待核）神话插入（鲁滨逊/屈原等——通说待核）。"],
"characters":[{"name":"曾祖父/高祖父/父亲","identity":"移民四代","note":"（通说待核）"}],
"themes":["华裔移民的'无名'史（通说待核）。",
 "神话与历史的编织（作者页语境）。",
 "'美国图书奖'（B注记）。"],
"influence":[{"text":"Britannica：China Men (1980)——美国图书奖（作者页注记）。","source":src_of('kingston')},{"text":"Britannica：《女勇士》为成名作（作者页交叉）。","source":src_of('kingston')}],
"reading":{"difficulties":["混合文体（神话+家史）。","华人移民法案史（通说待核）。"],
 "editions":["《中国佬》中译本（漓江等——通说待核）。","英文原版。"],
 "order":"汤亭亭第二作；与《女勇士》对读。"},
"pending":["代际人名核对（通说）。","1980年出版（Knopf说）待核。","'美国图书奖'（American Book Award——B注记）核对。"],
"sources":[src_of('kingston')],"year_source":src_of('kingston'),"author_source":src_of('kingston'),"related_works":["nvyongshi" if "nvyongshi" in existing else "kanbujian3","xiangtianhuhan","nongmin"],
"svg":G("《中国佬》四代结构图",[{"title":"四代","text":"移民的链条（通说）","color":"main"},{"title":"筑路","text":"内华达的铁轨（通说）","color":"antagonist"},{"title":"神话","text":"编织的插入（作者页语境）","color":"gold"},{"title":"无名","text":"史册的空白（通说）","color":"family"}])},
# 10. 尤涅斯库《国王死去》
{"id":"guowangsiq","title":"国王死去","original_title":"Le Roi se meurt","region":"法国","era":"现当代","era_detail":"20世纪60年代初",
"genre":"戏剧","genre_group":"戏剧","language":"法语","author_id":"ionesco","author_name":"欧仁·尤涅斯库",
"year_display":"1962年（Britannica B340：Exit the King (1962)——中译名待核）","year_sort":1962,
"background":["Britannica（B340）：Exit the King (1962)——剧作列表。","Britannica（B340）：尤涅斯库——荒诞派开创者之一；'theatre of derision'。","题材（通说待核）：国王贝朗热一世的90分钟死去——死亡作为倒数计时。"],
"outline":["（通说待核）王后玛尔戈的告别与王国的坍缩。","（通说待核）'90分钟'的死亡倒计时。"],
"characters":[{"name":"贝朗热一世","identity":"国王","note":"（通说待核）"},{"name":"玛尔戈王后","identity":"第一任王后","note":"（通说待核）"}],
"themes":["死亡的独角戏（通说待核）。",
 "'derision'的告别（B340：theatre of derision）。",
 "王权的崩塌（通说待核）。"],
"influence":[{"text":"Britannica：Exit the King (1962)（B340）。","source":"B340"},{"text":"Britannica：荒诞派开创者（B340 交叉）。","source":"B340"}],
"reading":{"difficulties":["死亡的舞台化。","与《犀牛》的对照。"],
 "editions":["《国王死去》中译名（《国王临终》两说——通说待核）。","法文原版。"],
 "order":"尤涅斯库中期；与《犀牛》《椅子》对读。"},
"pending":["贝朗热人名核对（通说）。","1962年首演细节待核。","'90分钟'结构待核。"],
"sources":["B340"],"year_source":"B340","author_source":"B340","related_works":["xiniu","yizi","toutougeonv"],
"svg":G("《国王死去》倒计时图",[{"title":"国王","text":"90分钟的死去（通说）","color":"main"},{"title":"王后","text":"告别的劝导（通说）","color":"gold"},{"title":"王国","text":"坍缩的疆域（通说）","color":"family"},{"title":"嘲讽","text":"'theatre of derision'（B340）","color":"antagonist"}])},
# 11. 布勒东《疯狂的爱》
{"id":"fengkuangdeai","title":"疯狂的爱","original_title":"L'Amour fou","region":"法国","era":"近代","era_detail":"20世纪30年代末",
"genre":"散文集","genre_group":"散文","language":"法语","author_id":"breton","author_name":"安德烈·布勒东",
"year_display":"1937年（Britannica B344：L'Amour fou (1937; Mad Love)——中译名待核）","year_sort":1937,
"background":["Britannica（B344）：L'Amour fou——'Mad Love'——作品列表。","Britannica（B344）：布勒东——超现实主义'chief promoter and one of the founders'。","题材（通说待核）：与神秘女子寻物之旅——'疯狂的爱'的对象化。"],
"outline":["（通说待核）布洛涅森林的寻物与'客观偶发'（objet à fonctionnement symbolique——通说待核）。","（通说待核）超现实主义爱情的宣言。"],
"characters":[{"name":"'我'","identity":"诗人","note":"（B344 语境）"}],
"themes":["'疯狂的爱'：超现实的爱情观（书名语境——通说待核）。",
 "'客观偶发'物的理论（通说待核）。",
 "自动写作的叙事化（B344 交叉）。"],
"influence":[{"text":"Britannica：L'Amour fou (1937)（B344）。","source":"B344"},{"text":"Britannica：超现实主义运动定位（B344 作者级）。","source":"B344"}],
"reading":{"difficulties":["' objet '理论术语。","巴黎的地形学。"],
 "editions":["《疯狂的爱》中译本（人民文学等——通说待核）。","法文原版。"],
 "order":"布勒东散文篇；与《娜佳》《磁场》对读。"},
"pending":["' objet à fonctionnement symbolique '术语核对（通说）。","1937年出版细节待核。","寻物之旅细节待核。"],
"sources":["B344"],"year_source":"B344","author_source":"B344","related_works":["najia","cichang","diyuzhiji"],
"svg":G("《疯狂的爱》寻物结构图",[{"title":"寻物","text":"客观的偶发（通说）","color":"gold"},{"title":"疯狂","text":"爱的超现实（书名）","color":"main"},{"title":"布洛涅森林","text":"巴黎的地形（通说）","color":"family"},{"title":"宣言","text":"爱情的诗学（通说）","color":"antagonist"}])},
# 12. 荷尔德林《恩培多克勒之死》
{"id":"enpeiduokele","title":"恩培多克勒之死","original_title":"Der Tod des Empedokles","region":"德国","era":"近代","era_detail":"18世纪90年代末",
"genre":"戏剧诗（未完成三稿）","genre_group":"戏剧","language":"德语","author_id":"holderlin","author_name":"弗里德里希·荷尔德林",
"year_display":"约1798年起（Britannica B338：Der Tod des Empedokles——begun c. 1798——first version nearly complete, fragments of 2nd and 3rd versions survive）","year_sort":1798,
"background":["Britannica（B338）：恩培多克勒之死——约1798年起——第一稿接近完成，第二、三稿存断片。","Britannica（B338）：荷尔德林——'a prophet of spiritual renewal, of \"the return of the gods\"'。","题材（通说待核）：哲学家恩培多克勒投身埃特纳火山——神人与民众的悲剧。"],
"outline":["（通说待核）恩培多克勒的放逐与民众的仰望。","（通说待核）火山之跳：'回归诸神'的终局。"],
"characters":[{"name":"恩培多克勒","identity":"哲学家","note":"（B338 书名人物）"},{"name":"民众","identity":"合唱","note":"（通说待核）"}],
"themes":["'神与人'的界限（通说待核）。",
 "火山的浪漫主义死亡（通说待核）。",
 "戏剧诗的三稿（B338：fragments of 2nd and 3rd versions）。"],
"influence":[{"text":"Britannica：三稿存断片（B338）。","source":"B338"},{"text":"Britannica：'uniquely expressive style'（B338 作者级）。","source":"B338"}],
"reading":{"difficulties":["三稿的版本比较。","前苏格拉底哲学语境。"],
 "editions":["《恩培多克勒之死》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"荷尔德林戏剧尝试；与《许珀里翁》对读。"},
"pending":["三稿年份（1797-1799说）待核。","'火山之死'传说细节待核。","希腊哲学原型（阿格里真托的恩培多克勒）待核。"],
"sources":["B338"],"year_source":"B338","author_source":"B338","related_works":["xuboliweng","mianbingyujiu","fushide"],
"svg":G("《恩培多克勒之死》火山结构图",[{"title":"恩培多克勒","text":"哲学家的自我神化（通说）","color":"main"},{"title":"火山","text":"回归的终点（通说）","color":"gold"},{"title":"三稿","text":"未完成的断片（B338）","color":"family"},{"title":"民众","text":"仰望与驱逐（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批48）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('shui','dingling','水'),('baixuehuanghou','andersen','白雪皇后'),('jiaoshi','charlotte-bronte','教师'),('zuihouguangshi','heller','最后时光'),('tangmosangte','burnsburns','汤姆·奥·桑特'),('dingxiang','elytis','定向'),('tala','gmistral','塔拉'),('yingziyuxingdong','ellison','影子与行动'),('zhongguolao','kingston','中国佬'),('guowangsiq','ionesco','国王死去'),('fengkuangdeai','breton','疯狂的爱'),('enpeiduokele','holderlin','恩培多克勒之死')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH48 DONE')
