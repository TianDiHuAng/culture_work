# -*- coding: utf-8 -*-
"""v6批6：中国 8部+5作家页+5来源（金瓶梅因来源失败跳过，记BLOCKERS）"""
import json, pathlib

new_src = [
{"id":"C032","title":"洪子诚：一首诗可以从什么地方读起——读北岛早期的诗（中国作家网）","author":"中国作家网","year":"2017-05-23","url":"https://www.chinawriter.com.cn/n1/2017/0523/c404031-29294426.html","type":"官方文学机构","verified":True,"covers":["beidao","beidaoshixuan"],"note":"2026-11-20 核对：'北岛出生在1949年'、原名赵振开、北京四中；1969年后在北京一个建筑队当建筑工人、70年代初期开始写诗；1978年12月北岛、芒克等创办《今天》；《回答》初刊《今天》第1期、'次年被《诗刊》转载'；初稿1973年《告诉你吧，世界》（齐简藏手抄本说）；'告诉你吧，世界 / 我－不－相－信！'；朦胧诗五人名单（北岛舒婷顾城江河杨炼）；1986年第一本国内诗集（广州新世纪）；80年代末以来在国外"},
{"id":"C033","title":"《啼笑因缘》的命名（中华读书报）","author":"中华读书报","year":"2024-08-28","url":"https://epaper.gmw.cn/zhdsb/html/2024-08/28/nw.D110000zhdsb_20240828_2-14.htm","type":"官方媒体","verified":True,"covers":["zhanghenshui","tixiaoyinyuan"],"note":"2026-11-20 核对：'1930年，张恨水的长篇小说《啼笑因缘》连载于上海《新闻报》副刊快活林，同年又出版单行本'；'一时间家弦户诵，被誉为民国第一畅销小说'；'曾经近百次被改编为其他艺术形式'；书名辨析：张恨水1932年自述'盖弟以因缘二字，根于佛说，恐人写作姻缘，未免伤俗'；初稿两名由严独鹤择定；越剧《樊家树与沈凤喜》"},
{"id":"C034","title":"中国农村土地改革的'百科全书'——周立波《暴风骤雨》（人民日报海外版）","author":"人民日报海外版（陈进）","year":"2021-09-09","url":"http://paper.people.com.cn/rmrbhwb/html/2021-09/09/content_25878498.htm","type":"官方媒体","verified":True,"covers":["zhoulibo","baofengzhouyu"],"note":"2026-11-20 核对：'周立波（1908—1979）'；1946年10月受珠河县委委派任元宝区区委书记参加土改；'以1946年至1947年间东北土地改革为背景……土改工作队开进松花江畔的元茂屯……斗争恶霸地主韩老六'；赵玉林、郭全海、老孙头人物述评；'该书于1948年由东北书店出版后反响强烈'；'并于1951年获得斯大林文学奖金'；下卷'分马'编入中学课本；日本学者安岛彬'百科全书'评价"},
{"id":"C035","title":"论《文化苦旅》的艺术魅力（中国作家网，吴欢章）","author":"中国作家网","year":"2019-05-24","url":"http://www.chinawriter.com.cn/n1/2019/0524/c427075-31102263.html","type":"官方文学机构","verified":True,"covers":["yuqiuyu","wenhuakulu"],"note":"2026-11-20 核对：'从1992年3月进入广大读者的视线，立刻引发了阅读的热潮'；'至今累计已印行千万册以上'、'中国现代散文出版史上的奇迹'；'精神内核是呼唤文化良知的回归，构建健全人格'；《道士塔》（敦煌文物流失之痛）、《都江堰》（对比句'秦始皇筑长城的指令，雄壮、蛮吓、残忍；他筑堰的命令，智慧、仁慈、透明'）、《风雨天一阁》（'极端艰难、又极端悲怆的文化奇迹'）、《柳侯祠》（贬官文化）；语言'新颖而又平易、精准而又深刻、机智而又隽永'"},
{"id":"C036","title":"王小波的小说成功抵御了时间（中国作家网转载中国青年报）","author":"中国作家网","year":"2017-04-18","url":"http://www.chinawriter.com.cn/n1/2017/0418/c403994-29219304.html","type":"官方文学机构","verified":True,"covers":["wangxiaobo","huangjinshidai"],"note":"2026-11-20 核对：'1997年4月11日，王小波猝然离世，在此后的20年里，他的书至少被20家出版机构出版'（原载中国青年报蒋肖斌）；程耳：'20多年过去了，王小波先生的小说成功抵御了时间。他的语言与叙事中的自由，他的冷静与深情'；'他的幽默与荒诞，使他腾空而起'；《黄金时代》为'这部王小波最重要的作品'；李银河：'为我们构筑了一个绝对美好、绝对超凡脱俗的精神家园'"},
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
"beidao": {
  "id": "beidao", "name": "北岛", "foreign_name": "Bei Dao（北岛，本名赵振开，1949— ）",
  "country": "中国", "birth": 1949, "death": None, "birth_year": 1949, "death_year": None, "era": "现当代",
  "summary": "北岛，本名赵振开，北京人——'北岛出生在1949年，就是通常所说的共和国的同龄人'（中国作家网 C032 洪子诚讲座）。'文革'初期参加过红卫兵运动后成为'逍遥派'，1969年后在北京一个建筑队当建筑工人，70年代初期开始写诗（C032）。1978年12月与芒克等创办《今天》——因非正式出版被称'民间刊物'（C032）。朦胧诗代表诗人（C032 五人名单之首：'北岛，舒婷，顾城、江河，杨炼'）；其诗争议最大——批评一为'晦涩，难懂'，一为感情'颓废''悲观主义''虚无主义'（C032）。80年代末以来一直在国外（C032）。",
  "timeline": [
    {"year": 1949, "text": "生于北京（C032：出生在1949年）。", "src": "C032"},
    {"year": 1973, "text": "《回答》初稿写于1973年3月，原名《告诉你吧，世界》（C032 转齐简回忆及手抄本）。", "src": "C032"},
    {"year": 1978, "text": "12月与芒克等创办《今天》；《回答》刊于《今天》第1期，'次年被《诗刊》转载'（C032）。", "src": "C032"},
    {"year": 1986, "text": "第一本国内个人诗集由广州'新世纪'出版社出版（C032）。", "src": "C032"},
    {"year": 1989, "text": "80年代末以来离开中国大陆，一直生活在国外（C032）。", "src": "C032"}],
  "major_works": [
    {"work_id": "beidaoshixuan", "note": "诗选（本库立目）"},
    {"title": "回答", "note": "（C032：初刊《今天》第1期）"},
    {"title": "城的开篇？——不：《一切》《结局或开始》", "note": "（C032 语境：《一切》常被当作'悲观'例证）"}],
  "style": [
    "否定式、宣言式诗情：'告诉你吧，世界 / 我－不－相－信！'（C032）。",
    "意象的平行对称并置（C032：意象平行对称的并置结构——搜索口径待核）。",
    "'既有诗的意象和形式的创新，又有某种主题的确定性'（C032：好处和弱点可能都包含于此）。"],
  "status": "朦胧诗代表诗人（C032 五人名单之首）；'经典'与新诗潮内部'打倒北岛''pass北岛'的口号并存（C032）——其'经典化'与新潮内部的更迭均具文学史意义（C032）。",
  "sources": ["C032"], "dates_source": "C032",
  "pending": ["《回答》是否针对四五事件的考辨（C032：'我觉得并不是那么重要'）展开核对。", "海外版《今天》的'经典化'与活力问题（C032 已载）核对。", "诺奖提名传闻（通说）待核。"]
},
"zhanghenshui": {
  "id": "zhanghenshui", "name": "张恨水", "foreign_name": "Zhang Henshui（张恨水，本名张心远，1895—1967，生卒通说待核）",
  "country": "中国", "birth": 1895, "death": 1967, "birth_year": 1895, "death_year": 1967, "era": "现当代",
  "summary": "张恨水，通俗章回小说大家（'民国第一写手'之誉——通说待核）。《啼笑因缘》1930年'连载于上海《新闻报》副刊快活林，同年又出版单行本'，'一时间家弦户诵，被誉为民国第一畅销小说'（中华读书报 C033）；'曾经近百次被改编为其他艺术形式'（C033）。书名辨析：张恨水1932年自述'盖弟以因缘二字，根于佛说，恐人写作姻缘，未免伤俗'（C033）。另有《春明外史》《金粉世家》等（通说待核）。",
  "timeline": [
    {"year": 1895, "text": "生于安徽潜山（1895年5月18日说——通说待核）。", "src": "C033"},
    {"year": 1930, "text": "《啼笑因缘》连载并出版单行本（中华读书报 C033）。", "src": "C033"},
    {"year": 1932, "text": "为书名'因缘/姻缘'作说明（C033 转引张恨水自述）。", "src": "C033"},
    {"year": 1967, "text": "卒（1967年2月15日说——通说待核）。", "src": "C033"}],
  "major_works": [
    {"work_id": "tixiaoyinyuan", "note": "长篇（C033：1930）"},
    {"title": "春明外史、金粉世家", "note": "（通说待核）"},
    {"title": "八十一梦、巴山夜雨", "note": "（通说待核）"}],
  "style": [
    "报人小说：连载体与市井读者（C033 语境）。",
    "'因缘'的佛家语：不写'姻缘'写'离合'（C033 转引张恨水自述）。",
    "章回体的现代转化（通说待核）。"],
  "status": "以《啼笑因缘》'家弦户诵'（C033）；鸳鸯蝴蝶派代表作家之定位（通说待核——学界对其'引雅入俗'的再评价见研究界口径）。",
  "sources": ["C033"], "dates_source": "C033",
  "pending": ["生卒年（1895—1967）与安徽潜山籍贯核对。", "'民国第一写手'评语出处待核。", "与严独鹤的合作（初稿两名由严择定——C033 已载）展开核对。"]
},
"zhoulibo": {
  "id": "zhoulibo", "name": "周立波", "foreign_name": "Zhou Libo（周立波，1908—1979）",
  "country": "中国", "birth": 1908, "death": 1979, "birth_year": 1908, "death_year": 1979, "era": "现当代",
  "summary": "周立波（人民日报海外版 C034：'周立波（1908—1979）'），湖南益阳人（通说待核）。1946年10月'受中共珠河（尚志）县委的委派到元宝区任区委书记，参加当地的土地改革运动'（C034）；据此写成《暴风骤雨》（1948年东北书店出版，'反响强烈'——C034）；1951年获斯大林文学奖金（C034）。另有《山乡巨变》等（通说待核）。'南周北赵'（与赵树理并称——通说待核）。",
  "timeline": [
    {"year": 1908, "text": "生于湖南益阳（1908年说——C034 载生卒；益阳籍贯通说待核）。", "src": "C034"},
    {"year": 1946, "text": "10月赴东北参加土改，任元宝区区委书记（C034）。", "src": "C034"},
    {"year": 1948, "text": "《暴风骤雨》由东北书店出版（C034）。", "src": "C034"},
    {"year": 1951, "text": "获斯大林文学奖金（C034）。", "src": "C034"}],
  "major_works": [
    {"work_id": "baofengzhouyu", "note": "长篇（C034：1948）"},
    {"title": "山乡巨变", "note": "（通说待核）"},
    {"title": "暴风骤雨（改编影视剧、连环画、长篇评书）", "note": "（C034 语境）"}],
  "style": [
    "土改叙事的'百科全书'（C034：日本学者安岛彬评价——'对土改的很多问题都进行了解答'）。",
    "东北方言与农民口语（通说待核）。",
    "'分马'一节被编入中学语文课本（C034）。"],
  "status": "《暴风骤雨》获1951年斯大林文学奖金（C034）；在第一次全国文代会上获解放区优秀作品表彰（C034）。",
  "sources": ["C034"], "dates_source": "C034",
  "pending": ["湖南益阳籍贯与'南周北赵'称谓出处核对。", "与丁玲《太阳照在桑干河上》同获斯大林奖的届次关系待核。", "《山乡巨变》1958年说待核。"]
},
"yuqiuyu": {
  "id": "yuqiuyu", "name": "余秋雨", "foreign_name": "Yu Qiuyu（余秋雨，1946— ，生年通说待核）",
  "country": "中国", "birth": 1946, "death": None, "birth_year": 1946, "death_year": None, "era": "现当代",
  "summary": "余秋雨，当代作家、学者（通说；浙江余姚人说——通说待核）。《文化苦旅》'从1992年3月进入广大读者的视线，立刻引发了阅读的热潮'，'至今累计已印行千万册以上'，是'中国现代散文出版史上的奇迹'（中国作家网 C035）；其精神内核是'呼唤文化良知的回归，构建健全人格'（C035）。曾任上海戏剧学院院长（通说待核）。",
  "timeline": [
    {"year": 1946, "text": "生于浙江余姚（1946年8月说——通说待核）。", "src": "C035"},
    {"year": 1992, "text": "3月《文化苦旅》进入读者视线（C035）。", "src": "C035"},
    {"year": 2000, "text": "新世纪初行程（'千禧之旅'说——通说待核）。", "src": "C035"}],
  "major_works": [
    {"work_id": "wenhuakulu", "note": "散文集（C035：1992）"},
    {"title": "山居笔记、千年一叹", "note": "（通说待核）"},
    {"title": "戏剧理论史稿", "note": "学术（通说待核）"}],
  "style": [
    "'文化散文'：以学者眼光审视'人文山水'（C035：结构三类型——开放式/立体型/聚焦型）。",
    "'呼唤文化良知的回归'（C035）。",
    "语言'新颖而又平易、精准而又深刻、机智而又隽永'（C035）。"],
  "status": "《文化苦旅》为'中国现代散文出版史上的奇迹'（C035）；90年代'余秋雨热'（媒体通说待核）；其争议（'金文明咬嚼'事件等）另见评论史（通说待核）。",
  "sources": ["C035"], "dates_source": "C035",
  "pending": ["生年1946与浙江余姚籍贯核对。", "上海戏剧学院院长任职年份核对。", "《文化苦旅》初版（上海知识出版社1992年3月说）核对。"]
},
"wangxiaobo": {
  "id": "wangxiaobo", "name": "王小波", "foreign_name": "Wang Xiaobo（王小波，1952—1997，生年通说待核）",
  "country": "中国", "birth": 1952, "death": 1997, "birth_year": 1952, "death_year": 1997, "era": "现当代",
  "summary": "王小波，北京人（生年1952年5月13日说——通说待核）。'1997年4月11日，王小波猝然离世，在此后的20年里，他的书至少被20家出版机构出版'（中国作家网 C036 转载中国青年报）。导演程耳：'20多年过去了，王小波先生的小说成功抵御了时间。他的语言与叙事中的自由，他的冷静与深情'、'他的幽默与荒诞，使他腾空而起，时至今日，仍然俯视着今天的时代'（C036）；李银河评价：他'为我们构筑了一个绝对美好、绝对超凡脱俗的精神家园'（C036）。",
  "timeline": [
    {"year": 1952, "text": "生于北京（1952年5月13日说——通说待核）。", "src": "C036"},
    {"year": 1992, "text": "《黄金时代》出版（1992年华夏出版社说——通说待核）。", "src": "C036"},
    {"year": 1997, "text": "4月11日猝然离世（C036）。", "src": "C036"}],
  "major_works": [
    {"work_id": "huangjinshidai", "note": "中篇/小说集（C036：'王小波最重要的作品'）"},
    {"title": "青铜时代、白银时代", "note": "（时代三部曲——通说待核）"},
    {"title": "沉默的大多数、一只特立独行的猪", "note": "杂文（通说待核）"}],
  "style": [
    "'他的语言与叙事中的自由，他的冷静与深情'（C036 程耳）。",
    "'他的幽默与荒诞，使他腾空而起'（C036）。",
    "直面身体的时代书写（C036：'去除了这些风一刮就能吹走的时代精神，直面身体'）。"],
  "status": "'王小波的小说成功抵御了时间'（C036 标题）；身后'至少被20家出版机构出版'（C036）——其接受史是90年代文学的重要现象（通说）。",
  "sources": ["C036"], "dates_source": "C036",
  "pending": ["生年1952年5月13日与逝世细节（心脏病说）核对。", "《黄金时代》1991年台湾《联合报》文学奖说待核。", "'时代三部曲'总名出处待核。"]
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
"beidaoshixuan": {
  "id":"beidaoshixuan","title":"北岛诗选","original_title":"北岛诗选（通行选集）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（白话自由体）","author_id":"beidao","author_name":"北岛（赵振开）",
  "year_display":"诗作于1970年代以来；第一本国内诗集1986年（中国作家网 C032：广州'新世纪'出版社）","year_sort":1978,
  "background":["中国作家网（C032）：1978年12月北岛、芒克等创办《今天》；《回答》初刊《今天》第1期、'次年被《诗刊》转载'。","朦胧诗定位（C032）：五人名单'北岛，舒婷，顾城、江河，杨炼'之首；'既有诗的意象和形式的创新，又有某种主题的确定性'。"],
  "outline":["《回答》：'告诉你吧，世界 / 我－不－相－信！'（C032）——否定式、宣言式诗情的典型。","《一切》常被当作'悲观'例证（C032）。","其他：《结局或开始》《雨夜》等（通说待核）。"],
  "characters":[{"name":"抒情主体","identity":"怀疑者","note":"'我不相信'的声音（C032）"}],
  "themes":["怀疑与见证（C032：否定式宣言）。",
   "'冷抒情'的意象系统（通说待核）。",
   "朦胧诗的'经典化'与新潮内部的更迭（C032：'打倒北岛'口号）。"],
  "influence":[{"text":"中国作家网：朦胧诗五人名单之首；其争议'晦涩''颓废'批评与'经典'地位并存（C032）。","source":"C032"},
   {"text":"中国作家网：《今天》'民间刊物'对新诗潮的启动（C032）。","source":"C032"}],
  "reading":{"difficulties":["意象的复义。","70年代语境的缺失。"],
   "editions":["《北岛诗选》（新世纪出版社1986年——C032 口径）。"],
   "order":"先《回答》《一切》→ 对照舒婷《致橡树》（通说）读朦胧诗论争。"},
  "pending":["选本篇目核对。","《回答》写作与发表年表（C032 已载）展开核对。","海外写作时期作品（《午夜歌手》等）待核。"],
  "sources":["C032"],"year_source":"C032","author_source":"C032","related_works":["aiqing-xuan","nvshen","yecao"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"北岛诗歌结构图",
    "cards":[{"title":"回答","text":"我不相信（C032）","color":"main"},{"title":"一切","text":"'悲观'例证（C032）","color":"antagonist"},{"title":"今天","text":"1978年12月创刊","color":"gold"},{"title":"朦胧诗","text":"五人名单之首","color":"family"}]}
},
"qiqiechengqun": {
  "id":"qiqiechengqun","title":"妻妾成群","original_title":"妻妾成群（中篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"中篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"sutong","author_name":"苏童",
  "year_display":"发表年份待核（《收获》1988年说——通说待核）；苏童代表作之一（中国作家网 C015）","year_sort":1988,
  "background":["中国作家网（C015）：'其代表作包括《妻妾成群》《红粉》等中篇'——本作为苏童代表作（C015 官方口径）。","改编（通说待核）：1991年张艺谋电影《大红灯笼高高挂》。"],
  "outline":["颂莲嫁入陈家：四房姨太太的庭院战争（通说待核）。","雁儿、毓如、卓云与'死人井'（通说待核）。"],
  "characters":[{"name":"颂莲","identity":"四姨太","note":"女大学生嫁入（通说待核）"},{"name":"陈佐千","identity":"老爷","note":"封建家长（通说待核）"}],
  "themes":["旧式庭院的女人们（通说）。",
   "阴冷的意象主义笔法（通说）。",
   "先锋与写实的中间形态（通说待核）。"],
  "influence":[{"text":"中国作家网：列为苏童代表作（C015）。","source":"C015"},
   {"text":"改编电影获威尼斯银狮奖与奥斯卡提名（1991年——通说待核）。","source":"C015"}],
  "reading":{"difficulties":["庭院空间的心理化。","先锋笔法与旧白话的杂糅。"],
   "editions":["《妻妾成群》（上海译文出版社/人民文学出版社版本，通说待核）。"],
   "order":"对照《黄雀记》：香椿树街内外。"},
  "pending":["初刊（《收获》1988年第6期说）与发表年份核对。","颂莲人名与情节细节核对。","电影改编获奖细节待核。"],
  "sources":["C015"],"year_source":"C015","author_source":"C015","related_works":["huangqueji","hongzi","jinsuoji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《妻妾成群》庭院结构图",
    "cards":[{"title":"颂莲","text":"第四房太太","color":"main"},{"title":"陈家花园","text":"井的恐惧","color":"antagonist"},{"title":"雁儿","text":"丫头的敌意","color":"gold"},{"title":"点灯","text":"捶脚与点灯","color":"family"}]}
},
"tixiaoyinyuan": {
  "id":"tixiaoyinyuan","title":"啼笑因缘","original_title":"啼笑因缘（长篇小说，二十二回）","region":"中国","era":"现当代","era_detail":"现代",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话·章回体）","author_id":"zhanghenshui","author_name":"张恨水",
  "year_display":"1930年连载于上海《新闻报》副刊'快活林'，同年出版单行本（中华读书报 C033）","year_sort":1930,
  "background":["中华读书报（C033）：'1930年，张恨水的长篇小说《啼笑因缘》连载于上海《新闻报》副刊快活林，同年又出版单行本'；'一时间家弦户诵，被誉为民国第一畅销小说'；'曾经近百次被改编为其他艺术形式'。","书名（C033）：张恨水1932年自述'盖弟以因缘二字，根于佛说，恐人写作姻缘，未免伤俗'——'啼、笑、恩、怨、亲、仇交织的离合'。"],
  "outline":["樊家树与鼓姬沈凤喜、侠女关秀姑、何丽娜的多角情缘（人物关系通说待核；C033 载越剧《樊家树与沈凤喜》）。","军阀势力拆散姻缘——凤喜的悲剧（通说待核）。"],
  "characters":[{"name":"樊家树","identity":"青年学生","note":"平权婚恋观（通说待核）"},{"name":"沈凤喜","identity":"鼓姬","note":"被军阀夺走（通说待核）"},{"name":"关秀姑","identity":"侠女","note":"豪侠线（通说待核）"}],
  "themes":["章回体与新媒载（报纸连载）的结合（C033）。",
   "'啼笑'的悲喜剧结构：啼笑因缘皆佛家'因缘'（C033）。",
   "通俗文学的现代高峰（C033：近百次改编）。"],
  "influence":[{"text":"中华读书报：'家弦户诵，被誉为民国第一畅销小说'；近百次改编（C033）。","source":"C033"},
   {"text":"中华读书报：初稿两名由严独鹤择定——报人与作家的协作机制（C033）。","source":"C033"}],
  "reading":{"difficulties":["章回套语与旧京风物。","通俗文学与'新文学'的价值等级（研究界再评价）。"],
   "editions":["《啼笑因缘》（人民文学出版社版本，通说待核）。"],
   "order":"对照《骆驼祥子》：1930年代北平的两种书写。"},
  "pending":["二十二回回目核对。","樊家树/沈凤喜/关秀姑/何丽娜情节核对。","1931年电影版权纠纷（C033 搜索口径）待核。"],
  "sources":["C033"],"year_source":"C033","author_source":"C033","related_works":["luotuo","ziye","chaguan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《啼笑因缘》三女一男结构图",
    "cards":[{"title":"沈凤喜","text":"鼓姬的悲剧","color":"main"},{"title":"关秀姑","text":"侠女之义","color":"gold"},{"title":"何丽娜","name":"","identity":"","note":"","text":"摩登小姐（通说）","color":"family"},{"title":"因缘","text":"佛说的离合（C033）","color":"plain"}]}
},
"baofengzhouyu": {
  "id":"baofengzhouyu","title":"暴风骤雨","original_title":"暴风骤雨（长篇小说）","region":"中国","era":"现当代","era_detail":"现代",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话·东北方言）","author_id":"zhoulibo","author_name":"周立波",
  "year_display":"1948年由东北书店出版（人民日报海外版 C034）；1951年获得斯大林文学奖金（C034）","year_sort":1948,
  "background":["人民日报海外版（C034）：周立波1946年10月'受中共珠河（尚志）县委的委派到元宝区任区委书记，参加当地的土地改革运动'；小说'以1946年至1947年间东北土地改革为背景，叙述了土改工作队开进松花江畔的元茂屯，发动和组织广大贫苦农民斗争恶霸地主韩老六'。","评价（C034）：日本学者安岛彬称其为描写中国农村土地改革的'百科全书'式的作品。","与丁玲《太阳照在桑干河上》同为土改叙事（对照）。"],
  "outline":["工作队进元茂屯：发动贫苦农民、斗争韩老六（C034）。","赵玉林、郭全海——'深受压迫的贫苦农民，勤劳勇敢、无私无畏'（C034）；老孙头——'狡黠、落后、自私、胆小'（C034）。","下卷'分马'被编入中学语文课本（C034）。"],
  "characters":[{"name":"郭全海","identity":"农会主任","note":"贫苦农民（C034）"},{"name":"赵玉林","identity":"积极分子","note":"（C034）"},{"name":"韩老六","identity":"恶霸地主","note":"被斗争对象（C034）"},{"name":"老孙头","identity":"赶车的","note":"中间人物（C034）"}],
  "themes":["土改的'暴风骤雨'：发动与斗争（C034）。",
   "中间人物与积极人物的两级描写（C034）。",
   "解放区文学的范本（C034：文代会表彰）。"],
  "influence":[{"text":"人民日报海外版：1951年获斯大林文学奖金；'分马'入课本（C034）。","source":"C034"},
   {"text":"人民日报海外版：安岛彬'百科全书'式评价（C034）。","source":"C034"}],
  "reading":{"difficulties":["土改史语境（对照《桑干河上》）。","东北方言。"],
   "editions":["《暴风骤雨》（人民文学出版社，通说待核）。"],
   "order":"与《太阳照在桑干河上》对读：同年土改叙事的两极。"},
  "pending":["上下卷出版时间（1948/1949说）核对。","韩老六原型事件待核。","郭全海与刘桂兰情节核对。"],
  "sources":["C034"],"year_source":"C034","author_source":"C034","related_works":["sangganhe","pingfan","hongyuhei"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《暴风骤雨》土改结构图",
    "cards":[{"title":"工作队","text":"进元茂屯","color":"family"},{"title":"斗韩老六","text":"斗争恶霸（C034）","color":"main"},{"title":"分马","text":"入课本章节（C034）","color":"gold"},{"title":"老孙头","text":"中间人物","color":"plain"}]}
},
"wenhuakulu": {
  "id":"wenhuakulu","title":"文化苦旅","original_title":"文化苦旅（散文集）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"文化散文集","genre_group":"散文","language":"汉语（白话）","author_id":"yuqiuyu","author_name":"余秋雨",
  "year_display":"1992年3月进入读者视线（中国作家网 C035）；'累计已印行千万册以上'（C035）","year_sort":1992,
  "background":["中国作家网（C035）：'从1992年3月进入广大读者的视线，立刻引发了阅读的热潮'，'至今累计已印行千万册以上'，是'中国现代散文出版史上的奇迹'。","精神内核（C035）：'呼唤文化良知的回归，构建健全人格'。"],
  "outline":["《道士塔》：由王园箓墓塔写起，'将笔触伸向一个重大的历史溃疡'——敦煌文物流失之痛（C035）。","《都江堰》：对比句'秦始皇筑长城的指令，雄壮、蛮吓、残忍；他筑堰的命令，智慧、仁慈、透明'（C035）。","《风雨天一阁》：家族护书是'极端艰难、又极端悲怆的文化奇迹'（C035）；《柳侯祠》：'贬官文化'（C035）。"],
  "characters":[{"name":"行走的学者","identity":"叙述者","note":"人文山水的考察者"}],
  "themes":["文化良知的回归（C035）。",
   "'人文山水'的时间化（C035：结构三类型——开放式/立体型/聚焦型）。",
   "健全的文化人格与历史使命感（C035）。"],
  "influence":[{"text":"中国作家网：印行千万册以上——'中国现代散文出版史上的奇迹'（C035）。","source":"C035"},
   {"text":"中国作家网：语言'新颖而又平易、精准而又深刻、机智而又隽永'（C035）。","source":"C035"}],
  "reading":{"difficulties":["文化散文的抒情尺度。","历史细节的可靠度（学界讨论）。"],
   "editions":["《文化苦旅》（东方出版中心/长江文艺出版社版本，通说待核）。"],
   "order":"先《道士塔》《都江堰》→《风雨天一阁》。"},
  "pending":["初版（上海知识出版社1992年3月说）核对。","《文化苦旅》新版（2014年增补说）待核。","余秋雨生年与职务核对。"],
  "sources":["C035"],"year_source":"C035","author_source":"C035","related_works":["waerdenghu","woyuditan","tangshi300"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《文化苦旅》山水人文图",
    "cards":[{"title":"道士塔","text":"敦煌之痛（C035）","color":"antagonist"},{"title":"都江堰","text":"智慧的命令","color":"main"},{"title":"天一阁","text":"悲怆的藏书楼","color":"gold"},{"title":"柳侯祠","text":"贬官文化","color":"family"}]}
},
"danaji": {
  "id":"danaji","title":"大淖记事","original_title":"大淖记事（短篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"短篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"wangzengqi","author_name":"汪曾祺",
  "year_display":"1981年发表（《中国文学》同年选译至海外——中国作家网 C014）","year_sort":1981,
  "background":["中国作家网（C014）：'《大淖记事》甫一问世，就被《中国文学》选中翻译至海外，1984年又入选英文版《当代优秀小说选》'。","中国作家网（C013）：汪曾祺'晚年凭借短篇小说《受戒》《大淖记事》等异军突起'。"],
  "outline":["大淖的风俗画：挑夫们的生活（通说待核）。","巧云与十一子：被打与'不知道为什么，她自己也尝了一口'（情节与名句待核）。"],
  "characters":[{"name":"巧云","identity":"姑娘","note":"被侮辱者（通说待核）"},{"name":"十一子","identity":"锡匠","note":"被打垂危（通说待核）"}],
  "themes":["风俗与人情（C013：人情美人性美语境）。",
   "'受戒'的姊妹篇：水乡的两幅画（通说）。",
   "民间伦理的自愈力（通说）。"],
  "influence":[{"text":"中国作家网：1981年被《中国文学》选译海外、1984年入选英文选集（C014）。","source":"C014"},
   {"text":"中国作家网：与《受戒》并提的复出代表作（C013）。","source":"C013"}],
  "reading":{"difficulties":["高邮水乡风物。","散文化结构的'淡'。"],
   "editions":["《汪曾祺全集》（人民文学出版社，通说待核）。"],
   "order":"先《受戒》后本作。"},
  "pending":["巧云/十一子人名与情节核对。","1981年发表刊物（《北京文学》说）核对。","英译篇名核对。"],
  "sources":["C014","C013"],"year_source":"C014","author_source":"C014","related_works":["shoujie","biancheng","xiangxingsanji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《大淖记事》水乡结构图",
    "cards":[{"title":"大淖","text":"挑夫的世界","color":"family"},{"title":"巧云","text":"被打与守护","color":"main"},{"title":"十一子","text":"锡匠的沉默","color":"gold"},{"title":"风俗","text":"伦理的自愈","color":"plain"}]}
},
"huangjinshidai": {
  "id":"huangjinshidai","title":"黄金时代","original_title":"黄金时代（中篇小说/小说集）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"中篇小说","genre_group":"小说","language":"汉语（白话·反讽体）","author_id":"wangxiaobo","author_name":"王小波",
  "year_display":"出版年待核（中国作家网 C036：'在此后的20年里，他的书至少被20家出版机构出版'——1992年华夏出版社说通说待核）","year_sort":1992,
  "background":["中国作家网（C036）：1997年4月11日王小波猝然离世；导演程耳评价：'20多年过去了，王小波先生的小说成功抵御了时间。他的语言与叙事中的自由，他的冷静与深情'；'他的幽默与荒诞，使他腾空而起，时至今日，仍然俯视着今天的时代'；称《黄金时代》为'这部王小波最重要的作品'。","李银河评价（C036）：他'为我们构筑了一个绝对美好、绝对超凡脱俗的精神家园'。"],
  "outline":["云南插队的王二与陈清扬：以'交代材料'的荒诞文体写性与自由（通说待核）。","名句：'那一天我二十一岁，在我一生的黄金时代'（通说待核——原文核对）。"],
  "characters":[{"name":"王二","identity":"知青","note":"反讽的叙述者（通说待核）"},{"name":"陈清扬","identity":"医生","note":"'破鞋'的自辩（通说待核）"}],
  "themes":["'对抗'的逻辑：从荒诞交代中夺回真实（通说）。",
   "身体的直视（C036：'直面身体'）。",
   "自由叙事的汉语可能（C036：语言与叙事中的自由）。"],
  "influence":[{"text":"中国作家网：程耳'王小波的小说成功抵御了时间'；《黄金时代》为'王小波最重要的作品'（C036）。","source":"C036"},
   {"text":"中国作家网：身后'至少被20家出版机构出版'的接受史（C036）。","source":"C036"}],
  "reading":{"difficulties":["反讽文体与'交代材料'的戏仿。","知青年代背景。"],
   "editions":["《黄金时代》（花城出版社，通说待核）。"],
   "order":"先本作 →《白银时代》《青铜时代》（时代三部曲）。"},
  "pending":["初刊（台湾《联合报》1991年文学奖说）与大陆出版年核对。","名句原文逐字核对。","陈清扬/王二人名核对。"],
  "sources":["C036"],"year_source":"C036","author_source":"C036","related_works":["huozhe","qinqiang","exin"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《黄金时代》反讽结构图",
    "cards":[{"title":"交代材料","text":"荒诞的文体","color":"antagonist"},{"title":"王二与陈清扬","text":"性与自由","color":"main"},{"title":"二十一岁","text":"黄金时代的自白","color":"gold"},{"title":"抵御时间","text":"身后经典化（C036）","color":"family"}]}
},
"xiaobaozhuang": {
  "id":"xiaobaozhuang","title":"小鲍庄","original_title":"小鲍庄（中篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"中篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"wanganyi","author_name":"王安忆",
  "year_display":"1985年出版（英文维基 B216：Baotown (1985)）；获第四届全国中篇小说奖（B216）","year_sort":1985,
  "background":["英文维基（B216）：'In Baotown (1985), Wang focused on the culture of rural China, drawing from her own experience'——转向乡土中国文化；获第四届全国中篇小说奖（B216 获奖列表）。","英文名著（B216 转述评论）：仁善的孩童主角与'自私、偏见的残酷和封闭的成年村民'的对照（'benevolent child protagonist is contrasted with selfish, prejudicial, cruel and close-minded adult villagers'）。"],
  "outline":["小鲍庄的'仁义'传统与涝渣（鲍仁文）之死（人物名与情节通说待核）。","'仁义'神话的解构（通说待核）。"],
  "characters":[{"name":"捞渣（鲍仁文）","identity":"孩童","note":"仁义的化身（通说待核）"},{"name":"鲍彦山一家","identity":"村民","note":"（通说待核）"}],
  "themes":["'仁义'文化的审视（B216：rural China culture）。",
   "孩童与成人的对照（B216：benevolent child protagonist）。",
   "寻根文学的乡土书写（B216 语境：王安忆'写于中国'的决定）。"],
  "influence":[{"text":"英文维基：获第四届全国中篇小说奖（1987年颁奖）（B216）。","source":"B216"},
   {"text":"英文维基：转引评论——'words that carry not the least hint of subjectivity'（不以主观色彩的语言）（B216 转引 Ying Hong）。","source":"B216"}],
  "reading":{"difficulties":["'仁义'话语的反讽。","多人物群像。"],
   "editions":["《小鲍庄》（人民文学出版社/上海文艺出版社版本，通说待核）。"],
   "order":"对照《爸爸爸》（韩少功——通说）：寻根文学的两幅面孔。"},
  "pending":["捞渣/鲍仁文人名与情节核对。","第四届全国中篇小说奖颁奖年份核对。","'寻根'标签与作者的疏离待核。"],
  "sources":["B216"],"year_source":"B216","author_source":"B216","related_works":["huozhe","pingfan","qiqiechengqun"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《小鲍庄》仁义结构图",
    "cards":[{"title":"小鲍庄","text":"'仁义'之庄","color":"family"},{"title":"捞渣","text":"孩童的仁义（B216）","color":"main"},{"title":"洪水","text":"牺牲与神话","color":"gold"},{"title":"解构","text":"仁义的背面","color":"antagonist"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
