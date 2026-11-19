# -*- coding: utf-8 -*-
"""v7批B：吉檀迦利/安徒生童话/格林童话/先知 + 4作家页 + 5来源"""
import json, pathlib

new_src = [
{"id":"B261","title":"Rabindranath Tagore — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Rabindranath-Tagore","type":"百科全书","verified":True,"covers":["tagore","jitangali"],"note":"2026-11-20 核对：1861-05-07加尔各答—1941-08-07；'the first non-European to receive the Nobel Prize for Literature'（1913）；《吉檀迦利》为英译散文诗集、'hailed by W.B. Yeats and André Gide'；授奖词'profoundly sensitive, fresh and beautiful verse'；'Tagore's poems are virtually untranslatable, as are his more than 2,000 songs'；'the only poet credited with authoring the national anthems of two countries'（印度与孟加拉国歌）；1915年受封爵士、1919年阿姆利则惨案后退还"},
{"id":"B262","title":"Hans Christian Andersen (Danish author) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Hans-Christian-Andersen-Danish-author","type":"百科全书","verified":True,"covers":["andersen","antushengtonghua"],"note":"2026-11-20 核对：1805-04-02欧登塞—1875-08-04哥本哈根；首部童话集 Eventyr, fortalte for børn (1835)——含《打火匣》《小克劳斯和大克劳斯》《豌豆公主》《小意达的花》；1837/1842年续卷（含《海的女儿》《丑小鸭》《白雪皇后》语境）；Nye eventyr og historier (1858–72)；'his fairy tales are among the most frequently translated works in all of literary history'；出身贫寒（鞋匠之子）"},
{"id":"B263","title":"Brothers Grimm — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Brothers-Grimm","type":"百科全书","verified":True,"covers":["grimm","gelintonghua"],"note":"2026-11-20 核对：雅各布 1785-01-04哈瑙—1863-09-20柏林；威廉 1786-02-24哈瑙—1859-12-16柏林；Kinder- und Hausmärchen (1812–22)；'the 200 stories of this collection (including……Snow White, Little Red Riding Hood, Sleeping Beauty, and Rumpelstiltskin)'；'Grimm's law'——雅各布论证辅音对应规律性（'first sound shift'）"},
{"id":"B264","title":"Khalil Gibran — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Khalil-Gibran","type":"百科全书","verified":True,"covers":["jibolan","xianzhi"],"note":"2026-11-20 核对：1883-01-06黎巴嫩布舍里—1931-04-10纽约（48岁）；'The Prophet (1923; film 2014)'为其英语代表作；'Gibran's literary and artistic output is highly romantic in outlook and was influenced by the Bible, Friedrich Nietzsche, and William Blake'；以阿拉伯语与英语双语写作"},
{"id":"B265","title":"The Prophet (by Gibran) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/The-Prophet-by-Gibran","type":"百科全书","verified":True,"covers":["xianzhi"],"note":"2026-11-20 核对：1923年出版的'a book of 26 poetic essays'；'translated into more than a dozen languages'；'a best-selling book of popular mysticism……reached cult status among American youth for generations'；先知谈爱与婚姻、美、理性与激情、死亡等"},
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

authors = {
"tagore": {
  "id": "tagore", "name": "泰戈尔", "foreign_name": "Rabindranath Tagore（罗宾德拉纳特·泰戈尔，1861-05-07—1941-08-07）",
  "country": "印度", "birth": 1861, "death": 1941, "birth_year": 1861, "death_year": 1941, "era": "近代",
  "summary": "泰戈尔，加尔各答人，孟加拉语诗人、小说家、剧作家、作曲家与画家——'modernized Bengali literature'（使孟加拉文学现代化——Britannica）；'the first non-European to win the Nobel Prize in Literature'（1913年，首位获诺贝尔文学奖的非欧洲人——Britannica）；授奖词：'profoundly sensitive, fresh and beautiful verse'（B261）。'Tagore's poems are virtually untranslatable, as are his more than 2,000 songs'（B261）；'the only poet credited with authoring the national anthems of two countries'（印、孟两国国歌词作者——B261）。1915年受封爵士，1919年阿姆利则惨案后退还（B261）。",
  "timeline": [
    {"year": 1861, "text": "5月7日生于加尔各答（Britannica：Born May 7, 1861, Calcutta）。", "src": "B261"},
    {"year": 1901, "text": "创办国际大学（Britannica：Visva-Bharati founded as school 1901）。", "src": "B261"},
    {"year": 1913, "text": "获诺贝尔文学奖——首位非欧洲获奖者（Britannica）。", "src": "B261"},
    {"year": 1919, "text": "阿姆利则惨案后退还爵士封号（Britannica：renounced 1919）。", "src": "B261"},
    {"year": 1941, "text": "8月7日卒于加尔各答（Britannica）。", "src": "B261"}],
  "major_works": [
    {"work_id": "jitangali", "note": "英译散文诗集（Britannica：Nobel 1913）"},
    {"title": "新月集、飞鸟集", "note": "（通说待核）"},
    {"title": "戈拉", "note": "长篇（通说待核）"}],
  "style": [
    "'profoundly sensitive, fresh and beautiful verse'（Britannica 授奖词）。",
    "'poems are virtually untranslatable'：歌与诗的不可译（B261）。",
    "宗教抒情与东方智慧的英语转渡（B261：English prose translations）。"],
  "status": "Britannica 定位泰戈尔为首位非欧洲诺奖文学家、两国国歌作者、国际大学的创办人（B261）。",
  "sources": ["B261"], "dates_source": "B261",
  "pending": ["《吉檀迦利》1912年英文版（伦敦印度协会说）与1913年孟加拉原集关系待核。", "《飞鸟集》郑振铎译本待核。", "国际大学1921年成为大学（Britannica 已载）核对。"]
},
"andersen": {
  "id": "andersen", "name": "安徒生", "foreign_name": "Hans Christian Andersen（汉斯·克里斯蒂安·安徒生，1805-04-02—1875-08-04）",
  "country": "丹麦", "birth": 1805, "death": 1875, "birth_year": 1805, "death_year": 1875, "era": "近代",
  "summary": "安徒生，丹麦欧登塞人，出身贫寒（鞋匠之子——Britannica 语境），从穷困中崛起为'文学童话'的世界级大师——'Danish master of the literary fairy tale'（Britannica）；'his fairy tales are among the most frequently translated works in all of literary history'（其童话是文学史上被翻译最多的作品之一——Britannica）。首部童话集 Eventyr, fortalte for børn（1835）；'Nye eventyr og historier'（1858–72）扩展文类（B262）。",
  "timeline": [
    {"year": 1805, "text": "4月2日生于欧登塞（Britannica：Born April 2, 1805, Odense, Denmark）。", "src": "B262"},
    {"year": 1835, "text": "首部童话集出版——含《打火匣》《豌豆公主》等（Britannica）。", "src": "B262"},
    {"year": 1858, "text": "《新童话和故事》开始出版（1858—72）（Britannica）。", "src": "B262"},
    {"year": 1875, "text": "8月4日卒于哥本哈根（Britannica）。", "src": "B262"}],
  "major_works": [
    {"work_id": "antushengtonghua", "note": "童话集（Britannica：1835年起）"},
    {"title": "海的女儿、丑小鸭、白雪皇后", "note": "（Britannica 语境）"},
    {"title": "即兴诗人", "note": "小说（通说待核）"}],
  "style": [
    "'文学童话'的创造：以口语讲述（Britannica 语境：innovative use of spoken language）。",
    "写给孩子的深刻：'not afraid of introducing feelings and ideas that were beyond a child's immediate comprehension'（Britannica）。",
    "边缘人与苦难超越的主题（Britannica 语境：outsiders and triumph over hardship）。"],
  "status": "Britannica 定位安徒生为'文学童话'的丹麦大师、世界文学的不朽者之一（B262 语境：immortals of world literature）。",
  "sources": ["B262"], "dates_source": "B262",
  "pending": ["《海的女儿》首刊（1837年说）核对。", "叶君健译本（安徒生童话全集）待核。", "1835年小册子册数与定价细节待核。"]
},
"grimm": {
  "id": "grimm", "name": "格林兄弟", "foreign_name": "Brothers Grimm（雅各布·格林 1785-01-04—1863-09-20；威廉·格林 1786-02-24—1859-12-16）",
  "country": "德国", "birth": 1785, "death": 1863, "birth_year": 1785, "death_year": 1863, "era": "近代",
  "summary": "格林兄弟——雅各布与威廉——德国民俗学家与语言学家，以《儿童与家庭童话集》（Kinder- und Hausmärchen，1812—22；英语世界称格林童话）传世（Britannica）；'the 200 stories of this collection (including……Snow White, Little Red Riding Hood, Sleeping Beauty, and Rumpelstiltskin)'（含白雪公主、小红帽、睡美人、侏儒怪等200篇——B263）。雅各布以'Grimm's law'（格里姆定律——'first sound shift'）开创历史语言学（B263）；兄弟二人亦是德语词典的编纂者（通说待核）。",
  "timeline": [
    {"year": 1785, "text": "雅各布生于哈瑙（Britannica：born January 4, 1785, Hanau）。", "src": "B263"},
    {"year": 1786, "text": "威廉生于哈瑙（Britannica：born February 24, 1786）。", "src": "B263"},
    {"year": 1812, "text": "《儿童与家庭童话集》开始出版（1812—22）（Britannica）。", "src": "B263"},
    {"year": 1835, "text": "雅各布出版《德国神话》（Britannica：German Mythology (1835)）。", "src": "B263"},
    {"year": 1863, "text": "雅各布卒于柏林（威廉先于1859年卒）（Britannica）。", "src": "B263"}],
  "major_works": [
    {"work_id": "gelintonghua", "note": "童话集（Britannica：1812—22）"},
    {"title": "德语词典", "note": "（通说待核——兄弟合编）"},
    {"title": "德国神话", "note": "（Britannica：1835）"}],
  "style": [
    "民间口传的忠实辑录与文学润色并进（通说）。",
    "'Grimm's law'：历史语言学的里程碑（B263）。",
    "从民俗到民族文化的建构（通说待核）。"],
  "status": "Britannica 定位格林兄弟为德国民俗学家与语言学家、现代民俗学的奠基者之一（B263 语境）。",
  "sources": ["B263"], "dates_source": "B263",
  "pending": ["童话篇数（1812年初版86篇说；第七版1857年211篇说）核对。", "魏玛版与儿童版之别待核。", "兄弟二人生平分工（威廉主笔润色说）待核。"]
},
"jibolan": {
  "id": "jibolan", "name": "纪伯伦", "foreign_name": "Kahlil Gibran（纪伯伦·哈利勒·纪伯伦，1883-01-06—1931-04-10）",
  "country": "黎巴嫩", "birth": 1883, "death": 1931, "birth_year": 1883, "death_year": 1931, "era": "近代",
  "summary": "纪伯伦，黎巴嫩布舍里人、移民波士顿的阿拉伯裔美国作家与画家（Britannica），以阿拉伯语与英语双语写作——'produced romantic, mystical essays, stories, poetry, and paintings on themes like love, death, nature, and longing for his homeland'（B264）。代表作《先知》（1923；'a book of 26 poetic essays'——B265）；'translated into more than a dozen languages'、'a best-selling book of popular mysticism……reached cult status among American youth for generations'（B265）。'Gibran's literary and artistic output is highly romantic in outlook and was influenced by the Bible, Friedrich Nietzsche, and William Blake'（B264）。",
  "timeline": [
    {"year": 1883, "text": "1月6日生于黎巴嫩布舍里（Britannica：Born January 6, 1883, Bsharrī, Lebanon）。", "src": "B264"},
    {"year": 1895, "text": "随家移民波士顿（Britannica：emigrated to Boston as a child——年份通说待核）。", "src": "B264"},
    {"year": 1923, "text": "《先知》出版（B265：published in 1923）。", "src": "B265"},
    {"year": 1931, "text": "4月10日卒于纽约（Britannica）。", "src": "B264"}],
  "major_works": [
    {"work_id": "xianzhi", "note": "散文诗集（Britannica：1923）"},
    {"title": "狂人、先行者、沙与沫", "note": "（Britannica：The Madman (1918), The Forerunner (1920), Sand and Foam (1926)）"},
    {"title": "先知园", "note": "（通说待核）"}],
  "style": [
    "'highly romantic in outlook'：受《圣经》、尼采与布莱克影响（B264）。",
    "先知的布道体：26 篇散文诗（B265）。",
    "双语写作：阿拉伯语的《泪与笑》与英语的《先知》（通说待核）。"],
  "status": "Britannica 定位纪伯伦为黎巴嫩裔美国作家与画家、《先知》作者（B264/B265）。",
  "sources": ["B264", "B265"], "dates_source": "B264",
  "pending": ["移民年份（1895年说）核对。", "《先知》中译本（冰心译本说）待核。", "纪伯伦与玛丽·哈斯凯尔的书信史待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

works = {
"jitangali": {
  "id":"jitangali","title":"吉檀迦利","original_title":"গীতাঞ্জলি（Gitanjali，英译本）","region":"印度","era":"近代","era_detail":"20世纪初",
  "genre":"散文诗集","genre_group":"诗歌","language":"英语（自孟加拉语转译）","author_id":"tagore","author_name":"泰戈尔",
  "year_display":"1912—13年英文版（Britannica：hailed by W.B. Yeats and André Gide and won him the Nobel Prize in 1913）","year_sort":1912,
  "background":["Britannica（B261）：'This book, containing Tagore's English prose translations of religious poems from several of his Bengali verse collections'——孟加拉语宗教诗的英语散文自译；'hailed by W.B. Yeats and André Gide and won him the Nobel Prize in 1913'。","授奖词（B261）：'profoundly sensitive, fresh and beautiful verse'。"],
  "outline":["103首散文诗（首数通说待核）：献给'神'的献歌——爱情、劳作、死亡与宁静（通说）。"],
  "characters":[{"name":"歌者","identity":"'我'","note":"向神献歌的人"}],
  "themes":["献歌体：人与神的对话（通说）。",
   "东方灵性的英语转渡（B261：English prose translations）。",
   "'fresh and beautiful verse'（B261 授奖词）。"],
  "influence":[{"text":"Britannica：1913年诺奖——'the first non-European to receive the Nobel Prize'（B261）。","source":"B261"},
   {"text":"Britannica：叶芝与纪德的推崇（hailed by W.B. Yeats and André Gide）（B261）。","source":"B261"}],
  "reading":{"difficulties":["'神'的多义（人格神/泛神/自我）。","散文诗的节奏——朗读。"],
   "editions":["《吉檀迦利》（冰心译本，人民文学出版社，通说待核）。","英文原版（公有领域）。"],
   "order":"与《飞鸟集》《新月集》合读。"},
  "pending":["篇数（103首说）核对。","冰心译本信息核对。","叶芝序言（1912年说）待核。"],
  "sources":["B261"],"year_source":"B261","author_source":"B261","related_works":["caoyeji","chuci","nvshen"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《吉檀迦利》献歌结构图",
    "cards":[{"title":"献歌","text":"与神的对话","color":"main"},{"title":"孟加拉","text":"原作的根","color":"family"},{"title":"叶芝与纪德","text":"西方的推崇（B261）","color":"gold"},{"title":"诺奖1913","text":"首位非欧洲（B261）","color":"plain"}]}
},
"antushengtonghua": {
  "id":"antushengtonghua","title":"安徒生童话","original_title":"Eventyr, fortalte for børn 等童话集","region":"丹麦","era":"近代","era_detail":"19世纪",
  "genre":"童话集","genre_group":"故事集","language":"丹麦语","author_id":"andersen","author_name":"安徒生",
  "year_display":"1835年首部童话集出版（Britannica：Eventyr, fortalte for børn (1835)）；1858—72年《新童话和故事》（B262）","year_sort":1835,
  "background":["Britannica（B262）：首部童话集'Eventyr, fortalte for børn (1835; Tales, Told for Children)'含《打火匣》《小克劳斯和大克劳斯》《豌豆公主》《小意达的花》等；1837/1842年续卷；'Nye eventyr og historier (1858–72)'扩展文类。","地位（B262）：'his fairy tales are among the most frequently translated works in all of literary history'。","'he was not afraid of introducing feelings and ideas that were beyond a child's immediate comprehension'（B262）。"],
  "outline":["名篇谱系（B262 语境+通说）：《海的女儿》《丑小鸭》《卖火柴的小女孩》《皇帝的新装》《白雪皇后》。","从民间童话到'文学童话'的自觉创作（通说）。"],
  "characters":[{"name":"小美人鱼","identity":"海的女儿","note":"牺牲与灵魂（通说）"},{"name":"丑小鸭","identity":"天鹅","note":"苦难的超越（通说）"}],
  "themes":["超越儿童理解的深刻（B262）。",
   "边缘人主题（B262：outsiders and triumph over hardship）。",
   "口语的讲述体（B262：innovative use of spoken language）。"],
  "influence":[{"text":"Britannica：'his fairy tales are among the most frequently translated works in all of literary history'（B262）。","source":"B262"},
   {"text":"Britannica：'Danish master of the literary fairy tale'（B262）。","source":"B262"}],
  "reading":{"difficulties":["童话的双重读者（儿童/成人）。","丹麦福利社会之前的苦难底色。"],
   "editions":["叶君健译《安徒生童话全集》（上海译文出版社，通说待核）。","英文原版（公有领域）。"],
   "order":"先《海的女儿》《丑小鸭》→《卖火柴的小女孩》《皇帝的新装》。"},
  "pending":["《海的女儿》1837年首刊核对。","叶君健译本信息核对。","童话总篇数（156篇说）待核。"],
  "sources":["B262"],"year_source":"B262","author_source":"B262","related_works":["gelintonghua","xiaowangzi","yiqianlingyiye"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"安徒生童话谱系图",
    "cards":[{"title":"1835","text":"首部童话集（B262）","color":"family"},{"title":"海的女儿","text":"牺牲与灵魂","color":"main"},{"title":"丑小鸭","text":"苦难的超越","color":"gold"},{"title":"1858—72","text":"新童话（B262）","color":"plain"}]}
},
"gelintonghua": {
  "id":"gelintonghua","title":"格林童话","original_title":"Kinder- und Hausmärchen（Grimm's Fairy Tales）","region":"德国","era":"近代","era_detail":"19世纪",
  "genre":"童话集","genre_group":"故事集","language":"德语","author_id":"grimm","author_name":"格林兄弟（雅各布/威廉）",
  "year_display":"1812—1822年出版（Britannica：Kinder- und Hausmärchen (1812–22)）","year_sort":1812,
  "background":["Britannica（B263）：'the 200 stories of this collection (including, among the most enduring, Snow White, Little Red Riding Hood, Sleeping Beauty, and Rumpelstiltskin)'——白雪公主、小红帽、睡美人、侏儒怪等200篇。","语言学的另一面（B263）：雅各布以'Grimm's law'（'first sound shift'）论证辅音对应规律——历史语言学的里程碑。"],
  "outline":["名篇谱系（B263）：《白雪公主》《小红帽》《睡美人》《侏儒怪》等200篇（通说篇目）。","从口头采集到书面定型——版本史中的净化与增删（通说待核）。"],
  "characters":[{"name":"白雪公主/灰姑娘","identity":"童话 heroine","note":"最持久的形象（B263 语境）"}],
  "themes":["民俗采集与民族文化建构（通说）。",
   "童话的暴力与净化史（通说待核）。",
   "语言学的副产品（B263：Grimm's law）。"],
  "influence":[{"text":"Britannica：200篇故事集——含最持久的白雪公主等（B263）。","source":"B263"},
   {"text":"Britannica：格里姆定律——历史语言学里程碑（B263）。","source":"B263"}],
  "reading":{"difficulties":["版本差异（初版残酷、后版净化）。","德语方言地名。"],
   "editions":["《格林童话全集》（人民文学出版社魏以新译本等，通说待核）。","德文原版（公有领域）。"],
   "order":"与《安徒生童话》对读：采集童话 vs 文学童话。"},
  "pending":["初版86篇/第七版211篇说核对。","《儿童与家庭童话》书名的双义（儿童/家庭）待核。","兄弟分工史待核。"],
  "sources":["B263"],"year_source":"B263","author_source":"B263","related_works":["antushengtonghua","yisuo","yiqianlingyiye"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"格林童话谱系图",
    "cards":[{"title":"1812—22","text":"两卷本（B263）","color":"family"},{"title":"白雪公主","text":"最持久的名篇","color":"main"},{"title":"200篇","text":"民间口传辑录（B263）","color":"gold"},{"title":"格里姆定律","text":"语言学的兄弟","color":"plain"}]}
},
"xianzhi": {
  "id":"xianzhi","title":"先知","original_title":"The Prophet","region":"黎巴嫩","era":"近代","era_detail":"20世纪初",
  "genre":"散文诗集","genre_group":"诗歌","language":"英语","author_id":"jibolan","author_name":"纪伯伦（Kahlil Gibran）",
  "year_display":"1923年出版（Britannica：published in 1923）","year_sort":1923,
  "background":["Britannica（B265）：'a book of 26 poetic essays'——先知阿穆斯塔法在离港前被市民拦下，'about the mysteries of life'（谈生命的奥秘）：'love, marriage, beauty, reason and passion, and death'。","影响（B265）：'a best-selling book of popular mysticism……reached cult status among American youth for generations'；'translated into more than a dozen languages'。","作者风格（B264）：'highly romantic in outlook and was influenced by the Bible, Friedrich Nietzsche, and William Blake'。"],
  "outline":["先知与船：离港前的26篇布道——爱、婚姻、孩子、施与、劳作、欢乐与悲哀（篇目通说待核）。"],
  "characters":[{"name":"阿穆斯塔法","identity":"先知","note":"布道者（通说待核）"}],
  "themes":["'奥秘的讲说'（B265：mysteries of life）。",
   "爱与自由的箴言体（通说）。",
   "东方神秘主义与《圣经》修辞（B264 语境）。"],
  "influence":[{"text":"Britannica：'reached cult status among American youth for generations'（B265）。","source":"B265"},
   {"text":"Britannica：'translated into more than a dozen languages'（B265）。","source":"B265"}],
  "reading":{"difficulties":["箴言的断片式阅读。","圣经体的节奏。"],
   "editions":["冰心译《先知·沙与沫》（译林出版社/人民文学出版社，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"先《论爱》《论孩子》→ 通读。"},
  "pending":["26篇篇目核对。","冰心译本信息核对。","先知名（Almustafa）核对。"],
  "sources":["B265","B264"],"year_source":"B265","author_source":"B264","related_works":["jitangali","shengqu","waerdenghu"] ,
  "svg":{"type":"grid","width":680,"height":340,"caption":"《先知》26篇布道图",
    "cards":[{"title":"论爱","text":"爱的重负与甜蜜","color":"main"},{"title":"论孩子","text":"生命的箭矢","color":"gold"},{"title":"论死","text":"生与死的统一","color":"family"},{"title":"先知与船","text":"离港前的讲说（B265）","color":"plain"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
