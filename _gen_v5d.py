# -*- coding: utf-8 -*-
"""v5批4：20世纪补强 8部+8作家页+8来源"""
import json, pathlib

new_src = [
{"id":"B244","title":"Juan Rulfo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Juan-Rulfo","type":"百科全书","verified":True,"covers":["rulfo","peideluobalamo"],"note":"2026-11-20 核对：1917年5月16日生（Apulco?——页面对出生地存疑）—1986-01-07墨西哥城；仅出版约两本书即被视为20世纪拉美最优秀小说家之一；'Pedro Páramo (1955)……examines the physical and moral disintegration of a laconic cacique'；'a mythical hell on earth inhabited by the dead'；'enormous impact on those Latin American authors, including Gabriel García Márquez'"},
{"id":"B245","title":"Alice Walker — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Alice-Walker","type":"百科全书","verified":True,"covers":["walker","zise"],"note":"2026-11-20 核对：1944-02-09佐治亚州伊顿顿生；'the first Black woman to win the Pulitzer Prize for fiction with The Color Purple (1982)'；书信体小说，写1909—1947佐治亚农村黑人女性的成长与自我实现；'The book won a Pulitzer Prize and was adapted into a film by Steven Spielberg in 1985'；争议句：'some African American men strongly objected to the perceived negative portrayal of Black men'"},
{"id":"B246","title":"Alice Munro — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Alice-Munro","type":"百科全书","verified":True,"covers":["munro","taoli"],"note":"2026-11-20 核对：1931-07-10安大略温厄姆—2024-05-13；'the first Canadian to be named the Nobel literature laureate'（2013）；'dubbed her a master of the contemporary short story'；'In Runaway (2004) Munro explores the depths of ordinary lives through the use of temporal shifts'；2009布克国际奖"},
{"id":"B247","title":"Wole Soyinka — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Wole-Soyinka","type":"百科全书","verified":True,"covers":["soyinka","siwangyu guowangdemafu"],"note":"2026-11-20 核对：1934-07-13尼日利亚阿贝奥库塔生；'the first Black African to be awarded the prize'（1986诺贝尔奖）；授奖词'vivid, often harrowing'、'marked by an evocative, poetically intensified diction'；《死亡与国王的马夫》1975；1967—69因比夫拉战争言论入狱并在狱中写《狱中诗》"},
{"id":"B248","title":"W. Somerset Maugham — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/W-Somerset-Maugham","type":"百科全书","verified":True,"covers":["maugham","yueliangyuliupian"],"note":"2026-11-20 核对：1874-01-25巴黎生—1965-12-16尼斯卒（'December 16?'——部分传记作15日）；'Maugham's reputation as a novelist rests primarily on four books'；《月亮与六便士》(1919)——'an account of an unconventional artist, suggested by the life of Paul Gauguin'；《人性的枷锁》(1915)半自传"},
{"id":"C029","title":"《金庸，带着武侠梦远去了》（人民日报海外版）","author":"人民日报海外版","year":"2018-11-13","url":"http://paper.people.com.cn/rmrbhwb/html/2018-11/13/content_1892302.htm","type":"官方媒体","verified":True,"covers":["jinjiong","shediao"],"note":"2026-11-20 核对：金庸（查良镛）10月30日逝世、11月12日香港殡仪馆丧礼；'九十四春秋永流芳'挽联（享年94岁）；'他创作15部脍炙人口的小说，最终成为绝响'；'赤子丹心，侠肝义胆'；金庸自述'引申出去就是侠之大者，为国为民'；影视改编约100部；'飞雪连天射白鹿，笑书神侠倚碧鸳'为14部书名首字对联；《射雕英雄传》《神雕侠侣》《天龙八部》《鹿鼎记》等作品名；'知名报人、社会活动家'"},
{"id":"C030","title":"泛文学及其当代接受问题——重勘阿城《棋王》（中国作家网）","author":"中国作家网","year":"2024-10-07","url":"http://www.chinawriter.com.cn/n1/2024/1007/c404030-40333835.html","type":"官方文学机构","verified":True,"covers":["acheng","qiwan"],"note":"2026-11-20 核对：'1984年第7期《上海文学》所发表的初版本《棋王》'；发表后'在文化热和迅速迭代更新的文学浪潮中被逐渐经典化'，'作为寻根文学的代表作之一进入到文学史叙述之中'；曾被《北京文学》以写了知青生活的阴暗面为由退稿；王一生'俗世奇人'、下盲棋以一敌九车轮大战；'不做俗人，哪儿会知道这般乐趣'、'衣食是本'；母亲用捡来的牙刷把磨成五子棋；阿城自述语言样貌无非是话本变奏，细节暗取《老残游记》《儒林外史》；生于文化宣传干部之家，青年辗转晋蒙滇，1986年赴美；自称'不是一个职业作家，是个专业作家'"},
{"id":"C031","title":"重读《官场现形记》：未完成的晚清官场百科全书（中国作家网转载《名作欣赏》）","author":"中国作家网","year":"2020-12-08","url":"https://www.chinawriter.com.cn/n1/2020/1208/c419384-31959116.html","type":"官方文学机构","verified":True,"covers":["liboyuan","guanchangxianxingji"],"note":"2026-11-20 核对：'李伯元（1867—1906），字宝嘉，别号南亭亭长。江苏武进人'，40岁去世；1897年赴上海创办《指南报》后改办《游戏报》；'1903—1905年，《官场现形记》六十回开始连载发表于《世界繁华报》'，初版本两卷各30回；鲁迅评'辞气浮露，笔无藏锋……故别谓之谴责小说'；胡适评与吴敬梓对比；慈禧索问轶事（顾颉刚引）；陶子尧购机器、剿匪虚报、黄河救灾肥缺、十二姨太打蚊子等情节举要"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new_src:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
raw = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for s in raw:
    seen[s["id"]] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources:", len(out))

# ---------- authors ----------
authors = {
"maugham": {
  "id": "maugham", "name": "威廉·萨默塞特·毛姆", "foreign_name": "W. Somerset Maugham（威廉·萨默塞特·毛姆，1874-01-25—1965-12-16）",
  "country": "英国", "birth": 1874, "death": 1965, "birth_year": 1874, "death_year": 1965, "era": "现当代",
  "summary": "毛姆，生于巴黎的英国小说家、剧作家与短篇小说家（Britannica），以平实清晰的白描、世界主义的场景与对人性的敏锐洞察著称（Britannica 语境：plain, clear prose, cosmopolitan settings, and sharp insight into human nature）。'Maugham's reputation as a novelist rests primarily on four books'（小说家声誉主要建立在四部书上——Britannica）：《人性的枷锁》（1915）、《月亮与六便士》（1919）等。1908年四部剧同时在伦敦上演（Britannica：four plays running in London at once）。",
  "timeline": [
    {"year": 1874, "text": "1月25日生于巴黎（Britannica：Born January 25, 1874, Paris）。", "src": "B248"},
    {"year": 1908, "text": "四部剧同时在伦敦上演（Britannica：four plays running in London at once）。", "src": "B248"},
    {"year": 1915, "text": "《人性的枷锁》出版（Britannica：Of Human Bondage (1915)）。", "src": "B248"},
    {"year": 1919, "text": "《月亮与六便士》出版（Britannica：The Moon and Sixpence (1919)）。", "src": "B248"},
    {"year": 1965, "text": "12月16日卒于尼斯（Britannica：Died December 16?, 1965, Nice；部分传记作15日）。", "src": "B248"}],
  "major_works": [
    {"work_id": "yueliangyuliupian", "note": "长篇（Britannica：1919）"},
    {"title": "人性的枷锁", "note": "（Britannica：1915 半自传）"},
    {"title": "刀锋、短篇集", "note": "（通说待核）"}],
  "style": [
    "白描的冷静叙事（Britannica：plain, clear prose）。",
    "世界主义场景与人性洞察（Britannica 语境）。",
    "以真实画家（高更）为原型的艺术家小说（Britannica：suggested by the life of Paul Gauguin）。"],
  "status": "Britannica 定位毛姆为英国小说家剧作家短篇家，小说声誉建于四部书（含《月亮与六便士》《人性的枷锁》）；'最会说故事的人'之誉（通说待核）。",
  "sources": ["B248"], "dates_source": "B248",
  "pending": ["卒年12月15/16日分歧（Britannica 已载?）核对。", "《刀锋》1944年待核。", "'最会说故事的人'评语出处待核。"]
},
"jinjiong": {
  "id": "jinjiong", "name": "金庸", "foreign_name": "Jin Yong（金庸，本名查良镛，1924—2018）",
  "country": "中国", "birth": 1924, "death": 2018, "birth_year": 1924, "death_year": 2018, "era": "现当代",
  "summary": "金庸，本名查良镛（人民日报海外版 C029：著名作家查良镛，笔名金庸），'知名报人、社会活动家'（C029）。2018年10月30日逝世，丧礼挽联'九十四春秋永流芳'（C029——享年94岁，1924年生为由此及通说互证）。'他创作15部脍炙人口的小说，最终成为绝响'（C029）；'飞雪连天射白鹿，笑书神侠倚碧鸳'为其中14部书名首字对联（C029）；'由其小说改编的影视作品约100部'（C029）。金庸自述侠义观：'引申出去就是侠之大者，为国为民'（C029）；被赞'赤子丹心，侠肝义胆'（C029）。",
  "timeline": [
    {"year": 1924, "text": "生于浙江海宁（1924年3月10日说——由享年94与C029互证，海宁籍贯通说待核）。", "src": "C029"},
    {"year": 1955, "text": "《书剑恩仇录》开始武侠创作（1955年说——通说待核；C029 载作品名）。", "src": "C029"},
    {"year": 1958, "text": "《射雕英雄传》连载（1957—1959说——通说待核；C029 载作品名）。", "src": "C029"},
    {"year": 2018, "text": "10月30日逝世，享年94岁（人民日报海外版 C029）。", "src": "C029"}],
  "major_works": [
    {"work_id": "shediao", "note": "长篇（C029 载作品名）"},
    {"title": "射雕三部曲（神雕侠侣/倚天屠龙记）", "note": "（C029 载神雕侠侣）"},
    {"title": "天龙八部、鹿鼎记", "note": "（C029 载作品名）"}],
  "style": [
    "'侠之大者，为国为民'：金庸自述的侠义观（C029）。",
    "以历史为背景的武侠长卷：15部小说构成'金庸宇宙'（C029：15部脍炙人口的小说）。",
    "章回白话与 modern 叙事的融合（通说待核）。"],
  "status": "'创作15部脍炙人口的小说'（人民日报海外版 C029）；华人世界最畅销作家之一、影视改编约100部（C029）；'有华人处有金庸'之誉（通说待核）。",
  "sources": ["C029"], "dates_source": "C029",
  "pending": ["生年1924年3月10日与浙江海宁籍贯核对。", "《明报》创办人经历（1959年说）待核。", "《射雕英雄传》连载报刊与日期待核。"]
},
"rulfo": {
  "id": "rulfo", "name": "胡安·鲁尔福", "foreign_name": "Juan Rulfo（胡安·鲁尔福，1917—1986）",
  "country": "墨西哥", "birth": 1917, "death": 1986, "birth_year": 1917, "death_year": 1986, "era": "现当代",
  "summary": "鲁尔福，墨西哥作家——'regarded as one of the finest novelists and short-story writers in 20th-century Latin America despite publishing essentially only two books'（仅出版约两本书即被视为20世纪拉美最优秀的小说家与短篇家之一——Britannica）。其小说汲取墨西哥乡村的暴力经验、影响魔幻现实主义运动（Britannica）。《佩德罗·巴拉莫》（1955）：'examines the physical and moral disintegration of a laconic cacique'，'set in a mythical hell on earth inhabited by the dead'（B244）。'He had an enormous impact on those Latin American authors, including Gabriel García Márquez'（B244）。",
  "timeline": [
    {"year": 1917, "text": "5月16日生于墨西哥（Britannica：Born May 16, 1917 (Apulco?, Mexico)——出生地该页存疑）。", "src": "B244"},
    {"year": 1955, "text": "《佩德罗·巴拉莫》出版（Britannica：1955）。", "src": "B244"},
    {"year": 1986, "text": "1月7日卒于墨西哥城（Britannica：died January 7, 1986, Mexico City）。", "src": "B244"}],
  "major_works": [
    {"work_id": "peideluobalamo", "note": "中长篇（Britannica：1955）"},
    {"title": "燃烧的原野", "note": "短篇集（通说待核）"}],
  "style": [
    "乡村暴力的诗意回声（Britannica：Mexico's rural violence）。",
    "生死一体的'科马拉'：亡灵的地理（Britannica：mythical hell on earth inhabited by the dead）。",
    "沉默的卡西克：权力与其败坏（Britannica：physical and moral disintegration of a laconic cacique）。"],
  "status": "Britannica 定位鲁尔福为拉美20世纪最优秀小说家之一（两书立身）；'enormous impact'于马尔克斯等魔幻现实主义作家（B244）。",
  "sources": ["B244"], "dates_source": "B244",
  "pending": ["出生地（Apulco?）与圣加布里埃尔镇说核对。", "《燃烧的原野》（El Llano en llamas，1953）待核。", "科马拉村名与'巴拉莫'词义（parámo）考订待核。"]
},
"walker": {
  "id": "walker", "name": "艾丽斯·沃克", "foreign_name": "Alice Walker（艾丽斯·沃克，1944-02-09— ）",
  "country": "美国", "birth": 1944, "death": None, "birth_year": 1944, "death_year": None, "era": "现当代",
  "summary": "沃克，佐治亚州伊顿顿人，美国作家——其小说、诗与随笔探索非裔美国文化尤其是女性生活（Britannica）；'she became the first Black woman to win the Pulitzer Prize for fiction'（凭《紫色》（1982）成为首位获小说类普利策奖的黑人女性——Britannica）。书信体小说写1909—1947年佐治亚农村黑人女性的成长与自我实现；'The book won a Pulitzer Prize and was adapted into a film by Steven Spielberg in 1985'（B245）。争议：'some African American men strongly objected to the perceived negative portrayal of Black men'（B245）。",
  "timeline": [
    {"year": 1944, "text": "2月9日生于佐治亚州伊顿顿（Britannica：Born February 9, 1944, Eatonton, Georgia）。", "src": "B245"},
    {"year": 1982, "text": "《紫色》出版（Britannica：The Color Purple (1982)）。", "src": "B245"},
    {"year": 1983, "text": "获普利策小说奖与美国国家图书奖（Britannica：Pulitzer and National Book Awards (1983)）。", "src": "B245"},
    {"year": 1985, "text": "斯皮尔伯格改编电影（Britannica：adapted into a film by Steven Spielberg in 1985）。", "src": "B245"}],
  "major_works": [
    {"work_id": "zise", "note": "长篇（Britannica：1982）"},
    {"title": "梅里迪安、拥有快乐的秘密", "note": "（Britannica 存目）"},
    {"title": " search of our mothers' gardens", "note": "文集（通说待核）"}],
  "style": [
    "书信体与黑人英语方言（Britannica：Black English Vernacular 语境）。",
   "'妇女主义'（womanism）概念的提出者（Britannica：womanist criticism 语境）。",
   " Celie 的上帝观转变（Britannica：Celie's changing views of God）。"],
  "status": "Britannica 定位沃克为首位获普利策小说奖的黑人女性（B245）；《紫色》对黑人男性形象描写的争议与作者的回应均有记载（B245）。",
  "sources": ["B245"], "dates_source": "B245",
  "pending": ["womanist 概念出处（In Search of Our Mothers' Gardens，1983）核对。", "书名 mid-transcription（In Search of Our Mothers' Gardens）核对。", "音乐剧2004/2005与2023电影改编（Britannica 已载）核对。"]
},
"munro": {
  "id": "munro", "name": "艾丽丝·门罗", "foreign_name": "Alice Munro（艾丽丝·门罗，1931-07-10—2024-05-13）",
  "country": "加拿大", "birth": 1931, "death": 2024, "birth_year": 1931, "death_year": 2024, "era": "现当代",
  "summary": "门罗，安大略省温厄姆人，加拿大短篇小说家——以精准、抒情的笔触写普通人生活、尤其是安大略小镇的女性（Britannica）。2013年获诺贝尔文学奖：'dubbed her a master of the contemporary short story'（被誉为当代短篇大师——Britannica）；'the first Canadian to be named the Nobel literature laureate'（首位获诺贝尔文学奖的加拿大人——Britannica，贝娄1976除外）。'In Runaway (2004) Munro explores the depths of ordinary lives through the use of temporal shifts'（B246）。2024年5月13日去世（B246）。",
  "timeline": [
    {"year": 1931, "text": "7月10日生于安大略省温厄姆（Britannica：Born July 10, 1931, Wingham, Ontario）。", "src": "B246"},
    {"year": 1968, "text": "首部集《快乐阴影之舞》出版（Britannica：Dance of the Happy Shades (1968)）。", "src": "B246"},
    {"year": 2004, "text": "《逃离》出版（Britannica：Runaway (2004)）。", "src": "B246"},
    {"year": 2013, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 2013）。", "src": "B246"},
    {"year": 2024, "text": "5月13日卒于安大略（Britannica：Died May 13, 2024, Port Hope, Ontario）。", "src": "B246"}],
  "major_works": [
    {"work_id": "taoli", "note": "短篇集（Britannica：2004）"},
    {"title": "快乐阴影之舞、亲爱的生活", "note": "（Britannica 存目）"},
    {"title": "女孩和女人们的生活", "note": "（Britannica 存目）"}],
  "style": [
    "'当代短篇大师'（Britannica：master of the contemporary short story）。",
    "以时间跳跃探入普通生活的深处（Britannica：temporal shifts）。",
    "安大略西南小镇的社会文化肌理（Britannica：social and cultural environment of her native southwestern Ontario）。"],
  "status": "Britannica 定位门罗为2013年诺贝尔文学奖得主、首位加拿大获奖者（除1976年贝娄外）；其女2024年披露的家庭事件成为身后新闻（B246：daughter's revelation reported July 2024）。",
  "sources": ["B246"], "dates_source": "B246",
  "pending": ["《逃离》八个短篇篇名核对。", "'master of the contemporary short story'系瑞典学院授奖词（Britannica 已载）原文核对。", "女儿披露事件（2024年7月报道）与文学评价的关系待核。"]
},
"soyinka": {
  "id": "soyinka", "name": "沃莱·索因卡", "foreign_name": "Wole Soyinka（沃莱·索因卡，1934-07-13— ）",
  "country": "尼日利亚", "birth": 1934, "death": None, "birth_year": 1934, "death_year": None, "era": "现当代",
  "summary": "索因卡，尼日利亚阿贝奥库塔人，剧作家、诗人与政治活动家——'the first Black African winner of the Nobel Prize for Literature in 1986'（首位获诺贝尔文学奖的黑非洲作家——Britannica）；授奖词称其作品'vivid, often harrowing'、'marked by an evocative, poetically intensified diction'（B247）。戏剧融合西方技巧与约鲁巴民间传统（Britannica）。1967—69年因比夫拉战争言论入狱并在狱中写《狱中诗》（Britannica：jailed in 1967–69 for speaking out against the war）。",
  "timeline": [
    {"year": 1934, "text": "7月13日生于阿贝奥库塔（Britannica：Born July 13, 1934, Abeokuta, Nigeria）。", "src": "B247"},
    {"year": 1960, "text": "《森林之舞》上演（Britannica：A Dance of the Forests produced 1960）。", "src": "B247"},
    {"year": 1975, "text": "《死亡与国王的马夫》出版/上演（Britannica：Death and the King's Horseman (1975)）。", "src": "B247"},
    {"year": 1986, "text": "获诺贝尔文学奖（Britannica：Nobel Prize for Literature 1986）。", "src": "B247"}],
  "major_works": [
    {"work_id": "siwangyuguowangdemafu", "note": "悲剧（Britannica：1975）"},
    {"title": "森林之舞、疯人与专家", "note": "（Britannica 存目）"},
    {"title": "人死了（狱中记）", "note": "（Britannica：The Man Died 1972）"}],
  "style": [
    "约鲁巴神话与现代剧场的融合（Britannica：blend Western techniques with Yoruba folklore）。",
    "'evocative, poetically intensified diction'（Britannica 授奖词）。",
    "政治正义的终生行动（Britannica：decades of activism against political injustice）。"],
  "status": "Britannica 定位索因卡为首位黑非洲诺贝尔文学奖得主（1986）；《死亡与国王的马夫》为其代表作（B247）。",
  "sources": ["B247"], "dates_source": "B247",
  "pending": ["《死亡与国王的马夫》主题（约鲁巴自杀仪式/殖民干涉）细节待核。", "1965年奈保尔？——不：1965年电台事件待核。", "2021年《地球 happiest 人们的编年史》（Britannica 已载）核对。"]
},
"acheng": {
  "id": "acheng", "name": "阿城", "foreign_name": "A Cheng（阿城，本名锺阿城说——通说待核，1949— ）",
  "country": "中国", "birth": 1949, "death": None, "birth_year": 1949, "death_year": None, "era": "现当代",
  "summary": "阿城，作家（'生于文化宣传干部之家'——中国作家网 C030；其父电影理论家钟惦棐说——通说待核），青年时期辗转晋蒙滇（C030），1986年赴美、游历欧洲（C030），自称'不是一个职业作家，是个专业作家'（C030），被冠以'奇人、杂家、大仙、高士、侃爷'诸般形象、涉猎绘画影视厨艺木工等（C030）。中篇《棋王》1984年发表于《上海文学》第7期（C030），发表后'在文化热和迅速迭代更新的文学浪潮中被逐渐经典化'、'作为寻根文学的代表作之一进入到文学史叙述之中'（C030）。",
  "timeline": [
    {"year": 1949, "text": "生于北京（1949年说——通说待核）。", "src": "C030"},
    {"year": 1984, "text": "《棋王》刊于《上海文学》第7期（C030）。", "src": "C030"},
    {"year": 1986, "text": "赴美（C030）。", "src": "C030"},
    {"year": 2000, "text": "2000年后基本回国定居（C030：此后再无纯文学创作）。", "src": "C030"}],
  "major_works": [
    {"work_id": "qiwan", "note": "中篇（C030：1984《上海文学》）"},
    {"title": "树王、孩子王", "note": "（通说待核——三王）"},
    {"title": "闲话闲说、常识与通识", "note": "随笔（通说待核）"}],
  "style": [
    "'语言样貌无非是话本变奏'——阿城自述（C030）。",
    "细节'暗取《老残游记》和《儒林外史》'，意象取《史记》与张岱笔记（C030 转述）。",
   "'世俗'智慧的书写：'不做俗人，哪儿会知道这般乐趣'（C030）。"],
  "status": "《棋王》为寻根文学代表作之一（C030）；阿城为当代文人式写作的独特个案——'泛文学（艺）者'（C030 语境）。",
  "sources": ["C030"], "dates_source": "C030",
  "pending": ["本名锺阿城、1949年4月5日生、籍贯重庆江津说待核。", "《树王》《孩子王》发表年份待核。", "父亲钟惦棐身份待核。"]
},
"liboyuan": {
  "id": "liboyuan", "name": "李伯元", "foreign_name": "Li Boyuan（李伯元，字宝嘉，别号南亭亭长，1867—1906）",
  "country": "中国", "birth": 1867, "death": 1906, "birth_year": 1867, "death_year": 1906, "era": "近代",
  "summary": "李伯元（李宝嘉），'字宝嘉，别号南亭亭长。江苏武进人，生于同治六年，死于光绪三十二年，年仅40岁'（中国作家网 C031）。1897年30岁赴上海创办《指南报》、后改办《游戏报》（C031）。1903—1905年《官场现形记》六十回连载于《世界繁华报》（C031）——中国近代第一部在报刊上连载并引起轰动的长篇小说（综述口径待核），晚清四大谴责小说之首（通说待核）。",
  "timeline": [
    {"year": 1867, "text": "生于（同治六年——C031）。", "src": "C031"},
    {"year": 1897, "text": "赴上海创办《指南报》（C031）。", "src": "C031"},
    {"year": 1903, "text": "《官场现形记》开始在《世界繁华报》连载（1903—1905——C031）。", "src": "C031"},
    {"year": 1906, "text": "因劳累过度去世，年仅40岁（C031：'因劳累过度，40岁就去世了'）。", "src": "C031"}],
  "major_works": [
    {"work_id": "guanchangxianxingji", "note": "章回小说（C031：1903—1905连载）"},
    {"title": "文明小史、活地狱", "note": "（通说待核）"},
    {"title": "南亭四话", "note": "笔记（通说待核）"}],
  "style": [
    "'辞气浮露，笔无藏锋'——鲁迅对其谴责笔法的定评（C031 转引）。",
    "报纸连载的快节奏群像（C031：官场百科全书式）。",
    "'老骥伏枥，流莺比邻'的门前对联与办报生涯（C031）。"],
  "status": "晚清谴责小说代表作家（C031）；其《官场现形记》使'谴责小说'与《儒林外史》的讽刺传统区分开来（C031 转引鲁迅与胡适的对比）。",
  "sources": ["C031"], "dates_source": "C031",
  "pending": ["《世界繁华报》创办与连载始末核对。", "'四大谴责小说'说法出处待核。", "李宝嘉/李伯元名字写法辨析待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

# ---------- works ----------
def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"shediao": {
  "id":"shediao","title":"射雕英雄传","original_title":"射雕英雄传（长篇武侠小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"长篇武侠小说","genre_group":"小说","language":"汉语（白话·章回余韵）","author_id":"jinjiong","author_name":"金庸（查良镛）",
  "year_display":"1957—1959年连载（通说待核）；'他创作15部脍炙人口的小说'之一（人民日报海外版 C029）","year_sort":1958,
  "background":["人民日报海外版（C029）：金庸'创作15部脍炙人口的小说'；'飞雪连天射白鹿，笑书神侠倚碧鸳'为其中14部书名首字对联；'由其小说改编的影视作品约100部'。","金庸侠义观自述：'引申出去就是侠之大者，为国为民'（C029）。"],
  "outline":["郭靖：蒙古草原的傻小子成长为'为国为民'的大侠——华山论剑与襄阳危局（通说）。","黄蓉、东邪西毒南帝北丐中神通的江湖谱系（通说）。","《九阴真经》与武学伦理（通说）。"],
  "characters":[{"name":"郭靖","identity":"大侠","note":"笨拙的侠之大者（通说）"},{"name":"黄蓉","identity":"东邪之女","note":"机敏的女主角（通说）"},{"name":"洪七公","identity":"丐帮帮主","note":"北丐（通说）"},{"name":"欧阳锋","identity":"西毒","note":"反派（通说）"}],
  "themes":["侠之大者，为国为民（C029 金庸自述）。",
   "历史（宋金蒙）与虚构的缝合（通说）。",
   "成长叙事：武功即人格修炼（通说）。"],
  "influence":[{"text":"人民日报海外版：15部小说；影视改编约100部；'赤子丹心，侠肝义胆'（C029）。","source":"C029"},
   {"text":"新武侠文类的定型之作（通说待核）。","source":"C029"}],
  "reading":{"difficulties":["三部曲世系（射雕—神雕—倚天）。","历史年代（南宋）与武林地理。"],
   "editions":["《射雕英雄传》（广州出版社/三联书店版，通说待核）。"],
   "order":"先本作 →《神雕侠侣》→《倚天屠龙记》。"},
  "pending":["连载报刊（香港商报说）与日期核对。","人物武功名目核对。","金庸小说的版本修订史（连载本/修订本/新修版）待核。"],
  "sources":["C029"],"year_source":"C029","author_source":"C029","related_works":["sanguo","shuihu","xixiangji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《射雕英雄传》江湖谱系图",
    "cards":[{"title":"郭靖","text":"侠之大者（C029）","color":"main"},{"title":"黄蓉","text":"东邪之女","color":"family"},{"title":"五绝","text":"东邪西毒南帝北丐","color":"gold"},{"title":"九阴真经","text":"武学伦理","color":"plain"}]}
},
"guanchangxianxingji": {
  "id":"guanchangxianxingji","title":"官场现形记","original_title":"官场现形记（章回小说六十回）","region":"中国","era":"近代","era_detail":"晚清",
  "genre":"章回小说（谴责小说）","genre_group":"小说","language":"汉语（白话·章回体）","author_id":"liboyuan","author_name":"李伯元（李宝嘉）",
  "year_display":"1903—1905年连载于《世界繁华报》（中国作家网 C031）","year_sort":1903,
  "background":["中国作家网（C031）：李伯元'1867—1906'、'字宝嘉，别号南亭亭长。江苏武进人'；'1897年，30岁的李伯元来到上海创办《指南报》，后来改办成《游戏报》'。","连载：'1903—1905年，《官场现形记》六十回开始连载发表于《世界繁华报》'；初版本'一共两卷，各30回'（C031）。","鲁迅定评（C031 转引）：'虽命意在于匡世，似与讽刺小说同伦，而辞气浮露，笔无藏锋，甚且过甚其辞，以合时人嗜好……故别谓之谴责小说。'"],
  "outline":["官员群像举要（C031）：陶子尧购机器的花天酒地、剿匪虚报冒功、钦差'只拉弓，不放箭'、黄河救灾肥缺、十二姨太打蚊子求官等。","上卷讲官场科举经贸军事吏治，下卷写赈灾捐款慈善交接制度与外交（C031）。"],
  "characters":[{"name":"陶子尧","identity":"候补官员","note":"购机器闹剧（C031）"},{"name":"傅钦差","identity":"钦差","note":"清廉表演（C031）"},{"name":"童子良","identity":"总署大员","note":"拒银元点银票（C031）"}],
  "themes":["官场的全方位'现形'（C031：官场百科全书）。",
   "'谴责小说'与讽刺传统的分野（C031 转引鲁迅）。",
   "报刊连载与批评的互动（C031：慈禧索问轶事——顾颉刚引）。"],
  "influence":[{"text":"中国作家网：鲁迅'故别谓之谴责小说'的命名（C031 转引）。","source":"C031"},
   {"text":"中国作家网：胡适以之与《儒林外史》对比——'近世做谴责小说的人大都是失意的文人'（C031 转引）。","source":"C031"}],
  "reading":{"difficulties":["晚清官制与捐纳制度注释。","六十回的群像结构——先画官阶表。"],
   "editions":["《官场现形记》（人民文学出版社，通说待核）。"],
   "order":"与《儒林外史》《老残游记》合读：晚清—近代讽刺三部曲。"},
  "pending":["五编六十回的分编出版细节核对。","'四大谴责小说'总名出处待核。","李宝嘉/李伯元写法辨析待核。"],
  "sources":["C031"],"year_source":"C031","author_source":"C031","related_works":["rulin","laocan","weijunzi"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《官场现形记》官场百态图",
    "cards":[{"title":"购机器","text":"花天酒地（C031）","color":"family"},{"title":"剿匪","text":"虚报冒功","color":"antagonist"},{"title":"黄河救灾","text":"肥缺生意","color":"gold"},{"title":"只拉弓不放箭","text":"钦差心法","color":"main"}]}
},
"qiwan": {
  "id":"qiwan","title":"棋王","original_title":"棋王（中篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"中篇小说","genre_group":"小说","language":"汉语（白话·话本变奏）","author_id":"acheng","author_name":"阿城",
  "year_display":"1984年刊于《上海文学》第7期（中国作家网 C030）","year_sort":1984,
  "background":["中国作家网（C030）：'1984年第7期《上海文学》所发表的初版本《棋王》'；曾被《北京文学》以'写了知青生活的阴暗面'为由退稿；发表后'在文化热和迅速迭代更新的文学浪潮中被逐渐经典化'、'作为寻根文学的代表作之一进入到文学史叙述之中'。","文体（C030 转述）：阿城自述'语言样貌无非是话本变奏'，细节'暗取《老残游记》和《儒林外史》'，意象取《史记》与张岱笔记。"],
  "outline":["知青时代的'棋呆子'王一生：'俗世奇人'——火车奇遇、地区赛、'下盲棋以一敌九'的'车轮大战'（C030）。","母亲用捡来的牙刷把磨成一副无字棋——'全篇中最为动人心魄的片段'（C030）。","'不做俗人，哪儿会知道这般乐趣？'、'衣食是本'（C030 引文）。"],
  "characters":[{"name":"王一生","identity":"棋呆子","note":"知青棋痴（C030）"},{"name":"我","identity":"叙述者","note":"同车知青"}],
  "themes":["艰难时世中对于自我的守持（C030）。",
   "世俗与超脱的辩证：'衣食是本'（C030）。",
   "寻根：传统文化资源的当代激活（C030：寻根文学代表作）。"],
  "influence":[{"text":"中国作家网：'作为寻根文学的代表作之一进入到文学史叙述之中'（C030）。","source":"C030"},
   {"text":"中国作家网：与吴趼人笔法对勘——阿城'在描述中夹杂了心理活动的议论，有着同情的悲悯'（C030）。","source":"C030"}],
  "reading":{"difficulties":["话本式白话的节奏。","象棋文化与'吃'的世俗描写。"],
   "editions":["《棋王》（作家出版社1985年11月说——通说待核）。"],
   "order":"与《树王》《孩子王》合读（'三王'）。"},
  "pending":["1985年11月作家出版社单行本说待核。","'三王'总名出处待核。","阿城生年与本名核对。"],
  "sources":["C030"],"year_source":"C030","author_source":"C030","related_works":["laocan","biancheng","zhuangzi"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《棋王》车轮大战结构图",
    "cards":[{"title":"火车相遇","text":"俗世奇人（C030）","color":"family"},{"title":"无字棋","text":"牙刷把磨成的棋","color":"gold"},{"title":"盲棋一敌九","text":"车轮大战（C030）","color":"main"},{"title":"衣食是本","text":"世俗的箴言","color":"plain"}]}
},
"yueliangyuliupian": {
  "id":"yueliangyuliupian","title":"月亮与六便士","original_title":"The Moon and Sixpence","region":"英国","era":"现当代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"maugham","author_name":"威廉·萨默塞特·毛姆",
  "year_display":"1919年出版（Britannica：The Moon and Sixpence (1919)）","year_sort":1919,
  "background":["Britannica：'an account of an unconventional artist, suggested by the life of Paul Gauguin'（以保罗·高更的生平为原型的离经叛道艺术家故事——B248）。","Britannica：'Maugham's reputation as a novelist rests primarily on four books'（B248）。"],
  "outline":["证券经纪人思特里克兰德中年抛家弃业奔赴巴黎学画，终死于塔希提——以高更生平为原型（Britannica+通说）。","叙述者'我'的双重视角：道德谴责与艺术敬畏（通说）。"],
  "characters":[{"name":"思特里克兰德","identity":"画家","note":"以高更为原型（Britannica）"},{"name":"我（作家）","identity":"叙述者","note":"毛姆式的旁观者"}],
  "themes":["月亮（艺术）与六便士（世俗）的选择（书名通说）。",
   "艺术家对伦理秩序的破坏与救赎（通说）。",
   "旁观者的克制叙事（通说）。"],
  "influence":[{"text":"Britannica：《月亮与六便士》为毛姆声誉四书之一（B248）。","source":"B248"},
   {"text":"艺术家小说的通俗经典：后世大量改编与再阐释（通说待核）。","source":"B248"}],
  "reading":{"difficulties":["叙述者的道德立场——毛姆的反讽。","高更生平对照（勿等同）。"],
   "editions":["傅惟慈译本（上海译文出版社，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"对照《人性的枷锁》：毛姆的两条成长线。"},
  "pending":["书名典故（毛姆自嘲说）待核。","傅惟慈译本信息核对。","塔希提段落与高更实际行程的差异待核。"],
  "sources":["B248"],"year_source":"B248","author_source":"B248","related_works":["laorenhai","daolian","baijing"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《月亮与六便士》抉择结构图",
    "cards":[{"title":"抛家弃业","text":"40岁的出走","color":"antagonist"},{"title":"巴黎贫病","text":"艺术的修行","color":"family"},{"title":"塔希提","text":"最后的画布","color":"main"},{"title":"月亮与六便士","text":"两种价值（书名通说）","color":"gold"}]}
},
"zise": {
  "id":"zise","title":"紫色","original_title":"The Color Purple","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"walker","author_name":"艾丽斯·沃克",
  "year_display":"1982年出版（Britannica：The Color Purple (1982)）","year_sort":1982,
  "background":["Britannica：沃克为'first Black woman to win the Pulitzer Prize for fiction'（凭本作，1983年普利策奖+国家图书奖——B245）。","书信体：'An epistolary novel, it depicts the growing up and self-realization of an African American woman between 1909 and 1947' in rural Georgia（B245）。","争议（B245）：'some African American men strongly objected to the perceived negative portrayal of Black men'。"],
  "outline":["西丽（Celie）写给上帝与妹妹耐蒂的信——从受害到自我实现（Britannica 语境+通说）。","莎格对西丽的爱的启蒙；'survives rape and abuse at the hands of her father and husband'（B245）。","'Celie's changing views of God'——上帝观的转变（B245）。"],
  "characters":[{"name":"西丽（Celie）","identity":"书信作者","note":"成长的主人公（B245）"},{"name":"莎格","identity":"歌女","note":"爱的启蒙者（通说）"},{"name":"耐蒂","identity":"妹妹","note":"非洲来信（通说待核）"}],
  "themes":["黑人女性的自我实现（B245：self-realization）。",
   "黑人英语方言与书信体（B245：Black English Vernacular）。",
   "上帝观的转变与'妇女主义'（B245；womanist——通说待核）。"],
  "influence":[{"text":"Britannica：首位黑人女性普利策小说奖；斯皮尔伯格1985年电影（B245）。","source":"B245"},
   {"text":"黑人男性形象描写的争议与其回应——评论史的焦点（B245）。","source":"B245"}],
  "reading":{"difficulties":["方言书信体。","争议阅读：女性主义与黑人社群内部的讨论（B245）。"],
   "editions":["《紫色》（译林出版社/北京十月文艺出版社版本，通说待核）。"],
   "order":"对照《宠儿》：黑人女性叙事的两代。"},
  "pending":["西丽/耐蒂/莎格人名核对。","普利策与国家图书奖（1983）核对（B245 已载）。","womanist 定义句（沃克答《纽约时报》——B245 已载）核对。"],
  "sources":["B245"],"year_source":"B245","author_source":"B245","related_works":["chonger","shinv","dierxing"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《紫色》书信成长图",
    "cards":[{"title":"写给上帝","text":"最初的信","color":"family"},{"title":"莎格","text":"爱的启蒙","color":"main"},{"title":"上帝观","text":"转变（B245）","color":"gold"},{"title":"重聚","text":"自我实现","color":"plain"}]}
},
"peideluobalamo": {
  "id":"peideluobalamo","title":"佩德罗·巴拉莫","original_title":"Pedro Páramo","region":"墨西哥","era":"现当代","era_detail":"20世纪",
  "genre":"中长篇小说","genre_group":"小说","language":"西班牙语","author_id":"rulfo","author_name":"胡安·鲁尔福",
  "year_display":"1955年出版（Britannica：Pedro Páramo (1955)）","year_sort":1955,
  "background":["Britannica：'examines the physical and moral disintegration of a laconic cacique (boss)'（写一个寡言地方强人的肉体与道德崩坏——B244）；'set in a mythical hell on earth inhabited by the dead, who are haunted by their past transgressions'（鬼魂栖居的人间地狱——B244）。","影响（B244）：'He had an enormous impact on those Latin American authors, including Gabriel García Márquez, who practiced what has come to be known as magic realism'。"],
  "outline":["胡安·普雷西亚多寻父来到科马拉——满村亡灵的对话（通说）。","佩德罗·巴拉莫的记忆碎片与苏萨娜的悲声（通说待核）。","生死界线的消融：小说即亡灵的合唱（通说）。"],
  "characters":[{"name":"佩德罗·巴拉莫","identity":"卡西克（强人）","note":"寡言的地主（B244）"},{"name":"胡安·普雷西亚多","identity":"寻父者","note":"私生子（通说）"},{"name":"苏萨娜·圣胡安","identity":"爱人","note":"亡者之声（通说待核）"}],
  "themes":["亡灵的人间地狱（B244）。",
   "强人的身体与道德崩坏（B244）。",
   "魔幻现实主义的先声（B244：enormous impact）。"],
  "influence":[{"text":"Britannica：对包括马尔克斯在内的拉美魔幻现实主义作家影响巨大（B244）。","source":"B244"},
   {"text":"两书立身的传奇：'essentially only two books'（B244）。","source":"B244"}],
  "reading":{"difficulties":["亡灵叙述——无提示的声部切换。","碎片时序。"],
   "editions":["屠孟超译本（译林出版社，通说待核）。","西班牙文原版（FCE，通说待核）。"],
   "order":"对照《百年孤独》：马尔克斯自称能背诵本书（通说待核）。"},
  "pending":["科马拉村名与普雷西亚多母训核对。","屠孟超译本信息核对。","马尔克斯'能背《佩德罗·巴拉莫》'轶事出处待核。"],
  "sources":["B244"],"year_source":"B244","author_source":"B244","related_works":["bainian","huoluan","youlingzhijia"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《佩德罗·巴拉莫》亡灵科马拉图",
    "cards":[{"title":"寻父","text":"普雷西亚多进村","color":"family"},{"title":"亡灵合唱","text":"生死不分（B244）","color":"main"},{"title":"巴拉莫","text":"寡言强人的崩坏","color":"antagonist"},{"title":"苏萨娜","text":"爱的亡音","color":"gold"}]}
},
"taoli": {
  "id":"taoli","title":"逃离","original_title":"Runaway","region":"加拿大","era":"现当代","era_detail":"21世纪",
  "genre":"短篇小说集","genre_group":"小说","language":"英语","author_id":"munro","author_name":"艾丽丝·门罗",
  "year_display":"2004年出版（Britannica：Runaway (2004)）","year_sort":2004,
  "background":["Britannica：'In Runaway (2004) Munro explores the depths of ordinary lives through the use of temporal shifts'（以时间跳跃探入普通生活的深处——B246）。","作者（B246）：2013年诺贝尔文学奖——'master of the contemporary short story'（当代短篇大师）；'the first Canadian to be named the Nobel literature laureate'。"],
  "outline":["八篇故事（篇数通说待核）：卡拉的出走与回归、《机缘》三部曲的朱丽叶线等（通说待核）。","'逃离'的多种形态：婚姻、母亲身份、记忆（通说）。"],
  "characters":[{"name":"卡拉","identity":"马场主妇","note":"《逃离》篇（通说待核）"},{"name":"朱丽叶","identity":"学者","note":"《机缘》三部曲（通说待核）"}],
  "themes":["普通生活的深处（B246：depths of ordinary lives）。",
   "女性的出走与折返（通说）。",
   "安大略西南的社会文化环境（B246：native southwestern Ontario）。"],
  "influence":[{"text":"Britannica：'master of the contemporary short story'；2009布克国际奖（B246）。","source":"B246"},
   {"text":"短篇文体的当代尊严：门罗让'短篇'进入诺奖叙事（通说）。","source":"B246"}],
  "reading":{"difficulties":["时间跳跃的叙事（B246）。","开放式结局的克制。"],
   "editions":["《逃离》（北京十月文艺出版社，通说待核）。"],
   "order":"先读《逃离》篇 →《机缘》三部曲 → 其余。"},
  "pending":["八篇篇目核对。","《机缘》《很快》《沉寂》三部曲标题核对。","朱丽叶线人物名核对。"],
  "sources":["B246"],"year_source":"B246","author_source":"B246","related_works":["qingzhong","changri","shengmingce"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《逃离》出走—回归结构图",
    "cards":[{"title":"卡拉出走","text":"巴士上的犹疑","color":"main"},{"title":"回归","text":"婚姻的惯性","color":"antagonist"},{"title":"朱丽叶线","text":"机缘三部曲","color":"family"},{"title":"时间跳跃","text":"门罗方法（B246）","color":"gold"}]}
},
"siwangyuguowangdemafu": {
  "id":"siwangyuguowangdemafu","title":"死亡与国王的马夫","original_title":"Death and the King's Horseman","region":"尼日利亚","era":"现当代","era_detail":"20世纪",
  "genre":"悲剧（话剧）","genre_group":"戏剧","language":"英语（约鲁巴语境）","author_id":"soyinka","author_name":"沃莱·索因卡",
  "year_display":"1975年出版/上演（Britannica：Death and the King's Horseman (1975)）","year_sort":1975,
  "background":["Britannica：索因卡为'first Black African winner of the Nobel Prize for Literature in 1986'，授奖词称其作品'vivid, often harrowing'、'marked by an evocative, poetically intensified diction'（B247）。","题材：约鲁巴仪式性自杀传统与殖民当局的干涉（通说待核）。","作者：戏剧'blend Western techniques with Yoruba folklore'（B247）；1967—69年因比夫拉战争言论入狱（B247）。"],
  "outline":["约鲁巴国王的马夫艾雷辛须在国王下葬后自尽护送——殖民区行政官皮顶斯以'阻止野蛮习俗'之名干涉（通说待核）。","死亡仪式的失败与'过渡'的失败（通说待核）。"],
  "characters":[{"name":"艾雷辛（Elesin）","identity":"国王马夫","note":"仪式执行者（通说待核）"},{"name":"皮顶斯（Pilkings）","identity":"殖民行政官","note":"干涉者（通说待核）"},{"name":"奥伦蒂","identity":"儿子","note":"在英国归来（通说待核）"}],
  "themes":["仪式、共同体与个体的责任（通说待核）。",
   "殖民干涉与'文明'的傲慢（通说）。",
   "生死'过渡'（transition）的形而上（通说待核）。"],
  "influence":[{"text":"Britannica：首位黑非洲诺奖得主；作品'vivid, often harrowing'（B247）。","source":"B247"},
   {"text":"后殖民戏剧的经典文本（通说待核）。","source":"B247"}],
  "reading":{"difficulties":["约鲁巴宇宙观与奥甘诸神注释。","诗性行白的节奏。"],
   "editions":["英文原版（Methuen，通说待核）。","中译本信息待核。"],
   "order":"对照《瓦解》：殖民遭遇的两种写法。"},
  "pending":["艾雷辛/奥伦蒂人名与史实原型（1943年约鲁巴事件说）待核。","四幕结构与'过渡'主题评论待核。","皮顶斯夫妇化装舞会情节核对。"],
  "sources":["B247"],"year_source":"B247","author_source":"B247","related_works":["wajie","banlunhuangri","chi"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《死亡与国王的马夫》仪式结构图",
    "cards":[{"title":"仪式","text":"马夫的义务","color":"main"},{"title":"干涉","text":"殖民者的'文明'","color":"antagonist"},{"title":"失败","text":"过渡的断裂","color":"gold"},{"title":"二代","text":"归国儿子的代价","color":"family"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
