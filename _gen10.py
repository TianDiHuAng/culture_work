# -*- coding: utf-8 -*-
"""创建10个缺失的作品页（供作者页 major_works 引用）"""
import json, pathlib

works = {
"baijuyishixuan": {
  "id":"baijuyishixuan","title":"白居易诗选","original_title":"白居易诗选（通行选集）","region":"中国","era":"古代","era_detail":"唐",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（文言诗体）","author_id":"baijuyi","author_name":"白居易",
  "year_display":"诗作于800—846年间；通行选本百余首","year_sort":816,
  "background":["Britannica：白居易为唐代最丰产诗人、以刻意浅白的语言批判腐败同情贫者（deliberately simple language——Britannica），精神承杜甫。"],
  "outline":["叙事诗双璧：《长恨歌》——『天长地久有时尽，此恨绵绵无绝期』（原文，公有领域）；《琵琶行》——『同是天涯沦落人，相逢何必曾相识』（原文，公有领域）。","讽喻诗：《卖炭翁》《观刈麦》——『新乐府』系列（通说）。"],
  "characters":[{"name":"李隆基与杨玉环","identity":"帝妃","note":"《长恨歌》主人公"},{"name":"江州司马","identity":"贬官","note":"《琵琶行》叙述者"}],
  "themes":["浅白语言：传说『老妪能解』（通说待核）。","新乐府：讽喻时事（通说）。","叙事诗：《长恨歌》《琵琶行》为唐叙事诗双璧（通说）。"],
  "influence":[{"text":"Britannica：唐代最丰产诗人（The most prolific Tang poet）。","source":"B179"},
    {"text":"Britannica：非正式领袖——率领拒绝宫廷风格的诗人（informal leader of poets who rejected courtly style）。","source":"B179"}],
  "reading":{"difficulties":["长恨歌的叙事结构。","新乐府的历史背景。"],
    "editions":["《白居易诗选》（人民文学出版社，通说待核）。","朱金城《白居易集笺校》（上海古籍，通说待核）。"],
    "order":"先读《长恨歌》《琵琶行》→ 新乐府组 → 编年通读。"},
  "pending":["《长恨歌》806年写作细节待核。","朱金城笺校出版信息待核。","『老妪能解』典故出处待核。"],
  "sources":["B179"],"year_source":"B179","author_source":"B179","related_works":["tangshi300","dufushixuan","honglou"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"白居易诗歌结构图",
    "cards":[{"title":"长恨歌","text":"帝妃之恋","color":"main"},{"title":"琵琶行","text":"浔阳江头","color":"main"},{"title":"新乐府","text":"讽喻时事","color":"family"},{"title":"闲适诗","text":"晚年香山居士","color":"gold"}]}
},
"caocaoshixuan": {
  "id":"caocaoshixuan","title":"曹操诗选","original_title":"曹操诗选（通行选集）","region":"中国","era":"古代","era_detail":"东汉",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（乐府）","author_id":"caocao","author_name":"曹操",
  "year_display":"诗作于约196—220年间","year_sort":200,
  "background":["曹操为建安文学领袖——『三曹』之一（通说）。Britannica 记其政治军事身份——skilled general and pragmatic politician（善战的将领与务实的政治家——Britannica）。"],
  "outline":["《短歌行》：『对酒当歌，人生几何……周公吐哺，天下归心』（原文，公有领域）。","《观沧海》：『东临碣石，以观沧海』（原文，公有领域）。","《蒿里行》：『白骨露于野，千里无鸡鸣』（原文，公有领域）。"],
  "characters":[{"name":"曹操","identity":"政治家·诗人","note":"建安风骨代表"}],
  "themes":["慷慨悲凉：统一天下的雄心与人生短暂的感伤（通说）。","乐府旧题写时事（通说）。"],
  "influence":[{"text":"Britannica（Cao Cao 条）：现代史家视其为善战的将领与务实的政治家（Modern historians see him as a skilled general）。","source":"B171"},
    {"text":"建安风骨为后世诗歌标准（通说待核）。","source":"B171"}],
  "reading":{"difficulties":["乐府旧题与史实关系。","三曹与建安七子。"],
    "editions":["《曹操集》（中华书局，通说待核）。","余冠英《汉魏六朝诗选》（通说待核）。"],
    "order":"先读《短歌行》《观沧海》→《蒿里行》《龟虽寿》→ 通读选本。"},
  "pending":["曹操诗存世数待核。","三曹与建安七子名单待核。","《短歌行》原文逐字核对。"],
  "sources":["B171"],"year_source":"B171","author_source":"B171","related_works":["sanguo","tangshi300","honglou"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"曹操诗结构图",
    "cards":[{"title":"短歌行","text":"对酒当歌·周公吐哺","color":"main"},{"title":"观沧海","text":"东临碣石·星汉灿烂","color":"family"},{"title":"蒿里行","text":"白骨露于野","color":"antagonist"},{"title":"龟虽寿","text":"老骥伏枥·志在千里","color":"gold"}]}
},
"sangganhe": {
  "id":"sangganhe","title":"太阳照在桑干河上","original_title":"太阳照在桑干河上（长篇小说）","region":"中国","era":"现当代","era_detail":"现代",
  "genre":"长篇小说","genre_group":"小说","language":"汉语（白话）","author_id":"dingling","author_name":"丁玲",
  "year_display":"1948年出版（Britannica）；1951年获斯大林文学奖（Britannica）","year_sort":1948,
  "background":["Britannica（Ding Ling 条）：The Sun Shines over the Sanggan River（1948）为 first Chinese novel to win the Soviet Stalin Prize (1951)（首部获斯大林奖的中国小说——Britannica）。","题材：1946年华北解放区暖水屯土地改革（通说）。"],
  "outline":["暖水屯土改：工作组进村——斗地主、分田地——农民的犹豫与斗争（通说）。","人物：张裕民、程仁（农会主任）、黑妮、钱文贵（地主）——阶级分析的人物群（通说）。"],
  "characters":[{"name":"张裕民","identity":"村支书","note":"土改领导者"},{"name":"程仁","identity":"农会主任","note":"与地主侄女的情感纠葛（通说）"},{"name":"黑妮","identity":"地主侄女","note":"被阶级身份困扰的少女"},{"name":"钱文贵","identity":"地主","note":"被斗争对象"}],
  "themes":["土改的复杂性：翻身的理想与现实（通说）。","阶级与情感的冲突（通说）。","艺术特点：心理描写超出当时一般水平（通说待核）。"],
  "influence":[{"text":"Britannica：first Chinese novel to win the Soviet Stalin Prize (1951)（首部获斯大林奖的中国小说——Britannica）。","source":"B170"},
    {"text":"Britannica：作者1957年被开除党籍（censured and expelled from the party as a rightist in 1957）——作者命运与作品的复杂性。","source":"B170"}],
  "reading":{"difficulties":["土改运动的历史背景——需要注释。","人物众多——先画人物表。"],
    "editions":["《太阳照在桑干河上》（人民文学出版社，通说待核）。"],
    "order":"通读 → 精读斗争大会一章 → 对照周立波《暴风骤雨》（通说待核）。"},
  "pending":["1948年出版细节待核。","1951年斯大林奖细节待核。","人物原名与原型考订待核。"],
  "sources":["B170"],"year_source":"B170","author_source":"B170","related_works":["nahan","pingfan","huozhe"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《太阳照在桑干河上》土改结构图",
    "cards":[{"title":"工作组进村","text":"土改开始","color":"family"},{"title":"斗地主","text":"钱文贵被斗","color":"antagonist"},{"title":"翻身","text":"分田地","color":"main"},{"title":"黑妮","text":"阶级与情感的冲突","color":"gold"}]}
},
"hanyuwenxuan": {
  "id":"hanyuwenxuan","title":"韩愈文选","original_title":"韩愈文选（通行文选）","region":"中国","era":"古代","era_detail":"唐",
  "genre":"散文选集","genre_group":"散文","language":"汉语（文言）","author_id":"hanyu","author_name":"韩愈",
  "year_display":"文作于约790—824年间；通行文选数十篇","year_sort":800,
  "background":["Britannica：韩愈为唐代散文大家（a Tang dynasty master of Chinese prose），被推为唐宋八大家之首（regarded as the first of the Eight Masters——Britannica）；倡导古文（guwen）对抗骈文（pianwen）——championed guwen, a simple prose style, over the ornate pianwen style（Britannica）。"],
  "outline":["《师说》：『师者，所以传道受业解惑也』（原文，公有领域）——论从师学习；《进学解》：『业精于勤，荒于嬉』（原文，公有领域）。","《论佛骨表》——谏迎佛骨被贬潮州（原文意，公有领域；史实通说）。","《祭十二郎文》——悼侄文，祭文中的千古绝调（通说）。"],
  "characters":[{"name":"韩愈","identity":"士大夫·道统捍卫者","note":"以文载道的实践者"}],
  "themes":["古文运动：以朴素散文对抗骈文（Britannica）。","道统论：《原道》捍卫儒道（Britannica）。","艺术特点：雄健奇崛（Britannica：unconventional prose style）。"],
  "influence":[{"text":"Britannica：被推为唐宋八大家之首（regarded as the first of the Eight Masters of the Tang and Song）。","source":"B172"},
    {"text":"Britannica：其政论反对苛政与国教，影响后世改革者（influencing later revolutions）。","source":"B172"}],
  "reading":{"difficulties":["唐代文体（古文vs骈文）的区别——需要注释。","儒家道统概念——需要注释。"],
    "editions":["《韩昌黎文集校注》（上海古籍出版社，通说待核）。","《韩愈文选》（人民文学出版社，通说待核）。"],
    "order":"先读《师说》《进学解》→《论佛骨表》《祭十二郎文》→《原道》→ 通读。"},
  "pending":["《师说》原文逐字核对。","《祭十二郎文》原文核对。","韩愈文选篇目因版本而异待核。"],
  "sources":["B172"],"year_source":"B172","author_source":"B172","related_works":["lunyu","shiji","tangshi300"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"韩愈散文结构图",
    "cards":[{"title":"师说","text":"传道受业解惑","color":"main"},{"title":"进学解","text":"业精于勤","color":"family"},{"title":"论佛骨表","text":"谏迎佛骨·贬潮州","color":"antagonist"},{"title":"祭十二郎文","text":"悼侄文·千古绝调","color":"gold"}]}
},
"ouyangxiuwenxuan": {
  "id":"ouyangxiuwenxuan","title":"欧阳修文选","original_title":"欧阳修文选（通行文选）","region":"中国","era":"古代","era_detail":"宋",
  "genre":"散文选集","genre_group":"散文","language":"汉语（文言）","author_id":"ouyangxiu","author_name":"欧阳修",
  "year_display":"文作于约1040—1072年间","year_sort":1050,
  "background":["Britannica：欧阳修为宋代诗人、史家与政治家（poet, historian, and statesman）；倡导平易的古文（plain ancient-style guwen prose），提拔苏轼、苏辙、曾巩（mentored Su Dongpo, Su Zhe, and Zeng Gong——Britannica）；唐宋八大家之一（ranks among the Eight Great Masters——Britannica）。"],
  "outline":["《醉翁亭记》：『醉翁之意不在酒，在乎山水之间也』（原文，公有领域）。","《秋声赋》：『欧阳子方夜读书，闻有声自西南来者』（原文，公有领域）。","《泷冈阡表》：祭父文（通说）。"],
  "characters":[{"name":"醉翁","identity":"太守·作者自号","note":"醉翁之意不在酒（原文，公有领域）"}],
  "themes":["古文的平易：Britannica——plain ancient-style guwen prose（朴素古文——Britannica）。","六一风神：欧阳修散文的独特风致（通说待核）。"],
  "influence":[{"text":"Britannica：唐宋八大家之一（ranks among the Eight Great Masters of Tang and Song）。","source":"B173"},
    {"text":"Britannica：提拔苏轼、苏辙、曾巩（mentored Su Dongpo, Su Zhe, and Zeng Gong）。","source":"B173"}],
  "reading":{"difficulties":["宋代散文文体——较唐文更平易。","《醉翁亭记》的21个也字句——修辞分析。"],
    "editions":["《欧阳修全集》（中华书局，通说待核）。","《欧阳修文选》（人民文学出版社，通说待核）。"],
    "order":"先读《醉翁亭记》《秋声赋》→《朋党论》《泷冈阡表》→ 通读。"},
  "pending":["《醉翁亭记》原文逐字核对。","欧阳修文选篇目因版本而异待核。","宋六家与唐宋八大家关系待核。"],
  "sources":["B173"],"year_source":"B173","author_source":"B173","related_works":["hanyuwenxuan","sushixuan","lunyu"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"欧阳修散文结构图",
    "cards":[{"title":"醉翁亭记","text":"醉翁之意不在酒","color":"main"},{"title":"秋声赋","text":"悲秋之声","color":"gold"},{"title":"朋党论","text":"论君子朋与小人群","color":"family"},{"title":"泷冈阡表","text":"祭父文","color":"plain"}]}
},
"wangweishixuan": {
  "id":"wangweishixuan","title":"王维诗选","original_title":"王维诗选（通行选集）","region":"中国","era":"古代","era_detail":"唐",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（文言诗体）","author_id":"wangwei","author_name":"王维",
  "year_display":"诗作于约720—761年间；通行选本百余首","year_sort":750,
  "background":["Britannica：王维为唐代著名诗人、画家与音乐家（a famed Tang dynasty poet, painter, and musician）；与李白杜甫并列（ranked alongside Li Bai and Du Fu——Britannica）；17世纪董其昌尊其为南宗文人画之祖（Dong Qichang named him founder of the Southern school of painter-poets——Britannica）。"],
  "outline":["《鹿柴》：『空山不见人，但闻人语响』（原文，公有领域）。","《送元二使安西》：『劝君更尽一杯酒，西出阳关无故人』（原文，公有领域）。","《山居秋暝》：『空山新雨后，天气晚来秋』（原文，公有领域）。"],
  "characters":[{"name":"辋川隐者","identity":"诗人自况","note":"晚年唯好静（《酬张少府》原文，公有领域）"}],
  "themes":["诗中有画：苏轼评语——味摩诘之诗，诗中有画（通说待核）。","禅意：辋川隐居习佛（Britannica：withdrew to a villa on the Wang River to study Buddhism——Britannica）。"],
  "influence":[{"text":"Britannica：与李白杜甫并列为唐代最伟大诗人（ranked alongside Li Bai and Du Fu）。","source":"B177"},
    {"text":"Britannica：董其昌尊其为南宗文人画之祖（founder of the Southern school of painter-poets）。","source":"B177"}],
  "reading":{"difficulties":["禅诗的空与静——需要佛教背景。","山水意象的哲学化——不要当风景诗读。"],
    "editions":["《王维诗选》（人民文学出版社，通说待核）。","《王右丞集笺注》（中华书局，通说待核）。"],
    "order":"先读《鹿柴》《鸟鸣涧》《山居秋暝》→《送元二使安西》→ 辋川集组诗 → 编年通读。"},
  "pending":["《鹿柴》原文逐字核对。","苏轼诗中有画评语出处待核。","辋川集二十首（与裴迪唱和——通说）待核。"],
  "sources":["B177"],"year_source":"B177","author_source":"B177","related_works":["tangshi300","libaishixuan","dufushixuan"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"王维诗歌结构图",
    "cards":[{"title":"鹿柴","text":"空山不见人","color":"main"},{"title":"山居秋暝","text":"明月松间照","color":"family"},{"title":"送元二使安西","text":"西出阳关无故人","color":"gold"},{"title":"水墨画","text":"南宗画祖（Britannica）","color":"plain"}]}
},
"taoyuanming": {
  "id":"taoyuanming","title":"陶渊明诗选","original_title":"陶渊明集（通行选集）","region":"中国","era":"古代","era_detail":"魏晋",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（文言）","author_id":"taoqian","author_name":"陶渊明（陶潜）",
  "year_display":"诗作于约400—427年间；通行选本百余首","year_sort":410,
  "background":["Britannica：陶潜为田园诗第一位伟大诗人（the first great poet of tianyuan pastoral poetry——Britannica）；朴素不雕饰的风格生前不受重视、唐代始获推崇（plain, unadorned style was underappreciated in his lifetime but gained recognition during the Tang dynasty——Britannica）。"],
  "outline":["《归园田居》：『少无适俗韵，性本爱丘山』（原文，公有领域）。","《饮酒》：『采菊东篱下，悠然见南山』（原文，公有领域）。","《桃花源记》：『不知有汉，无论魏晋』（原文，公有领域）——乌托邦。","《归去来兮辞》：『悟已往之不谏，知来者之可追』（原文，公有领域）——辞官宣言。"],
  "characters":[{"name":"五柳先生","identity":"隐者自况","note":"采菊东篱下的隐者形象"}],
  "themes":["平淡美学：Britannica——plain, unadorned style（朴素不雕饰——Britannica）。","田园：Britannica——田园诗第一位伟大诗人。","思想：以道为主、融合儒佛（Britannica：blended Daoism with selected Confucian and Buddhist elements——Britannica）。"],
  "influence":[{"text":"Britannica：田园诗第一位伟大诗人（the first great poet of tianyuan pastoral poetry）。","source":"B178"},
    {"text":"Britannica：生前不受重视、唐代始获推崇（gained recognition during the Tang dynasty）。","source":"B178"}],
  "reading":{"difficulties":["平淡中见深邃——不可一读即过。","《桃花源记》的乌托邦解读。"],
    "editions":["《陶渊明集》（中华书局，通说待核）。","《陶渊明诗选》（人民文学出版社，通说待核）。"],
    "order":"先读《归园田居》其一与《饮酒》其五 →《桃花源记》《归去来兮辞》→ 通读。"},
  "pending":["生年365与卒年427 Britannica 确认。","《桃花源记》原文逐字核对。","萧统《陶渊明集序》评语待核。"],
  "sources":["B178"],"year_source":"B178","author_source":"B178","related_works":["chuci","wangweishixuan","tangshi300"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"陶渊明作品结构图",
    "cards":[{"title":"归园田居","text":"少无适俗韵","color":"main"},{"title":"饮酒","text":"采菊东篱下","color":"gold"},{"title":"桃花源记","text":"不知有汉","color":"family"},{"title":"归去来兮辞","text":"知来者之可追","color":"plain"}]}
},
"sushixuan": {
  "id":"sushixuan","title":"苏轼诗词文选","original_title":"苏轼诗词文选（通行选集）","region":"中国","era":"古代","era_detail":"宋",
  "genre":"诗选集","genre_group":"诗歌","language":"汉语（文言）","author_id":"sushi","author_name":"苏轼",
  "year_display":"诗词文作于约1057—1101年间","year_sort":1082,
  "background":["Britannica：苏轼为宋代诗人、散文家、书法家与官员（a Song Dynasty poet, essayist, calligrapher, and official）；精通诗、词、赋、文（mastered shi, ci, fu, and essays——Britannica）；豪放派开创者（founder of the haofang school——Britannica）；以乐观著称（Known for his optimism——Britannica）。"],
  "outline":["《水调歌头·明月几时有》：『人有悲欢离合，月有阴晴圆缺，此事古难全』（原文，公有领域）。","《念奴娇·赤壁怀古》：『大江东去，浪淘尽，千古风流人物』（原文，公有领域）。","《前赤壁赋》：『清风徐来，水波不兴』（原文，公有领域）。","《记承天寺夜游》：『庭下如积水空明』（原文，公有领域）。"],
  "characters":[{"name":"东坡居士","identity":"诗人·官员·被贬者","note":"一蓑烟雨任平生（《定风波》原文，公有领域）"}],
  "themes":["豪放：Britannica——haofang school 开创者。","乐观：Britannica——Known for his optimism——多次被贬而不改。","多文体：Britannica——mastered shi, ci, fu, and essays。"],
  "influence":[{"text":"Britannica：豪放派开创者（the founder of the haofang school of writing）。","source":"B113"},
    {"text":"Britannica：精通诗、词、赋、文（mastered shi, ci, fu, and essays）。","source":"B113"}],
  "reading":{"difficulties":["诗、词、赋、散文四种文体的切换。","宋代政治（王安石变法、乌台诗案）背景。"],
    "editions":["《苏轼选集》（人民文学出版社，通说待核）。","《苏轼文集》（中华书局，通说待核）。"],
    "order":"先读《水调歌头》《念奴娇·赤壁怀古》→《前赤壁赋》《记承天寺夜游》→ 通读。"},
  "pending":["《水调歌头》原文逐字核对。","苏轼选本篇目因版本而异待核。","唐宋八大家中的宋六家名单待核。"],
  "sources":["B113","B173"],"year_source":"B113","author_source":"B113","related_works":["tangshi300","ouyangxiuwenxuan","waerdenghu"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"苏轼作品结构图",
    "cards":[{"title":"水调歌头","text":"明月几时有","color":"main"},{"title":"念奴娇·赤壁怀古","text":"大江东去","color":"main"},{"title":"前赤壁赋","text":"清风徐来","color":"family"},{"title":"记承天寺夜游","text":"积水空明","color":"gold"}]}
},
"liqingzhaocixuan": {
  "id":"liqingzhaocixuan","title":"李清照词选","original_title":"李清照词选（通行选集）","region":"中国","era":"古代","era_detail":"宋",
  "genre":"词选集","genre_group":"诗歌","language":"汉语（文言词体）","author_id":"liqingzhao","author_name":"李清照",
  "year_display":"词作于约1100—1155年间；通行选本数十首","year_sort":1130,
  "background":["Britannica：李清照为中国最伟大的女诗人（China's greatest woman poet——Britannica）；字句惊人、以个人经验入词（known for striking word choices and drawing on personal experience——Britannica）；前期活泼、南渡后凄怆（Earlier pieces show carefree vitality, while post-exile work carries a sombre, grieving quality——Britannica）。"],
  "outline":["前期：《如梦令》——『知否，知否？应是绿肥红瘦』（原文，公有领域）；《一剪梅》——『此情无计可消除』（原文，公有领域）。","后期：《声声慢》——『寻寻觅觅，冷冷清清，凄凄惨惨戚戚』（原文，公有领域）；《武陵春》——『物是人非事事休，欲语泪先流』（原文，公有领域）。"],
  "characters":[{"name":"易安居士","identity":"词人·南渡者","note":"前期活泼后期凄怆（Britannica）"}],
  "themes":["婉约：以女性视角写情感——词别是一家（《词论》观点，通说待核）。","国破家亡的晚期风格：南渡后的凄怆（Britannica）。","艺术特点：口语入词、叠字运用、情感真挚。"],
  "influence":[{"text":"Britannica：中国最伟大的女诗人（China's greatest woman poet）。","source":"B114"},
    {"text":"Britannica：其《词论》为最早的词学研究之一（one of the earliest scholarly studies of the form）。","source":"B114"}],
  "reading":{"difficulties":["词的音乐性——需要朗读。","前期后期风格差异——南渡分界。"],
    "editions":["王仲闻《李清照集校注》（人民文学出版社，通说待核）。","《李清照词选》（人民文学出版社，通说待核）。"],
    "order":"先读《如梦令》《一剪梅》→《声声慢》《武陵春》→ 对照《词论》。"},
  "pending":["卒年1155后的精确年份待核。","《声声慢》原文逐字核对。","王仲闻校注本信息待核。"],
  "sources":["B114","B175"],"year_source":"B114","author_source":"B114","related_works":["songci300","xinqijicixuan","hulanhe"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"李清照词前后期结构图",
    "cards":[{"title":"前期活泼","text":"如梦令·点绛唇","color":"family"},{"title":"后期凄怆","text":"声声慢·武陵春","color":"antagonist"},{"title":"南渡分界","text":"1129年夫亡（Britannica）","color":"gold"}]}
},
"xinqijicixuan": {
  "id":"xinqijicixuan","title":"辛弃疾词选","original_title":"辛弃疾词选（通行选集）","region":"中国","era":"古代","era_detail":"宋",
  "genre":"词选集","genre_group":"诗歌","language":"汉语（文言词体）","author_id":"xinqiji","author_name":"辛弃疾",
  "year_display":"词作于约1162—1207年间；存词623首（Britannica）","year_sort":1180,
  "background":["Britannica：辛弃疾存词623首，许多批评家赞为南宋最佳（praised by many critics as the finest of the Southern Song），以拓展词的情感深度著称（notable for expanding the form's emotional depth——Britannica）。"],
  "outline":["《永遇乐·京口北固亭怀古》：『千古江山，英雄无觅孙仲谋处』（原文，公有领域）。","《破阵子》：『醉里挑灯看剑，梦回吹角连营』（原文，公有领域）。","《青玉案·元夕》：『众里寻他千百度，蓦然回首，那人却在灯火阑珊处』（原文，公有领域）。"],
  "characters":[{"name":"稼轩","identity":"军人·词人","note":"以气节自负（通说待核）"}],
  "themes":["豪放继承苏轼：以气节自负（通说待核）。","用典：大量用典——辛词的典型争议（通说待核）。","Britannica——拓展词的情感深度（expanding the form's emotional depth）。"],
  "influence":[{"text":"Britannica：623首——许多批评家赞为南宋最佳（the finest of the Southern Song）。","source":"B115"},
    {"text":"Britannica：以拓展词的情感深度著称（expanding the form's emotional depth）。","source":"B115"}],
  "reading":{"difficulties":["大量用典——注释不可缺。","豪放与婉约并存。"],
    "editions":["邓广铭《稼轩词编年笺注》（上海古籍出版社，通说待核）。","《辛弃疾词选》（人民文学出版社，通说待核）。"],
    "order":"先读《永遇乐》《破阵子》《青玉案》→ 编年通读选本。"},
  "pending":["《永遇乐》原文逐字核对。","邓广铭笺注本信息待核。","623首统计口径待核。"],
  "sources":["B115","B176"],"year_source":"B115","author_source":"B115","related_works":["songci300","sushixuan","shiji"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"辛弃疾词结构图",
    "cards":[{"title":"永遇乐","text":"京口北固亭怀古","color":"main"},{"title":"破阵子","text":"醉里挑灯看剑","color":"family"},{"title":"青玉案·元夕","text":"灯火阑珊处","color":"gold"},{"title":"稼轩词623首","text":"南宋最佳（Britannica）","color":"plain"}]}
}
}

missing_rel = set()
existing_ids = set()
for p in pathlib.Path("data/works").glob("*.json"):
    try:
        existing_ids.add(json.loads(p.read_text(encoding="utf-8"))["id"])
    except Exception as e:
        print("BAD EXISTING", p.name, e)

for wid, d in works.items():
    for r in d["related_works"]:
        if r not in existing_ids and r not in works:
            missing_rel.add((wid, r))
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created", wid)

print("missing related:", sorted(missing_rel) if missing_rel else "NONE")
