# -*- coding: utf-8 -*-
"""批46：零成本 10 部（地下室手记/四个四重奏/在底层/斜阳/莎菲女士的日记/三个士兵/古斯泰·贝林/诗歌集/诗艺/面饼与酒）"""
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

S_DO, S_EL, S_GO, S_DA, S_DI, S_DP, S_LA, S_HE, S_HO, S_HO2 = (src_of(x) for x in ['dostoevsky','eliot','gorky','dazaiosamu','dingling','dospassos','lagerlof','heine','horace','holderlin'])
print('srcs:', S_DO, S_EL, S_GO, S_DA, S_DI, S_DP, S_LA, S_HE, S_HO, S_HO2)

works = [
# 1. 陀思妥耶夫斯基《地下室手记》
{"id":"dixiashishouji","title":"地下室手记","original_title":"Записки из подполья","region":"俄国","era":"近代","era_detail":"19世纪60年代",
"genre":"中篇小说","genre_group":"小说","language":"俄语","author_id":"dostoevsky","author_name":"费奥多尔·陀思妥耶夫斯基",
"year_display":"1864年（作者页注记：Britannica——地下室手记 (1864)——'挑战决定论与空想社会主义'——存在主义先声）","year_sort":1864,
"background":["作者页注记：地下室手记 (1864)——'挑战决定论与空想社会主义'（Britannica）——存在主义先声。","Britannica：陀思妥耶夫斯基——俄国小说家（作者页语境）。","题材（通说待核）：'地下室人'的两部分自白——自我意识的自虐与'二二得四'的算术反叛。"],
"outline":["（通说待核）第一部分：'地下室人'的哲学独白——反对水晶宫。","（通说待核）第二部分：丽莎与雪中追悔的往事。"],
"characters":[{"name":"'地下室人'","identity":"退休公务员","note":"（通说待核，Britannica未载）"},{"name":"丽莎","identity":"妓女","note":"（通说待核）"}],
"themes":["自由意志对决定论的反叛（Britannica 注记：挑战决定论）。",
 "自我意识的病态（通说待核）。",
 "存在主义先声（Britannica 注记）。"],
"influence":[{"text":"Britannica：'挑战决定论与空想社会主义'（作者页注记）。","source":S_DO},{"text":"Britannica：陀思妥耶夫斯基为'人类灵魂的伟大审问者'说待核（不采）。","source":S_DO}],
"reading":{"difficulties":["独白体的自我矛盾。","1860年代俄国虚无主义语境（通说待核）。"],
 "editions":["《地下室手记》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"陀氏思想门槛；后接《罪与罚》。"},
"pending":["人物名（地下室人/丽莎）核对（通说）。","1864年发表（《时代》杂志说）待核。","'水晶宫'指涉（车尔尼雪夫斯基说）待核。"],
"sources":[S_DO],"year_source":S_DO,"author_source":S_DO,"related_works":["zuoyufa","baichi","renshijian"],
"svg":G("《地下室手记》反叛结构图",[{"title":"地下室","text":"'我'的洞穴（通说）","color":"main"},{"title":"二二得四","text":"算术的反叛（通说）","color":"gold"},{"title":"水晶宫","text":"决定论的靶子（Britannica注记）","color":"antagonist"},{"title":"丽莎","text":"雪中的羞耻（通说）","color":"family"}])},
# 2. 艾略特《四个四重奏》
{"id":"sigesizhongzou","title":"四个四重奏","original_title":"Four Quartets","region":"英国","era":"近代","era_detail":"20世纪40年代",
"genre":"组诗","genre_group":"诗歌","language":"英语","author_id":"eliot","author_name":"T.S.艾略特",
"year_display":"1943年（作者页注记：Britannica——四个四重奏 (1943)——'considered his masterpiece'）","year_sort":1943,
"background":["作者页注记：四个四重奏 (1943)——'considered his masterpiece'（Britannica）。","Britannica：艾略特——1948诺奖（作者页语境——待核）。","题材（通说待核）：《焚毁的诺顿》《东库克》《干塞尔维吉斯》《小吉丁》——时间与永恒的四重奏。"],
"outline":["（通说待核）四首组诗的'现在与过去'时间冥想。","（通说待核）'旋转门'与'火与玫瑰'的终点。"],
"characters":[{"name":"冥想之'我'","identity":"诗人","note":"（通说待核）"}],
"themes":["时间的哲学（书名语境——通说待核）。",
 "'现在时间与过去时间'开篇（通说待核——不直接引文）。",
 "宗教沉思的晚期艾略特（通说待核）。"],
"influence":[{"text":"Britannica：'considered his masterpiece'（作者页注记）。","source":S_EL},{"text":"Britannica：《荒原》为其成名作（作者页交叉）。","source":S_EL}],
"reading":{"difficulties":["组诗的互文结构。","基督教神秘主义语境（通说待核）。"],
 "editions":["《四个四重奏》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"艾略特晚期首选；与《荒原》对读。"},
"pending":["四首标题与年份（1935-1942分别发表说）核对。","1943年结集细节待核。","'杰作'评价出处（Britannica 注记）核对。"],
"sources":[S_EL],"year_source":S_EL,"author_source":S_EL,"related_works":["huangyuan2" if "huangyuan2" in existing else "kanbujian3","wuguigu","diyuzhiji"],
"svg":G("《四个四重奏》时间结构图",[{"title":"诺顿","text":"时间的大门（通说）","color":"main"},{"title":"四重奏","text":"音乐的对应（书名）","color":"gold"},{"title":"永恒","text":"时间的交叉点（通说）","color":"family"},{"title":"杰作","text":"Britannica 之评（B注记）","color":"antagonist"}])},
# 3. 高尔基《在底层》
{"id":"zaidiceng","title":"在底层","original_title":"На дне（The Lower Depths）","region":"俄国","era":"近代","era_detail":"20世纪初",
"genre":"戏剧","genre_group":"戏剧","language":"俄语","author_id":"gorky","author_name":"马克西姆·高尔基",
"year_display":"1902年（作者页注记：Britannica——The Lower Depths (1902)）","year_sort":1902,
"background":["作者页注记：在底层——'戏剧（Britannica：The Lower Depths (1902)）'。","Britannica：高尔基——俄国作家、'社会主义现实主义'命名者（作者页语境——待核）。","题材（通说待核）：科斯蒂廖夫的地下室客栈——流浪汉们的'人'之辩论。"],
"outline":["（通说待核）鲁卡的出现：谎言的安慰与真相的残忍。","（通说待核）'人——这声音听起来多么骄傲'（通说待核——不直接引文）。"],
"characters":[{"name":"鲁卡","identity":"流浪朝圣者","note":"（通说待核，Britannica未载）"},{"name":"沙金","identity":"赌徒","note":"（通说待核）"}],
"themes":["安慰性的谎言 vs 残酷的真理（通说待核）。",
 "'底层'的社会档案（书名语境）。",
 "'人'的颂歌与虚无（通说待核）。"],
"influence":[{"text":"Britannica：The Lower Depths (1902)（作者页注记）。","source":S_GO},{"text":"Britannica：高尔基戏剧序列（作者页语境）。","source":S_GO}],
"reading":{"difficulties":["群像戏的'潜台词'。","1902年俄国社会语境。"],
 "editions":["《在底层》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"高尔基戏剧首选；与《母亲》对读。"},
"pending":["鲁卡/沙金人名核对（通说）。","1902年首演（莫斯科艺术剧院说）待核。","'人'的台词核对（不采为引文）。"],
"sources":[S_GO],"year_source":S_GO,"author_source":S_GO,"related_works":["muqin","haiou","sanzimei"],
"svg":G("《在底层》地下室客栈图",[{"title":"地下室","text":"社会的底层（书名）","color":"antagonist"},{"title":"鲁卡","text":"谎言的安慰（通说）","color":"gold"},{"title":"沙金","text":"真理的辩才（通说）","color":"main"},{"title":"'人'","text":"骄傲与虚无（通说）","color":"family"}])},
# 4. 太宰治《斜阳》
{"id":"xieyang","title":"斜阳","original_title":"斜陽","region":"日本","era":"近代","era_detail":"20世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"日语","author_id":"dazaiosamu","author_name":"太宰治",
"year_display":"1947年（作者页注记：Britannica——斜阳 1947年）","year_sort":1947,
"background":["作者页注记：斜阳——'1947年（Britannica）'。","Britannica：太宰治——'私小说'传统（作者页语境——待核）。","题材（通说待核）：没落贵族的战后——加子的日记与'斜阳族'。"],
"outline":["（通说待核）加子与母亲：战后贵族的优雅与凋零。","（通说待核）弟弟直治的自杀与'斜阳'意象。"],
"characters":[{"name":"加子","identity":"日记叙述者","note":"（通说待核，Britannica未载）"},{"name":"直治","identity":"弟弟","note":"（通说待核）"}],
"themes":["贵族制的没落（通说待核）。",
 "'斜阳族'：战后的身份（通说待核——词源为本作）。",
 "私小说的血肉（作者页语境）。"],
"influence":[{"text":"Britannica：斜阳 (1947)（作者页注记）。","source":S_DA},{"text":"Britannica：《人间失格》为代表作（作者页交叉）。","source":S_DA}],
"reading":{"difficulties":["战后日本贵族制。","日记体与私小说传统。"],
 "editions":["《斜阳》中译本（人民文学/上海译文等——通说待核）。","日文原版（公有领域状态待核）。"],
 "order":"太宰治第二代表作；与《人间失格》对读。"},
"pending":["加子/直治人名核对（通说）。","1947年发表（《新潮》说）待核。","'斜阳族'成为流行语的细节待核。"],
"sources":[S_DA],"year_source":S_DA,"author_source":S_DA,"related_works":["renshijian","luoshengmen","hetong"],
"svg":G("《斜阳》没落结构图",[{"title":"斜阳","text":"贵族的余晖（书名）","color":"gold"},{"title":"加子","text":"日记的优雅（通说）","color":"main"},{"title":"直治","text":"弟弟的自杀（通说）","color":"antagonist"},{"title":"战后","text":"身份的崩塌（通说）","color":"family"}])},
# 5. 丁玲《莎菲女士的日记》
{"id":"shafeinushideriji","title":"莎菲女士的日记","original_title":"莎菲女士的日记","region":"中国","era":"近代","era_detail":"20世纪20年代末",
"genre":"短篇小说","genre_group":"小说","language":"汉语","author_id":"dingling","author_name":"丁玲",
"year_display":"1928年（作者页注记：Britannica 语境——成名作）","year_sort":1928,
"background":["作者页注记：莎菲女士的日记 (1928)——'成名作（Britannica 语境）'。","Britannica：丁玲——现代中国女作家（作者页语境）。","题材（通说待核）：日记体——病中莎菲对凌吉士的欲望与蔑视。"],
"outline":["（通说待核）莎菲的日记：肺病疗养的冬春。","（通说待核）'灵与肉'的分裂与胜利的颓然。"],
"characters":[{"name":"莎菲","identity":"病中女学生","note":"（通说待核）"},{"name":"凌吉士","identity":"南洋侨生","note":"（通说待核）"}],
"themes":["女性欲望的大胆书写（通说待核）。",
 "日记体的内心独白（通说待核）。",
 "'五四'之后的个性解放（作者页语境）。"],
"influence":[{"text":"Britannica：丁玲成名作（作者页注记）。","source":S_DI},{"text":"Britannica：丁玲《太阳照在桑干河上》获斯大林奖说（作者页交叉——待核）。","source":S_DI}],
"reading":{"difficulties":["日记体的时间碎片。","1928年北京公寓语境（通说待核）。"],
 "editions":["《莎菲女士的日记》（人民文学出版社《丁玲全集》等——通说待核）。","1928年《小说月报》说待核。"],
 "order":"丁玲成名作；与《水》《太阳照在桑干河上》对照。"},
"pending":["莎菲/凌吉士人名核对（通说）。","1928年发表（《小说月报》说）待核。","'成名作'评价（Britannica 语境）核对。"],
"sources":[S_DI],"year_source":S_DI,"author_source":S_DI,"related_works":["shui" if "shui" in existing else "kanbujian3","cheng","rensheng"],
"svg":G("《莎菲女士的日记》欲望结构图",[{"title":"莎菲","text":"病中的日记（通说）","color":"main"},{"title":"凌吉士","text":"'卑劣的灵魂'（通说）","color":"antagonist"},{"title":"欲望","text":"灵与肉的分裂（通说）","color":"gold"},{"title":"日记","text":"女性的声音（通说）","color":"family"}])},
# 6. 多斯·帕索斯《三个士兵》
{"id":"sangeshibing","title":"三个士兵","original_title":"Three Soldiers","region":"美国","era":"近代","era_detail":"20世纪20年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"dospassos","author_name":"约翰·多斯·帕索斯",
"year_display":"1921年（Britannica B347：Three Soldiers (1921)——反战）","year_sort":1921,
"background":["Britannica（B347）：Three Soldiers——反战小说（antiwar novel）。","Britannica（B347）：多斯·帕索斯——一战救护车志愿司机（作者页交叉）。","题材（通说待核）：三个美国士兵在法国——战争机器的碾磨。"],
"outline":["（通说待核）三人各自的战场轨迹与幻灭。","（通说待核）'军队'作为非人化机器。"],
"characters":[{"name":"安德鲁斯等三人","identity":"美国士兵","note":"（通说待核，B347未载人名）"}],
"themes":["反战（B347：antiwar novel）。",
 "军事机器的非人化（通说待核）。",
 "艺术家的战争（通说待核）。"],
"influence":[{"text":"Britannica：Three Soldiers (1921)——antiwar novel（B347）。","source":"B347"},{"text":"Britannica：U.S.A. 的前奏（B347 语境）。","source":"B347"}],
"reading":{"difficulties":["一战美军后勤史。","三人视角的交替。"],
 "editions":["《三个士兵》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"多斯·帕索斯首作；后接《曼哈顿中转站》。"},
"pending":["三人名核对（通说：Andrews/Fuselli/Carroll说）。","1921年出版细节待核。","'反战'评价（B347）核对。"],
"sources":["B347"],"year_source":"B347","author_source":"B347","related_works":["manhadundian","meiguobuqu","sanjunsheng" if "sanjunsheng" in existing else "laorenhai"],
"svg":G("《三个士兵》反战结构图",[{"title":"三人","text":"战争的三个侧面（通说）","color":"main"},{"title":"军队","text":"非人化的机器（通说）","color":"antagonist"},{"title":"反战","text":"B347 定位","color":"gold"},{"title":"幻灭","text":"从法国到法庭（通说）","color":"family"}])},
# 7. 拉格洛夫《古斯泰·贝林的故事》
{"id":"gusitaibeilin","title":"古斯泰·贝林的故事","original_title":"Gösta Berlings saga","region":"瑞典","era":"近代","era_detail":"19世纪90年代初",
"genre":"长篇小说","genre_group":"小说","language":"瑞典语","author_id":"lagerlof","author_name":"塞尔玛·拉格洛夫",
"year_display":"1891年（作者页注记：Britannica B311——Gösta Berlings saga——年份通说待核）","year_sort":1891,
"background":["作者页（B311）注记：Gösta Berlings saga——拉格洛夫代表作之一（骑鹅旅行记作者）。","Britannica（B311）：拉格洛夫——1909诺奖（首位女作家得主说待核——B311 口径）。","题材（通说待核）：被革职的牧师古斯泰与'恶魔的骑士团'——瑞典庄园传奇。"],
"outline":["（通说待核）牧师古斯泰被革职后加入农庄的狂欢骑士团。","（通说待核）辛克莱夫人的救赎与雪夜试炼。"],
"characters":[{"name":"古斯泰·贝林","identity":"革职牧师","note":"（B311 书名人物）"},{"name":"玛格丽特·辛克莱","identity":"农庄女主人","note":"（通说待核）"}],
"themes":["传奇与现实的交织（通说待核）。",
 "'恶魔骑士团'的狂欢（通说待核）。",
 "瑞典庄圆的浪漫主义（B311 语境）。"],
"influence":[{"text":"Britannica：拉格洛夫1909诺奖（B311 作者页语境）。","source":"B311"},{"text":"Britannica：《骑鹅旅行记》为代表作（B311 交叉）。","source":"B311"}],
"reading":{"difficulties":["瑞典浪漫主义传统。","传奇化的人物群像。"],
 "editions":["《古斯泰·贝林的故事》中译名（《古斯泰·贝林传奇》）待核。","瑞典文原版（公有领域）。"],
 "order":"拉格洛夫成名作；先于《骑鹅旅行记》。"},
"pending":["1891年出版细节待核。","人物名（古斯泰/辛克莱）核对（通说）。","'恶魔骑士团'细节待核。"],
"sources":["B311"],"year_source":"B311","author_source":"B311","related_works":["qieelvxing","nongmin","xinnuofusuobaken"],
"svg":G("《古斯泰·贝林》传奇结构图",[{"title":"古斯泰","text":"革职的牧师（B311）","color":"main"},{"title":"骑士团","text":"狂欢的流浪（通说）","color":"gold"},{"title":"救赎","text":"雪夜的试炼（通说）","color":"family"},{"title":"传奇","text":"现实的魔化（通说）","color":"antagonist"}])},
# 8. 海涅《诗歌集》
{"id":"shigetu","title":"诗歌集","original_title":"Buch der Lieder","region":"德国","era":"近代","era_detail":"19世纪20年代末",
"genre":"诗集","genre_group":"诗歌","language":"德语","author_id":"heine","author_name":"海因里希·海涅",
"year_display":"1827年（作者页注记：Britannica——诗歌集 (1827)——抒情诗）","year_sort":1827,
"background":["作者页注记：诗歌集 (1827)——'抒情诗（Britannica）'。","Britannica：海涅——德语诗人与散文家（作者页语境）。","题材（通说待核）：《北海之歌》等组诗——民歌调与浪漫主义讽刺的融合。"],
"outline":["（通说待核）情歌与北海组诗的两极。","（通说待核）'浪漫主义的反讽'：民谣体与反讽的并置。"],
"characters":[{"name":"抒情'我'","identity":"歌者","note":"（通说待核）"}],
"themes":["民歌调的抒情（B注记语境）。",
 "浪漫主义的反讽（通说待核）。",
 "'北海'组诗的现代性（通说待核）。"],
"influence":[{"text":"Britannica：诗歌集 (1827)（作者页注记）。","source":S_HE},{"text":"Britannica：海涅为19世纪德语诗歌代表（作者页语境）。","source":S_HE}],
"reading":{"difficulties":["德语韵律。","浪漫主义民歌传统。"],
 "editions":["《诗歌集》中译名（《歌集》）待核。","德文原版（公有领域）。"],
 "order":"海涅诗歌首选；与《德国，一个冬天的童话》对读。"},
"pending":["组篇（《北海》等）核对（通说）。","1827年出版（Hambourg说）待核。","中译名两说待核。"],
"sources":[S_HE],"year_source":S_HE,"author_source":S_HE,"related_works":["dongtiantonghua","xuboliweng","diyuzhiji"],
"svg":G("《诗歌集》两极结构图",[{"title":"情歌","text":"民歌的调子（通说）","color":"main"},{"title":"北海","text":"现代的波涛（通说）","color":"gold"},{"title":"反讽","text":"浪漫的自我解构（通说）","color":"antagonist"},{"title":"1827","text":"结集之年（B注记）","color":"family"}])},
# 9. 贺拉斯《诗艺》(B302)
{"id":"shiyi","title":"诗艺","original_title":"Ars Poetica","region":"罗马","era":"古代","era_detail":"公元前1世纪",
"genre":"诗体信札（诗论）","genre_group":"散文","language":"拉丁语","author_id":"horace","author_name":"贺拉斯",
"year_display":"约公元前19-18年（Britannica B302：Ars Poetica——约19—18 BC）","year_sort":-19,
"background":["Britannica（B302）：Ars Poetica——'约19-18 BC'。","Britannica（B302）：贺拉斯——《颂歌》（Odes）作者、奥古斯都时代诗人。","题材（通说待核）：致皮索父子的诗学信札——'合式'（decorum）、寓教于乐。"],
"outline":["（通说待核）诗的'合式'：题材与语言的匹配。","（通说待核）'寓教于乐'（omne tulit punctum...——不直接引文）。"],
"characters":[{"name":"皮索父子","identity":"受信人","note":"（通说待核）"}],
"themes":["'合式'原则（通说待核）。",
 "诗人的修养与天才（通说待核）。",
 "罗马古典主义的纲领（B302 语境）。"],
"influence":[{"text":"Britannica：Ars Poetica（B302）。","source":"B302"},{"text":"Britannica：贺拉斯《颂歌》的地位（B302 作者页）。","source":"B302"}],
"reading":{"difficulties":["拉丁语诗体信札。","古典修辞学语境。"],
 "editions":["《诗艺》中译本（人民文学《缪灵珠译文集》等——通说待核）。","拉丁文原版（公有领域）。"],
 "order":"西方诗论源头之一；与《诗学》对读。"},
"pending":["'寓教于乐'拉丁原文核对（不采译文为引文）。","收信人（皮索说）核对。","与《诗学》的传承关系待核。"],
"sources":["B302"],"year_source":"B302","author_source":"B302","related_works":["geti","xunjiexiaoshuo","laokong"],
"svg":G("《诗艺》合式结构图",[{"title":"合式","text":"古典主义的准则（通说）","color":"main"},{"title":"皮索父子","text":"受信人（通说）","color":"family"},{"title":"寓教于乐","text":"诗的功能（通说）","color":"gold"},{"title":"罗马","text":"奥古斯都时代（B302）","color":"antagonist"}])},
# 10. 荷尔德林《面饼与酒》(B338)
{"id":"mianbingyujiu","title":"面饼与酒","original_title":"Brod und Wein","region":"德国","era":"近代","era_detail":"19世纪初",
"genre":"哀歌","genre_group":"诗歌","language":"德语","author_id":"holderlin","author_name":"弗里德里希·荷尔德林",
"year_display":"1798-1801年（Britannica B338：Brod und Wein——1798-1801哀歌）","year_sort":1800,
"background":["Britannica（B338）：Brod und Wein——1798-1801年哀歌（与'Menons Klagen um Diotima'并列）。","Britannica（B338）：'a prophet of spiritual renewal, of \"the return of the gods\"'——哀歌体。","Britannica（B338）：'especially admired for his uniquely expressive style'。"],
"outline":["（通说待核——B338未载细节）'面包是大地之果，酒是大地之果'（通说待核——不采为引文）的圣餐意象。","（通说待核）'贫乏时代'诗人何为的追问。"],
"characters":[{"name":"抒情'我'","identity":"哀歌者","note":"（通说待核）"}],
"themes":["'诸神的黑夜'与'贫乏时代'（通说待核）。",
 "圣餐意象：面饼与酒（B338 书名）。",
 "'诗人如鹰鹫'的使命（通说待核）。"],
"influence":[{"text":"Britannica：Brod und Wein——1798-1801哀歌（B338）。","source":"B338"},{"text":"Britannica：'uniquely expressive style'（B338 作者级）。","source":"B338"}],
"reading":{"difficulties":["哀歌体（elegiac couplets——通说待核）。","荷尔德林的希腊崇拜。"],
 "editions":["《面饼与酒》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"荷尔德林诗歌首选；与《许珀里翁》对读。"},
"pending":["篇内结构（九节说）核对（通说）。","'贫乏时代'说法出处待核。","与《许珀里翁·狄奥蒂玛》哀歌的关系待核。"],
"sources":["B338"],"year_source":"B338","author_source":"B338","related_works":["xuboliweng","diyuzhiji","ezhihua"],
"svg":G("《面饼与酒》哀歌结构图",[{"title":"面饼与酒","text":"圣餐的意象（B338）","color":"gold"},{"title":"贫乏时代","text":"诸神的黑夜（通说）","color":"antagonist"},{"title":"诗人","text":"鹰鹫的使命（通说）","color":"main"},{"title":"哀歌","text":"1798-1801（B338）","color":"family"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批46）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('dixiashishouji','dostoevsky','地下室手记'),('sigesizhongzou','eliot','四个四重奏'),('zaidiceng','gorky','在底层'),('xieyang','dazaiosamu','斜阳'),('shafeinushideriji','dingling','莎菲'),('sangeshibing','dospassos','三个士兵'),('gusitaibeilin','lagerlof','古斯泰'),('shigetu','heine','诗歌集'),('shiyi','horace','诗艺'),('mianbingyujiu','holderlin','面饼与酒')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH46 DONE')
