# -*- coding: utf-8 -*-
"""v5批1：外国经典大缺口 12 部 + 9 作家页 + 13 来源"""
import json, pathlib

# ---------- sources ----------
new_src = [
{"id":"B220","title":"Herman Melville — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Herman-Melville","type":"百科全书","verified":True,"covers":["melville","baijing"],"note":"2026-11-20 核对：1819-08-01纽约—1891-09-28纽约；'best known for his novels of the sea, including his masterpiece, Moby Dick (1851)'；'eventually considered to be one of the great American writers'（20世纪声誉回升）"},
{"id":"B221","title":"Edgar Allan Poe — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Edgar-Allan-Poe","type":"百科全书","verified":True,"covers":["poe","ailunpoxuan"],"note":"2026-11-20 核对：1809-01-19波士顿—1849-10-07巴尔的摩；'The Murders in the Rue Morgue (1841) initiated the modern detective story'；'the atmosphere in his tales of horror is unrivaled in American fiction'；《乌鸦》1845年1月29日刊于《纽约镜报》"},
{"id":"B222","title":"The Thousand and One Nights — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/The-Thousand-and-One-Nights","type":"百科全书","verified":True,"covers":["yiqianlingyiye"],"note":"2026-11-20 核对：'collection of largely Middle Eastern and Indian stories of uncertain date and authorship'；山鲁佐德每晚讲故事留悬念保命；'the frame story is probably Indian'；最早见于9世纪残篇；阿拉丁/阿里巴巴/辛巴达系18世纪欧洲改编层；迦兰法译本1704—1717"},
{"id":"B223","title":"Antoine de Saint-Exupery — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Antoine-de-Saint-Exupery","type":"百科全书","verified":True,"covers":["saintexupery","xiaowangzi"],"note":"2026-11-20 核对：1900-06-29里昂—1944-07-31（马赛附近侦察飞行失事）；Le Petit Prince (1943) 'a child's fable for adults'；'people can only see rightly with the heart and that what is essential is invisible to the eye'；'has become a modern classic'"},
{"id":"B224","title":"Alexandre Dumas pere — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Alexandre-Dumas-pere","type":"百科全书","verified":True,"covers":["dumaspere","jidushanbojue"],"note":"2026-11-20 核对：1802-07-24—1870-12-05；Le Comte de Monte Cristo (1844–45)；Les Trois Mousquetaires (1844)；'often working with collaborators (especially Auguste Maquet)'"},
{"id":"B225","title":"Mikhail Bulgakov — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Mikhail-Bulgakov","type":"百科全书","verified":True,"covers":["bulgakov","dashiyumageeligeta"],"note":"2026-11-20 核对：1891-05-15基辅—1940-03-10莫斯科；《大师与玛格丽特》写作于1928—1940，'published in the Soviet Union only in 1966–67, and then in an egregiously censored form'；'juxtaposes two planes of action—one set in contemporary Moscow and the other in Pontius Pilate's Judea'；魔鬼化名沃兰德"},
{"id":"B226","title":"The Tale of Genji — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/The-Tale-of-Genji","type":"百科全书","verified":True,"covers":["murasakishikibu","genjiwuyu"],"note":"2026-11-20 核对：'Written at the start of the 11th century, it is generally considered the world's first novel'；'Murasaki Shikibu composed The Tale of Genji while a lady in attendance at the Japanese court, likely completing it about 1010'；54章；'informed by a comprehensive knowledge of Chinese and Japanese poetry'"},
{"id":"B227","title":"Murasaki Shikibu — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Shikibu-Murasaki","type":"百科全书","verified":True,"covers":["murasakishikibu"],"note":"2026-11-20 核对：c. 978 Kyoto—c. 1014 Kyoto；'generally considered the greatest work of Japanese literature and thought to be the world's oldest full novel'；真名不详，'Murasaki'或来自书中女主人公、'Shikibu'来自父亲的式部省官职；《紫式部日记》英译见《Diaries of Court Ladies of Old Japan》(1935)"},
{"id":"B228","title":"Gunter Grass — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Gunter-Grass","type":"百科全书","verified":True,"covers":["grass","tiepigu"],"note":"2026-11-20 核对：1927-10-16但泽—2015-04-13吕贝克；《铁皮鼓》1959年；'This exuberant picaresque novel, written in a variety of styles, imaginatively distorts and exaggerates his personal experiences'；奥斯卡·马策拉特（侏儒，精神病院叙述）；1979年电影获戛纳金棕榈（与《现代启示录》并列）与奥斯卡最佳外语片；1999年诺贝尔奖；但泽三部曲"},
{"id":"B229","title":"Marguerite Duras — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Marguerite-Duras","type":"百科全书","verified":True,"covers":["duras","qingren"],"note":"2026-11-20 核对：1914-04-04越南嘉定—1996-03-03巴黎；'The novel L'Amant (1984; The Lover; film, 1992) won the prestigious Prix Goncourt in 1984'；'semiautobiographical story……about a French teenage girl's love affair with a Chinese man'；《广岛之恋》（1959，雷乃）编剧；《印度之歌》(1975)"},
{"id":"B230","title":"The Idiot (novel by Dostoyevsky) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/The-Idiot-novel-by-Dostoyevsky","type":"百科全书","verified":True,"covers":["baidi","dostoevsky"],"note":"2026-11-20 核对：'published in Russian as Idiot in 1868–69'；梅什金公爵对叶潘钦家的'unsettling effect'；'Myshkin's message of service, compassion, and brotherly love finally fails'"},
{"id":"B231","title":"A Sportsman's Sketches (work by Turgenev) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/A-Sportsmans-Sketches","type":"百科全书","verified":True,"covers":["liurenshengbi","turgenev"],"note":"2026-11-20 核对：'The stories concern life in rural Russia, in particular the relationship between landowners and their serfs'；1852年以 Zapiski okhotnika 首版、1870年代增补；农奴的肖像'always circumscribed by their serfdom'"},
{"id":"B232","title":"Simone de Beauvoir — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Simone-de-Beauvoir","type":"百科全书","verified":True,"covers":["beauvoir","dierxing"],"note":"2026-11-20 核对：1908-01-09巴黎—1986-04-14巴黎；Le Deuxième Sexe (1949; The Second Sex)——'a scholarly and passionate plea for the abolition of what she called the myth of the eternal feminine'；'It became a classic of feminist literature'；1929年与萨特相识并终身相伴"},
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
"melville": {
  "id": "melville", "name": "赫尔曼·梅尔维尔", "foreign_name": "Herman Melville（赫尔曼·梅尔维尔，1819-08-01—1891-09-28）",
  "country": "美国", "birth": 1819, "death": 1891, "birth_year": 1819, "death_year": 1891, "era": "近代",
  "summary": "梅尔维尔，生于纽约，美国小说家、短篇小说家与诗人（Britannica），1840年代的航海经历催生其冒险小说——'best known for his novels of the sea, including his masterpiece, Moby Dick (1851)'（以海洋小说著称，代表作《白鲸》——Britannica）。生前默默无闻，晚年以海关检查员谋生（Britannica 语境），20世纪声誉飙升：'eventually considered to be one of the great American writers'（终被列入美国最伟大作家之列——Britannica）。",
  "timeline": [
    {"year": 1819, "text": "生于纽约市（Britannica：Born August 1, 1819, New York City）。", "src": "B220"},
    {"year": 1841, "text": "1月乘捕鲸船阿库什奈号出海（Britannica：Acushnet sailing January 1841）。", "src": "B220"},
    {"year": 1846, "text": "《泰皮》出版带来短暂声名（Britannica：Typee (1846)）。", "src": "B220"},
    {"year": 1851, "text": "《白鲸》出版（Britannica：Moby Dick (1851)）。", "src": "B220"},
    {"year": 1891, "text": "9月28日卒于纽约（Britannica：Died September 28, 1891）。", "src": "B220"}
  ],
  "major_works": [
    {"work_id": "baijing", "note": "长篇（Britannica：masterpiece）"},
    {"title": "泰皮、奥穆", "note": "南洋冒险（Britannica：Typee (1846), Omoo (1847)）"},
    {"title": "抄写员巴特比", "note": "短篇（通说待核）"}
  ],
  "style": [
    "海洋百科叙事：捕鲸业知识+圣经式的象征体系（通说）。",
    "莎士比亚式独白与独白剧（通说待核）。",
    "'卓越美国作家'的世纪性重估（Britannica：rose in critical esteem）。"
  ],
  "status": "Britannica 定位梅尔维尔为美国小说家、短篇家与诗人，《白鲸》为其杰作；生前籍籍无名、20世纪被重估为美国最伟大作家之一（Britannica）。",
  "sources": ["B220"], "dates_source": "B220",
  "pending": ["《白鲸》英国版 The Whale 与美国版标题差异（1851）待核。", "与霍桑的交往及《白鲸》题献待核。", "《水手比利·巴德》遗稿1924年出版待核。"]
},
"poe": {
  "id": "poe", "name": "埃德加·爱伦·坡", "foreign_name": "Edgar Allan Poe（埃德加·爱伦·坡，1809-01-19—1849-10-07）",
  "country": "美国", "birth": 1809, "death": 1849, "birth_year": 1809, "death_year": 1849, "era": "近代",
  "summary": "爱伦·坡，波士顿人，美国短篇小说家、诗人、批评家与编辑，以神秘、恐怖与死亡题材著称，被视为现代侦探小说的开创者（Britannica：renowned for tales of mystery, horror, and the macabre, and for pioneering the modern detective story）。'其恐怖小说的氛围在美国小说中无可匹敌'（Britannica：the atmosphere in his tales of horror is unrivaled in American fiction）。1845年《乌鸦》一夜成名（Britannica：brought him national fame at once）。",
  "timeline": [
    {"year": 1809, "text": "生于波士顿（Britannica：Born January 19, 1809, Boston）。", "src": "B221"},
    {"year": 1841, "text": "《默格街血案》发表——现代侦探小说的开端（Britannica：initiated the modern detective story）。", "src": "B221"},
    {"year": 1845, "text": "1月29日《乌鸦》刊于《纽约镜报》全国成名（Britannica）。", "src": "B221"},
    {"year": 1847, "text": "妻子弗吉尼亚死于肺结核（Britannica：Virginia died January 1847）。", "src": "B221"},
    {"year": 1849, "text": "10月7日卒于巴尔的摩（Britannica：Died October 7, 1849）。", "src": "B221"}
  ],
  "major_works": [
    {"work_id": "ailunpoxuan", "note": "短篇选（本库立目）"},
    {"title": "乌鸦及其他诗", "note": "（Britannica：The Raven, 1845）"},
    {"title": "莫雷拉、莉姬", "note": "哥特短篇（通说待核）"}
  ],
  "style": [
    "'效果论'：短篇写作以单一效果为纲（通说待核——'unity of effect'出自其《创作哲学》）。",
    "哥特恐怖与现代侦探的双开山（Britannica：developing the Gothic horror story；pioneering the modern detective story）。",
    "对欧洲浪漫主义的美国化改造（Britannica：transform European Romantic literary traditions into a distinctly American form）。"
  ],
  "status": "Britannica 定位爱伦·坡为现代侦探小说开创者、哥特恐怖大师、科幻早期重要贡献者；其对波德莱尔以降法国象征主义的深远影响为通说（待核）。",
  "sources": ["B221"], "dates_source": "B221",
  "pending": ["《创作哲学》与《诗歌原理》原文核对。", "波德莱尔1856年法译《奇异故事集》细节待核。", "死因（'cooping'选举斗殴说）待核。"]
},
"saintexupery": {
  "id": "saintexupery", "name": "安托万·德·圣埃克苏佩里", "foreign_name": "Antoine de Saint-Exupéry（安托万·德·圣埃克苏佩里，1900-06-29—1944-07-31）",
  "country": "法国", "birth": 1900, "death": 1944, "birth_year": 1900, "death_year": 1944, "era": "现当代",
  "summary": "圣埃克苏佩里，里昂人，法国飞行员与作家（Britannica），飞行生涯为其小说供给素材与主题。'best remembered for the 1943 fable The Little Prince'（以1943年寓言《小王子》传世——Britannica）。1944年7月31日在科西嘉起飞的侦察飞行中失踪（Britannica：died on a 1944 reconnaissance flight from Corsica）。另著《夜航》《风沙星辰》等（Britannica 语境）。",
  "timeline": [
    {"year": 1900, "text": "生于里昂（Britannica：Born June 29, 1900, Lyon）。", "src": "B223"},
    {"year": 1926, "text": "加入拉泰科埃尔航空公司（Britannica：joined Compagnie Latécoère 1926）。", "src": "B223"},
    {"year": 1939, "text": "《风沙星辰》出版（通说待核）。", "src": "B223"},
    {"year": 1943, "text": "《小王子》在美国出版（Britannica：Le Petit Prince (1943)）。", "src": "B223"},
    {"year": 1944, "text": "7月31日侦察飞行中失事（Britannica：died……near Marseille）。", "src": "B223"}
  ],
  "major_works": [
    {"work_id": "xiaowangzi", "note": "寓言（Britannica：1943）"},
    {"title": "夜航、风沙星辰", "note": "（Britannica 语境）"},
    {"title": "空军飞行员", "note": "（通说待核）"}
  ],
  "style": [
    "飞行员文学：以高空俯瞰的视角写人与大地（通说）。",
    "'写给大人的童话'：Britannica——a child's fable for adults。",
    "简洁诗性的箴言体：'人只有用心才能看得正确，本质的东西肉眼是看不见的'（Britannica 转述：people can only see rightly with the heart……）。"
  ],
  "status": "Britannica 定位圣埃克苏佩里为飞行员作家，《小王子》'has become a modern classic'（已成现代经典）；其为数不多死于二战飞行中的作家之一（Britannica 语境）。",
  "sources": ["B223"], "dates_source": "B223",
  "pending": ["《小王子》法语初版细节（1943年纽约 Reynal & Hitchcock 说）待核。", "里昂机场更名事件（通说）待核。", "插图是否作者自绘（通说）待核。"]
},
"dumaspere": {
  "id": "dumaspere", "name": "大仲马", "foreign_name": "Alexandre Dumas père（亚历山大·仲马，'大仲马'，1802-07-24—1870-12-05）",
  "country": "法国", "birth": 1802, "death": 1870, "birth_year": 1802, "death_year": 1870, "era": "近代",
  "summary": "大仲马，维莱科特雷人，19世纪法国'多产而受欢迎'的小说家——先以剧作家成名、后以历史小说家传世（Britannica：a highly prolific and popular 19th-century French writer……first as a dramatist and then as a historical novelist）。代表作《基督山伯爵》（1844—45）与《三个火枪手》（1844）（Britannica）；常与八月·马凯等合作者共同写作（Britannica：often working with collaborators (especially Auguste Maquet)）。其子小仲马亦为作家（Britannica：father of the writer Alexandre Dumas, fils）。",
  "timeline": [
    {"year": 1802, "text": "生于维莱科特雷（Britannica：Born July 24, 1802）。", "src": "B224"},
    {"year": 1844, "text": "《三个火枪手》出版（Britannica：Les Trois Mousquetaires (published 1844)）。", "src": "B224"},
    {"year": 1844, "text": "《基督山伯爵》连载（1844—45）（Britannica：Le Comte de Monte Cristo (1844–45)）。", "src": "B224"},
    {"year": 1850, "text": "《黑郁金香》出版（Britannica：La Tulipe noire (1850)）。", "src": "B224"},
    {"year": 1870, "text": "12月5日卒于迪耶普附近的皮伊（Britannica：Died December 5, 1870, Puys）。", "src": "B224"}
  ],
  "major_works": [
    {"work_id": "jidushanbojue", "note": "长篇（Britannica：1844–45）"},
    {"title": "三个火枪手及其续篇", "note": "（Britannica：Vingt ans après (1845)；Bragelonne (1848–50)）"},
    {"title": "亨利三世宫廷戏剧", "note": "（通说待核）"}
  ],
  "style": [
    "历史小说的通俗化：真实历史+虚构人物的报章连载体（通说）。",
    "情节机器：复仇与冒险的高效驱动（通说）。",
    "合作工厂式写作：马凯提供史料骨架（Britannica：especially Auguste Maquet）。"
  ],
  "status": "Britannica 定位大仲马为19世纪最流行、最多产的法国作家之一；《基督山伯爵》与《三个火枪手》为其传世双璧；2002年其遗骸迁入先贤祠（通说待核）。",
  "sources": ["B224"], "dates_source": "B224",
  "pending": ["《基督山伯爵》连载日期（1844—46《辩论报》说）核对。", "马凯的分工争议（署名权）待核。", "混血出身与《我的黑仆回忆录》争议待核。"]
},
"murasakishikibu": {
  "id": "murasakishikibu", "name": "紫式部", "foreign_name": "Murasaki Shikibu（紫式部，约978—约1014）",
  "country": "日本", "birth": 978, "death": 1014, "birth_year": 978, "death_year": 1014, "era": "古代",
  "summary": "紫式部，京都人，平安时代宫廷女官——'Murasaki Shikibu composed The Tale of Genji while a lady in attendance at the Japanese court, likely completing it about 1010'（约1010年完成《源氏物语》——Britannica）。真名不详：'Murasaki'或来自其书中女主人公、'Shikibu'来自父亲在式部省的官职（Britannica）。其作被普遍视为'generally considered the greatest work of Japanese literature and thought to be the world's oldest full novel'（日本文学最高杰作、世界最早完整长篇小说——Britannica）。另著《紫式部日记》（Britannica：英译见 1935 年《Diaries of Court Ladies of Old Japan》）。",
  "timeline": [
    {"year": 978, "text": "约生于京都（Britannica：Born c. 978, Kyōto）。", "src": "B227"},
    {"year": 1005, "text": "入宫侍奉皇后（彰子/一条院皇后说——通说待核；Britannica：served 女院）。", "src": "B227"},
    {"year": 1010, "text": "《源氏物语》约于此年完成（Britannica：likely completing it about 1010）。", "src": "B226"},
    {"year": 1014, "text": "约卒于京都（Britannica：died c. 1014）。", "src": "B227"}
  ],
  "major_works": [
    {"work_id": "genjiwuyu", "note": "物语（Britannica：c. 1010）"},
    {"title": "紫式部日记", "note": "（Britannica：Diaries of Court Ladies of Old Japan 1935 英译）"},
    {"title": "紫式部集", "note": "和歌集（通说待核）"}
  ],
  "style": [
    "'物哀'美学的源头：王朝女性的敏感与哀感（通说待核——'物哀'概念出自本居宣长）。",
    "宫廷心理写实：以细腻笔触写恋爱与权力（Britannica 语境：each of the women in his life is vividly delineated）。",
    "中日文学的融汇：'informed by a comprehensive knowledge of Chinese and Japanese poetry'（Britannica）。"
  ],
  "status": "Britannica 定位紫式部为《源氏物语》作者——该书'generally considered the greatest work of Japanese literature and thought to be the world's oldest full novel'；她亦是平安时代宫廷日记与和歌的重要作者。",
  "sources": ["B226", "B227"], "dates_source": "B227",
  "pending": ["生卒约年（978/1014）与父亲藤原为时的官职细节核对。", "侍奉中宫彰子（一条天皇中宫）与 Britannica'女院'表述的对应核对。", "'物哀'概念出处（本居宣长《源氏物语玉的小栉》）待核。"]
},
"bulgakov": {
  "id": "bulgakov", "name": "米哈伊尔·布尔加科夫", "foreign_name": "Mikhail Bulgakov（米哈伊尔·布尔加科夫，1891-05-15—1940-03-10）",
  "country": "俄国", "birth": 1891, "death": 1940, "birth_year": 1891, "death_year": 1940, "era": "现当代",
  "summary": "布尔加科夫，基辅人，苏联剧作家、小说家与短篇小说家，以幽默与犀利讽刺著称（Britannica：known for humor and penetrating satire）。1930年起被禁止出版（Britannica：Censorship blocked him from publishing by 1930）；其杰作《大师与玛格丽特》写作于1928—1940年，死后才以删节版问世（Britannica：published in the Soviet Union only in 1966–67, and then in an egregiously censored form）。另著《白卫军》《狗心》（Britannica：Heart of a Dog——'a scathing comic satire on pseudoscience'）。",
  "timeline": [
    {"year": 1891, "text": "5月15日生于基辅（Britannica：Born May 15……1891, Kiev）。", "src": "B225"},
    {"year": 1925, "text": "《白卫军》连载、《狗心》写成（Britannica：The White Guard serialized 1925；Heart of a Dog written 1925）。", "src": "B225"},
    {"year": 1926, "text": "《图尔宾一家的日子》搬上舞台（Britannica：Days of the Turbins staged 1926）。", "src": "B225"},
    {"year": 1930, "text": "作品遭全面禁发（Britannica：Censorship blocked him from publishing by 1930）。", "src": "B225"},
    {"year": 1966, "text": "身后：《大师与玛格丽特》1966—67年在苏联删节出版（Britannica）。", "src": "B225"}
  ],
  "major_works": [
    {"work_id": "dashiyumageeligeta", "note": "长篇（Britannica：1928–40写作，1966–67出版）"},
    {"title": "白卫军、图尔宾一家的日子", "note": "（Britannica）"},
    {"title": "狗心", "note": "（Britannica：1925）"}
  ],
  "style": [
    "讽刺的精密工艺：'humor and penetrating satire'（Britannica）。",
    "魔幻与现实的并置：'juxtaposes two planes of action——contemporary Moscow and Pontius Pilate's Judea'（Britannica）。",
    "对伪科学的漫画式打击（Britannica：scathing comic satire on pseudoscience——《狗心》）。"
  ],
  "status": "Britannica 定位布尔加科夫为苏联讽刺大师；《大师与玛格丽特》被其称为'witty and ribald, and at the same time a penetrating philosophical novel wrestling with profound and eternal problems'（俏皮而放达、又是与永恒难题缠斗的深邃哲思小说——Britannica），死后出版即成世界经典（通说）。",
  "sources": ["B225"], "dates_source": "B225",
  "pending": ["沃兰德与随从（卡罗维耶夫/河马猫）人物名核对。", "'手稿不会烧毁'名句核对。", "《大师与玛格丽特》全本1969年法兰克福版细节待核。"]
},
"grass": {
  "id": "grass", "name": "君特·格拉斯", "foreign_name": "Günter Grass（君特·格拉斯，1927-10-16—2015-04-13）",
  "country": "德国", "birth": 1927, "death": 2015, "birth_year": 1927, "death_year": 2015, "era": "现当代",
  "summary": "格拉斯，但泽（今波兰格但斯克）人，德国诗人、小说家、剧作家、雕塑家与版画家（Britannica），其处女作使他成为'在纳粹之下成年、经历二战的那一代德国人的文学声音'（Britannica 语境：the literary voice of the German generation that came of age under Nazism and lived through World War II）。1999年获诺贝尔文学奖（Britannica）。《铁皮鼓》（1959）为'但泽三部曲'之首（Britannica：followed by Cat and Mouse (1961) and Dog Years (1963)）。",
  "timeline": [
    {"year": 1927, "text": "10月16日生于但泽（Britannica：Born October 16, 1927, Danzig）。", "src": "B228"},
    {"year": 1959, "text": "《铁皮鼓》出版（Britannica：1959）。", "src": "B228"},
    {"year": 1961, "text": "《猫与鼠》出版，与《狗年月》（1963）合称但泽三部曲（Britannica）。", "src": "B228"},
    {"year": 1999, "text": "获诺贝尔文学奖（Britannica：won the Nobel Prize for Literature in 1999）。", "src": "B228"},
    {"year": 2006, "text": "自传《剥洋葱》披露党卫军经历引发争议（通说待核）。", "src": "B228"}
  ],
  "major_works": [
    {"work_id": "tiepigu", "note": "长篇（Britannica：1959）"},
    {"title": "猫与鼠、狗年月", "note": "但泽三部曲（Britannica）"},
    {"title": "比目鱼、母鼠", "note": "（通说待核）"}
  ],
  "style": [
    "多风格拼贴：'written in a variety of styles, imaginatively distorts and exaggerates his personal experiences'（Britannica）。",
    "怪诞寓言：奥斯卡的鼓与尖叫（Britannica 语境：Oskar Matzerath, a dwarf who narrates from an asylum）。",
    "历史的道德清算：纳粹化的日常家庭（Britannica：the creeping Nazification of average families）。"
  ],
  "status": "Britannica 定位格拉斯为战后德国文学的核心声音、1999年诺奖得主；'his strong, and sometimes unpopular, political beliefs had prevented him from receiving the prize far earlier'（其强硬而有时不受欢迎的政治立场让他迟迟未获诺奖——Britannica）。",
  "sources": ["B228"], "dates_source": "B228",
  "pending": ["奥斯卡'三岁停止生长'的设定细节核对。", "《剥洋葱》2006年争议（党卫军装甲师经历）待核。", "但泽三部曲名称出处（英美评论界说）待核。"]
},
"duras": {
  "id": "duras", "name": "玛格丽特·杜拉斯", "foreign_name": "Marguerite Duras（玛格丽特·杜拉斯，本名玛格丽特·多纳迪厄，1914-04-04—1996-03-03）",
  "country": "法国", "birth": 1914, "death": 1996, "birth_year": 1914, "death_year": 1996, "era": "现当代",
  "summary": "杜拉斯，生于印度支那嘉定（今越南），本名玛格丽特·多纳迪厄（Britannica：pseudonym of Marguerite Donnadieu），法国小说家、剧作家、编剧与导演——以《广岛之恋》（1959）与《印度之歌》（1975）的剧本及'获1984年龚古尔奖的小说《情人》'著称（Britannica）。童年在中南半岛度过（Britannica：spent her childhood in Indochina）。",
  "timeline": [
    {"year": 1914, "text": "4月4日生于印度支那嘉定（Britannica：Born April 4, 1914, Gia Dinh, Cochinchina [Vietnam]）。", "src": "B229"},
    {"year": 1959, "text": "《广岛之恋》剧本（雷乃导演）（Britannica：Hiroshima mon amour (1959)）。", "src": "B229"},
    {"year": 1984, "text": "《情人》获龚古尔奖（Britannica：won the prestigious Prix Goncourt in 1984）。", "src": "B229"},
    {"year": 1991, "text": "改写为《来自中国北方的情人》（Britannica：L'Amant de la Chine du Nord (1991)）。", "src": "B229"},
    {"year": 1996, "text": "3月3日卒于巴黎（Britannica：Died March 3, 1996, Paris）。", "src": "B229"}
  ],
  "major_works": [
    {"work_id": "qingren", "note": "中长篇（Britannica：1984 龚古尔奖）"},
    {"title": "广岛之恋、印度之歌", "note": "剧本（Britannica）"},
    {"title": "琴声如诉", "note": "（通说待核）"}
  ],
  "style": [
    "极简与抽象：晚期转向'a more abstract and synthetic mode, with fewer characters, less plot and narrative'（Britannica）。",
    "对白的敏锐：'This splendid instinct for dialogue'（Britannica）。",
    "自传素材的反复改写：《情人》与《来自中国北方的情人》（Britannica）。"
  ],
  "status": "Britannica 定位杜拉斯为多面手（小说/戏剧/编剧/导演），《情人》为其国际声誉的顶点；其与'新小说'派的关系：她本人否认归入 nouveau roman（Britannica：though she denied any link to the nouveau roman movement）。",
  "sources": ["B229"], "dates_source": "B229",
  "pending": ["《情人》1992年电影（让-雅克·阿诺导演）细节待核。", "《抵挡太平洋的堤坝》1950年待核。", "湄公河渡船场景的自传对应（《来自中国北方的情人》改写差异）待核。"]
},
"beauvoir": {
  "id": "beauvoir", "name": "西蒙娜·德·波伏瓦", "foreign_name": "Simone de Beauvoir（西蒙娜·德·波伏瓦，1908-01-09—1986-04-14）",
  "country": "法国", "birth": 1908, "death": 1986, "birth_year": 1908, "death_year": 1986, "era": "现当代",
  "summary": "波伏瓦，巴黎人，法国作家、存在主义哲学家与女性主义者——'known primarily for her treatise Le Deuxième Sexe, 2 vol. (1949; The Second Sex)'（以两卷本《第二性》最为著称——Britannica），该书是'为废除她所称的永恒女性神话而作的学术而热情的呼吁'（Britannica：a scholarly and passionate plea for the abolition of what she called the myth of the eternal feminine），'已成为女性主义文学的经典'（Britannica：It became a classic of feminist literature）。1929年通过哲学教师资格并结识萨特，开始终身相伴（Britannica）。",
  "timeline": [
    {"year": 1908, "text": "1月9日生于巴黎（Britannica：Born January 9, 1908, Paris）。", "src": "B232"},
    {"year": 1929, "text": "通过哲学agrégation考试，结识萨特（Britannica：passed her agrégation in philosophy and met Jean-Paul Sartre）。", "src": "B232"},
    {"year": 1945, "text": "与萨特等创办《现代》杂志（Britannica：co-founded the journal Les Temps Modernes；年份通说待核）。", "src": "B232"},
    {"year": 1949, "text": "《第二性》两卷出版（Britannica：1949）。", "src": "B232"},
    {"year": 1986, "text": "4月14日卒于巴黎（Britannica：died April 14, 1986, Paris）。", "src": "B232"}
  ],
  "major_works": [
    {"work_id": "dierxing", "note": "论著（Britannica：1949）"},
    {"title": "名士风流、人都是要死的", "note": "小说（通说待核）"},
    {"title": "一个规矩女人的回忆录", "note": "自传（通说待核）"}
  ],
  "style": [
    "存在主义女性主义：'女人不是天生的，而是后天形成的'（名句通说待核——One is not born, but rather becomes, a woman）。",
    "哲学论辩与个案叙事的结合（Britannica 语境：scholarly and passionate）。",
    "自传四部曲与小说并行（通说待核）。"
  ],
  "status": "Britannica 定位波伏瓦为《第二性》作者——女性主义文学经典（classic of feminist literature——Britannica）；1953年英译遭严重删节、2009年新译方补全原文（Britannica），这一版本史是理解该书的重要背景。",
  "sources": ["B232"], "dates_source": "B232",
  "pending": ["'One is not born, but rather becomes, a woman'原文（第二性第二卷开篇）核对。", "《现代》杂志创刊1945年核对。", "《模糊性的道德》1947年待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

# ---------- works ----------
works = {
"baijing": {
  "id":"baijing","title":"白鲸","original_title":"Moby-Dick; or, The Whale","region":"美国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"melville","author_name":"赫尔曼·梅尔维尔",
  "year_display":"1851年出版（Britannica：Moby Dick (1851)）","year_sort":1851,
  "background":["Britannica：'best known for his novels of the sea, including his masterpiece, Moby Dick (1851)'——海洋小说的杰作。","素材来源：作者1841年乘捕鲸船阿库什奈号的南太平洋航行（Britannica：Acushnet sailing January 1841）。"],
  "outline":["以实玛利随裴廓德号出航——亚哈船长追猎咬断他一条腿的白鲸莫比·迪克（通说）。","全书编织捕鲸业百科（鲸类学章）与三大预言者、圣火夜、最后三日的追猎（通说）。","结局：白鲸撞沉裴廓德号，亚哈被鱼线缠住拖入海中；以实玛利靠棺材浮桶生还（通说待核）。"],
  "characters":[{"name":"亚哈船长","identity":"捕鲸船长","note":"复仇的偏执狂（通说）"},{"name":"以实玛利","identity":"水手·叙述者","note":"唯一生还者"},{"name":"莫比·迪克","identity":"白鲸","note":"自然的谜题（通说）"},{"name":"魁魁格","identity":"标枪手","note":"食人岛王子（通说）"}],
  "themes":["复仇与执念的毁灭性（通说）。","自然的不可知：白鲸的白色之谜（通说）。","民主的船：多元族裔水手的浮世（通说待核）。"],
  "influence":[{"text":"Britannica：20世纪初其作品声誉飙升，'eventually considered to be one of the great American writers'。","source":"B220"},
    {"text":"Britannica：《白鲸》为其杰作（masterpiece）。","source":"B220"}],
  "reading":{"difficulties":["鲸类学百科章——可跳读再回补。","圣经/莎士比亚典故密度。"],
    "editions":["曹庸译本（长江文艺出版社，通说待核）。","成时译本（人民文学出版社，通说待核）。","英文原版（公有领域）。"],
    "order":"先读第1、36、42章（戏白鲸出现）与最后三章 → 补百科章。"},
  "pending":["英国版1851年10月《The Whale》与美国版11月《Moby-Dick》差异待核。","题献霍桑细节待核。","《水手比利·巴德》遗稿待核。"],
  "sources":["B220"],"year_source":"B220","author_source":"B220","related_works":["hakebei","hongzi","fenwangyu"],
  "svg":{"type":"graph","width":680,"height":440,"caption":"《白鲸》追猎结构图",
    "nodes":[{"id":"ahab","label":"亚哈船长","x":340,"y":115,"color":"antagonist","sub":"复仇者"},
      {"id":"ishmael","label":"以实玛利","x":140,"y":115,"color":"main","sub":"叙述者"},
      {"id":"moby","label":"白鲸","x":540,"y":115,"color":"family","sub":"猎物·谜"},
      {"id":"pequod","label":"裴廓德号","x":230,"y":330,"color":"plain","sub":"捕鲸船"},
      {"id":"ahab2","label":"最后三日追猎","x":460,"y":330,"color":"gold","sub":"同归于尽"}],
    "edges":[{"a":"ahab","b":"moby","label":"宿仇"},{"a":"ishmael","b":"pequod","label":"上船"},{"a":"ahab","b":"pequod","label":"统率"},{"a":"moby","b":"ahab2","label":"决战"}]}
},
"ailunpoxuan": {
  "id":"ailunpoxuan","title":"爱伦·坡短篇小说选","original_title":"爱伦·坡短篇小说选（通行选集）","region":"美国","era":"近代","era_detail":"19世纪",
  "genre":"短篇小说选集","genre_group":"小说","language":"英语","author_id":"poe","author_name":"埃德加·爱伦·坡",
  "year_display":"篇作于1833—1849年间；《默格街血案》1841年（Britannica：initiated the modern detective story）","year_sort":1841,
  "background":["Britannica：坡为现代侦探小说开创者——'The Murders in the Rue Morgue (1841) initiated the modern detective story'；'the atmosphere in his tales of horror is unrivaled in American fiction'。","诗《乌鸦》1845年1月29日刊于《纽约镜报》、一夜成名（Britannica：brought him national fame at once）。"],
  "outline":["侦探系：《默格街血案》《失窃的信》（杜宾——通说）。","恐怖系：《厄舍府的倒塌》《黑猫》《泄密的心》《红死病的假面舞会》（Britannica：stories of supernatural horror——通说篇目）。","诗《乌鸦》：18节六行诗、abcbbb韵式'enhances the gloom of the lyric'（Britannica）。"],
  "characters":[{"name":"杜宾","identity":"业余侦探","note":"福尔摩斯的原型（通说）"},{"name":"厄舍府主人","identity":"没落贵族","note":"《厄舍府的倒塌》（通说）"}],
  "themes":["单一效果的短篇美学（通说待核——unity of effect）。","死亡与活埋、疯狂的心理恐怖（通说）。","侦探方法的理性之光（通说）。"],
  "influence":[{"text":"Britannica：开创现代侦探小说（pioneering the modern detective story）。","source":"B221"},
    {"text":"Britannica：对科幻文类的早期重要贡献（a significant early contributor to the science fiction genre）。","source":"B221"}],
  "reading":{"difficulties":["第一人称不可靠叙述。","坡的哥特修辞密度。"],
    "editions":["《爱伦·坡短篇小说集》（上海译文出版社，通说待核）。","英文原版（公有领域）。"],
    "order":"先《默格街血案》→《厄舍府的倒塌》→《黑猫》《泄密的心》→《乌鸦》。"},
  "pending":["各篇首刊年份逐篇核对。","《创作哲学》'unity of effect'原文核对。","波德莱尔法译本1856年待核。"],
  "sources":["B221"],"year_source":"B221","author_source":"B221","related_works":["huxiaoshanzhuang","daotadengqu","bianxingji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"爱伦·坡短篇双系结构图",
    "cards":[{"title":"杜宾探案","text":"默格街·失窃的信","color":"main"},{"title":"厄舍府","text":"哥特恐怖（Britannica）","color":"antagonist"},{"title":"黑猫·泄密的心","text":"疯狂自白","color":"gold"},{"title":"乌鸦","text":"1845年一夜成名","color":"family"}]}
},
"yiqianlingyiye": {
  "id":"yiqianlingyiye","title":"一千零一夜","original_title":"ألف ليلة وليلة（Alf laylah wa-laylah / The Thousand and One Nights，又称《天方夜谭》）","region":"阿拉伯","era":"近代","era_detail":"成书于9—16世纪（多源层累）；1704—1717年经迦兰法译本风行欧洲","genre":"故事集","genre_group":"故事集","language":"阿拉伯语（多源）","author_id":None,"author_name":"阿拉伯及更早的民间与文人故事层累总集（作者不可考）",
  "year_display":"最早见于9世纪残篇（Britannica）；迦兰法译本1704—1717年使其风行欧洲（Britannica）","year_sort":1704,
  "background":["Britannica：'collection of largely Middle Eastern and Indian stories of uncertain date and authorship'——源流多层的东方故事总集。","框架（Britannica）：国王山鲁亚尔因妻不忠而每日娶杀一女；宰相之女山鲁佐德（Scheherazade）'devised a scheme to save herself and others'——每晚讲故事留悬念，'he puts off her execution from day to day and finally abandons his cruel plan'。"],
  "outline":["框架故事：讲故事=活命——叙事的自我指涉（Britannica）。","故事层：'the frame story is probably Indian'，故事来自 India, Iran, Iraq, Egypt, Turkey, and possibly Greece（Britannica）。","著名篇目：阿拉丁、阿里巴巴、辛巴达——'added to the collection only in the 18th century in European adaptations'（Britannica）。","迦兰首译：Les Mille et Une Nuits，12卷（1704—17），'remained standard until the mid-19th century'（Britannica）。"],
  "characters":[{"name":"山鲁佐德","identity":"宰相之女","note":"以故事续命（Britannica）"},{"name":"山鲁亚尔","identity":"国王","note":"杀妻的暴君（Britannica）"},{"name":"辛巴达","identity":"航海家","note":"七次航行（通说）"}],
  "themes":["讲故事与生存：悬念即生命（Britannica 语境）。","多层文明的互嵌：印度框架+波斯/阿拉伯故事核（Britannica）。","'一千'只是虚指：'expressions……were intended merely to indicate a large number'（Britannica）。"],
  "influence":[{"text":"Britannica：阿拉丁、阿里巴巴、辛巴达的故事'have almost become part of Western folklore'（几乎成为西方民俗的一部分）。","source":"B222"},
    {"text":"Britannica：迦兰1704—1717年首译为欧洲标准译本直至19世纪中叶——欧洲浪漫主义的东方想象之源（通说待核）。","source":"B222"}],
  "reading":{"difficulties":["版本谱系：勿把18世纪欧洲添加层当作'原典'。","框架与嵌套的层级。"],
    "editions":["纳训译本（人民文学出版社，通说待核）。","李唯中译本（花城出版社，通说待核）。"],
    "order":"先读框架故事+辛巴达 → 阿里巴巴/阿拉丁（注意18世纪层）→ 自选故事。"},
  "pending":["六种连续形态（8—16世纪，Baghdad/Egypt 层）细节核对。","纳训/李唯中译本信息核对。","《阿拉丁》故事原无阿拉伯手稿本的确认（Britannica 已载）展开核对。"],
  "sources":["B222"],"year_source":"B222","author_source":"B222","related_works":["shiritan","kantebolei","yisuo"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《一千零一夜》框架嵌套图",
    "cards":[{"title":"框架","text":"山鲁佐德讲故事的夜晚","color":"main"},{"title":"印度—波斯—阿拉伯","text":"多层故事核（Britannica）","color":"family"},{"title":"辛巴达七航","text":"航海冒险","color":"gold"},{"title":"阿拉丁·阿里巴巴","text":"18世纪欧洲改编层","color":"antagonist"}]}
},
"xiaowangzi": {
  "id":"xiaowangzi","title":"小王子","original_title":"Le Petit Prince（The Little Prince）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"童话寓言","genre_group":"小说","language":"法语","author_id":"saintexupery","author_name":"安托万·德·圣埃克苏佩里",
  "year_display":"1943年出版（Britannica：Le Petit Prince (1943)）","year_sort":1943,
  "background":["Britannica：'Le Petit Prince (1943; The Little Prince), a child's fable for adults'——写给大人的童话。","Britannica：'has become a modern classic'（已成现代经典）——'a gentle and grave reminder that the best things in life are still the simplest ones and that real wealth is giving to others'。"],
  "outline":["'The story follows a pilot who crash lands in a desert and meets a little boy from a small planet'（坠机的飞行员遇见小行星来的男孩——Britannica）。","小王子的星际巡游：国王、爱慕虚荣者、酒鬼、商人、点灯人、地理学家（通说）。","玫瑰与狐狸：'people can only see rightly with the heart and that what is essential is invisible to the eye'（本质的东西肉眼看不见——Britannica）。"],
  "characters":[{"name":"飞行员","identity":"叙述者","note":"沙漠中的大人（Britannica）"},{"name":"小王子","identity":"B-612小行星来客","note":"星球巡游者（通说）"},{"name":"狐狸","identity":"驯养者","note":"'驯养'哲学（通说）"}],
  "themes":["本质与眼睛：用心去看（Britannica）。","驯养与责任（通说）。","大人的荒诞星球（通说）。"],
  "influence":[{"text":"Britannica：已成现代经典（a modern classic）；'real wealth is giving to others'。","source":"B223"},
    {"text":"全球译本数以百计（通说待核——Britannica 该页未载）。","source":"B223"}],
  "reading":{"difficulties":["寓意层与童话题面的双读。","玫瑰/狐狸的象征分配。"],
    "editions":["周克希译本（上海译文出版社，通说待核）。","马振骋译本（人民文学出版社，通说待核）。"],
    "order":"全书一次读完 → 回读狐狸一章 → 对照《夜航》。"},
  "pending":["1943年纽约 Reynal & Hitchcock 初版与法语版同年细节待核。","插图作者自绘说待核。","全球发行统计待核。"],
  "sources":["B223"],"year_source":"B223","author_source":"B223","related_works":["yisuo","weite","xiaojing"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《小王子》星球巡游图",
    "cards":[{"title":"B-612","text":"玫瑰与火山","color":"family"},{"title":"六个星球","text":"大人们的荒诞","color":"antagonist"},{"title":"地球","text":"狐狸与蛇","color":"main"},{"title":"回程","text":"用心去看（Britannica）","color":"gold"}]}
},
"jidushanbojue": {
  "id":"jidushanbojue","title":"基督山伯爵","original_title":"Le Comte de Monte-Cristo（The Count of Monte Cristo）","region":"法国","era":"近代","era_detail":"19世纪（七月王朝）",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"dumaspere","author_name":"大仲马（Alexandre Dumas père）",
  "year_display":"1844—1845年连载出版（Britannica：Le Comte de Monte Cristo (1844–45)）","year_sort":1844,
  "background":["Britannica：大仲马为'highly prolific and popular'的19世纪法国作家，《基督山伯爵》与《三个火枪手》为其最著名作品；'often working with collaborators (especially Auguste Maquet)'。","报章连载体：为偿债'forced to write more and more rapidly'（Britannica）——通俗连载的黄金形态。"],
  "outline":["水手唐泰斯在婚礼日遭嫉妒者构陷入狱十四年——伊夫堡（通说）。","狱中得法利亚神甫传授学识与宝藏所在；越狱后化身基督山伯爵逐个复仇（通说）。","终局：复仇完成，宽恕与远行（通说待核）。"],
  "characters":[{"name":"唐泰斯（基督山伯爵）","identity":"水手→伯爵","note":"复仇的化身（通说）"},{"name":"维尔福等","identity":"告密者三人组","note":"法官·银行家·军官（通说）"},{"name":"法利亚神甫","identity":"狱友","note":"知识与宝藏的授予者（通说）"}],
  "themes":["复仇的经济学：等待与希望（书末名句通说待核——'wait and hope'）。","身份与变身：复仇者的多重面具（通说）。","报章连载的叙事速度（Britannica 语境）。"],
  "influence":[{"text":"Britannica：《基督山伯爵》与《三个火枪手》为其 best-known works。","source":"B224"},
    {"text":"通俗历史小说的范本：对后世类型小说（武侠/复仇叙事）的深远影响（通说待核）。","source":"B224"}],
  "reading":{"difficulties":["体量巨大（两卷本）。","法政史背景（拿破仑百日/七月王朝）。"],
    "editions":["周克希/韩沪麟译本（上海译文出版社，通说待核）。","蒋学模译本（人民文学出版社，通说待核）。"],
    "order":"顺情节通读；狱中一章（法利亚）为精神枢纽。"},
  "pending":["连载起止日期（1844年8月—1846年1月《辩论报》说）待核。","书末'等待和希望'原文核对。","马凯贡献份额争议待核。"],
  "sources":["B224"],"year_source":"B224","author_source":"B224","related_works":["hongyuhei","balamingwuyuan","beican"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《基督山伯爵》复仇三部曲",
    "cards":[{"title":"婚礼日构陷","text":"十四年伊夫堡","color":"antagonist"},{"title":"法利亚神甫","text":"知识与宝藏","color":"family"},{"title":"化身伯爵","text":"巴黎的猎场","color":"main"},{"title":"等待与希望","text":"复仇的终点","color":"gold"}]}
},
"genjiwuyu": {
  "id":"genjiwuyu","title":"源氏物语","original_title":"源氏物语（The Tale of Genji）","region":"日本","era":"古代","era_detail":"平安时代",
  "genre":"长篇物语","genre_group":"小说","language":"日语（王朝文体）","author_id":"murasakishikibu","author_name":"紫式部",
  "year_display":"约1010年完成（Britannica：likely completing it about 1010）","year_sort":1010,
  "background":["Britannica：'Written at the start of the 11th century, it is generally considered the world's first novel'——一般被视为世界最早的长篇小说。","Britannica（作者页）：'generally considered the greatest work of Japanese literature and thought to be the world's oldest full novel'（日本文学最高杰作）。"],
  "outline":["'Most of the story concerns the loves of Genji, and each of the women in his life is vividly delineated'（源氏的爱恋与诸位女性的生动刻画——Britannica）；共54章（Britannica：54 chapters of one character and his legacy）。","后半部：宇治十帖（通说待核）。"],
  "characters":[{"name":"光源氏","identity":"皇子·廷臣","note":"'handsome, sensitive, gifted courtier'（Britannica）"},{"name":"紫之上","identity":"伴侣","note":"女主人公（通说）"},{"name":"藤壶","identity":"父帝女御","note":"禁忌之恋的原点（通说待核）"},{"name":"浮舟","identity":"宇治十帖主人公","note":"（通说待核）"}],
  "themes":["宫廷恋爱的荣光与代价（Britannica 语境）。","'物哀'——哀感的审美（通说待核——本居宣长提出）。","中日诗歌修养的织体：'informed by a comprehensive knowledge of Chinese and Japanese poetry'（Britannica）。"],
  "influence":[{"text":"Britannica：世界最早的长篇小说（world's first novel）；54章贯穿'one character and his legacy'。","source":"B226"},
    {"text":"Britannica（作者页）：日本文学的最高杰作（the greatest work of Japanese literature）。","source":"B227"}],
  "reading":{"difficulties":["平安朝称谓与官职。","和歌穿插——引文需读出声。","人物五代谱系——先画世系图。"],
    "editions":["丰子恺译本（人民文学出版社，通说待核）。","林文月译本（纯文学出版社/译林，通说待核）。"],
    "order":"前三十章通读 → 宇治十帖（浮舟）→ 回读桐壶。"},
  "pending":["丰子恺/林文月译本出版信息核对。","宇治十帖章数（45—54）核对。","本居宣长'物哀'论出处核对。"],
  "sources":["B226","B227"],"year_source":"B226","author_source":"B227","related_works":["honglou","xixue","luoshengmen"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《源氏物语》结构图",
    "cards":[{"title":"桐壶","text":"禁忌之恋的原点","color":"family"},{"title":"光源氏","text":"荣华与爱恋","color":"main"},{"title":"女人们","text":"逐一生动刻画（Britannica）","color":"gold"},{"title":"宇治十帖","text":"后代的余音","color":"plain"}]}
},
"dashiyumageeligeta": {
  "id":"dashiyumageeligeta","title":"大师与玛格丽特","original_title":"Мастер и Маргарита（The Master and Margarita）","region":"俄国","era":"现当代","era_detail":"苏联时期",
  "genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"bulgakov","author_name":"米哈伊尔·布尔加科夫",
  "year_display":"1928—1940年写作；1966—67年于苏联删节出版（Britannica）","year_sort":1966,
  "background":["Britannica：'Witty and ribald, and at the same time a penetrating philosophical novel wrestling with profound and eternal problems'（俏皮放达、又是与永恒难题缠斗的深邃哲思小说）。","出版史：'published in the Soviet Union only in 1966–67, and then in an egregiously censored form'（死后删节版——Britannica）。"],
  "outline":["双面并置：'juxtaposes two planes of action——one set in contemporary Moscow and the other in Pontius Pilate's Judea'（Britannica）。","魔鬼线：'The central character is the Devil—disguised as Professor Woland—who descends upon Moscow with his purgative'（魔鬼沃兰德降临莫斯科——Britannica）。","大师线：禁焚的手稿与玛格丽特的飞行（通说）。"],
  "characters":[{"name":"沃兰德","identity":"魔鬼","note":"化名教授（Britannica）"},{"name":"大师","identity":"作家","note":"手稿的作者（通说）"},{"name":"玛格丽特","identity":"大师之爱人","note":"魔鬼舞会女王（通说）"},{"name":"彼拉多","identity":"犹太大总督","note":"耶路撒冷线（通说）"}],
  "themes":["善与恶：撒旦之善（通说）。","苏联社会的讽刺（Britannica：satire of Soviet society）。","'手稿不会烧毁'——创作的不灭（名句通说待核）。"],
  "influence":[{"text":"Britannica：布尔加科夫以幽默与犀利讽刺著称；《大师与玛格丽特》为其杰作（语境）。","source":"B225"},
    {"text":"死后出版的世界性声誉：1966—67年删节版之后的完整化历程（通说待核）。","source":"B225"}],
  "reading":{"difficulties":["双城线切换。","苏联文艺界讽刺的真人影射（通说）。"],
    "editions":["钱诚译本（人民文学出版社，通说待核）。","高惠勤等译本（通说待核）。"],
    "order":"先莫斯科线通读 → 回读彼拉多线 → 复看舞会章。"},
  "pending":["沃兰德随从（卡罗维耶夫/河马/阿佐泽洛）人名核对。","1969年法兰克福全本版细节待核。","'手稿不会烧毁'原文核对。"],
  "sources":["B225"],"year_source":"B225","author_source":"B225","related_works":["shenpan","exin","yijiubasi"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《大师与玛格丽特》双城结构图",
    "cards":[{"title":"莫斯科","text":"沃兰德降临","color":"antagonist"},{"title":"耶路撒冷","text":"彼拉多的审判","color":"family"},{"title":"大师与玛格丽特","text":"手稿与舞会","color":"main"},{"title":"永恒的庇所","text":"结局（通说）","color":"gold"}]}
},
"tiepigu": {
  "id":"tiepigu","title":"铁皮鼓","original_title":"Die Blechtrommel（The Tin Drum）","region":"德国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"grass","author_name":"君特·格拉斯",
  "year_display":"1959年出版（Britannica：1959）","year_sort":1959,
  "background":["Britannica：'This exuberant picaresque novel, written in a variety of styles, imaginatively distorts and exaggerates his personal experiences'（多风格的狂想流浪汉小说，对个人经历作想象性的扭曲与夸大）。","但泽三部曲之首：后接《猫与鼠》（1961）与《狗年月》（1963）（Britannica）。"],
  "outline":["奥斯卡·马策拉特——'a dwarf who narrates from an asylum'（精神病院里 narrate 的侏儒——Britannica）；三岁生日自决停止生长，以铁皮鼓与尖叫记录但泽的纳粹化年代（通说+Britannica 语境：the creeping Nazification of average families）。","波兰走廊/但泽的多语环境：'the Polish-German dualism of Danzig……the attrition of the war years'（Britannica）。","结局：奥斯卡被控杀人进疗养院，以叙述自我清算（通说待核）。"],
  "characters":[{"name":"奥斯卡·马策拉特","identity":"侏儒·叙述者","note":"鼓与碎玻璃嗓（Britannica+通说）"},{"name":"阿格内斯","identity":"母亲","note":"两个父亲的故事（通说待核）"},{"name":"布朗斯基","identity":"表舅","note":"波兰认同（通说待核）"}],
  "themes":["小丑的见证：拒绝长大的拒绝服从（通说）。","日常家庭的纳粹化（Britannica）。","多风格拼贴：童话/歌德式/编年史（Britannica：variety of styles）。"],
  "influence":[{"text":"Britannica：格拉斯成为'在纳粹之下成年的一代德国人的文学声音'（语境）；1999年诺奖。","source":"B228"},
    {"text":"1979年施隆多夫电影版获戛纳金棕榈（与《现代启示录》并列）与奥斯卡最佳外语片（Britannica）。","source":"B228"}],
  "reading":{"difficulties":["奥斯卡的第一人称三视角（我/他/奥斯卡——通说待核）。","但泽德语-波兰语-卡舒比语地名。"],
    "editions":["胡其鼎译本（漓江出版社/上海译文，通说待核）。","德文原版（Steidl，通说待核）。"],
    "order":"对照《猫与鼠》《狗年月》补全但泽世界。"},
  "pending":["三视角（第一/第二/第三视角章法）核对。","《剥洋葱》2006年党卫军争议与本书的关系待核。","奥斯卡身高三英尺与'九岁'心智设定核对。"],
  "sources":["B228"],"year_source":"B228","author_source":"B228","related_works":["wuhao","renjianshige","dongwunongchang"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《铁皮鼓》但泽岁月结构图",
    "cards":[{"title":"三岁停长","text":"拒绝进入成人世界","color":"main"},{"title":"铁皮鼓与尖叫","text":"玻璃的武器","color":"gold"},{"title":"但泽","text":"德波双重世界（Britannica）","color":"family"},{"title":"疗养院","text":"叙述的现场","color":"plain"}]}
},
"qingren": {
  "id":"qingren","title":"情人","original_title":"L'Amant（The Lover）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"中长篇小说","genre_group":"小说","language":"法语","author_id":"duras","author_name":"玛格丽特·杜拉斯",
  "year_display":"1984年出版并获龚古尔奖（Britannica：L'Amant (1984; The Lover; film, 1992) won the prestigious Prix Goncourt in 1984）","year_sort":1984,
  "background":["Britannica：'The semiautobiographical story of L'Amant, about a French teenage girl's love affair with a Chinese man'（半自传：法国少女与中国男人的恋爱——Britannica）；1991年作者改写为《来自中国北方的情人》（Britannica）。","作者童年在中南半岛度过（Britannica：spent her childhood in Indochina）。"],
  "outline":["湄公河渡船上：15岁半的法国少女与中国富商之子的相遇（通说）。","西贡的单间、家庭的敌意与殖民地的目光（通说）。","老年重逢电话：'他对她说，和过去一样，他依然爱她，他不能不爱'（结尾名句通说待核）。"],
  "characters":[{"name":"少女（叙述者）","identity":"法国殖民地少女","note":"半自传性（Britannica）"},{"name":"中国情人","identity":"富商之子","note":"比少女年长（Britannica：12岁——原文'12'years her senior）"},{"name":"小哥哥","identity":"家人","note":"温情与阴影（通说待核）"}],
  "themes":["欲望与殖民的目光（通说）。","记忆的改写：1984年写作与1991年重写（Britannica）。","断裂句法的极简文体（Britannica：abstract and synthetic mode 语境）。"],
  "influence":[{"text":"Britannica：1984年龚古尔奖；《情人》电影1992年。","source":"B229"},
    {"text":"对谈式/意识流式中文写作的示范效应（通说待核）。","source":"B229"}],
  "reading":{"difficulties":["人称漂移（我/她）。","碎片时序。"],
    "editions":["王道乾译本（上海译文出版社，通说待核）。","法文原版（Minuit，通说待核）。"],
    "order":"对照《来自中国北方的情人》：同一素材的两次讲述。"},
  "pending":["王道乾译本信息核对。","结尾原句核对。","1992年电影（让-雅克·阿诺）细节待核。"],
  "sources":["B229"],"year_source":"B229","author_source":"B229","related_works":["moshengnvrendelaixin","baofali","daluolaiwei"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《情人》记忆改写结构图",
    "cards":[{"title":"湄公河渡船","text":"15岁半的相遇","color":"main"},{"title":"西贡单间","text":"殖民地的目光","color":"antagonist"},{"title":"写作","text":"1984龚古尔（Britannica）","color":"gold"},{"title":"1991重写","text":"来自中国北方的情人","color":"plain"}]}
},
"dierxing": {
  "id":"dierxing","title":"第二性","original_title":"Le Deuxième Sexe（The Second Sex）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"哲学论著","genre_group":"散文","language":"法语","author_id":"beauvoir","author_name":"西蒙娜·德·波伏瓦",
  "year_display":"1949年两卷出版（Britannica：Le Deuxième Sexe, 2 vol. (1949; The Second Sex)）","year_sort":1949,
  "background":["Britannica：'a scholarly and passionate plea for the abolition of what she called the myth of the eternal feminine'（为废除永恒女性神话而作的学术而热情的呼吁）；'It became a classic of feminist literature'（已成女性主义文学经典——Britannica）。","版本史（Britannica）：1953年英译遭严重删节；2009年新译首次完整呈现原文。"],
  "outline":["卷一《事实与神话》：生物学/精神分析/历史唯物论的批判+神话分析（通说待核）。","卷二《实际体验》：女性从童年到老年的处境书写（通说待核）。","核心命题：女人是'第二性'——他者化的产物（通说）。"],
  "characters":[{"name":"波伏瓦","identity":"论者","note":"以哲学与个案双轨写作"}],
  "themes":["'永恒女性'神话的解构（Britannica）。","处境论：性别是被造就的（通说；名句'One is not born, but rather becomes, a woman'待核）。","身体、劳动与自由的处境分析（通说）。"],
  "influence":[{"text":"Britannica：女性主义文学经典（classic of feminist literature）。","source":"B232"},
    {"text":"对20世纪60年代以降女性主义运动的理论奠基（通说待核）。","source":"B232"}],
  "reading":{"difficulties":["哲学与生物学的跨学科密度。","1953年英译删节问题——读2009年后新译。"],
    "editions":["郑克鲁译本（上海译文出版社，通说待核）。","桑竹影/南珊早期译本（对照版本史）。"],
    "order":"先读卷二导言与开篇（名句所在）→ 卷一神话章。"},
  "pending":["'One is not born, but rather becomes, a woman'原文核对。","郑克鲁译本信息核对。","《现代》杂志1945年创刊核对。"],
  "sources":["B232"],"year_source":"B232","author_source":"B232","related_works":["exin","mudanting","shinv"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《第二性》两卷结构图",
    "cards":[{"title":"卷一","text":"事实与神话","color":"family"},{"title":"卷二","text":"实际体验","color":"main"},{"title":"永恒女性","text":"神话的解构（Britannica）","color":"antagonist"},{"title":"处境论","text":"后天成为（名句待核）","color":"gold"}]}
},
"baidi": {
  "id":"baidi","title":"白痴","original_title":"Идиот（The Idiot）","region":"俄国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"dostoevsky","author_name":"费奥多尔·陀思妥耶夫斯基",
  "year_display":"1868—1869年连载发表（Britannica：published in Russian as Idiot in 1868–69）","year_sort":1868,
  "background":["Britannica：'The story involves the unsettling effect of the primitive Prince Myshkin on the sophisticated, conservative Yepanchin family'（'原始'的梅什金公爵给世故保守的叶潘钦家带来的不安）。","Britannica：梅什金的信息——'message of service, compassion, and brotherly love finally fails'（服务、同情与兄弟之爱的讯息最终失败）。"],
  "outline":["梅什金公爵自瑞士疗养归彼得堡——纯真者闯入名利场（通说）。","娜斯塔霞·菲利波夫娜的生日夜：十万元焚烧一幕（通说待核）。","结局：罗戈任杀死娜斯塔霞，梅什金重归痴呆（通说待核）。"],
  "characters":[{"name":"梅什金公爵","identity":"'白痴'","note":"纯真的局外人（Britannica 语境）"},{"name":"娜斯塔霞","identity":"没落贵族之女","note":"被侮辱者（通说）"},{"name":"罗戈任","identity":"商人之子","note":"激情的占有者（通说）"}],
  "themes":["基督式的纯真在世俗中的失败（Britannica：his message……finally fails）。","美将拯救世界？——争议命题（通说待核）。","金钱与羞辱的剧场（通说）。"],
  "influence":[{"text":"Britannica：1868—69年连载；梅什金的'不安效应'为全书枢纽。","source":"B230"},
    {"text":"'白痴'式的圣愚传统在俄国文学中的再现（通说待核）。","source":"B230"}],
  "reading":{"difficulties":["人物众多——先画人物表。","十九世纪彼得堡社交礼仪。"],
    "editions":["荣如德译本（上海译文出版社，通说待核）。","耿济之译本（人民文学出版社，通说待核）。"],
    "order":"可与《罪与罚》对读：理性犯罪 vs 纯真受难。"},
  "pending":["生日夜焚烧十万卢布情节核对。","'美将拯救世界'原文出处核对。","癫痫发作描写与作者自病经历的关系待核。"],
  "sources":["B230","B042"],"year_source":"B230","author_source":"B230","related_works":["zuiyufa","kalamasuofu","sihunling"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《白痴》三人结构图",
    "cards":[{"title":"梅什金","text":"纯真的闯入者","color":"main"},{"title":"娜斯塔霞","text":"被侮辱的美","color":"family"},{"title":"罗戈任","text":"激情的占有","color":"antagonist"},{"title":"失败","text":"兄弟之爱的落空（Britannica）","color":"gold"}]}
},
"liurenshengbi": {
  "id":"liurenshengbi","title":"猎人笔记","original_title":"Записки охотника（A Sportsman's Sketches，又译《猎人手记》）","region":"俄国","era":"近代","era_detail":"19世纪",
  "genre":"短篇小说集","genre_group":"小说","language":"俄语","author_id":"turgenev","author_name":"伊万·谢尔盖耶维奇·屠格涅夫",
  "year_display":"1852年首版（Britannica：first published in Russian as Zapiski okhotnika in 1852），1870年代增补","year_sort":1852,
  "background":["Britannica：'The stories concern life in rural Russia, in particular the relationship between landowners and their serfs'（俄国乡村生活——尤其地主与农奴的关系）。","视角：以猎人行脚串起诸篇；农奴的形象'always circumscribed by their serfdom'（总被农奴制框限——Britannica）。"],
  "outline":["名篇：《霍尔和卡里内奇》（首篇）、《白净草原》、《木木》、《总管》（篇目通说待核）。","地主群像与农奴群像的对位（Britannica 语境）。"],
  "characters":[{"name":"霍尔与卡里内奇","identity":"两个农奴","note":"理性与诗性双像（首篇，通说）"},{"name":"猎人","identity":"叙述者","note":"行脚视角"}],
  "themes":["农奴制的日常残酷：以'风景'写'制度'（通说）。","人性的尊严在底层（通说）。","俄罗斯自然风景的抒情化（通说）。"],
  "influence":[{"text":"Britannica：1852年初版——屠格涅夫第一部获得广泛承认的重要作品（语境）。","source":"B231"},
    {"text":"对俄国农奴制舆论的影响（通说待核——1861年废除农奴制的背景常被联系到本书）。","source":"B231"}],
  "reading":{"difficulties":["俄罗斯农奴制历史背景注释。","散文化的篇幅结构。"],
    "editions":["丰子恺译本（译文名著精选，通说待核）。","力冈译本（通说待核）。"],
    "order":"先读《霍尔和卡里内奇》《白净草原》→《木木》。"},
  "pending":["《木木》是否属初版（1852增订情况）待核。","丰子恺译本信息核对。","亚历山大二世受本书影响说（史料出处）待核。"],
  "sources":["B231"],"year_source":"B231","author_source":"B231","related_works":["fuyuzi","nahan","qikefuxuan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《猎人笔记》地主—农奴对位图",
    "cards":[{"title":"霍尔与卡里内奇","text":"首篇双像","color":"main"},{"title":"地主群像","text":"《总管》等（通说）","color":"antagonist"},{"title":"农奴群像","text":"尊严与屈辱","color":"gold"},{"title":"白净草原","text":"夜与自然","color":"family"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
