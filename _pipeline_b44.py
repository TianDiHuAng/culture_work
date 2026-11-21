# -*- coding: utf-8 -*-
"""批44：零成本 8 部（论爱情/快乐的男孩/超越人力/新韵/终局/六十篇/磁场/百鸟会议——网络受限期零成本池）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 司汤达《论爱情》(作者页 B038 注记：1822 '结晶'理论)
{"id":"lunaiqing","title":"论爱情","original_title":"De l'amour","region":"法国","era":"近代","era_detail":"19世纪20年代",
"genre":"论著","genre_group":"散文","language":"法语","author_id":"stendhal","author_name":"司汤达",
"year_display":"1822年（作者页 B038 注记：论爱情 (1822)——'结晶'理论）","year_sort":1822,
"background":["作者页（B038）注记：《红与黑》《巴马修道院》《论爱情》；B038：司汤达——'19世纪上半叶最具独创性最复杂的法国作家之一'。","题材（通说待核）：'结晶'理论（crystallization）——恋人心中的盐矿树枝比喻。","Britannica B038 口径：本作为其思想性著作（与小说并列列举）。"],
"outline":["（通说待核——B038未载细节）爱情的诞生：萨尔茨堡盐矿的'结晶'比喻。","（通说待核）'四种爱情'的分类与'快感的原则'。"],
"characters":[{"name":"（论著无人物）","identity":"——","note":"思想论著"}],
"themes":["'结晶'：想象的增幅（通说待核）。",
 "浪漫爱情的解剖（B038 列举语境）。",
 "幸福与激情的道德（通说待核）。"],
"influence":[{"text":"Britannica：司汤达与《论爱情》并列（B038 作者页注记）。","source":"B038"},{"text":"Britannica：'最具独创性最复杂的法国作家之一'（B038 作者级）。","source":"B038"}],
"reading":{"difficulties":["'结晶'概念的心理描述。","1820年代沙龙语境。"],
 "editions":["《论爱情》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"司汤达思想侧面；与《红与黑》对读。"},
"pending":["'结晶'理论细节核对（通说）。","1822年出版细节待核。","'四种爱情'分类待核。"],
"sources":["B038"],"year_source":"B038","author_source":"B038","related_works":["hongyuhei","baMaxiudaoyuan","mengya"],
"svg":G("《论爱情》结晶结构图",[{"title":"盐矿","text":"'结晶'的比喻（通说）","color":"gold"},{"title":"爱情","text":"想象的增幅（通说）","color":"main"},{"title":"分类","text":"四种爱情（通说）","color":"family"},{"title":"司汤达","text":"思想性著作（B038）","color":"antagonist"}])},
# 2. 比昂松《快乐的男孩》(B337)
{"id":"kuailedehaizi","title":"快乐的男孩","original_title":"En glad gutt","region":"挪威","era":"近代","era_detail":"19世纪60年代",
"genre":"中篇小说","genre_group":"小说","language":"挪威语","author_id":"bjornson","author_name":"比奥恩斯彻讷·比昂松",
"year_display":"1860年（Britannica B337：En glad gut (1860)——中译名待核）","year_sort":1860,
"background":["Britannica（B337）：En glad gut (1860)——农庄故事序列（与 Synnøve Solbakken 并列）。","Britannica（B337）：'sought to stimulate national pride...and to present ideals'。","题材（通说待核）：农家男孩的成长故事——'快乐的'心性。"],
"outline":["（通说待核——B337未载剧情）菲恩（Finn说）：孤儿被收养后的成长。","（通说待核）'快乐'心性与家庭的和解。"],
"characters":[{"name":"菲恩","identity":"孤儿","note":"（通说待核，B337未载）"}],
"themes":["农庄故事的教育理想（B337：peasant tales）。",
 "民族自豪的呈现（B337）。",
 "成长与接纳（通说待核）。"],
"influence":[{"text":"Britannica：'peasant tales'序列（B337）。","source":"B337"},{"text":"Britannica：1903诺奖（B337 交叉）。","source":"B337"}],
"reading":{"difficulties":["挪威乡土社会。","'农庄故事'类型。"],
 "editions":["《快乐的男孩》中译名（《快活的男孩》两说——通说待核）。","挪威文原版（公有领域）。"],
 "order":"比昂松农庄故事之二；与《辛诺夫·索巴肯》对读。"},
"pending":["菲恩人名核对（通说）。","1860年发表（《比昂格·比尔森的故事》说）待核。","中译名两说待核。"],
"sources":["B337"],"year_source":"B337","author_source":"B337","related_works":["xinnuofusuobaken","pochan","qieelvxing"],
"svg":G("《快乐的男孩》成长图",[{"title":"菲恩","text":"'快乐'的心性（通说）","color":"main"},{"title":"农庄","text":"收养的家庭（通说）","color":"family"},{"title":"理想","text":"教育的呈现（B337）","color":"gold"},{"title":"排斥","text":"成长的试炼（通说）","color":"antagonist"}])},
# 3. 比昂松《超越人力》(B337)
{"id":"chaoyuerenli","title":"超越人力","original_title":"Over Ævne I og II","region":"挪威","era":"近代","era_detail":"19世纪末",
"genre":"戏剧（两部）","genre_group":"戏剧","language":"挪威语","author_id":"bjornson","author_name":"比奥恩斯彻讷·比昂松",
"year_display":"1883/1895年（Britannica B337：Over Ævne I og II (1883, 1895)）","year_sort":1883,
"background":["Britannica（B337）：Over Ævne I og II——'The two dramas that brought him an international reputation were thus written in self-imposed exile'（带来国际声誉的两部戏剧，写于自我放逐中——B337 指向待核）。","Britannica（B337）：'his plays were influential in establishing social realism in Europe'。","题材（通说待核）：神父桑戈的信仰狂热——'超越人力'的奇迹主张与社会代价。"],
"outline":["（通说待核）第一部：桑戈神父以奇迹为名的葬礼赌注。","（通说待核）第二部：知识的傲慢与狂热的对撞。"],
"characters":[{"name":"桑戈","identity":"神父","note":"（通说待核）"}],
"themes":["信仰的狂热与理性（通说待核）。",
 "国际声誉的两部曲（B337 注记）。",
 "社会现实主义（B337）。"],
"influence":[{"text":"Britannica：'The two dramas that brought him an international reputation'（B337——指向待核）。","source":"B337"},{"text":"Britannica：1903诺奖（B337 交叉）。","source":"B337"}],
"reading":{"difficulties":["两部的主题延续。","宗教与社会改革的语境。"],
 "editions":["《超越人力》中译名（《越界》两说——通说待核）。","挪威文原版。"],
 "order":"比昂松戏剧之二；与《破产》对读。"},
"pending":["'国际声誉两部'是否确指本作核对（B337 语境）。","桑戈人名核对（通说）。","两部年份（1883/1895——B337）核对。"],
"sources":["B337"],"year_source":"B337","author_source":"B337","related_works":["pochan","xinnuofusuobaken","peierjinte"],
"svg":G("《超越人力》狂热结构图",[{"title":"桑戈","text":"信仰的赌注（通说）","color":"main"},{"title":"奇迹","text":"'超越人力'（书名）","color":"gold"},{"title":"放逐","text":"国际声誉的代价（B337）","color":"family"},{"title":"理性","text":"知识的对撞（通说）","color":"antagonist"}])},
# 4. 卡尔杜齐《新韵》(B345)
{"id":"xinyun","title":"新韵","original_title":"Rime nuove","region":"意大利","era":"近代","era_detail":"19世纪80年代",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"carducci","author_name":"焦苏埃·卡尔杜齐",
"year_display":"1887年（Britannica B345：Rime nuove (1887)——与《野蛮颂》'contain the best of Carducci's poetry'）","year_sort":1887,
"background":["Britannica（B345）：Rime nuove——与《野蛮颂》一起'contain the best of Carducci's poetry'。","Britannica（B345）：含 Maremma 风景、童年回忆与'the lament for the loss of his only son'（独子之殇）。","Britannica（B345）：1906诺奖。"],
"outline":["（通说待核——B345未载篇目）Maremma 风景的抒情与童年回忆。","（通说待核）'独子之殇'的哀歌（《致母亲》等说）。"],
"characters":[{"name":"抒情'我'","identity":"古典主义者","note":"（B345 语境）"}],
"themes":["风景与回忆（B345：Maremma evocations, childhood memories）。",
 "丧子的哀歌（B345）。",
 "古典格律的现代意语（B345 交叉）。"],
"influence":[{"text":"Britannica：'contain the best of Carducci's poetry'（B345）。","source":"B345"},{"text":"Britannica：1906诺奖（B345 交叉）。","source":"B345"}],
"reading":{"difficulties":["托斯卡纳方言地名。","哀歌与颂歌的语体切换。"],
 "editions":["《新韵》中译名（《新诗集》两说——通说待核）。","意大利文原版（公有领域）。"],
 "order":"卡杜齐抒情诗首选；与《野蛮颂》对读。"},
"pending":["篇目核对（B345未载）。","1887年出版细节待核。","'独子'哀歌篇目归属待核。"],
"sources":["B345"],"year_source":"B345","author_source":"B345","related_works":["yemanli","sadansong","xuboliweng"],
"svg":G("《新韵》哀歌结构图",[{"title":"Maremma","text":"风景的抒情（B345）","color":"gold"},{"title":"童年","text":"回忆的诗学（B345）","color":"family"},{"title":"独子之殇","text":"哀歌的核心（B345）","color":"main"},{"title":"古典","text":"格律的余音（B345语境）","color":"antagonist"}])},
# 5. 贝克特《终局》(B094)
{"id":"zhongju","title":"终局","original_title":"Endgame","region":"爱尔兰","era":"现当代","era_detail":"20世纪50年代",
"genre":"戏剧","genre_group":"戏剧","language":"法语（英译）","author_id":"beckett","author_name":"萨缪尔·贝克特",
"year_display":"1957年（作者页 B094 注记：终局（1957）、快乐的日子（1961）——'荒诞剧双璧（Britannica 列举）'）","year_sort":1957,
"background":["作者页（B094）注记：终局（1957）、快乐的日子 (1961)——'荒诞剧双璧（Britannica 列举）'。","Britannica（B094）：贝克特——1969诺奖；'his most celebrated play'为《等待戈多》。","题材（通说待核）：室内末日棋局——哈姆与仆人克洛夫的相互依赖。"],
"outline":["（通说待核）哈姆在扶椅上的'棋局'：仆人克洛夫无法离开。","（通说待核）窗外'零'的世界与'结束'的开始。"],
"characters":[{"name":"哈姆","identity":"盲的权威","note":"（通说待核）"},{"name":"克洛夫","identity":"仆人","note":"（通说待核）"}],
"themes":["依赖与厌恶的共生（通说待核）。",
 "'终局'：象棋术语的存在化（书名语境——通说待核）。",
 "语言的耗尽（B094 荒诞派语境）。"],
"influence":[{"text":"Britannica：'荒诞剧双璧'（作者页 B094 注记）。","source":"B094"},{"text":"Britannica：1969诺奖（B094 交叉）。","source":"B094"}],
"reading":{"difficulties":["'棋局'的结构隐喻。","与《等待戈多》的并读。"],
 "editions":["《终局》中译本（湖南文艺《贝克特选集》等——通说待核）。","法文原版 Fin de partie。"],
 "order":"贝克特戏剧之二；与《等待戈多》对读。"},
"pending":["哈姆/克洛夫/奈格/奈尔人名核对（通说）。","1957年首演（伦敦皇家宫廷剧院说法）待核。","法文原版年份（1957法文Fin de partie说）待核。"],
"sources":["B094"],"year_source":"B094","author_source":"B094","related_works":["dengdaigou","moluoyi","toutougeonv"],
"svg":G("《终局》棋局结构图",[{"title":"哈姆","text":"扶椅上的权威（通说）","color":"main"},{"title":"克洛夫","text":"无法离开的仆人（通说）","color":"gold"},{"title":"棋局","text":"'终局'的存在化（书名）","color":"antagonist"},{"title":"零","text":"窗外的世界（通说）","color":"family"}])},
# 6. 布扎蒂《六十篇》(B351)
{"id":"liushipian","title":"六十篇","original_title":"Sessanta racconti","region":"意大利","era":"现当代","era_detail":"20世纪50年代末",
"genre":"短篇小说集","genre_group":"故事集","language":"意大利语","author_id":"buzzati","author_name":"迪诺·布扎蒂",
"year_display":"1958年（Britannica B351：Sessanta racconti (1958)——'Sixty Tales' collection）","year_sort":1958,
"background":["Britannica（B351）：Sessanta racconti (1958)——'Sixty Tales' collection。","Britannica（B351）：布扎蒂——卡夫卡式超现实、象征与荒诞——'uniquely devastating skill and detached sense of irony and humor'。","题材（通说待核）：六十个短篇的荒诞集——电梯、坠落、怪物与时间。"],
"outline":["（通说待核——B351未载篇目）超现实短篇的精选集。","（通说待核）'K'式恐慌与反讽的并置。"],
"characters":[{"name":"众篇人物","identity":"——","note":"（通说待核）"}],
"themes":["卡夫卡式的超现实（B351：Kafkaesque surrealism）。",
 "日常的恐怖化（通说待核）。",
 "疏离的反讽（B351：detached sense of irony）。"],
"influence":[{"text":"Britannica：'Sixty Tales' collection（B351）。","source":"B351"},{"text":"Britannica：'detached sense of irony and humor'（B351）。","source":"B351"}],
"reading":{"difficulties":["超现实短篇的逻辑。","1950年代意大利都市背景。"],
 "editions":["《六十篇》中译名（《短篇小说六十篇》两说——通说待核）。","意大利文原版。"],
 "order":"布扎蒂短篇首选；与《鞑靼人沙漠》对读。"},
"pending":["篇目核对（B351未载）。","1958年出版（Mondadori说）待核。","'六十篇'实数核对。"],
"sources":["B351"],"year_source":"B351","author_source":"B351","related_works":["datatarenshamo","chengbao","luoshengmen"],
"svg":G("《六十篇》荒诞集结构图",[{"title":"六十篇","text":"超现实的精选（B351）","color":"main"},{"title":"恐慌","text":"'K'式日常（通说）","color":"antagonist"},{"title":"反讽","text":"疏离的幽默（B351）","color":"gold"},{"title":"卡夫卡","text":"影响的谱系（B351）","color":"family"}])},
# 7. 布勒东《磁场》(B344)
{"id":"cichang","title":"磁场","original_title":"Les Champs magnétiques","region":"法国","era":"近代","era_detail":"20世纪20年代",
"genre":"散文诗集（合作）","genre_group":"诗歌","language":"法语","author_id":"breton","author_name":"安德烈·布勒东",
"year_display":"1920年（Britannica B344：Les Champs magnétiques (1920)——with Philippe Soupault——'the first example of the Surrealist technique of automatic writing'）","year_sort":1920,
"background":["Britannica（B344）：与苏波合著——'the first example of the Surrealist technique of automatic writing'（超现实主义自动写作的首例）。","Britannica（B344）：1919年与阿拉贡、苏波创办 Littérature 杂志——本作为其直接产物。","Britannica（B344）：1924宣言定义超现实主义——'pure psychic automatism'——本作为其先声。"],
"outline":["（通说待核——B344未载篇目）轮流自动写作的章节：梦境、幻觉与都市流动。","（通说待核）'磁场的领域'：无意识与外部世界的交感。"],
"characters":[{"name":"双声部'我'","identity":"布勒东/苏波","note":"（B344：with Philippe Soupault）"}],
"themes":["自动写作的开端（B344：first example）。",
 "无意识的磁力学（书名语境——通说待核）。",
 "宣言之前的方法实践（B344：1924宣言交叉）。"],
"influence":[{"text":"Britannica：'the first example of the Surrealist technique of automatic writing'（B344）。","source":"B344"},{"text":"Britannica：1924《超现实主义宣言》定义（B344 交叉）。","source":"B344"}],
"reading":{"difficulties":["自动写作的语流。","合作无署名（通说待核）。"],
 "editions":["《磁场》中译名（《磁场》/《磁力场》两说——通说待核）。","法文原版（公有领域状态待核）。"],
 "order":"超现实主义源头文本；配合《宣言》阅读。"},
"pending":["章节结构核对（通说）。","1920年出版细节待核。","'合作'分工方式待核。"],
"sources":["B344"],"year_source":"B344","author_source":"B344","related_works":["najia","diyuzhiji","balideyouyu"],
"svg":G("《磁场》自动写作结构图",[{"title":"自动写作","text":"超现实主义首例（B344）","color":"gold"},{"title":"双声部","text":"布勒东×苏波（B344）","color":"main"},{"title":"磁场","text":"无意识的交感（书名）","color":"family"},{"title":"宣言","text":"1924的前声（B344交叉）","color":"antagonist"}])},
# 8. 乔叟《百鸟会议》(Britannica 列举 梦幻诗)
{"id":"bainiaohuiyi","title":"百鸟会议","original_title":"The Parliament of Fowls","region":"英国","era":"古代","era_detail":"14世纪80年代",
"genre":"梦幻诗","genre_group":"诗歌","language":"英语（中古英语）","author_id":"chaucer","author_name":"杰弗里·乔叟",
"year_display":"作者页注记：Britannica 列举（梦幻诗——公爵夫人之书、百鸟会议、名誉之宫——年份通说待核）","year_sort":1382,
"background":["作者页注记：公爵夫人之书、百鸟会议、名誉之宫——'梦幻诗（Britannica 列举）'。","Britannica：乔叟——'英国诗歌之父'（作者页语境——待核）。","题材（通说待核）：情人节的自然主持百鸟择偶辩论——西塞罗《西庇阿之梦》框架。"],
"outline":["（通说待核）'我'梦入维纳斯花园：众鸟辩论求爱。","（通说待核）'自然'女神的仲裁与三音步回旋曲结尾。"],
"characters":[{"name":"自然","identity":"仲裁者","note":"（通说待核）"},{"name":"众鸟","identity":"辩论者","note":"（通说待核）"}],
"themes":["爱与理性的辩论（通说待核）。",
 "梦幻诗框架（B注记：梦幻诗序列）。",
 "鸟类讽喻人类等级（通说待核）。"],
"influence":[{"text":"Britannica：梦幻诗序列（作者页注记）。","source":src_of('chaucer')},{"text":"Britannica：《坎特伯雷故事》为代表作（作者页交叉）。","source":src_of('chaucer')}],
"reading":{"difficulties":["梦幻诗的框架结构。","鸟类的社会隐喻。"],
 "editions":["《百鸟会议》中译名（《众鸟之会》两说——通说待核）。","中古英语原版（公有领域）。"],
 "order":"乔叟梦幻诗首选；与《特洛伊罗斯》对读。"},
"pending":["成诗年份（约1382说）待核。","篇名写法核对。","'西庇阿之梦'框架细节待核。"],
"sources":[src_of('chaucer')],"year_source":src_of('chaucer'),"author_source":src_of('chaucer'),"related_works":["teluoyiluosi","kanteboleigushi","leiyu"],
"svg":G("《百鸟会议》辩论结构图",[{"title":"自然","text":"爱的仲裁（通说）","color":"gold"},{"title":"众鸟","text":"等级的讽喻（通说）","color":"main"},{"title":"花园","text":"维纳斯的领地（通说）","color":"antagonist"},{"title":"梦幻","text":"乔叟的框架（B注记）","color":"family"}])},
]
created = []
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    created.append(w['id'])
    print('work', w['id'])

def link(aid, wid, kw=None):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        done = False
        if kw:
            for i, m in enumerate(j['major_works']):
                if m.get('title') and kw in m['title']:
                    j['major_works'][i] = {"work_id": wid, "note": m['note']}
                    done = True; break
        if not done:
            j['major_works'].append({"work_id": wid, "note": "（零成本批44）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('lunaiqing','stendhal','论爱情'),('kuailedehaizi','bjornson','快乐的男孩'),('chaoyuerenli','bjornson','超越人力'),('xinyun','carducci','新韵'),('zhongju','beckett','终局'),('liushipian','buzzati','六十篇'),('cichang','breton','磁场'),('bainiaohuiyi','chaucer','百鸟会议')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH44 DONE')
