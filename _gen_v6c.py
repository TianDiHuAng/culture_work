# -*- coding: utf-8 -*-
"""v6批7：7部（3部复用已有来源+4部新核）+4作家页+4来源"""
import json, pathlib

new_src = [
{"id":"B257","title":"V.S. Naipaul — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/V-S-Naipaul","type":"百科全书","verified":True,"covers":["naipaul","bisiwosixianshengdefangzi"],"note":"2026-11-20 核对：1932-08-17特立尼达生—2018-08-11伦敦卒；2001诺贝尔奖、1971布克奖（In a Free State）；'His fourth novel, A House for Mr. Biswas (1961)……won him major recognition'；'centres on the main character's attempt to assert his personal identity and establish his independence as symbolized by owning his own house'；'For these revelations of what the Swedish Academy called suppressed histories, Naipaul won the Nobel Prize'"},
{"id":"B258","title":"Nadine Gordimer — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Nadine-Gordimer","type":"百科全书","verified":True,"covers":["gordimer","qiyuderenmin"],"note":"2026-11-20 核对：1923-11-20南非斯普林斯生—2014-07-13约翰内斯堡卒；1991诺贝尔奖；'July's People (1981), A Sport of Nature (1987), My Son's Story (1990), The House Gun (1998)'；'Her stories concern the devastating effects of apartheid on the lives of South Africans——the constant tension between personal isolation and the commitment to social justice'"},
{"id":"B259","title":"Maxim Gorky — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Maxim-Gorky","type":"百科全书","verified":True,"covers":["gorky","muqin"],"note":"2026-11-20 核对：1868-03-16（儒历）/28（公历）下诺夫哥罗德生—1936-06-18莫斯科附近卒；'Mat (1906; Mother) is probably the least successful of the novels'但'has considerable interest as Gorky's only long work devoted to the Russian revolutionary movement'；普多夫金1926年默片、布莱希特《母亲》(1930–31)；'helped found the literary method of Socialist Realism and became the first president of the Soviet Writers' Union in 1934'；'considered the greatest proletarian writer in Russian literature'；自传三部曲'one of the finest autobiographies in Russian literature'"},
{"id":"B260","title":"Czeslaw Milosz — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Czeslaw-Milosz","type":"百科全书","verified":True,"covers":["milosz","beijingudetounao"],"note":"2026-11-20 核对：1911-06-30立陶宛Šeteniai生—2004-08-14克拉科夫卒；1951年出走巴黎、1960年移居美国、1980年诺奖；'his best-known work is the essay collection The Captive Mind (1953)'，'in which he condemns the accommodation of many Polish intellectuals to communism'；授奖词'a writer who with uncompromising clear-sightedness voices man's exposed condition in a world of severe conflicts'；'Until 1980……his work was banned in Poland'；诗'noted for their classical style'"},
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
"naipaul": {
  "id": "naipaul", "name": "V.S.奈保尔", "foreign_name": "V.S. Naipaul（维迪亚达尔·苏拉杰普拉萨德·奈保尔，1932-08-17—2018-08-11）",
  "country": "英国", "birth": 1932, "death": 2018, "birth_year": 1932, "death_year": 2018, "era": "现当代",
  "summary": "奈保尔，特立尼达出生的印度裔英国小说家（Britannica：Trinidadian-British novelist of Indian descent），其小说与游记考察发展中国家的后殖民疏离（Britannica）。1950年离开特立尼达赴牛津（Britannica）。'His fourth novel, A House for Mr. Biswas (1961)……won him major recognition'（B257）；2001年获诺贝尔文学奖——'For these revelations of what the Swedish Academy called suppressed histories'（瑞典学院所称'被压抑的历史'的揭示——B257）；1971年布克奖（In a Free State）（B257）。",
  "timeline": [
    {"year": 1932, "text": "8月17日生于特立尼达（Britannica：Born August 17, 1932, Trinidad）。", "src": "B257"},
    {"year": 1950, "text": "赴牛津大学（Britannica：Left Trinidad for Oxford 1950）。", "src": "B257"},
    {"year": 1961, "text": "《毕斯沃斯先生的房子》出版（Britannica：1961）。", "src": "B257"},
    {"year": 2001, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 2001）。", "src": "B257"}],
  "major_works": [
    {"work_id": "bisiwosixianshengdefangzi", "note": "长篇（Britannica：1961）"},
    {"title": "自由国度、河湾", "note": "（Britannica 语境：1971布克奖）"},
    {"title": "印度三部曲", "note": "游记（通说待核）"}],
  "style": [
    "后殖民疏离的精确解剖（Britannica：examined postcolonial alienation）。",
    "'被压抑的历史'的揭示（B257：suppressed histories）。",
    "游记与虚构互证（通说待核）。"],
  "status": "Britannica 定位奈保尔为2001年诺奖得主、后殖民书写代表（B257）；其游记对第三世界的批评引发争议（Britannica 外链语境：NPR 'Controversial Author'——细节待核）。",
  "sources": ["B257"], "dates_source": "B257",
  "pending": ["游记争议细节（爱德华·萨义德批评说）待核。", "《毕斯沃斯先生的房子》印度教史诗结构说待核。", "骑士封号（1989——Britannica 已载）核对。"]
},
"gordimer": {
  "id": "gordimer", "name": "纳丁·戈迪默", "foreign_name": "Nadine Gordimer（纳丁·戈迪默，1923-11-20—2014-07-13）",
  "country": "南非", "birth": 1923, "death": 2014, "birth_year": 1923, "death_year": 2014, "era": "现当代",
  "summary": "戈迪默，南非小说家与短篇小说家——其小说探察种族隔离制度下南非人的流放与疏离（Britannica：explored exile and alienation under apartheid）；'Her stories concern the devastating effects of apartheid on the lives of South Africans——the constant tension between personal isolation and the commitment to social justice'（B258）。终生批判种族隔离（Britannica：A lifelong critic of racial segregation），1991年获诺贝尔文学奖（B258）。",
  "timeline": [
    {"year": 1923, "text": "11月20日生于南非斯普林斯（Britannica：Born November 20, 1923, Springs, Transvaal）。", "src": "B258"},
    {"year": 1981, "text": "《七月的人民》出版（Britannica：July's People (1981)）。", "src": "B258"},
    {"year": 1991, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1991）。", "src": "B258"}],
  "major_works": [
    {"work_id": "qiyuderenmin", "note": "长篇（Britannica：1981）"},
    {"title": "我儿子的故事、自然资源保护者", "note": "（Britannica 存目）"},
    {"title": "短篇小说集", "note": "（通说待核）"}],
  "style": [
    "种族隔离的' devastating effects'（B258）。",
    "个人疏离与社会正义承诺的张力（B258）。",
    "道德复杂性的白描（通说）。"],
  "status": "Britannica 定位戈迪默为南非小说家、1991年诺奖得主（B258）；其书曾在南非被禁（通说待核）。",
  "sources": ["B258"], "dates_source": "B258",
  "pending": ["《七月的人民》情节（革命后白人家庭避居仆人家）细节待核。", "被禁书单（《晚期资产阶级世界》等）待核。", "与库切的并称关系待核。"]
},
"gorky": {
  "id": "gorky", "name": "马克西姆·高尔基", "foreign_name": "Maxim Gorky（马克西姆·高尔基，1868-03-16/28—1936-06-18）",
  "country": "俄国", "birth": 1868, "death": 1936, "birth_year": 1868, "death_year": 1936, "era": "近代",
  "summary": "高尔基，下诺夫哥罗德人（Britannica：Born March 16 [March 28, New Style], 1868, Nizhny Novgorod），俄国作家——早期写流浪汉的小说使其成名；'considered the greatest proletarian writer in Russian literature'（被视为俄国文学最伟大的无产阶级作家——Britannica，因其童年的贫困经验）。'helped found the literary method of Socialist Realism and became the first president of the Soviet Writers' Union in 1934'（参与创立社会主义现实主义方法并任苏联作家协会首任主席——Britannica）。《母亲》（1906）——'probably the least successful of the novels'但'has considerable interest as Gorky's only long work devoted to the Russian revolutionary movement'（B259）。自传三部曲'one of the finest autobiographies in Russian literature'（B259）。",
  "timeline": [
    {"year": 1868, "text": "3月16/28日生于下诺夫哥罗德（Britannica）。", "src": "B259"},
    {"year": 1906, "text": "《母亲》出版（Britannica：Mother (1906)）。", "src": "B259"},
    {"year": 1934, "text": "任苏联作家协会首任主席（Britannica）。", "src": "B259"},
    {"year": 1936, "text": "6月18日卒于莫斯科附近（Britannica：Died June 18, 1936, near Moscow）。", "src": "B259"}],
  "major_works": [
    {"work_id": "muqin", "note": "长篇（Britannica：1906）"},
    {"title": "童年/在人间/我的大学", "note": "自传三部曲（Britannica：'one of the finest autobiographies in Russian literature'）"},
    {"title": "在底层", "note": "戏剧（Britannica：The Lower Depths (1902)）"}],
  "style": [
    "流浪汉短篇的浪漫现实主义（Britannica 语境：tramps and outcasts）。",
    "社会主义现实主义的奠基者之一（Britannica）。",
    "托尔斯泰回忆被誉为其杰作（Britannica：Gorky's memoir of Tolstoy has been acclaimed as his masterpiece）。"],
  "status": "Britannica 定位高尔基为俄国文学最伟大的无产阶级作家、社会主义现实主义奠基人之一（B259）。",
  "sources": ["B259"], "dates_source": "B259",
  "pending": ["《母亲》1906年（美国说）出版细节待核。", "死因争议（被毒杀说）待核。", "与列宁的关系（《列宁》特写）待核。"]
},
"milosz": {
  "id": "milosz", "name": "切斯瓦夫·米沃什", "foreign_name": "Czesław Miłosz（切斯瓦夫·米沃什，1911-06-30—2004-08-14）",
  "country": "波兰", "birth": 1911, "death": 2004, "birth_year": 1911, "death_year": 2004, "era": "现当代",
  "summary": "米沃什，生于立陶宛的波兰-美国诗人、小说家、译者、批评家与外交官（Britannica），其作考察压迫体制对人类精神的影响（Britannica：examined how oppressive regimes affect the human spirit）。1951年从共产党波兰出走巴黎、1960年移居美国、在伯克利执教（Britannica）。'his best-known work is the essay collection The Captive Mind (1953)'——'in which he condemns the accommodation of many Polish intellectuals to communism'（《被禁锢的头脑》谴责许多波兰知识分子对共产主义的适应——B260）。1980年获诺贝尔文学奖——授奖词：'a writer who with uncompromising clear-sightedness voices man's exposed condition in a world of severe conflicts'（B260）；'Until 1980……his work was banned in Poland'（1980年前其作品在波兰被禁——B260）。",
  "timeline": [
    {"year": 1911, "text": "6月30日生于立陶宛舍泰伊尼亚（Britannica：Born June 30, 1911, Šeteniai, Lithuania）。", "src": "B260"},
    {"year": 1951, "text": "在巴黎寻求政治庇护（Britannica：Sought political asylum in Paris 1951）。", "src": "B260"},
    {"year": 1953, "text": "《被禁锢的头脑》出版（Britannica：1953）。", "src": "B260"},
    {"year": 1980, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1980）。", "src": "B260"}],
  "major_works": [
    {"work_id": "beijingudetounao", "note": "论集（Britannica：1953）"},
    {"title": "拆散的笔记本、太阳升起处", "note": "诗集（通说待核）"},
    {"title": " Izrael？——不：《Verses》？——不：《米沃什诗选》", "note": "（通说待核）"}],
  "style": [
    "古典风格与哲思政治的关注（Britannica：classical style and their preoccupation with philosophical and political issues）。",
    "'uncompromising clear-sightedness'（B260 授奖词：毫不妥协的清醒）。",
    "波兰语的故乡书写与流亡双语（通说）。"],
  "status": "Britannica 定位米沃什为1980年诺奖得主、以《被禁锢的头脑》闻名的论者（B260）。",
  "sources": ["B260"], "dates_source": "B260",
  "pending": ["《被禁锢的头脑》四种方法（屈从者类型学）细节待核。", "伯克利斯拉夫语教授职位（1960—1980——Britannica 已载）核对。", "《诗的艺术？》——不：《米沃什词典》待核。"]
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
"zuiLandeyanjing": {
  "id":"zuiLandeyanjing","title":"最蓝的眼睛","original_title":"The Bluest Eye","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"morrison","author_name":"托妮·莫里森",
  "year_display":"1970年出版（作者页 B150 口径：最蓝的眼睛（1970））","year_sort":1970,
  "background":["作者页（B150）：莫里森代表作谱系以'最蓝的眼睛（1970）'为起点（作者页 major_works 口径）。","莫里森为诺贝尔文学奖得主（作者页 B150 定位——详见 chonger 条）。"],
  "outline":["佩科拉渴望蓝眼睛——以'最蓝的眼睛'为黑皮肤女孩的自我憎恨之镜（通说待核）。","四季结构：秋/冬/春/夏（结构通说待核）。"],
  "characters":[{"name":"佩科拉","identity":"黑人女孩","note":"渴望蓝眼（通说待核）"},{"name":"克劳迪娅","identity":"叙述者","note":"反抗的孩子视角（通说待核）"}],
  "themes":["种族内部的白人审美暴力（通说）。",
   "童年与社区的见证（通说）。",
   "'狄克与珍妮'课本的拼贴（通说待核）。"],
  "influence":[{"text":"作者页：莫里森以《宠儿》等确立其地位；《最蓝的眼睛》为处女作（B150 作者页口径）。","source":"B150"},
   {"text":"美国中学与大学课程的常读文本（通说待核）。","source":"B150"}],
  "reading":{"difficulties":["多视角叙事与课本拼贴。","1940年代俄亥俄黑人社区背景。"],
   "editions":["《最蓝的眼睛》（南海出版公司新经典版，通说待核）。"],
   "order":"先《最蓝的眼睛》后《宠儿》：莫里森的起点与巅峰。"},
  "pending":["1970年出版（Holt, Rinehart 说）核对。","佩科拉/克劳迪娅人名与四季结构核对。","'Dick and Jane'课本引文待核。"],
  "sources":["B150"],"year_source":"B150","author_source":"B150","related_works":["chonger","zise","shinv"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《最蓝的眼睛》四季结构图",
    "cards":[{"title":"秋","text":"佩科拉的愿望","color":"family"},{"title":"冬","text":"学校与秀兰·邓波儿","color":"plain"},{"title":"春","text":"父亲的伤害","color":"antagonist"},{"title":"夏","text":"蓝眼睛的疯梦","color":"main"}]}
},
"qinchaidachen": {
  "id":"qinchaidachen","title":"钦差大臣","original_title":"Ревизор（The Government Inspector）","region":"俄国","era":"近代","era_detail":"19世纪",
  "genre":"讽刺喜剧","genre_group":"戏剧","language":"俄语","author_id":"gogol","author_name":"尼古拉·果戈理",
  "year_display":"1836年（作者页 B140 口径：钦差大臣（1836））","year_sort":1836,
  "background":["作者页（B140）：果戈理代表作谱系——'钦差大臣（1836）、外套（1842）'（作者页 major_works 口径）。","果戈理为俄国讽刺大师（作者页 B140 定位——详见 sihunling 条）。"],
  "outline":["外省小城误把过路的赫列斯塔科夫当作钦差大臣——全城官僚争相行贿（通说）。","结尾：真钦差到任的'哑场'（通说待核）。"],
  "characters":[{"name":"赫列斯塔科夫","identity":"纨绔子弟","note":"冒牌钦差（通说）"},{"name":"市长","identity":"贪官","note":"群像核心（通说）"}],
  "themes":["官僚机器的漫画（通说）。",
   "'笑'的净化论（果戈理笑美学——通说待核）。",
   "俄国喜剧的成熟（通说）。"],
  "influence":[{"text":"作者页：果戈理代表作（B140 作者页口径）。","source":"B140"},
   {"text":"俄国讽刺戏剧的原点：对契诃夫以降的深远影响（通说待核）。","source":"B140"}],
  "reading":{"difficulties":["俄国官制等级。","人物昵称的谐音喜剧。"],
   "editions":["《果戈理小说戏剧选》（人民文学出版社，通说待核）。"],
   "order":"先《钦差大臣》后《死魂灵》。"},
  "pending":["1836年首演（亚历山大剧院说）与果戈理不满观众反应的史实待核。","赫列斯塔科夫人名核对。","'笑'美学出处（《剧院门口》）待核。"],
  "sources":["B140"],"year_source":"B140","author_source":"B140","related_works":["sihunling","weijunzi","geliefo"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《钦差大臣》骗局结构图",
    "cards":[{"title":"误认","text":"全城的恐慌","color":"family"},{"title":"行贿","text":"官吏的丑态","color":"antagonist"},{"title":"许婚","text":"骗子的即兴","color":"main"},{"title":"哑场","text":"真钦差到任","color":"gold"}]}
},
"heiansenlin": {
  "id":"heiansenlin","title":"黑暗森林","original_title":"黑暗森林（长篇小说，'地球往事'三部曲之二）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"长篇科幻小说","genre_group":"小说","language":"汉语（白话）","author_id":"liucixin","author_name":"刘慈欣",
  "year_display":"2008年出版（通说待核；作者页 B088 口径——刘慈欣代表作谱系）","year_sort":2008,
  "background":["作者页（B088）：刘慈欣为以《三体》成名的科幻作家（作者页定位——详见 santi 条）。","'黑暗森林法则'：宇宙社会学两条公理的推演——猜疑链与技术爆炸（通说待核）。"],
  "outline":["面壁计划：四位面壁者对抗三体智子（通说）。","罗辑领悟黑暗森林法则——以星系坐标威慑三体（通说待核）。"],
  "characters":[{"name":"罗辑","identity":"面壁者","note":"黑暗森林的发现者（通说）"},{"name":"章北海","identity":"太空军","note":"自然选择号（通说待核）"},{"name":"叶文洁","identity":"智囊","note":"宇宙社会学的启发者（通说待核）"}],
  "themes":["黑暗森林：生存是文明的第一需要（法则表述待核）。",
   "猜疑链与威慑伦理（通说）。",
   "硬科幻的中国面孔（通说）。"],
  "influence":[{"text":"作者页：刘慈欣以《三体》系列获得雨果奖（作者页 B088 口径——详见 santi 条）。","source":"B088"},
   {"text":"《三体》三部曲被译成多种语言、奥巴马等读者（通说待核）。","source":"B088"}],
  "reading":{"difficulties":["三部曲顺序（《三体》→本作→《死神永生》）。","物理设定（智子/水滴）。"],
   "editions":["《黑暗森林》（重庆出版社，通说待核）。"],
   "order":"先读《三体》→ 本作 →《死神永生》。"},
  "pending":["2008年重庆出版社初版核对。","黑暗森林法则原文表述核对。","雨果奖（2015年《三体》第一部）与三部曲整体的关系核对。"],
  "sources":["B088"],"year_source":"B088","author_source":"B088","related_works":["santi","wuhao","meilixinshijie"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《黑暗森林》威慑结构图",
    "cards":[{"title":"面壁计划","text":"四位面壁者","color":"family"},{"title":"智子","text":"锁死地球科技","color":"antagonist"},{"title":"罗辑","text":"黑暗森林的发现","color":"main"},{"title":"威慑","text":"坐标广播","color":"gold"}]}
},
"bisiwosixianshengdefangzi": {
  "id":"bisiwosixianshengdefangzi","title":"毕斯沃斯先生的房子","original_title":"A House for Mr Biswas","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"naipaul","author_name":"V.S.奈保尔",
  "year_display":"1961年出版（Britannica：A House for Mr Biswas (1961)）","year_sort":1961,
  "background":["Britannica：'His fourth novel, A House for Mr Biswas (1961), also set in Trinidad, was a much more important work and won him major recognition'（第四部小说、仍以特立尼达为背景，使他获得重要认可——B257）。","Britannica：'It centres on the main character's attempt to assert his personal identity and establish his independence as symbolized by owning his own house'（以拥有自己的房子象征人格独立——B257）。"],
  "outline":["毕斯沃斯一生寄人篱下（图尔斯家族）——从记者到自建房屋（通说待核）。","房子落成不久即逝——独立的悲剧性完成（通说待核）。"],
  "characters":[{"name":"毕斯沃斯","identity":"记者","note":"寻求独立的人（B257）"},{"name":"图尔斯家族","identity":"婆家","note":"印度裔大家庭（通说待核）"}],
  "themes":["'房子'作为身份与独立的象征（B257）。",
   "印度裔特立尼达人的殖民经验（B257 语境）。",
   "反英雄的喜剧叙事（通说）。"],
  "influence":[{"text":"Britannica：使其获得重要认可（major recognition）（B257）。","source":"B257"},
   {"text":"后殖民英语小说的经典（通说待核）。","source":"B257"}],
  "reading":{"difficulties":["特立尼达印度社群词汇。","体量与松散结构。"],
   "editions":["《毕斯沃斯先生的房子》（译林出版社/南海出版公司版本，通说待核）。"],
   "order":"对照《生命册》：两种'房子'的寓言。"},
  "pending":["图尔斯家族（Tulsis）细节核对。","自传性（作者父亲生平说）待核。","1961年出版（McGraw-Hill/André Deutsch说）核对。"],
  "sources":["B257"],"year_source":"B257","author_source":"B257","related_works":["lubinxun","shengmingce","huozhe"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《毕斯沃斯先生的房子》独立之路",
    "cards":[{"title":"寄居","text":"图尔斯家族","color":"family"},{"title":"记者","text":"苏伊德斯的写作","color":"gold"},{"title":"房子","text":"独立的象征（B257）","color":"main"},{"title":"逝去","text":"悲剧的完成","color":"antagonist"}]}
},
"qiyuderenmin": {
  "id":"qiyuderenmin","title":"七月的人民","original_title":"July's People","region":"南非","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"gordimer","author_name":"纳丁·戈迪默",
  "year_display":"1981年出版（Britannica：July's People (1981)）","year_sort":1981,
  "background":["Britannica：戈迪默的小说'the devastating effects of apartheid on the lives of South Africans'（B258）——本作为架空叙事。","Britannica（B258）：'July's People (1981), A Sport of Nature (1987), My Son's Story (1990), The House Gun (1998)'为其代表作谱系。"],
  "outline":["架空：黑人革命成功后，白人斯梅尔斯一家逃往仆人七月的村庄避难（通说待核）。","主仆关系在乡土中的倒转与摩擦（通说待核）。"],
  "characters":[{"name":"莫琳","identity":"白人主妇","note":"避难者（通说待核）"},{"name":"七月","identity":"仆人","note":"村庄的庇护者（通说待核）"}],
  "themes":["主仆倒转的伦理实验（通说）。",
   "隔离制度的' devastating effects'（B258）。",
   "个人疏离与社会正义的张力（B258）。"],
  "influence":[{"text":"Britannica：1991年诺贝尔文学奖（B258）。","source":"B258"},
   {"text":"反乌托邦式的种族寓言（通说待核）。","source":"B258"}],
  "reading":{"difficulties":["南非政治史架空设定。","七月的名字关系（主仆称呼）。"],
   "editions":["《七月的人民》（译林出版社版本，通说待核）。"],
   "order":"对照《耻》（库切）：南非的两种后种族书写。"},
  "pending":["斯梅尔斯一家/莫琳/七月人名核对。","被禁历史（南非书检——通说）待核。","结尾直升机之谜待核。"],
  "sources":["B258"],"year_source":"B258","author_source":"B258","related_works":["chi","wajie","banlunhuangri"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《七月的人民》倒转结构图",
    "cards":[{"title":"革命","text":"架空的政权更替","color":"antagonist"},{"title":"避难","text":"白人家庭入村","color":"family"},{"title":"七月","text":"仆人的村庄","color":"main"},{"title":"倒转","text":"主仆的伦理","color":"gold"}]}
},
"muqin": {
  "id":"muqin","title":"母亲","original_title":"Мать（Mother）","region":"俄国","era":"近代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"gorky","author_name":"马克西姆·高尔基",
  "year_display":"1906年出版（Britannica：Mat (1906; Mother)）","year_sort":1906,
  "background":["Britannica：'Mat (1906; Mother) is probably the least successful of the novels'——但'has considerable interest as Gorky's only long work devoted to the Russian revolutionary movement'（唯一 devoted to 革命运动的长篇——B259）。","改编（B259）：普多夫金1926年著名默片；布莱希特戏剧《母亲》（1930–31）。"],
  "outline":["巴维尔（Pavel）的工人革命活动与母亲尼洛夫娜的觉醒（人物名通说待核）。","五一游行与母亲的传单散发（通说待核）。"],
  "characters":[{"name":"尼洛夫娜","identity":"母亲","note":"从受难到觉醒（通说）"},{"name":"巴维尔","identity":"工人","note":"革命者（通说待核）"}],
  "themes":["革命叙事的原型文本（B259）。",
   "母亲的觉醒：从受难者到传递者（通说）。",
   "社会主义现实主义的先声（B259 语境）。"],
  "influence":[{"text":"Britannica：普多夫金1926年默片与布莱希特《母亲》（B259）。","source":"B259"},
   {"text":"苏联文学中'母亲'形象的范式化（通说待核）。","source":"B259"}],
  "reading":{"difficulties":["宣传文学的公式化——Britannica 亦称其'least successful'。","1900年代俄国工人运动背景。"],
   "editions":["《母亲》（人民文学出版社，通说待核）。"],
   "order":"对照《铁水奔流》（周立波？——不：《创业史》柳青）：社会主义现实主义谱系。"},
  "pending":["巴维尔/尼洛夫娜人名核对。","1906年纽约出版（Appleton说）与柏林德译细节待核。","'觉醒'章法与布尔什维克刊物连载待核。"],
  "sources":["B259"],"year_source":"B259","author_source":"B259","related_works":["mengya","ansuan","nahan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《母亲》觉醒结构图",
    "cards":[{"title":"受难","text":"工人家庭","color":"family"},{"title":"觉醒","text":"巴维尔入狱","color":"main"},{"title":"传单","text":"车站散发","color":"gold"},{"title":"原型","text":"革命叙事的起点（B259）","color":"plain"}]}
},
"beijingudetounao": {
  "id":"beijingudetounao","title":"被禁锢的头脑","original_title":"Zniewolony umysł（The Captive Mind）","region":"波兰","era":"现当代","era_detail":"20世纪",
  "genre":"思想论集","genre_group":"散文","language":"波兰语","author_id":"milosz","author_name":"切斯瓦夫·米沃什",
  "year_display":"1953年出版（Britannica：The Captive Mind (1953)）","year_sort":1953,
  "background":["Britannica：'his best-known work is the essay collection The Captive Mind (1953), in which he condemns the accommodation of many Polish intellectuals to communism'（谴责许多波兰知识分子对共产主义的适应——B260）。","诺奖授奖词（B260）：'a writer who with uncompromising clear-sightedness voices man's exposed condition in a world of severe conflicts'。","'Until 1980……his work was banned in Poland'（B260）。"],
  "outline":["'波罗的海三国民众的哲学'：四种知识分子的化身——墨提斯/阿尔法/贝塔/戴尔塔（人名对应通说待核）。","'凯特曼主义'：新信仰的心理机制（通说待核）。"],
  "characters":[{"name":"墨提斯/阿尔法/贝塔/戴尔塔","identity":"知识分子四型","note":"字母化命名（通说待核）"}],
  "themes":["知识分子与新信仰的适应（B260）。",
   "极权时代的'凯特曼'心理（通说待核——Ketman 概念源自伊斯兰世界）。",
   "流亡者的清醒（B260：uncompromising clear-sightedness）。"],
  "influence":[{"text":"Britannica：其最著名的作品（best-known work）（B260）。","source":"B260"},
   {"text":"冷战知识分子的经典自省文本（通说待核）。","source":"B260"}],
  "reading":{"difficulties":["波兰思想史背景。","字母人物的真实对应（考证）。"],
   "editions":["《被禁锢的头脑》（广西师范大学出版社，通说待核）。"],
   "order":"对照《古拉格群岛》《二手时间》：三种极权记录。"},
  "pending":["四种化身的人物原型核对。","'凯特曼'（Ketman）概念的波斯源流待核。","中译本信息核对。"],
  "sources":["B260"],"year_source":"B260","author_source":"B260","related_works":["gulage","ershoushijian","fengzhonglvli"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《被禁锢的头脑》四型结构图",
    "cards":[{"title":"阿尔法","text":"道德家","color":"family"},{"title":"贝塔","text":"宿命论记者","color":"plain"},{"title":"戴尔塔","text":"田园诗人","color":"gold"},{"title":"凯特曼","text":"适应的心理（通说）","color":"main"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
