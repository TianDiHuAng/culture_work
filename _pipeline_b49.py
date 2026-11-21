# -*- coding: utf-8 -*-
"""批49：零成本 14 部（婚礼的成员/伤心咖啡馆之歌/人性的枷锁/阿姆斯特丹/我们街区的孩子们/小偷与狗/论出版自由/罗曼采罗/神圣的树林/山里的平凡故事/过界的仪式/会唱歌的鱼/设立守望者/明娜·冯·巴尔赫姆）+ 过期条目清理"""
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

S_MC, S_MG, S_MF, S_MI, S_HE, S_EL, S_KI, S_GO, S_LA, S_LE = (src_of(x) for x in ['mccalles','maugham','mahfouz','milton','heine','eliot','kipling','golding','laxness','lessing'])
print('srcs:', S_MC, S_MG, S_MF, S_MI, S_HE, S_EL, S_KI, S_GO, S_LA, S_LE)

works = [
# 1. 麦卡勒斯《婚礼的成员》
{"id":"hunlidechengyuan","title":"婚礼的成员","original_title":"The Member of the Wedding","region":"美国","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mccalles","author_name":"卡森·麦卡勒斯",
"year_display":"1946年（Britannica B331：The Member of the Wedding (1946)）","year_sort":1946,
"background":["Britannica（B331）：The Member of the Wedding (1946)——'novel; Broadway play ran over a year'（百老汇演出逾一年）。","Britannica（B331）：田纳西·威廉斯鼓励其改编为舞台剧。","Britannica（B331）：麦卡勒斯——'depict the inner lives of lonely people'。","题材（通说待核）：12岁的弗兰淇·亚当斯——夏日婚礼的'成员'渴望。"],
"outline":["（通说待核）弗兰淇被哥哥的婚礼排除——与伯妮丝和约翰·亨利度夏。","（通说待核）'我们'的归属渴望（we of them说——通说待核）。"],
"characters":[{"name":"弗兰淇","identity":"12岁少女","note":"（通说待核，B331未载）"},{"name":"伯妮丝","identity":"黑人厨娘","note":"（通说待核）"}],
"themes":["归属与'婚礼成员'的想象（书名语境——通说待核）。",
 "'孤独人的内心'（B331：lonely people）。",
 "南方小镇的夏末（B331 语境）。"],
"influence":[{"text":"Britannica：百老汇演出逾一年（B331）。","source":"B331"},{"text":"Britannica：威廉斯鼓励改编（B331）。","source":"B331"}],
"reading":{"difficulties":["'归属'的口语哲学。","南方种族语境。"],
 "editions":["《婚礼的成员》中译本（人民文学/上海译文等——通说待核）。","英文原版。"],
 "order":"麦卡勒斯第二作；与《心是孤独的猎手》对读。"},
"pending":["弗兰淇/伯妮丝人名核对（B331未载）。","1946年出版细节待核。","1952年电影/1950百老汇说待核。"],
"sources":["B331"],"year_source":"B331","author_source":"B331","related_works":["xinshigudeLieshou","bolidongwuyuan","zise"],
"svg":G("《婚礼的成员》归属结构图",[{"title":"弗兰淇","text":"婚礼的局外人（通说）","color":"main"},{"title":"婚礼","text":"归属的想象（书名）","color":"gold"},{"title":"伯妮丝","text":"夏日的智慧（通说）","color":"family"},{"title":"南方","text":"小镇的黄昏（通说）","color":"antagonist"}])},
# 2. 麦卡勒斯《伤心咖啡馆之歌》
{"id":"shangxinkafeizhige","title":"伤心咖啡馆之歌","original_title":"The Ballad of the Sad Café","region":"美国","era":"近代","era_detail":"20世纪50年代初",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"mccalles","author_name":"卡森·麦卡勒斯",
"year_display":"1951年（Britannica B331：The Ballad of the Sad Café——1951）","year_sort":1951,
"background":["Britannica（B331）：The Ballad of the Sad Café——1951。","Britannica（B331）：麦卡勒斯——'the incompatibility of lover and beloved'（爱者与被爱者的不相容）。","题材（通说待核）：爱密利亚小姐的咖啡馆与驼背李蒙——被爱者的暴政。"],
"outline":["（通说待核）爱密利亚的咖啡馆：小镇的公共空间。","（通说待核）驼背李蒙的'暴政'与马文·梅西的归来。"],
"characters":[{"name":"爱密利亚小姐","identity":"咖啡馆主人","note":"（通说待核，B331未载）"},{"name":"李蒙","identity":"驼背表亲","note":"（通说待核）"}],
"themes":["'爱者与被爱者的不相容'（B331）。",
 "咖啡馆作为社区仪式（通说待核）。",
 "'歌谣'的叙事调子（书名语境）。"],
"influence":[{"text":"Britannica：'the incompatibility of lover and beloved'（B331）。","source":"B331"},{"text":"Britannica：南方哥特语境（作者页交叉）。","source":"B331"}],
"reading":{"difficulties":["'歌谣'的叙事腔。","南方小镇的性别语境。"],
 "editions":["《伤心咖啡馆之歌》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"麦卡勒斯中篇首选。"},
"pending":["爱密利亚/李蒙人名核对（B331未载）。","1951年出版细节待核。","1991年电影改编说待核。"],
"sources":["B331"],"year_source":"B331","author_source":"B331","related_works":["xinshigudeLieshou","hunlidechengyuan","yuwanghaojieche"],
"svg":G("《伤心咖啡馆之歌》爱者结构图",[{"title":"爱密利亚","text":"咖啡馆的孤独（通说）","color":"main"},{"title":"李蒙","text":"被爱者的暴政（通说）","color":"antagonist"},{"title":"咖啡馆","text":"社区的仪式（通说）","color":"gold"},{"title":"歌谣","text":"讲述的调子（书名）","color":"family"}])},
# 3. 毛姆《人性的枷锁》
{"id":"renxingdejiasuo","title":"人性的枷锁","original_title":"Of Human Bondage","region":"英国","era":"近代","era_detail":"20世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"maugham","author_name":"威廉·萨默塞特·毛姆",
"year_display":"1915年（作者页注记：Britannica——人性的枷锁 1915 半自传）","year_sort":1915,
"background":["作者页注记：人性的枷锁——'（Britannica：1915 半自传）'。","Britannica：毛姆——《月亮与六便士》作者（作者页交叉）。","题材（通说待核）：跛足孤儿菲利普的求索——艺术、爱情与自由。"],
"outline":["（通说待核）菲利普的海德堡/巴黎/伦敦：学徒生涯。","（通说待核）米尔德丽德的反复折磨与'人性的枷锁'。"],
"characters":[{"name":"菲利普·凯里","identity":"跛足孤儿","note":"（通说待核）"},{"name":"米尔德丽德","identity":"女招待","note":"（通说待核）"}],
"themes":["'半自传'（B注记）。",
 "枷锁：激情、宗教与金钱（通说待核）。",
 "医学生涯与艺术的取舍（通说待核）。"],
"influence":[{"text":"Britannica：'1915 半自传'（作者页注记）。","source":S_MG},{"text":"Britannica：毛姆的畅销书地位（作者页语境——待核）。","source":S_MG}],
"reading":{"difficulties":["半自传的传记对应。","爱德华时代伦敦。"],
 "editions":["《人性的枷锁》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"毛姆长篇首选；与《月亮与六便士》对读。"},
"pending":["菲利普·凯里人名核对（通说）。","1915年出版细节待核。","'波斯地毯'人生隐喻待核。"],
"sources":[S_MG],"year_source":S_MG,"author_source":S_MG,"related_works":["yueliangyuliubianshi" if "yueliangyuliubianshi" in existing else "kanbujian3","renshijian","sangeshibing"],
"svg":G("《人性的枷锁》枷锁结构图",[{"title":"菲利普","text":"跛足的求索（通说）","color":"main"},{"title":"米尔德丽德","text":"反复的折磨（通说）","color":"antagonist"},{"title":"枷锁","text":"激情与惯例（书名）","color":"gold"},{"title":"地毯","text":"人生无意义说（通说）","color":"family"}])},
# 4. 麦克尤恩《阿姆斯特丹》
{"id":"amusitedan","title":"阿姆斯特丹","original_title":"Amsterdam","region":"英国","era":"现当代","era_detail":"20世纪90年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mcewan","author_name":"伊恩·麦克尤恩",
"year_display":"1998年（作者页注记：Britannica——阿姆斯特丹——1998布克奖）","year_sort":1998,
"background":["作者页注记：阿姆斯特丹——'（Britannica：1998布克奖）'。","Britannica：麦克尤恩——当代英国作家（作者页语境——待核）。","题材（通说待核）：两位老友的'安乐死'协定——黑色的道德喜剧。"],
"outline":["（通说待核）莫莉葬礼后的协定：谁先失能谁被终结。","（通说待核）各自的堕落与阿姆斯特丹的结局。"],
"characters":[{"name":"弗农/克莱夫","identity":"老友","note":"（通说待核）"}],
"themes":["'安乐死'协定的黑色喜剧（通说待核）。",
 "媒体与艺术的自利（通说待核）。",
 "布克奖（B注记）。"],
"influence":[{"text":"Britannica：1998布克奖（作者页注记）。","source":src_of('mcewan')},{"text":"Britannica：麦克尤恩《赎罪》等（作者页交叉）。","source":src_of('mcewan')}],
"reading":{"difficulties":["双主角的镜像结构。","'协定'的道德反转。"],
 "editions":["《阿姆斯特丹》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"麦克尤恩获奖作；与《赎罪》对读。"},
"pending":["弗农/克莱夫人名核对（通说）。","1998年出版细节待核。","'安乐死'情节细节待核。"],
"sources":[src_of('mcewan')],"year_source":src_of('mcewan'),"author_source":src_of('mcewan'),"related_works":["zhongjiendeganjue","shizhangshijieshi","lu"],
"svg":G("《阿姆斯特丹》协定结构图",[{"title":"协定","text":"互相的毁灭（通说）","color":"antagonist"},{"title":"葬礼","text":"故事的起点（通说）","color":"family"},{"title":"布克","text":"1998（B注记）","color":"gold"},{"title":"黑色","text":"道德的喜剧（通说）","color":"main"}])},
# 5. 马哈福兹《我们街区的孩子们》
{"id":"womenjiequdehaizimen","title":"我们街区的孩子们","original_title":"أولاد حارتنا","region":"埃及","era":"近代","era_detail":"20世纪50年代末",
"genre":"长篇小说","genre_group":"小说","language":"阿拉伯语","author_id":"mahfouz","author_name":"纳吉布·马哈福兹",
"year_display":"1959年（作者页注记：Britannica——我们街区的孩子们 (1959，被禁)——'banned in Egypt for its religious themes'）","year_sort":1959,
"background":["作者页注记：我们街区的孩子们——'（Britannica：banned in Egypt for its religious themes）'。","Britannica：马哈福兹——1988诺奖（作者页交叉——待核）。","题材（通说待核）：小街巷的'群主'寓言——先知们的轮回与'杰巴拉维'。"],
"outline":["（通说待核）代代'孩子'争取街区的权利。","（通说待核）'杰巴拉维'的隐匿与诸子的牺牲。"],
"characters":[{"name":"杰巴拉维","identity":"街区之主","note":"（通说待核）"},{"name":"诸子（加巴拉等）","identity":"先知化身","note":"（通说待核）"}],
"themes":["宗教寓言的争议（B注记：banned...religious themes）。",
 "权力与分配的轮回（通说待核）。",
 "'1988诺奖'（作者页交叉——待核）。"],
"influence":[{"text":"Britannica：'banned in Egypt for its religious themes'（作者页注记）。","source":S_MF},{"text":"Britannica：马哈福兹'开罗三部曲'（作者页交叉）。","source":S_MF}],
"reading":{"difficulties":["寓言与宗教的边界。","先知谱系的对应（通说待核）。"],
 "editions":["《我们街区的孩子们》中译本（人民文学/上海译文等——通说待核）。","阿拉伯文原版。"],
 "order":"马哈福兹寓言篇；与'开罗三部曲'对读。"},
"pending":["杰巴拉维等人名核对（通说）。","1959年连载（Al-Ahram说）与禁书细节待核。","'诺奖1988'交叉核对。"],
"sources":[S_MF],"year_source":S_MF,"author_source":S_MF,"related_works":["renshijian","aiyuheandegushi","tangjihuade"],
"svg":G("《我们街区的孩子们》寓言结构图",[{"title":"杰巴拉维","text":"隐匿的'主'（通说）","color":"gold"},{"title":"孩子们","text":"代代的抗争（通说）","color":"main"},{"title":"禁书","text":"宗教的争议（B注记）","color":"antagonist"},{"title":"街区","text":"世界的缩影（通说）","color":"family"}])},
# 6. 马哈福兹《小偷与狗》
{"id":"xiaotouyugou","title":"小偷与狗","original_title":"اللص والكلاب","region":"埃及","era":"近代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"阿拉伯语","author_id":"mahfouz","author_name":"纳吉布·马哈福兹",
"year_display":"1961年（作者页注记：Britannica 列举——小偷与狗 (1961)）","year_sort":1961,
"background":["作者页注记：小偷与狗——'（Britannica 列举）'。","Britannica：马哈福兹——开罗三部曲之后的转向（作者页语境——待核）。","题材（通说待核）：出狱的贼赛义德对'背叛者'的复仇——存在主义色调。"],
"outline":["（通说待核）赛义德出狱：妻子改嫁、女儿疏远。","（通说待核）复仇的循环与'狗'的意象。"],
"characters":[{"name":"赛义德·马兰","identity":"出狱的贼","note":"（通说待核）"}],
"themes":["复仇与虚无（通说待核）。",
 "'狗'：被背叛者与背叛者（书名语境——通说待核）。",
 "开罗市井的存在主义（作者页语境——待核）。"],
"influence":[{"text":"Britannica：小偷与狗 (1961)（作者页注记）。","source":S_MF},{"text":"Britannica：马哈福兹现实主义转向（作者页语境——待核）。","source":S_MF}],
"reading":{"difficulties":["60年代阿拉伯政治语境。","内心独白（意识流——通说待核）。"],
 "editions":["《小偷与狗》中译本（人民文学等——通说待核）。","阿拉伯文原版。"],
 "order":"马哈福兹'新现实主义'首选。"},
"pending":["赛义德人名核对（通说）。","1961年出版细节待核。","'意识流'手法说法待核。"],
"sources":[S_MF],"year_source":S_MF,"author_source":S_MF,"related_works":["womenjiequdehaizimen","dixiashishouji","xiniu"],
"svg":G("《小偷与狗》复仇结构图",[{"title":"赛义德","text":"出狱的复仇者（通说）","color":"main"},{"title":"狗","text":"背叛者的意象（书名）","color":"antagonist"},{"title":"虚无","text":"复仇的空洞（通说）","color":"gold"},{"title":"开罗","text":"市井的存在（通说）","color":"family"}])},
# 7. 弥尔顿《论出版自由》
{"id":"lunichubanziyou","title":"论出版自由","original_title":"Areopagitica","region":"英国","era":"古代","era_detail":"17世纪40年代",
"genre":"演讲文","genre_group":"散文","language":"英语","author_id":"milton","author_name":"约翰·弥尔顿",
"year_display":"1644年（作者页注记：Britannica——论出版自由 (1644)——言论自由经典）","year_sort":1644,
"background":["作者页注记：论出版自由 (1644)——'言论自由经典（Britannica）'。","Britannica：弥尔顿——《失乐园》作者（作者页交叉）。","题材（通说待核）：致英国国会——反对预先审查制（licensing）。"],
"outline":["（通说待核）'真理的种子'：审查的荒谬。","（通说待核）'阿雷奥帕古'：雅典法庭的隐喻。"],
"characters":[{"name":"（演讲文无人物）","identity":"——","note":"政论文"}],
"themes":["出版自由的经典论证（B注记）。",
 "'真理与审查'（通说待核）。",
 "内战时期的言论政治（通说待核）。"],
"influence":[{"text":"Britannica：'言论自由经典'（作者页注记）。","source":S_MI},{"text":"Britannica：《失乐园》为代表作（作者页交叉）。","source":S_MI}],
"reading":{"difficulties":["17世纪英语政论文。","英国长期国会语境（通说待核）。"],
 "editions":["《论出版自由》中译本（商务印书馆等——通说待核）。","英文原版（公有领域）。"],
 "order":"弥尔顿散文首选；与《失乐园》对读。"},
"pending":["'Areopagitica'标题直译核对。","1644年发表细节待核。","'预先审查'（licensing）制度细节待核。"],
"sources":[S_MI],"year_source":S_MI,"author_source":S_MI,"related_works":["shiyuandeyi" if "shiyuandeyi" in existing else "leiyu","fushide","zhainazhitan"],
"svg":G("《论出版自由》自由结构图",[{"title":"出版","text":"审查的靶子（书名）","color":"main"},{"title":"真理","text":"'被杀不死'（通说）","color":"gold"},{"title":"国会","text":"致意的对象（通说）","color":"family"},{"title":"内战","text":"言论的政治（通说）","color":"antagonist"}])},
# 8. 海涅《罗曼采罗》
{"id":"luomansailuo","title":"罗曼采罗","original_title":"Romanzero","region":"德国","era":"近代","era_detail":"19世纪50年代初",
"genre":"诗集","genre_group":"诗歌","language":"德语","author_id":"heine","author_name":"海因里希·海涅",
"year_display":"1851年（作者页注记：Britannica——罗曼采罗 (1851)——晚期诗集）","year_sort":1851,
"background":["作者页注记：罗曼采罗 (1851)——'晚期诗集（Britannica）'。","Britannica：海涅——德语诗人（作者页语境）。","题材（通说待核）：病榻上的三卷——'谣曲''沉思''希伯来旋律'。"],
"outline":["（通说待核）三卷结构：谣曲/沉思/希伯来旋律（卷名通说待核）。","（通说待核）'流亡与病痛'的自我审视。"],
"characters":[{"name":"抒情'我'","identity":"流亡病者","note":"（通说待核）"}],
"themes":["'晚期风格'的忧郁（B注记：晚期诗集）。",
 "'希伯来旋律'：犹太身份的回归（通说待核）。",
 "谣曲的叙事（通说待核）。"],
"influence":[{"text":"Britannica：Romanzero (1851)——晚期诗集（作者页注记）。","source":S_HE},{"text":"Britannica：海涅诗歌序列（作者页交叉）。","source":S_HE}],
"reading":{"difficulties":["三卷结构。","'希伯来旋律'的文化语境。"],
 "editions":["《罗曼采罗》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"海涅晚期；与《诗歌集》对读。"},
"pending":["三卷卷名核对（通说）。","1851年出版细节待核。","'病榻'写作细节待核。"],
"sources":[S_HE],"year_source":S_HE,"author_source":S_HE,"related_works":["shigetu","dongtiantonghua","wuguigu"],
"svg":G("《罗曼采罗》晚期结构图",[{"title":"谣曲","text":"叙事的回声（通说）","color":"main"},{"title":"希伯来旋律","text":"身份的回归（通说）","color":"gold"},{"title":"病榻","text":"晚期的自审（通说）","color":"antagonist"},{"title":"流亡","text":"巴黎的岁月（通说）","color":"family"}])},
# 9. 艾略特《神圣的树林》
{"id":"shenshendeshulin","title":"神圣的树林","original_title":"The Sacred Wood","region":"英国","era":"近代","era_detail":"20世纪20年代初",
"genre":"批评文集","genre_group":"散文","language":"英语","author_id":"eliot","author_name":"T.S.艾略特",
"year_display":"1920年（作者页注记：Britannica——The Sacred Wood (1920)）","year_sort":1920,
"background":["作者页注记：神圣的树林——'批评文集（Britannica：The Sacred Wood (1920)）'。","Britannica：艾略特——《传统与个人才能》等名文出处（待核——B注记未载篇目）。","题材（通说待核）：'传统与个人才能'、'玄学派诗人'等批评纲领。"],
"outline":["（通说待核）'传统'：非个人的诗学。","（通说待核）'客观对应物'（objective correlative——通说待核——篇目归属待核）。"],
"characters":[{"name":"（批评文集无人物）","identity":"——","note":"批评"}],
"themes":["'传统与个人才能'的诗学（通说待核——篇目归属待核）。",
 "批评的现代转向（B注记语境）。",
 "'非个人化'理论（通说待核）。"],
"influence":[{"text":"Britannica：The Sacred Wood (1920)（作者页注记）。","source":S_EL},{"text":"Britannica：艾略特批评家身份（作者页交叉）。","source":S_EL}],
"reading":{"difficulties":["批评术语（客观对应物等）。","17-19世纪英国文学史底本。"],
 "editions":["《神圣的树林》中译名（《传统与个人才能》单行本说）待核。","英文原版（公有领域状态待核）。"],
 "order":"艾略特批评首选；与《荒原》对读。"},
"pending":["篇目（'传统与个人才能'1921说——收录与否）核对。","1920年出版细节待核。","'客观对应物'篇目（《哈姆雷特》文说）待核。"],
"sources":[S_EL],"year_source":S_EL,"author_source":S_EL,"related_works":["sigesizhongzou","kanbujian3","laokong"],
"svg":G("《神圣的树林》批评结构图",[{"title":"传统","text":"非个人化的诗学（通说）","color":"main"},{"title":"树林","text":"批评的殿堂（书名）","color":"gold"},{"title":"玄学派","text":"重估的纲领（通说）","color":"family"},{"title":"1920","text":"结集之年（B注记）","color":"antagonist"}])},
# 10. 吉卜林《山里的平凡故事》
{"id":"shanlidepingfan","title":"山里的平凡故事","original_title":"Plain Tales from the Hills","region":"英国","era":"近代","era_detail":"19世纪80年代末",
"genre":"短篇小说集","genre_group":"故事集","language":"英语","author_id":"kipling","author_name":"拉迪亚德·吉卜林",
"year_display":"1888年（Britannica B277：Plain Tales from the Hills 1888）","year_sort":1888,
"background":["Britannica（B277）：Plain Tales from the Hills 1888——吉卜林早期印度短篇集。","Britannica（B277）：吉卜林——1907诺奖（作者页交叉——待核）。","题材（通说待核）：英属印度的'山间车站'——四十篇军政故事。"],
"outline":["（通说待核）西姆拉社会的众生相：军官、婚姻与流言。","（通说待核）'吉卜林式'的反讽结尾。"],
"characters":[{"name":"众篇人物","identity":"英印官员","note":"（通说待核）"}],
"themes":["英印社会的讽刺（通说待核）。",
 "'山里'：西姆拉避暑地（书名语境——通说待核）。",
 "短篇的反讽技艺（通说待核）。"],
"influence":[{"text":"Britannica：Plain Tales from the Hills 1888（B277）。","source":"B277"},{"text":"Britannica：吉卜林诺奖（B277 作者页交叉）。","source":"B277"}],
"reading":{"difficulties":["英印术语（'山站'等）。","40篇的体量。"],
 "editions":["《山里的平凡故事》中译本（人民文学等——通说待核）。","英文原版（公有领域）。"],
 "order":"吉卜林早期首选；与《丛林之书》对读。"},
"pending":["篇数（40篇说）核对（通说）。","1888年出版（Calcutta说）待核。","'西姆拉'背景细节待核。"],
"sources":["B277"],"year_source":"B277","author_source":"B277","related_works":["conglinzhishu" if "conglinzhishu" in existing else "leiyu","jimye" if "jimye" in existing else "luoshengmen","luoting"],
"svg":G("《山里的平凡故事》印度讽刺图",[{"title":"山站","text":"西姆拉的凉夏（通说）","color":"family"},{"title":"众生","text":"英印的浮世（通说）","color":"main"},{"title":"反讽","text":"吉卜林式结尾（通说）","color":"gold"},{"title":"1888","text":"成名的前夜（B277）","color":"antagonist"}])},
# 11. 戈尔丁《过界的仪式》
{"id":"guojideyishi","title":"过界的仪式","original_title":"Rites of Passage","region":"英国","era":"现当代","era_detail":"20世纪80年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"golding","author_name":"威廉·戈尔丁",
"year_display":"1980年（作者页注记：Britannica——过界的仪式（1980布克奖）——Sea trilogy）","year_sort":1980,
"background":["作者页注记：过界的仪式——'（1980布克奖）——Sea trilogy（Britannica）'。","Britannica：戈尔丁——《蝇王》作者、1983诺奖（作者页交叉——待核）。","题材（通说待核）：1812年驶往澳大利亚的船——日记体的海上'仪式'。"],
"outline":["（通说待核）塔尔伯特的日记：绅士的傲慢与海上惩罚。","（通说待核）'过界'：跨越赤道仪式与阶级的深渊。"],
"characters":[{"name":"塔尔伯特","identity":"贵族青年/日记者","note":"（通说待核）"}],
"themes":["航海日记的文体（通说待核）。",
 "阶级与'文明'的假面（通说待核）。",
 "海洋三部曲之首（B注记：Sea trilogy）。"],
"influence":[{"text":"Britannica：1980布克奖（作者页注记）。","source":S_GO},{"text":"Britannica：1983诺奖（作者页交叉——待核）。","source":S_GO}],
"reading":{"difficulties":["19世纪航海史。","日记体的不可靠。"],
 "editions":["《过界的仪式》中译名（《航祭》）待核。","英文原版。"],
 "order":"戈尔丁中期；与《蝇王》对读。"},
"pending":["塔尔伯特人名核对（通说）。","1980年出版（Faber说）待核。","'海洋三部曲'卷次核对。"],
"sources":[S_GO],"year_source":S_GO,"author_source":S_GO,"related_works":["yingwang","shizhangshijieshi","nongmin"],
"svg":G("《过界的仪式》航海结构图",[{"title":"帆船","text":"驶向南半球的木船（通说）","color":"family"},{"title":"日记","text":"傲慢的记录（通说）","color":"main"},{"title":"仪式","text":"跨越赤道（书名）","color":"gold"},{"title":"布克","text":"1980（B注记）","color":"antagonist"}])},
# 12. 拉克斯内斯《会唱歌的鱼》
{"id":"huichanggedeyu","title":"会唱歌的鱼","original_title":"Brekkukotsannáll","region":"冰岛","era":"现当代","era_detail":"20世纪50年代末",
"genre":"长篇小说","genre_group":"小说","language":"冰岛语","author_id":"laxness","author_name":"哈尔多尔·拉克斯内斯",
"year_display":"1957年（Britannica B361：Brekkukotsannáll (1957; The Fish Can Sing)——中译名待核）","year_sort":1957,
"background":["Britannica（B361）：Brekkukotsannáll——'more lyrical and introspective'（B361：1950年代后更抒情内省）。","Britannica（B361）：拉克斯内斯——1955诺奖。","题材（通说待核）：孤童阿尔夫格里姆在雷克雅未克'泥棚'的成长与'会唱歌的鱼'传说。"],
"outline":["（通说待核）'泥棚编年'：孤童与收养他的老夫妇。","（通说待核）'会唱歌的鱼'：加尔巴尔的声名与死亡。"],
"characters":[{"name":"阿尔夫格里姆","identity":"孤童","note":"（通说待核）"},{"name":"加尔巴尔","identity":"歌唱家","note":"（通说待核）"}],
"themes":["'抒情内省'的晚期风格（B361）。",
 "孤童的成长（通说待核）。",
 "冰岛小社会的幽默（通说待核）。"],
"influence":[{"text":"Britannica：Brekkukotsannáll (1957)（B361）。","source":"B361"},{"text":"Britannica：'more lyrical and introspective'（B361）。","source":"B361"}],
"reading":{"difficulties":["冰岛首都的市井语调。","'编年'的幽默。"],
 "editions":["《会唱歌的鱼》中译名（《唱歌的鱼》）待核。","冰岛文原版。"],
 "order":"拉克斯内斯抒情篇；与《独立的人们》对读。"},
"pending":["阿尔夫格里姆/加尔巴人名核对（通说）。","1957年出版细节待核。","'泥棚'（Brekkukot）细节待核。"],
"sources":["B361"],"year_source":"B361","author_source":"B361","related_works":["dulidemen","bingdaozhizhong","nongmin"],
"svg":G("《会唱歌的鱼》成长结构图",[{"title":"泥棚","text":"成长的角落（通说）","color":"family"},{"title":"孤童","text":"阿尔夫格里姆（通说）","color":"main"},{"title":"歌者","text":"传说的声名（通说）","color":"antagonist"},{"title":"抒情","text":"'内省'的风格（B361）","color":"gold"}])},
# 13. 哈珀·李《设立守望者》
{"id":"shelishouwangzhe","title":"设立守望者","original_title":"Go Set a Watchman","region":"美国","era":"现当代","era_detail":"21世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"lee","author_name":"哈珀·李",
"year_display":"2015年（作者页注记：Britannica——设立守望者（2015））","year_sort":2015,
"background":["作者页注记：设立守望者——'（Britannica）'。","Britannica：哈珀·李——《杀死一只知更鸟》作者（作者页交叉）。","题材（通说待核）：《知更鸟》二十年后的琼·露易丝返乡——种族立场的幻灭。"],
"outline":["（通说待核）斯库特（琼·露易丝）从纽约回梅科姆。","（通说待核）父亲阿蒂克斯的'另一面'。"],
"characters":[{"name":"琼·露易丝","identity":"成年斯库特","note":"（通说待核）"},{"name":"阿蒂克斯","identity":"父亲","note":"（通说待核）"}],
"themes":["'知更鸟'前传还是续章的争议（通说待核）。",
 "成年后对父亲的幻灭（通说待核）。",
 "2015年的出版风波（作者页语境——待核）。"],
"influence":[{"text":"Britannica：Go Set a Watchman (2015)（作者页注记）。","source":src_of('lee')},{"text":"Britannica：《杀死一只知更鸟》为代表作（作者页交叉）。","source":src_of('lee')}],
"reading":{"difficulties":["与《知更鸟》的关系定位。","1950年代南方种族语境。"],
 "editions":["《设立守望者》中译名（《守望之心》）待核。","英文原版。"],
 "order":"《知更鸟》续读（或前稿）；需注意其立场差异。"},
"pending":["2015年出版（Harper说）与'发现手稿'风波待核。","琼·露易丝人名核对（通说）。","'前稿/续篇'的争议待核。"],
"sources":[src_of('lee')],"year_source":src_of('lee'),"author_source":src_of('lee'),"related_works":["zhishigengniao" if "zhishigengniao" in existing else "kanbujian3","xiangtianhuhan","yuwanghaojieche"],
"svg":G("《设立守望者》幻灭结构图",[{"title":"返乡","text":"成年的斯库特（通说）","color":"main"},{"title":"守望者","text":"圣经的隐喻（书名）","color":"gold"},{"title":"父亲","text":"幻灭的偶像（通说）","color":"antagonist"},{"title":"梅科姆","text":"1950年代的南方（通说）","color":"family"}])},
# 14. 莱辛《明娜·冯·巴尔赫姆》
{"id":"mingnafengbaerhemu","title":"明娜·冯·巴尔赫姆","original_title":"Minna von Barnhelm","region":"德国","era":"近代","era_detail":"18世纪60年代",
"genre":"喜剧","genre_group":"戏剧","language":"德语","author_id":"lessing","author_name":"戈特霍尔德·埃夫莱姆·莱辛",
"year_display":"1767年（Britannica B368：Minna von Barnhelm (1767)——'marks the birth of classical German comedy'）","year_sort":1767,
"background":["Britannica（B368）：'marks the birth of classical German comedy'（古典德国喜剧的诞生）。","Britannica（B368）：莱辛——'helped free German drama from the influence of classical and French models'。","题材（通说待核）：七年战争后的军官台尔海姆与明娜——荣誉的误会与订婚。"],
"outline":["（通说待核）战后军官的'荣誉'困境与明娜的到来。","（通说待核）戒指的双关与和解。"],
"characters":[{"name":"台尔海姆","identity":"少校","note":"（通说待核）"},{"name":"明娜·冯·巴尔赫姆","identity":"富家女","note":"（B368 书名人物）"}],
"themes":["'古典德国喜剧的诞生'（B368）。",
 "荣誉与爱情的和解（通说待核）。",
 "七年战争的战后语境（通说待核）。"],
"influence":[{"text":"Britannica：'marks the birth of classical German comedy'（B368）。","source":"B368"},{"text":"Britannica：莱辛戏剧解放（B368 作者级）。","source":"B368"}],
"reading":{"difficulties":["喜剧的误会结构。","七年战争史。"],
 "editions":["《明娜·冯·巴尔赫姆》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"莱辛喜剧首选；与《智者纳坦》对读。"},
"pending":["台尔海姆人名核对（通说）。","1767年首演（汉堡说）待核。","'戒指'细节待核。"],
"sources":["B368"],"year_source":"B368","author_source":"B368","related_works":["zhainazhitan","laokong","leiyu"],
"svg":G("《明娜·冯·巴尔赫姆》喜剧结构图",[{"title":"明娜","text":"订婚的坚持（B368）","color":"main"},{"title":"荣誉","text":"误会的根源（通说）","color":"antagonist"},{"title":"喜剧","text":"'古典的诞生'（B368）","color":"gold"},{"title":"战后","text":"军官的困境（通说）","color":"family"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批49）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('hunlidechengyuan','mccalles','婚礼的成员'),('shangxinkafeizhige','mccalles','伤心咖啡馆之歌'),('renxingdejiasuo','maugham','人性的枷锁'),('amusitedan','mcewan','阿姆斯特丹'),('womenjiequdehaizimen','mahfouz','我们街区的孩子们'),('xiaotouyugou','mahfouz','小偷与狗'),('lunichubanziyou','milton','论出版自由'),('luomansailuo','heine','罗曼采罗'),('shenshendeshulin','eliot','神圣的树林'),('shanlidepingfan','kipling','山里的平凡故事'),('guojideyishi','golding','过界的仪式'),('huichanggedeyu','laxness','会唱歌的鱼'),('shelishouwangzhe','lee','设立守望者'),('mingnafengbaerhemu','lessing','明娜·冯·巴尔赫姆')]:
    if wid in created:
        link(aid, wid, kw)

# 过期条目清理：amiller 炼狱（salemwunv 已存在）、beckett 莫洛伊三部曲（moluoyi 已存在）
for aid, stale_kw, wid_new, note_new in [('amiller', '炼狱/萨勒姆的女巫', 'salemwunv', '（B325：The Crucible, 1953——即本库《萨勒姆的女巫》）'), ('beckett', '莫洛伊三部曲', 'moluoyi', '（B094：莫洛伊三部曲——即本库《莫洛伊》）')]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    for i, m in enumerate(j['major_works']):
        if m.get('title') and stale_kw in m['title'] and not m.get('work_id'):
            j['major_works'][i] = {"work_id": wid_new, "note": note_new}
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('stale fixed', aid)
print('BATCH49 DONE')
