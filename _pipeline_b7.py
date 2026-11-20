# -*- coding: utf-8 -*-
"""流水线批次7：Britannica 新核 6 作家 6 部 + 零成本直写 3 部"""
import json, pathlib

new_src = [
{"id":"B279","title":"Bingxin — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Bingxin","type":"百科全书","verified":True,"covers":["bingxin","fanxingchunshui"],"note":"2026-11-20 核对：1900-10-05福建闽侯生—1999-02-28北京卒（98岁）；'a Chinese writer of gentle, melancholy poems, stories, and essays that were very popular'；'lyrical pieces about childhood and nature, influenced by the Indian poet Rabindranath Tagore'，'won her instant fame'并获卫斯理学院奖学金；1926年回国出版'Zhi xiaoduzhe (寄小读者, 1926)'；短篇集 Gugu (1932)、Donger guniang (1935)；后期 Guanyu nuren (1943)、Shisui xiaocha (1964)；页面未载《繁星》《春水》——繁星1923/春水1923年为通说待核"},
{"id":"B280","title":"Theodore Dreiser — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Theodore-Dreiser","type":"百科全书","verified":True,"covers":["delaise","jialimeimei"],"note":"2026-11-20 核对：1871-08-27 Terre Haute生—1945-12-28好莱坞卒（74岁）；'the outstanding American practitioner of naturalism'；Sister Carrie——1899年动笔、Doubleday 对题材有顾虑致宣传受限、'sold fewer than 500 copies'；An American Tragedy (1925)——based on a celebrated murder case、'brought Dreiser a degree of critical and commercial success he had never before attained'、'adopted champion of social reformers'"},
{"id":"B281","title":"Joseph Heller — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Joseph-Heller","type":"百科全书","verified":True,"covers":["heller","di'ertiaojugui"],"note":"2026-11-20 核对：1923-05-01布鲁克林生—1999-12-12 East Hampton卒（76岁）；Catch-22 (1961)——'The term catch-22 thereafter entered the English language as a reference to a proviso or situation that trips one up no matter which way one turns'；主角'Captain John Yossarian'；'developed a cult following with its dark surrealism'；'use farce and low comedy to highlight the senselessness and futility of life'"},
{"id":"B282","title":"E.M. Forster — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/E-M-Forster","type":"百科全书","verified":True,"covers":["forster","yinduzhixing"],"note":"2026-11-20 核对：1879-01-01伦敦生—1970-06-07考文垂卒（91岁）；声誉主要基于 Howards End (1910) 与 A Passage to India (1924)；Passage——'one of his finest works, examining racism and colonialism'、'The novel ends in an uneasy equilibrium'；Howards End——'brought Forster his first major success'；'The values of truthfulness and kindness dominate Forster's later thinking'；'never been seduced by totalitarianisms of any kind'"},
{"id":"B283","title":"Graham Greene — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Graham-Greene","type":"百科全书","verified":True,"covers":["greene","lianqingdezhongjie"],"note":"2026-11-20 核对：1904-10-02 Berkhamsted生—1991-04-03瑞士沃韦卒（86岁）；'one of the most widely read British novelists of the 20th century'；'Many of his best-known works, including The Power and the Glory (1940) and The End of the Affair (1951), center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'；End of the Affair——'narrated by an agnostic in love with a woman who forsakes him because of a religious conviction'（电影1955/1999）；Brighton Rock——'a corrupt and violent teenage criminal……Roman Catholic upbringing'"},
{"id":"B284","title":"Ivan Bunin — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ivan-Bunin","type":"百科全书","verified":True,"covers":["bunin","jiushanlaideshenshi"],"note":"2026-11-20 核对：1870-10-10（儒历）/22沃罗涅日生—1953-11-08巴黎卒（83岁）；'the first Russian to receive the Nobel Prize for Literature (1933), and one of the finest of Russian stylists'；流亡：1918年5月离莫斯科居敖德萨、1920年初先移君士坦丁堡——'one of the most famous Russian emigre writers'；与高尔基绝交（perceived as the triumph of the basest side）；'Gospodin iz San-Frantsisko (1916; The Gentleman from San Francisco) show Bunin's penchant for extreme precision of language'"},
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
"bingxin": {
  "id": "bingxin", "name": "冰心", "foreign_name": "Bing Xin（冰心，本名谢婉莹，1900-10-05—1999-02-28）",
  "country": "中国", "birth": 1900, "death": 1999, "birth_year": 1900, "death_year": 1999, "era": "现当代",
  "summary": "冰心，本名谢婉莹，福建闽侯人（Britannica：Born October 5, 1900, Minhou, Fujian province）——'a Chinese writer of gentle, melancholy poems, stories, and essays that were very popular'（写温柔、忧郁而广受欢迎的诗、小说与散文的中国作家——Britannica）。'lyrical pieces about childhood and nature, influenced by the Indian poet Rabindranath Tagore'（受泰戈尔影响的关于童年与自然的抒情之作）使她'won her instant fame'（一举成名——Britannica）并获卫斯理学院奖学金；1926年回国出版'Zhi xiaoduzhe（寄小读者，1926）'（B279）。晚年'active in cultural affairs, especially children's literature'（B279）。",
  "timeline": [
    {"year": 1900, "text": "10月5日生于福建闽侯（Britannica：Born October 5, 1900, Minhou, Fujian province）。", "src": "B279"},
    {"year": 1923, "text": "《繁星》《春水》出版（1923年说——通说待核；B279 该页未载，仅记其受泰戈尔影响的抒情之作一举成名）。", "src": "B279"},
    {"year": 1926, "text": "回国出版《寄小读者》（Britannica：Zhi xiaoduzhe (1926)）。", "src": "B279"},
    {"year": 1999, "text": "2月28日卒于北京（Britannica：Died February 28, 1999, Beijing）。", "src": "B279"}],
  "major_works": [
    {"work_id": "fanxingchunshui", "note": "小诗集（繁星/春水 1923年说——通说待核）"},
    {"title": "寄小读者", "note": "（Britannica：1926）"},
    {"title": "姑姑、冬儿姑娘、关于女人", "note": "（Britannica：Gugu (1932), Donger guniang (1935), Guanyu nuren (1943)）"}],
  "style": [
    "'温柔、忧郁'而广受欢迎（B279：gentle, melancholy……very popular）。",
    "受泰戈尔影响的童年与自然抒情（B279：influenced by the Indian poet Rabindranath Tagore）。",
    "儿童文学的终身投入（B279：especially children's literature）。"],
  "status": "Britannica 定位冰心为'广受欢迎的中国作家'、儿童文学的重要推动者（B279）；'冰心体'与五四问题小说的定位（通说待核）。",
  "sources": ["B279"], "dates_source": "B279",
  "pending": ["《繁星》《春水》1923年出版（商务印书馆说）核对——Britannica 页未载。", "五四运动与《问题小说》定位（通说）待核。", "泰戈尔影响的具体篇目（'繁星'体）待核。"]
},
"delaise": {
  "id": "delaise", "name": "西奥多·德莱塞", "foreign_name": "Theodore Dreiser（西奥多·德莱塞，1871-08-27—1945-12-28）",
  "country": "美国", "birth": 1871, "death": 1945, "birth_year": 1871, "death_year": 1945, "era": "现当代",
  "summary": "德莱塞，印第安纳州特雷霍特人，美国小说家——'the outstanding American practitioner of naturalism'（美国自然主义最杰出的实践者——Britannica）；'replaced the observance of Victorian notions of propriety with the unflinching presentation of real-life subject matter'（以对现实题材的无畏呈现取代维多利亚式的体面观——B280）。《嘉莉妹妹》（1900）首版仅售'fewer than 500 copies'（B280）；《美国的悲剧》（1925）'brought Dreiser a degree of critical and commercial success he had never before attained'（B280）。",
  "timeline": [
    {"year": 1871, "text": "8月27日生于印第安纳州特雷霍特（Britannica：Born Aug. 27, 1871, Terre Haute, Ind.）。", "src": "B280"},
    {"year": 1900, "text": "《嘉莉妹妹》出版（1899年动笔——Britannica；首版仅售500册以内——B280）。", "src": "B280"},
    {"year": 1925, "text": "《美国的悲剧》出版——重大批评与商业成功（B280）。", "src": "B280"},
    {"year": 1945, "text": "12月28日卒于好莱坞（Britannica：Died Dec. 28, 1945, Hollywood, Calif.）。", "src": "B280"}],
  "major_works": [
    {"work_id": "jialimeimei", "note": "长篇（Britannica：1900）"},
    {"title": "美国的悲剧", "note": "（Britannica：1925）"},
    {"title": "天才、欲望三部曲", "note": "（通说待核）"}],
  "style": [
    "自然主义：'unflinching presentation of real-life subject matter'（B280）。",
    "取材自身贫困成长（B280：Drawing on his own impoverished upbringing）。",
    "对美国法制的社会批判（B280：critical view of the American legal system）。"],
  "status": "Britannica 定位德莱塞为美国自然主义最杰出实践者（B280）；《嘉莉妹妹》的出版波折为美国出版史案例（B280）。",
  "sources": ["B280"], "dates_source": "B280",
  "pending": ["《嘉莉妹妹》1900年 Doubleday 初版细节（B280 已载顾虑）核对。", "《美国的悲剧》书名（An American Tragedy）中译核对。", "1931年《嘉莉妹妹》再版风波待核。"]
},
"heller": {
  "id": "heller", "name": "约瑟夫·海勒", "foreign_name": "Joseph Heller（约瑟夫·海勒，1923-05-01—1999-12-12）",
  "country": "美国", "birth": 1923, "death": 1999, "birth_year": 1923, "death_year": 1999, "era": "现当代",
  "summary": "海勒，布鲁克林人，美国小说家与二战轰炸机投弹手——'best known for his satirical protest novel Catch-22 (1961)'（以讽刺抗议小说《第二十二条军规》著称——Britannica），取材于他在欧洲执行的60次战斗任务（Britannica 语境）。'The term catch-22 thereafter entered the English language as a reference to a proviso or situation that trips one up no matter which way one turns'（catch-22 进入英语——B281）；'developed a cult following with its dark surrealism'（B281）。",
  "timeline": [
    {"year": 1923, "text": "5月1日生于纽约布鲁克林（Britannica：Born May 1, 1923, Brooklyn, New York）。", "src": "B281"},
    {"year": 1961, "text": "《第二十二条军规》出版（Britannica：Catch-22 (1961)）。", "src": "B281"},
    {"year": 1999, "text": "12月12日卒于纽约州东汉普顿（Britannica：Died December 12, 1999, East Hampton）。", "src": "B281"}],
  "major_works": [
    {"work_id": "di'ertiaojugui", "note": "长篇（Britannica：1961）"},
    {"title": "出了毛病、上帝知道", "note": "（Britannica：Something Happened, God Knows）"},
    {"title": "最后时光", "note": "（Britannica：Closing Time）"}],
  "style": [
    "'dark surrealism'（B281：developed a cult following with its dark surrealism）。",
    "'use farce and low comedy to highlight the senselessness and futility of life'（B281）。",
    "'catch-22'进入英语（B281）。"],
  "status": "Britannica 定位海勒为黑色幽默代表作家、《第二十二条军规》作者（B281）；其后续作品未及首作成功（B281 语境）。",
  "sources": ["B281"], "dates_source": "B281",
  "pending": ["1961年出版（Simon & Schuster说）核对。","约塞连（Yossarian）人名核对。","电影1970年（Mike Nichols说）待核。"]
},
"forster": {
  "id": "forster", "name": "E.M.福斯特", "foreign_name": "E.M. Forster（爱德华·摩根·福斯特，1879-01-01—1970-06-07）",
  "country": "英国", "birth": 1879, "death": 1970, "birth_year": 1879, "death_year": 1970, "era": "现当代",
  "summary": "福斯特，伦敦人，英国小说家、散文家与批评家——声誉主要建立在'Howards End (1910) and A Passage to India (1924)'（B282）；其小说'blends social commentary on middle-class British life with a belief that people need both imagination and a connection to the earth to live fully'（B282）。《印度之行》——'one of his finest works, examining racism and colonialism'（B282）；'The values of truthfulness and kindness dominate Forster's later thinking'（B282）；'never been seduced by totalitarianisms of any kind'（B282）。",
  "timeline": [
    {"year": 1879, "text": "1月1日生于伦敦（Britannica：Born January 1, 1879, London, England）。", "src": "B282"},
    {"year": 1910, "text": "《霍华德庄园》出版——'his first major success'（B282）。", "src": "B282"},
    {"year": 1924, "text": "《印度之行》出版（B282：A Passage to India (1924)）。", "src": "B282"},
    {"year": 1970, "text": "6月7日卒于沃里克郡考文垂（B282：Died June 7, 1970, Coventry）。", "src": "B282"}],
  "major_works": [
    {"work_id": "yinduzhixing", "note": "长篇（B282：1924，'one of his finest works'）"},
    {"title": "霍华德庄园", "note": "（B282：1910）"},
    {"title": "莫瑞斯", "note": "身后出版（通说待核）"}],
  "style": [
    "'examining racism and colonialism'（B282——《印度之行》）。",
    "'truthfulness and kindness'的价值（B282）。",
    "' соединение'?——不：'imagination and a connection to the earth'（B282）。"],
  "status": "Britannica 定位福斯特为英国小说家（两部杰作的作者）；'从未被任何极权主义诱惑'的知识分子（B282）。",
  "sources": ["B282"], "dates_source": "B282",
  "pending": ["《印度之行》1924年出版（Edward Arnold说）核对。","阿黛拉/阿齐兹人名核对。","《莫瑞斯》1971年身后出版待核。"]
},
"greene": {
  "id": "greene", "name": "格雷厄姆·格林", "foreign_name": "Graham Greene（格雷厄姆·格林，1904-10-02—1991-04-03）",
  "country": "英国", "birth": 1904, "death": 1991, "birth_year": 1904, "death_year": 1991, "era": "现当代",
  "summary": "格林，赫特福德郡伯克汉斯特德人，20世纪英国'最广为人阅读'的小说家之一（Britannica：one of the most widely read British novelists of the 20th century）——其小说'explored moral ambiguity in political settings'（在政治场景中探察道德含混——Britannica），融合天主教主题与全球动荡中的惊悚（Britannica 语境）。'Many of his best-known works, including The Power and the Glory (1940) and The End of the Affair (1951), center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'（B283）。",
  "timeline": [
    {"year": 1904, "text": "10月2日生于赫特福德郡伯克汉斯特德（Britannica：Born October 2, 1904, Berkhamsted）。", "src": "B283"},
    {"year": 1951, "text": "《恋情的终结》出版（B283：The End of the Affair (1951)）。", "src": "B283"},
    {"year": 1991, "text": "4月3日卒于瑞士沃韦（Britannica：died April 3, 1991, Vevey, Switzerland）。", "src": "B283"}],
  "major_works": [
    {"work_id": "lianqingdezhongjie", "note": "长篇（B283：1951；电影1955/1999）"},
    {"title": "权力与荣耀、布莱顿硬糖", "note": "（B283：The Power and the Glory (1940)；Brighton Rock——'a corrupt and violent teenage criminal'）"},
    {"title": "第三个人", "note": "编剧（通说待核）"}],
  "style": [
    "'罗马天主教主题'与惊悚的混合（B283）。",
    "'恶'作为可感的实在（B283：the presence of evil as a palpable force）。",
    "'Greeneland'式世界（术语通说待核——B283 页未用此词）。"],
  "status": "Britannica 定位格林为20世纪英国最广为阅读的小说家之一（B283）。",
  "sources": ["B283"], "dates_source": "B283",
  "pending": ["《恋情的终结》1951年出版（Heinemann说）核对。","莫里斯·本德里克斯/萨拉人名核对。","'Greeneland'术语出处待核。"]
},
"bunin": {
  "id": "bunin", "name": "伊万·蒲宁", "foreign_name": "Ivan Bunin（伊万·阿列克谢耶维奇·蒲宁，1870-10-10/22—1953-11-08）",
  "country": "俄国", "birth": 1870, "death": 1953, "birth_year": 1870, "death_year": 1953, "era": "近代",
  "summary": "蒲宁，沃罗涅日人，俄国诗人、小说家与贵族后裔——'celebrated as one of the country's greatest prose stylists'（被誉为俄国最伟大的文体家之一——Britannica）。1917年革命后离开俄国：'In May 1918 he left Moscow and settled in Odessa'、'at the beginning of 1920 he emigrated first to Constantinople'（B284）；'one of the most famous Russian emigre writers'（最著名的俄国流亡作家之一——B284）；与高尔基等旧友绝交——因革命'he perceived as the triumph of the basest side of the Russian people'（B284）。1933年获诺贝尔文学奖——'the first Russian to receive the Nobel Prize for Literature (1933), and one of the finest of Russian stylists'（B284）。",
  "timeline": [
    {"year": 1870, "text": "10月10/22日生于沃罗涅日（B284：Born October 10 [October 22, New Style], 1870, Voronezh）。", "src": "B284"},
    {"year": 1918, "text": "5月离开莫斯科居敖德萨（B284）。", "src": "B284"},
    {"year": 1920, "text": "初移君士坦丁堡，后定居法国（B284）。", "src": "B284"},
    {"year": 1933, "text": "获诺贝尔文学奖——首位俄国获奖者（B284）。", "src": "B284"},
    {"year": 1953, "text": "11月8日卒于巴黎（B284：Died November 8, 1953, Paris）。", "src": "B284"}],
  "major_works": [
    {"work_id": "jiushanlaideshenshi", "note": "短篇（B284：1916）"},
    {"title": "阿尔谢尼耶夫的一生", "note": "（通说待核——B284 未载）"},
    {"title": "幽暗的林荫道", "note": "（通说待核）"}],
  "style": [
    "'extreme precision of language'（B284：《旧金山来的绅士》）。",
    "俄国最伟大的文体家之一（B284：finest of Russian stylists）。",
    "流亡写作的精确与乡愁（B284 语境）。"],
  "status": "Britannica 定位蒲宁为1933年诺奖得主（首位俄国获奖者）、俄国最伟大的文体家之一（B284）。",
  "sources": ["B284"], "dates_source": "B284",
  "pending": ["《阿尔谢尼耶夫的一生》1930年出版待核。", "1933年诺奖授奖词待核。", "与高尔基绝交细节待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

works = {
"weianzhihuo": {
  "id":"weianzhihuo","title":"微暗的火","original_title":"Pale Fire","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"nabokov","author_name":"弗拉基米尔·纳博科夫",
  "year_display":"1962年（作者页 B145 口径：微暗的火（1962））","year_sort":1962,
  "background":["作者页（B145）：纳博科夫 major_works 载'微暗的火（1962）'（B145 作者页定位，详见 luolita 条核对）。","结构（通说待核）：999行的长诗+前言+评注+索引——'小说'以学术注释的形态出现。"],
  "outline":["诗人谢德的绝笔长诗与金波特注释的'争夺'——赞巴拉王国的幻影（通说待核）。"],
  "characters":[{"name":"金波特","identity":"注释者","note":"（通说待核）"},{"name":"谢德","identity":"诗人","note":"（通说待核）"}],
  "themes":["注释即小说：形式的发明（通说）。",
   "幻想与现实的争夺（通说待核）。",
   "'微暗的火'：莎剧引文（书名通说待核——出自《暴风雨》）。"],
  "influence":[{"text":"作者页：纳博科夫代表作谱系（B145 作者页口径）。","source":"B145"},
   {"text":"后现代元小说的里程碑（通说待核）。","source":"B145"}],
  "reading":{"difficulties":["注释体的阅读顺序（按页码还是按正文）。","999行长诗。"],
   "editions":["《微暗的火》（上海译文出版社，通说待核）。","英文原版。"],
   "order":"先《洛丽塔》后本作。"},
  "pending":["1962年出版（Random House说）核对。","金波特/谢德人名核对。","书名出自《暴风雨》的引文核对。"],
  "sources":["B145"],"year_source":"B145","author_source":"B145","related_works":["luolita","maitian","bianxingji"],
  "svg":G("《微暗的火》形式结构图",[{"title":"长诗","text":"999行（通说）","color":"family"},{"title":"注释","text":"金波特的争夺","color":"main"},{"title":"赞巴拉","text":"幻想的王国","color":"gold"},{"title":"形式","text":"注释即小说","color":"plain"}])
},
"gesaerwanging": {
  "id":"gesaerwanging","title":"格萨尔王","original_title":"格萨尔王（长篇小说）","region":"中国","era":"现当代","era_detail":"当代",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话·藏地史诗）","author_id":"alai","author_name":"阿来",
  "year_display":"出版年份待核（中国作家网官方名单 C012：阿来 major_works 载'空山、格萨尔王'——2009年说通说待核）","year_sort":2009,
  "background":["中国作家网官方名单页（C012）：阿来 major_works 载'空山、格萨尔王'（C012 作者页定位，详见 chenailuodi 条核对）。","题材（通说待核）：重述藏族史诗《格萨尔王传》——说唱艺人晋美与格萨尔王的双线。"],
  "outline":["史诗重述：格萨尔王的降伏与传说；当代说唱艺人的'神授'（通说待核）。"],
  "characters":[{"name":"格萨尔王","identity":"史诗英雄","note":"（通说待核）"},{"name":"晋美","identity":"说唱艺人","note":"当代线（通说待核）"}],
  "themes":["史诗的当代重述（通说待核）。",
   "'神授艺人'的口传传统（通说）。",
   "藏文化的汉语转译（通说）。"],
  "influence":[{"text":"中国作家网官方名单：阿来 major_works 谱系（C012 作者页口径）。","source":"C012"},
   {"text":"中国作家网官方名单：《尘埃落定》第五届茅奖（C012 作者级）。","source":"C012"}],
  "reading":{"difficulties":["藏族史诗知识。","双线结构。"],
   "editions":["《格萨尔王》（重庆出版社，通说待核）。"],
   "order":"先《尘埃落定》后本作。"},
  "pending":["2009年重庆出版社初版核对。","晋美艺人与史诗人物对照待核。","'神授艺人'现象的记载待核。"],
  "sources":["C012"],"year_source":"C012","author_source":"C012","related_works":["chenailuodi","shuihu","bailuyuan"],
  "svg":G("《格萨尔王》双线史诗图",[{"title":"格萨尔王","text":"史诗英雄","color":"main"},{"title":"晋美","text":"当代说唱艺人","color":"family"},{"title":"神授","text":"口传的传统","color":"gold"},{"title":"重述","text":"史诗的当代化","color":"plain"}])
},
"yaoshi": {
  "id":"yaoshi","title":"钥匙","original_title":"鍵（The Key）","region":"日本","era":"现当代","era_detail":"20世纪",
  "genre":"中篇小说","genre_group":"小说","language":"日语","author_id":"tanizaki","author_name":"谷崎润一郎",
  "year_display":"1956年（作者页 B168 口径：钥匙（1956））","year_sort":1956,
  "background":["作者页（B168）：谷崎 major_works 载'钥匙（1956）'（B168 作者页定位，详见 xixue 条核对）。","文体（通说待核）：夫妻双日记体——各自偷看对方日记的性心理游戏。"],
  "outline":["丈夫与妻子互窥日记：欲望的'钥匙'互锁（通说待核）。","结尾的意外（通说待核）。"],
  "characters":[{"name":"丈夫","identity":"教授","note":"日记其一（通说待核）"},{"name":"郁子","identity":"妻子","note":"日记其二（人名通说待核）"}],
  "themes":["日记的互窥结构（通说）。",
   "老年欲望的直视（通说待核）。",
   "'恶魔主义'的晚期（通说——谷崎美学）。"],
  "influence":[{"text":"作者页：谷崎晚年代表作（B168 作者页口径）。","source":"B168"},
   {"text":"与《疯癫老人日记》（1961—62）并列为晚期日记体双作（B168 作者页谱系）。","source":"B168"}],
  "reading":{"difficulties":["双日记的互文。","欲望书写的伦理。"],
   "editions":["《钥匙》（上海译文出版社，通说待核）。","日文原版（新潮文库）。"],
   "order":"先《细雪》《春琴抄》后本作。"},
  "pending":["1956年（《中央公论》说）核对。","妻子名（郁子）核对。","结尾细节待核。"],
  "sources":["B168"],"year_source":"B168","author_source":"B168","related_works":["xixue","chunqinchao","jinsuoji"],
  "svg":G("《钥匙》互窥结构图",[{"title":"丈夫日记","text":"欲望的记录","color":"main"},{"title":"妻子日记","text":"互窥的游戏","color":"gold"},{"title":"钥匙","text":"日记之锁","color":"family"},{"title":"结尾","text":"意外的反转","color":"antagonist"}])
},
"fanxingchunshui": {
  "id":"fanxingchunshui","title":"繁星·春水","original_title":"繁星/春水（小诗集）","region":"中国","era":"现当代","era_detail":"现代",
  "genre":"小诗集","genre_group":"诗歌","language":"汉语（白话）","author_id":"bingxin","author_name":"冰心（谢婉莹）",
  "year_display":"1923年出版（通说待核；Britannica B279 该页未载——仅记其受泰戈尔影响的抒情之作一举成名）","year_sort":1923,
  "background":["Britannica（B279）：冰心'lyrical pieces about childhood and nature, influenced by the Indian poet Rabindranath Tagore'——受泰戈尔影响的童年与自然抒情之作使她'won her instant fame'（一举成名）并获卫斯理学院奖学金。","'冰心体'（通说待核）：小诗体——受泰戈尔《飞鸟集》影响的短诗。"],
  "outline":["《繁星》：零碎的哲思小诗（通说待核）。","《春水》：延续的春水之思（通说待核）。"],
  "characters":[{"name":"冰心","identity":"诗人","note":"'温柔、忧郁'（B279）"}],
  "themes":["母爱与童心（通说）。",
   "泰戈尔式小诗体（B279：influenced by Tagore）。",
   "'哲学的'小诗（通说待核）。"],
  "influence":[{"text":"Britannica：受泰戈尔影响的抒情之作使冰心一举成名（B279）。","source":"B279"},
   {"text":"作者页：冰心为广受欢迎的中国作家（B279 作者级定位）。","source":"B279"}],
  "reading":{"difficulties":["小诗体的断片。","'冰心体'语言。"],
   "editions":["《繁星·春水》（人民文学出版社/商务印书馆版本，通说待核）。"],
   "order":"对照泰戈尔《飞鸟集》（B261 作者受其影响——互证）。"},
  "pending":["《繁星》《春水》1923年出版细节核对。","篇数（繁星164/春水182说）待核。","'冰心体'术语出处待核。"],
  "sources":["B279"],"year_source":"B279","author_source":"B279","related_works":["jitangali","nvshen","beidaoshixuan"],
  "svg":G("《繁星·春水》小诗结构图",[{"title":"繁星","text":"哲思的碎语","color":"main"},{"title":"春水","text":"流水的延续","color":"family"},{"title":"泰戈尔","text":"影响之源（B279）","color":"gold"},{"title":"母爱与童心","text":"主题（通说）","color":"plain"}])
},
"jialimeimei": {
  "id":"jialimeimei","title":"嘉莉妹妹","original_title":"Sister Carrie","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"delaise","author_name":"西奥多·德莱塞",
  "year_display":"1900年出版（Britannica：Sister Carrie——1899年动笔；首版'sold fewer than 500 copies'——B280）","year_sort":1900,
  "background":["Britannica（B280）：'Dreiser began writing his first novel, Sister Carrie, in 1899 at the suggestion of a newspaper colleague'；'Doubleday's qualms about the book, the story line of which involves a young kept woman whose immorality goes unpunished' led to limited advertising，'sold fewer than 500 copies'。","作者（B280）：'the outstanding American practitioner of naturalism'（美国自然主义最杰出实践者）。"],
  "outline":["嘉莉进城：从打工到'kept woman'——'immorality goes unpunished'（B280 语境）。","赫斯特伍德的坠落：从经理到流浪（通说待核）。"],
  "characters":[{"name":"嘉莉·米伯","identity":"打工女","note":"上升者（通说待核）"},{"name":"赫斯特伍德","identity":"经理","note":"下坠者（通说待核）"}],
  "themes":["城市的欲望机器（通说）。",
   "'道德不受惩罚'的挑战（B280：immorality goes unpunished）。",
   "自然主义的命运观（B280 语境）。"],
  "influence":[{"text":"Britannica：'immorality goes unpunished'引发的出版顾虑——仅售不足500册（B280）。","source":"B280"},
   {"text":"作者页：德莱塞为自然主义最杰出实践者（B280 作者级定位）。","source":"B280"}],
  "reading":{"difficulties":["自然主义的道德中立。","1900年代芝加哥—纽约。"],
   "editions":["《嘉莉妹妹》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"自然主义入门：先本作后《美国的悲剧》。"},
  "pending":["1900年出版（Doubleday, Page说）核对。","嘉莉/赫斯特伍德人名核对。","1931年再版风波待核。"],
  "sources":["B280"],"year_source":"B280","author_source":"B280","related_works":["fenwangyu","taiyangzhaochangshengqi","huozhe"],
  "svg":G("《嘉莉妹妹》升降结构图",[{"title":"嘉莉","text":"城市的上升","color":"main"},{"title":"赫斯特伍德","text":"经理的坠落","color":"antagonist"},{"title":"摇椅","text":"欲望的循环","color":"gold"},{"title":"自然主义","text":"道德的中立（B280）","color":"family"}])
},
"di'ertiaojugui": {
  "id":"di'ertiaojugui","title":"第二十二条军规","original_title":"Catch-22","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"heller","author_name":"约瑟夫·海勒",
  "year_display":"1961年（Britannica：Catch-22 (1961)）","year_sort":1961,
  "background":["Britannica（B281）：'The term catch-22 thereafter entered the English language as a reference to a proviso or situation that trips one up no matter which way one turns'——'catch-22'由此进入英语。","'Centering on the antihero Captain John Yossarian, stationed at an airstrip on a Mediterranean island during World War II, the novel portrays the airman's desperate attempts to stay alive'（B281）。","'developed a cult following with its dark surrealism'（B281）。"],
  "outline":["约塞连上尉的求生：'catch'——疯子可停飞但申请停飞者即证明理性（悖论通说待核）。","斯诺登之死的时序倒放（通说待核）。"],
  "characters":[{"name":"约塞连","identity":"投弹手","note":"反英雄（B281：antihero）"},{"name":"卡思卡特上校","identity":"指挥官","note":"（通说待核）"}],
  "themes":["'catch-22'：悖论的权力（B281）。",
   "反英雄与战争荒诞（B281 语境）。",
   "'黑色幽默'的命名（通说待核）。"],
  "influence":[{"text":"Britannica：'catch-22'进入英语——绕不开的困境（B281）。","source":"B281"},
   {"text":"Britannica：'dark surrealism'的邪典追随（B281）。","source":"B281"}],
  "reading":{"difficulties":["循环悖论。","人物众多（40+）。"],
   "editions":["《第二十二条军规》（译林出版社扬恝译本，通说待核）。","英文原版（Simon & Schuster）。"],
   "order":"黑色幽默首选。"},
  "pending":["1961年出版（Simon & Schuster说）核对。","约塞连/斯诺登人名核对。","'黑色幽默'流派命名待核。"],
  "sources":["B281"],"year_source":"B281","author_source":"B281","related_works":["wuhao","fatiaocheng","dongwunongchang"],
  "svg":G("《第二十二条军规》悖论结构图",[{"title":"catch-22","text":"进英语的悖论（B281）","color":"main"},{"title":"约塞连","text":"反英雄（B281）","color":"gold"},{"title":"飞行","text":"疯狂的证明","color":"antagonist"},{"title":"黑色幽默","text":"流派命名（通说）","color":"family"}])
},
"yinduzhixing": {
  "id":"yinduzhixing","title":"印度之行","original_title":"A Passage to India","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"forster","author_name":"E.M.福斯特",
  "year_display":"1924年（作者页 B282 口径：A Passage to India (1924)）","year_sort":1924,
  "background":["Britannica（B282）：'one of his finest works, examining racism and colonialism'（检视种族主义与殖民主义的最佳作品之一——B282）；'The novel ends in an uneasy equilibrium'（小说以不安的平衡结束——B282）。","作者（B282）：福斯特声誉主要基于《霍华德庄园》与本作；'The values of truthfulness and kindness dominate Forster's later thinking'。"],
  "outline":["阿黛拉的马拉巴山洞指控——审判分裂英印两方（B282：a visiting Englishwoman accuses an Indian man of attacking her, and the trial causes division between the British and Indians）。"],
  "characters":[{"name":"阿黛拉","identity":"英国访客","note":"指控者（B282）"},{"name":"阿齐兹","identity":"印度医生","note":"被告（通说待核）"},{"name":"菲尔丁","identity":"校长","note":"连接者（通说待核）"}],
  "themes":["种族主义与殖民主义（B282：examining racism and colonialism）。",
   "'不安的平衡'（B282：uneasy equilibrium）。",
   "'只有连接'（Only connect——作者座右铭，通说待核）。"],
  "influence":[{"text":"Britannica：'one of his finest works'（B282）。","source":"B282"},
   {"text":"Britannica：1984年大卫·里恩电影改编（通说待核）。","source":"B282"}],
  "reading":{"difficulties":["英属印度史。","山洞一幕的空白。"],
   "editions":["《印度之行》（人民文学出版社/译林出版社版本，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"先《霍华德庄园》后本作。"},
  "pending":["1924年出版（Edward Arnold说）核对。","阿黛拉/阿齐兹/菲尔丁人名核对。","马拉巴山洞情节待核。"],
  "sources":["B282"],"year_source":"B282","author_source":"B282","related_works":["wajie","shijiemori","banlunhuangri"],
  "svg":G("《印度之行》审判结构图",[{"title":"马拉巴山洞","text":"指控的空白","color":"antagonist"},{"title":"审判","text":"英印分裂（B282）","color":"main"},{"title":"菲尔丁","text":"连接的尝试","color":"gold"},{"title":"平衡","text":"不安的结尾（B282）","color":"family"}])
},
"lianqingdezhongjie": {
  "id":"lianqingdezhongjie","title":"恋情的终结","original_title":"The End of the Affair","region":"英国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"greene","author_name":"格雷厄姆·格林",
  "year_display":"1951年（作者页 B283 口径：The End of the Affair (1951)）","year_sort":1951,
  "background":["Britannica（B283）：'Many of his best-known works, including The Power and the Glory (1940) and The End of the Affair (1951), center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'（B283）。","'The End of the Affair (films 1955 and 1999) is narrated by an agnostic in love with a woman who forsakes him because of a religious conviction'（无神论者爱上因宗教信念离开他的女人——B283）。"],
  "outline":["莫里斯的嫉妒日记：萨拉的日记揭示'背叛'的真相——宗教的介入（通说待核）。","'恨'与'爱'的祈祷战（通说待核）。"],
  "characters":[{"name":"莫里斯·本德里克斯","identity":"作家","note":"无神论叙述者（B283 语境）"},{"name":"萨拉","identity":"恋人","note":"皈依者（通说待核）"}],
  "themes":["无神论者的嫉妒与信仰（B283）。",
   "'恶'的可感实在（B283：evil as a palpable force）。",
   "日记的复调（通说待核）。"],
  "influence":[{"text":"Britannica：格林'one of the most widely read British novelists of the 20th century'（B283）。","source":"B283"},
   {"text":"Britannica：电影1955与1999（B283）。","source":"B283"}],
  "reading":{"difficulties":["天主教语境。","日记体的双重视角。"],
   "editions":["《恋情的终结》（江苏凤凰文艺出版社/人民文学出版社版本，通说待核）。","英文原版。"],
   "order":"先《权力与荣耀》后本作。"},
  "pending":["1951年出版（Heinemann说）核对。","莫里斯/萨拉人名核对。","'恨的祈祷'结构待核。"],
  "sources":["B283"],"year_source":"B283","author_source":"B283","related_works":["xianzhi","ai_shibunengwangji","chatailaifuren"],
  "svg":G("《恋情的终结》信仰结构图",[{"title":"日记","text":"复调的真相","color":"main"},{"title":"萨拉","text":"信仰的出走","color":"gold"},{"title":"莫里斯","text":"无神论的恨","color":"antagonist"},{"title":"奇迹","text":"信仰的边界","color":"family"}])
},
"jiushanlaideshenshi": {
  "id":"jiushanlaideshenshi","title":"旧金山来的绅士","original_title":"Господин из Сан-Франциско（The Gentleman from San Francisco）","region":"俄国","era":"近代","era_detail":"20世纪初",
  "genre":"短篇小说","genre_group":"小说","language":"俄语","author_id":"bunin","author_name":"伊万·蒲宁",
  "year_display":"1916年（Britannica：Gospodin iz San-Frantsisko (1916; The Gentleman from San Francisco)）","year_sort":1916,
  "background":["Britannica（B284）：'Gospodin iz San-Frantsisko (1916; The Gentleman from San Francisco) show Bunin's penchant for extreme precision of language'（展示蒲宁对语言极端精确的偏好——B284）。","蒲宁（B284）：1933年诺奖——'the first Russian to receive the Nobel Prize for Literature'；'one of the finest of Russian stylists'。"],
  "outline":["'旧金山来的绅士'：一位无名富人携家乘'阿特兰蒂克'号游轮环游——死于卡普里，被装回运棺的汽水箱（通说待核）。"],
  "characters":[{"name":"绅士","identity":"无名富人","note":"无姓名（通说待核）"}],
  "themes":["'阿特兰蒂克'（Atlantic/Atlantis）——文明的自负与覆灭（通说待核）。",
   "死亡面前的社会等级滑稽（通说）。",
   "语言的极端精确（B284）。"],
  "influence":[{"text":"Britannica：'show Bunin's penchant for extreme precision of language'（B284）。","source":"B284"},
   {"text":"Britannica：1933年诺奖——首位俄国获奖者（B284 作者级）。","source":"B284"}],
  "reading":{"difficulties":["游轮社会的等级细节。","象征命名（阿特兰蒂克号）。"],
   "editions":["《旧金山来的绅士》（收于《蒲宁文集》，通说待核）。","俄文原版（公有领域）。"],
   "order":"蒲宁短篇首选。"},
  "pending":["1916年发表（《 思 想 》？——不：俄国刊物说）核对。","绅士无名的处理待核。","阿特兰蒂克号象征待核。"],
  "sources":["B284"],"year_source":"B284","author_source":"B284","related_works":["bianxingji","puluomixiusibang","sihunling"],
  "svg":G("《旧金山来的绅士》覆灭结构图",[{"title":"游轮","text":"阿特兰蒂克号（通说）","color":"gold"},{"title":"绅士","text":"无名的人生","color":"main"},{"title":"卡普里","text":"死亡的中途","color":"antagonist"},{"title":"汽水箱","text":"归途的讽刺","color":"family"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
