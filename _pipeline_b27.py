# -*- coding: utf-8 -*-
"""批27：Britannica 新核 3 作家 4 部（卡杜齐/桑德堡/多斯·帕索斯x2 B345-B347）"""
import json, pathlib

newsrc = [
{"id":"B345","title":"Giosue Carducci — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Giosue-Carducci","type":"百科全书","verified":True,"covers":["carducci","yemanli"],"note":"2026-11-21 核对：1835-07-27托斯卡纳Val di Castello（近卢卡）生—1907-02-16博洛尼亚卒（71岁）；1906诺贝尔文学奖；'one of the most influential literary figures of his age'；古典学家——'Carduccis enthusiasm for the classical in art led him to adapt Latin prosody to Italian verse'；青年时领导反浪漫主义、回归古典的团体；1860年任博洛尼亚意大利文学教授；1890终身参议员；'Inno a Satana'（撒旦颂, 1863）——共和反教权情绪；Giambi ed epodi (1867-69)——'violent, bitter language'；Odi barbare (1877; 野蛮颂)——仿贺拉斯与维吉尔格律，追忆罗马荣光与古典异教幸福；Rime nuove (1887)——与《野蛮颂》'contain the best of Carduccis poetry'，含 Maremma 风景、童年回忆、'the lament for the loss of his only son'"},
{"id":"B346","title":"Carl Sandburg — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Carl-Sandburg","type":"百科全书","verified":True,"covers":["sandburg","zhijiage"],"note":"2026-11-21 核对：1878-01-06伊利诺伊州Galesburg生—1967-07-22北卡州Flat Rock卒（89岁）；Chicago Poems 组诗1914年刊于 Poetry 杂志、1916年成书；'Chicago'——'Hog Butcher, Tool Maker, Stacker of Wheat, Player with Railroads and Freight Handler to the Nation'；The People, Yes (1936)——大萧条中——'a poetic testament to the power of the people to go forward'；Abraham Lincoln: The Prairie Years 两卷 (1926)——通俗传记；Abraham Lincoln: The War Years 四卷 (1939)——1940年普利策历史奖；另有1959年格莱美奖；引文 'Pittsburgh, Youngstown, Gary, they make their steel with men'（Smoke and Steel, 1920）；Rootabaga Stories (1922) 等儿童书；The American Songbag (1927)"},
{"id":"B347","title":"John Dos Passos — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/John-Dos-Passos","type":"百科全书","verified":True,"covers":["dospassos","meiguobuqu"],"note":"2026-11-21 核对：1896-01-14芝加哥生—1970-09-28巴尔的摩卒（74岁）；哈佛1916；一战救护车志愿司机；U.S.A. 三部曲——The 42nd Parallel (1930, 至战前)、1919 (1932, 战争与凡尔赛)、The Big Money (1936, 1920年代繁荣至1930年代崩溃)——'the portrait of these two nations'（富者与贫者的两个美国）；1927年萨柯-万泽蒂处决后定型其'两个国家'观；Manhattan Transfer (1925)——'a rapid-transit riders view of the metropolis'，十余人印象派闪现；技巧：'Newsreels'（真报纸标题+流行歌曲蒙太奇）与'camera-eye'（'brief, poetic, personal reminiscences'）；插入传记：福特/爱迪生/威尔逊/摩根/德布斯/凡勃伦/乔·希尔/无名战士；Three Soldiers (1921)反战；后转保守，卒时'his books scarcely received critical attention'"},
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
    return got[0] if got else None

def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

rel_card = [rid(find_work('horace', []), 'xuboliweng'), rid('xuboliweng'), rid('diyuzhiji')]
rel_sand = [rid(find_work('whitman', []), 'xueseziwuxian'), rid(find_work('hughes', []), 'tuyuzhizideneizi'), rid('tuyuzhizideneizi')]
rel_usa = [rid('zhijiage'), rid('xueseziwuxian'), rid(find_work('hemingway', []), 'yongbieliao')]
rel_mt = [rid('meiguobuqu'), rid('zhijiage'), rid('tuyuzhizideneizi')]
rel_sand = list(dict.fromkeys(rel_sand))[:3]; rel_usa = list(dict.fromkeys(rel_usa))[:3]; rel_mt = list(dict.fromkeys(rel_mt))[:3]
print('rel:', rel_card, rel_sand, rel_usa, rel_mt)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"carducci","name":"焦苏埃·卡尔杜齐","foreign_name":"Giosuè Carducci（焦苏埃·卡尔杜齐，1835-07-27—1907-02-16）","country":"意大利","birth":1835,"death":1907,"birth_year":1835,"death_year":1907,"era":"近代",
"summary":"卡尔杜齐，托斯卡纳Val di Castello生，意大利诗人——1906年诺贝尔文学奖；'one of the most influential literary figures of his age'（其时代最有影响的文学人物之一——B345）。古典学家：'Carduccis enthusiasm for the classical in art led him to adapt Latin prosody to Italian verse'（把拉丁格律移植入意语诗——B345）；青年时领导推翻浪漫主义、回归古典的团体（B345）。'Inno a Satana'（撒旦颂, 1863）显其共和反教权情绪（B345）；Odi barbare（野蛮颂, 1877）仿贺拉斯与维吉尔格律，追忆罗马荣光与古典异教幸福（B345）；与 Rime nuove（新韵, 1887）'contain the best of Carduccis poetry'（B345）。1860年任博洛尼亚意大利文学教授、1890年终身参议员（B345）。",
"timeline":[
 {"year":1835,"text":"7月27日生于托斯卡纳Val di Castello（B345）。","src":"B345"},
 {"year":1860,"text":"任博洛尼亚大学意大利文学教授（B345）。","src":"B345"},
 {"year":1863,"text":"'Inno a Satana'（撒旦颂）——共和反教权（B345）。","src":"B345"},
 {"year":1877,"text":"Odi barbare（野蛮颂）——拉丁格律的意语移植（B345）。","src":"B345"},
 {"year":1906,"text":"获诺贝尔文学奖（B345）。","src":"B345"},
 {"year":1907,"text":"2月16日卒于博洛尼亚（B345）。","src":"B345"}],
"major_works":[
 {"work_id":"yemanli","note":"1877（B345）"},
 {"title":"新韵","note":"（B345：Rime nuove (1887)——中译名待核）"},
 {"title":"撒旦颂","note":"（B345：Inno a Satana, 1863）"}],
"style":["拉丁格律的意大利移植（B345）。",
 "共和反教权的政治抒情（B345：'Inno a Satana'）。",
 "'violent, bitter language'的政治讽刺（B345：Giambi ed epodi）。"],
"status":"Britannica 定位卡尔杜齐为其时代最有影响的意大利文学人物、1906年诺奖得主（B345）。",
"sources":["B345"],"dates_source":"B345",
"pending":["Odi barbare 通行中译名（《野蛮颂》）待核。","'独子之殇'细节（B345：the lament for the loss of his only son）待核。","1906诺奖授奖理由细节待核。"]},
{"id":"sandburg","name":"卡尔·桑德堡","foreign_name":"Carl Sandburg（卡尔·桑德堡，1878-01-06—1967-07-22）","country":"美国","birth":1878,"death":1967,"birth_year":1878,"death_year":1967,"era":"现当代",
"summary":"桑德堡，伊利诺伊州Galesburg生，美国诗人、林肯传记作者——Chicago Poems 组诗1914年刊于 Poetry、1916年成书（B346）。'Chicago'——'Hog Butcher, Tool Maker, Stacker of Wheat, Player with Railroads and Freight Handler to the Nation'（屠夫、工具匠、麦垛工、铁路玩家、全国的货运员——B346）。The People, Yes (1936)——大萧条中——'a poetic testament to the power of the people to go forward'（B346）。Abraham Lincoln: The Prairie Years 两卷 (1926)、The War Years 四卷 (1939)——后者获1940年普利策历史奖（B346）。引文：'Pittsburgh, Youngstown, Gary, they make their steel with men'（Smoke and Steel, 1920——B346）。",
"timeline":[
 {"year":1878,"text":"1月6日生于伊利诺伊州Galesburg（B346）。","src":"B346"},
 {"year":1916,"text":"Chicago Poems 成书（1914年组诗刊于Poetry杂志——B346）。","src":"B346"},
 {"year":1926,"text":"Lincoln: The Prairie Years 两卷（B346）。","src":"B346"},
 {"year":1940,"text":"Lincoln: The War Years 获普利策历史奖（B346）。","src":"B346"},
 {"year":1967,"text":"7月22日卒于北卡州Flat Rock（B346）。","src":"B346"}],
"major_works":[
 {"work_id":"zhijiage","note":"1916（B346）"},
 {"title":"钢与烟","note":"（B346：Smoke and Steel (1920)——中译名待核）"},
 {"title":"人民，是的","note":"（B346：The People, Yes (1936)）"}],
"style":["城市工业意象：屠夫/工具匠/麦垛（B346）。",
 "'人民'的史诗声音（B346：The People, Yes）。",
 "民歌收集者（B346：The American Songbag (1927)）。"],
"status":"Britannica 定位桑德堡为芝加哥诗歌的代表、普利策历史奖得主（B346）。",
"sources":["B346"],"dates_source":"B346",
"pending":["'Chicago'全诗通行译文待核。","Corn Huskers (1918) 未见于 B346—— Pulitzer 诗歌奖说待核。","1959格莱美奖详情待核。"]},
{"id":"dospassos","name":"约翰·多斯·帕索斯","foreign_name":"John Dos Passos（约翰·多斯·帕索斯，1896-01-14—1970-09-28）","country":"美国","birth":1896,"death":1970,"birth_year":1896,"death_year":1970,"era":"现当代",
"summary":"多斯·帕索斯，芝加哥生，美国小说家——哈佛1916、一战救护车志愿司机（B347）。U.S.A. 三部曲（The 42nd Parallel, 1930；1919, 1932；The Big Money, 1936）——'the portrait of these two nations'（富者与贫者'两个国家'的肖像——B347）；其'两个国家'观在1927年萨柯-万泽蒂处决后定型（B347）。Manhattan Transfer（曼哈顿中转站, 1925）——'a rapid-transit riders view of the metropolis'（B347）。技巧：'Newsreels'（真报纸标题与流行歌曲蒙太奇）与'camera-eye'（'brief, poetic, personal reminiscences'）；插入福特/爱迪生/威尔逊/摩根/德布斯/凡勃伦/乔·希尔/无名战士的传记（B347）。",
"timeline":[
 {"year":1896,"text":"1月14日生于芝加哥（B347）。","src":"B347"},
 {"year":1921,"text":"Three Soldiers——反战小说（B347）。","src":"B347"},
 {"year":1925,"text":"Manhattan Transfer（曼哈顿中转站）（B347）。","src":"B347"},
 {"year":1936,"text":"U.S.A. 三部曲完成（The Big Money）（B347）。","src":"B347"},
 {"year":1970,"text":"9月28日卒于巴尔的摩；'his books scarcely received critical attention'（B347）。","src":"B347"}],
"major_works":[
 {"work_id":"meiguobuqu","note":"U.S.A. 1930-36（B347）"},
 {"work_id":"manhadundian","note":"1925（B347）"},
 {"title":"三个士兵","note":"（B347：Three Soldiers (1921)——反战）"}],
"style":["'Newsreel'蒙太奇：报纸标题+流行歌曲（B347）。",
 "'Camera-eye'：诗性个人回忆流（B347）。",
 "插入名人传记的拼贴结构（B347）。"],
"status":"Britannica 定位多斯·帕索斯为'两个美国'的编年史家（B347）。",
"sources":["B347"],"dates_source":"B347",
"pending":["U.S.A. 通行译名（《美国》三部曲）待核。","camera-eye 通行译名（'摄影机眼'）待核。","后期转保守的细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"yemanli","title":"野蛮颂","original_title":"Odi barbare","region":"意大利","era":"近代","era_detail":"19世纪70年代",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"carducci","author_name":"焦苏埃·卡尔杜齐",
"year_display":"1877年（Britannica B345：Odi barbare (1877)——仿贺拉斯与维吉尔格律）","year_sort":1877,
"background":["Britannica（B345）：Odi barbare——'written in metres imitative of Horace and Virgil'（以仿贺拉斯、维吉尔的格律写成）——'recalling Roman glory and classical pagan happiness'（追忆罗马荣光与古典异教幸福）。","Britannica（B345）：与 Rime nuove (1887) 一起'contain the best of Carduccis poetry'（卡杜齐诗歌之最佳）。","Britannica（B345）：诗人——'enthusiasm for the classical in art led him to adapt Latin prosody to Italian verse'。"],
"outline":["古典格律的意大利移植：萨福体/阿尔凯奥斯体等（格律细节通说待核——B345未载具体诗目）。","罗马荣光与异教幸福的挽歌化（B345：Roman glory and classical pagan happiness）。","'独子之殇'的哀歌（B345：the lament for the loss of his only son——篇目归属通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"古典主义者","note":"（B345 语境）"}],
"themes":["古典格律的现代移植（B345）。","反浪漫主义的诗学宣言（B345：青年时领导回归古典的团体）。","罗马与异教的荣光（B345）。"],
"influence":[{"text":"Britannica：1906年诺贝尔文学奖（B345）。","source":"B345"},{"text":"Britannica：'one of the most influential literary figures of his age'（B345）。","source":"B345"}],
"reading":{"difficulties":["古典格律（萨福体等）。","意大利统一时代的政治语境（共和反教权——B345）。"],
 "editions":["《野蛮颂》中译本（人民文学/译林等——通说待核）。","意大利文原版。"],
 "order":"卡杜齐首选；后接《新韵》(1887)。"},
"pending":["具体篇目与格律名核对（B345未载）。","'独子'哀歌篇目归属待核。","中译名两说（《野蛮颂》/《野蛮的诗》）待核。"],
"sources":["B345"],"year_source":"B345","author_source":"B345","related_works":rel_card,
"svg":G("《野蛮颂》古典移植图",[{"title":"拉丁格律","text":"移植入意语（B345）","color":"gold"},{"title":"罗马","text":"荣光与异教幸福（B345）","color":"main"},{"title":"反浪漫主义","text":"回归古典（B345）","color":"antagonist"},{"title":"哀歌","text":"独子之殇（B345）","color":"family"}])},
{"id":"zhijiage","title":"芝加哥诗集","original_title":"Chicago Poems","region":"美国","era":"现当代","era_detail":"20世纪10年代",
"genre":"诗集","genre_group":"诗歌","language":"英语","author_id":"sandburg","author_name":"卡尔·桑德堡",
"year_display":"1916年（Britannica B346：Chicago Poems——1914年组诗刊于Poetry杂志、1916年成书）","year_sort":1916,
"background":["Britannica（B346）：'Chicago'——'Hog Butcher, Tool Maker, Stacker of Wheat, Player with Railroads and Freight Handler to the Nation'——城市即工人、机器与肉。","Britannica（B346）：桑德堡的大萧条诗集 The People, Yes (1936)——'a poetic testament to the power of the people to go forward'。","Britannica（B346）：引文——'Pittsburgh, Youngstown, Gary, they make their steel with men'（Smoke and Steel, 1920——钢是用人炼的）。"],
"outline":["'芝加哥'：城市的自我命名与辩护（B346：五重头衔——诗中通说待核细节）。","工人、钢铁与'人民'的抒情（B346 语系）。"],
"characters":[{"name":"芝加哥","identity":"被拟人化的城市","note":"（B346：'Chicago'一诗）"},{"name":"'人民'","identity":"集体主角","note":"（B346：The People, Yes 语系）"}],
"themes":["工业城市的自我辩护（B346：'Chicago'）。",
 "'人民'的史诗（B346：The People, Yes——'the power of the people to go forward'）。",
 "以人炼钢（B346：'they make their steel with men'）。"],
"influence":[{"text":"Britannica：芝加哥诗歌传统的命名之作（B346 定位）。","source":"B346"},{"text":"Britannica：Lincoln: The War Years 获1940普利策历史奖（B346）。","source":"B346"}],
"reading":{"difficulties":["自由体的工业节奏。","芝加哥屠宰场与铁路史。"],
 "editions":["《芝加哥诗集》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"桑德堡首选；后接《钢与烟》《人民，是的》。"},
"pending":["'Chicago'全诗引文核对（五重头衔原文B346已载）。","1914年 Poetry 杂志首发期数待核。","与惠特曼传统的比较说法待核。"],
"sources":["B346"],"year_source":"B346","author_source":"B346","related_works":rel_sand,
"svg":G("《芝加哥诗集》城市图",[{"title":"芝加哥","text":"五重头衔的城（B346）","color":"main"},{"title":"工人","text":"'以人炼钢'（B346）","color":"gold"},{"title":"人民","text":"向前的力量（B346）","color":"family"},{"title":"机器","text":"铁路与屠宰场","color":"antagonist"}])},
{"id":"meiguobuqu","title":"美国","original_title":"U.S.A.","region":"美国","era":"现当代","era_detail":"20世纪30年代",
"genre":"长篇小说（三部曲）","genre_group":"小说","language":"英语","author_id":"dospassos","author_name":"约翰·多斯·帕索斯",
"year_display":"1930-36年（Britannica B347：U.S.A. 三部曲——The 42nd Parallel (1930)、1919 (1932)、The Big Money (1936)）","year_sort":1930,
"background":["Britannica（B347）：三部曲——'the portrait of these two nations'（'两个国家'的肖像：富者/特权者与贫者/无权者）。","Britannica（B347）：其'两个国家'观在1927年萨柯-万泽蒂处决后定型。","Britannica（B347）：技巧——'Newsreels'（真报纸标题+流行歌曲蒙太奇）、'camera-eye'（'brief, poetic, personal reminiscences'）与名人传记插入（福特/爱迪生/威尔逊/摩根/德布斯/凡勃伦/乔·希尔/无名战士）。"],
"outline":["《北纬42度》：1900至战前——'两种国家'的萌芽（B347：covering 1900 up to the war）。","《1919》：战争与凡尔赛；《大钱》：1920年代繁荣至1930年代崩溃（B347）。","新闻片、摄影机眼与传记的拼贴（B347）。"],
"characters":[{"name":"群像（十余人）","identity":"交替视点","note":"（B347：多人物结构——人名通说待核）"},{"name":"无名战士","identity":"插入传记之一","note":"（B347：the Unknown Soldier）"}],
"themes":["'两个国家'：富与贫（B347）。",
 "蒙太奇拼贴的史诗（B347：Newsreels/camera-eye）。",
 "萨柯-万泽蒂事件的政治创伤（B347：1927年处决）。"],
"influence":[{"text":"Britannica：'the portrait of these two nations'（B347）。","source":"B347"},{"text":"Britannica：现代主义叙事技术的集大成（B347：技巧清单）。","source":"B347"}],
"reading":{"difficulties":["拼贴结构与多人物。","1900-1930美国史。"],
 "editions":["《美国》三部曲中译本（人民文学/上海译文等——通说待核）。","英文原版。"],
 "order":"多斯·帕索斯首选；可先读《曼哈顿中转站》。"},
"pending":["三部曲中文名（《北纬42度》/《一九一九》/《赚大钱》——通说待核）。","'摄影机眼'译名待核。","人物名（麦克/珍妮等）核对（B347未载）。"],
"sources":["B347"],"year_source":"B347","author_source":"B347","related_works":rel_usa,
"svg":G("U.S.A. 拼贴结构图",[{"title":"新闻片","text":"报纸+歌曲蒙太奇（B347）","color":"gold"},{"title":"摄影机眼","text":"诗性回忆流（B347）","color":"main"},{"title":"两个国家","text":"富与贫的肖像（B347）","color":"antagonist"},{"title":"传记","text":"福特/德布斯/无名战士（B347）","color":"family"}])},
{"id":"manhadundian","title":"曼哈顿中转站","original_title":"Manhattan Transfer","region":"美国","era":"现当代","era_detail":"20世纪20年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"dospassos","author_name":"约翰·多斯·帕索斯",
"year_display":"1925年（Britannica B347：Manhattan Transfer (1925)）","year_sort":1925,
"background":["Britannica（B347）：Manhattan Transfer——'a rapid-transit riders view of the metropolis'（一个高速列车乘客眼中的大都会）。","Britannica（B347）：在十余人之间以'印象派闪现'的方式移动（shifting among more than a dozen characters in impressionistic flashes）。","与 U.S.A. 的关系：本作为其城市实验，三部曲为全国编年（B347 语境）。"],
"outline":["曼哈顿的'高速列车视角'：十余人印象派闪现（B347）。","城市即主角：从移民到摩天楼（情节通说待核）。"],
"characters":[{"name":"群像（十余人）","identity":"交替视点","note":"（B347：more than a dozen characters——人名通说待核）"}],
"themes":["大都会的机械化速度（B347：rapid-transit view）。",
 "印象派的城市蒙太奇（B347：impressionistic flashes）。",
 "通往 U.S.A. 的技术预演（B347 语境）。"],
"influence":[{"text":"Britannica：'a rapid-transit riders view of the metropolis'（B347）。","source":"B347"},{"text":"Britannica：乔伊斯式多线叙事的美国化（通说待核）。","source":"B347"}],
"reading":{"difficulties":["多线拼贴（无单一主角）。","1920年代纽约都市史。"],
 "editions":["《曼哈顿中转站》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"读 U.S.A. 前的技术热身。"},
"pending":["人物名核对（B347未载）。","1925年出版（Harper说）待核。","书名直译（'曼哈顿换乘站'）待核。"],
"sources":["B347"],"year_source":"B347","author_source":"B347","related_works":rel_mt,
"svg":G("《曼哈顿中转站》速度结构图",[{"title":"高速列车","text":"都会的视角（B347）","color":"main"},{"title":"十余人","text":"印象派闪现（B347）","color":"family"},{"title":"曼哈顿","text":"城市即主角（通说）","color":"antagonist"},{"title":"U.S.A.","text":"技术的预演（B347语境）","color":"gold"}])},
]
for w in works:
    assert w['id'] not in existing, f'dup {w["id"]}'
for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("carducci","yemanli"),("sandburg","zhijiage"),("dospassos","meiguobuqu"),("dospassos","manhadundian")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B34x/B35x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH27 DONE')
