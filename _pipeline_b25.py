# -*- coding: utf-8 -*-
"""批25：Britannica 新核 3 作家 4 部（斯韦沃/尤涅斯库x2/蒙塔莱 B339-B341）"""
import json, pathlib

newsrc = [
{"id":"B339","title":"Italo Svevo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Italo-Svevo","type":"百科全书","verified":True,"covers":["svevo","zenodeyishi"],"note":"2026-11-21 核对：原名 Ettore Schmitz；1861-12-19的里雅斯特（奥匈帝国，今意大利）生—1928-09-13 Motta di Livenza卒（66岁，车祸）；La coscienza di Zeno (1923)——'a brilliant work in the form of a patient's statement for his psychiatrist'——自费出版；'a pioneer of the psychological novel in Italy'；Senilità (1898)——'featuring another bewildered hero'；Una vita (1892)——'the agonies of an ineffectual hero'；1907年英语家庭教师为乔伊斯，乔伊斯对其早期两部小说的推崇促使其重返写作；法国评论家 Larbaud 与 Crémieux 后为其扬名；蒙塔莱1925年在 L'Esame 撰文推崇"},
{"id":"B340","title":"Eugene Ionesco — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Eugene-Ionesco","type":"百科全书","verified":True,"covers":["ionesco","toutougeonv"],"note":"2026-11-21 核对：1909-11-26罗马尼亚Slatina生—1994-03-28巴黎卒（84岁）；'whose one-act antiplay La Cantatrice chauve (1949; The Bald Soprano) inspired a revolution in dramatic techniques and helped inaugurate the Theatre of the Absurd'；1970入选法兰西学院；自称' Theatre of derision'；Rhinoceros (1959)——'a play about totalitarianism, remains Ionesco's most popular work'；'the absurdity of bourgeois life, the meaninglessness of social conventions, and the futile and mechanical nature of modern civilization'；The Bald Soprano——'masterly catalog of senseless platitudes'；道具的'humorous multiplication of objects on stage until they overwhelm the actors'；The Lesson (1951)、The Chairs (1952)、Exit the King (1962)、Macbett (1972)——Macbeth重述"},
{"id":"B341","title":"Eugenio Montale — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Eugenio-Montale","type":"百科全书","verified":True,"covers":["montale","wuguigu"],"note":"2026-11-21 核对：1896-10-12热那亚生—1981-09-12米兰卒（84岁）；1975诺贝尔文学奖；Ossi di seppia (1925; Cuttlefish Bones 乌贼骨)——'expressed the bitter pessimism of the postwar period'；'A tragic vision of the world as a dry, barren, hostile wilderness'；Le occasioni (1939)、Finisterre (1943)、La bufera e altro (1956)、Satura (1962)、Xenia (1966)——'gentle and evocative series of love poems in memory of his wife'；隐逸派（Hermeticism）——'emotional suggestiveness of words and a symbolism of purely subjective meaning'；'progressively more introverted and obscure'；学过声乐、一战服役、1929-38年佛罗伦萨 Gabinetto Vieusseux 图书馆馆长、后任晚邮报文学与音乐编辑；译莎翁/艾略特/霍普金斯/梅尔维尔/奥尼尔"},
]
raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in newsrc:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
srcs = json.load(open('sources.json', encoding='utf-8'))
have = {s['id'] for s in srcs}
srcs.extend(s for s in newsrc if s['id'] not in have)
pathlib.Path('sources.json').write_text(json.dumps(srcs, ensure_ascii=False, indent=1), encoding='utf-8')
print('sources:', len(srcs))

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
def find_work(aid, prefer=None):
    got = [p.stem for p in pathlib.Path('data/works').glob('*.json') if json.load(open(p, encoding='utf-8'))['author_id'] == aid]
    for pref in prefer or []:
        if pref in got: return pref
    return got[0] if got else 'leiyu'

rel_zeno = ['yigewushiwan', find_work('kafka', ['chengbao', 'bianxingji']), 'xinshigudeLieshou']
rel_bald = ['dengdaigou', 'liugejuesesouzhao', 'leiyu']
rel_rhino = ['toutougeonv', 'dengdaigou', 'salemwunv']
rel_mont = ['diyuzhiji' if 'diyuzhiji' in existing else 'ezhihua', 'ezhihua', find_work('eliot', [])]
rel_mont = [r for r in rel_mont if r in existing][:3] or ['ezhihua']
print('rel:', rel_zeno, rel_bald, rel_rhino, rel_mont)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"svevo","name":"伊塔洛·斯韦沃","foreign_name":"Italo Svevo（伊塔洛·斯韦沃，原名 Ettore Schmitz，1861-12-19—1928-09-13）","country":"意大利","birth":1861,"death":1928,"birth_year":1861,"death_year":1928,"era":"近代",
"summary":"斯韦沃，原名 Ettore Schmitz，的里雅斯特生（时属奥匈帝国），意大利小说家——'a pioneer of the psychological novel in Italy'（意大利心理小说的先驱——B339）。La coscienza di Zeno（泽诺的意识, 1923）——'a brilliant work in the form of a patient's statement for his psychiatrist'（以病人向精神医生的自述为形式的天才之作——B339）——最初自费出版（B339）。1907年他的英语家庭教师是乔伊斯；乔伊斯对其早期两部小说的推崇促使他重返写作（B339）；后经法国评论家 Larbaud 与 Crémieux 扬名（B339）；蒙塔莱1925年在 L'Esame 撰文推崇（B339）。1928年9月13日因车祸卒（B339）。",
"timeline":[
 {"year":1861,"text":"12月19日生于的里雅斯特（B339：Born Dec. 19, 1861, Trieste, Austrian Empire）。","src":"B339"},
 {"year":1892,"text":"处女作 Una vita——'the agonies of an ineffectual hero'，出版后被忽视（B339）。","src":"B339"},
 {"year":1907,"text":"英语家庭教师乔伊斯到任；乔伊斯的推崇促使其重返写作（B339）。","src":"B339"},
 {"year":1923,"text":"《泽诺的意识》自费出版（B339）。","src":"B339"},
 {"year":1928,"text":"9月13日因车祸卒于 Motta di Livenza（B339）。","src":"B339"}],
"major_works":[
 {"work_id":"zenodeyishi","note":"1923（B339）"},
 {"title":"暮老/年长之后","note":"（B339：Senilità (1898)——'featuring another bewildered hero'——中译名待核）"},
 {"title":"一生","note":"（B339：Una vita (1892)）"}],
"style":["病人自述体的心理书写（B339：patient's statement for his psychiatrist）。",
 "'ineffective hero'——无能者的悲剧（B339：ineffectual/bewildered hero）。",
 "的里雅斯特商人与作家的双重身份（B339 语境：German-Jewish glassware merchant 之子）。"],
"status":"Britannica 定位斯韦沃为意大利心理小说的先驱；乔伊斯是其文学复出的推手（B339）。",
"sources":["B339"],"dates_source":"B339",
"pending":["Senilità 通行中译名（《暮老》/《年长之后》）待核。","《泽诺的意识》1923年 Cappelli 出版社自费出版说待核。","乔伊斯授课细节（Berlitz学校说）待核。"]},
{"id":"ionesco","name":"欧仁·尤涅斯库","foreign_name":"Eugène Ionesco（欧仁·尤涅斯库，1909-11-26—1994-03-28）","country":"法国","birth":1909,"death":1994,"birth_year":1909,"death_year":1994,"era":"现当代",
"summary":"尤涅斯库，罗马尼亚 Slatina 生、巴黎成家，法国剧作家——'whose one-act antiplay La Cantatrice chauve (1949; The Bald Soprano) inspired a revolution in dramatic techniques and helped inaugurate the Theatre of the Absurd'（其独幕'反戏剧'《秃头歌女》引发戏剧技巧的革命并促成荒诞派——B340）。1970年入选法兰西学院（B340）。他更愿意称自己的戏剧为'theatre of derision'（嘲弄的戏剧——B340）。Rhinoceros（犀牛, 1959）——'a play about totalitarianism, remains Ionesco's most popular work'（B340）。其戏剧呈现'the absurdity of bourgeois life, the meaninglessness of social conventions, and the futile and mechanical nature of modern civilization'（B340）。",
"timeline":[
 {"year":1909,"text":"11月26日生于罗马尼亚 Slatina（B340）。","src":"B340"},
 {"year":1949,"text":"独幕'反戏剧'《秃头歌女》——促成荒诞派（B340）。","src":"B340"},
 {"year":1959,"text":"《犀牛》——关于极权主义的剧作，其最受欢迎的作品（B340）。","src":"B340"},
 {"year":1970,"text":"入选法兰西学院（B340）。","src":"B340"},
 {"year":1994,"text":"3月28日卒于巴黎（B340）。","src":"B340"}],
"major_works":[
 {"work_id":"toutougeonv","note":"1949（B340）"},
 {"work_id":"xiniu","note":"1959（B340）"},
 {"title":"椅子","note":"（B340：Les Chaises (1952)）"},
 {"title":"国王死去","note":"（B340：Exit the King (1962)——中译名待核）"}],
"style":["'反戏剧'与'反逻辑'（B340：antiplay / antilogical）。",
 "陈词滥调与无序对话（B340：clichés, non sequiturs——'masterly catalog of senseless platitudes'）。",
 "道具的滑稽增殖直至淹没演员（B340：multiplication of objects on stage）。"],
"status":"Britannica 定位尤涅斯库为荒诞派戏剧的开创者之一、法兰西学院院士（B340）。",
"sources":["B340"],"dates_source":"B340",
"pending":["《秃头歌女》1949年巴黎首演（Théâtre des Noctambules说）待核。","《犀牛》1960年伦敦演出细节待核。","'theatre of derision'通行译名待核。"]},
{"id":"montale","name":"埃乌杰尼奥·蒙塔莱","foreign_name":"Eugenio Montale（埃乌杰尼奥·蒙塔莱，1896-10-12—1981-09-12）","country":"意大利","birth":1896,"death":1981,"birth_year":1896,"death_year":1981,"era":"现当代",
"summary":"蒙塔莱，热那亚生，意大利诗人——1975年诺贝尔文学奖（B341）。Ossi di seppia（乌贼骨, 1925）——'expressed the bitter pessimism of the postwar period'（表达了战后年代的苦涩悲观——B341）——'A tragic vision of the world as a dry, barren, hostile wilderness'（把世界看作干涸荒芜充满敌意的荒野的悲剧性视野——B341）。此后 Le occasioni (1939)、Finisterre (1943)、Satura (1962)；Xenia (1966)——'gentle and evocative series of love poems in memory of his wife'（悼亡妻的温柔组诗——B341）。属隐逸派（Hermeticism）传统——'emotional suggestiveness of words and a symbolism of purely subjective meaning'（B341）。",
"timeline":[
 {"year":1896,"text":"10月12日生于热那亚（B341）。","src":"B341"},
 {"year":1925,"text":"Ossi di seppia（乌贼骨）——战后苦涩悲观（B341）。","src":"B341"},
 {"year":1939,"text":"Le occasioni（B341）。","src":"B341"},
 {"year":1975,"text":"获诺贝尔文学奖（B341）。","src":"B341"},
 {"year":1981,"text":"9月12日卒于米兰（B341）。","src":"B341"}],
"major_works":[
 {"work_id":"wuguigu","note":"1925（B341）"},
 {"title":" occasions/境遇","note":"（B341：Le occasioni (1939)——中译名待核）"},
 {"title":"萨图拉","note":"（B341：Satura (1962)）"}],
"style":["'干涸荒芜的荒野'的悲剧性视野（B341）。",
 "隐逸派：词的情感暗示与纯主观的象征（B341：Hermeticism）。",
 "越来越内省与晦涩（B341：progressively more introverted and obscure）。"],
"status":"Britannica 定位蒙塔莱为1975年诺奖得主、意大利隐逸派代表诗人（B341）。",
"sources":["B341"],"dates_source":"B341",
"pending":["Le occasioni 通行中译名待核。","诺奖授奖词细节待核。","隐逸派与'纯诗'论的关系待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"zenodeyishi","title":"泽诺的意识","original_title":"La coscienza di Zeno","region":"意大利","era":"近代","era_detail":"20世纪20年代",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"svevo","author_name":"伊塔洛·斯韦沃",
"year_display":"1923年（Britannica B339：La coscienza di Zeno (1923)——自费出版）","year_sort":1923,
"background":["Britannica（B339）：'a brilliant work in the form of a patient's statement for his psychiatrist'——小说以病人写给精神医生的自述为形式。","Britannica（B339）：斯韦沃——'a pioneer of the psychological novel in Italy'。","Britannica（B339）：本书最初由作者自费出版；此前两部小说出版后被忽视，乔伊斯的推崇促使其重返写作。"],
"outline":["'病人'泽诺向精神医生自述：戒烟、婚姻、外遇、父丧与商海（自述章节结构通说待核——B339未载细节）。","'意识'的拖延与自我辩护：心理小说的先驱形式（B339：pioneer of the psychological novel）。"],
"characters":[{"name":"泽诺","identity":"病人/自述者","note":"（B339 书名人物）"},{"name":"精神医生","identity":"自述的接受者","note":"（通说待核，B339未载）"}],
"themes":["'意识'即自我辩护的档案（B339：patient's statement 形式）。","无能者与自欺的喜剧（B339：ineffectual hero 语系）。","精神分析与小说形式的交汇（B339 语境）。"],
"influence":[{"text":"Britannica：'a brilliant work...'（B339）。","source":"B339"},{"text":"Britannica：乔伊斯推动其复出、法国评论家与蒙塔莱为其扬名（B339）。","source":"B339"}],
"reading":{"difficulties":["自述体的不可靠叙述。","一战前后奥匈治下的的里雅斯特背景。"],
 "editions":["《泽诺的意识》中译本（人民文学/上海译文等——通说待核）。","意大利文原版。"],
 "order":"斯韦沃首选；可后接《暮老》。"},
"pending":["泽诺全名（Cosini说）核对（B339未载）。","章节名（烟/婚事/妻子之死等）核对。","1923年自费出版细节核对。"],
"sources":["B339"],"year_source":"B339","author_source":"B339","related_works":rel_zeno,
"svg":G("《泽诺的意识》自述结构图",[{"title":"泽诺","text":"自述的病人（B339）","color":"main"},{"title":"精神医生","text":"自述的档案（B339）","color":"gold"},{"title":"戒烟","text":"拖延与自欺（通说）","color":"antagonist"},{"title":"意识","text":"心理小说先驱（B339）","color":"family"}])},
{"id":"toutougeonv","title":"秃头歌女","original_title":"La Cantatrice chauve","region":"法国","era":"现当代","era_detail":"20世纪40年代末",
"genre":"独幕剧","genre_group":"戏剧","language":"法语","author_id":"ionesco","author_name":"欧仁·尤涅斯库",
"year_display":"1949年（Britannica B340：La Cantatrice chauve (1949; The Bald Soprano)）","year_sort":1949,
"background":["Britannica（B340）：'one-act antiplay'——'inspired a revolution in dramatic techniques and helped inaugurate the Theatre of the Absurd'（其独幕'反戏剧'引发戏剧技巧革命并促成荒诞派）。","Britannica（B340）：'masterly catalog of senseless platitudes'（对陈腐套话的大师级清点）。","Britannica（B340）：尤涅斯库自称其戏剧为'theatre of derision'（嘲弄的戏剧）。"],
"outline":["'反戏剧'：一场由陈词滥调组成的晚餐对话（B340：catalog of senseless platitudes——剧情细节通说待核）。","剧终人物互换与循环：'秃头歌女'并未出现（剧终细节通说待核）。"],
"characters":[{"name":"马丁夫妇/史密斯夫妇","identity":"两对中产夫妇","note":"（通说待核，B340未载）"},{"name":"消防队长","identity":"来客","note":"（通说待核，B340未载）"}],
"themes":["中产生活的荒诞（B340：the absurdity of bourgeois life）。","语言的失效：套话的空转（B340：senseless platitudes）。","'反戏剧'的形式宣言（B340：antiplay / antilogical）。"],
"influence":[{"text":"Britannica：'inspired a revolution in dramatic techniques and helped inaugurate the Theatre of the Absurd'（B340）。","source":"B340"},{"text":"Britannica：与贝克特等同为荒诞派源头（作者页 B340 定位）。","source":"B340"}],
"reading":{"difficulties":["'反戏剧'的舞台惯例。","伦敦腔套话的法语戏仿（原文语境）。"],
 "editions":["《秃头歌女》中译本（人民文学《荒诞派戏剧集》等——通说待核）。","法文原版。"],
 "order":"荒诞派入门首选；后接《犀牛》《等待戈多》。"},
"pending":["1949年首演（Théâtre des Noctambules说）与导演（Nicolas Bataille说）待核。","史密斯/马丁夫妇人名核对（B340未载）。","'antiplay'一词通行译法待核。"],
"sources":["B340"],"year_source":"B340","author_source":"B340","related_works":rel_bald,
"svg":G("《秃头歌女》语言空转图",[{"title":"晚餐","text":"套话的清点（B340）","color":"main"},{"title":"'反戏剧'","text":"antiplay（B340）","color":"gold"},{"title":"荒诞派","text":"由此开幕（B340）","color":"family"},{"title":"空转","text":"语言的失效（B340）","color":"antagonist"}])},
{"id":"xiniu","title":"犀牛","original_title":"Le Rhinocéros","region":"法国","era":"现当代","era_detail":"20世纪50年代末",
"genre":"戏剧","genre_group":"戏剧","language":"法语","author_id":"ionesco","author_name":"欧仁·尤涅斯库",
"year_display":"1959年（Britannica B340：Rhinoceros (1959)——'a play about totalitarianism, remains Ionesco's most popular work'）","year_sort":1959,
"background":["Britannica（B340）：Rhinoceros——'a play about totalitarianism'——'remains Ionesco's most popular work'（关于极权主义；仍是尤涅斯库最受欢迎的作品）。","Britannica（B340）：尤涅斯库戏剧呈现'意义的失落'与'现代文明的机械性'（the meaninglessness of social conventions, the futile and mechanical nature of modern civilization）。","题材（通说待核）：小城居民相继变成犀牛——'独善其身'者的抵抗与溃败。"],
"outline":["城里人一个个'变犀牛'：从街谈巷议到集体兽化（B340：about totalitarianism——变身情节通说待核）。","贝朗热的独留：'我还是人'的挣扎（人物名与结局通说待核）。"],
"characters":[{"name":"贝朗热","identity":"小职员","note":"（通说待核，B340未载）"},{"name":"让","identity":"朋友","note":"（通说待核，B340未载）"}],
"themes":["极权主义的'兽化'寓言（B340：about totalitarianism）。","从众与抵抗（通说待核）。","现代文明的机械性（B340：futile and mechanical nature of modern civilization）。"],
"influence":[{"text":"Britannica：'remains Ionesco's most popular work'（B340）。","source":"B340"},{"text":"Britannica：荒诞派开创者之一（B340 定位）。","source":"B340"}],
"reading":{"difficulties":["极权主义的历史语境（1930年代罗马尼亚铁卫团说待核）。","'变身'的舞台美学。"],
 "editions":["《犀牛》中译本（人民文学/上海译文等——通说待核）。","法文原版。"],
 "order":"尤涅斯库代表作；与《秃头歌女》并读。"},
"pending":["贝朗热/让人名核对（B340未载）。","1959年巴黎首演、1960年伦敦（奥利弗主演说）待核。","'集体狂热'意象与审巫案的互文待核。"],
"sources":["B340"],"year_source":"B340","author_source":"B340","related_works":rel_rhino,
"svg":G("《犀牛》兽化结构图",[{"title":"犀牛","text":"极权主义的兽化（B340）","color":"antagonist"},{"title":"贝朗热","text":"最后的人（通说）","color":"main"},{"title":"从众","text":"一个接一个（通说）","color":"family"},{"title":"抵抗","text":"'我还是人'（通说）","color":"gold"}])},
{"id":"wuguigu","title":"乌贼骨","original_title":"Ossi di seppia","region":"意大利","era":"现当代","era_detail":"20世纪20年代",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"montale","author_name":"埃乌杰尼奥·蒙塔莱",
"year_display":"1925年（Britannica B341：Ossi di seppia (1925; Cuttlefish Bones)）","year_sort":1925,
"background":["Britannica（B341）：Ossi di seppia——'expressed the bitter pessimism of the postwar period'（表达了战后年代的苦涩悲观）。","Britannica（B341）：'A tragic vision of the world as a dry, barren, hostile wilderness'——把世界视为干涸、荒芜、充满敌意的荒野的悲剧性视野。","Britannica（B341）：蒙塔莱属隐逸派传统——'emotional suggestiveness of words and a symbolism of purely subjective meaning'。"],
"outline":["利古里亚海岸的'干石'意象群：荒凉之地与'墙缝里的光'（意象通说待核——B341未载具体篇目）。","'苦涩悲观'的抒情化：个人声音对抗公共语言（B341 语境）。"],
"characters":[{"name":"抒情'我'","identity":"旁观者/幸存者","note":"（通说待核）"}],
"themes":["战后苦涩悲观（B341：bitter pessimism of the postwar period）。","世界即荒野的悲剧视野（B341）。","隐逸派：主观象征与词的暗示力（B341：Hermeticism）。"],
"influence":[{"text":"Britannica：蒙塔莱1975年诺奖（B341）。","source":"B341"},{"text":"Britannica：'progressively more introverted and obscure'——其后来诗风的起点（B341）。","source":"B341"}],
"reading":{"difficulties":["隐逸派的晦涩。","利古里亚海岸地名（莱里奇等——通说待核）。"],
 "editions":["《乌贼骨》中译本（人民文学/译林等——通说待核）。","意大利文原版。"],
 "order":"蒙塔莱首选；后接《境遇》(1939)。"},
"pending":["具体篇目（《常常身处 mechanical》等）核对——B341未载。","'干石/墙缝'意象细节待核。","1925年出版（Pier Angelo Soldini序说）待核。"],
"sources":["B341"],"year_source":"B341","author_source":"B341","related_works":rel_mont,
"svg":G("《乌贼骨》荒野意象图",[{"title":"乌贼骨","text":"海滩的残骸（通说）","color":"main"},{"title":"荒野","text":"干涸敌意的世界（B341）","color":"antagonist"},{"title":"悲观","text":"战后的苦涩（B341）","color":"gold"},{"title":"象征","text":"主观的暗示（B341）","color":"family"}])},
]
for w in works:
    assert w['id'] not in existing, f'dup {w["id"]}'
for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("svevo","zenodeyishi"),("ionesco","toutougeonv"),("ionesco","xiniu"),("montale","wuguigu")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B33x/B34x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH25 DONE')
