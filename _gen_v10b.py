# -*- coding: utf-8 -*-
"""v10批B：枕草子/塔杜施先生/你往何处去/樱桃园 + 4作家页 + 4来源"""
import json, pathlib

new_src = [
{"id":"B267","title":"Sei Shonagon — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Sei-Shonagon","type":"百科全书","verified":True,"covers":["seishonagon","zhencaozi"],"note":"2026-11-20 核对：c.966日本生—c.1025卒；约993—1000年侍奉中宫定子（'service of the empress Teishi (Sadako) at the capital of Heian-kyo'）；'her witty, learned Pillow Book (Makura no soshi) exhibits a brilliant and original Japanese prose style'；'the best source of information on Japanese court life in the Heian period (794–1185)'；紫式部日记称其自负（'declared Sei Shonagon conceited'）；英译：Arthur Waley (1929)、Ivan Morris (1967)"},
{"id":"B268","title":"Adam Mickiewicz (Polish poet) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Adam-Mickiewicz-Polish-poet","type":"百科全书","verified":True,"covers":["mickiewicz","tadushixiansheng"],"note":"2026-11-20 核对：1798-12-24生—1855-11-26卒（56岁）；'one of Poland's greatest Romantic poets'；1823年因爱国活动被流放俄国；'Mickiewicz's masterpiece, the great epic poem Pan Tadeusz (1834)'——两大贵族家族的世仇写波兰绅士生活；'came to epitomize the Polish spirit'"},
{"id":"B269","title":"Henryk Sienkiewicz — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Henryk-Sienkiewicz","type":"百科全书","verified":True,"covers":["sienkiewicz","niwanghechuqu"],"note":"2026-11-20 核对：1846-05-05 Wola Okrzejska生—1916-11-15瑞士Vevey卒；1905年诺贝尔文学奖；Quo Vadis?——'a historical novel set in Rome under Nero, which established Sienkiewicz's international reputation'；'Sienkiewicz's great trilogy of historical novels began to appear in Slowo in 1883'"},
{"id":"B270","title":"Anton Chekhov — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Anton-Chekhov","type":"百科全书","verified":True,"covers":["chikefu","yingtaoyuan"],"note":"2026-11-20 核对：1860-01-29（儒历1月17日）塔甘罗格生—1904-07-14/15巴登维勒卒；'master of the modern short story'；'known for the principle in drama called Chekhov's gun'（每个元素都必须服务于情节）；'what is left unsaid seems much more important than what is said'；《樱桃果园》1904年——'a poignant picture of Russian landowners in decline'，1904年1月17日莫斯科首演、约六个月后作者死于肺疾"},
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
"seishonagon": {
  "id": "seishonagon", "name": "清少纳言", "foreign_name": "Sei Shōnagon（清少纳言，约966—约1025）",
  "country": "日本", "birth": 966, "death": 1025, "birth_year": 966, "death_year": 1025, "era": "古代",
  "summary": "清少纳言，平安时代女官、日记作者与歌人——'her witty, learned Pillow Book (Makura no soshi) exhibits a brilliant and original Japanese prose style'（机智博学的《枕草子》展现灿烂而独创的日本散文风格——Britannica）；'It is also the best source of information on Japanese court life in the Heian period (794–1185)'（平安朝宫廷生活的最佳史料——Britannica）。约993—1000年侍奉中宫定子（Britannica）；紫式部日记称其自负（Britannica：who herself declared Sei Shonagon conceited）。",
  "timeline": [
    {"year": 966, "text": "约生于日本（Britannica：Born c. 966, Japan）。", "src": "B267"},
    {"year": 993, "text": "入中宫定子（Sadako）宫中服务至1000年（Britannica：from about 993 to 1000）。", "src": "B267"},
    {"year": 1000, "text": "《枕草子》主要写作期（与定子宫廷同步——通说待核）。", "src": "B267"},
    {"year": 1025, "text": "约卒（Britannica：died c. 1025）。", "src": "B267"}],
  "major_works": [
    {"work_id": "zhencaozi", "note": "随笔集（Britannica：'brilliant and original Japanese prose style'）"},
    {"title": "清少纳言集", "note": "和歌集（通说待核）"}],
  "style": [
    "'brilliant and original Japanese prose style'（B267）。",
    "'机智、博学'（B267：witty, learned）。",
    "段拾式随笔：'春，曙为最'式的 listing（通说待核）。"],
  "status": "Britannica 定位清少纳言为平安朝随笔与歌人、《枕草子》作者——古典日本散文的杰作与平安宫廷生活的最佳史料（B267）；与紫式部并称（两人互评——B267）。",
  "sources": ["B267"], "dates_source": "B267",
  "pending": ["段落数（300余段说）核对。", "'春曙为最'首段原文核对。", "与定子中宫的进宫细节待核。"]
},
"mickiewicz": {
  "id": "mickiewicz", "name": "亚当·密茨凯维奇", "foreign_name": "Adam Mickiewicz（亚当·密茨凯维奇，1798-12-24—1855-11-26）",
  "country": "波兰", "birth": 1798, "death": 1855, "birth_year": 1798, "death_year": 1855, "era": "近代",
  "summary": "密茨凯维奇，'波兰最伟大的浪漫主义诗人之一'（Britannica：one of Poland's greatest Romantic poets），波兰民族自由的终身倡导者；1823年因爱国活动被流放俄国，后定居巴黎（Britannica）。'Mickiewicz's masterpiece, the great epic poem Pan Tadeusz (1834)'（B268）；'With his exalted patriotism, mystical feeling, and passionate appreciation of the positive aspects of Polish life, he came to epitomize the Polish spirit'（以崇高的爱国精神、神秘的情感与对波兰生活积极面的热烈珍视，成为波兰精神的化身——B268）。",
  "timeline": [
    {"year": 1798, "text": "12月24日生（Britannica：Born December 24, 1798）。", "src": "B268"},
    {"year": 1823, "text": "因爱国活动被流放俄国（Britannica：Deported to Russia in 1823）。", "src": "B268"},
    {"year": 1834, "text": "史诗《塔杜施先生》出版（Britannica：Pan Tadeusz (1834)）。", "src": "B268"},
    {"year": 1855, "text": "11月26日卒（Britannica：died November 26, 1855）。", "src": "B268"}],
  "major_works": [
    {"work_id": "tadushixiansheng", "note": "史诗（Britannica：1834，masterpiece）"},
    {"title": "先人祭", "note": "诗剧（Britannica 语境：Dziady——通说待核）"},
    {"title": "康拉德·华伦洛德", "note": "（通说待核）"}],
  "style": [
    "'崇高的爱国主义'与'神秘的情感'（B268：exalted patriotism, mystical feeling）。",
    "民族史诗的立国书写（B268：define the Polish national spirit——综述语境）。",
    "立陶宛风物与贵族世仇（B268：a feud between two noble families）。"],
  "status": "Britannica 定位密茨凯维奇为波兰最伟大的浪漫主义诗人之一、'波兰精神的化身'（B268）。",
  "sources": ["B268"], "dates_source": "B268",
  "pending": ["《先人祭》四部结构核对。", "《塔杜施先生》书名（波兰语 Pan Tadeusz 或 Thaddeus）译法待核。", "君士坦丁堡之死（霍乱说）待核。"]
},
"sienkiewicz": {
  "id": "sienkiewicz", "name": "亨利克·显克维奇", "foreign_name": "Henryk Sienkiewicz（亨利克·显克维奇，1846-05-05—1916-11-15）",
  "country": "波兰", "birth": 1846, "death": 1916, "birth_year": 1846, "death_year": 1916, "era": "近代",
  "summary": "显克维奇，波兰小说家——'best known for historical fiction'（以历史小说著称——Britannica），含17世纪波兰背景的三部曲与'internationally acclaimed'的《你往何处去？》（B269）。1905年获诺贝尔文学奖（Britannica：winner of the Nobel Prize for Literature in 1905）。'Sienkiewicz's great trilogy of historical novels began to appear in Slowo in 1883'（三部曲1883年起在《言论报》连载——B269）。",
  "timeline": [
    {"year": 1846, "text": "5月5日生于波兰（Britannica：Born May 5, 1846, Wola Okrzejska, Poland）。", "src": "B269"},
    {"year": 1883, "text": "历史小说三部曲开始在《言论报》连载（Britannica：began to appear in Slowo in 1883）。", "src": "B269"},
    {"year": 1896, "text": "《你往何处去？》出版（Britannica 语境）。", "src": "B269"},
    {"year": 1905, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1905）。", "src": "B269"},
    {"year": 1916, "text": "11月15日卒于瑞士沃韦（Britannica：Died November 15, 1916, Vevey, Switzerland）。", "src": "B269"}],
  "major_works": [
    {"work_id": "niwanghechuqu", "note": "长篇（Britannica：国际声誉之作）"},
    {"title": "三部曲（火与剑/洪流/火与剑？）", "note": "（Britannica：great trilogy——卷名待核）"},
    {"title": "十字军骑士", "note": "（通说待核）"}],
  "style": [
    "历史小说：'set in Rome under Nero'（B269——《你往何处去？》）。",
    "民族史诗的通俗叙事（B269：trilogy in Slowo）。",
    "波兰国难记忆的文学化（通说待核）。"],
  "status": "Britannica 定位显克维奇为波兰历史小说家、1905年诺奖得主（B269）。",
  "sources": ["B269"], "dates_source": "B269",
  "pending": ["三部曲卷名（火与剑/洪流/伏沃迪约夫斯基先生说）核对。", "《你往何处去？》1896年出版细节核对。", "黎诺基（Ligęzy？）人名待核。"]
},
"chikefu": {
  "id": "chikefu", "name": "安东·契诃夫", "foreign_name": "Anton Chekhov（安东·契诃夫，1860-01-29—1904-07-14/15）",
  "country": "俄国", "birth": 1860, "death": 1904, "birth_year": 1860, "death_year": 1904, "era": "近代",
  "summary": "契诃夫，塔甘罗格人，俄国剧作家与'现代短篇小说大师'（Britannica：master of the modern short story），以克制的、不动声色的写实著称（Britannica：laconic, understated realism）。医生出身（Britannica：A trained doctor）。'known for the principle in drama called Chekhov's gun'（戏剧中'契诃夫之枪'原则：故事中引入的每个元素都必须必要——Britannica）；'what is left unsaid seems much more important than what is said'（未说出的比说出的更重要——Britannica）。《樱桃果园》（1904）——'a poignant picture of Russian landowners in decline'（俄国地主没落的辛酸图景——B270），1904年1月17日莫斯科首演、约六个月后作者死于肺疾（B270）。",
  "timeline": [
    {"year": 1860, "text": "1月29日（儒历）生于塔甘罗格（Britannica）。", "src": "B270"},
    {"year": 1884, "text": "医学院毕业（Britannica：Graduated medical school 1884）。", "src": "B270"},
    {"year": 1897, "text": "肺出血（Britannica：Lung hemorrhage March 1897）。", "src": "B270"},
    {"year": 1904, "text": "1月17日《樱桃果园》莫斯科首演（B270）；7月14/15日卒于巴登维勒（B270）。", "src": "B270"}],
  "major_works": [
    {"work_id": "yingtaoyuan", "note": "戏剧（Britannica：1904）"},
    {"title": "海鸥、万尼亚舅舅", "note": "（Britannica：Uncle Vanya (1897)）"},
    {"title": "契诃夫短篇小说选", "note": "（本库另条 qikefuxuan）"}],
  "style": [
    "'契诃夫之枪'：元素的必要性（B270）。",
    "'未说出的比说出的更重要'（B270）。",
    "'deceptively simple technique'：貌似简单的技术（B270）。"],
  "status": "Britannica 定位契诃夫为现代短篇小说大师、戏剧'契诃夫之枪'原则的来源（B270）。",
  "sources": ["B270"], "dates_source": "B270",
  "pending": ["《海鸥》1896年彼得堡首演失败与1898年莫斯科艺术剧院成功说待核。", "《樱桃果园》'喜剧'标签之争待核。", "qikefuxuan 作品页与本页的关联补全。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"zhencaozi": {
  "id":"zhencaozi","title":"枕草子","original_title":"枕草子（まくらのそうし，Makura no Sōshi）","region":"日本","era":"古代","era_detail":"平安时代",
  "genre":"随笔集","genre_group":"散文","language":"日语（王朝文体）","author_id":"seishonagon","author_name":"清少纳言",
  "year_display":"约993—1000年宫廷期间写作（Britannica 语境）；定本年代通说待核","year_sort":1000,
  "background":["Britannica（B267）：'her witty, learned Pillow Book (Makura no soshi) exhibits a brilliant and original Japanese prose style'；'It is also the best source of information on Japanese court life in the Heian period (794–1185)'。","'Those qualities also won her enemies, according to the diary of her contemporary Murasaki Shikibu, who herself declared Sei Shonagon conceited'（紫式部日记称其自负——B267）。"],
  "outline":["段拾式随笔：'春，曙为最'等三百余段（段数通说待核）+ 日记部分 + 和歌（B267：vividly recounted memoirs of her impressions）。"],
  "characters":[{"name":"清少纳言","identity":"随笔作者","note":"定子女官（B267）"},{"name":"中宫定子","identity":"皇后","note":"服务的对象（B267）"}],
  "themes":["'をかし'（有趣）与'あはれ'（哀）的审美分野（通说待核）。",
   "平安宫廷生活的最佳史料（B267）。",
   "与《源氏物语》的双峰（通说——两人互评见 B267）。"],
  "influence":[{"text":"Britannica：'brilliant and original Japanese prose style'（B267）。","source":"B267"},
   {"text":"英译：Arthur Waley (1929)、Ivan Morris (1967)（B267）。","source":"B267"}],
  "reading":{"difficulties":["平安朝称谓与名物。","'段'的分立逻辑。"],
   "editions":["周作人译本（上海译文出版社《枕草子》，通说待核）。","英译（Ivan Morris 版）。"],
   "order":"先读'春曙为最'段 → 与《源氏物语》对照。"},
  "pending":["段落数核对。","周作人译本信息核对。","与紫式部的互评（B267 已载）展开核对。"],
  "sources":["B267"],"year_source":"B267","author_source":"B267","related_works":["genjiwuyu","xixue","liuyan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《枕草子》段拾结构图",
    "cards":[{"title":"春曙为最","text":"四季的段拾（通说）","color":"main"},{"title":"宫廷","text":"定子女官时代","color":"family"},{"title":"机智","text":"brilliant prose（B267）","color":"gold"},{"title":"紫式部","text":"互评的对手","color":"plain"}]}
},
"tadushixiansheng": {
  "id":"tadushixiansheng","title":"塔杜施先生","original_title":"Pan Tadeusz（即《塔杜施先生，或立陶宛的最后一次袭击》）","region":"波兰","era":"近代","era_detail":"19世纪",
  "genre":"民族史诗","genre_group":"诗歌","language":"波兰语","author_id":"mickiewicz","author_name":"亚当·密茨凯维奇",
  "year_display":"1834年出版（Britannica：Pan Tadeusz (1834)）","year_sort":1834,
  "background":["Britannica（B268）：'Mickiewicz's masterpiece, the great epic poem Pan Tadeusz (1834)'——描述'life of the Polish gentry through a feud between two noble families'；'shows the effect of the Napoleonic myth'——波兰人视法军为'从俄国统治下解放的唯一希望'。","地位（B268）：'came to epitomize the Polish spirit'。"],
  "outline":["两大贵族家族的世仇与和解——塔杜施与佐霞的爱情（通说待核）。","波诺尼茨基神父的调停与爱国教育（通说待核）。"],
  "characters":[{"name":"塔杜施","identity":"青年","note":"史诗主角（通说待核）"},{"name":"佐霞","identity":"姑娘","note":"爱情线（通说待核）"}],
  "themes":["民族史诗：世仇的和解即民族的和解（通说）。",
   "拿破仑神话（B268）。",
   "立陶宛风物的白描（通说待核）。"],
  "influence":[{"text":"Britannica：'masterpiece'；'epitomize the Polish spirit'（B268）。","source":"B268"},
   {"text":"波兰的民族圣典：卡钦斯基总统曾于克里姆林宫朗读（通说待核）。","source":"B268"}],
  "reading":{"difficulties":["波兰贵族'萨姆拉'制度。","十二卷书的结构。"],
   "editions":["《塔杜施先生》（人民文学出版社景凯旋译本？——通说待核）。","英文原版（公有领域）。"],
   "order":"对照《巴尼？》——不：对照《先人祭》读。"},
  "pending":["十二卷（Books）结构核对。","景凯旋译本信息待核。","拿破仑神话段落核对。"],
  "sources":["B268"],"year_source":"B268","author_source":"B268","related_works":["aonijin","shangweidenv'er","zhanzheng"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《塔杜施先生》世仇和解图",
    "cards":[{"title":"世仇","text":"霍莱什卡与索利茨卡（通说）","color":"antagonist"},{"title":"塔杜施","text":"青年的成长","color":"main"},{"title":"佐霞","text":"爱情的和解","color":"gold"},{"title":"波兰精神","text":"史诗的化身（B268）","color":"family"}]}
},
"niwanghechuqu": {
  "id":"niwanghechuqu","title":"你往何处去","original_title":"Quo Vadis: A Narrative of the Time of Nero","region":"波兰","era":"近代","era_detail":"19世纪末",
  "genre":"长篇历史小说","genre_group":"小说","language":"波兰语","author_id":"sienkiewicz","author_name":"亨利克·显克维奇",
  "year_display":"1896年出版（Britannica 语境；Nobel 1905）","year_sort":1896,
  "background":["Britannica（B269）：Quo Vadis?——'a historical novel set in Rome under Nero, which established Sienkiewicz's international reputation'（尼禄治下罗马的历史小说，确立其国际声誉）。","显克维奇 1905年诺奖（B269）。"],
  "outline":["罗马将军维尼兹尤斯与基督教徒莉吉亚的爱情——尼禄焚城的暴政（通说待核）。","彼得的殉道：'主往何处去'（题解通说待核）。"],
  "characters":[{"name":"维尼兹尤斯","identity":"罗马将领","note":"皈依者（通说待核）"},{"name":"莉吉亚","identity":"基督教徒","note":"爱的对象（通说待核）"},{"name":"尼禄","identity":"皇帝","note":"焚城暴君（通说待核）"}],
  "themes":["早期基督教与罗马暴政（通说）。",
   "'你往何处去'的题解（通说待核——Quo vadis, Domine）。",
   "历史小说的国际声誉（B269）。"],
  "influence":[{"text":"Britannica：确立国际声誉（established……international reputation）（B269）。","source":"B269"},
   {"text":"1905年诺贝尔文学奖（B269）。","source":"B269"}],
  "reading":{"difficulties":["尼禄罗马史。","基督教早期术语。"],
   "editions":["《你往何处去》（上海译文出版社林洪亮译本？——通说待核）。","英文原版（公有领域）。"],
   "order":"显克维奇三部曲之外的第一站。"},
  "pending":["1896年出版（波兰《新闻报》连载说）核对。","维尼兹尤斯/莉吉亚人名核对。","林洪亮译本信息待核。"],
  "sources":["B269"],"year_source":"B269","author_source":"B269","related_works":["shenqu","zhanzheng","muqin"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《你往何处去》罗马结构图",
    "cards":[{"title":"尼禄焚城","text":"暴政的狂欢","color":"antagonist"},{"title":"莉吉亚","text":"信仰的少女","color":"main"},{"title":"维尼兹尤斯","text":"爱的皈依","color":"gold"},{"title":"你往何处去","text":"彼得的回望（题解通说）","color":"family"}]}
},
"yingtaoyuan": {
  "id":"yingtaoyuan","title":"樱桃园","original_title":"Вишнёвый сад（The Cherry Orchard）","region":"俄国","era":"近代","era_detail":"20世纪初",
  "genre":"四幕喜剧（正剧之争）","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
  "year_display":"1904年莫斯科首演（Britannica：premiered in Moscow January 17, 1904）","year_sort":1904,
  "background":["Britannica（B270）：'In another great play, The Cherry Orchard (1904), Chekhov created a poignant picture of Russian landowners in decline'（俄国地主没落的辛酸图景）；首演六个月后作者死于肺疾（B270）。","文体之争（通说待核）：契诃夫称'喜剧'、斯坦尼斯拉夫斯基演成悲剧。","'契诃夫之枪'原则（B270：every element introduced in a story should be necessary to the plot）。"],
  "outline":["朗涅夫斯卡娅与樱桃园拍卖：伐木声与斧头（通说待核）。","罗巴辛买下樱桃园——'新生活'的开始（通说待核）。"],
  "characters":[{"name":"朗涅夫斯卡娅","identity":"女地主","note":"挥霍的归来者（通说待核）"},{"name":"罗巴辛","identity":"商人","note":"买主（通说待核）"},{"name":"费尔斯","identity":"老仆","note":"被遗忘者（通说待核）"}],
  "themes":["没落的辛酸图景（B270）。",
   "'喜剧'与'悲剧'的作者意图之争（通说待核）。",
   "'契诃夫之枪'（B270）。"],
  "influence":[{"text":"Britannica：'a poignant picture of Russian landowners in decline'（B270）。","source":"B270"},
   {"text":"作者页：'契诃夫之枪'（B270）。","source":"B270"}],
  "reading":{"difficulties":["'契诃夫式'的停顿与潜台词。","1904—05俄国革命前夜。"],
   "editions":["《樱桃果园》（童道明译本？——通说待核）。","英文原版（公有领域）。"],
   "order":"与《海鸥》《万尼亚舅舅》合读。"},
  "pending":["作者定名'喜剧'的说明核对。","朗涅夫斯卡娅/罗巴辛/费尔斯人名核对。","莫斯科艺术剧院演出细节待核。"],
  "sources":["B270"],"year_source":"B270","author_source":"B270","related_works":["leiyu","richu","beijingren"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《樱桃园》没落结构图",
    "cards":[{"title":"樱桃园","text":"旧贵族的象征","color":"family"},{"title":"拍卖","text":"斧头的声音","color":"antagonist"},{"title":"罗巴辛","text":"新阶级的胜利","color":"gold"},{"title":"费尔斯","text":"被遗忘的老仆","color":"main"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
