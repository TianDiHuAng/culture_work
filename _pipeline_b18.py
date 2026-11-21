# -*- coding: utf-8 -*-
"""流水线批18：复用已核来源直写 10 部"""
import json, pathlib

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

def W(id_, title, orig, region, era, era_detail, genre, gg, lang, aid, aname, yd, ys, bg, outline, chars, themes, inf, read, pend, srcs, ysrc, asrc, rel, svg):
    return {"id":id_,"title":title,"original_title":orig,"region":region,"era":era,"era_detail":era_detail,
"genre":genre,"genre_group":gg,"language":lang,"author_id":aid,"author_name":aname,"year_display":yd,"year_sort":ys,
"background":bg,"outline":outline,"characters":chars,"themes":themes,"influence":inf,"reading":read,"pending":pend,
"sources":srcs,"year_source":ysrc,"author_source":asrc,"related_works":rel,"svg":svg}

works = [
W("manchangdeheian","进入黑夜的漫长旅程","Long Day's Journey into Night","美国","现当代","20世纪","自传性戏剧","戏剧","英语","ONeill","尤金·奥尼尔","身后1956年上演（作者页B272口径：Long Day's Journey into Night produced posthumously 1956——masterpiece）",1956,
["作者页（B272）：'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'——身后上演的杰作；'drew heavily on family tragedy and Greek tragedy'。","四项普利策戏剧奖之一（B272：four Pulitzer prizes in drama——含本作）。","题材（通说待核）：蒂龙一家的一天——吗啡、酗酒与病（自传性）。"],
["蒂龙一家的一天：吗啡、酗酒与病——'过去'如何纠缠当下（通说待核）。"],
[{"name":"詹姆斯·蒂龙","identity":"父亲","note":"吝啬演员（通说待核）"},{"name":"玛丽","identity":"母亲","note":"吗啡成瘾（通说待核）"},{"name":"埃德蒙","identity":"小儿子","note":"作者化身（通说待核）"}],
["家庭的毒瘾与宽恕（通说待核）。","'希腊悲剧'的家庭版（B272 语境）。","自传性（通说待核——奥尼尔家庭）。"],
[{"text":"Britannica：'His masterpiece, Long Day's Journey into Night (produced posthumously 1956)'（B272）。","source":"B272"},{"text":"Britannica：四项普利策戏剧奖之一（B272）。","source":"B272"}],
{"difficulties":["自传对应（奥尼尔家族）。","长独白的节奏。"],"editions":["《进入黑夜的漫长旅程》（人民文学出版社/湖南文艺出版社版本，通说待核）。","英文原版（Yale）。"],"order":"奥尼尔收官之作。"},
["身后1956年（Yale University Press出版/百老汇演出说）核对。","蒂龙一家对应（奥尼尔父兄）待核。","四项普利策年份逐项核对。"],
["B272"],"B272","B272",["leiyu","richu","yingtaoyuan"],
G2("《漫长旅程》家庭结构图",[{"title":"父亲","text":"吝啬与悔恨","color":"antagonist"},{"title":"母亲","text":"吗啡的回归","color":"main"},{"title":"埃德蒙","text":"作者的化身","color":"gold"},{"title":"雾","text":"过去的纠缠","color":"family"}])),

W("ouhengliduanpianxuan","欧·亨利短篇小说选","The Four Million 等","美国","近代","20世纪初","短篇小说集","小说","英语","ohenry","欧·亨利（O. Henry）","1906年（作者页B273口径：The Four Million (1906)——含'麦琪的礼物'）",1906,
["作者页（B273）：'From December 1903 to January 1906 he produced a story a week for the New York Sunday World magazine'；'Both The Four Million (1906) and The Trimmed Lamp (1907) explored the lives of the multitude of New York'——'the former contained the widely popular story The Gift of the Magi'。","风格（B273）：'His stories often had surprise endings, a device that became identified with his name'；'expressed the effect of coincidence on character through humour, grim or ironic'。"],
["名篇谱系（B273+通说）：《麦琪的礼物》《最后一片叶子》《警察与赞美诗》等。"],
[{"name":"小人物们","identity":"纽约多众","note":"'the multitude of New York'（B273）"}],
["'欧·亨利式结尾'（B273）。","巧合对性格的作用（B273：effect of coincidence on character）。","小人物的温暖（B273 语境）。"],
[{"text":"Britannica：'surprise endings, a device that became identified with his name'（B273）。","source":"B273"},{"text":"Britannica：每周一篇的生产力（B273）。","source":"B273"}],
{"difficulties":["'欧·亨利式结尾'的预期管理。","1900年代纽约俚语。"],"editions":["《欧·亨利短篇小说选》（人民文学出版社王永年译本，通说待核）。","英文原版（公有领域）。"],"order":"先《麦琪的礼物》→《最后一片叶子》。"},
["《麦琪的礼物》首发日期核对。","《最后一片叶子》篇名（The Last Leaf）核对。","王永年译本信息待核。"],
["B273"],"B273","B273",["mauposangxuan","kafuxuan","qikefuxuan"],
G2("欧·亨利结尾图",[{"title":"麦琪的礼物","text":"互赠的牺牲","color":"main"},{"title":"最后一片叶子","text":"常春藤的奇迹（通说）","color":"gold"},{"title":"巧合","text":" grim 或 ironic（B273）","color":"antagonist"},{"title":"结尾","text":"欧·亨利式反转","color":"family"}])),

W("yuesefuandelusi","约瑟夫·安德鲁斯","Joseph Andrews","英国","近代","18世纪","长篇小说","小说","英语","fielding","亨利·菲尔丁","1742年（作者页B274口径：Joseph Andrews was published anonymously in 1742）",1742,
["Britannica（B274）：'Fielding's Joseph Andrews was published anonymously in 1742'；'He was certainly inaugurating a new genre in fiction'；前言自述'a comic Epic-Poem in Prose'（B274）。","缘起（B274 语境）：戏仿理查森《帕梅拉》——帕梅拉之弟约瑟夫的贞洁冒险（通说待核）。"],
["约瑟夫与帕森·亚当斯的公路冒险：正直者的滑稽考验（通说待核）。"],
[{"name":"约瑟夫","identity":"男仆","note":"（通说待核）"},{"name":"帕森·亚当斯","identity":"牧师","note":"唐吉诃德式牧师（通说待核）"}],
["'滑稽史诗'的实践（B274：comic Epic-Poem in Prose）。","对感伤主义的戏仿（B274 语境：Shamela 的姊妹）。","正直的公路喜剧（通说待核）。"],
[{"text":"Britannica：'He was certainly inaugurating a new genre in fiction'（B274）。","source":"B274"},{"text":"作者页：菲尔丁'英国小说之父'（B274 作者级定位）。","source":"B274"}],
{"difficulties":["与《帕梅拉》的互文。","18世纪公路叙事。"],"editions":["《约瑟夫·安德鲁斯》（人民文学出版社，通说待核）。","英文原版（公有领域）。"],"order":"先《汤姆·琼斯》或本作（互为前奏）。"},
["1742年2月出版（Andrew Millar说）核对。","约瑟夫/亚当斯人名核对。","《莎米拉》戏仿（1741——B274 已载）展开核对。"],
["B274"],"B274","B274",["tangmuqiongsi","lubinxun","moerflandes"],
G2("《约瑟夫·安德鲁斯》公路喜剧图",[{"title":"贞洁","text":"男性的'帕梅拉'","color":"main"},{"title":"亚当斯","text":"堂吉诃德式牧师","color":"gold"},{"title":"公路","text":"滑稽的冒险","color":"family"},{"title":"戏仿","text":"对感伤主义的反讽","color":"antagonist"}])),

W("weibizaozhe","伪币制造者","Les Faux-Monnayeurs（The Counterfeiters）","法国","现当代","20世纪","长篇小说","小说","法语","gide","安德烈·纪德","1926年（作者页B275口径：Les Faux-Monnayeurs (1926; The Counterfeiters)——'his only novel'）",1926,
["作者页（B275）：纪德 major_works 载'伪币制造者'（B275 作者页定位，详见 yinduzhixing 条核对）。","Britannica（B275）：'Gide called his next work, Les Faux-Monnayeurs (1926; The Counterfeiters), his only novel'；'the most complex and intricately constructed of his works'；'told through discontinuous scenes'。","作者（B275）：1947年诺奖。"],
["中学生贝尔纳与'伪币'：假币与假情的巴黎（通说待核）。","'小说中的小说'：爱德华的日记（通说待核）。"],
[{"name":"爱德华","identity":"作家","note":"日记体嵌套（通说待核）"},{"name":"贝尔纳","identity":"中学生","note":"（通说待核）"}],
["'伪币'：假与真的哲学（通说待核）。","不连续场景（B275）。","'唯一小说'的自认（B275）。"],
[{"text":"Britannica：'the most complex and intricately constructed of his works'（B275）。","source":"B275"},{"text":"Britannica：1947年诺奖（B275 作者级）。","source":"B275"}],
{"difficulties":["嵌套结构。","多人物。"],"editions":["《伪币制造者》（人民文学出版社/上海译文版本，通说待核）。","法文原版（Gallimard）。"],"order":"先《背德者》《窄门》后本作。"},
["1926年出版（Gallimard/NRF说）核对。","爱德华/贝尔纳人名核对。","'唯一小说'的自称与评论界立场待核。"],
["B275"],"B275","B275",["xianzhi","duoluo","qingzhong"],
G2("《伪币制造者》嵌套结构图",[{"title":"伪币","text":"假与真","color":"main"},{"title":"爱德华日记","text":"小说中的小说（通说）","color":"gold"},{"title":"不连续场景","text":"B275 方法","color":"family"},{"title":"少年们","text":"堕落的诱惑","color":"antagonist"}])),

W("yuehankelisituofu","约翰·克利斯朵夫","Jean-Christophe","法国","现当代","20世纪","大河小说（十卷）","小说","法语","rolland","罗曼·罗兰","1904—1912年十卷（作者页B276口径：Jean-Christophe 10卷 (1904–12)——'a prime example of the roman fleuve'）",1908,
["Britannica（B276）：'Rolland's masterpiece, Jean-Christophe... is a prime example of the roman fleuve (novel cycle) in France'；10卷刊于 Les Cahiers de la Quinzaine（B276）。","题材（通说待核）：德国血统的音乐家约翰·克利斯朵夫·克拉夫特的一生——以贝多芬为原型（B276：Vie de Beethoven 语境）。"],
["音乐家的一生：德国—巴黎—瑞士—意大利（通说待核）。","'音乐'与'生活'的同构（通说待核）。"],
[{"name":"约翰·克利斯朵夫·克拉夫特","identity":"音乐家","note":"以贝多芬为原型（通说待核）"},{"name":"奥里维","identity":"法国友人","note":"（通说待核）"}],
["'大河小说'（B276：roman fleuve）。","英雄与音乐（B276：贝多芬传记语境）。","法德文化的桥（通说待核）。"],
[{"text":"Britannica：'masterpiece'；'prime example of the roman fleuve'（B276）。","source":"B276"},{"text":"Britannica：1915年诺奖（B276 作者级）。","source":"B276"}],
{"difficulties":["十卷体量。","音乐结构章节。"],"editions":["《约翰·克利斯朵夫》（人民文学出版社傅雷译本四册，通说待核）。","法文原版（公有领域）。"],"order":"傅雷译本为中文世界经典。"},
["十卷分卷与四册（傅雷）对应核对。","克拉夫特人名核对。","傅雷译本（1930—40年代）信息待核。"],
["B276"],"B276","B276",["beican","jian","renshijian"],
G2("《约翰·克利斯朵夫》大河结构图",[{"title":"诞生","text":"莱茵河畔","color":"family"},{"title":"音乐","text":"一生的乐章","color":"main"},{"title":"巴黎","text":"文化的战场","color":"antagonist"},{"title":"大河","text":"roman fleuve（B276）","color":"gold"}])),

W("jim","吉姆","Kim","英国","近代","19世纪末","长篇小说","小说","英语","kipling","鲁德亚德·吉卜林","1901年（作者页B277口径：Kim (1901), about an Irish orphan in India, is a classic）",1901,
["作者页（B277）：吉卜林 major_works 载'吉姆'（B277 作者页定位，详见 conglinzhihue 条核对）。","Britannica（B277）：'Kim (1901), about an Irish orphan in India, is a classic'；吉卜林1907年诺奖——'the first English writer to receive the Nobel Prize'。","题材（通说待核）：孤儿吉姆与西藏喇嘛的'大游戏'（Great Game）间谍之旅。"],
["吉姆与喇嘛的寻找之河：从拉合尔到喜马拉雅（通说待核）。"],
[{"name":"吉姆","identity":"孤儿","note":"（通说待核）"},{"name":"喇嘛","identity":"西藏僧人","note":"寻找圣河（通说待核）"}],
["'大游戏'：英俄在中亚的谍战（通说待核）。","印度全景（通说）。","寻找与身份（通说待核）。"],
[{"text":"Britannica：'is a classic'（B277）。","source":"B277"},{"text":"Britannica：1907诺奖——首位英国获奖者（B277）。","source":"B277"}],
{"difficulties":["'大游戏'史。","印度地名与宗教。"],"editions":["《吉姆》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],"order":"吉卜林代表作。"},
["1901年出版（Macmillan说）核对。","吉姆/喇嘛人名核对。","'大游戏'（Great Game）术语核对。"],
["B277"],"B277","B277",["hakebei","shijiemori","yidudewunv"],
G2("《吉姆》大游戏结构图",[{"title":"拉合尔","text":"出发的炮台","color":"family"},{"title":"寻找圣河","text":"喇嘛的祈愿","color":"main"},{"title":"大游戏","text":"中亚的谍战（通说）","color":"antagonist"},{"title":"经典","text":"B277 定位","color":"gold"}])),

W("fanxingchunshui","繁星·春水","繁星/春水（小诗集）","中国","现当代","现代","小诗集","诗歌","汉语（白话）","bingxin","冰心（谢婉莹）","1923年出版（通说待核；作者页B279口径：Britannica 页未载——仅记其受泰戈尔影响的抒情之作一举成名）",1923,
["作者页（B279）：冰心'lyrical pieces about childhood and nature, influenced by the Indian poet Rabindranath Tagore'——受泰戈尔影响的童年与自然抒情之作使她'won her instant fame'（一举成名）并获卫斯理学院奖学金。","'冰心体'（通说待核）：小诗体——受泰戈尔《飞鸟集》影响的短诗。"],
["《繁星》：零碎的哲思小诗（通说待核）。","《春水》：延续的春水之思（通说待核）。"],
[{"name":"冰心","identity":"诗人","note":"'温柔、忧郁'（B279）"}],
["母爱与童心（通说）。","泰戈尔式小诗体（B279：influenced by Tagore）。","'哲学的'小诗（通说待核）。"],
[{"text":"Britannica：受泰戈尔影响的抒情之作使冰心一举成名（B279）。","source":"B279"},{"text":"作者页：冰心为广受欢迎的中国作家（B279 作者级定位）。","source":"B279"}],
{"difficulties":["小诗体的断片。","'冰心体'语言。"],"editions":["《繁星·春水》（人民文学出版社/商务印书馆版本，通说待核）。"],"order":"对照泰戈尔《飞鸟集》（B261 作者受其影响——互证）。"},
["《繁星》《春水》1923年出版细节核对。","篇数（繁星164/春水182说）待核。","'冰心体'术语出处待核。"],
["B279"],"B279","B279",["jitangali","nvshen","beidaoshixuan"],
G2("《繁星·春水》小诗结构图",[{"title":"繁星","text":"哲思的碎语","color":"main"},{"title":"春水","text":"流水的延续","color":"family"},{"title":"泰戈尔","text":"影响之源（B279）","color":"gold"},{"title":"母爱与童心","text":"主题（通说）","color":"plain"}])),

W("jialimeimei","嘉莉妹妹","Sister Carrie","美国","现当代","20世纪","长篇小说","小说","英语","delaise","西奥多·德莱塞","1900年出版（作者页B280口径：Sister Carrie——1899年动笔；首版'sold fewer than 500 copies'）",1900,
["Britannica（B280）：'Dreiser began writing his first novel, Sister Carrie, in 1899 at the suggestion of a newspaper colleague'；'Doubleday's qualms about the book, the story line of which involves a young kept woman whose immorality goes unpunished' led to limited advertising，'sold fewer than 500 copies'。","作者（B280）：'the outstanding American practitioner of naturalism'（美国自然主义最杰出实践者）。"],
["嘉莉进城：从打工到'kept woman'——'immorality goes unpunished'（B280 语境）。","赫斯特伍德的坠落：从经理到流浪（通说待核）。"],
[{"name":"嘉莉·米伯","identity":"打工女","note":"上升者（通说待核）"},{"name":"赫斯特伍德","identity":"经理","note":"下坠者（通说待核）"}],
["城市的欲望机器（通说）。","'道德不受惩罚'的挑战（B280：immorality goes unpunished）。","自然主义的命运观（B280 语境）。"],
[{"text":"Britannica：'immorality goes unpunished'引发的出版顾虑——仅售不足500册（B280）。","source":"B280"},{"text":"作者页：德莱塞为自然主义最杰出实践者（B280 作者级定位）。","source":"B280"}],
{"difficulties":["自然主义的道德中立。","1900年代芝加哥—纽约。"],"editions":["《嘉莉妹妹》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],"order":"自然主义入门：先本作后《美国的悲剧》。"},
["1900年出版（Doubleday, Page说）核对。","嘉莉/赫斯特伍德人名核对。","1931年再版风波待核。"],
["B280"],"B280","B280",["fenwangyu","taiyangzhaochangshengqi","huozhe"],
G2("《嘉莉妹妹》升降结构图",[{"title":"嘉莉","text":"城市的上升","color":"main"},{"title":"赫斯特伍德","text":"经理的坠落","color":"antagonist"},{"title":"摇椅","text":"欲望的循环","color":"gold"},{"title":"自然主义","text":"道德的中立（B280）","color":"family"}])),

W("di'ertiaojugui","第二十二条军规","Catch-22","美国","现当代","20世纪","长篇小说","小说","英语","heller","约瑟夫·海勒","1961年（作者页B281口径：Catch-22 (1961)——'catch-22'进入英语）",1961,
["作者页（B281）：海勒 major_works 载'第二十二条军规'（B281 作者页定位，详见 manchangdeheian 条核对）。","Britannica（B281）：'The term catch-22 thereafter entered the English language as a reference to a proviso or situation that trips one up no matter which way one turns'；'Centering on the antihero Captain John Yossarian'；'developed a cult following with its dark surrealism'。"],
["约塞连上尉的求生：'catch'——疯子可停飞但申请停飞者即证明理性（悖论通说待核）。","斯诺登之死的时序倒放（通说待核）。"],
[{"name":"约塞连","identity":"投弹手","note":"反英雄（B281：antihero）"},{"name":"卡思卡特上校","identity":"指挥官","note":"（通说待核）"}],
["'catch-22'：悖论的权力（B281）。","反英雄与战争荒诞（B281 语境）。","'黑色幽默'的命名（通说待核）。"],
[{"text":"Britannica：'catch-22'进入英语——绕不开的困境（B281）。","source":"B281"},{"text":"Britannica：'dark surrealism'的邪典追随（B281）。","source":"B281"}],
{"difficulties":["循环悖论。","人物众多（40+）。"],"editions":["《第二十二条军规》（译林出版社扬恝译本，通说待核）。","英文原版（Simon & Schuster）。"],"order":"黑色幽默首选。"},
["1961年出版（Simon & Schuster说）核对。","约塞连/斯诺登人名核对。","'黑色幽默'流派命名待核。"],
["B281"],"B281","B281",["wuhao","fatiaocheng","dongwunongchang"],
G2("《第二十二条军规》悖论结构图",[{"title":"catch-22","text":"进英语的悖论（B281）","color":"main"},{"title":"约塞连","text":"反英雄（B281）","color":"gold"},{"title":"飞行","text":"疯狂的证明","color":"antagonist"},{"title":"黑色幽默","text":"流派命名（通说）","color":"family"}])),

W("yinduzhixing","印度之行","A Passage to India","英国","现当代","20世纪","长篇小说","小说","英语","forster","E.M.福斯特","1924年（作者页B282口径：A Passage to India (1924)——'one of his finest works, examining racism and colonialism'）",1924,
["作者页（B282）：福斯特 major_works 载'印度之行'（B282 作者页定位，详见 huohuadezhuangyuan 条核对）。","Britannica（B282）：'one of his finest works, examining racism and colonialism'；'The novel ends in an uneasy equilibrium'（B282）。","作者（B282）：'The values of truthfulness and kindness dominate Forster's later thinking'。"],
["阿黛拉的马拉巴山洞指控——审判分裂英印两方（B282：a visiting Englishwoman accuses an Indian man of attacking her, and the trial causes division between the British and Indians）。"],
[{"name":"阿黛拉","identity":"英国访客","note":"指控者（B282）"},{"name":"阿齐兹","identity":"印度医生","note":"被告（通说待核）"},{"name":"菲尔丁","identity":"校长","note":"连接者（通说待核）"}],
["种族主义与殖民主义（B282：examining racism and colonialism）。","'不安的平衡'（B282：uneasy equilibrium）。","'只有连接'（Only connect——作者座右铭，通说待核）。"],
[{"text":"Britannica：'one of his finest works'（B282）。","source":"B282"},{"text":"Britannica：1984年大卫·里恩电影改编（通说待核）。","source":"B282"}],
{"difficulties":["英属印度史。","山洞一幕的空白。"],"editions":["《印度之行》（人民文学出版社/译林出版社版本，通说待核）。","英文原版（公有领域渐近）。"],"order":"先《霍华德庄园》后本作。"},
["1924年出版（Edward Arnold说）核对。","阿黛拉/阿齐兹/菲尔丁人名核对。","马拉巴山洞情节待核。"],
["B282"],"B282","B282",["wajie","shijiemori","banlunhuangri"],
G2("《印度之行》审判结构图",[{"title":"马拉巴山洞","text":"指控的空白","color":"antagonist"},{"title":"审判","text":"英印分裂（B282）","color":"main"},{"title":"菲尔丁","text":"连接的尝试","color":"gold"},{"title":"平衡","text":"不安的结尾（B282）","color":"family"}])),
]

for d in works:
    wid = d["id"]
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
