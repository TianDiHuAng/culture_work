# -*- coding: utf-8 -*-
"""批38：零成本 10 部（2666/群众与权力/寒冬夜行人/树上的男爵/日出/蒂凡尼的早餐/我的米海尔/都是我的儿子/万尼亚舅舅/狗心）"""
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
# 1. 波拉尼奥《2666》
{"id":"erliuliu","title":"2666","original_title":"2666","region":"智利","era":"现当代","era_detail":"21世纪初（身后出版）",
"genre":"长篇小说（五部曲结构）","genre_group":"小说","language":"西班牙语","author_id":"bolano","author_name":"罗贝托·波拉尼奥",
"year_display":"2004年（作者页注记：Britannica——2004 身后出版，鸿篇巨制）","year_sort":2004,
"background":["作者页注记：2666——'（Britannica：2004 身后出版，鸿篇巨制）'。","Britannica：波拉尼奥——智利作家（作者页语境）。","题材（通说待核）：五位学者追踪神秘作家阿琴波尔迪——圣特莱萨的连续凶案。"],
"outline":["（通说待核——Britannica未载剧情）五部结构：学者/阴谋/记者/凶案/阿琴波尔迪。","（通说待核）边境城市圣特莱萨的女性连环被害。"],
"characters":[{"name":"阿琴波尔迪","identity":"神秘作家","note":"（通说待核）"}],
"themes":["暴力档案化的书写（通说待核）。",
 "文学与罪的关系（通说待核）。",
 "'鸿篇巨制'的未完成性（Britannica：身后出版——注记）。"],
"influence":[{"text":"Britannica：'2004 身后出版，鸿篇巨制'（作者页注记）。","source":src_of('bolano')},{"text":"Britannica：波拉尼奥为当代西语文学代表（作者页语境）。","source":src_of('bolano')}],
"reading":{"difficulties":["五部曲的多线程。","墨西哥边境史（华雷斯案原型——通说待核）。"],
 "editions":["《2666》中译本（上海人民出版社等——通说待核）。","西班牙文原版。"],
 "order":"波拉尼奥收官；与《荒野侦探》对读。"},
"pending":["五部曲各部标题核对（通说）。","阿琴波尔迪人名核对。","2004年出版（Anagrama说）待核。"],
"sources":[src_of('bolano')],"year_source":src_of('bolano'),"author_source":src_of('bolano'),"related_works":["huangyezhentan","meiguobuqu","xueseziwuxian"],
"svg":G("《2666》五部结构图",[{"title":"学者","text":"追踪的起点（通说）","color":"main"},{"title":"凶案","text":"边境的档案（通说）","color":"antagonist"},{"title":"阿琴波尔迪","text":"神秘的作家（通说）","color":"gold"},{"title":"身后","text":"2004 出版（Britannica）","color":"family"}])},
# 2. 卡内蒂《群众与权力》
{"id":"qunzhongyuquanli","title":"群众与权力","original_title":"Masse und Macht","region":"奥地利","era":"现当代","era_detail":"20世纪60年代",
"genre":"论著","genre_group":"散文","language":"德语","author_id":"canetti","author_name":"埃利亚斯·卡内蒂",
"year_display":"1960年（Britannica B312：Masse und Macht (1960)——'His major work'）","year_sort":1960,
"background":["Britannica（B312）：Masse und Macht (1960)——'His major work'（其巨著）。","Britannica（B312）：卡内蒂——1981诺奖（与布罗赫并列条目口径——covers: singer, canetti）。","题材（通说待核）：群众的类型学与权力的象征——人类学式的政体解剖。"],
"outline":["（通说待核）群众四类型：环形/开放/猎捕/内聚（分类通说待核）。","（通说待核）权力的想象学：幸存者与命令。"],
"characters":[{"name":"（论著无人物）","identity":"——","note":"人类学式论著"}],
"themes":["群众心理学（B312：major work 定位）。",
 "权力的符号学（通说待核）。",
 "幸存者作为权力原型（通说待核）。"],
"influence":[{"text":"Britannica：'His major work'（B312）。","source":"B312"},{"text":"Britannica：1981诺奖交叉（B312 口径）。","source":"B312"}],
"reading":{"difficulties":["人类学式的分类体系。","多文明材料的并置。"],
 "editions":["《群众与权力》中译本（广西师大等——通说待核）。","德文原版。"],
 "order":"卡内蒂首选；与《迷惘》对读。"},
"pending":["群众分类术语核对（通说）。","1960年出版（Hanser说）待核。","诺奖授奖词引用待核。"],
"sources":["B312"],"year_source":"B312","author_source":"B312","related_works":["miwang","leiyu","aiyuheandegushi"],
"svg":G("《群众与权力》解剖结构图",[{"title":"群众","text":"四类型学（通说）","color":"main"},{"title":"权力","text":"幸存者的符号（通说）","color":"antagonist"},{"title":"命令","text":"权力的话语（通说）","color":"gold"},{"title":"人类学","text":"跨文明的材料（通说）","color":"family"}])},
# 3. 卡尔维诺《寒冬夜行人》
{"id":"handongyexingren","title":"寒冬夜行人","original_title":"Se una notte d'inverno un viaggiatore","region":"意大利","era":"现当代","era_detail":"20世纪70年代末",
"genre":"长篇小说（元小说）","genre_group":"小说","language":"意大利语","author_id":"calvino","author_name":"伊塔洛·卡尔维诺",
"year_display":"1979年（作者页注记：Britannica 列举——元小说的百科）","year_sort":1979,
"background":["作者页注记：寒冬夜行人 (1979)——'元小说的百科（Britannica 列举）'。","Britannica：卡尔维诺——寓言式想象与后现代实验（作者页语境——待核）。","题材（通说待核）：'你'与'另一位读者'追寻被装订错误的十部小说开头。"],
"outline":["（通说待核）十部互不相关的小说开头与读者追寻的框架。","（通说待核）'读者'与'另一位读者'的相遇。"],
"characters":[{"name":"'你'","identity":"读者","note":"（通说待核）"},{"name":"柳德米拉","identity":"另一位读者","note":"（通说待核）"}],
"themes":["阅读行为本身作为小说（书名语境——通说待核）。",
 "开头的诱惑与延宕（通说待核）。",
 "作者—读者—出版商的循环（通说待核）。"],
"influence":[{"text":"Britannica：'元小说的百科'（作者页注记）。","source":src_of('calvino')},{"text":"Britannica：卡尔维诺为寓言式想象大师（作者页语境）。","source":src_of('calvino')}],
"reading":{"difficulties":["第二人称叙述。","十种文体的戏仿。"],
 "editions":["《寒冬夜行人》中译名（《如果在冬夜，一个旅人》两说）待核。","意大利文原版。"],
 "order":"卡尔维诺实验首选。"},
"pending":["十个开头篇名核对（通说）。","1979年出版（Einaudi说）待核。","'另一位读者'人名待核。"],
"sources":[src_of('calvino')],"year_source":src_of('calvino'),"author_source":src_of('calvino'),"related_works":["shushangdenanjue","bukesh","shizhangshijieshi"],
"svg":G("《寒冬夜行人》元小说结构图",[{"title":"'你'","text":"追寻的读者（通说）","color":"main"},{"title":"十部开头","text":"延宕的小说（通说）","color":"gold"},{"title":"元小说","text":"阅读的自我指涉（B注记）","color":"antagonist"},{"title":"相遇","text":"读者的爱情（通说）","color":"family"}])},
# 4. 卡尔维诺《树上的男爵》
{"id":"shushangdenanjue","title":"树上的男爵","original_title":"Il barone rampante","region":"意大利","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"calvino","author_name":"伊塔洛·卡尔维诺",
"year_display":"1957年（作者页注记：Britannica 列举——寓言三部曲之巅）","year_sort":1957,
"background":["作者页注记：树上的男爵 (1957)——'寓言三部曲之巅（Britannica 列举）'。","Britannica：卡尔维诺——寓言与想象的书写者（作者页语境）。","题材（通说待核）：科希莫·皮奥瓦斯科自十二岁起终身栖居树上。"],
"outline":["（通说待核）科希莫上树——对家庭与社会的拒斥。","（通说待核）树上的启蒙：读书、恋爱与革命。"],
"characters":[{"name":"科希莫","identity":"树上的男爵","note":"（通说待核）"},{"name":"薇奥拉","identity":"邻家少女","note":"（通说待核）"}],
"themes":["'在树上'——非逃逸的抵抗（通说待核）。",
 "启蒙时代与贵族的终结（背景通说待核）。",
 "寓言三部的位置（Britannica：三部曲——注记）。"],
"influence":[{"text":"Britannica：'寓言三部曲之巅'（作者页注记）。","source":src_of('calvino')},{"text":"Britannica：卡尔维诺1985年离世前未诺奖（作者页语境——不采）。","source":src_of('calvino')}],
"reading":{"difficulties":["寓言化的18世纪背景。","'树上'的空间象征。"],
 "editions":["《树上的男爵》中译本（译林/人民文学等——通说待核）。","意大利文原版。"],
 "order":"卡尔维诺入门首选。"},
"pending":["科希莫/薇奥拉人名核对（通说）。","'三部曲'其余两部（《分成两半的子爵》《不存在的骑士》）待核。","1957年出版细节待核。"],
"sources":[src_of('calvino')],"year_source":src_of('calvino'),"author_source":src_of('calvino'),"related_works":["handongyexingren","bukesh","xuboliweng"],
"svg":G("《树上的男爵》树上结构图",[{"title":"科希莫","text":"终身在树上（通说）","color":"main"},{"title":"树冠","text":"社会的边界（通说）","color":"gold"},{"title":"启蒙","text":"读书与恋爱（通说）","color":"family"},{"title":"地面","text":"被拒斥的世界（通说）","color":"antagonist"}])},
# 5. 曹禺《日出》
{"id":"richu","title":"日出","original_title":"日出","region":"中国","era":"近代","era_detail":"20世纪30年代",
"genre":"戏剧","genre_group":"戏剧","language":"汉语","author_id":"caoyu","author_name":"曹禺",
"year_display":"1936年（作者页注记：Britannica 列举——日出 (1936)）","year_sort":1936,
"background":["作者页注记：日出 (1936)——''损不足以奉有余'的社会悲剧（Britannica 列举）'。","Britannica：曹禺——现代中国戏剧奠基人（作者页语境——待核）。","题材（通说待核）：大旅馆与下等妓院的空间对照——交际花陈白露的黄昏与日出。"],
"outline":["（通说待核）陈白露的沉沦与'日出'的呼唤。","（通说待核）打夯工人的歌声作为结尾象征。"],
"characters":[{"name":"陈白露","identity":"交际花","note":"（通说待核）"},{"name":"方达生","identity":"旧日恋人","note":"（通说待核）"}],
"themes":["'损不足以奉有余'（Britannica 引语——注记）。",
 "都市空间的阶级对照（通说待核）。",
 "女性悲剧与时代（通说待核）。"],
"influence":[{"text":"Britannica：'损不足以奉有余'（作者页注记）。","source":src_of('caoyu')},{"text":"Britannica：曹禺戏剧四部之一（作者页语境）。","source":src_of('caoyu')}],
"reading":{"difficulties":["1930年代天津都市背景（通说待核）。","'横断面'结构（人像展览式——通说待核）。"],
 "editions":["《日出》（人民文学出版社《曹禺戏剧集》等——通说待核）。","1936年《文季》连载说待核。"],
 "order":"曹禺第二剧；与《雷雨》《北京人》对读。"},
"pending":["陈白露/方达生人名核对（通说）。","1936年发表细节待核。","'人像展览式'结构说法待核。"],
"sources":[src_of('caoyu')],"year_source":src_of('caoyu'),"author_source":src_of('caoyu'),"related_works":["leiyu","beijingren","yuwanghaojieche"],
"svg":G("《日出》阶级对照图",[{"title":"陈白露","text":"黄昏的交际花（通说）","color":"main"},{"title":"大旅馆","text":"'有余'的世界（通说）","color":"antagonist"},{"title":"打夯歌","text":"'日出'的呼唤（通说）","color":"gold"},{"title":"损不足","text":"奉有余的社会（B注记）","color":"family"}])},
# 6. 卡波特《蒂凡尼的早餐》
{"id":"difannidezaocan","title":"蒂凡尼的早餐","original_title":"Breakfast at Tiffany's","region":"美国","era":"现当代","era_detail":"20世纪50年代末",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"capote","author_name":"杜鲁门·卡波特",
"year_display":"1958年（Britannica B332：Breakfast at Tiffany's (1958)）","year_sort":1958,
"background":["Britannica（B332）：Breakfast at Tiffany's——Holly Golightly——'a young fey café society girl'（B332）。","Britannica（B332）：卡波特——'nonfiction novel'的先驱；In Cold Blood 为其巅峰（交叉）。","题材（通说待核）：纽约'unamed nameless'叙述者眼中的霍莉——野性、漂泊与'蒂凡尼'的安宁想象。"],
"outline":["（通说待核——B332未载剧情）霍莉与叙述者的公寓友谊与她的消失。","（通说待核）'蒂凡尼'：不上锁的安宁想象。"],
"characters":[{"name":"霍莉·戈莱特利","identity":"café society girl","note":"（B332：Holly Golightly——'a young fey café society girl'）"},{"name":"叙述者","identity":"作家","note":"（通说待核，B332未载）"}],
"themes":["漂泊与归属（通说待核）。",
 "'蒂凡尼'：消费时代的安宁想象（通说待核）。",
 "纽约战后都市风情（B332 语境）。"],
"influence":[{"text":"Britannica：'a young fey café society girl'（B332）。","source":"B332"},{"text":"Britannica：卡波特 In Cold Blood 为'nonfiction novel'巅峰（B332 交叉）。","source":"B332"}],
"reading":{"difficulties":["'café society'语境。","第一人称回忆框架。"],
 "editions":["《蒂凡尼的早餐》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"卡波特入门首选；后接《冷血》。"},
"pending":["霍莉人名核对（B332拼写）。","1961年电影改编（奥黛丽·赫本说）待核。","1958年出版细节待核。"],
"sources":["B332"],"year_source":"B332","author_source":"B332","related_works":["lengxue","biedeshengyin","leiyu"],
"svg":G("《蒂凡尼的早餐》漂泊结构图",[{"title":"霍莉","text":"café society girl（B332）","color":"main"},{"title":"纽约","text":"战后的漂泊（通说）","color":"family"},{"title":"蒂凡尼","text":"安宁的想象（通说）","color":"gold"},{"title":"消失","text":"无名的去向（通说）","color":"antagonist"}])},
# 7. 奥兹《我的米海尔》
{"id":"wodemihaier","title":"我的米海尔","original_title":"Mikhaʾel sheli","region":"以色列","era":"现当代","era_detail":"20世纪60年代末",
"genre":"长篇小说","genre_group":"小说","language":"希伯来语","author_id":"aoz","author_name":"阿摩司·奥兹",
"year_display":"1968年（Britannica B329：My Michael (1968)）","year_sort":1968,
"background":["Britannica（B329）：My Michael (1968)——Britannica 列举。","Britannica（B329）：奥兹——'in whose works Israeli society is unapologetically scrutinized'。","题材（通说待核）：汉娜的独白——对地质学家丈夫米海尔的想象与疏离。"],
"outline":["（通说待核——B329未载剧情）汉娜的第一人称独白与白日梦。","（通说待核）耶路撒冷的阿拉伯邻居双胞胎意象。"],
"characters":[{"name":"汉娜","identity":"叙述者","note":"（通说待核，B329未载）"},{"name":"米海尔","identity":"丈夫","note":"（B329 书名人物）"}],
"themes":["婚姻内部的疏离（通说待核）。",
 "女性欲望的书写（通说待核）。",
 "耶路撒冷的政治潜流（B329：society scrutinized 语系）。"],
"influence":[{"text":"Britannica：奥兹作品序列（B329）。","source":"B329"},{"text":"Britannica：'unapologetically scrutinized'（B329）。","source":"B329"}],
"reading":{"difficulties":["女性独白的不可靠性。","1950年代耶路撒冷背景。"],
 "editions":["《我的米海尔》中译本（译林出版社等——通说待核）。","希伯来文原版。"],
 "order":"奥兹早期首选；与《爱与黑暗的故事》对读。"},
"pending":["汉娜/米海尔人名核对（B329未载细节）。","1968年出版（Am Oved说）待核。","双胞胎意象细节待核。"],
"sources":["B329"],"year_source":"B329","author_source":"B329","related_works":["aiyuheandegushi","youda","leiyu"],
"svg":G("《我的米海尔》独白结构图",[{"title":"汉娜","text":"独白的洪流（通说）","color":"main"},{"title":"米海尔","text":"沉默的丈夫（B329书名）","color":"family"},{"title":"耶路撒冷","text":"政治的潜流（B329）","color":"antagonist"},{"title":"白日梦","text":"欲望的通道（通说）","color":"gold"}])},
# 8. 米勒《都是我的儿子》
{"id":"doushiwodeerzi","title":"都是我的儿子","original_title":"All My Sons","region":"美国","era":"现当代","era_detail":"20世纪40年代",
"genre":"戏剧","genre_group":"戏剧","language":"英语","author_id":"amiller","author_name":"阿瑟·米勒",
"year_display":"1947年（Britannica B325：All My Sons (1947)——第一部重要剧作获Tony奖）","year_sort":1947,
"background":["Britannica（B325）：All My Sons——'first important play, won a Tony'。","Britannica（B325）：米勒把'普通人'置于悲剧中心。","题材（通说待核）：战争期间发售缺陷气缸的工厂主乔·凯勒——利润与责任。"],
"outline":["（通说待核——B325未载剧情）凯勒家的秘密与阵亡飞行员。","（通说待核）'都是我的儿子'：责任的普遍化。"],
"characters":[{"name":"乔·凯勒","identity":"工厂主","note":"（通说待核，B325未载）"},{"name":"克里斯","identity":"儿子","note":"（通说待核，B325未载）"}],
"themes":["社会责任与家庭神话（通说待核）。",
 "'普通人'的道德重量（B325）。",
 "战争经济的伦理（通说待核）。"],
"influence":[{"text":"Britannica：All My Sons (1947)——'first important play, won a Tony'（B325）。","source":"B325"},{"text":"Britannica：《推销员之死》为其巅峰（B325 交叉）。","source":"B325"}],
"reading":{"difficulties":["易卜生式回溯结构（通说待核）。","二战军需工业背景。"],
 "editions":["《都是我的儿子》中译本（人民文学《阿瑟·米勒戏剧集》等——通说待核）。","英文原版。"],
 "order":"米勒成名作；后接《推销员之死》。"},
"pending":["乔·凯勒/克里斯/拉里人名核对（B325未载）。","1947年首演（Coronet Theatre说）待核。","Tony奖类别待核。"],
"sources":["B325"],"year_source":"B325","author_source":"B325","related_works":["tuixiaoyuanzhisi","salemwunv","leiyu"],
"svg":G("《都是我的儿子》责任结构图",[{"title":"乔·凯勒","text":"发战争财的父亲（通说）","color":"antagonist"},{"title":"阵亡者","text":"'我的儿子们'（通说）","color":"main"},{"title":"秘密","text":"信件的真相（通说）","color":"gold"},{"title":"责任","text":"普通人道德（B325）","color":"family"}])},
# 9. 契诃夫《万尼亚舅舅》
{"id":"wanyaniuju","title":"万尼亚舅舅","original_title":"Дядя Ваня（Uncle Vanya）","region":"俄国","era":"近代","era_detail":"19世纪末",
"genre":"戏剧","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
"year_display":"1897年（Britannica：Uncle Vanya (1897)——契诃夫页列举）","year_sort":1897,
"background":["Britannica：Uncle Vanya (1897)——契诃夫页列举（B-契诃夫页）。","Britannica：'Chekhovs gun'与'what is left unsaid'（作者页口径——B270交叉）。","题材（通说待核）：庄园的冗日——沃伊尼茨基的幻灭与教授的抵达。"],
"outline":["（通说待核）万尼亚为教授操劳半生的觉醒。","（通说待核）叶列娜与医生阿斯特罗夫的三角。"],
"characters":[{"name":"万尼亚","identity":"庄园管家","note":"（B 书名人物）"},{"name":"阿斯特罗夫","identity":"医生","note":"（通说待核）"}],
"themes":["幻灭与日常（通说待核）。",
 "'未说出之重'（B270 交叉）。",
 "庄园经济的黄昏（通说待核）。"],
"influence":[{"text":"Britannica：契诃夫戏剧四部之一（B270 交叉）。","source":"B270"},{"text":"Britannica：1897年（契诃夫页列举）。","source":"B270"}],
"reading":{"difficulties":["'潜台词'的表演。","俄国庄园社会（通说待核）。"],
 "editions":["《万尼亚舅舅》（人民文学出版社《契诃夫戏剧集》——通说待核）。","俄文原版（公有领域）。"],
 "order":"契诃夫戏剧之二；与《海鸥》《樱桃园》对读。"},
"pending":["1897年出版/首演年份核对（B口径）。","沃伊尼茨基/阿斯特罗夫人名核对（通说）。","1899年首演说待核。"],
"sources":["B270"],"year_source":"B270","author_source":"B270","related_works":["haiou","yingtaoyuan","leiyu"],
"svg":G("《万尼亚舅舅》幻灭结构图",[{"title":"万尼亚","text":"半生操劳的觉醒（通说）","color":"main"},{"title":"教授","text":"寄生的权威（通说）","color":"antagonist"},{"title":"庄园","text":"冗日的黄昏（通说）","color":"family"},{"title":"潜台词","text":"'未说出之重'（B270）","color":"gold"}])},
# 10. 布尔加科夫《狗心》
{"id":"gouxin","title":"狗心","original_title":"Собачье сердце","region":"苏联","era":"近代","era_detail":"20世纪20年代",
"genre":"中篇小说","genre_group":"小说","language":"俄语","author_id":"bulgakov","author_name":"米哈伊尔·布尔加科夫",
"year_display":"1925年（作者页注记：Britannica——狗心 (1925)）","year_sort":1925,
"background":["作者页注记：狗心——'（Britannica：1925）'。","Britannica：布尔加科夫——《大师与玛格丽特》作者、苏联时期被禁（作者页语境——待核）。","题材（通说待核）：教授普列奥布拉任斯基把狗'改造'成人——新苏联人的讽刺实验。"],
"outline":["（通说待核）沙里克：从流浪狗到'新公民'的堕落改造。","（通说待核）'手术'的逆转与社会讽刺。"],
"characters":[{"name":"普列奥布拉任斯基","identity":"教授","note":"（通说待核）"},{"name":"沙里克","identity":"狗/人","note":"（通说待核）"}],
"themes":["'新人类'工程的讽刺（通说待核）。",
 "科学实验的伦理（通说待核）。",
 "苏维埃日常的怪诞（作者页语境）。"],
"influence":[{"text":"Britannica：狗心 (1925)（作者页注记）。","source":src_of('bulgakov')},{"text":"Britannica：布尔加科夫《大师与玛格丽特》作者（作者页交叉）。","source":src_of('bulgakov')}],
"reading":{"difficulties":["讽刺的寓言层次。","1920年代新经济政策时期（通说待核）。"],
 "editions":["《狗心》中译本（人民文学/上海译文等——通说待核）。","俄文原版。"],
 "order":"布尔加科夫入门；后接《大师与玛格丽特》。"},
"pending":["普列奥布拉任斯基/沙里科夫名核对（通说）。","1925年写作、1987年苏联发表说待核。","电影改编（1988说）待核。"],
"sources":[src_of('bulgakov')],"year_source":src_of('bulgakov'),"author_source":src_of('bulgakov'),"related_works":["dashiyumagelit","chengbao","bianxingji"],
"svg":G("《狗心》讽刺实验图",[{"title":"手术","text":"狗变成人（通说）","color":"gold"},{"title":"沙里克","text":"'新公民'的堕落（通说）","color":"antagonist"},{"title":"教授","text":"科学的傲慢（通说）","color":"main"},{"title":"讽刺","text":"苏维埃日常（B注记）","color":"family"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批38）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('erliuliu','bolano','2666'),('qunzhongyuquanli','canetti','群众与权力'),('handongyexingren','calvino','寒冬夜行人'),('shushangdenanjue','calvino','树上的男爵'),('richu','caoyu','日出'),('difannidezaocan','capote','蒂凡尼'),('wodemihaier','aoz','我的米海尔'),('doushiwodeerzi','amiller','都是我的儿子'),('wanyaniuju','chikefu','万尼亚舅舅'),('gouxin','bulgakov','狗心')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH38 DONE')
