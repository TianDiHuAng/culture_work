# -*- coding: utf-8 -*-
"""连续扩充：零成本直写全部剩余"""
import json, pathlib

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

def mk(id_, title, orig, region, era, ed, genre, gg, lang, aid, aname, yd, ys, bg, outline, chars, themes, inf, read, pend, srcs, ysrc, asrc, rel, svg):
    return {"id":id_,"title":title,"original_title":orig,"region":region,"era":era,"era_detail":ed,
"genre":genre,"genre_group":gg,"language":lang,"author_id":aid,"author_name":aname,"year_display":yd,"year_sort":ys,
"background":bg,"outline":outline,"characters":chars,"themes":themes,"influence":inf,"reading":read,"pending":pend,
"sources":srcs,"year_source":ysrc,"author_source":asrc,"related_works":rel,"svg":svg}

W = []

# 1. 弗兰妮与祖伊
W.append(mk("funniyuzuyi","弗兰妮与祖伊","Franny and Zooey","美国","现当代","20世纪","中篇二部合刊","小说","英语","salinger","J.D.塞林格","1961年（Britannica B319：Franny and Zooey (1961)）",1961,
["Britannica（B319）：Franny and Zooey (1961)——塞林格格拉斯家族系列之一；B319：'After the success of The Catcher in the Rye, Salinger became a recluse'。","题材（通说待核）：弗兰妮的精神危机与祖伊的开导——格拉斯家族最小的两兄妹。"],
["弗兰妮的崩溃与祖伊的开导（通说待核）。"],
[{"name":"弗兰妮","identity":"大学生","note":"（通说待核）"},{"name":"祖伊","identity":"演员","note":"（通说待核）"}],
["格拉斯家族的精神危机（通说待核）。","宗教与世俗的对立（通说待核）。"],
[{"text":"Britannica：Franny and Zooey (1961)——'all three books were best-sellers'（B319）。","source":"B319"},{"text":"作者页：塞林格1953年后隐居（B319：became a recluse）。","source":"B319"}],
{"difficulties":["对话的密度。","宗教语境。"],"editions":["《弗兰妮与祖伊》（人民文学出版社/译林出版社版本，通说待核）。","英文原版。"],"order":"《九故事》后读。"},
["1961年出版（Little, Brown说）核对。","弗兰妮/祖伊人名核对。","'耶稣祈祷词'细节待核。"],
["B319"],"B319","B319",["maitian","jiugushi","haorennanxun"],
G("格拉斯家族图",[{"title":"弗兰妮","text":"崩溃的周末","color":"main"},{"title":"祖伊","text":"哥哥的开导","color":"family"},{"title":"格拉斯家族","text":"七兄妹（通说）","color":"gold"},{"title":"宗教","text":"灵性的寻找","color":"plain"}])))

# 2. 权力与荣耀
W.append(mk("quanliyurongyao","权力与荣耀","The Power and the Glory","英国","现当代","20世纪","长篇小说","小说","英语","greene","格雷厄姆·格林","1940年（Britannica B320：The Power and the Glory (1940)）",1940,
["Britannica（B320）：'Many of his best-known works, including The Power and the Glory (1940)……center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'。","题材（通说待核）：墨西哥革命时期一名威士忌神父的逃亡——'威士忌神父'的殉道。"],
["无名神父在宗教迫害下逃亡——最终自愿返回送死（通说待核）。"],
[{"name":"神父","identity":"天主教神父","note":"（通说待核）"},{"name":"中尉","identity":"追捕者","note":"（通说待核）"}],
["信仰与迫害（通说待核）。","'恶'作为可感的实在（B320：evil as a palpable force）。","殉道的含混性（通说待核）。"],
[{"text":"Britannica：'The Power and the Glory (1940)……center on Roman Catholic themes'（B320）。","source":"B320"},{"text":"Britannica：格林'one of the most widely read British novelists of the 20th century'（B320 作者级）。","source":"B320"}],
{"difficulties":["天主教语境。","墨西哥革命史。"],"editions":["《权力与荣耀》（人民文学出版社/上海译文版本，通说待核）。","英文原版。"],"order":"格林代表作。"},
["1940年出版（Heinemann说）核对。","神父/中尉人名核对。","'威士忌神父'绰号待核。"],
["B320"],"B320","B320",["lianqingdezhongjie","muqin_brecht","fengsheng"],
G("殉道结构图",[{"title":"逃亡","text":"威士忌神父","color":"main"},{"title":"追捕","text":"中尉的追踪","color":"antagonist"},{"title":"殉道","text":"信仰的代价","color":"gold"},{"title":"天主教","text":"B320 主题","color":"family"}])))

# 3. 一个青年艺术家的画像
W.append(mk("yigepingnianyishujiadehuaxiang","一个青年艺术家的画像","A Portrait of the Artist as a Young Man","爱尔兰","现当代","20世纪初","长篇小说","小说","英语","joyce","詹姆斯·乔伊斯","1916年（作者页B321口径：A Portrait of the Artist as a Young Man (1916)）",1916,
["Britannica（B321）：乔伊斯 major works 含'A Portrait of the Artist as a Young Man (1916)'（B321 作者页定位）。","作者（B321）：'His literary masterpiece is Ulysses (1922)'；Dubliners (1914)。","题材（通说待核）：斯蒂芬·迪达勒斯从童年到大学的成长——'艺术家画像'的自传性小说。"],
["斯蒂芬·迪达勒斯：从童年到大学——宗教、家庭、艺术的觉醒（通说待核）。"],
[{"name":"斯蒂芬·迪达勒斯","identity":"青年","note":"（通说待核）"}],
["成长小说与艺术觉醒（通说待核）。","'流亡即我的艺术'（通说待核）。","意识流前奏（通说）。"],
[{"text":"作者页：乔伊斯代表作（B321 作者页口径）。","source":"B321"},{"text":"作者页：乔伊斯'His literary masterpiece is Ulysses'（B321 作者级）。","source":"B321"}],
{"difficulties":["意识流前奏的叙事。","爱尔兰天主教背景。"],"editions":["《一个青年艺术家的画像》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域渐近）。"],"order":"先《都柏林人》后本作→《尤利西斯》。"},
["1916年出版（B.W. Huebsch说）核对。","斯蒂芬·迪达勒斯人名核对。","'流亡即我的艺术'出处待核。"],
["B321"],"B321","B321",["dubolinen","youlisisi","luoshengmen"],
G("成长结构图",[{"title":"童年","text":"教会学校","color":"family"},{"title":"觉醒","text":"性与宗教","color":"main"},{"title":"流亡","text":"'流亡即我的艺术'（通说）","color":"gold"},{"title":"艺术家","text":"画像的完成","color":"plain"}])))

# 4. 背德者
W.append(mk("beidezhe","背德者","L'Immoraliste（The Immoralist）","法国","现当代","20世纪","中篇小说","小说","法语","gide","安德烈·纪德","1902年（作者页B275口径：L'Immoraliste (1902)——创作盛期之作）",1902,
["Britannica（B275）：纪德 major_works 载'L'Immoraliste (1902)'——'the page lists it among works from his great creative period'（创作盛期——B275）；'the point at which concern for the self must be superseded by moral principles'（B275 问答）。","纪德（B275）：1947年诺奖。"],
["米歇尔的北非觉醒与自我放纵（通说待核）。"],
[{"name":"米歇尔","identity":"学者","note":"（通说待核）"},{"name":"玛尔塞拉","identity":"妻子","note":"（通说待核）"}],
["自我的觉醒与'背德'（B275：moral ambiguity 语境）。","北非的身体苏醒（通说待核）。","'自我关切与道德原则'的边界（B275 问答）。"],
[{"text":"作者页：纪德创作盛期之作（B275 作者页口径）。","source":"B275"},{"text":"Britannica：纪德1947年诺奖（B275 作者级）。","source":"B275"}],
{"difficulties":["'背德'的伦理阅读。","殖民地北非背景。"],"editions":["《背德者》（人民文学出版社/上海译文版本，通说待核）。","法文原版（Gallimard）。"],"order":"先《窄门》后本作（两极对照）。"},
["1902年出版（Mercure de France说）核对。","米歇尔/玛尔塞拉人名核对。","与《窄门》的对位（作者婚姻语境——B275 已载）待核。"],
["B275"],"B275","B275",["weibizaozhe","xianzhi","duoluo"],
G("觉醒结构图",[{"title":"北非","text":"身体的苏醒","color":"family"},{"title":"米歇尔","text":"自我的放纵","color":"main"},{"title":"玛尔塞拉","text":"病与死","color":"antagonist"},{"title":"背德","text":"道德的边界（B275）","color":"gold"}])))

# 5. 送冰的人来了
W.append(mk("songbingerenlaile","送冰的人来了","The Iceman Cometh","美国","现当代","20世纪","戏剧","戏剧","英语","ONeill","尤金·奥尼尔","1946年（作者页B272口径：The Iceman Cometh (1946)——'Considered by many to be ONeill's finest work'——页面问答）",1946,
["Britannica（B272）：The Iceman Cometh (1946)——'Considered by many to be ONeill's finest work'（页面问答——B272）。","作者（B272）：四项普利策戏剧奖；1936诺奖。","场景（通说待核）：纽约一间酒吧的酒鬼群像——希基的'福音'与幻灭。"],
["希基的到来：酒吧酒鬼们的幻灭——'没有明天'（通说待核）。"],
[{"name":"希基","identity":"推销员","note":"（通说待核）"},{"name":"哈里·霍普","identity":"酒吧主","note":"（通说待核）"}],
["' pipe dream'（白日梦）的幻灭（通说待核）。","推销员的'福音'：放弃希望即自由（通说待核）。","酒鬼群像的悲剧（通说）。"],
[{"text":"Britannica：'Considered by many to be ONeill's finest work'（B272 页面问答）。","source":"B272"},{"text":"Britannica：奥尼尔1936诺奖、四项普利策奖（B272）。","source":"B272"}],
{"difficulties":["酒鬼群像的人物表。","'白日梦'的戏剧概念。"],"editions":["《送冰的人来了》（人民文学出版社/湖南文艺出版社版本，通说待核）。","英文原版（Yale）。"],"order":"奥尼尔晚期杰作。"},
["1946年首演（Martin Beck Theatre说）核对。","希基/哈里·霍普人名核对。","'pipe dream'术语核对。"],
["B272"],"B272","B272",["manchangdeheian","leiyu","dengdaigou"],
G("酒吧群像图",[{"title":"希基","text":"送冰的推销员（通说）","color":"main"},{"title":"酒吧","text":"酒鬼的避难所","color":"family"},{"title":"pipe dream","text":"白日梦（通说）","color":"gold"},{"title":"幻灭","text":"希望的终结","color":"antagonist"}])))

# 6. 美国的悲剧
W.append(mk("meiguodebeiju","美国的悲剧","An American Tragedy","美国","现当代","20世纪","长篇小说","小说","英语","delaise","西奥多·德莱塞","1925年（作者页B280口径：An American Tragedy (1925)——'brought Dreiser a degree of critical and commercial success he had never before attained'）",1925,
["Britannica（B280）：'In 1925 Dreiser's first novel in a decade, An American Tragedy, based on a celebrated murder case, was published'；'This book brought Dreiser a degree of critical and commercial success he had never before attained'。","题材（通说待核）：克莱德·格里菲思的犯罪与处决——美国梦的黑暗面。","'The book's highly critical view of the American legal system also made him the adopted champion of social reformers.'（B280）。"],
["克莱德的阶级攀附与谋杀：美国梦的黑暗面（通说待核）。"],
[{"name":"克莱德·格里菲思","identity":"青年","note":"（通说待核）"},{"name":"桑德拉","identity":"富家女","note":"（通说待核）"}],
["美国梦的黑暗面（B280：critical view of the American legal system）。",
"自然主义：'determinism'（B280）。",
"阶级与欲望（通说待核）。"],
[{"text":"Britannica：'brought Dreiser a degree of critical and commercial success he had never before attained'（B280）。","source":"B280"},{"text":"Britannica：'adopted champion of social reformers'（B280）。","source":"B280"}],
{"difficulties":["长篇的体量（两卷）。","1920年代美国社会。"],"editions":["《美国的悲剧》（人民文学出版社，通说待核）。","英文原版（公有领域渐近）。"],"order":"德莱塞代表作。"},
["1925年出版（Bonif & Liveright说）核对。","克莱德/桑德拉人名核对。","两卷本结构待核。"],
["B280"],"B280","B280",["jialimeimei","fenwangyu","taiyangzhaochangshengqi"],
G("美国梦黑暗面图",[{"title":"克莱德","text":"阶级的攀附","color":"main"},{"title":"谋杀","text":"欲望的代价","color":"antagonist"},{"title":"审判","text":"法律的虚伪（B280）","color":"gold"},{"title":"美国梦","text":"黑暗的一面","color":"family"}])))

# 7. 权力与荣耀（同上#2）→ 跳过（已写）
# 8. 苔蕾丝·德斯盖鲁
W.append(mk("taileisi","苔蕾丝·德斯盖鲁","Thérèse Desqueyroux","法国","现当代","20世纪","长篇小说","小说","法语","mauriac","弗朗索瓦·莫里亚克","1927年（作者页B289口径：Thérèse Desqueyroux published 1927）",1927,
["Britannica（B289）：莫里亚克 major_works 载'苔蕾丝·德斯盖鲁'（B289 作者页定位，详见 aidewangmo 条核对）。","Britannica（B289）：'whose heroine is driven to attempt the murder of her husband to escape her suffocating life'（女主人公为逃离窒息生活而试图谋杀丈夫——B289）。","作者（B289）：1952诺奖。"],
["苔蕾丝毒害丈夫伯纳德未遂——家族的'庇护'与无罪释放（通说待核）。","结尾：'自由'的荒凉（通说待核）。"],
[{"name":"苔蕾丝","identity":"妻子","note":"投毒者（B289）"},{"name":"伯纳德","identity":"丈夫","note":"（通说待核）"}],
["窒息的婚姻与谋杀（B289）。","'自由'的荒凉（通说待核）。","天主教罪恶观（B289 作者级语境）。"],
[{"text":"Britannica：'whose heroine is driven to attempt the murder of her husband'（B289）。","source":"B289"},{"text":"Britannica：1952年诺奖（B289 作者级）。","source":"B289"}],
{"difficulties":["心理剧的封闭结构。","波尔多资产阶级语境。"],"editions":["《苔蕾丝·德斯盖鲁》（广西师范大学出版社，通说待核）。","法文原版（公有领域渐近）。"],"order":"先《爱的荒漠》后本作。"},
["1927年出版（Grasset说）核对。","苔蕾丝/伯纳德人名核对。","1950年电影改编待核。"],
["B289"],"B289","B289",["aidewangmo","lianqingdezhongjie","ouyeni"],
G("窒息结构图",[{"title":"投毒","text":"逃离的未遂","color":"antagonist"},{"title":"家族","text":"无罪的庇护","color":"family"},{"title":"苔蕾丝","text":"窒息的妻子","color":"main"},{"title":"自由","text":"荒凉的出路","color":"gold"}])))

# 9. 终结的感觉
W.append(mk("zhongjiedeganjue","终结的感觉","The Sense of an Ending","英国","现当代","21世纪","中篇小说","小说","英语","barnes","朱利安·巴恩斯","2011年（作者页B290口径：2011年布克奖——'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'）",2011,
["作者页（B290）：巴恩斯 major_works 载'终结的感觉'（B290 作者页定位，详见 fuloubaideyingwu 条核对）。","Britannica（B290）：2011年布克奖——'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'（以不可靠叙述者探察记忆与衰老——B290）。","作者（B290）：'inventive and intellectual novels about obsessed characters curious about the past'。"],
["退休律师托尼的回忆被一封遗嘱与一封信改写（通说待核）。","'不可靠的记忆'：自我辩护的崩塌（通说待核）。"],
[{"name":"托尼","identity":"退休律师","note":"不可靠叙述者（B290）"},{"name":"维罗妮卡","identity":"前女友","note":"（通说待核）"}],
["记忆的不可靠（B290）。","衰老与清算（B290：memory and aging）。","'终结的感觉'：历史的追索（书名通说待核）。"],
[{"text":"Britannica：2011年布克奖——不可靠叙述者探察记忆与衰老（B290）。","source":"B290"},{"text":"Britannica：2017年电影改编（B290 语境）。","source":"B290"}],
{"difficulties":["上下两部（第一/第二部分）结构。","不可靠叙述的细节。"],"editions":["《终结的感觉》（译林出版社，通说待核）。","英文原版。"],"order":"先《福楼拜的鹦鹉》后本作。"},
["2011年出版（Jonathan Cape说）核对。","托尼/维罗妮卡人名核对。","2017年电影（Ritesh Batra说）待核。"],
["B290"],"B290","B290",["fuloubaideyingwu","banshengyuan","changri"],
G("记忆结构图",[{"title":"遗嘱","text":"改写的开始","color":"antagonist"},{"title":"记忆","text":"不可靠的自辩（B290）","color":"main"},{"title":"维罗妮卡","text":"真相的持有者","color":"gold"},{"title":"衰老","text":"清算的晚年","color":"family"}])))

# 10. 慧血
W.append(mk("huixue","慧血","Wise Blood","美国","现当代","20世纪","长篇小说","小说","英语","oconnor","弗兰纳里·奥康纳","1952年（作者页B291口径：Wise Blood (1952)）",1952,
["作者页（B291）：奥康纳 major_works 载'Wise Blood (1952)'（B291 作者页定位，详见 haorennanxun 条核对）。","题材（通说待核）：退伍兵黑兹尔·莫茨的'无教会'布道——拒绝基督却离不开基督。"],
["黑兹尔创立'无教会之教'——荒诞布道与最后的自毁（通说待核）。"],
[{"name":"黑兹尔·莫茨","identity":"退伍兵","note":"（通说待核）"},{"name":"伊诺克","identity":"青年","note":"（通说待核）"}],
["'无教会'的悖论：拒绝即证明（通说待核）。","南方哥特（B291：master of the Southern gothic——作者级）。","瞎眼与忏悔（通说待核）。"],
[{"text":"作者页：奥康纳首部长篇（B291 作者页口径）。","source":"B291"},{"text":"作者页：南方哥特大师（B291 作者级定位）。","source":"B291"}],
{"difficulties":["'无教会'的宗教戏仿。","哥特细节。"],"editions":["《慧血》（新星出版社《慧血：奥康纳作品集》，通说待核）。","英文原版。"],"order":"先《好人难寻》后本作。"},
["1952年出版（Harcourt, Brace说）核对。","黑兹尔·莫茨人名核对。","1969年电影改编待核。"],
["B291"],"B291","B291",["haorennanxun","juwairen","bianxingji"],
G("悖论结构图",[{"title":"无教会","text":"拒绝的布道","color":"main"},{"title":"黑兹尔","text":"瞎眼的忏悔（通说）","color":"antagonist"},{"title":"慧血","text":"书名的反讽","color":"gold"},{"title":"南方","text":"哥特的荒原","color":"family"}])))

# 11. 螺丝在拧紧
W.append(mk("luosizainingjin","螺丝在拧紧","The Turn of the Screw","英国","现当代","19世纪末","中篇小说","小说","英语","henryjames","亨利·詹姆斯","1898年（作者页B297口径：The Turn of the Screw (1898)——'best remembered'）",1898,
["Britannica（B297）：'Today he is best remembered as the author of the novel The Portrait of a Lady (1881) and the novella The Turn of the Screw (1898).'（B297）。","作者（B297）：'a key transitional figure between literary realism and Modernism'。","题材（通说待核）：家庭女教师与两个孩子的幽灵故事——'被污染的'哥特叙事。"],
["女教师的幽灵见闻：'看不见的'恐惧（通说待核）。"],
[{"name":"女教师","identity":"家庭教师","note":"（通说待核）"},{"name":"迈尔斯与弗洛拉","identity":"孩子","note":"（通说待核）"}],
["'幽灵'与'心理'的双重解读（通说待核）。",
"不可靠叙述（通说待核）。",
"哥特与心理的融合（通说）。"],
[{"text":"Britannica：'best remembered as the author of……The Turn of the Screw (1898)'（B297）。","source":"B297"},{"text":"作者页：'key transitional figure between literary realism and Modernism'（B297 作者级）。","source":"B297"}],
{"difficulties":["'幽灵'还是'幻觉'的解读。","叙事框套。"],"editions":["《螺丝在拧紧》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],"order":"亨利·詹姆斯哥特之作。"},
["1898年出版（Macmillan说）核对。","女教师/迈尔斯/弗洛拉人名核对。","'幽灵还是幻觉'的学术争论待核。"],
["B297"],"B297","B297",["jianWenzhaji","weite","嘉莉妹妹"],
G("哥特结构图",[{"title":"女教师","text":"幽灵的目击者（通说）","color":"main"},{"title":"孩子","text":"迈尔斯与弗洛拉","color":"gold"},{"title":"幽灵","text":"看不见的威胁","color":"antagonist"},{"title":"解读","text":"幽灵还是幻觉","color":"family"}])))

# 写入
for w in W:
    p = pathlib.Path(f"data/works/{w['id']}.json")
    p.write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", w['id'])
print(len(W), "works created")
