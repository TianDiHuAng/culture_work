# -*- coding: utf-8 -*-
"""流水线批次9：Britannica 新核 4 作家 4 部 + 零成本直写 5 部"""
import json, pathlib

new_src = [
{"id":"B289","title":"Francois Mauriac — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Francois-Mauriac","type":"百科全书","verified":True,"covers":["mauriac","aidewangmo"],"note":"2026-11-20 核对：1885-10-11波尔多生—1970-09-01巴黎卒（84岁）；1952诺贝尔奖；1933年入选法兰西学院；'Mauriac showed increasing mastery in Le Desert de l amour (1925; The Desert of Love)'；Thérèse Desqueyroux (1927)——'whose heroine is driven to attempt the murder of her husband to escape her suffocating life'；'Le Noeud de vipères (1932; Vipers Tangle...) is often considered Mauriac's masterpiece'；'His major novels are somber, austere psychological dramas set in an atmosphere of unrelieved tension'；波尔多与资产阶级生活的框架"},
{"id":"B290","title":"Julian Barnes — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Julian-Barnes","type":"百科全书","verified":True,"covers":["barnes","fuloubaideyingwu"],"note":"2026-11-20 核对：1946-01-19莱斯特生；'Flaubert's Parrot (1984), Barnes's breakthrough novel, is a humorous mixture of biography, fiction, and literary criticism'（入围布克奖）；2011年布克奖 The Sense of an Ending——'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'；'British critic and author of inventive and intellectual novels about obsessed characters curious about the past'；2026年 Departure(s) 自称最后一部小说"},
{"id":"B291","title":"Flannery OConnor — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Flannery-OConnor","type":"百科全书","verified":True,"covers":["oconnor","haorennanxun"],"note":"2026-11-20 核对：1925-03-25佐治亚州萨凡纳生—1964-08-03米利奇维尔卒（39岁）；A Good Man Is Hard to Find, and Other Stories (1955)——'she came to be regarded as a master of the form'；'In it OConnor created an unexpected agent of salvation in the character of an escaped convict called The Misfit'；'regarded as a master of the Southern gothic'（grotesque, macabre, or fantastic incidents）；暴力'is strangely capable of returning my characters to reality and preparing them to accept their moment of grace'；红斑狼疮（inherit from father）致命；Complete Stories (1971) 获1972年国家图书奖"},
{"id":"B292","title":"Willa Cather — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Willa-Cather","type":"百科全书","verified":True,"covers":["cather","wodeandongnia"],"note":"2026-11-20 核对：1873-12-07弗吉尼亚州温切斯特附近生—1947-04-24纽约卒（73岁）；'With O Pioneers! (1913) and My Antonia (1918), which has frequently been adjudged her finest achievement'；My Antonia——'It tells the story of Antonia Shimerda, a daughter of Bohemian immigrants on the Nebraska frontier'；One of Ours (1922)——'won the Pulitzer Prize'；'Her unique regionalism captured the essence of the American West'（引述片段）；强调'spiritual and moral values over materialism'"},
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
"mauriac": {
  "id": "mauriac", "name": "弗朗索瓦·莫里亚克", "foreign_name": "François Mauriac（弗朗索瓦·莫里亚克，1885-10-11—1970-09-01）",
  "country": "法国", "birth": 1885, "death": 1970, "birth_year": 1885, "death_year": 1970, "era": "现当代",
  "summary": "莫里亚克，波尔多生，法国天主教小说家、散文家、诗人、剧作家与记者——'best known for somber psychological dramas set in Bordeaux'（以波尔多背景的阴郁心理剧著称——Britannica）；'His major novels are somber, austere psychological dramas set in an atmosphere of unrelieved tension'（B289）。1933年入选法兰西学院、1952年获诺贝尔文学奖（B289）。'Le Noeud de vipères (1932; Vipers' Tangle...) is often considered Mauriac's masterpiece'（蝮蛇结常被视为其杰作——B289）。",
  "timeline": [
    {"year": 1885, "text": "10月11日生于波尔多（Britannica：Born October 11, 1885, Bordeaux, France）。", "src": "B289"},
    {"year": 1925, "text": "《爱的荒漠》出版——'Mauriac showed increasing mastery'（B289）。", "src": "B289"},
    {"year": 1933, "text": "入选法兰西学院（Britannica：Elected to the French Academy 1933）。", "src": "B289"},
    {"year": 1952, "text": "获诺贝尔文学奖（Britannica：Nobel Prize for Literature 1952）。", "src": "B289"},
    {"year": 1970, "text": "9月1日卒于巴黎（Britannica：Died September 1, 1970, Paris）。", "src": "B289"}],
  "major_works": [
    {"work_id": "aidewangmo", "note": "长篇（B289：1925）"},
    {"title": "苔蕾丝·德斯盖鲁", "note": "（B289：Thérèse Desqueyroux (1927)）"},
    {"title": "蝮蛇结", "note": "（B289：Vipers' Tangle (1932)——'often considered Mauriac's masterpiece'）"}],
  "style": [
    "'阴郁、简朴的心理剧'（B289：somber, austere psychological dramas）。",
    "'无休止紧张的氛围'（B289：atmosphere of unrelieved tension）。",
    "波尔多与资产阶级生活的框架（B289）。"],
  "status": "Britannica 定位莫里亚克为法国天主教小说家、1952年诺奖得主（B289）；《蝮蛇结》常被视为其杰作（B289）。",
  "sources": ["B289"], "dates_source": "B289",
  "pending": ["《爱的荒漠》1925年出版细节核对。","《苔蕾丝》1950年电影改编待核。","《蝮蛇结》结构（书信体）待核。"]
},
"barnes": {
  "id": "barnes", "name": "朱利安·巴恩斯", "foreign_name": "Julian Barnes（朱利安·巴恩斯，1946-01-19— ）",
  "country": "英国", "birth": 1946, "death": None, "birth_year": 1946, "death_year": None, "era": "现当代",
  "summary": "巴恩斯，莱斯特人，英国批评家与作家——'British critic and author of inventive and intellectual novels about obsessed characters curious about the past'（以关于执迷于过去的人物的独创性智性小说著称——B290）。'Flaubert's Parrot (1984), Barnes's breakthrough novel, is a humorous mixture of biography, fiction, and literary criticism'（突破之作《福楼拜的鹦鹉》——B290）；2011年布克奖 The Sense of an Ending——'a Booker Prize-winning novel that uses an unreliable narrator to explore the subjects of memory and aging'（B290）。2026年 Departure(s) 自称最后一部小说（B290）。",
  "timeline": [
    {"year": 1946, "text": "1月19日生于莱斯特（B290：Born January 19, 1946, Leicester, England）。", "src": "B290"},
    {"year": 1984, "text": "《福楼拜的鹦鹉》出版（B290：Flaubert's Parrot (1984)——breakthrough）。", "src": "B290"},
    {"year": 2011, "text": "《终结的感觉》获布克奖（B290：Booker Prize 2011）。", "src": "B290"},
    {"year": 2026, "text": "Departure(s) 出版——自称最后一部小说（B290）。", "src": "B290"}],
  "major_works": [
    {"work_id": "fuloubaideyingwu", "note": "长篇（B290：1984，突破之作）"},
    {"title": "终结的感觉", "note": "（B290：2011布克奖）"},
    {"title": "10 1/2章世界史", "note": "（B290：A History of the World in 10½ Chapters (1989)）"}],
  "style": [
    "'inventive and intellectual novels about obsessed characters'（B290）。",
    "'幽默混合传记、虚构与文学批评'（B290——福楼拜的鹦鹉）。",
    "不可靠叙述者（B290：unreliable narrator——终结的感觉）。"],
  "status": "Britannica 定位巴恩斯为英国批评家与作家、2011年布克奖得主（B290）；2026年 Departure(s) 为其自称的最后一部小说（B290）。",
  "sources": ["B290"], "dates_source": "B290",
  "pending": ["1984年出版（Jonathan Cape说）核对。","杰弗里·布雷思韦特人名核对。","2026年 Departure(s) 细节（B290 已载）核对。"]
},
"oconnor": {
  "id": "oconnor", "name": "弗兰纳里·奥康纳", "foreign_name": "Flannery O'Connor（弗兰纳里·奥康纳，1925-03-25—1964-08-03）",
  "country": "美国", "birth": 1925, "death": 1964, "birth_year": 1925, "death_year": 1964, "era": "现当代",
  "summary": "奥康纳，佐治亚州萨凡纳人，美国小说家与短篇家——其小说多设于南方乡村，'probes the bond between individuals and God'（探察个人与上帝的联结——Britannica）；'regarded as a master of the Southern gothic, a style of writing often characterized by grotesque, macabre, or fantastic incidents'（南方哥特大师——B291）；暴力'is strangely capable of returning my characters to reality and preparing them to accept their moment of grace'（B291——作者自述引文）。红斑狼疮（承自父亲）致命，39岁去世（B291）。Complete Stories (1971) 获1972年国家图书奖（B291）。",
  "timeline": [
    {"year": 1925, "text": "3月25日生于佐治亚州萨凡纳（B291：Born March 25, 1925, Savannah, Georgia）。", "src": "B291"},
    {"year": 1952, "text": "首部长篇《慧血》出版（B291：Wise Blood (1952)）。", "src": "B291"},
    {"year": 1955, "text": "《好人难寻》短篇集出版（B291：A Good Man Is Hard to Find, and Other Stories (1955)）。", "src": "B291"},
    {"year": 1964, "text": "8月3日卒于米利奇维尔（B291：Died August 3, 1964, Milledgeville, Georgia）。", "src": "B291"},
    {"year": 1972, "text": "身后 Complete Stories 获国家图书奖（B291：National Book Award 1972）。", "src": "B291"}],
  "major_works": [
    {"work_id": "haorennanxun", "note": "短篇集（B291：1955）"},
    {"title": "慧血、暴力夺取", "note": "（B291：Wise Blood (1952), The Violent Bear It Away (1960)）"},
    {"title": "升 rise？——不：《上升的一切必将汇聚》", "note": "（B291：Everything That Rises Must Converge (1965)）"}],
  "style": [
    "南方哥特：'grotesque, macabre, or fantastic incidents'（B291）。",
    "暴力通向'恩典时刻'（B291 作者自述引文）。",
    "'The Misfit'——意外的救赎者（B291）。"],
  "status": "Britannica 定位奥康纳为南方哥特大师、'个人与上帝之联结'的探察者（B291）。",
  "sources": ["B291"], "dates_source": "B291",
  "pending": ["《好人难寻》九篇篇目核对。","'The Misfit'与老太太的对话待核。","《慧血》1952年出版核对。"]
},
"cather": {
  "id": "cather", "name": "薇拉·凯瑟", "foreign_name": "Willa Cather（薇拉·凯瑟，1873-12-07—1947-04-24）",
  "country": "美国", "birth": 1873, "death": 1947, "birth_year": 1873, "death_year": 1947, "era": "近代",
  "summary": "凯瑟，弗吉尼亚州温切斯特附近生，美国小说家——'celebrated for her depictions of settlers and frontier life on the Great Plains'（以大草原移民与边疆生活描写著称——Britannica），取材于内布拉斯加欧洲移民中的童年。'With O Pioneers! (1913) and My Ántonia (1918), which has frequently been adjudged her finest achievement'（《我的安东妮亚》常被裁定为其最佳成就——B292）；One of Ours (1922)——'won the Pulitzer Prize'（B292）；'Her unique regionalism captured the essence of the American West'（独特的地域主义捕捉了美国西部的本质——B292 引述）。",
  "timeline": [
    {"year": 1873, "text": "12月7日生于弗吉尼亚州温切斯特附近（B292：Born December 7, 1873, near Winchester, Virginia）。", "src": "B292"},
    {"year": 1913, "text": "《啊，拓荒者！》出版（B292：O Pioneers! (1913)）。", "src": "B292"},
    {"year": 1918, "text": "《我的安东妮亚》出版（B292：My Ántonia (1918)）。", "src": "B292"},
    {"year": 1922, "text": "《我们中的一个》获普利策奖（B292：One of Ours (1922), which won the Pulitzer Prize）。", "src": "B292"},
    {"year": 1947, "text": "4月24日卒于纽约（B292：Died April 24, 1947, New York City）。", "src": "B292"}],
  "major_works": [
    {"work_id": "wodeandongnia", "note": "长篇（B292：1918，'her finest achievement'之一）"},
    {"title": "啊，拓荒者！", "note": "（B292：1913）"},
    {"title": "我们中的一个", "note": "（B292：1922，普利策奖）"}],
  "style": [
    "边疆与移民：大草原的地域主义（B292：unique regionalism）。",
    "'精神与道德价值高于物质主义'（B292：spiritual and moral values over materialism）。",
    "拓荒者勇气与道德力量（B292 语境）。"],
  "status": "Britannica 定位凯瑟为美国小说家（《我的安东妮亚》常被裁定为其最佳成就）、普利策奖得主（B292）。",
  "sources": ["B292"], "dates_source": "B292",
  "pending": ["《我的安东妮亚》1918年出版（Houghton Mifflin说）核对。","安东妮亚·希默尔达/吉姆·伯登人名核对。","波西米亚移民史实待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"zaixifang": {
  "id":"zaixifang","title":"在西方的眼睛下","original_title":"Under Western Eyes","region":"英国","era":"近代","era_detail":"19世纪末",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"conrad","author_name":"约瑟夫·康拉德",
  "year_display":"1911年（作者页 B124 口径：在西方的眼睛下（1911））","year_sort":1911,
  "background":["作者页（B124）：康拉德 major_works 载'在西方的眼睛下（1911）'（B124 作者页定位，详见 heianddixin 条核对）。","题材（通说待核）：日内瓦的俄国革命者拉祖莫夫——告密与良心的'西方眼睛'下的自白。"],
  "outline":["拉祖莫夫的背叛与自白——'西方的眼睛'即叙述者（通说待核）。"],
  "characters":[{"name":"拉祖莫夫","identity":"学生","note":"（通说待核）"},{"name":"娜塔莉亚","identity":"姊妹","note":"（通说待核）"}],
  "themes":["革命伦理的灰色（通说待核）。",
   "陀思妥耶夫斯基式心理（康拉德自称与陀氏竞争——通说待核）。",
   "叙述的道德重量（通说）。"],
  "influence":[{"text":"作者页：康拉德政治小说（B124 作者页口径）。","source":"B124"},
   {"text":"作者页：康拉德对陀思妥耶夫斯基的态度（通说待核——B124 未载）。","source":"B124"}],
  "reading":{"difficulties":["俄国革命史。","康拉德最'俄国'的文本。"],
   "editions":["《在西方的眼睛下》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"康拉德政治小说之末。"},
  "pending":["1911年出版（Methuen说）核对。","拉祖莫夫/娜塔莉亚人名核对。","康拉德与陀氏关系待核。"],
  "sources":["B124"],"year_source":"B124","author_source":"B124","related_works":["heianddixin","jimuye","nuositeluomo"],
  "svg":G2("《在西方的眼睛下》良心结构图",[{"title":"告密","text":"拉祖莫夫的选择","color":"antagonist"},{"title":"自白","text":"西方的眼睛下","color":"main"},{"title":"革命者","text":"日内瓦的流亡者","color":"family"},{"title":"良心","text":"道德的灰色","color":"gold"}])
},
"buyi": {
  "id":"buyi","title":"布宜诺斯艾利斯的热情","original_title":"Fervor de Buenos Aires（The Passion of Buenos Aires）","region":"阿根廷","era":"现当代","era_detail":"20世纪",
  "genre":"诗集","genre_group":"诗歌","language":"西班牙语","author_id":"borges","author_name":"豪尔赫·路易斯·博尔赫斯",
  "year_display":"1923年（作者页 B095 口径：布宜诺斯艾利斯的热情（1923））","year_sort":1923,
  "background":["作者页（B095）：博尔赫斯 major_works 载'布宜诺斯艾利斯的热情（1923）'——其首部诗集（B095 作者页定位，详见 xiaojing 条核对）。","文体（通说待核）：极端的前博尔赫斯——都市抒情与街头刀光的诗歌起点。"],
  "outline":["布宜诺斯艾利斯的街巷、黄昏与匕首（通说待核）。"],
  "characters":[{"name":"年轻的博尔赫斯","identity":"诗人","note":"起点（通说待核）"}],
  "themes":["都市场景的诗化（通说待核）。",
   "'热情'的青年宣言（书名通说待核）。",
   "走向《虚构集》的起点（通说）。"],
  "influence":[{"text":"作者页：博尔赫斯作品谱系的起点（B095 作者页口径）。","source":"B095"},
   {"text":"作者页：博尔赫斯为拉美文学巨匠（B095 作者级定位）。","source":"B095"}],
  "reading":{"difficulties":["早期诗体的粗糙与热情。","布宜诺斯艾利斯地名。"],
   "editions":["《布宜诺斯艾利斯的热情》（收于博尔赫斯全集，通说待核）。","西班牙文原版。"],
   "order":"博尔赫斯诗歌起点。"},
  "pending":["1923年出版细节核对。","篇目核对。","后来自称'后悔'的早年诗集（作者态度）待核。"],
  "sources":["B095"],"year_source":"B095","author_source":"B095","related_works":["xiaojing","alaifu","shazhishu"],
  "svg":G2("《布宜诺斯艾利斯的热情》起点图",[{"title":"街区","text":"都市的诗","color":"main"},{"title":"匕首","text":"刀光的隐喻","color":"antagonist"},{"title":"黄昏","text":"布市的时刻","color":"gold"},{"title":"起点","text":"博尔赫斯的1923","color":"family"}])
},
"kulian": {
  "id":"kulian","title":"苦炼","original_title":"L'Oeuvre au noir（The Abyss）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"历史小说","genre_group":"小说","language":"法语","author_id":"yourcenar","author_name":"玛格丽特·尤瑟纳尔",
  "year_display":"1968年（Britannica：L'Oeuvre au noir (1968; The Abyss)——B285）","year_sort":1968,
  "background":["Britannica（B285）：'Another historical novel is L'Oeuvre au noir (1968; The Abyss)...'——另一部历史小说；作者文体：'rigorously classical style, their erudition, and their psychological subtlety'（B285）。","题材（通说待核）：16世纪佛兰德斯炼金术士/外科医生泽诺的一生——'苦炼'（the Work in Black）的炼金术隐喻。"],
  "outline":["泽诺的求知与流亡：从修道院到阿尔卑斯的处决（通说待核）。"],
  "characters":[{"name":"泽诺","identity":"炼金术士","note":"（通说待核）"}],
  "themes":["知识与自由的代价（通说待核）。",
   "'苦炼'：黑业（通说待核——炼金术术语）。",
   "文艺复兴的怀疑精神（通说）。"],
  "influence":[{"text":"Britannica：'Another historical novel is L'Oeuvre au noir (1968; The Abyss)...'（B285）。","source":"B285"},
   {"text":"作者页：尤瑟纳尔古典与博学（B285 作者级定位）。","source":"B285"}],
  "reading":{"difficulties":["文艺复兴与炼金术史。","尤瑟纳尔的古典语汇。"],
   "editions":["《苦炼》（上海三联书店版本，通说待核）。","法文原版（Gallimard）。"],
   "order":"先《哈德良回忆录》后本作。"},
  "pending":["1968年出版（Gallimard说）核对。","泽诺人物原型（真实炼金术士说）待核。","'苦炼'（Oeuvre au noir）术语核对。"],
  "sources":["B285"],"year_source":"B285","author_source":"B285","related_works":["hadilianghuiyilu","shenqu","niwanghechuqu"],
  "svg":G2("《苦炼》求知结构图",[{"title":"炼金术","text":"黑业（通说）","color":"gold"},{"title":"泽诺","text":"16世纪的求知者","color":"main"},{"title":"流亡","text":"自由的代价","color":"antagonist"},{"title":"处决","text":"怀疑的终点","color":"family"}])
},
"zuimingjing": {
  "id":"zuimingjing","title":"最明净的地区","original_title":"La región más transparente（Where the Air Is Clear）","region":"墨西哥","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"西班牙语","author_id":"fuentes","author_name":"卡洛斯·富恩特斯",
  "year_display":"出版年份待核（Britannica B287：'experimental, postmodern novels—including Where the Air Is Clear and The Death of Artemio Cruz'——1959年说通说待核）","year_sort":1959,
  "background":["Britannica（B287）：'experimental, postmodern novels——including Where the Air Is Clear and The Death of Artemio Cruz——explored Mexican identity and won him international acclaim'。","题材（通说待核）：墨西哥城全景——从革命到工业化的城市'明净'反讽。"],
  "outline":["多人物全景：银行家、矿工、夫人（通说待核）。","城市即主角（通说待核）。"],
  "characters":[{"name":"罗德里戈·波拉","identity":"银行家","note":"（通说待核）"}],
  "themes":["城市作为主角（通说待核）。",
   "墨西哥革命的遗产（通说）。",
   "'最明净'的反讽（书名通说待核）。"],
  "influence":[{"text":"Britannica：与《阿尔特米奥·克罗斯之死》并列的实验后现代小说（B287）。","source":"B287"},
   {"text":"作者页：富恩特斯'20世纪墨西哥最重要的作家之一'（B287 作者级）。","source":"B287"}],
  "reading":{"difficulties":["墨西哥城地名与历史。","多人物全景。"],
   "editions":["《最明净的地区》（上海译文出版社/人民文学出版社版本，通说待核）。","西班牙文原版（FCE）。"],
   "order":"富恩特斯处女作。"},
  "pending":["1959年出版（FCE说）核对。","罗德里戈·波拉人名核对。","处女作地位待核。"],
  "sources":["B287"],"year_source":"B287","author_source":"B287","related_works":["aertemio","bainian","huoluan"],
  "svg":G2("《最明净的地区》全景图",[{"title":"墨西哥城","text":"城市即主角（通说）","color":"main"},{"title":"革命遗产","text":"1910年的余波","color":"antagonist"},{"title":"全景","text":"多人物","color":"family"},{"title":"明净","text":"反讽的书名","color":"gold"}])
},
"xinyue": {
  "id":"xinyue","title":"欣悦的灵魂","original_title":"L'Âme enchantée（The Enchanted Soul）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说（七卷）","genre_group":"小说","language":"法语","author_id":"rolland","author_name":"罗曼·罗兰",
  "year_display":"1922—1933年（作者页 B276 口径：L'Âme-enchantée 1922–33）","year_sort":1922,
  "background":["作者页（B276）：罗兰 major_works 载'L'Âme-enchantée 1922–33'（B276 作者页定位，详见 yuehankelisituofu 条核对）。","题材（通说待核）：安乃德的'欣悦'之路——母性与神秘主义的演进。"],
  "outline":["安乃德的女性成长与'灵魂的欣悦'（通说待核）。"],
  "characters":[{"name":"安乃德","identity":"女性","note":"（通说待核）"}],
  "themes":["女性成长的'欣悦'（通说待核）。",
   "和平主义与神秘主义（B276 语境：committed to pacifism）。",
   "继《约翰·克利斯朵夫》之后的女性史诗（通说待核）。"],
  "influence":[{"text":"Britannica：罗兰 works 谱系（L'Âme-enchantée 1922–33）（B276）。","source":"B276"},
   {"text":"作者页：罗兰1915年诺奖（B276 作者级）。","source":"B276"}],
  "reading":{"difficulties":["七卷体量。","神秘主义段落。"],
   "editions":["《欣悦的灵魂》（中译本信息待核）。","法文原版（公有领域渐近）。"],
   "order":"罗兰两大河小说之二。"},
  "pending":["七卷卷名核对。","安乃德人名核对。","与《约翰·克利斯朵夫》的'女性对位'说待核。"],
  "sources":["B276"],"year_source":"B276","author_source":"B276","related_works":["yuehankelisituofu","beican","jian"],
  "svg":G2("《欣悦的灵魂》女性成长图",[{"title":"安乃德","text":"女性的一生","color":"main"},{"title":"欣悦","text":"灵魂的状态","color":"gold"},{"title":"和平主义","text":"罗兰的立场（B276）","color":"family"},{"title":"七卷","text":"1922—1933","color":"plain"}])
},
"aidewangmo": {
  "id":"aidewangmo","title":"爱的荒漠","original_title":"Le Désert de l'amour（The Desert of Love）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"mauriac","author_name":"弗朗索瓦·莫里亚克",
  "year_display":"1925年（Britannica：Le Désert de l'amour (1925; The Desert of Love)——'Mauriac showed increasing mastery'）","year_sort":1925,
  "background":["Britannica（B289）：'Mauriac showed increasing mastery in Le Désert de l'amour (1925; The Desert of Love)'（显示日益成熟的掌控——B289）。","题材（通说待核）：父子同恋一个女人的'荒漠'——波尔多医生库雷热一家。"],
  "outline":["父与子同爱玛丽亚——爱如荒漠（通说待核）。"],
  "characters":[{"name":"库雷热医生","identity":"父亲","note":"（通说待核）"},{"name":"库雷热之子","identity":"青年","note":"（通说待核）"},{"name":"玛丽亚","identity":"交际花","note":"（通说待核）"}],
  "themes":["'爱的荒漠'：欲望的无果（书名通说待核）。",
   "父子的暗战（通说待核）。",
   "天主教的悲悯（B289 语境：Catholic novelist）。"],
  "influence":[{"text":"Britannica：'Mauriac showed increasing mastery in Le Désert de l'amour (1925)'（B289）。","source":"B289"},
   {"text":"Britannica：1952年诺奖（B289 作者级）。","source":"B289"}],
  "reading":{"difficulties":["天主教叙事。","父子的心理镜像。"],
   "editions":["《爱的荒漠》（广西师范大学出版社，通说待核）。","法文原版（公有领域渐近）。"],
   "order":"先《爱的荒漠》后《苔蕾丝》《蝮蛇结》。"},
  "pending":["1925年出版核对。","库雷热父子/玛丽亚人名核对。","回忆的倒叙结构待核。"],
  "sources":["B289"],"year_source":"B289","author_source":"B289","related_works":["lianqingdezhongjie","richu","beiyi"],
  "svg":G2("《爱的荒漠》荒漠结构图",[{"title":"父与子","text":"同爱的对手","color":"main"},{"title":"玛丽亚","text":"荒漠中的绿洲","color":"gold"},{"title":"波尔多","text":"阴郁的城市（B289）","color":"family"},{"title":"荒漠","text":"爱的无果","color":"antagonist"}])
},
"fuloubaideyingwu": {
  "id":"fuloubaideyingwu","title":"福楼拜的鹦鹉","original_title":"Flaubert's Parrot","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"barnes","author_name":"朱利安·巴恩斯",
  "year_display":"1984年（Britannica：Flaubert's Parrot (1984), Barnes's breakthrough novel）","year_sort":1984,
  "background":["Britannica（B290）：'Flaubert's Parrot (1984), Barnes's breakthrough novel, is a humorous mixture of biography, fiction, and literary criticism'（幽默混合传记、虚构与文学批评——B290）；'was shortlisted for the Booker Prize'（入围布克奖——B290）。","作者（B290）：'inventive and intellectual novels about obsessed characters curious about the past'。"],
  "outline":["退休医生杰弗里追寻福楼拜的'那只鹦鹉'——传记、虚构与批评的混体（通说待核）。"],
  "characters":[{"name":"杰弗里·布雷思韦特","identity":"退休医生","note":"（通说待核）"},{"name":"福楼拜","identity":"作家","note":"被研究的对象"}],
  "themes":["'那只鹦鹉'：作家的真身在哪里（通说待核）。",
   "传记、虚构与批评的混合（B290）。",
   "寡居的哀悼（通说待核——妻子病亡线）。"],
  "influence":[{"text":"Britannica：'breakthrough novel'；'shortlisted for the Booker Prize'（B290）。","source":"B290"},
   {"text":"作者页：巴恩斯'obsessed characters curious about the past'（B290 作者级定位）。","source":"B290"}],
  "reading":{"difficulties":["文体拼贴（年表/考试卷/目录）。","福楼拜生平知识。"],
   "editions":["《福楼拜的鹦鹉》（译林出版社，通说待核）。","英文原版（Jonathan Cape）。"],
   "order":"巴恩斯入门首选。"},
  "pending":["1984年出版（Jonathan Cape说）核对。","杰弗里·布雷思韦特人名核对。","鹦鹉标本的'真假两只'细节待核。"],
  "sources":["B290"],"year_source":"B290","author_source":"B290","related_works":["weianzhihuo","xiaojing","mi"],
  "svg":G2("《福楼拜的鹦鹉》文体拼贴图",[{"title":"传记","text":"福楼拜的生平","color":"family"},{"title":"虚构","text":"杰弗里的追寻","color":"main"},{"title":"批评","text":"文学史的对话","color":"gold"},{"title":"鹦鹉","text":"两只的真伪","color":"antagonist"}])
},
"haorennanxun": {
  "id":"haorennanxun","title":"好人难寻","original_title":"A Good Man Is Hard to Find, and Other Stories","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"短篇小说集","genre_group":"小说","language":"英语","author_id":"oconnor","author_name":"弗兰纳里·奥康纳",
  "year_display":"1955年（Britannica：A Good Man Is Hard to Find, and Other Stories (1955)——'she came to be regarded as a master of the form'）","year_sort":1955,
  "background":["Britannica（B291）：同名篇创造'an unexpected agent of salvation in the character of an escaped convict called The Misfit'（逃犯'格格不入者'成为意外的救赎媒介——B291）；'regarded as a master of the Southern gothic, a style of writing often characterized by grotesque, macabre, or fantastic incidents'（B291）。","暴力（B291 作者自述引文）：'is strangely capable of returning my characters to reality and preparing them to accept their moment of grace'。"],
  "outline":["同名篇：老祖母一家遇逃犯'格格不入者'——枪响前的'恩典时刻'（通说待核）。","《人造黑人》《善良的乡下人》等（篇目通说待核）。"],
  "characters":[{"name":"老祖母","identity":"叙述对象","note":"（通说待核）"},{"name":"'格格不入者'（The Misfit）","identity":"逃犯","note":"（B291）"}],
  "themes":["暴力与'恩典时刻'（B291 作者自述）。",
   "南方哥特（B291：grotesque, macabre, or fantastic）。",
   "'好人'的反讽（篇名通说待核）。"],
  "influence":[{"text":"Britannica：'regarded as a master of the Southern gothic'（B291）。","source":"B291"},
   {"text":"Britannica：Complete Stories (1971) 获国家图书奖（B291 作者级）。","source":"B291"}],
  "reading":{"difficulties":["哥特暴力与恩典的语法。","南方宗教背景。"],
   "editions":["《好人难寻》（新星出版社/上海译文版本，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"奥康纳首选。"},
  "pending":["1955年出版（Harcourt, Brace说）核对。","老祖母/The Misfit对话核对。","1972年国家图书奖核对。"],
  "sources":["B291"],"year_source":"B291","author_source":"B291","related_works":["kafuxuan","burunv","jiugushi"],
  "svg":G2("《好人难寻》恩典结构图",[{"title":"老祖母","text":"末路的絮语","color":"family"},{"title":"The Misfit","text":"意外的救赎媒介（B291）","color":"antagonist"},{"title":"枪响","text":"恩典时刻（通说）","color":"main"},{"title":"南方哥特","text":"怪诞大师（B291）","color":"gold"}])
},
"wodeandongnia": {
  "id":"wodeandongnia","title":"我的安东妮亚","original_title":"My Ántonia","region":"美国","era":"近代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"cather","author_name":"薇拉·凯瑟",
  "year_display":"1918年（Britannica：My Ántonia (1918), which has frequently been adjudged her finest achievement）","year_sort":1918,
  "background":["Britannica（B292）：'It tells the story of Ántonia Shimerda, a daughter of Bohemian immigrants on the Nebraska frontier'（写内布拉斯加边疆波西米亚移民之女安东妮亚——B292）；'With O Pioneers! (1913) and My Ántonia (1918)……'（B292：characteristic themes of frontier spirit and courage——通说待核）。","地位（B292）：'frequently been adjudged her finest achievement'（常被裁定为其最佳成就）。"],
  "outline":["吉姆·伯登的回忆：波西米亚移民女安东妮亚在内布拉斯加边疆的一生（通说待核）。","'安东妮亚'：土地与母性（通说待核）。"],
  "characters":[{"name":"安东妮亚·希默尔达","identity":"移民之女","note":"（B292）"},{"name":"吉姆·伯登","identity":"叙述者","note":"（通说待核）"}],
  "themes":["移民与边疆（B292）。",
   "'安东妮亚'：土地的生命力（通说待核）。",
   "地域主义（B292：unique regionalism——作者级）。"],
  "influence":[{"text":"Britannica：'frequently been adjudged her finest achievement'（B292）。","source":"B292"},
   {"text":"Britannica：'unique regionalism captured the essence of the American West'（B292 作者级引述）。","source":"B292"}],
  "reading":{"difficulties":["移民史（波西米亚）。","回忆录框架。"],
   "editions":["《我的安东妮亚》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"先《啊，拓荒者！》后本作。"},
  "pending":["1918年出版（Houghton Mifflin说）核对。","安东妮亚/吉姆人名核对。","'K'字结尾的暗示待核。"],
  "sources":["B292"],"year_source":"B292","author_source":"B292","related_works":["fenwangyu","yijiubasi","huozhe"],
  "svg":G2("《我的安东妮亚》边疆结构图",[{"title":"内布拉斯加","text":"边疆的草原","color":"family"},{"title":"安东妮亚","text":"波西米亚移民之女（B292）","color":"main"},{"title":"吉姆","text":"回忆者","color":"gold"},{"title":"拓荒者","text":"勇气与道德力量（B292）","color":"plain"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
