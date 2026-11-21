# -*- coding: utf-8 -*-
"""流水线批次14：Britannica 新核 6 作家 6 部"""
import json, pathlib

new_src = [
{"id":"B310","title":"Guy de Maupassant — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Guy-de-Maupassant","type":"百科全书","verified":True,"covers":["maupassant","yisheng"],"note":"2026-11-21 核对：1850-08-05 Miromesnil城堡（迪耶普附近）生—1893-07-06巴黎卒（42岁）；'the greatest French short-story author'（约300篇）；Flaubert 门徒——'He is my disciple and I love him like a son'；Flaubert 1880年猝逝为'a grievous blow'；'Boule de suif' 1880年4月发表成名；Une Vie 与 Bel-Ami 仅见于 Notable Works 列表（正文无细节——年份通说待核：一生1883、漂亮朋友1885）"},
{"id":"B311","title":"Selma Lagerlof — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Selma-Lagerlof","type":"百科全书","verified":True,"covers":["lagerlof","qieelvxing"],"note":"2026-11-21 核对：1858-11-20瑞典 Mårbacka 生—1940-03-16卒（81岁）；'became the first woman and also the first Swedish writer to win the Nobel Prize for Literature'（1909）；Nils Holgerssons underbara resa genom Sverige 2卷 (1906–07)——'a geography reader for children'；诺贝尔奖金购回 Mårbacka 庄园；'ranks among the most naturally gifted of modern storytellers'；另有 Gösta Berlings saga"},
{"id":"B312","title":"Isaac Bashevis Singer — Encyclopaedia Britannica 与 Elias Canetti — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Isaac-Bashevis-Singer","type":"百科全书","verified":True,"covers":["singer","canetti"],"note":"2026-11-21 核对——辛格：生年'July 14?, 1903'（不确定，另有1904年11/10月说）Leoncin, Poland—1991-07-24 Surfside FL；1978诺奖；'the short story, Gimpel the Fool (1957)'；A Crown of Feathers (1973; National Book Award)；Yentl 电影(1983)改编自其故事；瑞典学院特别称赞 In My Father's Court (1966)；意第绪语写作。卡内蒂：1905-07-25保加利亚鲁塞生—1994-08-14苏黎世卒；1981诺奖；Die Blendung (1935; Auto-da-Fé)；'His major work, Masse und Macht (1960; Crowds and Power)'；'crowds……the psychopathology of power'"},
{"id":"B313","title":"Joseph Brodsky — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Joseph-Brodsky","type":"百科全书","verified":True,"covers":["brodsky","xiaoyuyi"],"note":"2026-11-21 核对：1940-05-24列宁格勒生—1996-01-28布鲁克林卒（55岁）；1987诺奖——'for his important lyric and elegiac poems'；1964年判5年苦役、1965年缩短；1972年被逐出苏联、1977年美国籍；MacArthur fellowship 1981；美国桂冠诗人1991–92；主要作品含'the essays in Less Than One (1986)'"},
{"id":"B314","title":"Winston Churchill — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Winston-Churchill","type":"百科全书","verified":True,"covers":["churchill","erzhanyihuilu"],"note":"2026-11-21 核对：1874-11-30布伦海姆宫生—1965-01-24伦敦卒（90岁）；两任首相（1940–45、1951–55）；诺贝尔奖1953（Quick Facts——正文无描述句）；'He excelled in the set speech, on which he always spent enormous pains'；有言语缺陷'until he never wholly lost'；The River War——'brilliantly describes the campaign'；Malakand 派遣稿'launch him on the career of authorship'；二战回忆录六卷（1948—54说）正文未载——通说待核"},
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
"maupassant": {
  "id": "maupassant", "name": "莫泊桑", "foreign_name": "Guy de Maupassant（基·德·莫泊桑，1850-08-05—1893-07-06）",
  "country": "法国", "birth": 1850, "death": 1893, "birth_year": 1850, "death_year": 1893, "era": "近代",
  "summary": "莫泊桑，米罗梅思尼尔堡（迪耶普附近）生，法国自然主义作家——'widely considered the greatest French short-story author'（公认法国最伟大的短篇作家——Britannica），约300篇短篇加长篇。福楼拜的门徒：'He is my disciple and I love him like a son'（Flaubert 语——B310）；Flaubert 1880年猝逝是'a grievous blow to Maupassant'（B310）。'Boule de suif'（1880年4月发表）成名（B310）。42岁早逝（B310）。",
  "timeline": [
    {"year": 1850, "text": "8月5日生于米罗梅思尼尔堡（B310：Born August 5, 1850, Château de Miromesnil? near Dieppe——出生地存疑）。", "src": "B310"},
    {"year": 1880, "text": "4月《羊脂球》发表成名；同年福楼拜猝逝（B310）。", "src": "B310"},
    {"year": 1890, "text": "《穆恰》出版（B310：Mouche published 1890）。", "src": "B310"},
    {"year": 1893, "text": "7月6日卒于巴黎（42岁）（B310）。", "src": "B310"}],
  "major_works": [
    {"work_id": "mauposangxuan", "note": "短篇选（约300篇短篇——B310）"},
    {"work_id": "yisheng", "note": "长篇（Notable Works 列表——B310）"},
    {"title": "漂亮朋友", "note": "（B310：Bel-Ami——Notable Works 列表；本库另条 piaoliangpengyou）"}],
  "style": [
    "'the greatest French short-story author'（B310）。",
    "'economy and objectivity'描写中下阶层（B310 语境）。",
    "福楼拜门徒（B310：Flaubert said of Maupassant）。"],
  "status": "Britannica 定位莫泊桑为法国最伟大的短篇作家（约300篇）、福楼拜门徒（B310）；梅毒致疯早逝说（通说待核）。",
  "sources": ["B310"], "dates_source": "B310",
  "pending": ["《一生》1883年、《漂亮朋友》1885年出版年份核对（B310 Quick Facts 口径）。", "梅毒与精神病院（1892年说）待核。", "出生地 Château de Miromesnil? 的问号（B310 已载）待核。"]
},
"lagerlof": {
  "id": "lagerlof", "name": "塞尔玛·拉格洛夫", "foreign_name": "Selma Lagerlöf（塞尔玛·拉格勒夫/拉格洛夫，1858-11-20—1940-03-16）",
  "country": "瑞典", "birth": 1858, "death": 1940, "birth_year": 1858, "death_year": 1940, "era": "现当代",
  "summary": "拉格洛夫，瑞典 Mårbacka 人，小说家——'celebrated for lyrical works like Gösta Berlings saga and The Wonderful Adventures of Nils'（以《古斯泰·贝林的故事》《尼尔斯骑鹅旅行记》等抒情之作著称——B311）；1909年'became the first woman and also the first Swedish writer to win the Nobel Prize for Literature'（首位女性与首位瑞典作家诺奖——B311）；以奖金购回 Mårbacka 庄园（B311）。'ranks among the most naturally gifted of modern storytellers'（现代最有天赋的讲故事者之一——B311）。",
  "timeline": [
    {"year": 1858, "text": "11月20日生于瑞典 Mårbacka（B311：Born Nov. 20, 1858, Mårbacka, Sweden）。", "src": "B311"},
    {"year": 1906, "text": "《尼尔斯骑鹅旅行记》2卷出版（1906–07）——'a geography reader for children'（B311）。", "src": "B311"},
    {"year": 1909, "text": "获诺贝尔文学奖（B311：first woman and first Swedish writer）。", "src": "B311"},
    {"year": 1940, "text": "3月16日卒于 Mårbacka（B311）。", "src": "B311"}],
  "major_works": [
    {"work_id": "qieelvxing", "note": "2卷（B311：1906–07，'a geography reader for children'）"},
    {"title": "古斯泰·贝林的故事", "note": "（B311：Gösta Berlings saga）"},
    {"title": "耶路撒冷", "note": "（通说待核）"}],
  "style": [
    "'最自然天赋的讲故事者之一'（B311：naturally gifted……storytellers）。",
    "抒情与传说融合（B311 语境：lyrical works）。",
    "地理读本与童话的嫁接（B311：geography reader for children）。"],
  "status": "Britannica 定位拉格洛夫为1909年诺奖得主（首位女性、首位瑞典获奖者）、'现代最有天赋的讲故事者之一'（B311）。",
  "sources": ["B311"], "dates_source": "B311",
  "pending": ["《尼尔斯骑鹅旅行记》中译本（高子英等说）待核。","1909年诺奖授奖词待核。","《古斯泰·贝林的故事》1891年说待核。"]
},
"singer": {
  "id": "singer", "name": "艾萨克·巴什维斯·辛格", "foreign_name": "Isaac Bashevis Singer（艾萨克·巴什维斯·辛格，1903—1991-07-24；生年存疑）",
  "country": "美国", "birth": 1903, "death": 1991, "birth_year": 1903, "death_year": 1991, "era": "现当代",
  "summary": "辛格，波兰莱翁钦生（出生日期不确定——B312：Born July 14?, 1903, Leoncin, Poland……year possibly 1904），波兰裔美国作家——以意第绪语写长篇、短篇与散文，1978年获诺贝尔文学奖（B312）。'His fiction depicts Jewish life in Poland and the United States, blending irony, wit, and wisdom with the occult and grotesque'（写波兰与美国的犹太生活，融合反讽、机智、智慧与神秘怪诞——B312）。瑞典学院特别称赞其'in My Father's Court (1966)'（B312）。",
  "timeline": [
    {"year": 1903, "text": "生于波兰莱翁钦（出生日期不确定——B312：Born July 14?, 1903……year possibly 1904）。", "src": "B312"},
    {"year": 1935, "text": "移民美国（1935年说——通说待核）。", "src": "B312"},
    {"year": 1978, "text": "获诺贝尔文学奖（B312：Nobel Prize for Literature 1978）。", "src": "B312"},
    {"year": 1991, "text": "7月24日卒于佛罗里达州瑟夫赛德（B312：Died July 24, 1991, Surfside, Florida）。", "src": "B312"}],
  "major_works": [
    {"work_id": "shagua", "note": "短篇（B312：Gimpel the Fool (1957)）"},
    {"title": "羽毛冠", "note": "（B312：A Crown of Feathers (1973; National Book Award)）"},
    {"title": "卢布林的魔术师", "note": "（通说待核——B312 未载）"}],
  "style": [
    "'blending irony, wit, and wisdom with the occult and grotesque'（B312）。",
    "意第绪语写作（B312：novels, short stories, and essays in Yiddish）。",
    "魔鬼与怪诞（通说待核——其恶魔故事）。"],
  "status": "Britannica 定位辛格为意第绪语作家、1978年诺奖得主（B312）；瑞典学院特别称赞《在父亲的法庭上》（B312）。",
  "sources": ["B312"], "dates_source": "B312",
  "pending": ["生年与出生日期的多说并存核对。", "《卢布林的魔术师》1960年说待核。", "《傻瓜吉姆佩尔》与《迈塞斯》关系待核。"]
},
"canetti": {
  "id": "canetti", "name": "埃利亚斯·卡内蒂", "foreign_name": "Elias Canetti（埃利亚斯·卡内蒂，1905-07-25—1994-08-14）",
  "country": "英国", "birth": 1905, "death": 1994, "birth_year": 1905, "death_year": 1994, "era": "现当代",
  "summary": "卡内蒂，保加利亚鲁塞生、德语写作的小说家与剧作家（Britannica：Bulgarian-born, German-language novelist and playwright）——写群体心理学与权力：'His major work, Masse und Macht (1960; Crowds and Power), is an outgrowth of that interest'（B312 语境）；1981年获诺贝尔文学奖（B312）。《迷惑》——'A planned eight-novel saga of the disorder he saw around him was reduced to Die Blendung (1935; Auto-da-Fé, or The Tower of Babel)'（原计划八部曲缩减为一部——B312 语境）。",
  "timeline": [
    {"year": 1905, "text": "7月25日生于保加利亚鲁塞（B312：Born July 25, 1905, Ruse, Bulg.）。", "src": "B312"},
    {"year": 1935, "text": "《迷惑》出版（B312：Die Blendung (1935)）。", "src": "B312"},
    {"year": 1960, "text": "《群众与权力》出版（B312：Masse und Macht (1960)——'His major work'）。", "src": "B312"},
    {"year": 1981, "text": "获诺贝尔文学奖（B312：Nobel Prize 1981）。", "src": "B312"},
    {"year": 1994, "text": "8月14日卒于苏黎世（B312：died Aug. 14, 1994, Zürich, Switz.）。", "src": "B312"}],
  "major_works": [
    {"work_id": "mihuo", "note": "长篇（B312：Die Blendung (1935)）"},
    {"title": "群众与权力", "note": "（B312：Masse und Macht (1960)——'His major work'）"},
    {"title": "获救之舌", "note": "自传（通说待核）"}],
  "style": [
    "'crowds, the psychopathology of power'（B312 语境）。",
    "个体与社会的对峙（B312：the position of the individual at odds）。",
    "巴洛式狂想文体（通说待核）。"],
  "status": "Britannica 定位卡内蒂为保加利亚出生德语作家、1981年诺奖得主（B312）。",
  "sources": ["B312"], "dates_source": "B312",
  "pending": ["《迷惑》1935/1936出版（Herbert Reichner说）核对。","汉斯/彼得·基恩人名核对。","1981诺奖授奖词待核。"]
},
"brodsky": {
  "id": "brodsky", "name": "约瑟夫·布罗茨基", "foreign_name": "Joseph Brodsky（约瑟夫·布罗茨基，1940-05-24—1996-01-28）",
  "country": "美国", "birth": 1940, "death": 1996, "birth_year": 1940, "death_year": 1996, "era": "现当代",
  "summary": "布罗茨基，列宁格勒生，'a Russian-born American poet'（俄国出生的美国诗人——B313）——1987年获诺贝尔文学奖 'for his important lyric and elegiac poems'（抒情诗与挽歌——B313）。1964年判5年苦役（1965缩短）；1972年被逐出苏联，此后居美国（B313：Exiled from the Soviet Union in 1972）；MacArthur fellowship 1981；美国桂冠诗人1991–92（B313）。主要作品含'the essays in Less Than One (1986)'（B313）。",
  "timeline": [
    {"year": 1940, "text": "5月24日生于列宁格勒（B313：Born May 24, 1940, Leningrad）。", "src": "B313"},
    {"year": 1964, "text": "判5年苦役（1965年缩短）（B313：Sentenced 1964……commuted 1965）。", "src": "B313"},
    {"year": 1972, "text": "被逐出苏联（B313：Exiled from the Soviet Union in 1972）。", "src": "B313"},
    {"year": 1987, "text": "获诺贝尔文学奖（B313）。", "src": "B313"},
    {"year": 1996, "text": "1月28日卒于布鲁克林（B313）。", "src": "B313"}],
  "major_works": [
    {"work_id": "xiaoyuyi", "note": "散文集（B313：Less Than One (1986)）"},
    {"title": "诗选", "note": "（通说待核）"},
    {"title": "水印", "note": "（通说待核）"}],
  "style": [
    "'lyric and elegiac poems'（B313 授奖词）。",
    "流亡诗学（B313：exiled……settled in the United States）。",
    "英语散文随笔（B313：Less Than One）。"],
  "status": "Britannica 定位布罗茨基为1987年诺奖得主、俄国出生的美国诗人（B313）；美国桂冠诗人1991–92（B313）。",
  "sources": ["B313"], "dates_source": "B313",
  "pending": ["流亡罪名（'社会寄生'说）待核。","《小于一》1986年出版（Farrar, Straus说）核对。","'诗歌应该像步枪射击'说待核。"]
},
"churchill": {
  "id": "churchill", "name": "温斯顿·丘吉尔", "foreign_name": "Winston Churchill（温斯顿·丘吉尔，1874-11-30—1965-01-24）",
  "country": "英国", "birth": 1874, "death": 1965, "birth_year": 1874, "death_year": 1965, "era": "现当代",
  "summary": "丘吉尔，牛津郡布伦海姆宫生，英国政治家——两任首相（1940–45、1951–55——B314）；1953年获诺贝尔文学奖（B314 Quick Facts）。演说（B314）：'He excelled in the set speech, on which he always spent enormous pains'；曾有言语缺陷'until he never wholly lost'；The River War——'brilliantly describes the campaign'；马拉坎德派遣稿'launch him on the career of authorship'（B314）。",
  "timeline": [
    {"year": 1874, "text": "11月30日生于牛津郡布伦海姆宫（B314：Born November 30, 1874, Blenheim Palace）。", "src": "B314"},
    {"year": 1898, "text": "《马拉坎德野战军纪实》出版（B314：The Story of the Malakand Field Force (1898)）。", "src": "B314"},
    {"year": 1940, "text": "首任首相（1940–45——B314）。", "src": "B314"},
    {"year": 1953, "text": "获诺贝尔文学奖（B314：Nobel Prize 1953——Quick Facts）。", "src": "B314"},
    {"year": 1965, "text": "1月24日卒于伦敦（B314）。", "src": "B314"}],
  "major_works": [
    {"work_id": "erzhanyihuilu", "note": "回忆录六卷（1948—54说——通说待核；B314 正文未载）"},
    {"title": "马拉坎德野战军纪实、河流战争", "note": "（B314：1898/1899）"},
    {"title": "英语民族史", "note": "（通说待核）"}],
  "style": [
    "'set speech'的苦工（B314：enormous pains）。",
    "'heavy but not very mobile guns'（Balfour 语——B314 转引）。",
    "历史书写以演说家笔法（通说待核）。"],
  "status": "Britannica 定位丘吉尔为英国政治家、1953年诺贝尔文学奖得主（B314 Quick Facts）；两次首相（B314）。",
  "sources": ["B314"], "dates_source": "B314",
  "pending": ["《第二次世界大战回忆录》六卷（1948—1954，Houghton Mifflin说）核对——B314 正文未载。","1953诺奖授奖词（'master of historical description'说）待核。","《英语民族史》四卷说待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"yisheng": {
  "id":"yisheng","title":"一生","original_title":"Une Vie（A Woman's Life）","region":"法国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"maupassant","author_name":"居·德·莫泊桑",
  "year_display":"出版年份待核（Britannica B310：Notable Works 列表载'A Woman's Life'——1883年说通说待核）","year_sort":1883,
  "background":["Britannica（B310）：莫泊桑 major works Quick Facts 载'A Woman's Life'（一生）——正文未载细节（通说待核：约娜的诺曼底庄园故事）。","作者（B310）：'widely considered the greatest French short-story author'，约300篇短篇；福楼拜门徒——'He is my disciple and I love him like a son'。"],
  "outline":["约娜的一生：修道院→婚姻→丈夫的背叛→儿子的堕落（通说待核）。","诺曼底庄园的四季（通说待核）。"],
  "characters":[{"name":"约娜","identity":"女庄园主","note":"（通说待核）"},{"name":"于连","identity":"丈夫","note":"（通说待核）"}],
  "themes":["女性一生的幻灭（通说待核）。",
   "诺曼底乡土（通说）。",
   "自然主义的婚姻解剖（通说待核）。"],
  "influence":[{"text":"Britannica：莫泊桑 Notable Works 含'A Woman's Life'（B310）。","source":"B310"},
   {"text":"Britannica：莫泊桑为福楼拜门徒、'greatest French short-story author'（B310）。","source":"B310"}],
  "reading":{"difficulties":["长篇的心理铺陈。","诺曼底庄园生活。"],
   "editions":["《一生》（人民文学出版社，通说待核）。","法文原版（公有领域）。"],
   "order":"先短篇后《一生》。"},
  "pending":["1883年出版（Victor Havard说）核对。","约娜/于连人名核对。","《漂亮朋友》1885年说待核。"],
  "sources":["B310"],"year_source":"B310","author_source":"B310","related_works":["piaoliangpengyou","baofali","ouhengliduanpianxuan"],
  "svg":G2("《一生》约娜一生图",[{"title":"修道院","text":"梦的开始","color":"family"},{"title":"婚姻","text":"于连的背叛","color":"antagonist"},{"title":"儿子","text":"二次幻灭","color":"gold"},{"title":"约娜","text":"一生如寄","color":"main"}])
},
"qieelvxing": {
  "id":"qieelvxing","title":"骑鹅旅行记","original_title":"Nils Holgerssons underbara resa genom Sverige（The Wonderful Adventures of Nils）","region":"瑞典","era":"现当代","era_detail":"20世纪初",
  "genre":"童话（2卷）","genre_group":"故事集","language":"瑞典语","author_id":"lagerlof","author_name":"塞尔玛·拉格洛夫",
  "year_display":"1906—1907年2卷出版（Britannica：2 vol. (1906–07)——'a geography reader for children'）","year_sort":1906,
  "background":["Britannica（B311）：'Nils Holgerssons underbara resa genom Sverige, 2 vol. (1906–07; The Wonderful Adventures of Nils and Further Adventures of Nils)'——'a geography reader for children'（给孩子的地理读本——B311）。","作者（B311）：1909年诺奖——'first woman and also the first Swedish writer'；'ranks among the most naturally gifted of modern storytellers'。"],
  "outline":["顽童尼尔斯变小、骑鹅随雁群纵贯瑞典——地理读本与童话的嫁接（通说待核）。"],
  "characters":[{"name":"尼尔斯","identity":"顽童","note":"（通说待核）"},{"name":"阿卡","identity":"领头雁","note":"（通说待核）"}],
  "themes":["瑞典地理的童话化（B311：geography reader）。",
   "变小的成长（通说待核）。",
   "人与自然的温柔（通说）。"],
  "influence":[{"text":"Britannica：'a geography reader for children'——教育与文学的双重设计（B311）。","source":"B311"},
   {"text":"作者页：拉格洛夫'现代最有天赋的讲故事者之一'（B311 作者级定位）。","source":"B311"}],
  "reading":{"difficulties":["瑞典地名与地理。","童话与地理读本的切换。"],
   "editions":["《骑鹅旅行记》（人民文学出版社/中国少年儿童出版社版本，通说待核）。","瑞典文原版。"],
   "order":"诺奖童话首选。"},
  "pending":["1906—07年2卷出版社说核对。","尼尔斯/阿卡人名核对。","原为教育委员会委托说待核。"],
  "sources":["B311"],"year_source":"B311","author_source":"B311","related_works":["antushengtonghua","wodeandongnia","gelintonghua"],
  "svg":G2("《骑鹅旅行记》雁群地图",[{"title":"变小","text":"狐仙的魔法（通说）","color":"gold"},{"title":"雁群","text":"纵贯瑞典","color":"main"},{"title":"尼尔斯","text":"顽童的成长","color":"family"},{"title":"地理读本","text":"教育设计（B311）","color":"plain"}])
},
"shagua": {
  "id":"shagua","title":"傻瓜吉姆佩尔","original_title":"Gimpel the Fool（גימפל תאַמ）","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"短篇小说","genre_group":"小说","language":"意第绪语","author_id":"singer","author_name":"艾萨克·巴什维斯·辛格",
  "year_display":"1957年（Britannica B312：'the short story, Gimpel the Fool (1957)'）","year_sort":1957,
  "background":["Britannica（B312）：'the short story, Gimpel the Fool (1957)'——辛格 best-known works 之一；作者：'blending irony, wit, and wisdom with the occult and grotesque'（B312 作者级定位）。","题材（通说待核）：圣彼得堡？——不：犹太村里被愚弄的面包师吉姆佩尔的'信仰'与'魔鬼'对话。"],
  "outline":["吉姆佩尔被全村愚弄——魔鬼的怂恿与最终的宽恕出走（通说待核）。"],
  "characters":[{"name":"吉姆佩尔","identity":"面包师","note":"（通说待核）"},{"name":"埃尔卡","identity":"妻子","note":"（通说待核）"}],
  "themes":["'傻瓜'的信仰（通说待核——以撒·辛格式）。",
   "魔鬼与犹太神秘主义（通说待核）。",
   "宽恕与出走（通说待核）。"],
  "influence":[{"text":"Britannica：辛格 best-known works 含'Gimpel the Fool (1957)'（B312）。","source":"B312"},
   {"text":"Britannica：辛格1978年诺奖（B312 作者级定位）。","source":"B312"}],
  "reading":{"difficulties":["意第绪语背景（中译自英译）。","犹太神秘主义（通说待核）。"],
   "editions":["《傻瓜吉姆佩尔》（收于辛格短篇集，通说待核）。","英译（Saul Bellow 译——通说待核）。"],
   "order":"辛格短篇首选。"},
  "pending":["1957年（《评论》Translation说）核对。","吉姆佩尔/埃尔卡人名核对。","贝娄英译（1957《常青树评论》说）待核。"],
  "sources":["B312"],"year_source":"B312","author_source":"B312","related_works":["haorennanxun","jiugushi","luoshengmen"],
  "svg":G2("《傻瓜吉姆佩尔》信仰结构图",[{"title":"吉姆佩尔","text":"被愚弄的面包师","color":"main"},{"title":"魔鬼","text":"怂恿的声音","color":"antagonist"},{"title":"宽恕","text":"出走与流浪","color":"gold"},{"title":"信仰","text":"傻瓜的智慧","color":"family"}])
},
"mihuo": {
  "id":"mihuo","title":"迷惑","original_title":"Die Blendung（Auto-da-Fé）","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"canetti","author_name":"埃利亚斯·卡内蒂",
  "year_display":"1935年（Britannica：Die Blendung (1935; Auto-da-Fé, or The Tower of Babel)）","year_sort":1935,
  "background":["Britannica（B312）：'A planned eight-novel saga of the disorder he saw around him was reduced to Die Blendung (1935; Auto-da-Fé, or The Tower of Babel)'——原计划八部曲缩为一部。","作者（B312）：1981诺奖；'His major work, Masse und Macht (1960; Crowds and Power)'；'crowds, the psychopathology of power'（B312 语境）。"],
  "outline":["汉学家彼得·基恩的藏书与房间——被女仆与'弟弟'逐出家门（通说待核）。","藏书之火（通说待核）。"],
  "characters":[{"name":"彼得·基恩","identity":"汉学家","note":"（通说待核）"},{"name":"泰蕾兹","identity":"女仆","note":"（通说待核）"}],
  "themes":["藏书人自焚的寓言（通说待核）。",
   "群众与权力的先声（B312：Masse und Macht 语境）。",
   "知识分子的脆弱（通说待核）。"],
  "influence":[{"text":"Britannica：'A planned eight-novel saga……was reduced to Die Blendung (1935)'（B312）。","source":"B312"},
   {"text":"作者页：卡内蒂1981年诺奖（B312 作者级定位）。","source":"B312"}],
  "reading":{"difficulties":["巴洛式狂想文体。","书痴心理。"],
   "editions":["《迷惑》（中译本信息待核）。","德文原版（Herbert Reichner）。"],
   "order":"先《迷惑》后《群众与权力》。"},
  "pending":["1935/1936出版核对。","彼得·基恩/泰蕾兹人名核对。","书名 Auto-da-Fé（火刑）的题解待核。"],
  "sources":["B312"],"year_source":"B312","author_source":"B312","related_works":["dashiyumageeligeta","di'ertiaojugui","muqin_brecht"],
  "svg":G2("《迷惑》藏书火图",[{"title":"藏书","text":"两万五千册（通说）","color":"family"},{"title":"基恩","text":"书痴的疯狂","color":"main"},{"title":"火","text":"Auto-da-Fé（B312）","color":"antagonist"},{"title":"群众","text":"《群众与权力》的先声","color":"gold"}])
},
"xiaoyuyi": {
  "id":"xiaoyuyi","title":"小于一","original_title":"Less Than One","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"散文集","genre_group":"散文","language":"英语","author_id":"brodsky","author_name":"约瑟夫·布罗茨基",
  "year_display":"1986年（作者页 B313 口径：the essays in Less Than One (1986)）","year_sort":1986,
  "background":["作者页（B313）：布罗茨基 major works 含'the essays in Less Than One (1986)'（B313 作者页定位）。","作者（B313）：1987年诺奖——'for his important lyric and elegiac poems'；1972年被逐出苏联；美国桂冠诗人1991–92。"],
  "outline":["彼得堡童年、阿赫玛托娃、茨维塔耶娃、Riga？——不：流亡与诗的散文自白（篇目通说待核）。"],
  "characters":[{"name":"布罗茨基","identity":"散文作者","note":"（B313）"}],
  "themes":["流亡与语言（通说待核）。",
   "诗人的前辈（阿赫玛托娃等——通说待核）。",
   "'小于一'：自我的减法（通说待核）。"],
  "influence":[{"text":"作者页：布罗茨基散文代表作（B313 作者页口径）。","source":"B313"},
   {"text":"作者页：1987年诺奖——'lyric and elegiac poems'（B313 作者级）。","source":"B313"}],
  "reading":{"difficulties":["散文的诗性密度。","俄苏文学史背景。"],
   "editions":["《小于一》（浙江大学出版社/上海译文版本，通说待核）。","英文原版（Farrar, Straus）。"],
   "order":"布罗茨基散文首选。"},
  "pending":["篇目（ Less Than One/Praise of Boredom 等）核对。","1986年出版（Farrar, Straus and Giroux说）核对。","'诗歌是语言的最高的存在形式'说待核。"],
  "sources":["B313"],"year_source":"B313","author_source":"B313","related_works":["anhunqu","ershoushijian","mengtiansuibi"],"x_placeholder":None,
  "svg":G2("《小于一》流亡散文图",[{"title":"彼得堡","text":"童年的语言","color":"family"},{"title":"流亡","text":"1972年出走（B313）","color":"antagonist"},{"title":"前辈诗人","text":"阿赫玛托娃等","color":"gold"},{"title":"小于一","text":"自我的减法","color":"main"}])
},
"erzhanyihuilu": {
  "id":"erzhanyihuilu","title":"第二次世界大战回忆录","original_title":"The Second World War（六卷）","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"回忆录（六卷）","genre_group":"散文","language":"英语","author_id":"churchill","author_name":"温斯顿·丘吉尔",
  "year_display":"1948—1954年六卷出版（通说待核；Britannica B314 正文未载——仅 Nobel Prize 1953 Quick Facts）","year_sort":1948,
  "background":["作者页（B314）：丘吉尔诺贝尔奖 1953（Quick Facts——'Nobel Prize (1953)'）；演说（B314）：'He excelled in the set speech, on which he always spent enormous pains'。","六卷（1948—54说——通说待核）；1953年诺奖授奖词（'master of historical description'说——通说待核）。"],
  "outline":["六卷：风云紧急/最光辉的时刻/伟大的同盟/命运的关键/紧缩包围圈/胜利与悲剧（卷名通说待核）。"],
  "characters":[{"name":"丘吉尔","identity":"首相·作者","note":"（B314）"}],
  "themes":["战时 memoir 与历史书写（通说待核）。",
   "'胜利不惜一切代价'的演说（通说待核）。",
   "英语民族的历史叙事（通说待核）。"],
  "influence":[{"text":"Britannica：丘吉尔诺贝尔奖 1953（B314 Quick Facts）。","source":"B314"},
   {"text":"作者页：'He excelled in the set speech'（B314）。","source":"B314"}],
  "reading":{"difficulties":["六卷体量。","二战史全景。"],
   "editions":["《第二次世界大战回忆录》（商务印书馆/译林版本，通说待核）。","英文原版（Cassell/Houghton Mifflin）。"],
   "order":"对照《第一次世界大战回忆录》（通说——丘吉尔 World Crisis）。"},
  "pending":["六卷卷名与年份核对。","1953诺奖授奖词（'master of historical description'说）核对。","'The Second World War'书名（六卷本各卷名）待核。"],
  "sources":["B314"],"year_source":"B314","author_source":"B314","related_works":["zhanzheng","yijiubasi","gulage"],
  "svg":G2("《二战回忆录》六卷结构图",[{"title":"风云紧急","text":"卷一（通说）","color":"family"},{"title":"最光辉的时刻","text":"卷二（通说）","color":"main"},{"title":"命运的关键","text":"卷四（通说）","color":"gold"},{"title":"胜利与悲剧","text":"卷六（通说）","color":"antagonist"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
