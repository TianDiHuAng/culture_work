# -*- coding: utf-8 -*-
"""流水线批次8：Britannica 新核 4 部 + 薄注记补全 3 部"""
import json, pathlib

new_src = [
{"id":"B285","title":"Marguerite Yourcenar — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Marguerite-Yourcenar","type":"百科全书","verified":True,"covers":["yourcenar","hadilianghuiyilu"],"note":"2026-11-20 核对：1903-06-08布鲁塞尔生（原名 Marguerite de Crayencour）—1987-12-17美国缅因州东北港卒（84岁）；1980年'the first woman to be elected to the Academie Francaise'（法兰西学院40席院士中首位女性）；'Her masterpiece is Memoires d Hadrien (1951; Memoirs of Hadrian), a historical novel'；另一历史小说 L Oeuvre au noir (1968; The Abyss)；'rigorously classical style, their erudition, and their psychological subtlety'"},
{"id":"B286","title":"Julio Cortazar — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Julio-Cortazar","type":"百科全书","verified":True,"covers":["cortazar","tiaofangzi"],"note":"2026-11-20 核对：1914-08-26布鲁塞尔生—1984-02-12巴黎卒（69岁）；1951年因对庇隆政府失望定居巴黎、1981年获双重国籍；'Cortazar's masterpiece, Rayuela (1963; Hopscotch), is an open-ended novel, or antinovel'；'the reader is invited to rearrange the different parts of the novel according to a plan prescribed by the author'；'It was the first of the boom of Latin American novels of the 1960s to gain international attention'；'often incorporates fantastic or mythical elements into realistic fiction'（magic realism 语境）"},
{"id":"B287","title":"Carlos Fuentes — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Carlos-Fuentes","type":"百科全书","verified":True,"covers":["fuentes","aertemio"],"note":"2026-11-20 核对：1928-11-11巴拿马城生—2012-05-15墨西哥城卒（83岁）；外交官（驻法大使1975—77）；1987年塞万提斯奖；La muerte de Artemio Cruz (1962)——'presents the agony of the last hours of a wealthy survivor of the Mexican Revolution'、'translated into several languages and established Fuentes as a major international novelist'；'undoubtedly one of the foremost Mexican writers of the 20th century'"},
{"id":"B288","title":"Philip Roth — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Philip-Roth","type":"百科全书","verified":True,"covers":["roth","meiguomuge"],"note":"2026-11-20 核对：1933-03-19纽瓦克生—2018-05-22纽约卒（85岁）；成名作 Goodbye, Columbus (1959)；'For his next work, American Pastoral (1997; film 2016), Roth was awarded a Pulitzer Prize'；'about a middle-class couple whose daughter becomes a terrorist, is the first entry in the American Trilogy series'；'sharp dialogue and exploration of Jewish middle-class life'；2012年封笔"},
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
"yourcenar": {
  "id": "yourcenar", "name": "玛格丽特·尤瑟纳尔", "foreign_name": "Marguerite Yourcenar（玛格丽特·尤瑟纳尔，原名玛格丽特·德·克拉扬古尔，1903-06-08—1987-12-17）",
  "country": "法国", "birth": 1903, "death": 1987, "birth_year": 1903, "death_year": 1987, "era": "现当代",
  "summary": "尤瑟纳尔，布鲁塞尔出生（Britannica：originally Marguerite de Crayencour），法国小说家、散文家与短篇家——以古典、博学的历史小说著称（Britannica）。1980年'the first woman to be elected to the Académie Française'（首位入选法兰西学院的女性——该学院'with a membership limited to 40'——Britannica）。'Her masterpiece is Mémoires d'Hadrien (1951; Memoirs of Hadrian), a historical novel'（杰作《哈德良回忆录》——B285）。文体：'rigorously classical style, their erudition, and their psychological subtlety'（严谨的古典风格、博学与心理细腻——B285）。",
  "timeline": [
    {"year": 1903, "text": "6月8日生于布鲁塞尔（Britannica：Born June 8, 1903, Brussels, Belgium）。", "src": "B285"},
    {"year": 1951, "text": "《哈德良回忆录》出版（Britannica：Mémoires d'Hadrien (1951)）。", "src": "B285"},
    {"year": 1968, "text": "《苦炼》（L'Oeuvre au noir）出版（Britannica：1968; The Abyss）。", "src": "B285"},
    {"year": 1980, "text": "成为法兰西学院首位女性院士（Britannica：first woman……1980）。", "src": "B285"},
    {"year": 1987, "text": "12月17日卒于美国缅因州东北港（Britannica：died December 17, 1987, Northeast Harbor, Maine）。", "src": "B285"}],
  "major_works": [
    {"work_id": "hadilianghuiyilu", "note": "历史小说（Britannica：masterpiece，1951）"},
    {"title": "苦炼", "note": "（Britannica：L'Oeuvre au noir (1968; The Abyss)）"},
    {"title": "东方奇观", "note": "（通说待核）"}],
  "style": [
    "'严谨的古典风格、博学与心理细腻'（B285：rigorously classical style……erudition……psychological subtlety）。",
    "历史小说的博学重构（B285：classical, erudite historical fiction——综述语境）。",
    "第一人称的'自我传记'式历史（通说待核——《哈德良回忆录》形式）。"],
  "status": "Britannica 定位尤瑟纳尔为法国小说家、散文家与短篇家，1980年法兰西学院首位女性院士（B285）。",
  "sources": ["B285"], "dates_source": "B285",
  "pending": ["1980年入选年份（Britannica 已载）与院士辞就任演说核对。", "《哈德良回忆录》梅里奥版本细节待核。", "中译本（三联书店版）待核。"]
},
"cortazar": {
  "id": "cortazar", "name": "胡利奥·科塔萨尔", "foreign_name": "Julio Cortázar（胡利奥·科塔萨尔，1914-08-26—1984-02-12）",
  "country": "阿根廷", "birth": 1914, "death": 1984, "birth_year": 1914, "death_year": 1984, "era": "现当代",
  "summary": "科塔萨尔，布鲁塞尔出生的阿根廷小说家与短篇家——'blended existential questioning with experimental techniques'（把存在之问与实验技术混合——Britannica），'best known for the open-ended novel Rayuela (Hopscotch)'（以开放式的《跳房子》最著名——Britannica）。1951年因对庇隆政府失望定居巴黎、1981年获法阿双重国籍（Britannica）。'It was the first of the boom of Latin American novels of the 1960s to gain international attention'（《跳房子》是1960年代拉美小说'繁荣'中第一部引起国际关注的作品——B286）。其作'often incorporates fantastic or mythical elements into realistic fiction'（B286 语境）。",
  "timeline": [
    {"year": 1914, "text": "8月26日生于布鲁塞尔（Britannica：Born August 26, 1914, Brussels, Belgium）。", "src": "B286"},
    {"year": 1951, "text": "定居巴黎（Britannica：settled in Paris in 1951, disillusioned with Juan Perón's government）。", "src": "B286"},
    {"year": 1963, "text": "《跳房子》出版（Britannica：Rayuela (1963; Hopscotch)）。", "src": "B286"},
    {"year": 1981, "text": "获法国国籍（Britannica：French citizenship in 1981）。", "src": "B286"},
    {"year": 1984, "text": "2月12日卒于巴黎（Britannica：Died February 12, 1984, Paris）。", "src": "B286"}],
  "major_works": [
    {"work_id": "tiaofangzi", "note": "长篇（B286：masterpiece，antinovel）"},
    {"title": "动物寓言集、游戏的终结", "note": "（Britannica：Bestiario (1951), Final del juego (1956), Las armas secretas (1958)）"},
    {"title": "万火归一", "note": "（通说待核）"}],
  "style": [
    "'antinovel'（反小说）：读者可按作者规划重排章节（B286：the reader is invited to rearrange the different parts）。",
    "魔幻元素嵌入写实（B286：fantastic or mythical elements into realistic fiction）。",
    "短篇的幻想—现实裂缝（通说）。"],
  "status": "Britannica 定位科塔萨尔为阿根廷小说家与短篇家、《跳房子》作者——拉美'繁荣'的国际先声（B286）。",
  "sources": ["B286"], "dates_source": "B286",
  "pending": ["《跳房子》155章与'两种读法'表（通说）核对。","拉丁美洲'boom'定义（B286 已载）展开核对。","与尼加拉瓜桑地诺运动的关联待核。"]
},
"fuentes": {
  "id": "fuentes", "name": "卡洛斯·富恩特斯", "foreign_name": "Carlos Fuentes（卡洛斯·富恩特斯，1928-11-11—2012-05-15）",
  "country": "墨西哥", "birth": 1928, "death": 2012, "birth_year": 1928, "death_year": 2012, "era": "现当代",
  "summary": "富恩特斯，巴拿马城出生的墨西哥小说家、剧作家、批评家与外交官（Britannica；驻法大使1975—77）——其'experimental, postmodern novels—including Where the Air Is Clear and The Death of Artemio Cruz'探索墨西哥身份并赢得国际声誉（Britannica），1987年获塞万提斯奖（Britannica：the most prestigious Spanish-language literary award）。'La muerte de Artemio Cruz (1962)……established Fuentes as a major international novelist'（B287）；'undoubtedly one of the foremost Mexican writers of the 20th century'（20世纪墨西哥最重要的作家之一——B287）。",
  "timeline": [
    {"year": 1928, "text": "11月11日生于巴拿马城（Britannica：Born November 11, 1928, Panama City, Panama）。", "src": "B287"},
    {"year": 1962, "text": "《阿尔特米奥·克罗斯之死》出版（Britannica：La muerte de Artemio Cruz (1962)）。", "src": "B287"},
    {"year": 1975, "text": "任驻法大使（Britannica：ambassador to France 1975–77）。", "src": "B287"},
    {"year": 1987, "text": "获塞万提斯奖（Britannica：Cervantes Prize 1987）。", "src": "B287"},
    {"year": 2012, "text": "5月15日卒于墨西哥城（Britannica：Died May 15, 2012, Mexico City）。", "src": "B287"}],
  "major_works": [
    {"work_id": "aertemio", "note": "长篇（B287：1962）"},
    {"title": "最明净的地区", "note": "（Britannica：Where the Air Is Clear）"},
    {"title": "换皮", "note": "（通说待核）"}],
  "style": [
    "'experimental, postmodern novels'（B287）。",
    "墨西哥身份的探察（B287：explored Mexican identity）。",
    "时序拼贴（临终时刻的三声部——通说待核）。"],
  "status": "Britannica 定位富恩特斯为'20世纪墨西哥最重要的作家之一'、1987年塞万提斯奖得主（B287）。",
  "sources": ["B287"], "dates_source": "B287",
  "pending": ["《阿尔特米奥·克罗斯之死》三声部（我/他/神）结构待核。","1962年出版（Fondo de Cultura说）核对。","与《最明净的地区》的关系待核。"]
},
"roth": {
  "id": "roth", "name": "菲利普·罗斯", "foreign_name": "Philip Roth（菲利普·罗斯，1933-03-19—2018-05-22）",
  "country": "美国", "birth": 1933, "death": 2018, "birth_year": 1933, "death_year": 2018, "era": "现当代",
  "summary": "罗斯，新泽西州纽瓦克人，美国小说家与短篇家——'celebrated for his sharp dialogue, portrayals of Jewish middle-class life, and later work confronting aging and mortality'（以犀利对话、犹太中产生活刻画与直面衰老死亡的后期作品著称——Britannica）。成名作《再见，哥伦布》（1959）；'For his next work, American Pastoral (1997; film 2016), Roth was awarded a Pulitzer Prize'（《美国牧歌》获普利策奖——B288）；2012年封笔（Britannica：retired from writing in 2012）。",
  "timeline": [
    {"year": 1933, "text": "3月19日生于新泽西州纽瓦克（Britannica：Born March 19, 1933, Newark, New Jersey）。", "src": "B288"},
    {"year": 1959, "text": "《再见，哥伦布》成名（Britannica：rose to fame with Goodbye, Columbus (1959)）。", "src": "B288"},
    {"year": 1997, "text": "《美国牧歌》获普利策奖（B288：American Pastoral (1997)……Pulitzer Prize）。", "src": "B288"},
    {"year": 2012, "text": "宣布封笔（Britannica：retired from writing in 2012）。", "src": "B288"},
    {"year": 2018, "text": "5月22日卒于纽约（B288：Died May 22, 2018, New York）。", "src": "B288"}],
  "major_works": [
    {"work_id": "meiguomuge", "note": "长篇（B288：1997，普利策奖）"},
    {"title": "美国三部曲", "note": "（B288：American Trilogy series——牧歌/我嫁给了一个死人/人性的污秽）"},
    {"title": "波特诺伊的控诉", "note": "（通说待核）"}],
  "style": [
    "'sharp dialogue'（B288）。",
    "犹太中产阶级生活刻画（B288：Jewish middle-class life）。",
    "后期直面衰老与死亡（B288：confronting aging and mortality）。"],
  "status": "Britannica 定位罗斯为美国小说家与短篇家（普利策奖得主、美国三部曲作者）；'朱利安·巴恩斯'并称论（通说待核）。",
  "sources": ["B288"], "dates_source": "B288",
  "pending": ["《美国牧歌》1997年出版（Houghton Mifflin说）核对。","斯威德·利沃夫/梅瑞狄斯人名核对。","美国三部曲余两部（《我嫁给了一个死人》《人性的污秽》）核对。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"hadilianghuiyilu": {
  "id":"hadilianghuiyilu","title":"哈德良回忆录","original_title":"Mémoires d'Hadrien（Memoirs of Hadrian）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"历史小说","genre_group":"小说","language":"法语","author_id":"yourcenar","author_name":"玛格丽特·尤瑟纳尔",
  "year_display":"1951年（Britannica：Her masterpiece is Mémoires d'Hadrien (1951; Memoirs of Hadrian), a historical novel）","year_sort":1951,
  "background":["Britannica（B285）：'Her masterpiece is Mémoires d'Hadrien (1951; Memoirs of Hadrian), a historical novel'（杰作）。","文体（B285 语境）：'rigorously classical style, their erudition, and their psychological subtlety'——以第一人称书信体重构罗马皇帝哈德良的内心。"],
  "outline":["致马可·奥勒留的长信：从西班牙到罗马的一生（通说待核）。","'Animula vagula blandula'——临终对灵魂的发问（通说待核）。"],
  "characters":[{"name":"哈德良","identity":"罗马皇帝","note":"第一人称（通说待核）"},{"name":"安提诺乌斯","identity":"爱人","note":"（通说待核）"}],
  "themes":["历史的心理重构（B285：psychological subtlety）。",
   "权力与美、生与死（通说）。",
   "'古典'的博学（B285：erudition）。"],
  "influence":[{"text":"Britannica：'Her masterpiece'（B285）。","source":"B285"},
   {"text":"Britannica：1980年法兰西学院首位女性院士（B285）。","source":"B285"}],
  "reading":{"difficulties":["罗马史知识。","书信体的静穆语调。"],
   "editions":["《哈德良回忆录》（上海三联书店/东方出版中心版本，通说待核）。","法文原版（Plon/Gallimard）。"],
   "order":"历史小说进阶之作。"},
  "pending":["1951年出版（Plon说）核对。","安提诺乌斯/马可·奥勒留情节核对。","'Animula vagula blandula'引文核对。"],
  "sources":["B285"],"year_source":"B285","author_source":"B285","related_works":["aeneid","niwanghechuqu","shenqu"],
  "svg":G2("《哈德良回忆录》帝国回望图",[{"title":"书信","text":"致未来的皇帝","color":"main"},{"title":"帝国","text":"罗马的疆域","color":"gold"},{"title":"安提诺乌斯","text":"爱与哀","color":"family"},{"title":"临终","text":"灵魂的问句（通说）","color":"plain"}])
},
"tiaofangzi": {
  "id":"tiaofangzi","title":"跳房子","original_title":"Rayuela（Hopscotch）","region":"阿根廷","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说（反小说）","genre_group":"小说","language":"西班牙语","author_id":"cortazar","author_name":"胡利奥·科塔萨尔",
  "year_display":"1963年（Britannica：Rayuela (1963; Hopscotch)——'an open-ended novel, or antinovel'）","year_sort":1963,
  "background":["Britannica（B286）：'Cortázar's masterpiece, Rayuela (1963; Hopscotch), is an open-ended novel, or antinovel'；'the reader is invited to rearrange the different parts of the novel according to a plan prescribed by the author'（读者被邀请按作者规划重排章节）。","'It was the first of the boom of Latin American novels of the 1960s to gain international attention'（B286）。"],
  "outline":["拉美与巴黎的双城：奥利维拉与'俱乐部'（通说待核）。","155章+'不必读的章'——按表重排的两种读法（通说待核）。"],
  "characters":[{"name":"奥利维拉","identity":"流浪者","note":"（通说待核）"},{"name":"拉蜜拉","identity":"女子","note":"（通说待核）"}],
  "themes":["读者参与的开放文本（B286：rearrange the different parts）。",
   "反小说（B286：antinovel）。",
   "拉美'boom'的先声（B286：first of the boom）。"],
  "influence":[{"text":"Britannica：'masterpiece'；拉美boom第一部国际关注之作（B286）。","source":"B286"},
   {"text":"Britannica：魔幻元素嵌入写实（B286 语境）。","source":"B286"}],
  "reading":{"difficulties":["两种读法的选择。","哲学对话章。"],
   "editions":["《跳房子》（人民文学出版社/上海译文出版社版本，通说待核）。","西班牙文原版（Southget）。"],
   "order":"拉美boom进阶之作。"},
  "pending":["155章与跳读表核对。","奥利维拉/拉蜜拉人名核对。","与马尔克斯等的boom谱系待核。"],
  "sources":["B286"],"year_source":"B286","author_source":"B286","related_works":["bainian","huangyezhentan","di'ertiaojugui"],
  "svg":G2("《跳房子》重排结构图",[{"title":"顺读","text":"1—56章","color":"family"},{"title":"跳读","text":"按表重排（B286）","color":"main"},{"title":"奥利维拉","text":"流浪的智者","color":"gold"},{"title":"反小说","text":"开放文本","color":"antagonist"}])
},
"meiguomuge": {
  "id":"meiguomuge","title":"美国牧歌","original_title":"American Pastoral","region":"美国","era":"现当代","era_detail":"21世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"roth","author_name":"菲利普·罗斯",
  "year_display":"1997年（Britannica：American Pastoral (1997; film 2016), Roth was awarded a Pulitzer Prize）","year_sort":1997,
  "background":["Britannica（B288）：'For his next work, American Pastoral (1997; film 2016), Roth was awarded a Pulitzer Prize'；'about a middle-class couple whose daughter becomes a terrorist, is the first entry in the American Trilogy series'（美国三部曲之首——B288）。","作者（B288）：'sharp dialogue and exploration of Jewish middle-class life'。"],
  "outline":["犹太棒球明星'瑞典佬'利沃夫的女儿成为反战炸弹客——美国梦的爆破（通说待核）。"],
  "characters":[{"name":"瑞典佬（斯威德·利沃夫）","identity":"手套业商人","note":"（通说待核）"},{"name":"梅瑞狄斯","identity":"女儿","note":"炸弹客（通说待核）"}],
  "themes":["美国梦的爆破（书名反讽——通说）。",
   "60年代炸弹的年代（通说待核）。",
   "犹太中产三代（B288 语境）。"],
  "influence":[{"text":"Britannica：普利策奖；美国三部曲之首（B288）。","source":"B288"},
   {"text":"Britannica：2016年电影改编（B288）。","source":"B288"}],
  "reading":{"difficulties":["三代人的时间跨度。","罗斯的对话密度。"],
   "editions":["《美国牧歌》（上海译文出版社，通说待核）。","英文原版（Houghton Mifflin）。"],
   "order":"美国三部曲之首。"},
  "pending":["1997年出版（Houghton Mifflin说）核对。","瑞典佬/梅瑞狄斯人名核对。","三部曲后两部（《我嫁给了共产党人》《人性的污秽》）核对。"],
  "sources":["B288"],"year_source":"B288","author_source":"B288","related_works":["jueshi","fenwangyu","yinduzhixing"],
  "svg":G2("《美国牧歌》梦爆结构图",[{"title":"棒球明星","text":"美国梦的偶像","color":"family"},{"title":"女儿","text":"炸弹客（B288）","color":"antagonist"},{"title":"牧歌","text":"田园的反讽","color":"main"},{"title":"三部曲","text":"美国世纪之变","color":"gold"}])
},
"aertemio": {
  "id":"aertemio","title":"阿尔特米奥·克罗斯之死","original_title":"La muerte de Artemio Cruz","region":"墨西哥","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"fuentes","author_name":"卡洛斯·富恩特斯",
  "year_display":"1962年（Britannica：La muerte de Artemio Cruz (1962)）","year_sort":1962,
  "background":["Britannica（B287）：'La muerte de Artemio Cruz (1962; The Death of Artemio Cruz), which presents the agony of the last hours of a wealthy survivor of the Mexican Revolution'（写墨西哥革命幸存富人的最后时刻——B287）；'translated into several languages and established Fuentes as a major international novelist'（B287）。","作者（B287）：'undoubtedly one of the foremost Mexican writers of the 20th century'；1987塞万提斯奖。"],
  "outline":["垂死的阿尔特米奥·克罗斯的三声部回忆（我/他/你——通说待核）。","革命理想背叛者的忏悔与恐惧（通说待核）。"],
  "characters":[{"name":"阿尔特米奥·克罗斯","identity":"幸存富商","note":"（B287）"}],
  "themes":["革命背叛者的临终（B287：agony of the last hours）。",
   "三声部时序拼贴（通说待核）。",
   "墨西哥身份的暴力起源（B287 语境：explored Mexican identity）。"],
  "influence":[{"text":"Britannica：'established Fuentes as a major international novelist'（B287）。","source":"B287"},
   {"text":"Britannica：'undoubtedly one of the foremost Mexican writers of the 20th century'（B287）。","source":"B287"}],
  "reading":{"difficulties":["三声部人称切换。","墨西哥革命史。"],
   "editions":["《阿尔特米奥·克罗斯之死》（人民文学出版社/上海译文版本，通说待核）。","西班牙文原版（FCE）。"],
   "order":"先《最明净的地区》后本作。"},
  "pending":["1962年出版（Fondo de Cultura Económica说）核对。","三声部结构（我/他/你——通说）核对。","临终日（1959年4月）细节待核。"],
  "sources":["B287"],"year_source":"B287","author_source":"B287","related_works":["bainian","peideluobalamo","shijiemori"],
  "svg":G2("《阿尔特米奥》三声部图",[{"title":"我","text":"记忆的独白","color":"main"},{"title":"他","text":"社会的档案","color":"family"},{"title":"你","text":"灵魂的对话","color":"gold"},{"title":"临终","text":"最后12小时（通说）","color":"antagonist"}])
},
"niezi": {
  "id":"niezi","title":"孽子","original_title":"孽子（长篇小说）","region":"中国","era":"现当代","era_detail":"台湾现代主义",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"baixianyung","author_name":"白先勇",
  "year_display":"出版年份待核（作者页 B208 存目：孽子——1983年说通说待核）","year_sort":1983,
  "background":["作者页（B208）：白先勇 major_works 载'孽子'（B208 作者页定位，详见 taibeiren 条核对）。","题材（通说待核）：台北新公园夜间的'青春鸟'群落——李青的父与子。"],
  "outline":["李青被学校开除、被父亲逐出家门——新公园'王国'的夜游者（通说待核）。","父子线：'父亲'与'孽子'的双重不赦（通说待核）。"],
  "characters":[{"name":"李青","identity":"少年","note":"被逐者（通说待核）"},{"name":"阿凤","identity":"'传说'","note":"（通说待核）"}],
  "themes":["父与子的和解之难（通说待核）。",
   "边缘群体的'王国'（通说）。",
   "'孽'：不赦与悲悯（书名通说）。"],
  "influence":[{"text":"作者页：白先勇代表作（B208 作者页口径）。","source":"B208"},
   {"text":"华语第一部以同性恋题材立目的长篇之一（通说待核）。","source":"B208"}],
  "reading":{"difficulties":["'新公园'的空间与暗语。","父子伦理的重负。"],
   "editions":["《孽子》（白先勇作品集，通说待核）。"],
   "order":"先《台北人》后本作。"},
  "pending":["1983年出版（《现代文学》连载说）核对。","李青/阿凤人名核对。","电视剧与舞台剧改编待核。"],
  "sources":["B208"],"year_source":"B208","author_source":"B208","related_works":["taibeiren","qingchengzhilian","jiandie"],
  "svg":G2("《孽子》夜园结构图",[{"title":"新公园","text":"夜间的王国（通说）","color":"family"},{"title":"李青","text":"被逐的少年","color":"main"},{"title":"父子","text":"不赦与和解","color":"gold"},{"title":"青春鸟","text":"群像的飞散","color":"plain"}])
},
"quyuan": {
  "id":"quyuan","title":"屈原","original_title":"屈原（历史剧）","region":"中国","era":"现当代","era_detail":"现代",
  "genre":"历史剧","genre_group":"戏剧","language":"汉语（白话·诗剧）","author_id":"guomoruo","author_name":"郭沫若",
  "year_display":"1942年（作者页 B207 口径：major_works 载'屈原（历史剧）'——1942年说通说待核）","year_sort":1942,
  "background":["作者页（B207）：郭沫若 major_works 载'屈原（历史剧）'（B207 作者页定位，详见 nvshen 条核对）。","题材（通说待核）：以《史记》屈原事迹为骨——'雷电颂'的爆发的五幕历史剧。"],
  "outline":["屈原被谗放逐：南后的构陷、婵娟的忠、'雷电颂'的独白（通说待核）。"],
  "characters":[{"name":"屈原","identity":"诗人·三闾大夫","note":"（通说待核）"},{"name":"婵娟","identity":"侍女","note":"虚构人物（通说待核）"},{"name":"南后郑袖","identity":"后妃","note":"构陷者（通说待核）"}],
  "themes":["借古讽今：皖南事变语境（通说待核）。",
   "'雷电颂'的诗剧高潮（通说待核）。",
   "历史剧'古为今用'（通说）。"],
  "influence":[{"text":"作者页：郭沫若历史剧代表作（B207 作者页口径）。","source":"B207"},
   {"text":"作者页：郭沫若'在每个文类上都极其多产'（B207 作者级定位）。","source":"B207"}],
  "reading":{"difficulties":["战时重庆语境。","历史与虚构的比例。"],
   "editions":["《屈原》（人民文学出版社《沫若剧作选》，通说待核）。"],
   "order":"对照《虎符》《棠棣之花》（通说——郭沫若历史剧系列）。"},
  "pending":["1942年重庆首演（中华剧艺社说）核对。","婵娟虚构人物确认。","'雷电颂'原文核对。"],
  "sources":["B207"],"year_source":"B207","author_source":"B207","related_works":["chuci","richu","nvshen"],
  "svg":G2("《屈原》历史剧结构图",[{"title":"构陷","text":"南后的毒计","color":"antagonist"},{"title":"雷电颂","text":"诗剧的高潮","color":"main"},{"title":"婵娟","text":"忠的替死","color":"gold"},{"title":"借古讽今","text":"1942年的重庆","color":"family"}])
},
"meiyouyingxiongdechangshi": {
  "id":"meiyouyingxiongdechangshi","title":"没有英雄的长诗","original_title":"Поэма без героя（Poem Without a Hero）","region":"俄国","era":"现当代","era_detail":"20世纪",
  "genre":"长诗","genre_group":"诗歌","language":"俄语","author_id":"akhmatova","author_name":"安娜·阿赫玛托娃",
  "year_display":"写作于1940年起，定稿年代待核（作者页 B144 口径：没有英雄的长诗（通说待核））","year_sort":1960,
  "background":["作者页（B144）：阿赫玛托娃 major_works 载'没有英雄的长诗（通说待核）'（B144 作者页定位，详见 anhunqu 条核对）。","文体（通说待核）：回忆1913年彼得堡的艺术世界——三部分的长诗，跨越白银时代的挽歌。"],
  "outline":["1913年的假面舞会——白银时代的回光（通说待核）。","'没有英雄'：历史的缺席者（通说待核）。"],
  "characters":[{"name":"抒情女声","identity":"诗人","note":"（通说待核）"}],
  "themes":["白银时代的挽歌（通说待核）。",
   "'没有英雄'的悖论（通说待核）。",
   "战争的见证（作者页 B144 语境——安魂曲同期）。"],
  "influence":[{"text":"作者页：阿赫玛托娃作品谱系（B144 作者页口径）。","source":"B144"},
   {"text":"作者页：阿赫玛托娃为白银时代代表（B144 作者级定位）。","source":"B144"}],
  "reading":{"difficulties":["彼得堡文艺史。","注释（作者自注说）。"],
   "editions":["《没有英雄的长诗》（收于《阿赫玛托娃诗文集》，通说待核）。","俄文原版。"],
   "order":"先《安魂曲》后本作。"},
  "pending":["写作—定稿年表（1940—1962说）核对。","三部分标题（献词/第一部分/尾诗）待核。","列宁格勒1913年的假面舞会原型待核。"],
  "sources":["B144"],"year_source":"B144","author_source":"B144","related_works":["anhunqu","nianzhu","lianqingdezhongjie"],
  "svg":G2("《没有英雄的长诗》回望图",[{"title":"1913","text":"假面舞会的回光","color":"family"},{"title":"没有英雄","text":"缺席的承担","color":"main"},{"title":"挽歌","text":"白银时代的终曲","color":"gold"},{"title":"见证","text":"战争的另一面","color":"antagonist"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
