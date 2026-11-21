# -*- coding: utf-8 -*-
"""批47：零成本 12 部（新生/帝制论/波士顿以北/卡斯特桥市长/无名的裘德/救风尘/冰岛之钟/下一次将是烈火/三个火枪手/弗洛斯河上的磨坊/织工马南/潘）"""
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
# 1. 但丁《新生》
{"id":"xinshengbutan","title":"新生","original_title":"Vita nuova","region":"意大利","era":"古代","era_detail":"13世纪90年代",
"genre":"诗文合集","genre_group":"散文","language":"意大利语（俗语）","author_id":"dante","author_name":"但丁",
"year_display":"约1293年（作者页注记：Britannica 列举——新生（约1293）——抒情诗集）","year_sort":1293,
"background":["作者页注记：新生（约1293）、论俗语——'抒情诗集与俗语理论（Britannica 列举）'。","Britannica：但丁——《神曲》作者（作者页交叉）。","题材（通说待核）：贝雅特丽齐的三十一节'新生'——散文与十四行诗的交替。"],
"outline":["（通说待核）散文'说'与诗歌的交替：爱情书（libello）。","（通说待核）贝雅特丽齐之死与'新见'（又一说：novissimo——细节待核）。"],
"characters":[{"name":"但丁（叙述者）","identity":"诗人","note":"（通说待核）"},{"name":"贝雅特丽齐","identity":"受爱者","note":"（通说待核）"}],
"themes":["'温柔的井'（dolce stil novo——通说待核）。",
 "散文与诗的交替（B注记：抒情诗集）。",
 "'爱'的神学化（通说待核）。"],
"influence":[{"text":"Britannica：'抒情诗集与俗语理论'（作者页注记）。","source":src_of('dante')},{"text":"Britannica：《神曲》的先声（作者页交叉）。","source":src_of('dante')}],
"reading":{"difficulties":["'温柔的新体'诗派。","散文与诗的交替结构。"],
 "editions":["《新生》中译本（人民文学等——通说待核）。","意大利文原版（公有领域）。"],
 "order":"《神曲》前的自传性预演。"},
"pending":["篇目数（31/42章说）核对（通说）。","约1293年成书待核。","贝雅特丽齐细节待核。"],
"sources":[src_of('dante')],"year_source":src_of('dante'),"author_source":src_of('dante'),"related_works":["shenqu" if "shenqu" in existing else "leiyu","safucanpian","ezhihua"],
"svg":G("《新生》散文诗交替图",[{"title":"散文","text":"抒情的说（通说）","color":"main"},{"title":"诗","text":"十四行的歌（通说）","color":"gold"},{"title":"贝雅特丽齐","text":"'新生'的源泉（通说）","color":"family"},{"title":"温柔的新体","text":"诗派的坐标（通说）","color":"antagonist"}])},
# 2. 但丁《帝制论》
{"id":"dizhilun","title":"帝制论","original_title":"De monarchia","region":"意大利","era":"古代","era_detail":"14世纪10年代",
"genre":"政治哲学论著","genre_group":"散文","language":"拉丁语","author_id":"dante","author_name":"但丁",
"year_display":"作者页注记：Britannica——帝制论（De monarchia）——'key medieval political-philosophy tract'（中世纪政治哲学重要论著）","year_sort":1312,
"background":["作者页注记：帝制论（De monarchia）——'政治哲学论著（Britannica：key medieval political-philosophy tract）'。","Britannica：但丁——流亡中的佛罗伦萨人（作者页语境——待核）。","题材（通说待核）：三卷论普世帝制——世俗权力独立于教会。"],
"outline":["（通说待核）第一卷：普世帝制的必要。","（通说待核）第三卷：'两把刀'——皇帝不从属于教皇。"],
"characters":[{"name":"（论著无人物）","identity":"——","note":"政治哲学论著"}],
"themes":["世俗与教会的权力分立（通说待核）。",
 "'key medieval political-philosophy tract'（B注记）。",
 "流亡者的政治学（作者页语境）。"],
"influence":[{"text":"Britannica：'key medieval political-philosophy tract'（作者页注记）。","source":src_of('dante')},{"text":"Britannica：但丁《神曲》为代表作（作者页交叉）。","source":src_of('dante')}],
"reading":{"difficulties":["中世纪政治神学。","亚里士多德-经院哲学框架。"],
 "editions":["《帝制论》中译本（商务印书馆等——通说待核）。","拉丁文原版（公有领域）。"],
 "order":"但丁思想侧写；与《论俗语》对读。"},
"pending":["成书年份（约1312-1313说）待核。","三卷结构核对（通说）。","'两把刀'论细节待核。"],
"sources":[src_of('dante')],"year_source":src_of('dante'),"author_source":src_of('dante'),"related_works":["leiyu","dizhi" if "dizhi" in existing else "luomashi","tangjihuade"],
"svg":G("《帝制论》两权结构图",[{"title":"皇帝","text":"世俗的普世权（通说）","color":"main"},{"title":"教皇","text":"精神的权杖（通说）","color":"gold"},{"title":"两把刀","text":"权力的分立（通说）","color":"antagonist"},{"title":"流亡","text":"写作的处境（作者页语境）","color":"family"}])},
# 3. 弗罗斯特《波士顿以北》
{"id":"bosidunyibei","title":"波士顿以北","original_title":"North of Boston","region":"美国","era":"近代","era_detail":"20世纪10年代",
"genre":"诗集","genre_group":"诗歌","language":"英语","author_id":"frost","author_name":"罗伯特·弗罗斯特",
"year_display":"1914年（作者页注记：Britannica——少年的意志（1913）、波士顿以北（1914）——伦敦成名作）","year_sort":1914,
"background":["作者页注记：少年的意志 (1913)、波士顿以北 (1914)——'伦敦成名作（Britannica）'。","Britannica：弗罗斯特——美国诗人、四度普利策（作者页语境——待核）。","题材（通说待核）：'修墙'《补墙》等人物对话诗——新英格兰农庄。"],
"outline":["（通说待核）《补墙》（Mending Wall）等以人物说话的诗。","（通说待核）新英格兰的农庄伦理。"],
"characters":[{"name":"说话者（农人等）","identity":"——","note":"（通说待核）"}],
"themes":["'伦敦成名作'（B注记——诗集于英国出版）。",
 "对话体叙事诗（通说待核）。",
 "农庄的生存伦理（通说待核）。"],
"influence":[{"text":"Britannica：'伦敦成名作'（作者页注记）。","source":src_of('frost')},{"text":"Britannica：《雪夜林边小驻》等名篇（作者页交叉——待核）。","source":src_of('frost')}],
"reading":{"difficulties":["新英格兰方言与意象。","'诗始于愉悦，终于智慧'（通说待核——不采为引文）。"],
 "editions":["《波士顿以北》中译本（人民文学等——通说待核）。","英文原版（公有领域状态待核）。"],
 "order":"弗罗斯特第二部诗集；与《少年的意志》对读。"},
"pending":["篇目（《补墙》等）核对（通说）。","1914年出版（David Nutt伦敦说）待核。","'成名作'细节核对。"],
"sources":[src_of('frost')],"year_source":src_of('frost'),"author_source":src_of('frost'),"related_works":["zhijiage","caoyeji","mianbingyujiu"],
"svg":G("《波士顿以北》农庄对话图",[{"title":"补墙","text":"墙的辩证（通说）","color":"main"},{"title":"新英格兰","text":"农庄的场景（通说）","color":"family"},{"title":"伦敦","text":"成名的起点（B注记）","color":"gold"},{"title":"对话","text":"叙事诗的形态（通说）","color":"antagonist"}])},
# 4. 哈代《卡斯特桥市长》
{"id":"kasiteqiaoshizhang","title":"卡斯特桥市长","original_title":"The Mayor of Casterbridge","region":"英国","era":"近代","era_detail":"19世纪80年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"hardy","author_name":"托马斯·哈代",
"year_display":"1886年（作者页注记：Britannica 列举——卡斯特桥市长 (1886)——'威塞克斯小说'）","year_sort":1886,
"background":["作者页注记：远离尘嚣 (1874)、还乡 (1878)、卡斯特桥市长 (1886)、无名的裘德 (1895)——''威塞克斯小说'（Britannica 列举）'。","Britannica：哈代——英国小说家与诗人（作者页语境）。","题材（通说待核）：亨查德卖妻——命运与性格悲剧。"],
"outline":["（通说待核）亨查德的卖妻悔恨与发迹为市长。","（通说待核）伐尔弗雷的登场与亨查德的败落。"],
"characters":[{"name":"迈克尔·亨查德","identity":"市长/谷物商","note":"（通说待核）"},{"name":"唐纳德·伐尔弗雷","identity":"苏格兰人对手","note":"（通说待核）"}],
"themes":["'性格即命运'的希腊式悲剧（通说待核）。",
 "威塞克斯的乡村与市场（B注记语境）。",
 "传统农业社会的解体（通说待核）。"],
"influence":[{"text":"Britannica：'威塞克斯小说'（作者页注记）。","source":src_of('hardy')},{"text":"Britannica：哈代《德伯家的苔丝》为代表作（作者页交叉）。","source":src_of('hardy')}],
"reading":{"difficulties":["多塞特乡村社会。","'性格悲剧'的古典结构。"],
 "editions":["《卡斯特桥市长》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"哈代中期首选；与《德伯家的苔丝》对读。"},
"pending":["亨查德人名核对（通说）。","1886年连载/出版细节待核。","'卖妻'开场细节待核。"],
"sources":[src_of('hardy')],"year_source":src_of('hardy'),"author_source":src_of('hardy'),"related_works":["debojiadetaisi","wumingdeqiude","nongmin"],
"svg":G("《卡斯特桥市长》性格悲剧图",[{"title":"亨查德","text":"卖妻的悔恨（通说）","color":"main"},{"title":"市长","text":"发迹与败落（通说）","color":"gold"},{"title":"伐尔弗雷","text":"性格的对照（通说）","color":"antagonist"},{"title":"威塞克斯","text":"乡村的世界（B注记）","color":"family"}])},
# 5. 哈代《无名的裘德》
{"id":"wumingdeqiude","title":"无名的裘德","original_title":"Jude the Obscure","region":"英国","era":"近代","era_detail":"19世纪90年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"hardy","author_name":"托马斯·哈代",
"year_display":"1895年（作者页注记：Britannica 列举——无名的裘德 (1895)）","year_sort":1895,
"background":["作者页注记：无名的裘德 (1895)——''威塞克斯小说'（Britannica 列举）'。","Britannica：哈代——此后转而专事诗歌（作者页语境——待核）。","题材（通说待核）：石匠裘德的求学梦与婚姻悲剧——'肉体的苇草'。"],
"outline":["（通说待核）裘德攻克里斯特敏斯特学院的梦想破灭。","（通说待核）淑·布莱德赫：'契约婚姻'的反叛。"],
"characters":[{"name":"裘德·福雷","identity":"石匠","note":"（通说待核）"},{"name":"淑·布莱德赫","identity":"表妹/伴侣","note":"（通说待核）"}],
"themes":["教育壁垒与阶级（通说待核）。",
 "婚姻制度与宗教（通说待核）。",
 "'最暗的哈代'的评价（通说待核）。"],
"influence":[{"text":"Britannica：'威塞克斯小说'（作者页注记）。","source":src_of('hardy')},{"text":"Britannica：哈代1895年后转向诗歌说（作者页交叉——待核）。","source":src_of('hardy')}],
"reading":{"difficulties":["1890年代道德气候。","'小说悲剧'的分期（通说待核）。"],
 "editions":["《无名的裘德》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"哈代收官小说；与《卡斯特桥市长》对读。"},
"pending":["裘德/淑人名核对（通说）。","1895年出版细节待核。","'出版风波'（主教焚书说）待核。"],
"sources":[src_of('hardy')],"year_source":src_of('hardy'),"author_source":src_of('hardy'),"related_works":["kasiteqiaoshizhang","debojiadetaisi","nuhuodeputao"],
"svg":G("《无名的裘德》壁垒结构图",[{"title":"裘德","text":"石匠的求学梦（通说）","color":"main"},{"title":"学院","text":"不可入的壁垒（通说）","color":"antagonist"},{"title":"淑","text":"婚姻的反叛（通说）","color":"gold"},{"title":"悲剧","text":"'小说悲剧'（通说）","color":"family"}])},
# 6. 关汉卿《救风尘》
{"id":"jiufengchen","title":"救风尘","original_title":"赵盼儿风月救风尘","region":"中国","era":"古代","era_detail":"13世纪",
"genre":"杂剧","genre_group":"戏剧","language":"汉语","author_id":"guanhanqing","author_name":"关汉卿",
"year_display":"作者页注记：Britannica 关汉卿条署名条目（作品归属通行说法——年代通说待核）","year_sort":1300,
"background":["作者页注记：救风尘——'喜剧代表作，写妓女赵盼儿智救同伴；署名条目见 Britannica 关汉卿条（作品归属通行说法）'。","Britannica：关汉卿——元杂剧四大家之首说（作者页语境——待核）。","题材（通说待核）：赵盼儿以风月手段搭救被周舍欺骗的姐妹宋引章。"],
"outline":["（通说待核）赵盼儿的风月圈套：智取周舍。","（通说待核）'风月救风尘'：以恶治恶的喜剧智慧。"],
"characters":[{"name":"赵盼儿","identity":"妓女/救人者","note":"（B注记：赵盼儿）"},{"name":"宋引章","identity":"被骗姐妹","note":"（B注记）"},{"name":"周舍","identity":"负心商人","note":"（通说待核）"}],
"themes":["底层女性的互助（通说待核）。",
 "'风月'作为武器（通说待核）。",
 "元杂剧喜剧的典范（B注记语境）。"],
"influence":[{"text":"Britannica：关汉卿条署名条目（作者页注记）。","source":src_of('guanhanqing')},{"text":"Britannica：《窦娥冤》为代表作（作者页交叉）。","source":src_of('guanhanqing')}],
"reading":{"difficulties":["元杂剧四折一楔子体制。","市井口语的元代语法。"],
 "editions":["《救风尘》（人民文学出版社《关汉卿全集》等——通说待核）。","元刊本（公有领域）。"],
 "order":"关汉卿喜剧首选；与《窦娥冤》对读。"},
"pending":["四折结构核对（通说）。","署名条目的'通行说法'边界核对（B注记）。","2023年影视改编不采。"],
"sources":[src_of('guanhanqing')],"year_source":src_of('guanhanqing'),"author_source":src_of('guanhanqing'),"related_works":["doueyuan","xiniu","richu"],
"svg":G("《救风尘》风月智取图",[{"title":"赵盼儿","text":"智救的巧计（B注记）","color":"main"},{"title":"周舍","text":"负心的骗局（通说）","color":"antagonist"},{"title":"风月","text":"以恶制恶（书名）","color":"gold"},{"title":"姐妹","text":"底层的互助（通说）","color":"family"}])},
# 7. 拉克斯内斯《冰岛之钟》
{"id":"bingdaozhizhong","title":"冰岛之钟","original_title":"Íslandsklukkan","region":"冰岛","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说（三部曲）","genre_group":"小说","language":"冰岛语","author_id":"laxness","author_name":"哈尔多尔·拉克斯内斯",
"year_display":"1943-46年（Britannica B361：Íslandsklukkan (1943-46)——三部曲）","year_sort":1943,
"background":["Britannica（B361）：Íslandsklukkan——三部曲（'Iceland's Bell'）。","Britannica（B361）：拉克斯内斯——1955诺奖——'renewed the great narrative art of Iceland'。","题材（通说待核）：17世纪冰岛——约翰·哈尔滨普的'钟声'与民族觉醒。"],
"outline":["（通说待核）第一部：冰岛之钟；第二、三部：钟声的余波（卷名通说待核）。","（通说待核）饥饿、丹麦统治与'财宝'传说。"],
"characters":[{"name":"约翰·哈尔滨普","identity":"求学者","note":"（通说待核）"},{"name":"斯诺里·坡尔","identity":"压迫者","note":"（通说待核）"}],
"themes":["17世纪冰岛的殖民史（通说待核）。",
 "民族叙事的更新（B361：诺奖引语）。",
 "苦难与传说（通说待核）。"],
"influence":[{"text":"Britannica：1955诺奖（B361）。","source":"B361"},{"text":"Britannica：'renewed the great narrative art of Iceland'（B361）。","source":"B361"}],
"reading":{"difficulties":["17世纪冰岛历史。","三部曲的卷次。"],
 "editions":["《冰岛之钟》中译本（人民文学等——通说待核）。","冰岛文原版。"],
 "order":"拉克斯内斯史诗篇；与《独立的人们》对读。"},
"pending":["三部卷名核对（通说）。","哈尔滨普人名核对（通说）。","1943-46出版细节待核（B361口径）。"],
"sources":["B361"],"year_source":"B361","author_source":"B361","related_works":["dulidemen","nongmin","tangjihuade"],
"svg":G("《冰岛之钟》民族叙事图",[{"title":"钟声","text":"民族的觉醒（书名）","color":"gold"},{"title":"哈尔滨普","text":"17世纪的求索（通说）","color":"main"},{"title":"丹麦","text":"殖民的阴影（通说）","color":"antagonist"},{"title":"冰岛","text":"叙事的更新（B361）","color":"family"}])},
# 8. 鲍德温《下一次将是烈火》
{"id":"xiayicijiangshiliehuo","title":"下一次将是烈火","original_title":"The Fire Next Time","region":"美国","era":"现当代","era_detail":"20世纪60年代初",
"genre":"散文集","genre_group":"散文","language":"英语","author_id":"jbaldwin","author_name":"詹姆斯·鲍德温",
"year_display":"1963年（Britannica B327：The Fire Next Time, 1963）","year_sort":1963,
"background":["Britannica（B327）：The Fire Next Time——散文列表（1963）。","Britannica（B327）：鲍德温——民权运动语境（作者页交叉——'民权活动家'定位待核）。","题材（通说待核）：致侄子的信+《从我的藏在地下室里的手册》——'黑人 Muslim'与爱之可能。"],
"outline":["（通说待核）'致侄子'：美国黑人处境的家书。","（通说待核）地下室手册：宗教与民族的清算。"],
"characters":[{"name":"'我'","identity":"写信人","note":"（B327 语境）"}],
"themes":["种族与爱（通说待核）。",
 "'下一次——烈火'的预言（书名语境——通说待核）。",
 "民权时代的公共写作（B327 交叉）。"],
"influence":[{"text":"Britannica：The Fire Next Time (1963)（B327）。","source":"B327"},{"text":"Britannica：《向苍天呼吁》为'first and finest novel'（B327 交叉）。","source":"B327"}],
"reading":{"difficulties":["民权运动史。","'黑人穆斯林'语境（通说待核）。"],
 "editions":["《下一次将是烈火》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"鲍德温散文首选；与《向苍天呼吁》对读。"},
"pending":["两篇散文标题核对（通说）。","1963年出版（Dial Press说）待核。","'民权'细节待核。"],
"sources":["B327"],"year_source":"B327","author_source":"B327","related_works":["xiangtianhuhan","qiaowandefangjian","kanbujian3"],
"svg":G("《下一次将是烈火》预言结构图",[{"title":"家书","text":"致侄子的信（通说）","color":"main"},{"title":"烈火","text":"'下一次'的警告（书名）","color":"antagonist"},{"title":"民权","text":"时代的公共写作（B327）","color":"gold"},{"title":"爱","text":"种族的出路（通说）","color":"family"}])},
# 9. 大仲马《三个火枪手》
{"id":"sangeshouqiangshou","title":"三个火枪手","original_title":"Les Trois Mousquetaires","region":"法国","era":"近代","era_detail":"19世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"dumaspere","author_name":"大仲马",
"year_display":"1844年（作者页注记：Britannica——三个火枪手及其续篇——Vingt ans après (1845)；Bragelonne (1848-50)——出版年通说待核）","year_sort":1844,
"background":["作者页注记：三个火枪手及其续篇——'（Britannica：Vingt ans après (1845)；Bragelonne (1848-50)）'。","Britannica：大仲马——《基督山伯爵》作者（作者页交叉）。","题材（通说待核）：达达尼昂与三剑客——路易十三宫廷的决斗与阴谋。"],
"outline":["（通说待核）达达尼昂赴巴黎与'三剑客'结盟。","（通说待核）王后项坠事件与米拉迪的阴谋。"],
"characters":[{"name":"达达尼昂","identity":"加斯科尼青年","note":"（通说待核）"},{"name":"阿托斯/波托斯/阿拉密斯","identity":"三剑客","note":"（通说待核）"}],
"themes":["'人人为我，我为人人'（通说待核——口号出处待核）。",
 "历史冒险小说（B注记语境）。",
 "黎塞留时代的宫廷阴谋（通说待核）。"],
"influence":[{"text":"Britannica：续篇 Vingt ans après (1845)（作者页注记）。","source":src_of('dumaspere')},{"text":"Britannica：大仲马为通俗历史小说大师（作者页语境——待核）。","source":src_of('dumaspere')}],
"reading":{"difficulties":["路易十三时代史。","连载小说的节奏。"],
 "editions":["《三个火枪手》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"大仲马历史小说首选；与《基督山伯爵》对读。"},
"pending":["1844年连载（《时代》报说）待核。","达达尼昂/三剑客名核对（通说）。","与《基督山伯爵》的连载关系待核。"],
"sources":[src_of('dumaspere')],"year_source":src_of('dumaspere'),"author_source":src_of('dumaspere'),"related_works":["jidushanbojue","nongmin","tangjihuade"],
"svg":G("《三个火枪手》决斗结构图",[{"title":"达达尼昂","text":"加斯科尼的热血（通说）","color":"main"},{"title":"三剑客","text":"'人人为我'（通说）","color":"gold"},{"title":"米拉迪","text":"蛇蝎的阴谋（通说）","color":"antagonist"},{"title":"路易十三","text":"宫廷的舞台（通说）","color":"family"}])},
# 10. 乔治·爱略特《弗洛斯河上的磨坊》
{"id":"fuluosihemofang","title":"弗洛斯河上的磨坊","original_title":"The Mill on the Floss","region":"英国","era":"近代","era_detail":"19世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"geluote","author_name":"乔治·爱略特",
"year_display":"1860年（作者页注记：Britannica 列举——弗洛斯河上的磨坊 (1860)）","year_sort":1860,
"background":["作者页注记：亚当·比德 (1859)、弗洛斯河上的磨坊 (1860)——'早期名作（Britannica 列举）'。","Britannica：乔治·爱略特——《米德尔马契》作者（作者页交叉）。","题材（通说待核）：麦琪与汤姆兄妹——弗洛斯河畔的家族恩怨与洪水。"],
"outline":["（通说待核）麦琪的才情与家族的排斥。","（通说待核）洪水的终局与兄妹的和解。"],
"characters":[{"name":"麦琪·塔利弗","identity":"女主角","note":"（通说待核）"},{"name":"汤姆","identity":"兄长","note":"（通说待核）"}],
"themes":["兄妹的对立与和解（通说待核）。",
 "女性才情的压抑（通说待核）。",
 "'早期名作'（B注记）。"],
"influence":[{"text":"Britannica：'早期名作'（作者页注记）。","source":src_of('geluote')},{"text":"Britannica：《米德尔马契》为代表作（作者页交叉）。","source":src_of('geluote')}],
"reading":{"difficulties":["多塞特/林肯郡乡村（圣奥格镇说——通说待核）。","心理现实主义的早期形态。"],
 "editions":["《弗洛斯河上的磨坊》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"乔治·爱略特第二作；先于《米德尔马契》。"},
"pending":["麦琪/汤姆人名核对（通说）。","1860年出版细节待核。","洪水结局细节待核。"],
"sources":[src_of('geluote')],"year_source":src_of('geluote'),"author_source":src_of('geluote'),"related_works":["midengmamaqi","zhigongmanan","leiyu"],
"svg":G("《弗洛斯河上的磨坊》兄妹图",[{"title":"麦琪","text":"才情的压抑（通说）","color":"main"},{"title":"汤姆","text":"拘谨的兄长（通说）","color":"antagonist"},{"title":"磨坊","text":"家族的产业（书名）","color":"family"},{"title":"洪水","text":"和解的终局（通说）","color":"gold"}])},
# 11. 乔治·爱略特《织工马南》
{"id":"zhigongmanan","title":"织工马南","original_title":"Silas Marner","region":"英国","era":"近代","era_detail":"19世纪60年代初",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"geluote","author_name":"乔治·爱略特",
"year_display":"1861年（作者页注记：Britannica 列举——织工马南 (1861)）","year_sort":1861,
"background":["作者页注记：织工马南 (1861)、丹尼尔·德龙达 (1876)——'（Britannica 列举）'。","Britannica：乔治·爱略特——维多利亚小说家（作者页交叉）。","题材（通说待核）：被诬的织工马南的金币失窃与弃婴伊莱的收养。"],
"outline":["（通说待核）马南的金币失窃：社区的怀疑。","（通说待核）弃婴的到来与'金币'换成'金发'的救赎。"],
"characters":[{"name":"马南","identity":"织工","note":"（通说待核）"},{"name":"伊莱（Eppie）","identity":"弃婴","note":"（通说待核）"}],
"themes":["金币与金发的交换（书名语境——通说待核）。",
 "社区与信仰的重建（通说待核）。",
 "'寓言式'的中篇（通说待核）。"],
"influence":[{"text":"Britannica：织工马南 (1861)（作者页注记）。","source":src_of('geluote')},{"text":"Britannica：《米德尔马契》为代表作（作者页交叉）。","source":src_of('geluote')}],
"reading":{"difficulties":["19世纪早期英国乡村。","'寓言'与'写实'的平衡。"],
 "editions":["《织工马南》中译名（《织工马南传》）待核。","英文原版（公有领域）。"],
 "order":"乔治·爱略特短篇入门。"},
"pending":["马南/伊莱人名核对（通说）。","1861年出版细节待核。","'弃婴'情节细节待核。"],
"sources":[src_of('geluote')],"year_source":src_of('geluote'),"author_source":src_of('geluote'),"related_works":["fuluosihemofang","midengmamaqi","nongmin"],
"svg":G("《织工马南》救赎结构图",[{"title":"金币","text":"被窃的积攒（通说）","color":"antagonist"},{"title":"织机","text":"孤寂的劳作（通说）","color":"main"},{"title":"伊莱","text":"金发的孩子（通说）","color":"gold"},{"title":"社区","text":"信仰的重建（通说）","color":"family"}])},
# 12. 汉姆生《潘》
{"id":"pan1894","title":"潘","original_title":"Pan","region":"挪威","era":"近代","era_detail":"19世纪90年代",
"genre":"长篇小说","genre_group":"小说","language":"挪威语","author_id":"hamsun","author_name":"克努特·汉姆生",
"year_display":"1894年（Britannica B360：Pan (1894)）","year_sort":1894,
"background":["Britannica（B360）：Pan——早期作品——'asocial heroes'——'either was indifferent to or took an irreverent view of progress'。","Britannica（B360）：汉姆生——1920诺奖；《饥饿》为其成名作（交叉）。","题材（通说待核）：中尉格拉恩与爱德华在挪威森林的夏恋——'潘'的野性。"],
"outline":["（通说待核）森林猎人的夏日与商人的女儿。","（通说待核）'潘'的合唱与自然的独白。"],
"characters":[{"name":"格拉恩","identity":"中尉","note":"（通说待核，B360未载）"},{"name":"爱德华","identity":"商人女儿","note":"（通说待核）"}],
"themes":["自然的泛神论（书名语境——通说待核）。",
 "'asocial heroes'（B360）。",
 "对进步的漠然或不敬（B360）。"],
"influence":[{"text":"Britannica：Pan (1894)（B360）。","source":"B360"},{"text":"Britannica：1920诺奖（B360 交叉）。","source":"B360"}],
"reading":{"difficulties":["'潘'的神话语境。","抒情与叙事的混合（通说待核）。"],
 "editions":["《潘》中译本（人民文学等——通说待核）。","挪威文原版（公有领域）。"],
 "order":"汉姆生第二作；与《饥饿》《大地的成长》对读。"},
"pending":["格拉恩/爱德华人名核对（通说）。","1894年出版细节待核。","'合唱'结构（Chorus of Pan说）待核。"],
"sources":["B360"],"year_source":"B360","author_source":"B360","related_works":["jihe","dadidechengzhang","xinnuofusuobaken"],
"svg":G("《潘》森林夏恋图",[{"title":"潘","text":"野性的神（书名）","color":"gold"},{"title":"森林","text":"挪威的夏天（通说）","color":"family"},{"title":"夏恋","text":"注定错位（通说）","color":"main"},{"title":"进步","text":"'不敬'的目光（B360）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批47）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('xinshengbutan','dante','新生'),('dizhilun','dante','帝制论'),('bosidunyibei','frost','波士顿以北'),('kasiteqiaoshizhang','hardy','卡斯特桥市长'),('wumingdeqiude','hardy','无名的裘德'),('jiufengchen','guanhanqing','救风尘'),('bingdaozhizhong','laxness','冰岛之钟'),('xiayicijiangshiliehuo','jbaldwin','下一次将是烈火'),('sangeshouqiangshou','dumaspere','三个火枪手'),('fuluosihemofang','geluote','弗洛斯河上的磨坊'),('zhigongmanan','geluote','织工马南'),('pan1894','hamsun','潘')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH47 DONE')
