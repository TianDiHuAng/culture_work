# -*- coding: utf-8 -*-
"""v6批5：外国当代 8部+8作家页+8来源"""
import json, pathlib

new_src = [
{"id":"B249","title":"Seamus Heaney — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Seamus-Heaney","type":"百科全书","verified":True,"covers":["heaney","xinishixuan"],"note":"2026-11-20 核对：1939-04-13北爱尔兰Castledawson附近—2013-08-30都柏林；1995诺奖授奖词 'for works of lyrical beauty and ethical depth, which exalt everyday miracles and the living past'；Wintering Out (1972) 与 North (1975) 更直接触及北爱暴力；《挖掘》：'Between my finger and my thumb / The squat pen rests. / I'll dig with it.'；遗言 Noli timere（不要害怕）"},
{"id":"B250","title":"Ian McEwan — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ian-McEwan","type":"百科全书","verified":True,"covers":["mcewan","shuzui"],"note":"2026-11-20 核对：1948-06-21生；Booker 1998（Amsterdam）；'Atonement (film 2007) traces over six decades the consequences of a lie told in the 1930s'；早期获绰号 'Ian Macabre'；'restrained, refined prose style accentuates the horror of his dark humor'"},
{"id":"B251","title":"Roberto Bolano — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Roberto-Bolano","type":"百科全书","verified":True,"covers":["bolano","huangyezhentan"],"note":"2026-11-20 核对：1953-04-28圣地亚哥—2003-07-15巴塞罗那（50岁）；'Los detectives salvajes (1998; The Savage Detectives)'获罗慕洛·加列戈斯奖、'made Bolaño a literary star throughout Latin America'；'His worldwide literary reputation was made with the posthumous publication of his magnum opus, 2666 (2004)'；'one of the leading South American literary figures at the turn of the 21st century'"},
{"id":"B252","title":"Herta Muller — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Herta-Muller","type":"百科全书","verified":True,"covers":["muller","fengzhonglvli"],"note":"2026-11-20 核对：1953-08-17罗马尼亚Nițchidorf生；1987年移居西德；Herztier (1994)英译 The Land of Green Plums 获国际IMPAC都柏林奖（1998）；诺奖2009授奖词：以'诗歌的凝练与散文的率真'描绘'the landscape of the dispossessed'（被剥夺者的风景）"},
{"id":"B253","title":"Svetlana Alexievich — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Svetlana-Alexievich","type":"百科全书","verified":True,"covers":["alexievich","ershou shijian"],"note":"2026-11-20 核对：1948-05-31生于Stanislav（今乌克兰伊万诺-弗兰科夫斯克）；Secondhand Time (2013)；方法：'hybrid literary genre that evolved as the closest possible approximation to real life'、'human voices were allowed to speak for themselves'；目标'a history of human feelings'；诺奖2015授奖词 'for her polyphonic writings, a monument to suffering and courage in our time'"},
{"id":"B254","title":"Don DeLillo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Don-DeLillo","type":"百科全书","verified":True,"covers":["delillo","baizaoyin"],"note":"2026-11-20 核对：1936-11-20纽约生；White Noise (1985; film 2022) 获全国图书奖小说奖——'tells of a professor of Hitler studies'；'postmodernist works portray the anomie of an America cosseted by material excess'；Underworld (1997)为其最受赞誉之作"},
{"id":"B255","title":"Raymond Carver — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Raymond-Carver","type":"百科全书","verified":True,"covers":["carver","kafuxuan"],"note":"2026-11-20 核对：1938-05-25俄勒冈Clatskanie—1988-08-02华盛顿州安吉利斯港（50岁）；What We Talk About When We Talk About Love (1981)、Cathedral (1984)；'stripped-down, minimalist prose style is remarkable for its honesty and power'；'His style, influenced by Ernest Hemingway and Samuel Beckett, was spare and flat but powerfully suggestive'；被视为使英语短篇在20世纪晚期复兴"},
{"id":"B256","title":"John Updike — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/John-Updike","type":"百科全书","verified":True,"covers":["updike","tuzipaopa"],"note":"2026-11-20 核对：1932-03-18宾州Reading—2009-01-27；兔子五书：Rabbit, Run (1960)/Rabbit Redux (1971)/Rabbit Is Rich (1981)/Rabbit at Rest (1990)/Rabbit Remembered (2001)；Rabbit Is Rich 与 Rabbit at Rest 两获普利策奖；'concerns a former star athlete who is unable to recapture success when bound by marriage and small-town life'"},
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
"heaney": {
  "id": "heaney", "name": "谢默斯·希尼", "foreign_name": "Seamus Heaney（谢默斯·希尼，1939-04-13—2013-08-30）",
  "country": "爱尔兰", "birth": 1939, "death": 2013, "birth_year": 1939, "death_year": 2013, "era": "现当代",
  "summary": "希尼，北爱尔兰伦敦德里郡人，爱尔兰诗人——其诗唤起爱尔兰乡村生活、历史与神话，间接映照北爱'动乱'（Britannica：evoked Irish rural life, history, and myth, often reflecting indirectly on the Troubles）。1995年获诺贝尔文学奖，授奖词：'for works of lyrical beauty and ethical depth, which exalt everyday miracles and the living past'（以抒情之美与伦理深度颂扬日常奇迹与活着的过去——Britannica）。2013年8月30日在都柏林去世，临终拉丁语遗言'Noli timere'（不要害怕——Britannica）。",
  "timeline": [
    {"year": 1939, "text": "4月13日生于北爱尔兰伦敦德里郡（Britannica：Born April 13, 1939）。", "src": "B249"},
    {"year": 1966, "text": "首部诗集《一个自然主义者的死亡》出版（1966年说——通说待核）。", "src": "B249"},
    {"year": 1975, "text": "《北方》出版——更直接触及北爱暴力（Britannica：In Wintering Out (1972) and North (1975)……）。", "src": "B249"},
    {"year": 1995, "text": "获诺贝尔文学奖（Britannica）。", "src": "B249"},
    {"year": 2013, "text": "8月30日卒于都柏林（Britannica：died in Dublin in 2013 at age 74）。", "src": "B249"}],
  "major_works": [
    {"work_id": "xinishixuan", "note": "诗选（本库立目）"},
    {"title": "北方、田野工作", "note": "（Britannica：North (1975)）"},
    {"title": "诗学文集《写作的愉悦》", "note": "（通说待核）"}],
  "style": [
    "'抒情之美与伦理深度'（Britannica 授奖词）。",
    "泥炭考古意象：以远古尸骸映照当下暴力（Britannica：《惩罚》将古爱尔兰的仪式惩罚与动乱中对女性的涂柏油羽毛之刑并置）。",
    "'日常工作'的圣化：掘土与笔（Britannica：《挖掘》——'I'll dig with it.'）。"],
  "status": "Britannica 定位希尼为唤起爱尔兰乡村与神话、间接映照动乱的诗人、1995年诺奖得主；其诺贝尔演说'Crediting Poetry'（通说待核）。",
  "sources": ["B249"], "dates_source": "B249",
  "pending": ["首部诗集1966年出版细节核对。", "'bog poems'（泥炭诗）学术命名待核。", "诺贝尔演说标题核对。"]
},
"mcewan": {
  "id": "mcewan", "name": "伊恩·麦克尤恩", "foreign_name": "Ian McEwan（伊恩·麦克尤恩，1948-06-21— ）",
  "country": "英国", "birth": 1948, "death": None, "birth_year": 1948, "death_year": None, "era": "现当代",
  "summary": "麦克尤恩，英国小说家、短篇家与编剧，早期阴郁小说为他赢得'Ian Macabre'（麦克尤恩阴森）的绰号，1980年代转向家庭剧与政治主题（Britannica），代表作《阿姆斯特丹》（1998布克奖）与《赎罪》（2001）。'Atonement (film 2007) traces over six decades the consequences of a lie told in the 1930s'（《赎罪》追踪1930年代一句谎言在六十年间的后果——Britannica）。文体：'restrained, refined prose style accentuates the horror of his dark humor and perverse subject matter'（克制而精炼的文风放大其黑色幽默与乖异题材的恐怖——Britannica）。",
  "timeline": [
    {"year": 1948, "text": "6月21日生于英格兰奥尔德肖特（Britannica：Born June 21, 1948, Aldershot, England）。", "src": "B250"},
    {"year": 1998, "text": "《阿姆斯特丹》获布克奖（Britannica：Booker Prize 1998）。", "src": "B250"},
    {"year": 2001, "text": "《赎罪》出版（Britannica：Atonement (2001)）。", "src": "B250"},
    {"year": 2007, "text": "《赎罪》电影上映（Britannica：film 2007）。", "src": "B250"}],
  "major_works": [
    {"work_id": "shuzui", "note": "长篇（Britannica：2001）"},
    {"title": "阿姆斯特丹", "note": "（Britannica：1998布克奖）"},
    {"title": "时间中的孩子、切瑟尔海滩", "note": "（Britannica 存目）"}],
  "style": [
    "'克制、精炼的散文'（Britannica：restrained, refined prose style）。",
    "从'Ian Macabre'式乖异到家庭伦理剧（Britannica 语境）。",
    "谎言—记忆—赎罪的叙事机器（Britannica：the consequences of a lie told in the 1930s）。"],
  "status": "Britannica 定位麦克尤恩为当代英国最重要的小说家之一（1998布克奖得主）；《赎罪》为其国际声誉之作（语境）。",
  "sources": ["B250"], "dates_source": "B250",
  "pending": ["《赎罪》布克奖落选争议（2001年说）待核。", "小说三部结构（Part One/Two/Three+尾声）核对。", "电影乔·怀特导演（2007——Britannica 已载年份）细节待核。"]
},
"bolano": {
  "id": "bolano", "name": "罗贝托·波拉尼奥", "foreign_name": "Roberto Bolaño（罗贝托·波拉尼奥，1953-04-28—2003-07-15）",
  "country": "智利", "birth": 1953, "death": 2003, "birth_year": 1953, "death_year": 2003, "era": "现当代",
  "summary": "波拉尼奥，生于圣地亚哥的智利小说家与诗人——'rose from obscurity to become a major Latin American literary voice'（从默默无闻跃为拉美主要文学声音——Britannica）；'one of the leading South American literary figures at the turn of the 21st century'（21世纪初南美文学领军人物之一——Britannica）。1990年由诗转向小说后高产创作直至50岁去世；《荒野侦探》（1998）'made Bolaño a literary star throughout Latin America'并获罗慕洛·加列戈斯奖（Britannica）；身后出版的'鸿篇巨制'《2666》（2004）奠定世界声誉（Britannica：His worldwide literary reputation was made with the posthumous publication of his magnum opus, 2666 (2004)）。",
  "timeline": [
    {"year": 1953, "text": "4月28日生于智利圣地亚哥（Britannica：Born April 28, 1953, Santiago, Chile）。", "src": "B251"},
    {"year": 1990, "text": "由诗转向小说（Britannica：After turning from poetry to fiction in 1990）。", "src": "B251"},
    {"year": 1998, "text": "《荒野侦探》出版并获加列戈斯奖（Britannica）。", "src": "B251"},
    {"year": 2003, "text": "7月15日卒于巴塞罗那（Britannica：Died July 15, 2003, Barcelona, Spain）。", "src": "B251"},
    {"year": 2004, "text": "《2666》身后出版（Britannica：2666 (2004, posthumous)）。", "src": "B251"}],
  "major_works": [
    {"work_id": "huangyezhentan", "note": "长篇（Britannica：1998）"},
    {"title": "2666", "note": "（Britannica：2004 身后出版，鸿篇巨制）"},
    {"title": "智利之夜、护身符", "note": "（Britannica 存目）"}],
  "style": [
    "'现实主义、末日感与黑色幽默'的混合（通说待核）。",
    "文学浪游者的群像：真实与虚构诗人互嵌（通说）。",
    "'unflinching exploration of suffering and grief'（Britannica：《2666》第四部分——不回避的受难书写）。"],
  "status": "Britannica 定位波拉尼奥为21世纪初南美文学领军人物之一；《2666》出版后'几乎其所有早期西语作品都被译成英文'（Britannica）。",
  "sources": ["B251"], "dates_source": "B251",
  "pending": ["《荒野侦探》中译本（世纪文景说）待核。","圣特雷莎（圣特莱莎）与边境杀婴案母题待核。","'现实以下主义'（infrarrealismo）运动待核。"]
},
"muller": {
  "id": "muller", "name": "赫塔·米勒", "foreign_name": "Herta Müller（赫塔·米勒，1953-08-17— ）",
  "country": "德国", "birth": 1953, "death": None, "birth_year": 1953, "death_year": None, "era": "现当代",
  "summary": "米勒，罗马尼亚出生的德语作家（Britannica：Romanian-born German writer），以描写齐奥塞斯库独裁下的生活获2009年诺贝尔文学奖（Britannica）。1979年因拒绝与秘密警察合作被解雇（Britannica：Fired from translator job 1979），1987年移居西德（Britannica：Emigrated 1987）。小说《风中绿李》（Herztier，1994）获国际IMPAC都柏林文学奖（Britannica）；诺奖授奖词：以'诗歌的凝练与散文的率真'描绘'the landscape of the dispossessed'（被剥夺者的风景——Britannica）。",
  "timeline": [
    {"year": 1953, "text": "8月17日生于罗马尼亚尼奇基多夫（Britannica：Born August 17, 1953, Nițchidorf, Romania）。", "src": "B252"},
    {"year": 1979, "text": "被解雇（Britannica：Fired from translator job 1979）。", "src": "B252"},
    {"year": 1987, "text": "移居西德（Britannica：Emigrated 1987）。", "src": "B252"},
    {"year": 2009, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 2009）。", "src": "B252"}],
  "major_works": [
    {"work_id": "fengzhonglvli", "note": "长篇（Britannica：Herztier 1994）"},
    {"title": "饥饿天使、低地", "note": "（Britannica 语境）"},
    {"title": "诗与散文合集", "note": "（通说待核）"}],
  "style": [
    "'totalitarianism and exile'（极权与流放）贯穿其作（Britannica）。",
    "'诗歌的凝练与散文的率真'（Britannica 授奖词）。",
    "罗尼亚德语少数族裔的记忆书写（通说待核）。"],
  "status": "Britannica 定位米勒为以齐奥塞斯库独裁生活书写获2009年诺奖的德语作家；'The Land of Green Plums'为其代表作（B252）。",
  "sources": ["B252"], "dates_source": "B252",
  "pending": ["中译本（《风中绿李》译林说）信息核对。", "Herztier 德文原义（心脏兽）与英文转译差异待核。", "秘密警察档案事件细节待核。"]
},
"alexievich": {
  "id": "alexievich", "name": "斯韦特兰娜·阿列克谢耶维奇", "foreign_name": "Svetlana Alexievich（斯韦特兰娜·阿列克谢耶维奇，1948-05-31— ）",
  "country": "白俄罗斯", "birth": 1948, "death": None, "birth_year": 1948, "death_year": None, "era": "现当代",
  "summary": "阿列克谢耶维奇，白俄罗斯记者与散文作家（Britannica），以俄语写作，'blends reportage with literature'（报道与文学交融——Britannica），以普通人声音记录苏联与后苏联的剧变；'human voices were allowed to speak for themselves about the main events of the age'（让人的声音自己讲述时代大事——Britannica）；目标：'a history of human feelings'（一部人类情感的历史——Britannica）。2015年获诺贝尔文学奖——'for her polyphonic writings, a monument to suffering and courage in our time'（复调书写，我们时代苦难与勇气的纪念碑——Britannica）；为首位白俄罗斯获奖者（Britannica）。",
  "timeline": [
    {"year": 1948, "text": "5月31日生于Stanislav（今乌克兰伊万诺-弗兰科夫斯克）（Britannica）。", "src": "B253"},
    {"year": 1985, "text": "《战争中没有女性》《最后的见证人》出版（Britannica：War's Unwomanly Face and Last Witnesses (1985)）。", "src": "B253"},
    {"year": 2013, "text": "《二手时间》出版（Britannica：Secondhand Time (2013)）。", "src": "B253"},
    {"year": 2015, "text": "获诺贝尔文学奖（Britannica）。", "src": "B253"}],
  "major_works": [
    {"work_id": "ershoushijian", "note": "口述实录（Britannica：2013）"},
    {"title": "切尔诺贝利的祭祷", "note": "（Britannica：Voices from Chernobyl (1997)）"},
    {"title": "锌皮娃娃兵", "note": "（Britannica：Zinky Boys (1990)）"}],
  "style": [
    "'复调'（polyphonic）书写（Britannica 授奖词）。",
    "'最接近真实生活的文类'（Britannica：the closest possible approximation to real life）。",
    "人的声音即史料：情感史替代事件史（Britannica：a history of human feelings）。"],
  "status": "Britannica 定位阿列克谢耶维奇为白俄罗斯首位诺奖作家、'复调书写'的创造者（B253）。",
  "sources": ["B253"], "dates_source": "B253",
  "pending": ["《二手时间》中译本（中信2016说）核对。", "'red man'（红色人）概念待核。", "白俄罗斯国内出版压力与流亡细节待核。"]
},
"delillo": {
  "id": "delillo", "name": "唐·德里罗", "foreign_name": "Don DeLillo（唐·德里罗，1936-11-20— ）",
  "country": "美国", "birth": 1936, "death": None, "birth_year": 1936, "death_year": None, "era": "现当代",
  "summary": "德里罗，纽约人，美国后现代主义小说家——'whose postmodernist works portray the anomie of an America cosseted by material excess'（其作品刻画被物质过剩娇惯的美国之失范——Britannica）。《白噪音》（1985）获全国图书奖小说奖——'tells of a professor of Hitler studies'（写一位'希特勒研究'教授——Britannica）；《地下世界》（1997）为其最受赞誉之作（Britannica：significant acclaim）。",
  "timeline": [
    {"year": 1936, "text": "11月20日生于纽约（Britannica：Born November 20, 1936, New York）。", "src": "B254"},
    {"year": 1971, "text": "首部长篇《美国志异》出版（Britannica：First novel Americana 1971）。", "src": "B254"},
    {"year": 1985, "text": "《白噪音》获全国图书奖（Britannica：White Noise 1985）。", "src": "B254"},
    {"year": 1997, "text": "《地下世界》出版（Britannica：Underworld 1997）。", "src": "B254"}],
  "major_works": [
    {"work_id": "baizaoyin", "note": "长篇（Britannica：1985）"},
    {"title": "地下世界", "note": "（Britannica：1997）"},
    {"title": "天秤星座、坠落的人", "note": "（Britannica 存目）"}],
  "style": [
    "后现代的'失范'书写（Britannica：anomie of an America cosseted by material excess）。",
    "媒体、消费与死亡的三角（通说）。",
    "希特勒研究的学术戏仿（Britannica：professor of Hitler studies）。"],
  "status": "Britannica 定位德里罗为美国后现代主义代表小说家；2013年国会图书馆美国小说奖、2015年美国图书奖章（B254）。",
  "sources": ["B254"], "dates_source": "B254",
  "pending": ["《白噪音》中译本信息核对。", "'最杰出的活着的美国小说家'类评价出处待核。", "2022年电影改编（Britannica 已载）核对。"]
},
"carver": {
  "id": "carver", "name": "雷蒙德·卡佛", "foreign_name": "Raymond Carver（雷蒙德·卡佛，1938-05-25—1988-08-02）",
  "country": "美国", "birth": 1938, "death": 1988, "birth_year": 1938, "death_year": 1988, "era": "现当代",
  "summary": "卡佛，俄勒冈州人，美国短篇小说家与诗人——其极简主义白描现实地刻画底层劳动者的挣扎（Britannica 语境：minimalist prose realistically depicted the struggles of the working poor），取材于自身生活；被视为使英语短篇小说在20世纪晚期重获生机的人之一（Britannica：helping revitalize the English-language short story）。'stripped-down, minimalist prose style is remarkable for its honesty and power'（削减到极简的文体以诚实与力量著称——Britannica）；风格受海明威与贝克特影响——'spare and flat but powerfully suggestive'（简省、平淡却有力地暗示——Britannica）。50岁去世（Britannica）。",
  "timeline": [
    {"year": 1938, "text": "5月25日生于俄勒冈州克拉茨卡尼（Britannica：Born May 25, 1938, Clatskanie, Oregon）。", "src": "B255"},
    {"year": 1981, "text": "《当我们谈论爱情时我们在谈论什么》出版（Britannica）。", "src": "B255"},
    {"year": 1984, "text": "《大教堂》出版（Britannica：Cathedral (1984)）。", "src": "B255"},
    {"year": 1988, "text": "8月2日卒于华盛顿州安吉利斯港（Britannica：Died August 2, 1988）。", "src": "B255"}],
  "major_works": [
    {"work_id": "kafuxuan", "note": "短篇集（Britannica：1981）"},
    {"title": "大教堂", "note": "（Britannica：1984）"},
    {"title": "愤怒的冬季、需要时给我电话", "note": "（通说待核）"}],
  "style": [
    "极简主义：'stripped-down, minimalist prose style'（Britannica）。",
    "受海明威与贝克特影响——'spare and flat but powerfully suggestive'（Britannica）。",
    "底层劳动者生活（Britannica：the working poor）。"],
  "status": "Britannica 定位卡佛为20世纪晚期英语短篇小说复兴的关键人物（B255）；'脏现实主义'（dirty realism）标签（通说待核）。",
  "sources": ["B255"], "dates_source": "B255",
  "pending": ["戈登·利什编辑争议（原文与刊出本差异）待核。", "《大教堂》1983/1984年（Britannica 正文作1984）核对。", "中译本信息核对。"]
},
"updike": {
  "id": "updike", "name": "约翰·厄普代克", "foreign_name": "John Updike（约翰·厄普代克，1932-03-18—2009-01-27）",
  "country": "美国", "birth": 1932, "death": 2009, "birth_year": 1932, "death_year": 2009, "era": "现当代",
  "summary": "厄普代克，宾夕法尼亚州雷丁人，多产的美国小说家、短篇家与诗人（Britannica），以细腻的白描刻画美国小镇中产新教徒生活（Britannica 语境：careful prose……small-town, middle-class Protestant American life）。'兔子五书'（1960—2001）中《兔子富了》（1982）与《兔子安息》（1990）两获普利策奖（Britannica：both earned him Pulitzer Prizes）。《兔子，跑吧》（1960）——'concerns a former star athlete who is unable to recapture success when bound by marriage and small-town life'（写一个被婚姻与小城生活束缚的前球星无法重获成功——Britannica）。",
  "timeline": [
    {"year": 1932, "text": "3月18日生于宾州雷丁（Britannica：Born March 18, 1932, Reading, Pennsylvania）。", "src": "B256"},
    {"year": 1960, "text": "《兔子，跑吧》出版（Britannica：Rabbit, Run (1960)）。", "src": "B256"},
    {"year": 1982, "text": "《兔子富了》获普利策奖（Britannica）。", "src": "B256"},
    {"year": 2009, "text": "1月27日卒于马萨诸塞州丹弗斯（Britannica：Died January 27, 2009, Danvers, Massachusetts）。", "src": "B256"}],
  "major_works": [
    {"work_id": "tuzipaopa", "note": "长篇（Britannica：1960）"},
    {"title": "兔子回家/兔子富了/兔子安息", "note": "（Britannica：兔子五书）"},
    {"title": "《_MAPPING》？——不：巴西、圣彼得堡的伊丽莎白", "note": "（通说待核）"}],
  "style": [
    "'careful prose'：细腻写实的白描（Britannica 语境）。",
    "中产美国身体的编年史：性与信仰的挣扎（通说）。",
    "兔子哈利·安斯特朗：美国三十年的一面镜子（通说待核）。"],
  "status": "Britannica 定位厄普代克为多产小说家、两获普利策奖（B256）；'Rabbit Remembered (2001) returns to characters from those books in the wake of Rabbit's death'（Britannica）。",
  "sources": ["B256"], "dates_source": "B256",
  "pending": ["《兔子，跑吧》中译本信息核对。", "厄普代克的国家图书奖与笔会福克纳奖待核。", "'Protestant小城'背景自传性待核。"]
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
"xinishixuan": {
  "id":"xinishixuan","title":"希尼诗选","original_title":"希尼诗选（通行选集）","region":"爱尔兰","era":"现当代","era_detail":"20—21世纪",
  "genre":"诗选集","genre_group":"诗歌","language":"英语","author_id":"heaney","author_name":"谢默斯·希尼",
  "year_display":"诗作于1966—2013年间；通行选本数十首","year_sort":1975,
  "background":["Britannica：希尼之诗'evoked Irish rural life, history, and myth, often reflecting indirectly on the Troubles'（唤起爱尔兰乡村、历史与神话，间接映照北爱动乱）。","诺奖授奖词（B249）：'for works of lyrical beauty and ethical depth, which exalt everyday miracles and the living past'。"],
  "outline":["《挖掘》：'Between my finger and my thumb / The squat pen rests. / I'll dig with it.'（B249）——以笔为锹的起点。","《惩罚》：以远古泥炭女尸并置动乱中的涂油之刑（B249 转述）。","《北方》（1975）直接处理北爱暴力（B249）。"],
  "characters":[{"name":"挖土者/诗人","identity":"抒情自我","note":"锹与笔的转换（B249）"}],
  "themes":["日常奇迹与'活着的过去'（B249 授奖词）。",
   "语言与暴力的伦理（B249：《惩罚》并置法）。",
   "乡村劳作的圣化（B249：《挖掘》）。"],
  "influence":[{"text":"Britannica：1995年诺奖——'lyrical beauty and ethical depth'。","source":"B249"},
   {"text":"Britannica：《北方》'began to encompass more directly such subjects as the violence in Northern Ireland'。","source":"B249"}],
  "reading":{"difficulties":["北爱历史（'Troubles'）背景注释。","泥炭考古意象的互文。"],
   "editions":["《希尼诗选》（广西人民出版社，通说待核）。","《通往Electric之光》？（中译本信息待核）。"],
   "order":"先《挖掘》→《惩罚》→《北方》组诗。"},
  "pending":["中译本信息核对。","《田野工作》等篇目核对。","诺贝尔演说'Crediting Poetry'待核。"],
  "sources":["B249"],"year_source":"B249","author_source":"B249","related_works":["yezhishixuan","frosite","caoyeji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"希尼诗歌结构图",
    "cards":[{"title":"挖掘","text":"锹与笔（B249）","color":"main"},{"title":"惩罚","text":"泥炭与动乱","color":"antagonist"},{"title":"北方","text":"1975（B249）","color":"family"},{"title":"Noli timere","text":"遗言：不要害怕","color":"gold"}]}
},
"shuzui": {
  "id":"shuzui","title":"赎罪","original_title":"Atonement","region":"英国","era":"现当代","era_detail":"21世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mcewan","author_name":"伊恩·麦克尤恩",
  "year_display":"2001年出版（Britannica：Atonement (film 2007)——2001年出版说待核）","year_sort":2001,
  "background":["Britannica：'Atonement (film 2007) traces over six decades the consequences of a lie told in the 1930s'（《赎罪》追踪1930年代一句谎言在六十年间的后果）。","作者文体（B250）：'restrained, refined prose style accentuates the horror of his dark humor and perverse subject matter'。"],
  "outline":["1935年庄园：布里奥妮的误证拆散塞西莉亚与罗比（通说待核）。","敦刻尔克与战地医院——谎言的代价（通说待核）。","尾声：老年布里奥妮的'赎罪'书写——虚构与真相（通说待核）。"],
  "characters":[{"name":"布里奥妮","identity":"少女/作家","note":"谎言之源（通说）"},{"name":"塞西莉亚","identity":"姐姐","note":"爱情受害者"},{"name":"罗比","identity":"仆人之子","note":"蒙冤者"}],
  "themes":["谎言的六十年后果（Britannica）。",
   "小说家的赎罪权：'虚构'能否赦免（通说待核）。",
   "敦刻尔克与庄园的两极（通说）。"],
  "influence":[{"text":"Britannica：《赎罪》列为麦克尤恩最知名小说之一；2007年改编电影（B250）。","source":"B250"},
   {"text":"当代英语小说的'元虚构'代表作（通说待核）。","source":"B250"}],
  "reading":{"difficulties":["三部结构与'尾声'的元虚构翻转。","敦刻尔克撤退历史背景。"],
   "editions":["《赎罪》（上海译文出版社，通说待核）。"],
   "order":"对照《长日留痕》：英伦记忆的两代书写。"},
  "pending":["2001年出版（Jonathan Cape说）核对。","布里奥妮三部结尾版本差异核对。","电影乔·怀特导演（2007）细节待核。"],
  "sources":["B250"],"year_source":"B250","author_source":"B250","related_works":["changri","qingzhong","shenpan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《赎罪》谎言—六十年结构图",
    "cards":[{"title":"1935","text":"一句谎言","color":"antagonist"},{"title":"1940","text":"敦刻尔克","color":"family"},{"title":"1999","text":"作家的忏悔","color":"main"},{"title":"赎罪","text":"虚构与真相","color":"gold"}]}
},
"huangyezhentan": {
  "id":"huangyezhentan","title":"荒野侦探","original_title":"Los detectives salvajes（The Savage Detectives）","region":"智利","era":"现当代","era_detail":"20世纪末",
  "genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"bolano","author_name":"罗贝托·波拉尼奥",
  "year_display":"1998年出版（Britannica：Los detectives salvajes (1998; The Savage Detectives)）","year_sort":1998,
  "background":["Britannica：'Bolaño's breakthrough work was Los detectives salvajes (1998)……The novel made Bolaño a literary star throughout Latin America'（突破之作、使其成为拉美文学明星）并获罗慕洛·加列戈斯奖（B251）。","作者：21世纪初南美文学领军人物之一（Britannica：one of the leading South American literary figures at the turn of the 21st century）。"],
  "outline":["三段结构：墨西哥城的'现实以下主义'诗人闯荡——寻找女诗人塞萨雷亚· Tinajero 的足迹——跨越二十年的口述接力（通说待核）。","中间部：以数十位口述者讲述两位'侦探'的漂泊（通说待核）。"],
  "characters":[{"name":"胡安与乌利塞斯","identity":"文学侦探","note":"虚构诗人（通说待核）"},{"name":"塞萨雷亚·蒂纳赫罗","identity":"消失的女诗人","note":"寻访对象（通说待核）"}],
  "themes":["文学浪游与暴力年代（通说）。",
   "口述接力：'侦探'的真相永不可得（通说）。",
   "一代诗人的挽歌（通说）。"],
  "influence":[{"text":"Britannica：获罗慕洛·加列戈斯奖、使其成为拉美文学明星（B251）。","source":"B251"},
   {"text":"《2666》身后出版奠定世界声誉（Britannica：magnum opus, 2666 (2004)）。","source":"B251"}],
  "reading":{"difficulties":["口述者众多——先列名单。","拉美诗歌史影射。"],
   "editions":["《荒野侦探》（上海人民出版社，通说待核）。"],
   "order":"先本作后《2666》；对照《百年孤独》的口述史。"},
  "pending":["中译本信息核对。","现实以下主义（infrarrealismo）细节待核。","圣特雷莎与《2666》的关系待核。"],
  "sources":["B251"],"year_source":"B251","author_source":"B251","related_works":["bainian","chengshiyugou","huoluan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《荒野侦探》口述接力图",
    "cards":[{"title":"1975墨西哥","text":"诗人闯荡","color":"family"},{"title":"寻访","text":"消失的女诗人","color":"main"},{"title":"口述接力","text":"数十个声音","color":"gold"},{"title":"荒野","text":"文学的尽头","color":"plain"}]}
},
"fengzhonglvli": {
  "id":"fengzhonglvli","title":"风中绿李","original_title":"Herztier（The Land of Green Plums）","region":"德国","era":"现当代","era_detail":"20世纪末",
  "genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"muller","author_name":"赫塔·米勒",
  "year_display":"1994年出版（Britannica：Herztier (1994) was published as The Land of Green Plums）","year_sort":1994,
  "background":["Britannica：米勒获2009年诺贝尔文学奖——'诗歌的凝练与散文的率真'描绘'the landscape of the dispossessed'（被剥夺者的风景——B252）。","主题（B252）：'totalitarianism and exile'（极权与流放）'pervade her work'；《风中绿李》获国际IMPAC都柏林文学奖（1998）（B252）。"],
  "outline":["罗马尼亚德语少数族裔大学生群：友谊、告密、逃亡（通说待核）。"," Lola 之死与'风中的绿李'意象——被剥夺者的记忆（通说待核）。"],
  "characters":[{"name":"无名叙述者","identity":"大学生","note":"'我们'的凝练（通说待核）"},{"name":"罗拉","identity":"同学","note":"自杀的起点（通说待核）"}],
  "themes":["极权与流放（B252：totalitarianism and exile）。",
   "语言即抵抗：'每个人的词语携带着自己的秘密警察'（表述待核）。",
   "物件的变形记忆（通说待核）。"],
  "influence":[{"text":"Britannica：2009诺奖授奖词——'the concentration of poetry and the frankness of prose'（B252）。","source":"B252"},
   {"text":"国际IMPAC都柏林文学奖（1998）（B252）。","source":"B252"}],
  "reading":{"difficulties":["罗马尼亚语境（齐奥塞斯库时代）注释。","凝练诗化的断裂句法。"],
   "editions":["《风中绿李》（译林出版社，通说待核）。","德文原版（Rowohlt，通说待核）。"],
   "order":"对照《古拉格群岛》：两种极权书写。"},
  "pending":["中译本信息核对。","Herztier 原义与英译差异待核。","秘密警察'Papi'人物线待核。"],
  "sources":["B252"],"year_source":"B252","author_source":"B252","related_works":["gulage","anhunqu","renjianshige"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《风中绿李》极权记忆图",
    "cards":[{"title":"大学","text":"告密的年代","color":"antagonist"},{"title":"友谊","text":"德语 minority（通说）","color":"family"},{"title":"绿李","text":"被剥夺者的风景","color":"main"},{"title":"流亡","text":"1987西德（B252）","color":"gold"}]}
},
"ershoushijian": {
  "id":"ershoushijian","title":"二手时间","original_title":"Время секонд хэнд（Secondhand Time）","region":"白俄罗斯","era":"现当代","era_detail":"21世纪",
  "genre":"口述实录","genre_group":"散文","language":"俄语","author_id":"alexievich","author_name":"斯韦特兰娜·阿列克谢耶维奇",
  "year_display":"2013年出版（Britannica：Secondhand Time (2013)）","year_sort":2013,
  "background":["Britannica：'Vremya sekond chend'（2013）——记录苏联解体后的'红色人'生活（语境转述）；方法（B253）：'hybrid literary genre that evolved as the closest possible approximation to real life'。","诺奖授奖词（B253）：'for her polyphonic writings, a monument to suffering and courage in our time'。"],
  "outline":["上卷'启示录的慰藉'与下卷'空空的装饰'（卷名通说待核）：苏联解体后20年的普通人自白（通说待核）。","'革命'的街头与厨房：'二手'的岁月（通说待核）。"],
  "characters":[{"name":"受访者群","identity":"普通人","note":"让人的声音自己讲述（B253）"}],
  "themes":["'人类情感的历史'（B253：a history of human feelings）。",
   "红色世纪的'二手时间'：理想与幻灭（通说）。",
   "复调：无权威叙述者（B253：polyphonic writings）。"],
  "influence":[{"text":"Britannica：2015年诺奖——'a monument to suffering and courage in our time'（B253）。","source":"B253"},
   {"text":"口述文学文类的世界影响（通说）。","source":"B253"}],
  "reading":{"difficulties":["口述体——多人称切换。","苏联解体（1991）背景注释。"],
   "editions":["《二手时间》（中信出版社，通说待核）。"],
   "order":"对照《古拉格群岛》：从档案到声音的两种记录。"},
  "pending":["卷名与篇目核对。","'红色人'（red man）概念核对。","中译本（中信2016说）核对。"],
  "sources":["B253"],"year_source":"B253","author_source":"B253","related_works":["gulage","riwage","zhanzheng"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《二手时间》复调结构图",
    "cards":[{"title":"厨房自白","text":"理想与幻灭","color":"main"},{"title":"街头革命","text":"1991之后","color":"antagonist"},{"title":"复调","text":"无权威叙述（B253）","color":"gold"},{"title":"情感史","text":"人的声音","color":"family"}]}
},
"baizaoyin": {
  "id":"baizaoyin","title":"白噪音","original_title":"White Noise","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"delillo","author_name":"唐·德里罗",
  "year_display":"1985年出版（Britannica：White Noise (1985; film 2022)）","year_sort":1985,
  "background":["Britannica：'White Noise (1985; film 2022), which won the National Book Award for fiction, tells of a professor of Hitler studies'（全国图书奖小说奖；写一位'希特勒研究'教授——B254）。","主题（B254）：'the anomie of an America cosseted by material excess'（被物质过剩娇惯的美国之失范）。"],
  "outline":["杰克·格拉迪尼：'希特勒研究'教授与'空中毒物事件'——化学品泄漏引发的疏散（通说）。","超市、电视与药丸：家庭的'白噪音'日常（通说）。","'最令人惧怕的是死亡'：SIMUVAC 演习与'戴乐儿'药（通说待核）。"],
  "characters":[{"name":"杰克·格拉迪尼","identity":"教授","note":"希特勒研究系主任（B254）"},{"name":"芭比特","identity":"妻子","note":"交换药物（通说待核）"}],
  "themes":["物质过剩中的失范（B254：anomie）。",
   "媒体与死亡的'白噪音'（通说）。",
   "消费社会的末日日常（通说）。"],
  "influence":[{"text":"Britannica：全国图书奖小说奖（1985）（B254）。","source":"B254"},
   {"text":"《地下世界》（1997）为其最受赞誉之作（B254 语境）。","source":"B254"}],
  "reading":{"difficulties":["后现代戏仿（学术讲座/超市清单）。","'空中毒物事件'的媒介叙事。"],
   "editions":["《白噪音》（译林出版社？中译本信息待核）。"],
   "order":"对照《五号屠场》：黑色幽默的两代。"},
  "pending":["中译本信息核对。","SIMUVAC/'戴乐儿'（Dylar）情节核对。","2022年电影（诺亚·鲍姆巴赫——Britannica 已载）细节待核。"],
  "sources":["B254"],"year_source":"B254","author_source":"B254","related_works":["wuhao","meilixinshijie","yijiubasi"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《白噪音》失范三景图",
    "cards":[{"title":"超市","text":"物质的白噪音","color":"main"},{"title":"毒雾","text":"泄漏与疏散","color":"antagonist"},{"title":"希特勒研究","text":"学术戏仿（B254）","color":"gold"},{"title":"怕死","text":"家庭的药","color":"plain"}]}
},
"kafuxuan": {
  "id":"kafuxuan","title":"当我们谈论爱情时我们在谈论什么","original_title":"What We Talk About When We Talk About Love（卡佛短篇集）","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"短篇小说集","genre_group":"小说","language":"英语","author_id":"carver","author_name":"雷蒙德·卡佛",
  "year_display":"1981年出版（Britannica：What We Talk About When We Talk About Love (1981)）","year_sort":1981,
  "background":["Britannica：卡佛'stripped-down, minimalist prose style is remarkable for its honesty and power'（削减到极简的文体以诚实与力量著称——B255）；风格'受海明威与贝克特影响——spare and flat but powerfully suggestive'（B255）。","被视为20世纪晚期英语短篇小说复兴的关键人物（B255：helping revitalize the English-language short story）。"],
  "outline":["十七篇（篇数通说待核）：《当我们谈论爱情时我们在谈论什么》《一件事若何？》《大教堂不在本集》（集外）——旅馆房间、厨房餐桌上的对话与沉默（通说）。"],
  "characters":[{"name":"丈夫们与妻子们","identity":"底层劳动 poorer","note":"餐桌上的失语（通说）"}],
  "themes":["'极简'的诚实与力量（B255）。",
   "普通生活的不可言说（通说）。",
   "劳动 poor 的挣扎（B255：struggles of the working poor）。"],
  "influence":[{"text":"Britannica：'helping revitalize the English-language short story in the late 20th century'（B255）。","source":"B255"},
   {"text":"极简主义（minimalism）与'脏现实主义'标签（通说待核）。","source":"B255"}],
  "reading":{"difficulties":["省略的艺术——沉默大于对话。","戈登·利什编辑争议（版本学）。"],
   "editions":["《当我们谈论爱情时我们在谈论什么》（译林出版社，通说待核）。"],
   "order":"先读同名篇 →《一件很好很好的事》→ 对照《大教堂》（1984）。"},
  "pending":["篇目数量（十七篇说）核对。","利什编辑争议细节待核。","中译本信息核对。"],
  "sources":["B255"],"year_source":"B255","author_source":"B255","related_works":["qikefuxuan","mauposangxuan","maitian"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"卡佛短篇的餐桌世界",
    "cards":[{"title":"厨房餐桌","text":"对话与沉默","color":"main"},{"title":"旅馆房间","text":"漂泊的临时性","color":"family"},{"title":" Gin ","text":"酒精的窄门","color":"antagonist"},{"title":"省略","text":"极简的诚实（B255）","color":"gold"}]}
},
"tuzipaopa": {
  "id":"tuzipaopa","title":"兔子，跑吧","original_title":"Rabbit, Run","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"updike","author_name":"约翰·厄普代克",
  "year_display":"1960年出版（Britannica：Rabbit, Run (1960)）","year_sort":1960,
  "background":["Britannica：'concerns a former star athlete who is unable to recapture success when bound by marriage and small-town life'（写被婚姻与小城生活束缚的前球星无法重获成功——B256）。","兔子五书（B256）：Rabbit, Run (1960)/Rabbit Redux (1971)/Rabbit Is Rich (1981)/Rabbit at Rest (1990)/Rabbit Remembered (2001)；后两部获普利策奖。"],
  "outline":["'兔子'哈利·安斯特朗抛下怀孕妻子出逃——教练、妓女与牧师间辗转（通说）。","结局：产房外的逃离（通说待核）。","四十年后的《兔子记得》（2001）回望其死后世界（Britannica：Rabbit Remembered (2001)）。"],
  "characters":[{"name":"哈利（兔子）","identity":"前球星","note":"出逃者（B256）"},{"name":"詹妮丝","identity":"妻子","note":"怀孕（通说待核）"},{"name":"鲁丝","identity":"妓女","note":"同居者（通说待核）"}],
  "themes":["逃逸的冲动与婚姻的束缚（B256）。",
   "美国中产新教生活的身体史（通说）。",
   "五十年代到世纪末的时间编年（B256：兔子五书）。"],
  "influence":[{"text":"Britannica：两获普利策奖（1982/1990）（B256）。","source":"B256"},
   {"text":"'considered to be one of his best novels'（B256——本作）。","source":"B256"}],
  "reading":{"difficulties":["现在时叙述（通说）。","美国50年代礼俗。"],
   "editions":["《兔子，跑吧》（上海译文出版社，通说待核）。"],
   "order":"按五书顺序通读（可选只读首尾）。"},
  "pending":["中译本信息核对。","现时态叙事的评论待核。","兔子五书美国史对应（艾森豪威尔—布什）待核。"],
  "sources":["B256"],"year_source":"B256","author_source":"B256","related_works":["gaicibi","fenwangyu","zise"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《兔子，跑吧》出逃结构图",
    "cards":[{"title":"球场旧梦","text":"无法重获的成功（B256）","color":"family"},{"title":"出逃","text":"婚姻的边界","color":"main"},{"title":"教堂","text":"牧师的劝诫","color":"gold"},{"title":"产房外","text":"再次逃跑","color":"antagonist"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
