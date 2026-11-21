# -*- coding: utf-8 -*-
"""批50：零成本 12 部（所有漂亮的马/丰饶之海/说吧记忆/一般之歌/境遇/上升的一切必将汇聚/向加泰罗尼亚致敬/纽约外史/奇鸟行状录/中国小说史略/童年/爱米丽雅·迦洛蒂）"""
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

S_MC, S_MI, S_NB, S_NE, S_MO, S_OC, S_OW, S_OW2, S_MU, S_LU, S_GK, S_LE = (src_of(x) for x in ['mccarthy','mishima','nabokov','neruda','montale','oconnor','orwell','ouwen','murakami','luxun','gorky','lessing'])
print('srcs ok')

works = [
# 1. 麦卡锡《所有漂亮的马》
{"id":"suoyoupiaoliangdema","title":"所有漂亮的马","original_title":"All the Pretty Horses","region":"美国","era":"近代","era_detail":"20世纪90年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mccarthy","author_name":"科马克·麦卡锡",
"year_display":"1992年（Britannica B328：All the Pretty Horses (1992)——'Won the National Book Award'）","year_sort":1992,
"background":["Britannica（B328）：All the Pretty Horses——'Won the National Book Award and National Book Critics Circle Award'——'a coming-of-age story of John Grady Cole, a Texan who travels to Mexico'——'more Hemingway- than Faulkner-influenced in style'。","Britannica（B328）：'The Border Trilogy (1992-98)'——'rewrote and challenged myths of the American West'。","题材（通说待核）：16岁的约翰·格雷迪·科尔与同伴骑马赴墨西哥牧场。"],
"outline":["（通说待核）德州少年的墨西哥牧场之梦与监狱之祸。","（通说待核）'边境三部曲'之首（B328）。"],
"characters":[{"name":"约翰·格雷迪·科尔","identity":"16岁德州人","note":"（B328：John Grady Cole——'a Texan who travels to Mexico'）"},{"name":"莱西·罗林斯","identity":"同伴","note":"（通说待核）"}],
"themes":["西部神话的改写（B328：Border Trilogy——rewrote and challenged myths）。",
 "成长小说（B328：coming-of-age）。",
 "海明威式文体（B328：more Hemingway- than Faulkner-influenced）。"],
"influence":[{"text":"Britannica：National Book Award（B328）。","source":"B328"},{"text":"Britannica：'brought McCarthy public fame'（B328）。","source":"B328"}],
"reading":{"difficulties":["西班牙语对白。","西部边境史。"],
 "editions":["《所有漂亮的马》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"麦卡锡大众入门；后接《穿越》《平原上的城市》。"},
"pending":["约翰·格雷迪/莱西人名核对（B328载John Grady Cole）。","1992年出版（Knopf说）待核。","'边境三部曲'卷次核对。"],
"sources":["B328"],"year_source":"B328","author_source":"B328","related_works":["xueseziwuxian","lu","nongmin"],
"svg":G("《所有漂亮的马》边境三部曲图",[{"title":"科尔","text":"16岁的德州人（B328）","color":"main"},{"title":"边境","text":"'三部曲'之首（B328）","color":"gold"},{"title":"墨西哥","text":"牧场之梦（通说）","color":"family"},{"title":"西部","text":"神话的改写（B328）","color":"antagonist"}])},
# 2. 三岛由纪夫《丰饶之海》
{"id":"fengraozhihai","title":"丰饶之海","original_title":"豊饒の海","region":"日本","era":"近代","era_detail":"20世纪60-70年代",
"genre":"长篇小说（四部曲）","genre_group":"小说","language":"日语","author_id":"mishima","author_name":"三岛由纪夫",
"year_display":"1965-70年（作者页注记：Britannica——丰饶之海四部曲（1965—70）——'which many consider his lasting achievement'）","year_sort":1965,
"background":["作者页注记：丰饶之海四部曲 (1965-70)——''许多视为其恒久成就'（Britannica：which many consider his lasting achievement）'。","Britannica：三岛由纪夫——1970年自戕（作者页语境——待核）。","题材（通说待核）：本多繁邦的四次轮回目击——春雪/奔马/晓寺/天人五衰。"],
"outline":["（通说待核）四部曲：轮回的清显与老本多的证词。","（通说待核）'天人五衰'的终局与'无智与无知'。"],
"characters":[{"name":"本多繁邦","identity":"见证者","note":"（通说待核）"},{"name":"松枝清显","identity":"第一部主角","note":"（通说待核）"}],
"themes":["轮回与虚无（书名语境——通说待核）。",
 "'恒久成就'（B注记）。",
 "四部曲的年龄对应（通说待核）。"],
"influence":[{"text":"Britannica：'many consider his lasting achievement'（作者页注记）。","source":S_MI},{"text":"Britannica：三岛由纪夫戏剧与小说（作者页交叉）。","source":S_MI}],
"reading":{"difficulties":["四部曲的轮回结构。","佛教与唯识论底色（通说待核）。"],
 "editions":["《丰饶之海》中译本（人民文学等——通说待核）。","日文原版。"],
 "order":"三岛收官之作；与《金阁寺》对读。"},
"pending":["四部曲卷名与年份核对（通说）。","本多/清显人名核对（通说）。","1970年11月25日交稿与自戕说待核。"],
"sources":[S_MI],"year_source":S_MI,"author_source":S_MI,"related_works":["jingulesi" if "jingulesi" in existing else "renshijian","xieyang","luoshengmen"],
"svg":G("《丰饶之海》轮回结构图",[{"title":"轮回","text":"四部的转世（通说）","color":"gold"},{"title":"本多","text":"见证的老人（通说）","color":"main"},{"title":"海","text":"'丰饶'的虚妄（书名）","color":"family"},{"title":"五衰","text":"天人五衰（通说）","color":"antagonist"}])},
# 3. 纳博科夫《说吧，记忆》
{"id":"shuobajiuyi","title":"说吧，记忆","original_title":"Speak, Memory","region":"美国","era":"近代","era_detail":"20世纪60年代",
"genre":"自传","genre_group":"散文","language":"英语（俄译）","author_id":"nabokov","author_name":"弗拉基米尔·纳博科夫",
"year_display":"1966年（作者页注记：Britannica——说吧，记忆（1966）——自传）","year_sort":1966,
"background":["作者页注记：说吧，记忆——'自传（Britannica 列举 Speak, Memory）'。","Britannica：纳博科夫——《洛丽塔》作者（作者页交叉）。","题材（通说待核）：俄国贵族童年的记忆百科——蝴蝶、象棋与流亡。"],
"outline":["（通说待核）十五篇记忆的'主题变奏'（通说待核——章节结构）。","（通说待核）'说吧，记忆'：时间的召唤。"],
"characters":[{"name":"纳博科夫","identity":"回忆者","note":"（通说待核）"}],
"themes":["记忆的艺术化（通说待核）。",
 "流亡与母语（作者页语境）。",
 "'时间的迷宫'（通说待核）。"],
"influence":[{"text":"Britannica：Speak, Memory（作者页注记）。","source":S_NB},{"text":"Britannica：《洛丽塔》1955（作者页交叉）。","source":S_NB}],
"reading":{"difficulties":["记忆的互文。","双语写作的转换。"],
 "editions":["《说吧，记忆》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"纳博科夫自传首选；与《洛丽塔》对读。"},
"pending":["章节结构核对（通说）。","1966年出版（Harper & Row说）待核。","1951年英文初版 Conclusive Evidence 待核。"],
"sources":[S_NB],"year_source":S_NB,"author_source":S_NB,"related_works":["luolita" if "luolita" in existing else "leiyu","zenodeyishi","moluoyi"],
"svg":G("《说吧，记忆》时间结构图",[{"title":"记忆","text":"艺术的召唤（书名）","color":"gold"},{"title":"童年","text":"俄国的贵族（通说）","color":"main"},{"title":"蝴蝶","text":"收藏的隐喻（通说）","color":"family"},{"title":"流亡","text":"双语的转换（作者页语境）","color":"antagonist"}])},
# 4. 聂鲁达《一般之歌》
{"id":"yibanzhige","title":"一般之歌","original_title":"Canto general","region":"智利","era":"近代","era_detail":"20世纪中叶",
"genre":"史诗","genre_group":"诗歌","language":"西班牙语","author_id":"neruda","author_name":"巴勃罗·聂鲁达",
"year_display":"1950年（作者页注记：Britannica——一般之歌（Canto general, 1950）——拉丁美洲史诗）","year_sort":1950,
"background":["作者页注记：一般之歌——'拉丁美洲史诗（Britannica）'。","Britannica：聂鲁达——1971诺奖（作者页交叉——待核）。","题材（通说待核）：15章的拉美史诗——从创世到当代政治。"],
"outline":["（通说待核）15章结构：美洲的植物、动物、征服者与解放者。","（通说待核）'一般之歌'：为大陆代言。"],
"characters":[{"name":"抒情'我'","identity":"大陆的代言人","note":"（通说待核）"}],
"themes":["拉丁美洲史诗（B注记）。",
 "政治诗歌的巅峰（通说待核）。",
 "'马丘比丘之巅'（通说待核——不采为引文）。"],
"influence":[{"text":"Britannica：Canto general (1950)——拉丁美洲史诗（作者页注记）。","source":S_NE},{"text":"Britannica：聂鲁达1971诺奖（作者页交叉——待核）。","source":S_NE}],
"reading":{"difficulties":["15章结构。","拉美史与原住民词汇。"],
 "editions":["《一般之歌》中译本（人民文学等——通说待核）。","西班牙文原版。"],
 "order":"聂鲁达史诗首选；与《二十首情诗》对读。"},
"pending":["15章篇名核对（通说）。","1950年出版（墨西哥说）待核。","'马丘比丘'篇细节待核。"],
"sources":[S_NE],"year_source":S_NE,"author_source":S_NE,"related_works":["ershisou","huangliang","diyuzhiji"],
"svg":G("《一般之歌》大陆史诗图",[{"title":"大陆","text":"拉美的史诗（B注记）","color":"main"},{"title":"15章","text":"创世到当下（通说）","color":"gold"},{"title":"政治","text":"诗人的选择（通说）","color":"antagonist"},{"title":"马丘比丘","text":"高原的巅峰（通说）","color":"family"}])},
# 5. 蒙塔莱《境遇》
{"id":"jingyu","title":"境遇","original_title":"Le occasioni","region":"意大利","era":"近代","era_detail":"20世纪30年代末",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"montale","author_name":"埃乌杰尼奥·蒙塔莱",
"year_display":"1939年（Britannica B341：Le occasioni (1939)——中译名待核）","year_sort":1939,
"background":["Britannica（B341）：Le occasioni (1939)——蒙塔莱代表作序列（B341：'progressively more introverted and obscure'）。","Britannica（B341）：蒙塔莱——1975诺奖；隐逸派。","题材（通说待核）：《达莉亚》等——'克拉夫蒂娅'（Clizia）与'沃尔夫'意象。"],
"outline":["（通说待核）'境遇'：记忆中的'克拉夫蒂娅'与利古里亚。","（通说待核）'蛇'与'鹰'的动物意象（通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"隐逸诗人","note":"（B341 语系）"}],
"themes":["'隐逸派'的深化（B341：more introverted and obscure）。",
 "'境遇'：个人记忆的客观化（书名语境——通说待核）。",
 "反法西斯年代的诗（通说待核）。"],
"influence":[{"text":"Britannica：Le occasioni (1939)（B341）。","source":"B341"},{"text":"Britannica：1975诺奖（B341 交叉）。","source":"B341"}],
"reading":{"difficulties":["'克拉夫蒂娅'等私人代号。","隐逸派的晦涩升级。"],
 "editions":["《境遇》中译名（《 occasions》）待核。","意大利文原版。"],
 "order":"蒙塔莱中期；后接《萨图拉》。"},
"pending":["'克拉夫蒂娅'原型（Irma Brandeis说）待核。","1939年出版（Einaudi说）待核。","篇目核对（B341未载）。"],
"sources":["B341"],"year_source":"B341","author_source":"B341","related_works":["wuguigu","shunxijiandeyewan","ezhihua"],
"svg":G("《境遇》记忆客观化图",[{"title":"境遇","text":"记忆的场合（书名）","color":"main"},{"title":"克拉夫蒂娅","text":"私人代号（通说）","color":"gold"},{"title":"晦涩","text":"'更内省与晦涩'（B341）","color":"antagonist"},{"title":"利古里亚","text":"海岸的底片（通说）","color":"family"}])},
# 6. 奥康纳《上升的一切必将汇聚》
{"id":"shangshengdeyiqie","title":"上升的一切必将汇聚","original_title":"Everything That Rises Must Converge","region":"美国","era":"近代","era_detail":"20世纪60年代",
"genre":"短篇小说集","genre_group":"故事集","language":"英语","author_id":"oconnor","author_name":"弗兰纳里·奥康纳",
"year_display":"1965年（Britannica B291：Everything That Rises Must Converge (1965)）","year_sort":1965,
"background":["Britannica（B291）：Everything That Rises Must Converge (1965)——短篇集。","Britannica（B291）：奥康纳——《暴力夺取》(B291)与《慧血》(B291)作者——南方哥特。","题材（通说待核）：同名篇——朱利安与母亲的公交对峙——南方种族的降卑。"],
"outline":["（通说待核）朱利安陪母亲上'减肥班'——黑人大妈与礼帽的冒犯。","（通说待核）'汇聚'：一切上升的将汇聚——德日进式标题（通说待核）。"],
"characters":[{"name":"朱利安","identity":"儿子","note":"（通说待核）"},{"name":"母亲","identity":"南方老太太","note":"（通说待核）"}],
"themes":["南方种族的'汇聚'（书名语境——通说待核）。",
 "救赎与恩典的暴力（B291 作者级语境）。",
 "哥特式反讽（B291 语系）。"],
"influence":[{"text":"Britannica：Everything That Rises Must Converge (1965)（B291）。","source":"B291"},{"text":"Britannica：奥康纳'暴力夺取'的救赎观（B291 交叉——待核）。","source":"B291"}],
"reading":{"difficulties":["'汇聚'的神学标题（德日进说待核）。","1960年代南方种族语境。"],
 "editions":["《上升的一切必将汇聚》中译本（新星/上海译文等——通说待核）。","英文原版。"],
 "order":"奥康纳短篇收官；与《慧血》对读。"},
"pending":["篇目（9篇说）核对（通说）。","1965年身后出版细节待核。","'德日进'标题来源待核。"],
"sources":["B291"],"year_source":"B291","author_source":"B291","related_works":["huixue","xinshigudeLieshou","shangxinkafeizhige"],
"svg":G("《上升的一切必将汇聚》汇聚结构图",[{"title":"汇聚","text":"上升的终局（书名）","color":"gold"},{"title":"公交","text":"种族的对峙（通说）","color":"main"},{"title":"恩典","text":"暴力的救赎（B291语境）","color":"family"},{"title":"南方","text":"1960年代（通说）","color":"antagonist"}])},
# 7. 奥威尔《向加泰罗尼亚致敬》
{"id":"xiangjiataeluniyazhijing","title":"向加泰罗尼亚致敬","original_title":"Homage to Catalonia","region":"英国","era":"近代","era_detail":"20世纪30年代末",
"genre":"纪实文学","genre_group":"散文","language":"英语","author_id":"orwell","author_name":"乔治·奥威尔",
"year_display":"1938年（作者页注记：Britannica——向加泰罗尼亚致敬 (1938)——非虚构）","year_sort":1938,
"background":["作者页注记：向加泰罗尼亚致敬——'（Britannica 列举 1938）'——非虚构与随笔。","Britannica：奥威尔——《一九八四》《动物农场》作者（作者页交叉）。","题材（通说待核）：西班牙内战中的民兵经历——斯大林派与统一社会党的内讧。"],
"outline":["（通说待核）奥威尔赴西班牙参战与喉部中弹。","（通说待核）五月事变与'托派'的清洗。"],
"characters":[{"name":"奥威尔","identity":"民兵/记者","note":"（通说待核）"}],
"themes":["革命的内讧（通说待核）。",
 "'诚实报告'的非虚构伦理（作者页语境——待核）。",
 "《一九八四》的前史（作者页交叉）。"],
"influence":[{"text":"Britannica：Homage to Catalonia (1938)（作者页注记）。","source":S_OW},{"text":"Britannica：奥威尔散文'Politics and the English Language'（作者页注记——并列）。","source":S_OW}],
"reading":{"difficulties":["西班牙内战各派系。","非虚构的第一人称。"],
 "editions":["《向加泰罗尼亚致敬》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"奥威尔非虚构首选；与《一九八四》对读。"},
"pending":["派系细节核对（POUM说——通说）。","1938年出版细节待核。","喉部中弹细节待核。"],
"sources":[S_OW],"year_source":S_OW,"author_source":S_OW,"related_works":["yibajiusi" if "yibajiusi" in existing else "kanbujian3","sangeshibing","renshijian"],
"svg":G("《向加泰罗尼亚致敬》内战结构图",[{"title":"民兵","text":"战壕的冬天（通说）","color":"main"},{"title":"内讧","text":"革命的自相残杀（通说）","color":"antagonist"},{"title":"致敬","text":"非虚构的诚实（书名）","color":"gold"},{"title":"一九八四","text":"先声（作者页交叉）","color":"family"}])},
# 8. 欧·文《纽约外史》
{"id":"niuyuewaishi","title":"纽约外史","original_title":"A History of New York","region":"美国","era":"近代","era_detail":"19世纪初",
"genre":"讽刺小说","genre_group":"小说","language":"英语","author_id":"ouwen","author_name":"华盛顿·欧文",
"year_display":"1809年（Britannica B318：纽约外史 (1809)）","year_sort":1809,
"background":["Britannica（B318）：A History of New York——欧文作品（作者页：jianWenzhaji 交叉——见闻札记）。","Britannica（B318）：欧文——美国文学之父说（作者页语境——待核）。","题材（通说待核）：'迪特里希·尼克博克'署名——荷兰殖民纽约的伪史戏仿。"],
"outline":["（通说待核）尼克博克的'荷裔纽约史'：第一至七卷。","（通说待核）' harassing'（——通说待核）的滑稽史官腔。"],
"characters":[{"name":"迪特里希·尼克博克","identity":"伪作者","note":"（通说待核）"},{"name":"彼得·施托伊弗桑特","identity":"总督","note":"（通说待核）"}],
"themes":["伪史的戏仿（通说待核）。",
 "荷兰裔纽约的记忆（通说待核）。",
 "'美国文学的独立'（作者页语境——待核）。"],
"influence":[{"text":"Britannica：A History of New York (1809)（B318）。","source":"B318"},{"text":"Britannica：《见闻札记》为代表作（B318 交叉）。","source":"B318"}],
"reading":{"difficulties":["18-19世纪纽约史。","'尼克博克'叙述腔。"],
 "editions":["《纽约外史》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"欧文早期；先于《见闻札记》。"},
"pending":["1809年出版细节待核。","尼克博克人名核对（通说）。","'美国文学之父'定位待核（B318口径）。"],
"sources":["B318"],"year_source":"B318","author_source":"B318","related_works":["jianWenzhaji","naikesibotezhiye" if "naikesibotezhiye" in existing else "leiyu","tangjihuade"],
"svg":G("《纽约外史》伪史结构图",[{"title":"尼克博克","text":"伪史的作者（通说）","color":"gold"},{"title":"纽约","text":"荷兰裔的记忆（书名）","color":"main"},{"title":"戏仿","text":"滑稽的史官腔（通说）","color":"antagonist"},{"title":"独立","text":"美国文学的起点（B318语境）","color":"family"}])},
# 9. 村上春树《奇鸟行状录》
{"id":"qiniaoxingzhuanglu","title":"奇鸟行状录","original_title":"ねじまき鳥クロニクル","region":"日本","era":"现当代","era_detail":"20世纪90年代",
"genre":"长篇小说","genre_group":"小说","language":"日语","author_id":"murakami","author_name":"村上春树",
"year_display":"1994-95年（作者页注记：Britannica——奇鸟行状录（1994—95））","year_sort":1994,
"background":["作者页注记：奇鸟行状录——'（Britannica 列举 1994—95）'。","Britannica：村上春树——当代日本作家（作者页语境）。","题材（通说待核）：冈田亨与拧发条鸟——井底的沉思与诺门罕战役的阴影。"],
"outline":["（通说待核）妻子的失踪与拧发条鸟的叫声。","（通说待核）诺门罕的历史地狱与井下的通道。"],
"characters":[{"name":"冈田亨","identity":"失业者","note":"（通说待核，Britannica未载）"},{"name":"久美子","identity":"妻子","note":"（通说待核）"}],
"themes":["历史创伤的通道（通说待核）。",
 "'拧发条鸟'的声音（书名语境——通说待核）。",
 "从都市独白到历史叙事（作者页语境）。"],
"influence":[{"text":"Britannica：奇鸟行状录 (1994-95)（作者页注记）。","source":S_MU},{"text":"Britannica：《挪威的森林》为代表作（作者页交叉）。","source":S_MU}],
"reading":{"difficulties":["三部结构（日语三卷说）。","诺门罕战役史。"],
 "editions":["《奇鸟行状录》中译本（上海译文等——通说待核）。","日文原版。"],
 "order":"村上中期首选；与《海边的卡夫卡》对读。"},
"pending":["冈田亨/久美子人名核对（通说）。","三卷年份（1994/1995）核对。","'拧发条鸟'意象细节待核。"],
"sources":[S_MU],"year_source":S_MU,"author_source":S_MU,"related_works":["haiBiandekafuka" if "haiBiandekafuka" in existing else "leiyu","nuoweidesenlin" if "nuoweidesenlin" in existing else "kanbujian3","moluoyi"],
"svg":G("《奇鸟行状录》井底结构图",[{"title":"拧发条鸟","text":"声音的引路（书名）","color":"gold"},{"title":"井底","text":"沉思的通道（通说）","color":"main"},{"title":"诺门罕","text":"历史的创伤（通说）","color":"antagonist"},{"title":"失踪","text":"妻子的缺席（通说）","color":"family"}])},
# 10. 鲁迅《中国小说史略》
{"id":"xiaoshuoshilue","title":"中国小说史略","original_title":"中国小说史略","region":"中国","era":"近代","era_detail":"20世纪20年代初",
"genre":"学术专著","genre_group":"散文","language":"汉语（文言）","author_id":"luxun","author_name":"鲁迅",
"year_display":"1923-24年（作者页注记：Britannica——中国小说史略 (1923—24)——'中国小说史研究的奠基之作'）","year_sort":1923,
"background":["作者页注记：中国小说史略 (1923-24)——'中国小说史研究的奠基之作（Britannica）'。","Britannica：鲁迅——现代中国文学奠基人（作者页语境）。","题材（通说待核）：28篇的讲义——从神话传说到清末谴责小说。"],
"outline":["（通说待核）讲义体：神话→六朝志怪→唐传奇→宋话本→明清小说。","（通说待核）'史略'的分期框架。"],
"characters":[{"name":"（学术专著无人物）","identity":"——","note":"文学史"}],
"themes":["小说史的开创（B注记：奠基之作）。",
 "文言讲义体（通说待核）。",
 "明清小说的谱系（《红楼梦》论——通说待核）。"],
"influence":[{"text":"Britannica：'奠基之作'（作者页注记）。","source":S_LU},{"text":"Britannica：鲁迅《狂人日记》为现代小说开端（作者页交叉——待核）。","source":S_LU}],
"reading":{"difficulties":["文言讲义体。","古代小说的版本知识。"],
 "editions":["《中国小说史略》（人民文学出版社《鲁迅全集》等——通说待核）。","1923-24年北大讲义本说待核。"],
 "order":"鲁迅学术首选；与《中国小说的历史的变迁》对读。"},
"pending":["28篇结构核对（通说）。","1923-24年出版（北大新潮社说）待核。","'奠基之作'评价出处核对。"],
"sources":[S_LU],"year_source":S_LU,"author_source":S_LU,"related_works":["kuangrenriji" if "kuangrenriji" in existing else "leiyu","shui","nongmin"],
"svg":G("《中国小说史略》谱系结构图",[{"title":"小说史","text":"奠基的框架（B注记）","color":"main"},{"title":"志怪传奇","text":"六朝到唐（通说）","color":"gold"},{"title":"讲义体","text":"文言的课堂（通说）","color":"family"},{"title":"五四","text":"白话的对照（作者页语境）","color":"antagonist"}])},
# 11. 高尔基《童年》
{"id":"tongnian","title":"童年","original_title":"Детство","region":"俄国","era":"近代","era_detail":"20世纪10年代",
"genre":"自传小说","genre_group":"小说","language":"俄语","author_id":"gorky","author_name":"马克西姆·高尔基",
"year_display":"作者页注记：Britannica——自传三部曲——'one of the finest autobiographies in Russian literature'（年份通说待核——1913-14说）","year_sort":1913,
"background":["作者页注记：童年/在人间/我的大学——'自传三部曲（Britannica：one of the finest autobiographies in Russian literature）'。","Britannica：高尔基——俄国作家（作者页语境）。","题材（通说待核）：阿列克谢的童年——外祖父的染坊与外祖母的民间故事。"],
"outline":["（通说待核）阿列克谢·彼什科夫的童年：暴力与温暖的日常。","（通说待核）外祖母的民间故事与'善'的教育。"],
"characters":[{"name":"阿列克谢","identity":"叙述者（童年高尔基）","note":"（通说待核）"},{"name":"外祖母","identity":"民间故事的讲述者","note":"（通说待核）"}],
"themes":["自传三部曲之首（B注记：自传三部曲）。",
 "'俄国文学最优秀的自传之一'（B注记引语）。",
 "民间叙事的教育（通说待核）。"],
"influence":[{"text":"Britannica：'one of the finest autobiographies in Russian literature'（作者页注记）。","source":S_GK},{"text":"Britannica：高尔基三部曲（作者页注记）。","source":S_GK}],
"reading":{"difficulties":["自传与小说的边界。","伏尔加河下层生活。"],
 "editions":["《童年》中译本（人民文学等——通说待核）。","俄文原版（公有领域状态待核）。"],
 "order":"三部曲之首；后接《在人间》《我的大学》。"},
"pending":["三部曲年份（1913-1922说）核对。","阿列克谢/外祖母人名核对（通说）。","'最优秀的自传'评价（B注记引语）核对。"],
"sources":[S_GK],"year_source":S_GK,"author_source":S_GK,"related_works":["zaidiceng","muqin","nongmin"],
"svg":G("《童年》民间叙事图",[{"title":"染坊","text":"暴力的日常（通说）","color":"antagonist"},{"title":"外祖母","text":"故事的暖流（通说）","color":"gold"},{"title":"阿列克谢","text":"童年的眼睛（通说）","color":"main"},{"title":"自传","text":"三部曲之首（B注记）","color":"family"}])},
# 12. 莱辛《爱米丽雅·迦洛蒂》
{"id":"aimiliyajialuoti","title":"爱米丽雅·迦洛蒂","original_title":"Emilia Galotti","region":"德国","era":"近代","era_detail":"18世纪70年代初",
"genre":"悲剧","genre_group":"戏剧","language":"德语","author_id":"lessing","author_name":"戈特霍尔德·埃夫莱姆·莱辛",
"year_display":"1772年（Britannica B368：Emilia Galotti (1772)）","year_sort":1772,
"background":["Britannica（B368）：Emilia Galotti (1772)——剧作列表。","Britannica（B368）：莱辛——'plays of lasting importance'。","题材（通说待核）：亲王赫托勒的强权——爱米丽雅以死守贞。"],
"outline":["（通说待核）亲王劫婚的阴谋与'死'的选择。","（通说待核）父权与贞洁的市民悲剧。"],
"characters":[{"name":"爱米丽雅","identity":"市民之女","note":"（B368 书名人物）"},{"name":"亲王赫托勒","identity":"施暴的权力","note":"（通说待核）"}],
"themes":["市民悲剧（B368：bürgerliches Trauerspiel 语系）。",
 "权力对平民的觊觎（通说待核）。",
 "'以死守贞'的启蒙批判（通说待核）。"],
"influence":[{"text":"Britannica：Emilia Galotti (1772)（B368）。","source":"B368"},{"text":"Britannica：莱辛戏剧序列（B368 作者级）。","source":"B368"}],
"reading":{"difficulties":["18世纪意大利背景（小说原型说）。","'市民悲剧'的形式。"],
 "editions":["《爱米丽雅·迦洛蒂》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"莱辛悲剧首选；与《智者纳坦》对读。"},
"pending":["爱米丽雅/亲王人名核对（通说）。","1772年首演（不伦瑞克说）待核。","'小说原型'（《教士》说）待核。"],
"sources":["B368"],"year_source":"B368","author_source":"B368","related_works":["zhainazhitan","laokong","yinmouyuaiqing"],
"svg":G("《爱米丽雅·迦洛蒂》权力结构图",[{"title":"亲王","text":"强权的觊觎（通说）","color":"antagonist"},{"title":"爱米丽雅","text":"'以死守贞'（通说）","color":"main"},{"title":"父亲","text":"市民的无力（通说）","color":"family"},{"title":"悲剧","text":"市民的形式（B368语系）","color":"gold"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批50）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('suoyoupiaoliangdema','mccarthy','所有漂亮的马'),('fengraozhihai','mishima','丰饶之海'),('shuobajiuyi','nabokov','说吧，记忆'),('yibanzhige','neruda','一般之歌'),('jingyu','montale','境遇'),('shangshengdeyiqie','oconnor','上升'),('xiangjiataeluniyazhijing','orwell','向加泰罗尼亚致敬'),('niuyuewaishi','ouwen','纽约外史'),('qiniaoxingzhuanglu','murakami','奇鸟行状录'),('xiaoshuoshilue','luxun','中国小说史略'),('tongnian','gorky','童年'),('aimiliyajialuoti','lessing','爱米丽雅')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH50 DONE')
