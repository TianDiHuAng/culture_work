# -*- coding: utf-8 -*-
"""批53：零成本 12 部（俄瑞斯忒亚/先人祭/德国神话/孙行者/提堂/檀香刑/爱经/哀歌集/旅行日记/萨朗波/海边的卡夫卡/我的大学）"""
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
{"id":"eruosteya","title":"俄瑞斯忒亚","original_title":"Oresteia","region":"希腊","era":"古代","era_detail":"公元前5世纪",
"genre":"三部曲悲剧","genre_group":"戏剧","language":"希腊语","author_id":"aeschylus","author_name":"埃斯库罗斯",
"year_display":"公元前458年（作者页注记：Britannica——俄瑞斯忒亚三部曲——458 BC）","year_sort":-458,
"background":["作者页注记：俄瑞斯忒亚三部曲——'（Britannica：458 BC）'。","Britannica（B234）：埃斯库罗斯——'Father of Tragedy'、'adding a second actor'、13次首奖。","题材（通说待核）：阿伽门农之死→俄瑞斯忒斯弑母→雅典法庭的审判——血亲复仇向法治的转变。"],
"outline":["（通说待核）《阿伽门农》《奠酒人》《复仇女神》三部连演。","（通说待核）雅典娜建立战神山法庭。"],
"characters":[{"name":"克吕泰涅斯特拉","identity":"弑夫王后","note":"（通说待核）"},{"name":"俄瑞斯忒斯","identity":"弑母子","note":"（通说待核）"},{"name":"雅典娜","identity":"法庭的建立者","note":"（通说待核）"}],
"themes":["复仇循环的终结与法治的诞生（通说待核）。",
 "'三部曲'的完整结构（B注记：458 BC）。",
 "种族诅咒的终结（通说待核）。"],
"influence":[{"text":"Britannica：458 BC（作者页注记）。","source":src_of('aeschylus')},{"text":"Britannica：'Father of Tragedy'（B234 交叉）。","source":"B234"}],
"reading":{"difficulties":["三部曲的连读。","古希腊复仇伦理（通说待核）。"],
 "editions":["《俄瑞斯忒亚》中译本（人民文学等——通说待核）。","希腊语原版（公有领域）。"],
 "order":"埃斯库罗斯唯一完整三部曲；与《被缚的普罗米修斯》对读。"},
"pending":["三部剧名核对（通说）。","458年获首奖说待核。","'唯一完整传世三部曲'说法核对。"],
"sources":[src_of('aeschylus')],"year_source":src_of('aeschylus'),"author_source":src_of('aeschylus'),"related_works":["baofuodepuluo" if "baofuodepuluo" in existing else "leiyu","shenglisong","safucanpian"],
"svg":G("《俄瑞斯忒亚》审判结构图",[{"title":"弑夫","text":"浴缸的复仇（通说）","color":"antagonist"},{"title":"弑母","text":"儿子的挣扎（通说）","color":"main"},{"title":"法庭","text":"法治的诞生（通说）","color":"gold"},{"title":"复仇女神","text":"转化为敬神（通说）","color":"family"}])},
{"id":"xianrenji","title":"先人祭","original_title":"Dziady","region":"波兰","era":"近代","era_detail":"19世纪20-30年代",
"genre":"诗剧","genre_group":"戏剧","language":"波兰语","author_id":"mickiewicz","author_name":"亚当·密茨凯维奇",
"year_display":"作者页注记：Britannica 语境（Dziady——成稿年代通说待核——第二/四部1823、第三部1832说）","year_sort":1823,
"background":["作者页注记：先人祭——'诗剧（Britannica 语境：Dziady——通说待核）'。","Britannica：密茨凯维奇——波兰民族诗人（作者页语境）。","题材（通说待核）：'先人祭'（亡灵节仪式）——古斯塔夫的 love 与'康拉德'的爱国。"],
"outline":["（通说待核）乡村的亡灵祭仪式与鬼魂的诉说。","（通说待核）第三部：维尔诺囚禁与'康拉德'的自比。"],
"characters":[{"name":"古斯塔夫/康拉德","identity":"转变的叙述者","note":"（通说待核）"},{"name":"魔鬼/神甫","identity":"仪式人物","note":"（通说待核）"}],
"themes":["民间仪式与民族叙事（通说待核）。",
 "'爱'向'爱国'的转变（通说待核）。",
 "沙俄统治下的波兰（B注记语境——通说待核）。"],
"influence":[{"text":"Britannica：Dziady 列举（作者页注记）。","source":src_of('mickiewicz')},{"text":"Britannica：密茨凯维奇《塔杜施先生》为代表作（作者页交叉）。","source":src_of('mickiewicz')}],
"reading":{"difficulties":["四部结构（二/四/一/三）。","民间祭仪词汇。"],
 "editions":["《先人祭》中译本（人民文学等——通说待核）。","波兰文原版（公有领域）。"],
 "order":"密茨凯维奇诗剧首选；与《塔杜施先生》对读。"},
"pending":["四部结构与年份核对（通说）。","1968年波兰演出风波待核。","'康拉德'细节待核。"],
"sources":[src_of('mickiewicz')],"year_source":src_of('mickiewicz'),"author_source":src_of('mickiewicz'),"related_works":["tadushixiansheng" if "tadushixiansheng" in existing else "leiyu","emo","jipusaiyaoqu"],
"svg":G("《先人祭》亡灵结构图",[{"title":"亡灵祭","text":"仪式的框架（通说）","color":"gold"},{"title":"古斯塔夫","text":"失恋的幽灵（通说）","color":"main"},{"title":"康拉德","text":"爱国的高呼（通说）","color":"antagonist"},{"title":"维尔诺","text":"囚禁的教堂（通说）","color":"family"}])},
{"id":"deguoshenhua","title":"德国神话","original_title":"Deutsche Mythologie","region":"德国","era":"近代","era_detail":"19世纪30年代",
"genre":"神话研究","genre_group":"散文","language":"德语","author_id":"grimm","author_name":"雅各布·格林",
"year_display":"1835年（作者页注记：Britannica——德国神话 (1835)）","year_sort":1835,
"background":["作者页注记：德国神话——'（Britannica：1835）'。","Britannica：格林——童话与语言学的双峰（作者页语境——待核）。","题材（通说待核）：日耳曼诸神的'堕落史'——从神话到民间信仰与童话。"],
"outline":["（通说待核）诸神（沃坦等）的残留：习俗、传说与迷信。","（通说待核）'神话→传说→童话'的降解序列。"],
"characters":[{"name":"（研究著作无人物）","identity":"——","note":"神话研究"}],
"themes":["日耳曼神话的重建（B注记：1835）。",
 "'神话-传说-童话'的降解（通说待核）。",
 "语言学的证据法（作者页语境）。"],
"influence":[{"text":"Britannica：Deutsche Mythologie (1835)（作者页注记）。","source":src_of('grimm')},{"text":"Britannica：格林兄弟《儿童与家庭童话集》为代表作（作者页交叉）。","source":src_of('grimm')}],
"reading":{"difficulties":["19世纪语言学方法。","北欧/德意志神话的对应。"],
 "editions":["《德国神话》中译名（《德意志神话学》）待核。","德文原版（公有领域）。"],
 "order":"格林学术侧面；与《童话集》对读。"},
"pending":["1835年出版细节待核。","'沃坦'章细节待核。","与《童话集》的方法关联待核。"],
"sources":[src_of('grimm')],"year_source":src_of('grimm'),"author_source":src_of('grimm'),"related_works":["haidenvren","chouxiaoya","xuboliweng"],
"svg":G("《德国神话》降解结构图",[{"title":"神话","text":"诸神的时代（通说）","color":"gold"},{"title":"传说","text":"民间的残留（通说）","color":"main"},{"title":"童话","text":"最后的形态（通说）","color":"family"},{"title":"语言学","text":"证据的方法（作者页语境）","color":"antagonist"}])},
{"id":"sunxingzhe","title":"孙行者：他的伪书","original_title":"Tripmaster Monkey: His Fake Book","region":"美国","era":"现当代","era_detail":"20世纪80年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"kingston","author_name":"汤亭亭",
"year_display":"1989年（作者页注记：Britannica 列举）","year_sort":1989,
"background":["作者页注记：孙行者：他的伪书——'（Britannica 列举）'。","Britannica：汤婷婷——华裔美国作家（《女勇士》《中国佬》作者——交叉）。","题材（通说待核）：惠特曼·阿新——1960年代旧金山的华裔'猴王'剧作家。"],
"outline":["（通说待核）阿新的独角戏：'猴王'的街头表演。","（通说待核）'伪书'：惠特曼的《草叶集》底本（通说待核）。"],
"characters":[{"name":"惠特曼·阿新","identity":"华裔青年","note":"（通说待核）"}],
"themes":["'猴王'的美国化（通说待核）。",
 "'伪书'（fake book）的双关（书名语境）。",
 "60年代反文化（通说待核）。"],
"influence":[{"text":"Britannica：Tripmaster Monkey（作者页注记）。","source":src_of('kingston')},{"text":"Britannica：《女勇士》为成名作（作者页交叉）。","source":src_of('kingston')}],
"reading":{"difficulties":["'惠特曼·阿新'名字的戏谑。","60年代旧金山。"],
 "editions":["《孙行者：他的伪书》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"汤婷亭三部曲之三；与《中国佬》对读。"},
"pending":["阿新人名核对（通说）。","1989年出版（Knopf说）待核。","'独角戏'结构待核。"],
"sources":[src_of('kingston')],"year_source":src_of('kingston'),"author_source":src_of('kingston'),"related_works":["zhongguolao","xiangtianhuhan","luoshengmen"],
"svg":G("《孙行者》猴王结构图",[{"title":"阿新","text":"华裔的猴王（通说）","color":"main"},{"title":"伪书","text":"戏仿的底本（书名）","color":"gold"},{"title":"旧金山","text":"60年代的街头（通说）","color":"family"},{"title":"表演","text":"独白的舞台（通说）","color":"antagonist"}])},
{"id":"tilang","title":"提堂","original_title":"Bring Up the Bodies","region":"英国","era":"现当代","era_detail":"21世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mantel","author_name":"希拉里·曼特尔",
"year_display":"2012年（作者页注记：Britannica——提堂 (2012)——三部曲之一）","year_sort":2012,
"background":["作者页注记：提堂 (2012)、镜与光 (2020)——'三部曲（Britannica）'。","Britannica：曼特尔——都铎历史小说（作者页交叉——克伦威尔三部曲）。","题材（通说待核）：克伦威尔与安妮·博林的倒台——第二部。"],
"outline":["（通说待核）安妮·博林的审判：克伦威尔的织网。","（通说待核）'提堂'（Bring up the Bodies）：召唤嫌疑人。"],
"characters":[{"name":"托马斯·克伦威尔","identity":"首席国务大臣","note":"（通说待核）"},{"name":"安妮·博林","identity":"王后","note":"（通说待核）"}],
"themes":["权力机器的运转（通说待核）。",
 "'克伦威尔三部曲'之二（B注记）。",
 "历史小说的当代声誉（布克奖说——通说待核）。"],
"influence":[{"text":"Britannica：三部曲（作者页注记）。","source":src_of('mantel')},{"text":"Britannica：《狼厅》2009布克奖说（作者页交叉——待核）。","source":src_of('mantel')}],
"reading":{"difficulties":["都铎宫廷史。","'现在时'叙述（通说待核）。"],
 "editions":["《提堂》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"三部曲第二部；先读《狼厅》。"},
"pending":["2012布克奖说待核。","克伦威尔/安妮人名核对（通说）。","'三部曲'卷次核对。"],
"sources":[src_of('mantel')],"year_source":src_of('mantel'),"author_source":src_of('mantel'),"related_works":["sangeshouqiangshou","fuluosihemofang","kasiteqiaoshizhang"],
"svg":G("《提堂》权力织网图",[{"title":"克伦威尔","text":"织网的大臣（通说）","color":"main"},{"title":"安妮","text":"倒台的王后（通说）","color":"antagonist"},{"title":"都铎","text":"宫廷的舞台（通说）","color":"family"},{"title":"三部曲","text":"B注记的位置","color":"gold"}])},
{"id":"tanxiangxing","title":"檀香刑","original_title":"檀香刑","region":"中国","era":"近代","era_detail":"20世纪初",
"genre":"长篇小说","genre_group":"小说","language":"汉语","author_id":"moyan","author_name":"莫言",
"year_display":"2001年（作者页注记：Britannica——丰乳肥臀（1995）、檀香刑（2001）——年份通说待核）","year_sort":2001,
"background":["作者页注记：丰乳肥臀 (1995)、檀香刑 (2001)——'重要长篇（Britannica 列举）'。","Britannica：莫言——2012诺奖（作者页交叉——待核）。","题材（通说待核）：1900年高密——'猫腔'戏与檀香刑的酷刑美学。"],
"outline":["（通说待核）孙丙的猫腔戏与德国铁路的入侵。","（通说待核）'檀香刑'：赵甲的酷刑与眉娘的周旋。"],
"characters":[{"name":"孙丙","identity":"猫腔艺人","note":"（通说待核）"},{"name":"赵甲","identity":"刽子手","note":"（通说待核）"}],
"themes":["酷刑的展示政治（通说待核）。",
 "'猫腔'民间戏曲（通说待核）。",
 "义和团时期的乡土（通说待核）。"],
"influence":[{"text":"Britannica：'重要长篇'（作者页注记）。","source":src_of('moyan')},{"text":"Britannica：莫言2012诺奖（作者页交叉——待核）。","source":src_of('moyan')}],
"reading":{"difficulties":["'凤头—猪肚—豹尾'结构（作者自述说——待核）。","山东方言与戏文。"],
 "editions":["《檀香刑》（人民文学/作家出版社等——通说待核）。","2001年作家出版社说待核。"],
 "order":"莫言中期首选；与《丰乳肥臀》《红高粱》对读。"},
"pending":["孙丙/赵甲/眉娘人名核对（通说）。","2001年出版细节待核。","'猫腔'戏曲细节待核。"],
"sources":[src_of('moyan')],"year_source":src_of('moyan'),"author_source":src_of('moyan'),"related_works":["fengrushenbi" if "fengrushenbi" in existing else "leiyu","honggaoliang" if "honggaoliang" in existing else "kanbujian3","tanxiangxing" if False else "nongmin"],
"svg":G("《檀香刑》酷刑美学图",[{"title":"檀香刑","text":"酷刑的仪式（书名）","color":"antagonist"},{"title":"猫腔","text":"戏文的悲歌（通说）","color":"gold"},{"title":"孙丙","text":"戏子的抗争（通说）","color":"main"},{"title":"高密","text":"1900的乡土（通说）","color":"family"}])},
{"id":"aijing","title":"爱经","original_title":"Ars amatoria","region":"罗马","era":"古代","era_detail":"公元前1世纪末",
"genre":"教谕诗","genre_group":"诗歌","language":"拉丁语","author_id":"ovid","author_name":"奥维德",
"year_display":"约公元前2年（作者页注记：Britannica——爱经（Ars amatoria）——流放原因之一——年份通说待核）","year_sort":-2,
"background":["作者页注记：爱经——'（Britannica：流放原因之一）'。","Britannica：奥维德——《变形记》作者（作者页交叉）。","题材（通说待核）：求爱与保持爱——罗马宴会的'调情手册'。"],
"outline":["（通说待核）三卷：如何找到、赢得与保持爱人。","（通说待核）'库迈的门'与流放的阴影（交叉）。"],
"characters":[{"name":"教师之'我'","identity":"求爱导师","note":"（通说待核）"}],
"themes":["'爱的技艺'（B注记：Ars amatoria）。",
 "流放的'原因之一'（B注记）。",
 "奥古斯都道德立法的冲突（通说待核）。"],
"influence":[{"text":"Britannica：'流放原因之一'（作者页注记）。","source":src_of('ovid')},{"text":"Britannica：《变形记》为代表作（作者页交叉）。","source":src_of('ovid')}],
"reading":{"difficulties":["教谕诗的戏谑。","奥古斯都时代的道德法。"],
 "editions":["《爱经》中译本（人民文学等——通说待核）。","拉丁文原版（公有领域）。"],
 "order":"奥维德侧面；与《变形记》对读。"},
"pending":["三卷结构核对（通说）。","约前2年出版待核。","流放（公元8年）与本作关系待核。"],
"sources":[src_of('ovid')],"year_source":src_of('ovid'),"author_source":src_of('ovid'),"related_works":["shiyi","aigeji","leiyu"],
"svg":G("《爱经》教谕结构图",[{"title":"爱","text":"技艺的教导（书名）","color":"gold"},{"title":"罗马","text":"宴会的沙龙（通说）","color":"main"},{"title":"流放","text":"'原因之一'（B注记）","color":"antagonist"},{"title":"教谕","text":"戏谑的诗体（通说）","color":"family"}])},
{"id":"aigeji","title":"哀歌集","original_title":"Tristia","region":"罗马","era":"古代","era_detail":"公元1世纪初",
"genre":"哀歌集","genre_group":"诗歌","language":"拉丁语","author_id":"ovid","author_name":"奥维德",
"year_display":"公元8年后（作者页注记：Britannica——哀歌集（Tristia）、黑海书简——流放期作品——年份通说待核）","year_sort":8,
"background":["作者页注记：哀歌集（Tristia）、黑海书简——'流放期作品（Britannica）'。","Britannica：奥维德——公元8年被流放（作者页交叉——待核）。","题材（通说待核）：黑海托米斯的流亡诗——致奥古斯都、妻子与友人的书简。"],
"outline":["（通说待核）五卷哀歌：流亡的冬天与'棺材'自比。","（通说待核）'黑海书简'（Epistulae ex Ponto）的续写。"],
"characters":[{"name":"流亡者'我'","identity":"被放逐的诗人","note":"（通说待核）"}],
"themes":["流亡与'消逝的声名'（通说待核）。",
 "'哀歌'体的晚年（B注记）。",
 "对奥古斯都的求赦（通说待核）。"],
"influence":[{"text":"Britannica：流放期作品（作者页注记）。","source":src_of('ovid')},{"text":"Britannica：《变形记》为代表作（作者页交叉）。","source":src_of('ovid')}],
"reading":{"difficulties":["哀歌格律。","'卡门'（carmen et error）之谜（通说待核）。"],
 "editions":["《哀歌集》中译名（《悲歌》）待核。","拉丁文原版（公有领域）。"],
 "order":"奥维德晚年；与《爱经》对照。"},
"pending":["五卷结构核对（通说）。","'carmen et error'之谜待核。","公元8年流放细节待核。"],
"sources":[src_of('ovid')],"year_source":src_of('ovid'),"author_source":src_of('ovid'),"related_works":["aijing","shiyi","xuboliweng"],
"svg":G("《哀歌集》流亡结构图",[{"title":"黑海","text":"流亡的冬天（通说）","color":"antagonist"},{"title":"哀歌","text":"书简的诗体（书名）","color":"main"},{"title":"求赦","text":"致皇帝的信（通说）","color":"gold"},{"title":"声名","text":"罗马的回望（通说）","color":"family"}])},
{"id":"luxingriji","title":"旅行日记","original_title":"Journal de voyage en Italie","region":"法国","era":"近代","era_detail":"16世纪（身后1774出版）",
"genre":"日记","genre_group":"散文","language":"法语","author_id":"montaigne","author_name":"蒙田",
"year_display":"1774年出版（Britannica B296：Journal de voyage published 1774——写于1580-81说待核）","year_sort":1774,
"background":["Britannica（B296）：旅行日记——'Journal de voyage published 1774'（1774年出版）。","Britannica（B296）：蒙田——《随笔集》作者（作者页交叉）。","题材（通说待核）：1580-81年意大利之行——从巴黎经瑞士到罗马的日记（由秘书记录+亲笔后半）。"],
"outline":["（通说待核）瑞士与意大利的观察：温泉、客栈与罗马。","（通说待核）'罗马公民'荣誉与《随笔》的增订。"],
"characters":[{"name":"蒙田","identity":"旅行者","note":"（B296 语境）"}],
"themes":["'观察自己'的旅行（通说待核）。",
 "身后1774年的出版（B296）。",
 "《随笔》第三卷的母体（通说待核）。"],
"influence":[{"text":"Britannica：Journal de voyage published 1774（B296）。","source":"B296"},{"text":"Britannica：《随笔集》为代表作（B296 交叉）。","source":"B296"}],
"reading":{"difficulties":["日记的两手笔（秘书/亲笔——通说待核）。","16世纪意大利地理。"],
 "editions":["《蒙田意大利之旅》中译名（《旅行日记》）待核。","法文原版（公有领域）。"],
 "order":"蒙田侧写；与《随笔集》对读。"},
"pending":["写作年份（1580-81说）与出版年（1774——B296）双口径核对。","'罗马公民'细节待核。","秘书记录比例待核。"],
"sources":["B296"],"year_source":"B296","author_source":"B296","related_works":["suibi" if "suibi" in existing else "leiyu","renshijian","luomashi"],
"svg":G("《旅行日记》观察结构图",[{"title":"旅行","text":"意大利的道路（通说）","color":"main"},{"title":"日记","text":"观察的方法（书名）","color":"gold"},{"title":"身后","text":"1774的出版（B296）","color":"antagonist"},{"title":"随笔","text":"第三卷的母体（通说）","color":"family"}])},
{"id":"salangbo","title":"萨朗波","original_title":"Salammbô","region":"法国","era":"近代","era_detail":"19世纪60年代初",
"genre":"历史小说","genre_group":"小说","language":"法语","author_id":"flaubert","author_name":"居斯塔夫·福楼拜",
"year_display":"1862年（作者页注记：Britannica 列举——萨朗波 (1862)）","year_sort":1862,
"background":["作者页注记：萨朗波 (1862)、三故事 (1877)——'历史小说与短篇杰作（Britannica 列举）'。","Britannica：福楼拜——现代小说文体家（作者页交叉）。","题材（通说待核）：公元前3世纪迦太基雇佣兵起义——马托与萨朗波。"],
"outline":["（通说待核）雇佣兵起义：马托攻入迦太基。","（通说待核）萨朗波取回'神衣'与马托之死。"],
"characters":[{"name":"萨朗波","identity":"迦太基将军之女","note":"（通说待核）"},{"name":"马托","identity":"利比亚雇佣兵","note":"（通说待核）"}],
"themes":["'考古式'的历史小说（通说待核）。",
 "东方主义的图像（通说待核）。",
 "'神衣'的象征（通说待核）。"],
"influence":[{"text":"Britannica：'历史小说'（作者页注记）。","source":S_FL if False else src_of('flaubert')},{"text":"Britannica：福楼拜文体（作者页交叉）。","source":src_of('flaubert')}],
"reading":{"difficulties":["布匿战争史。","考古化的语言。"],
 "editions":["《萨朗波》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"福楼拜历史篇；与《情感教育》对读。"},
"pending":["萨朗波/马托人名核对（通说）。","1862年出版细节待核。","'神衣'细节待核。"],
"sources":[src_of('flaubert')],"year_source":src_of('flaubert'),"author_source":src_of('flaubert'),"related_works":["qingganjiaoyu","baofalifuren" if "baofalifuren" in existing else "baofali","mengya"],
"svg":G("《萨朗波》历史考古图",[{"title":"迦太基","text":"起义的战场（通说）","color":"antagonist"},{"title":"萨朗波","text":"神衣的守护者（通说）","color":"main"},{"title":"马托","text":"雇佣兵的爱（通说）","color":"gold"},{"title":"考古","text":"文体的雄心（通说）","color":"family"}])},
{"id":"haiBiandekafuka","title":"海边的卡夫卡","original_title":"海辺のカフカ","region":"日本","era":"现当代","era_detail":"21世纪初",
"genre":"长篇小说","genre_group":"小说","language":"日语","author_id":"murakami","author_name":"村上春树",
"year_display":"2002年（作者页注记：Britannica——海边的卡夫卡（与奇鸟并列列举）——年份通说待核）","year_sort":2002,
"background":["作者页注记：海边的卡夫卡——'（Britannica 列举——与奇鸟行状录并列）'。","Britannica：村上春树——当代日本作家（作者页语境）。","题材（通说待核）：15岁'田村卡夫卡'的出走与中田的寻猫——双线梦境。"],
"outline":["（通说待核）少年卡夫卡：俄狄浦斯预言的出走。","（通说待核）中田老人与'入口的石头'。"],
"characters":[{"name":"田村卡夫卡","identity":"15岁少年","note":"（通说待核）"},{"name":"中田","identity":"寻猫老人","note":"（通说待核）"}],
"themes":["'卡夫卡'的名字与预言（通说待核）。",
 "双线平行结构（通说待核）。",
 "战争记忆的暗渠（通说待核）。"],
"influence":[{"text":"Britannica：列举（作者页注记）。","source":src_of('murakami')},{"text":"Britannica：《挪威的森林》为代表作（作者页交叉）。","source":src_of('murakami')}],
"reading":{"difficulties":["双线的梦境逻辑。","俄狄浦斯原型（通说待核）。"],
 "editions":["《海边的卡夫卡》中译本（上海译文等——通说待核）。","日文原版。"],
 "order":"村上中期；与《奇鸟行状录》对读。"},
"pending":["2002年出版细节待核。","田村卡夫卡/中田人名核对（通说）。","'入口的石头'细节待核。"],
"sources":[src_of('murakami')],"year_source":src_of('murakami'),"author_source":src_of('murakami'),"related_works":["qiniaoxingzhuanglu","moluoyi","bianxingji"],
"svg":G("《海边的卡夫卡》双线结构图",[{"title":"少年","text":"出走的预言（通说）","color":"main"},{"title":"中田","text":"寻猫的旅程（通说）","color":"gold"},{"title":"海边","text":"两界的沙滩（通说）","color":"family"},{"title":"预言","text":"俄狄浦斯的阴影（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批53）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('eruosteya','aeschylus','俄瑞斯忒亚'),('xianrenji','mickiewicz','先人祭'),('deguoshenhua','grimm','德国神话'),('sunxingzhe','kingston','孙行者'),('tilang','mantel','提堂'),('tanxiangxing','moyan','檀香刑'),('aijing','ovid','爱经'),('aigeji','ovid','哀歌集'),('luxingriji','montaigne','旅行日记'),('salangbo','flaubert','萨朗波'),('haiBiandekafuka','murakami','海边的卡夫卡')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH53 DONE')
