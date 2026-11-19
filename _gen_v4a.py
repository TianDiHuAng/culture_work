# -*- coding: utf-8 -*-
"""v4批次：13个新作家页"""
import json, pathlib

authors = {
"yudafu": {
  "id": "yudafu", "name": "郁达夫", "foreign_name": "Yu Dafu（郁达夫，1896-12-07—1945-09-17）",
  "country": "中国", "birth": 1896, "death": 1945, "birth_year": 1896, "death_year": 1945, "era": "现当代",
  "summary": "郁达夫，富阳人，创造社创始成员之一（Britannica：a founding member of the Creation Society, a group promoting modern Chinese literature）。留日归国（1922）后成为文坛明星（Britannica：he became a literary celebrity upon returning to China in 1922）。首部小说集《沉沦》（1921）以白话写作、因'坦率处理性'而大受欢迎（Britannica：Chenlun became a popular success in China because of its frank treatment of sex）。1945年遇害于南洋（Britannica 记卒于1945-09-17；苏门答腊遇害说为通说待核）。",
  "timeline": [
    {"year": 1896, "text": "生于浙江富阳（Britannica：Born December 7, 1896）。", "src": "B206"},
    {"year": 1921, "text": "首部小说集《沉沦》出版（Britannica：his first story collection was Chenlun (1921; Sinking)），创造社成立（通说待核）。", "src": "B206"},
    {"year": 1922, "text": "归国，成为文学名人（Britannica：he became a literary celebrity upon returning to China in 1922）。", "src": "B206"},
    {"year": 1923, "text": "患肺结核后主题转变——由自我转向大众（Britannica：after contracting tuberculosis, he abruptly changed his major theme）。", "src": "B206"},
    {"year": 1945, "text": "卒（Britannica：died September 17, 1945；南洋遇害说通说待核）。", "src": "B206"}
  ],
  "major_works": [
    {"work_id": "chenlun", "note": "首部小说集（Britannica：Chenlun (1921)）"},
    {"title": "日记九种、过去", "note": "1927年作品（Britannica：Rijijiuzhong; Guoqu (1927)）"},
    {"title": "出奔", "note": "1935年（Britannica：Chuben (1935; Flight)）"}
  ],
  "style": [
    "'自叙传'抒情小说：以大胆的自我暴露写零余者的苦闷（通说）。",
    "'坦率处理性'：《沉沦》因 frank treatment of sex 大受欢迎亦招非议（Britannica）。",
    "旧体诗与散文造诣亦深（通说待核）。"
  ],
  "status": "Britannica 定位郁达夫为 1920 年代读者最广的中国短篇小说家之一（a widely read Chinese short-story writer of the 1920s）、创造社创始成员；其《沉沦》是新文学早期白话小说的代表（Britannica：written in vernacular Chinese, as advocated by the new generation of writers）。",
  "sources": ["B206"], "dates_source": "B206",
  "pending": ["创造社成立细节（1921年东京说）待核。", "1945年苏门答腊遇害细节待核。", "《沉沦》篇目（三篇说：《沉沦》《南迁》《银灰色的死》）待核。"]
},
"guomoruo": {
  "id": "guomoruo", "name": "郭沫若", "foreign_name": "Guo Moruo（郭沫若，1892年11月—1978-06-12）",
  "country": "中国", "birth": 1892, "death": 1978, "birth_year": 1892, "death_year": 1978, "era": "现当代",
  "summary": "郭沫若，乐山沙湾人，20世纪中国最重要的学者、诗人与作家之一，曾任中国科学院院长等要职（Britannica：a leading 20th-century Chinese scholar, poet, and writer……as president of the Chinese Academy of Sciences）。新诗发表于《时事新报》后辑为《女神》（1921）——'为中国新诗发展奠定了第一块基石'（Britannica：laid the first cornerstone for the development of new verse in China）。'在每个文类上都极其多产'（Britannica：enormously prolific in every genre）——诗歌、小说、戏剧、自传、翻译。",
  "timeline": [
    {"year": 1892, "text": "生于四川乐山沙湾（Britannica：Born November 1892, Shawan, Leshan county, Sichuan province）。", "src": "B207"},
    {"year": 1921, "text": "新诗结集为《女神》出版（Britannica：later compiled into the anthology Nü shen (1921; Goddess)）。", "src": "B207"},
    {"year": "1921—37", "text": "创造社主要成员（通说待核）；北伐与流亡日本时期（通说待核）。", "src": "B207"},
    {"year": 1949, "text": "后任中国科学院院长等（Britannica：high-ranking government official in the People's Republic of China）。", "src": "B207"},
    {"year": 1978, "text": "卒于北京（Britannica：Died June 12, 1978, Beijing）。", "src": "B207"}
  ],
  "major_works": [
    {"work_id": "nvshen", "note": "诗集（Britannica：Nü shen (1921; Goddess)）"},
    {"title": "屈原（历史剧）", "note": "1942年（通说待核）"},
    {"title": "甲申三百年祭、甲骨文研究", "note": "学术（通说待核）"}
  ],
  "style": [
    "'浪漫主义'开山：自我扩张、火山式抒情（通说）。",
    "自由体新诗：不受旧格律束缚——为中国新诗奠基（Britannica：laid the first cornerstone for the development of new verse）。",
    "多面手：诗人/学者/政治家三位一体（Britannica：enormously prolific in every genre）。"
  ],
  "status": "Britannica 称郭沫若为 20 世纪中国最重要的作家之一、新诗发展的奠基人（laid the first cornerstone for the development of new verse in China）；其《女神》为中国现代新诗的起点（通说与 Britannica 互证）。",
  "sources": ["B207"], "dates_source": "B207",
  "pending": ["生月（1892年11月16日说）精确日期待核。", "创造社时期细节待核。", "历史剧《屈原》1942年细节待核。"]
},
"baixianyung": {
  "id": "baixianyung", "name": "白先勇", "foreign_name": "Pai Hsien-yung（白先勇，1937— ）",
  "country": "中国", "birth": 1937, "death": None, "birth_year": 1937, "death_year": None, "era": "现当代",
  "summary": "白先勇，将门之后，生于桂林、后随家赴台，台湾现代主义文学运动的领军人物（Britannica：a leading figure of Taiwan's Modernist literary movement of the 1960s）；'其小说影响力延续到21世纪'（Britannica：his fiction has remained influential well into the 21st century）。代表作《台北人》（通说）、《游园惊梦》（Britannica：Yu-yüan ching-meng (1982; Wandering in the Garden, Waking from a Dream)）。晚年致力于昆曲青春版《牡丹亭》推广（通说待核）。",
  "timeline": [
    {"year": 1937, "text": "生于广西桂林（通说待核；Britannica 该页未载生卒）。", "src": "B208"},
    {"year": 1952, "text": "随家迁台（通说待核）。", "src": "B208"},
    {"year": 1960, "text": "与同学创办《现代文学》杂志（通说待核）。", "src": "B208"},
    {"year": "1965—71", "text": "《台北人》各篇陆续发表并结集（通说待核）。", "src": "B208"},
    {"year": 1982, "text": "《游园惊梦》出版（Britannica：Yu-yüan ching-meng (1982)）。", "src": "B208"}
  ],
  "major_works": [
    {"work_id": "taibeiren", "note": "短篇小说集（通说；本库立目）"},
    {"title": "游园惊梦", "note": "（Britannica：Yu-yüan ching-meng (1982)）"},
    {"title": "孽子", "note": "长篇（通说待核）"}
  ],
  "style": [
    "'大陆—台湾'的双重时空：流亡者的乡愁与今昔对照（通说）。",
    "中国古典与西方现代主义技法的融合（Britannica：Modernist literary movement）。",
    "写实与悲悯：写没落贵族、市井众生（通说）。"
  ],
  "status": "Britannica 定位白先勇为台湾现代主义文学领军人物，且是 1949 年后台湾作家中'影响力延续至 21 世纪'的代表（remained influential well into the 21st century——Britannica）；'台北人'系列被广泛视为其巅峰（通说待核）。",
  "sources": ["B208"], "dates_source": "B208",
  "pending": ["生年1937与桂林出生（Britannica 该页未载）待核。", "《台北人》1971年结集（远景出版社说）待核。", "《现代文学》杂志1960年创刊细节待核。"]
},
"wanganyi": {
  "id": "wanganyi", "name": "王安忆", "foreign_name": "Wang Anyi（王安忆，1954-03-06— ）",
  "country": "中国", "birth": 1954, "death": None, "birth_year": 1954, "death_year": None, "era": "现当代",
  "summary": "王安忆，生于南京，作家茹志鹃之女（英文维基：Her mother was the prominent writer Ru Zhijuan）；中国作协副主席（2006年起）、复旦大学教授（英文维基）。'The Song of Everlasting Sorrow'（《长恨歌》）为其最著名小说——'traces the life story of a young Shanghainese girl from the 1940s all the way till her death after the Cultural Revolution'（英文维基），2000年获第五届茅盾文学奖（英文维基）；2017年获纽曼华语文学奖（英文维基）。被视为张爱玲的传人（英文维基：earned the reputation of Wang as the successor of Eileen Chang——海派书写）。",
  "timeline": [
    {"year": 1954, "text": "生于南京，一岁随母迁上海（英文维基：Born March 6, 1954 Nanjing；moved to Shanghai with her mother when she was a year old）。", "src": "B216"},
    {"year": 1970, "text": "赴安徽五河插队（英文维基：sent down to the countryside of Wuhe County, Anhui）。", "src": "B216"},
    {"year": 1978, "text": "回上海任《儿童时代》编辑（英文维基：worked as an editor of the literature magazine Childhood）。", "src": "B216"},
    {"year": 1996, "text": "《长恨歌》出版（英文维基：In 1996, Wang's most famous novel, The Song of Everlasting Sorrow）。", "src": "B216"},
    {"year": 2000, "text": "获第五届茅盾文学奖（英文维基：won the most prestigious Mao Dun Literary Prize in 2000）。", "src": "B216"}
  ],
  "major_works": [
    {"work_id": "changhenge", "note": "长篇（英文维基：The Song of Everlasting Sorrow (1995/1996)）"},
    {"title": "小鲍庄", "note": "中篇，1985年（英文维基：Baotown (1985)）"},
    {"title": "流逝、本次列车终点", "note": "获奖中短篇（英文维基）"}
  ],
  "style": [
    "海派写实：以弄堂市民书写上海（英文维基：Haipai (Shanghai style)）。",
    "'以小见大'：从人物命运折射时代变迁（英文维基：narrative methods that see the 'big' from the 'small'——转引）。",
    "写实主义的城市日常：'stories are about everyday urban life'（英文维基转引 Jeffrey Kinkley）。"
  ],
  "status": "英文维基定位王安忆为当代中国最重要的作家之一：作协副主席、复旦教授；《长恨歌》被视为其写作的巅峰（made Wang's writing reached its peak——英文维基口径）并获茅奖；戴锦华评其'善于捕捉日常生活的微型戏剧'（英文维基转引 Dai Jinhua）。",
  "sources": ["B216"], "dates_source": "B216",
  "pending": ["《长恨歌》初刊（《钟山》1995年连载说）与单行本年份待核。", "王琦瑶原型'蓝桥事件'新闻源细节待核。", "2017 Newman Prize 与 2013 法国艺术与文学勋章细节（英文维基已载）可再核对。"]
},
"jiapingwa": {
  "id": "jiapingwa", "name": "贾平凹", "foreign_name": "Jia Pingwa（贾平凹，1952-02-21— ）",
  "country": "中国", "birth": 1952, "death": None, "birth_year": 1952, "death_year": None, "era": "现当代",
  "summary": "贾平凹，陕西丹凤棣花村人，'中国最受欢迎的小说家、短篇小说家、诗人与非虚构作者之一'（英文维基：one of China's most popular authors）。商州系列开创乡土书写；《废都》（1993）因性描写被禁17年（英文维基：banned by the State Publishing Administration for over 17 years），2009年解禁（英文维基）；《秦腔》（2005）获第七届茅盾文学奖（英文维基：winner of the 2008 Mao Dun Literature Prize）与首届红楼梦奖（英文维基：2006 Hong Kong The Dream of the Red Chamber Award）。陕西省作协主席、中国作协副主席团成员（英文维基）。",
  "timeline": [
    {"year": 1952, "text": "生于陕西商洛丹凤县棣花村（英文维基：Born 21 February 1952 Dihua Village, Danfeng County, Shangluo, Shaanxi）。", "src": "B217"},
    {"year": 1971, "text": "入西北大学中文系（英文维基：sent to study literature at Northwest University in Xi'an in 1971）。", "src": "B217"},
    {"year": 1978, "text": "短篇《满月》获全国奖（英文维基：his short story Full Moon won a national award from the China Writers Association）。", "src": "B217"},
    {"year": 1993, "text": "《废都》出版后被禁（英文维基：Ruined City……banned……for over 17 years）。", "src": "B217"},
    {"year": 2005, "text": "《秦腔》出版（英文维基：Qin Qiang (2005)）；2008年获茅盾文学奖（英文维基）。", "src": "B217"}
  ],
  "major_works": [
    {"work_id": "qinqiang", "note": "长篇（英文维基：The Shaanxi Opera (Qin Qiang, 2005)）"},
    {"title": "废都", "note": "1993年（英文维基：Ruined City；2016年英译 Ruined City）"},
    {"title": "商州三录、月迹", "note": "散文（英文维基）"}
  ],
  "style": [
    "乡土书写：商州世界的变迁与挽歌（英文维基：native-place fiction）。",
    "'传统白话叙事与现代现实主义的混合'（英文维基转引 Carlos Rojas：mixing traditional vernacular story-telling with modern realism）。",
    "古朴与混沌并存的语言：'以中国传统美学的眼光写当代'（通说）。"
  ],
  "status": "英文维基称贾平凹为'中国最受欢迎的作者之一'；商州系列奠定乡土文学地位；《废都》的禁毁史是中国当代出版审查的重要案例（英文维基专节）；《秦腔》为茅奖与红楼梦奖双料得主。",
  "sources": ["B217"], "dates_source": "B217",
  "pending": ["《秦腔》茅奖届次（第七届/2008年颁给2003—06年间作品）与《收获》首发细节核对。", "《废都》解禁日期（2009年说）与出版社细节待核。", "'平凹'读音（píngwā）说明（英文维基已载）可入正文。"]
},
"shitiesheng": {
  "id": "shitiesheng", "name": "史铁生", "foreign_name": "Shi Tiesheng（史铁生，1951-01-04—2010-12-31）",
  "country": "中国", "birth": 1951, "death": 2010, "birth_year": 1951, "death_year": 2010, "era": "现当代",
  "summary": "史铁生，北京人，散文家与小说家，以'对残障、苦难、命运、信仰与人之境遇的深刻哲学思考'著称（英文维基：profound philosophical reflections on disability, suffering, fate, faith, and the human condition）。1969年赴陕北插队，1972年21岁双腿瘫痪（英文维基：In 1972, at age 21, he became paralyzed in both legs）。《我与地坛》（1991）为'20世纪中国最好的散文之一'（China Daily 转述，见英文维基：Many critics have considered I and the Temple of Earth as one of the best Chinese prose essays of the 20th century）。晚年患尿毒症靠透析维持，2010年12月31日因脑溢血去世（英文维基），捐献肝脏（英文维基）。",
  "timeline": [
    {"year": 1951, "text": "生于北京（英文维基：Born 4 January 1951 Beijing）。", "src": "B218"},
    {"year": 1969, "text": "赴陕北插队（英文维基：sent to a rural village in Shaanxi Province as part of the Down to the Countryside Movement）。", "src": "B218"},
    {"year": 1972, "text": "21岁双腿瘫痪，回京（英文维基：at age 21, he became paralyzed in both legs）。", "src": "B218"},
    {"year": 1991, "text": "《我与地坛》发表（英文维基：I and the Temple of Earth (我与地坛, 1991)）。", "src": "B218"},
    {"year": 2010, "text": "12月31日因脑溢血去世（英文维基：died of cerebral hemorrhage）。", "src": "B218"}
  ],
  "major_works": [
    {"work_id": "woyuditan", "note": "散文（英文维基：1991年）"},
    {"title": "我的遥远的清平湾", "note": "短篇，1983年全国优秀短篇小说奖（英文维基）"},
    {"title": "命若琴弦、务虚笔记、病隙碎笔", "note": "1985/1996/2002（英文维基）"}
  ],
  "style": [
    "'轮椅上的写作'：残障经验升华为存在之思（英文维基：writer in a wheelchair）。",
    "宗教感与哲学性：苦难、救赎与超越（英文维基：philosophical and religious themes, exploring love, redemption, and transcendence）。",
    "母亲书写的深情：《我与地坛》第二主题（通说）。"
  ],
  "status": "英文维基称史铁生去世后'在21世纪年轻读者中经历显著的再流行'（a significant resurgence in popularity, particularly among young readers）；《我与地坛》入选教材并被广泛英译（英文维基）；2002年老舍文学奖（英文维基）。",
  "sources": ["B218"], "dates_source": "B218",
  "pending": ["《我与地坛》首发刊物（《上海文学》1991年第1期说）待核。", "老舍文学奖2002年（英文维基已载）具体作品待核。", "'职业是生病，业余在写作'自述出处待核。"]
},
"thomasmann": {
  "id": "thomasmann", "name": "托马斯·曼", "foreign_name": "Thomas Mann（托马斯·曼，1875-06-06—1955-08-12）",
  "country": "德国", "birth": 1875, "death": 1955, "birth_year": 1875, "death_year": 1955, "era": "现当代",
  "summary": "托马斯·曼，吕贝克人，德国小说家与散文家（Britannica：a German novelist and essayist），《布登勃洛克一家》《魂断威尼斯》《魔山》为其早期代表作，1929年获诺贝尔文学奖（Britannica）。一战期间一度威权立场、后转向民主，1933年流亡，1936年被纳粹剥夺德国国籍（Britannica：stripped of German citizenship），1938年起旅居美国，1952年定居苏黎世附近（Britannica）。",
  "timeline": [
    {"year": 1875, "text": "生于吕贝克（Britannica：Born June 6, 1875, Lübeck）。", "src": "B209"},
    {"year": 1901, "text": "《布登勃洛克一家》出版（Britannica：the novel builds the story of the family and its business house over four generations；年份通说待核）。", "src": "B209"},
    {"year": 1924, "text": "《魔山》出版（通说待核；Britannica 语境）。", "src": "B209"},
    {"year": 1929, "text": "获诺贝尔文学奖（Britannica：Nobel Prize 1929）。", "src": "B209"},
    {"year": 1933, "text": "离开德国开始流亡（Britannica：left Germany 1933）。", "src": "B209"}
  ],
  "major_works": [
    {"work_id": "mosha", "note": "长篇（Britannica 语境）"},
    {"title": "布登勃洛克一家", "note": "（Britannica：Buddenbrooks）"},
    {"title": "魂断威尼斯、浮士德博士", "note": "（通说待核）"}
  ],
  "style": [
    "'反讽的史诗'：家族衰亡题材的冷峻观察（Britannica：a tender elegy for the old bourgeois virtues）。",
    "观念小说：以疗养院映照欧洲文明的可能与危险（Britannica：the spiritual reflection of the possibilities and dangers of the actual world）。",
    "音乐性与神话结构（通说待核）。"
  ],
  "status": "Britannica 定位托马斯·曼为德国小说家与散文家、1929年诺奖得主；其流亡生涯与对纳粹的反对使其成为'德国良知的象征'（通说待核，Britannica 记其被剥夺国籍与流亡事实）。",
  "sources": ["B209"], "dates_source": "B209",
  "pending": ["《魔山》1924年出版与连载（1923年起）细节待核。", "《布登勃洛克一家》1901年出版待核。", "《浮士德博士》1947年待核。"]
},
"faulkner": {
  "id": "faulkner", "name": "威廉·福克纳", "foreign_name": "William Faulkner（威廉·福克纳，1897-09-25—1962-07-06）",
  "country": "美国", "birth": 1897, "death": 1962, "birth_year": 1897, "death_year": 1962, "era": "现当代",
  "summary": "福克纳，密西西比州人，美国小说家与短篇小说家，'现代主义与南方哥特文学的领军人物'（Britannica 语境：a leading figure of Modernism and Southern gothic fiction），大部分作品设定在虚构的约克纳帕塔法县（Britannica：the fictional Yoknapatawpha County），以意识流等实验技巧著称（Britannica：experimental techniques like stream-of-consciousness narration）。1949年获诺贝尔文学奖（Britannica：awarded the 1949 Nobel Prize for Literature）。",
  "timeline": [
    {"year": 1897, "text": "生于密西西比州新奥尔巴尼（Britannica：Born September 25, 1897, New Albany, Mississippi）。", "src": "B210"},
    {"year": 1929, "text": "《喧哗与骚动》出版（Britannica：In The Sound and the Fury, his first major novel……；年份通说待核）。", "src": "B210"},
    {"year": 1936, "text": "《押沙龙，押沙龙！》出版（通说待核）。", "src": "B210"},
    {"year": 1949, "text": "获诺贝尔文学奖（Britannica：awarded the 1949 Nobel Prize for Literature）。", "src": "B210"},
    {"year": 1962, "text": "卒于密西西比州（Britannica：Died July 6, 1962, Byhalia, Mississippi）。", "src": "B210"}
  ],
  "major_works": [
    {"work_id": "xuanhuayusaodong", "note": "长篇（Britannica：his first major novel）"},
    {"title": "押沙龙，押沙龙！", "note": "（通说待核）"},
    {"title": "我弥留之际、去吧，摩西", "note": "（通说待核）"}
  ],
  "style": [
    "意识流与多视角叙事：'radical technical experimentation'（Britannica）。",
    "南方历史的重负：种族、家族与罪（通说）。",
    "约克纳帕塔法世系：'一个邮票大小的地方'写整个世界（通说待核——'little postage stamp of native soil'出处待核）。"
  ],
  "status": "Britannica 定位福克纳为美国现代主义与南方哥特领军人物、1949年诺奖得主；其对拉丁美洲作家（马尔克斯等）的深远影响为通说（待核）。",
  "sources": ["B210"], "dates_source": "B210",
  "pending": ["《喧哗与骚动》1929年出版精确日期待核。", "'邮票大小的故乡'引语出处待核。", "诺奖演说'endure and prevail'细节待核。"]
},
"dazaiosamu": {
  "id": "dazaiosamu", "name": "太宰治", "foreign_name": "Dazai Osamu（太宰治，本名津岛修治，1909-06-19—1948-06-13）",
  "country": "日本", "birth": 1909, "death": 1948, "birth_year": 1909, "death_year": 1948, "era": "现当代",
  "summary": "太宰治，本名津岛修治，青森县金木町人，'战后日本最重要的文学声音'（Britannica 语境：the leading literary voice of postwar Japan）。'其阴郁而自嘲的笔调完美捕捉了战后日本的混乱——传统价值观崩解之际'（Britannica：His dark, wry tone perfectly captured the confusion of postwar Japan, when traditional values were discredited）。代表作《斜阳》（1947）《人间失格》（1948）（Britannica）。1948年与情人山崎富荣投水自尽（Britannica：committed suicide in 1948；地点通说待核）。",
  "timeline": [
    {"year": 1909, "text": "生于青森县（Britannica：Born June 19, 1909, Kanagi, Aomori prefecture）。", "src": "B211"},
    {"year": 1933, "text": "开始使用'太宰治'笔名（通说待核）。", "src": "B211"},
    {"year": 1947, "text": "《斜阳》《维庸之妻》出版（Britannica：Shayō (1947; The Setting Sun), Biyon no tsuma (1947; Villon's Wife)）。", "src": "B211"},
    {"year": 1948, "text": "《人间失格》发表（Britannica：Ningen shikkaku (1948; No Longer Human)）；6月13日自杀（Britannica）。", "src": "B211"}
  ],
  "major_works": [
    {"work_id": "renjianshige", "note": "（Britannica：Ningen shikkaku (1948)）"},
    {"title": "斜阳", "note": "1947年（Britannica）"},
    {"title": "维庸之妻、跑吧！梅洛斯", "note": "（通说待核）"}
  ],
  "style": [
    "'私小说'传统与无赖派：自嘲、堕落与纯粹的软弱（通说；Britannica 语境：dark, wry tone）。",
    "手记体：以三篇手记拼贴大庭叶藏的一生（通说）。",
    "幽默与滑稽的另一面（Britannica：humor verging on farce）。"
  ],
  "status": "Britannica 定位太宰治为战后日本最重要的文学声音之一；《人间失格》为其绝笔级代表作（'情感危机的反映'——Britannica：reflecting the emotional crisis of the author）；战后作品多经 Donald Keene 英译（Britannica）。",
  "sources": ["B211"], "dates_source": "B211",
  "pending": ["玉川上水投水自尽地点细节待核。", "'生而为人，我很抱歉'名句归属辨析（寺内寿太郎原句说）待核。", "无赖派（buraiha）概念界定待核。"]
},
"lessing": {
  "id": "lessing", "name": "多丽丝·莱辛", "foreign_name": "Doris Lessing（多丽丝·莱辛，1919-10-22—2013-11-17）",
  "country": "英国", "birth": 1919, "death": 2013, "birth_year": 1919, "death_year": 2013, "era": "现当代",
  "summary": "莱辛，生于波斯（今伊朗）克尔曼沙阿、长于南罗得西亚（今津巴布韦），英国作家（Britannica：British writer, born in Persia and raised in Southern Rhodesia）。'其小说与短篇关注卷入20世纪社会政治动荡的个人'（Britannica：largely concerned with people involved in the social and political upheavals of the 20th century）。《金色笔记》（1962）——'一位女作家试图与她的时代生活和解'（Britannica：in which a woman writer attempts to come to terms with the life of her times）。2007年获诺贝尔文学奖（Britannica），时年88岁为最年长诺奖文学得主（通说待核）。",
  "timeline": [
    {"year": 1919, "text": "生于波斯克尔曼沙阿（Britannica：Born October 22, 1919, Kermānshāh, Persia）。", "src": "B212"},
    {"year": 1949, "text": "移居英国，携《野草在歌唱》手稿（通说待核）。", "src": "B212"},
    {"year": 1962, "text": "《金色笔记》出版（Britannica：The Golden Notebook (1962)）。", "src": "B212"},
    {"year": 2007, "text": "获诺贝尔文学奖（Britannica：She was awarded the Nobel Prize for Literature in 2007）。", "src": "B212"},
    {"year": 2013, "text": "卒于伦敦（Britannica：Died November 17, 2013, London）。", "src": "B212"}
  ],
  "major_works": [
    {"work_id": "jinsebiji", "note": "长篇（Britannica：1962）"},
    {"title": "野草在歌唱", "note": "1950年（通说待核）"},
    {"title": "玛莎·奎斯特五部曲、拉格泰姆系列", "note": "（通说待核）"}
  ],
  "style": [
    "社会政治关怀与心理深度的结合（Britannica：social and political upheavals）。",
    "形式实验：《金色笔记》以四色笔记+自由文本的结构拼贴（通说）。",
    "女性经验的书写：'自由女性'主题（通说；莱辛本人对被标签化持保留态度——通说待核）。"
  ],
  "status": "Britannica 定位莱辛为英国作家、2007年诺奖得主；《金色笔记》被广泛视为女性主义文本与形式实验的双重经典（通说待核；亦被诺奖授奖词以'史诗性的女性经验书写者'定位——引文待核）。",
  "sources": ["B212"], "dates_source": "B212",
  "pending": ["《野草在歌唱》1950年出版待核。", "诺奖授奖词'epistemic'评语原文待核。", "苏菲神秘主义研究（苏非派时期）细节待核。"]
},
"rushdie": {
  "id": "rushdie", "name": "萨尔曼·拉什迪", "foreign_name": "Salman Rushdie（萨尔曼·拉什迪，1947-06-19— ）",
  "country": "英国", "birth": 1947, "death": None, "birth_year": 1947, "death_year": None, "era": "现当代",
  "summary": "拉什迪，生于孟买的英裔美籍小说家（Britannica：Indian-born British-American novelist），以《午夜之子》《撒旦诗篇》等寓言性作品著称（Britannica：known for allegorical works like Midnight's Children and The Satanic Verses）。《午夜之子》（1981）获布克奖，并获'布克中的布克'（1993）与'布克奖40年最佳'（2008）（Britannica：a fable about modern India, was an unexpected critical and popular success）。1989年因《撒旦诗篇》遭伊朗精神领袖霍梅尼下令追杀（fatwa），隐匿近十年；2022年在纽约文学活动遇袭受伤（Britannica：a 2022 knife attack……cost him an eye）。",
  "timeline": [
    {"year": 1947, "text": "生于孟买（Britannica：June 19, 1947——born in Bombay）。", "src": "B213"},
    {"year": 1981, "text": "《午夜之子》出版并获布克奖（Britannica：received the Booker Prize in 1981 for Midnight's Children）。", "src": "B213"},
    {"year": 1989, "text": "《撒旦诗篇》引发 fatwa（Britannica：February 14, 1989）。", "src": "B213"},
    {"year": 2007, "text": "受封爵士（Britannica：knighted）。", "src": "B213"},
    {"year": 2022, "text": "8月在纽约州肖托夸遇袭（Britannica：attacked in Chautauqua, New York）。", "src": "B213"}
  ],
  "major_works": [
    {"work_id": "wuzhizidezi", "note": "长篇（Britannica：1981 Booker）"},
    {"title": "撒旦诗篇", "note": "1988年（Britannica）"},
    {"title": "羞耻、摩尔人的最后叹息", "note": "（通说待核）"}
  ],
  "style": [
    "魔幻现实主义与印度口述传统的嫁接：'想象的历史'（通说）。",
    "多语混成（英语+印地语/乌尔都语词汇）与不可靠叙述（通说）。",
    "政治寓言：以个体的诞生隐喻国家的诞生（通说）。"
  ],
  "status": "Britannica 定位拉什迪为'关于言论自由与审查辩论的中心人物'（a central figure in debates about free speech and censorship）；《午夜之子》为布克奖史上最佳（布克中的布克——Britannica）。",
  "sources": ["B213"], "dates_source": "B213",
  "pending": ["《午夜之子》中译本信息待核。", "三亿零一分钟印度史（'30分钟'倍数说）细节待核。", "2022遇袭案后续（Britannica 已载2026年定罪进展）可更新。"]
},
"zweig": {
  "id": "zweig", "name": "斯蒂芬·茨威格", "foreign_name": "Stefan Zweig（斯蒂芬·茨威格，1881-11-28—1942-02-23）",
  "country": "奥地利", "birth": 1881, "death": 1942, "birth_year": 1881, "death_year": 1942, "era": "现当代",
  "summary": "茨威格，维也纳人，奥地利作家——'在诗歌、散文、短篇小说与戏剧多个文类皆有成就，尤以对虚构与历史人物的刻画最负盛名'（Britannica：achieved distinction in several genres……most notably in his interpretations of imaginary and historical characters）。'对心理学与弗洛伊德学说的兴趣，造就了他最具个人特色的工作：对人物心理的精细刻画'（Britannica：Zweig's interest in psychology and the teachings of Sigmund Freud led to his most characteristic work, the subtle portrayal of character）。1934年遭纳粹流亡，1942年与妻子在巴西里约附近自尽（Britannica：he and his second wife died by suicide in 1942）。",
  "timeline": [
    {"year": 1881, "text": "生于维也纳（Britannica：Born November 28, 1881, Vienna）。", "src": "B214"},
    {"year": 1901, "text": "首部诗集出版（通说待核）。", "src": "B214"},
    {"year": 1922, "text": "《一个陌生女人的来信》等中篇结集发表（通说待核；Britannica 该页未提本篇）。", "src": "B214"},
    {"year": 1934, "text": "遭纳粹驱逐开始流亡（Britannica：Exiled by the Nazis in 1934）。", "src": "B214"},
    {"year": 1942, "text": "2月23日在巴西彼得罗波利斯自尽（Britannica：Found dead February 23, 1942, Petrópolis）。", "src": "B214"}
  ],
  "major_works": [
    {"work_id": "moshengnvrendelaixin", "note": "中篇（通说；本库立目）"},
    {"title": "人类群星闪耀时、昨日的世界", "note": "历史特写与回忆录（通说待核）"},
    {"title": "象棋的故事", "note": "中篇，1942年（通说待核）"}
  ],
  "style": [
    "'心理现实主义'：弗洛伊德式的人物内心剖析（Britannica）。",
    "女性视角的情感叙事（陌生女人来信以书信体自白——通说）。",
    "'昨日的世界'：对欧洲黄金时代的怀旧与幻灭（通说待核）。"
  ],
  "status": "Britannica 定位茨威格为多文类大师、以心理刻画著称；其作品在中国的传播极广（高尔基曾评——通说待核），但 Britannica 该页未提《陌生女人来信》——本页对该作品的分析以通说为锚并列为待核。",
  "sources": ["B214"], "dates_source": "B214",
  "pending": ["《一个陌生女人的来信》1922年（首次发表于《大日记》说）细节待核。", "徐静蕾电影《一个陌生女人的来信》2005年改编待核。", "高尔基评语'以罕见的温存与同情写女人'出处待核。"]
},
"sartre": {
  "id": "sartre", "name": "让-保罗·萨特", "foreign_name": "Jean-Paul Sartre（让-保罗·萨特，1905-06-21—1980-04-15）",
  "country": "法国", "birth": 1905, "death": 1980, "birth_year": 1905, "death_year": 1980, "era": "现当代",
  "summary": "萨特，巴黎人，法国哲学家、小说家与剧作家，20世纪存在主义的旗手（Britannica 语境：the leading voice of 20th-century existentialism）。《恶心》（1938）为其首部长篇（Britannica：During his years of teaching in Le Havre, Sartre published La Nausée (1938; Nausea)）；《存在与虚无》（1943）奠定哲学体系（Britannica）。'人是被判处自由的'（Britannica：Man is condemned to be free）。1964年获诺贝尔文学奖并公开拒绝（Britannica：famously declined the prize），拒绝成为'制度中人'。与西蒙娜·德·波伏娃的伴侣关系（1929年结识——Britannica）亦为思想史佳话。",
  "timeline": [
    {"year": 1905, "text": "生于巴黎（Britannica：Born June 21, 1905, Paris）。", "src": "B215"},
    {"year": 1929, "text": "毕业于巴黎高师，结识波伏娃（Britannica：Graduated École Normale Supérieure 1929; Met Simone de Beauvoir 1929）。", "src": "B215"},
    {"year": 1938, "text": "《恶心》出版（Britannica：La Nausée (1938; Nausea)）。", "src": "B215"},
    {"year": 1943, "text": "《存在与虚无》出版（Britannica：Being and Nothingness 1943）。", "src": "B215"},
    {"year": 1964, "text": "获诺贝尔奖并拒绝（Britannica：In 1964 Jean-Paul Sartre was awarded the Nobel Prize……famously declined）。", "src": "B215"}
  ],
  "major_works": [
    {"work_id": "exin", "note": "日记体长篇（Britannica：1938）"},
    {"title": "存在与虚无、存在主义是一种人道主义", "note": "哲学（Britannica 语境）"},
    {"title": "苍蝇、禁闭", "note": "戏剧（通说待核）"}
  ],
  "style": [
    "哲学小说化的开端：《恶心》以日记体呈现'存在'的直接体验（Britannica 语境）。",
    "'存在先于本质'（Britannica：existence precedes essence）。",
    "介入文学：作家必须介入时代（通说待核——'engagé'概念出处待核）。"
  ],
  "status": "Britannica 定位萨特为20世纪存在主义旗手；《恶心》为其哲学的小说化宣言；1964年拒诺奖成为20世纪文学事件的象征（Britannica）。",
  "sources": ["B215"], "dates_source": "B215",
  "pending": ["《恶心》最初书名《梅洛 doorway》?（Melancholia说）待核。", "'他人即地狱'出自《禁闭》原文核对。", "萨特拒诺奖公开信原文（Le Figaro 1964）待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)
print(len(authors), "author pages created")
