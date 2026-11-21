# -*- coding: utf-8 -*-
"""批40：零成本 12 部（谢利/维莱特/姆采里/假面舞会/贵族之家/前夜/萨哈林岛/白卫军/特洛伊罗斯/海的女儿/丑小鸭/名女传）"""
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

S_CB, S_LM, S_TU, S_CH, S_BG, S_CU, S_AN, S_BO = (src_of(x) for x in ['charlotte-bronte','lermontov','turgenev','chekhov','bulgakov','chaucer','andersen','boccaccio'])
print('srcs:', S_CB, S_LM, S_TU, S_CH, S_BG, S_CU, S_AN, S_BO)

works = [
{"id":"sheli","title":"谢利","original_title":"Shirley","region":"英国","era":"近代","era_detail":"19世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"charlotte-bronte","author_name":"夏洛蒂·勃朗特",
"year_display":"1849年（作者页注记：Britannica 列举——谢利 (1849)）","year_sort":1849,
"background":["作者页注记：谢利 (1849)、维莱特 (1853)——'后续长篇（Britannica）'。","Britannica：夏洛蒂·勃朗特——《简·爱》作者（作者页语境）。","题材（通说待核）：约克郡毛纺业萧条期——两个女子的友谊与工厂骚乱。"],
"outline":["（通说待核）卡罗琳与谢利：性情相反的友谊。","（通说待核）1811-12年卢德骚乱背景。"],
"characters":[{"name":"谢利·基尔达","identity":"女地主","note":"（通说待核）"},{"name":"卡罗琳·赫尔斯通","identity":"牧师侄女","note":"（通说待核）"}],
"themes":["工业化的社会图景（通说待核）。",
 "女性友谊（通说待核）。",
 "'社会小说'的勃朗特变体（通说待核）。"],
"influence":[{"text":"Britannica：'后续长篇'（作者页注记）。","source":S_CB},{"text":"Britannica：《简·爱》为代表作（作者页交叉）。","source":S_CB}],
"reading":{"difficulties":["卢德运动史。","与《简·爱》的文体差异。"],
 "editions":["《谢利》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"勃朗特第二作；与《简·爱》对读。"},
"pending":["谢利/卡罗琳人名核对（通说）。","1849年出版细节待核。","卢德运动细节待核。"],
"sources":[S_CB],"year_source":S_CB,"author_source":S_CB,"related_works":["jianai","weilaite","leiyu"],
"svg":G("《谢利》友谊结构图",[{"title":"谢利","text":"明亮的业主（通说）","color":"main"},{"title":"卡罗琳","text":"温顺的旁观者（通说）","color":"family"},{"title":"毛纺厂","text":"骚乱的时代（通说）","color":"antagonist"},{"title":"友谊","text":"性情的互补（通说）","color":"gold"}])},
{"id":"weilaite","title":"维莱特","original_title":"Villette","region":"英国","era":"近代","era_detail":"19世纪50年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"charlotte-bronte","author_name":"夏洛蒂·勃朗特",
"year_display":"1853年（作者页注记：Britannica 列举——维莱特 (1853)）","year_sort":1853,
"background":["作者页注记：维莱特 (1853)——'后续长篇（Britannica）'。","Britannica：夏洛蒂·勃朗特——布鲁塞尔经历（作者页语境——待核）。","题材（通说待核）：露西·斯诺在异国'维莱特'的教书生涯与孤寂。"],
"outline":["（通说待核）露西在女子学校的克制与观察。","（通说待核）保罗·埃马纽埃尔教师的别扭情感。"],
"characters":[{"name":"露西·斯诺","identity":"叙述者","note":"（通说待核）"},{"name":"保罗教师","identity":"怪脾气教师","note":"（通说待核）"}],
"themes":["异乡的孤寂与克制（通说待核）。",
 "第一人称的不可靠（通说待核）。",
 "天主教与新教的目光（背景通说待核）。"],
"influence":[{"text":"Britannica：'后续长篇'（作者页注记）。","source":S_CB},{"text":"Britannica：作者布鲁塞尔经历的自传性（作者页语境——待核）。","source":S_CB}],
"reading":{"difficulties":["'维莱特'（布鲁塞尔的化名——通说待核）。","克制的叙述风格。"],
 "editions":["《维莱特》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"勃朗特第三作；最成熟的心理书写。"},
"pending":["露西·斯诺人名核对（通说）。","1853年出版细节待核。","布鲁塞尔自传对应待核。"],
"sources":[S_CB],"year_source":S_CB,"author_source":S_CB,"related_works":["jianai","sheli","mengya"],
"svg":G("《维莱特》孤寂结构图",[{"title":"露西","text":"克制的观察者（通说）","color":"main"},{"title":"女子学校","text":"异乡的围城（通说）","color":"family"},{"title":"保罗教师","text":"别扭的爱（通说）","color":"gold"},{"title":"孤寂","text":"心理的暗流（通说）","color":"antagonist"}])},
{"id":"mucaili","title":"姆采里","original_title":"Мцыри（Mtsyri）","region":"俄国","era":"近代","era_detail":"19世纪30年代末",
"genre":"长诗","genre_group":"诗歌","language":"俄语","author_id":"lermontov","author_name":"米哈伊尔·莱蒙托夫",
"year_display":"作者页注记：Britannica 列举 Mtsyri（成稿/发表年份通说待核）","year_sort":1839,
"background":["作者页注记：恶魔、假面舞会、姆采里——'诗与剧（Britannica 列举）'。","Britannica：莱蒙托夫——普希金之后俄国诗歌代表（作者页语境）。","题材（通说待核）：修道院长大的高加索少年——三天逃亡与自由的死亡。"],
"outline":["（通说待核）'姆采里'（异乡人）的自述：三天的自由。","（通说待核）与山豹的搏斗及格鲁吉亚少女的幻影。"],
"characters":[{"name":"姆采里","identity":"逃亡少年","note":"（B 书名人物）"}],
"themes":["自由与囚禁（通说待核）。",
 "高加索的自然礼赞（通说待核）。",
 "浪漫主义英雄的少年版（通说待核）。"],
"influence":[{"text":"Britannica：Mtsyri 列举（作者页注记）。","source":S_LM},{"text":"Britannica：莱蒙托夫诗歌地位（作者页语境）。","source":S_LM}],
"reading":{"difficulties":["长诗独白体。","修道院与高加索的对立（通说待核）。"],
 "editions":["《姆采里》中译名（《童僧》两说——通说待核）。","俄文原版（公有领域）。"],
 "order":"莱蒙托夫诗歌之二；与《恶魔》并读。"},
"pending":["发表年份（1839/1840说）待核。","'姆采里'格鲁吉亚语含义待核。","山豹搏斗细节待核。"],
"sources":[S_LM],"year_source":S_LM,"author_source":S_LM,"related_works":["emo","dangdaiyingxiong","xuboliweng"],
"svg":G("《姆采里》三天自由图",[{"title":"修道院","text":"囚禁的童年（通说）","color":"antagonist"},{"title":"三天","text":"自由的长度（通说）","color":"main"},{"title":"山豹","text":"野性的相遇（通说）","color":"gold"},{"title":"死亡","text":"自由人的安息（通说）","color":"family"}])},
{"id":"jiamianwuhui","title":"假面舞会","original_title":"Маскарад（Masquerade）","region":"俄国","era":"近代","era_detail":"19世纪30年代",
"genre":"戏剧","genre_group":"戏剧","language":"俄语","author_id":"lermontov","author_name":"米哈伊尔·莱蒙托夫",
"year_display":"作者页注记：Britannica 列举 Masquerade（首演/发表年份通说待核）","year_sort":1835,
"background":["作者页注记：假面舞会——'Britannica 列举'。","Britannica：莱蒙托夫——《当代英雄》作者（作者页语境）。","题材（通说待核）：阿尔贝宁因失落的bracelet而杀妻——嫉妒的悲剧。"],
"outline":["（通说待核）假面舞会的误会与手镯。","（通说待核）被社会操纵的嫉妒。"],
"characters":[{"name":"阿尔贝宁","identity":"军官","note":"（通说待核）"},{"name":"尼娜","identity":"妻子","note":"（通说待核）"}],
"themes":["嫉妒与猜疑的悲剧（通说待核）。",
 "彼得堡上流社会的假面（书名语境——通说待核）。",
 "命运的偶然（通说待核）。"],
"influence":[{"text":"Britannica：Masquerade 列举（作者页注记）。","source":S_LM},{"text":"Britannica：莱蒙托夫戏剧序列（作者页语境）。","source":S_LM}],
"reading":{"difficulties":["19世纪30年代彼得堡沙龙。","'误会剧'的结构。"],
 "editions":["《假面舞会》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"莱蒙托夫戏剧首选。"},
"pending":["阿尔贝宁/尼娜人名核对（通说）。","1835年写成、禁演史待核。","手镯细节待核。"],
"sources":[S_LM],"year_source":S_LM,"author_source":S_LM,"related_works":["emo","mucaili","leiyu"],
"svg":G("《假面舞会》误会结构图",[{"title":"假面","text":"社会的伪装（通说）","color":"gold"},{"title":"手镯","text":"误会的信物（通说）","color":"antagonist"},{"title":"嫉妒","text":"悲剧的引擎（通说）","color":"main"},{"title":"尼娜","text":"无辜的牺牲（通说）","color":"family"}])},
{"id":"guizhuzhijia","title":"贵族之家","original_title":"Дворянское гнездо","region":"俄国","era":"近代","era_detail":"19世纪50年代末",
"genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"turgenev","author_name":"伊万·屠格涅夫",
"year_display":"1859年（Britannica（B141）：1859《贵族之家》）","year_sort":1859,
"background":["B141：'1856《罗亭》1859《贵族之家》1860《前夜》1862《父与子》'。","Britannica（B141）：屠格涅夫——斯帕斯科耶庄园（作者页语境）。","题材（通说待核）：拉夫列茨基的归乡与莉莎的宗教决意。"],
"outline":["（通说待核）'死而复生'的妻子归来与旧梦破碎。","（通说待核）莉莎入修道院与'贵族之巢'的凋零。"],
"characters":[{"name":"拉夫列茨基","identity":"归乡贵族","note":"（通说待核）"},{"name":"莉莎","identity":"少女","note":"（通说待核）"}],
"themes":["贵族庄园的黄昏（书名语境——通说待核）。",
 "爱情与义务（通说待核）。",
 "1850年代改革前夜（通说待核）。"],
"influence":[{"text":"Britannica：1859《贵族之家》（B141）。","source":S_TU},{"text":"Britannica：屠格涅夫庄园书写（B141 语境）。","source":S_TU}],
"reading":{"difficulties":["改革前夜的社会史。","抒情与挽歌的语调。"],
 "editions":["《贵族之家》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"屠格涅夫抒情巅峰；与《罗亭》《前夜》对读。"},
"pending":["拉夫列茨基/莉莎人名核对（通说）。","1859年发表（《现代人》说）待核。","瓦尔瓦拉·帕夫洛夫娜细节待核。"],
"sources":[S_TU],"year_source":S_TU,"author_source":S_TU,"related_works":["luoting","qianye","lierenbiji"],
"svg":G("《贵族之家》黄昏结构图",[{"title":"庄园","text":"'贵族之巢'的凋零（书名）","color":"family"},{"title":"归乡","text":"旧梦的破碎（通说）","color":"main"},{"title":"莉莎","text":"信仰的抉择（通说）","color":"gold"},{"title":"妻子","text":"复活的障碍（通说）","color":"antagonist"}])},
{"id":"qianye","title":"前夜","original_title":"Накануне","region":"俄国","era":"近代","era_detail":"19世纪50年代末",
"genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"turgenev","author_name":"伊万·屠格涅夫",
"year_display":"1860年（Britannica（B141）：1860《前夜》）","year_sort":1860,
"background":["B141：'1860《前夜》1862《父与子》（虚无主义者巴扎罗夫——激进与保守两头挨骂促其自我流放西欧）'。","Britannica（B141）：屠格涅夫——终生恋波琳娜·维亚尔多（作者页语境）。","题材（通说待核）：叶莲娜与保加利亚革命者英沙罗夫——解放前夜的爱情与牺牲。"],
"outline":["（通说待核）叶莲娜的选择：追随革命者的私奔。","（通说待核）英沙罗夫之死与'前夜'的落空。"],
"characters":[{"name":"叶莲娜","identity":"贵族少女","note":"（通说待核）"},{"name":"英沙罗夫","identity":"保加利亚革命者","note":"（通说待核）"}],
"themes":["解放前夜的社会期待（书名语境——通说待核）。",
 "'新人'的登场（通说待核—— precedes 巴扎罗夫）。",
 "跨国革命的牺牲（通说待核）。"],
"influence":[{"text":"Britannica：1860《前夜》（B141）。","source":S_TU},{"text":"Britannica：《父与子》巴扎罗夫的'新人'先声（B141 交叉）。","source":S_TU}],
"reading":{"difficulties":["1860年俄国社会语境。","保加利亚民族解放史（通说待核）。"],
 "editions":["《前夜》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"屠格涅夫'新人'序曲；后接《父与子》。"},
"pending":["叶莲娜/英沙罗夫人名核对（通说）。","1860年发表细节待核。","杜勃罗留波夫《真正的白天何时到来》评论文待核。"],
"sources":[S_TU],"year_source":S_TU,"author_source":S_TU,"related_works":["fuyuzi","guizhuzhijia","luoting"],
"svg":G("《前夜》新人结构图",[{"title":"前夜","text":"解放的黎明前（书名）","color":"gold"},{"title":"英沙罗夫","text":"革命者之爱（通说）","color":"main"},{"title":"叶莲娜","text":"出走的新女性（通说）","color":"family"},{"title":"死亡","text":"落空的黎明（通说）","color":"antagonist"}])},
{"id":"sahalindao","title":"萨哈林岛","original_title":"Остров Сахалин","region":"俄国","era":"近代","era_detail":"19世纪90年代",
"genre":"调查报告","genre_group":"散文","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
"year_display":"1893-94年（作者页注记：Britannica——萨哈林岛 (1893—94)——苦役地调查报告）","year_sort":1893,
"background":["作者页注记：萨哈林岛 (1893-94)——'苦役地调查报告（Britannica）'。","Britannica（B270）：契诃夫——医生作家（作者页语境）。","题材（通说待核）：1890年横跨西伯利亚的苦役岛调查——人口普查式的记录。"],
"outline":["（通说待核）苦役犯、流放者与移民的清单式记录。","（通说待核）'我为文明欠债'的动机。"],
"characters":[{"name":"契诃夫（调查者）","identity":"医生/作家","note":"（B270 语境）"}],
"themes":["苦役制度的档案（通说待核）。",
 "医生的道德行动（B270 语境）。",
 "帝国边地的报告文学（通说待核）。"],
"influence":[{"text":"Britannica：萨哈林岛 (1893-94)（作者页注记）。","source":S_CH},{"text":"Britannica：契诃夫'医生与作家'的双重身份（B270 交叉——待核）。","source":"B270"}],
"reading":{"difficulties":["流放制度史。","报告文学与文学的边界。"],
 "editions":["《萨哈林岛》中译名（《萨哈林旅行记》两说——通说待核）。","俄文原版（公有领域）。"],
 "order":"契诃夫散文側面；与《萨哈林旅行记》译本对照。"},
"pending":["1890年之旅与1893-94成书年份核对（B注记）。","人口普查细节待核。","'债'的说法出处待核。"],
"sources":[S_CH],"year_source":S_CH,"author_source":S_CH,"related_works":["haiou","sanzimei","nongmin"],
"svg":G("《萨哈林岛》调查结构图",[{"title":"苦役地","text":"帝国的边地（通说）","color":"antagonist"},{"title":"调查","text":"档案的清单（B注记）","color":"main"},{"title":"医生","text":"道德的行动（B270语境）","color":"gold"},{"title":"流放者","text":"被记录的人（通说）","color":"family"}])},
{"id":"baiweijun","title":"白卫军","original_title":"Белая гвардия","region":"苏联","era":"近代","era_detail":"20世纪20年代",
"genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"bulgakov","author_name":"米哈伊尔·布尔加科夫",
"year_display":"作者页注记：Britannica——白卫军（年份通说待核——1925-27连载说）","year_sort":1925,
"background":["作者页注记：白卫军、图尔宾一家的日子——'（Britannica）'。","Britannica：布尔加科夫——《大师与玛格丽特》作者、多部被禁（作者页语境）。","题材（通说待核）：1918年基辅——图尔宾一家在内战中的覆灭。"],
"outline":["（通说待核）图尔宾兄妹与'白卫军'的崩溃。","（通说待核）冬夜壁炉与家宅的象征。"],
"characters":[{"name":"阿列克谢·图尔宾","identity":"军医","note":"（通说待核）"},{"name":"叶莲娜","identity":"妹妹","note":"（通说待核）"}],
"themes":["内战中'白'的挽歌（通说待核）。",
 "家宅的守护（通说待核）。",
 "历史的暴力与日常（作者页语境）。"],
"influence":[{"text":"Britannica：白卫军（作者页注记）。","source":S_BG},{"text":"Britannica：改编《图尔宾一家的日子》被禁史（作者页注记——待核）。","source":S_BG}],
"reading":{"difficulties":["乌克兰内战的多方势力。","'白军'视角的历史叙事。"],
 "editions":["《白卫军》中译本（人民文学等——通说待核）。","俄文原版。"],
 "order":"布尔加科夫早期首选；后接《大师与玛格丽特》。"},
"pending":["图尔宾人名核对（通说）。","1925-27年连载（《俄罗斯》杂志说）待核。","《图尔宾一家的日子》1926首演细节待核。"],
"sources":[S_BG],"year_source":S_BG,"author_source":S_BG,"related_works":["dashiyumagelit","gouxin","yigerendeyu"],
"svg":G("《白卫军》覆灭结构图",[{"title":"基辅","text":"1918年的冬天（通说）","color":"antagonist"},{"title":"图尔宾家","text":"壁炉旁的家宅（通说）","color":"main"},{"title":"白卫军","text":"崩溃的旗帜（B注记）","color":"gold"},{"title":"日常","text":"历史的暴力（通说）","color":"family"}])},
{"id":"teluoyiluosi","title":"特洛伊罗斯与克丽西达","original_title":"Troilus and Criseyde","region":"英国","era":"古代","era_detail":"14世纪80年代",
"genre":"长诗","genre_group":"诗歌","language":"英语（中古英语）","author_id":"chaucer","author_name":"杰弗里·乔叟",
"year_display":"作者页注记：Britannica——取材薄伽丘《菲洛斯特拉托》（成诗年份通说待核——约1385）","year_sort":1385,
"background":["作者页注记：特洛伊罗斯与克丽西达——'取材薄伽丘《菲洛斯特拉托》（Britannica：Chaucer drew on Il filostrato）'。","Britannica：乔叟——'英国诗歌之父'（作者页语境——待核）。","题材（通说待核）：特洛伊战争中特洛伊罗斯与克丽西达的爱情与背叛。"],
"outline":["（通说待核）爱情五卷结构：相遇—盟誓—交换—背叛—哀悼。","（通说待核）彭斯瑞俄斯与命运女神的议论。"],
"characters":[{"name":"特洛伊罗斯","identity":"特洛伊王子","note":"（通说待核）"},{"name":"克丽西达","identity":"寡妇之女","note":"（通说待核）"}],
"themes":["爱情的可变与忠诚（通说待核）。",
 "'命运'的哲理框架（通说待核）。",
 "意大利文学的英语转化（B注记：drew on Il filostrato）。"],
"influence":[{"text":"Britannica：'Chaucer drew on Il filostrato'（作者页注记）。","source":S_CU},{"text":"Britannica：乔叟《坎特伯雷故事》作者（作者页交叉）。","source":S_CU}],
"reading":{"difficulties":["中古英语。","薄伽丘底本的改写比较。"],
 "editions":["《特洛伊罗斯与克丽西达》中译本（人民文学等——通说待核）。","中古英语原版（公有领域）。"],
 "order":"乔叟长诗首选；与《坎特伯雷故事》对读。"},
"pending":["成诗年份（约1385说）待核。","五卷结构核对（通说）。","莎士比亚同名戏剧的关系待核。"],
"sources":[S_CU],"year_source":S_CU,"author_source":S_CU,"related_works":["kanteboleigushi","xunjiexiaoshuo","luoting"],
"svg":G("《特洛伊罗斯与克丽西达》背叛结构图",[{"title":"特洛伊","text":"战争中的爱情（通说）","color":"family"},{"title":"克丽西达","text":"交换与背叛（通说）","color":"antagonist"},{"title":"命运","text":"哲理的框架（通说）","color":"gold"},{"title":"薄伽丘","text":"意大利底本（B注记）","color":"main"}])},
{"id":"haidenvren","title":"海的女儿","original_title":"Den lille Havfrue（The Little Mermaid）","region":"丹麦","era":"近代","era_detail":"19世纪30年代",
"genre":"童话","genre_group":"故事集","language":"丹麦语","author_id":"andersen","author_name":"安徒生",
"year_display":"1837年（作者页注记：Britannica 语境——发表年份通说待核）","year_sort":1837,
"background":["作者页注记：海的女儿、丑小鸭、白雪皇后——'（Britannica 语境）'。","Britannica：安徒生——童话作家（作者页语境）。","题材（通说待核）：小人鱼以声音换双腿——爱而不得化为泡沫。"],
"outline":["（通说待核）海底宫殿的少女与海上王子。","（通说待核）'泡沫'的结尾与灵魂的可能。"],
"characters":[{"name":"小人鱼","identity":"海王之女","note":"（通说待核）"},{"name":"王子","identity":"岸上的人","note":"（通说待核）"}],
"themes":["牺牲与'不灭的灵魂'（通说待核）。",
 "身体的代价：声音（通说待核）。",
 "童话的悲剧性（通说待核）。"],
"influence":[{"text":"Britannica：安徒生童话序列（作者页注记）。","source":S_AN},{"text":"Britannica：安徒生为童话大师（作者页语境）。","source":S_AN}],
"reading":{"difficulties":["童话与民间故事的区别。","'灵魂'的神学设定。"],
 "editions":["《海的女儿》（人民文学出版社《安徒生童话全集》等——通说待核）。","丹麦文原版（公有领域）。"],
 "order":"安徒生代表作；与《丑小鸭》对读。"},
"pending":["1837年发表（《童话集》第三分册说）待核。","'泡沫'结尾细节待核。","小人鱼人名核对（无名的'小女儿'说）。"],
"sources":[S_AN],"year_source":S_AN,"author_source":S_AN,"related_works":["chouxiaoya","baixuehuanghou","xuboliweng"],
"svg":G("《海的女儿》牺牲结构图",[{"title":"小人鱼","text":"声音的交换（通说）","color":"main"},{"title":"王子","text":"不可得的爱（通说）","color":"antagonist"},{"title":"泡沫","text":"结局的升华（通说）","color":"gold"},{"title":"灵魂","text":"童话的神学（通说）","color":"family"}])},
{"id":"chouxiaoya","title":"丑小鸭","original_title":"Den grimme ælling（The Ugly Duckling）","region":"丹麦","era":"近代","era_detail":"19世纪40年代",
"genre":"童话","genre_group":"故事集","language":"丹麦语","author_id":"andersen","author_name":"安徒生",
"year_display":"作者页注记：Britannica 语境——发表年份通说待核（1843说）","year_sort":1843,
"background":["作者页注记：丑小鸭——'（Britannica 语境）'。","Britannica：安徒生——出身贫寒的童话作家（作者页语境——待核）。","题材（通说待核）：被嘲笑的'鸭子'终成天鹅——自传性寓言。"],
"outline":["（通说待核）农场的排斥与冬天的漂泊。","（通说待核）天鹅群的接纳与'我是'的确认。"],
"characters":[{"name":"丑小鸭","identity":"天鹅幼鸟","note":"（通说待核）"}],
"themes":["身份的自我发现（通说待核）。",
 "排斥与接纳（通说待核）。",
 "'受苦的孩子'的寓言（作者页语境——通说待核）。"],
"influence":[{"text":"Britannica：安徒生童话序列（作者页注记）。","source":S_AN},{"text":"Britannica：安徒生生平的寓言对应（作者页语境——待核）。","source":S_AN}],
"reading":{"difficulties":["寓言与童话的边界。","'成长'叙事的原型。"],
 "editions":["《丑小鸭》（人民文学出版社《安徒生童话全集》等——通说待核）。","丹麦文原版（公有领域）。"],
 "order":"安徒生代表作；与《海的女儿》对读。"},
"pending":["1843年发表（《新童话》第一集说）待核。","自传性对应细节待核。","'天鹅'意象来源待核。"],
"sources":[S_AN],"year_source":S_AN,"author_source":S_AN,"related_works":["haidenvren","baixuehuanghou","xinnuofusuobaken"],
"svg":G("《丑小鸭》成长结构图",[{"title":"排斥","text":"农场的嘲笑（通说）","color":"antagonist"},{"title":"漂泊","text":"寒冬的旅途（通说）","color":"main"},{"title":"天鹅","text":"身份的确认（通说）","color":"gold"},{"title":"接纳","text":"群体的和解（通说）","color":"family"}])},
{"id":"mingnuzhuan","title":"名女传","original_title":"De mulieribus claris","region":"意大利","era":"近代","era_detail":"14世纪60年代",
"genre":"传记集","genre_group":"散文","language":"拉丁语","author_id":"boccaccio","author_name":"乔万尼·薄伽丘",
"year_display":"作者页注记：Britannica——名女传（拉丁人文主义著作——年份通说待核）","year_sort":1362,
"background":["作者页注记：异教诸神谱系、名女传——'拉丁人文主义著作（Britannica）'。","Britannica：薄伽丘——《十日谈》作者（作者页语境）。","题材（通说待核）：106（或104）位著名女性的传记——从夏娃到当代。"],
"outline":["（通说待核）女性的传记序列：美德与恶行的榜样。","（通说待核）人文主义的女性观及其矛盾。"],
"characters":[{"name":"众名女","identity":"——","note":"（通说待核）"}],
"themes":["女性传记的开创（通说待核）。",
 "人文主义的拉丁写作（B注记）。",
 "美德与恶行的道德谱系（通说待核）。"],
"influence":[{"text":"Britannica：'拉丁人文主义著作'（作者页注记）。","source":S_BO},{"text":"Britannica：薄伽丘《十日谈》为代表作（作者页交叉）。","source":S_BO}],
"reading":{"difficulties":["拉丁语。","古典与中世纪的传记传统。"],
 "editions":["《名女传》中译本（人民文学等——通说待核）。","拉丁文原版（公有领域）。"],
 "order":"《十日谈》后的学术侧面。"},
"pending":["篇数（106/104说）核对（通说）。","1361-62年写作年份待核。","首个专写女性的传记集说法待核。"],
"sources":[S_BO],"year_source":S_BO,"author_source":S_BO,"related_works":["shiritan","teluoyiluosi","xunjiexiaoshuo"],
"svg":G("《名女传》传记结构图",[{"title":"名女","text":"百位女性的谱系（通说）","color":"main"},{"title":"拉丁","text":"人文主义的写作（B注记）","color":"gold"},{"title":"美德","text":"道德的榜样（通说）","color":"family"},{"title":"开创","text":"女性传记的先河（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批40）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('sheli','charlotte-bronte','谢利'),('weilaite','charlotte-bronte','维莱特'),('mucaili','lermontov','姆采里'),('jiamianwuhui','lermontov','假面舞会'),('guizhuzhijia','turgenev','贵族之家'),('qianye','turgenev','前夜'),('sahalindao','chekhov','萨哈林岛'),('baiweijun','bulgakov','白卫军'),('teluoyiluosi','chaucer','特洛伊罗斯'),('haidenvren','andersen','海的女儿'),('chouxiaoya','andersen','丑小鸭'),('mingnuzhuan','boccaccio','名女传')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH40 DONE')
