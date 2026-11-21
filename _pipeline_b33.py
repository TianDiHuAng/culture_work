# -*- coding: utf-8 -*-
"""批33：零成本 8 部（复用 B253/B107/B109/B039/B037/B106 作者页注记）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 阿列克谢耶维奇《切尔诺贝利的祭祷》(B253)
{"id":"qieernuobei","title":"切尔诺贝利的祭祷","original_title":"Чернобыльская молитва（Voices from Chernobyl）","region":"白俄罗斯","era":"现当代","era_detail":"20世纪90年代",
"genre":"纪实文学（口述实录）","genre_group":"散文","language":"俄语","author_id":"alexievich","author_name":"斯韦特兰娜·阿列克谢耶维奇",
"year_display":"1997年（Britannica B253：Voices from Chernobyl (1997)——中译名通说待核）","year_sort":1997,
"background":["Britannica（B253）：Voices from Chernobyl (1997)——作者页列举（剧情/篇目细节通说待核）。","Britannica（B253）：其方法——'hybrid literary genre that evolved as the closest possible approximation to real life'、'human voices were allowed to speak for themselves'。","Britannica（B253）：目标'a history of human feelings'；2015诺奖授奖词'for her polyphonic writings, a monument to suffering and courage in our time'。"],
"outline":["核灾难幸存者与清理者们的众声独白（B253 方法语境——受访者细节通说待核）。","'人类情感史'的切尔诺贝利卷（B253：a history of human feelings）。"],
"characters":[{"name":"众声受访者","identity":"清理者/撤离者/遗属","note":"（通说待核，B253未载具体人名）"}],
"themes":["'人类情感史'的口述档案（B253）。",
 "'复调'写作：让声音自己说话（B253：human voices...speak for themselves）。",
 "核时代的日常之痛（通说待核）。"],
"influence":[{"text":"Britannica：2015诺奖——'a monument to suffering and courage in our time'（B253）。","source":"B253"},{"text":"Britannica：'polyphonic writings'（B253）。","source":"B253"}],
"reading":{"difficulties":["口述实录的复调结构。","切尔诺贝利事故史（1986——通说待核）。"],
 "editions":["《切尔诺贝利的祭祷》中译本（中信等——通说待核）。","俄文原版。"],
 "order":"阿列克谢耶维奇首选之一；与《二手时间》对读。"},
"pending":["中译名（《切尔诺贝利的祭祷》/《切尔诺贝利的悲鸣》）待核。","1997年俄文初版细节待核。","受访者章节结构待核。"],
"sources":["B253"],"year_source":"B253","author_source":"B253","related_works":["ershoushijian","huoluan","xiaoyuyi"],
"svg":G("《切尔诺贝利的祭祷》众声结构图",[{"title":"众声","text":"让声音自己说话（B253）","color":"main"},{"title":"复调","text":"polyphonic writings（B253）","color":"gold"},{"title":"情感史","text":"a history of human feelings（B253）","color":"family"},{"title":"核灾","text":"1986年的余波（通说）","color":"antagonist"}])},
# 2. 阿列克谢耶维奇《锌皮娃娃兵》(B253)
{"id":"xinpifawabing","title":"锌皮娃娃兵","original_title":"Цинковые мальчики（Zinky Boys）","region":"白俄罗斯","era":"现当代","era_detail":"20世纪80年代末",
"genre":"纪实文学（口述实录）","genre_group":"散文","language":"俄语","author_id":"alexievich","author_name":"斯韦特兰娜·阿列克谢耶维奇",
"year_display":"1990年（Britannica B253：Zinky Boys (1990)——中译名通说待核）","year_sort":1990,
"background":["Britannica（B253）：Zinky Boys (1990)——作者页列举（阿富汗战争题材——通说待核）。","Britannica（B253）：方法——'human voices were allowed to speak for themselves'；'a history of human feelings'。","Britannica（B253）：2015诺奖授奖词——'for her polyphonic writings, a monument to suffering and courage in our time'。"],
"outline":["阿富汗战争归来的士兵与母亲们的口述（题材通说待核——B253未载细节）。","'锌皮棺材'：战争的代价（书名意象通说待核）。"],
"characters":[{"name":"众声受访者","identity":"士兵/母亲","note":"（通说待核，B253未载）"}],
"themes":["战争的口述档案（B253 方法）。",
 "母亲与士兵的对话（通说待核）。",
 "政治与身体的账目（通说待核）。"],
"influence":[{"text":"Britannica：'polyphonic writings'——2015诺奖（B253）。","source":"B253"},{"text":"Britannica：'hybrid literary genre'（B253）。","source":"B253"}],
"reading":{"difficulties":["苏联阿富汗战争史（1979-89——通说待核）。","口述的伦理。"],
 "editions":["《锌皮娃娃兵》中译本（中信等——通说待核）。","俄文原版。"],
 "order":"与《切尔诺贝利的祭祷》对读。"},
"pending":["中译名两说（《锌皮娃娃兵》/《锌皮男孩》）待核。","1990年出版争议细节待核。","章节结构待核。"],
"sources":["B253"],"year_source":"B253","author_source":"B253","related_works":["ershoushijian","qieernuobei","xiaoyuyi"],
"svg":G("《锌皮娃娃兵》口述结构图",[{"title":"士兵","text":"归来的口述（通说）","color":"main"},{"title":"母亲","text":"锌皮棺材（通说）","color":"family"},{"title":"战争","text":"阿富汗的账目（通说）","color":"antagonist"},{"title":"复调","text":"诺奖的评语（B253）","color":"gold"}])},
# 3. 阿特伍德《盲刺客》(B107)
{"id":"mangcike","title":"盲刺客","original_title":"The Blind Assassin","region":"加拿大","era":"现当代","era_detail":"21世纪初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"atwood","author_name":"玛格丽特·阿特伍德",
"year_display":"2000年（Britannica B107：布克奖 2000《盲刺客》）","year_sort":2000,
"background":["Britannica（B107）：布克奖 2000《盲刺客》。","Britannica（B107）：阿特伍德——'以散文虚构与女性主义视角著称'。","结构（通说待核）：小说套小说——姐姐的回忆+《盲刺客》连载+报告。"],
"outline":["（通说待核——B107未载剧情）两姐妹、一桩死亡与一部连载小说的嵌套。","（通说待核）'盲刺客'的故事层：战争与外星文明。"],
"characters":[{"name":"艾丽丝","identity":"回忆者/姐姐","note":"（通说待核，B107未载）"},{"name":"劳拉","identity":"妹妹","note":"（通说待核，B107未载）"}],
"themes":["女性叙述与历史秘辛（通说待核）。",
 "嵌套结构的叙事游戏（通说待核）。",
 "商业社会的批判（B107 女性主义视角语境）。"],
"influence":[{"text":"Britannica：布克奖 2000（B107）。","source":"B107"},{"text":"Britannica：'女性主义视角'（B107 作者级定位）。","source":"B107"}],
"reading":{"difficulties":["三层嵌套叙事。","1930-40年代加拿大商界史（通说待核）。"],
 "editions":["《盲刺客》中译本（译林等——通说待核）。","英文原版。"],
 "order":"阿特伍德进阶；与《使女的故事》对读。"},
"pending":["艾丽丝/劳拉人名核对（B107未载）。","2000年出版（McClelland & Stewart说）待核。","《盲刺客》连载细节待核。"],
"sources":["B107"],"year_source":"B107","author_source":"B107","related_works":["shinv","zise","dulidemen"],
"svg":G("《盲刺客》嵌套结构图",[{"title":"回忆","text":"姐姐的讲述（通说）","color":"main"},{"title":"连载","text":"小说中的小说（通说）","color":"gold"},{"title":"布克奖","text":"2000（B107）","color":"family"},{"title":"秘辛","text":"死亡与真相（通说）","color":"antagonist"}])},
# 4. 阿特伍德《证言》(B107)
{"id":"zhengyan","title":"证言","original_title":"The Testaments","region":"加拿大","era":"现当代","era_detail":"21世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"atwood","author_name":"玛格丽特·阿特伍德",
"year_display":"2019年（Britannica B107：布克奖 2019《证言》共享）","year_sort":2019,
"background":["Britannica（B107）：布克奖 2019《证言》——共享奖（'2019《证言》共享'）。","Britannica（B107）：《使女的故事》(1985)——'基督教原教旨主义神权下的反乌托邦'——本作为其续章。","题材（通说待核）：基列国十五章后的三重证言。"],
"outline":["（通说待核——B107未载剧情）三位女性的证言：执政者、逃亡者与幸存者。","（通说待核）基列国的内溃。"],
"characters":[{"name":"丽德阿姨","identity":"执政者","note":"（通说待核，B107未载）"},{"name":"奥芙格伦","identity":"幸存者","note":"（通说待核，B107未载）"}],
"themes":["反乌托邦的内部视角（通说待核）。",
 "证言：法律与叙事（通说待核）。",
 "女性主义的当代回声（B107）。"],
"influence":[{"text":"Britannica：布克奖 2019 共享（B107）。","source":"B107"},{"text":"Britannica：《使女的故事》——神权反乌托邦（B107）。","source":"B107"}],
"reading":{"difficulties":["基列国词汇表。","与《使女的故事》的互文。"],
 "editions":["《证言》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"《使女的故事》续读。"},
"pending":["丽德/奥芙格伦人名核对（B107未载）。","2019年出版（Penguin说）待核。","布克'共享'细节待核。"],
"sources":["B107"],"year_source":"B107","author_source":"B107","related_works":["shinv","mangcike","leiyu"],
"svg":G("《证言》三重证言图",[{"title":"证言一","text":"执政者的忏悔（通说）","color":"antagonist"},{"title":"证言二","text":"逃亡者的路（通说）","color":"main"},{"title":"证言三","text":"幸存者的档案（通说）","color":"family"},{"title":"布克","text":"2019共享（B107）","color":"gold"}])},
# 5. 芥川龙之介《河童》(B109)
{"id":"hetong","title":"河童","original_title":"河童（Kappa）","region":"日本","era":"近代","era_detail":"20世纪20年代",
"genre":"中篇小说","genre_group":"小说","language":"日语","author_id":"akutagawa","author_name":"芥川龙之介",
"year_display":"1927年（Britannica B109：绝笔讽刺《河童》(1927)映照抑郁）","year_sort":1927,
"background":["Britannica（B109）：绝笔讽刺《河童》(1927)——'映照抑郁'（санаторий语境——页面口径）。","Britannica（B109）：芥川——'改写12-13世纪故事集以现代心理学'、取材中国典籍与欧洲见闻；35岁自杀震惊文坛。","题材（通说待核）：病人掉入河童国——人类社会的讽刺倒影。"],
"outline":["河童国的讽喻：文明、宗教与艺术的倒影（B109：讽刺——情节通说待核）。","产房'先行产权'等段落的讽刺（细节通说待核）。"],
"characters":[{"name":"病人/'我'","identity":"叙述者","note":"（通说待核，B109未载）"},{"name":"河童学生","identity":"讽喻伙伴","note":"（通说待核，B109未载）"}],
"themes":["文明的倒影讽刺（B109：讽刺）。",
 "'映照抑郁'的自白性（B109）。",
 "现代心理学的古典改写法（B109：改写...以现代心理学）。"],
"influence":[{"text":"Britannica：绝笔——35岁自杀震惊文坛（B109）。","source":"B109"},{"text":"Britannica：讽刺传统与《罗生门》并置（B109 语境）。","source":"B109"}],
"reading":{"difficulties":["河童民俗与讽喻的转换。","大正末年的思想史（通说待核）。"],
 "editions":["《河童》中译本（人民文学/上海译文等——通说待核）。","日文原版（公有领域状态待核）。"],
 "order":"芥川后期首选；与《罗生门》对读。"},
"pending":["情节细节核对（河童国诸段落——通说）。","1927年发表（《文艺春秋》说）待核。","'映照抑郁'语境（精神病院口述框架）待核。"],
"sources":["B109"],"year_source":"B109","author_source":"B109","related_works":["luoshengmen","renshijian","bianxingji"],
"svg":G("《河童》讽喻倒影图",[{"title":"河童国","text":"人类的倒影（通说）","color":"gold"},{"title":"讽刺","text":"绝笔的锋芒（B109）","color":"main"},{"title":"抑郁","text":"'映照抑郁'（B109）","color":"antagonist"},{"title":"改写","text":"古典的现代心理（B109）","color":"family"}])},
# 6. 巴尔扎克《欧也妮·葛朗台》(B039)
{"id":"ouyanigelangtai","title":"欧也妮·葛朗台","original_title":"Eugénie Grandet","region":"法国","era":"近代","era_detail":"19世纪30年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"balzac","author_name":"奥诺雷·德·巴尔扎克",
"year_display":"1833年（Britannica B039：《人间喜剧》列举 Eugénie Grandet——出版年通说待核）","year_sort":1833,
"background":["Britannica（B039）：《人间喜剧》约90部——Eugénie Grandet 在列举之列（作者页注记）。","Britannica（B039）：巴尔扎克——'现实主义主要先驱、现代小说系列开创者、公认史上最伟大小说家之一'之评；'偏执狂'人物塑造论。","题材（通说待核）：索缪城的守财奴葛朗台与其女欧也妮——金钱对家庭的腐蚀。"],
"outline":["（通说待核——B039未载剧情）守财奴的遗产游戏与女儿的牺牲。","（通说待核）堂弟夏尔的到来与巴黎的诱惑。"],
"characters":[{"name":"葛朗台","identity":"守财奴","note":"（通说待核——'守财奴文学经典'之注记）"},{"name":"欧也妮","identity":"女儿","note":"（通说待核，B039未载）"}],
"themes":["金钱对亲情的腐蚀（通说待核）。",
 "'偏执狂'人物塑造（B039：人物塑造论）。",
 "外省与巴黎的对比（通说待核）。"],
"influence":[{"text":"Britannica：'现实主义主要先驱'（B039 作者级）。","source":"B039"},{"text":"Britannica：《人间喜剧》人物复现法（B039）。","source":"B039"}],
"reading":{"difficulties":["复辟时期外省社会（通说待核）。","《人间喜剧》体系定位。"],
 "editions":["《欧也妮·葛朗台》中译本（人民文学/上海译文等——通说待核）。","法文原版（公有领域）。"],
 "order":"巴尔扎克入门首选；与《高老头》对读。"},
"pending":["1833年出版细节核对（通说）。","葛朗台/欧也妮/夏尔人名核对（B039未载）。","与《人间喜剧》分册归属待核。"],
"sources":["B039"],"year_source":"B039","author_source":"B039","related_works":["gaolaotou","mengya","baofali"],
"svg":G("《欧也妮·葛朗台》金钱腐蚀图",[{"title":"葛朗台","text":"守财奴（通说）","color":"antagonist"},{"title":"欧也妮","text":"牺牲的女儿（通说）","color":"main"},{"title":"金钱","text":"家庭的腐蚀（通说）","color":"gold"},{"title":"偏执狂","text":"人物塑造论（B039）","color":"family"}])},
# 7. 奥斯汀《爱玛》(B037)
{"id":"aimaa","title":"爱玛","original_title":"Emma","region":"英国","era":"近代","era_detail":"19世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"austen","author_name":"简·奥斯汀",
"year_display":"1815年（出版年通说待核；Britannica B037：司各特1816年《评论季刊》评《爱玛》）","year_sort":1815,
"background":["Britannica（B037）：司各特1816年《评论季刊》评《爱玛》——奥斯汀严肃批评史的起点脉络之一。","Britannica（B037）：奥斯汀——'自由间接引语、风尚小说奠基'（作者页注记）。","题材（通说待核）：'漂亮、聪明、有钱'的爱玛·伍德豪斯的媒人游戏与自我认知。"],
"outline":["（通说待核——B037未载剧情）爱玛的撮合游戏与误判。","（通说待核）奈特利先生的批评与和解。"],
"characters":[{"name":"爱玛·伍德豪斯","identity":"女主人公","note":"（通说待核，B037未载）"},{"name":"奈特利","identity":"批评者","note":"（通说待核，B037未载）"}],
"themes":["自由间接引语的成熟实践（B037：作者页注记）。",
 "风尚小说（comedy of manners）的延续（B037）。",
 "自我认知的喜剧（通说待核）。"],
"influence":[{"text":"Britannica：司各特1816年评论（B037）。","source":"B037"},{"text":"Britannica：惠特利1821评论开创严肃批评（B037 交叉）。","source":"B037"}],
"reading":{"difficulties":["摄政时期英国乡绅社会。","自由间接引语的辨识。"],
 "editions":["《爱玛》中译本（人民文学/译林等——通说待核）。","英文原版（公有领域）。"],
 "order":"奥斯汀第三部；与《傲慢与偏见》《劝导》对读。"},
"pending":["1815年出版（John Murray说）核对。","爱玛/奈特利人名核对（B037未载）。","司各特评论原文待核。"],
"sources":["B037"],"year_source":"B037","author_source":"B037","related_works":["aoman","baofali","leiyu"],
"svg":G("《爱玛》自我认知图",[{"title":"爱玛","text":"媒人游戏（通说）","color":"main"},{"title":"误判","text":"撮合的连锁（通说）","color":"antagonist"},{"title":"自由间接引语","text":"叙事的成熟（B037）","color":"gold"},{"title":"和解","text":"认知的完成（通说）","color":"family"}])},
# 8. 阿契贝《荒原蚁丘》(B106)
{"id":"huangyanyiqiu","title":"荒原蚁丘","original_title":"Anthills of the Savannah","region":"尼日利亚","era":"现当代","era_detail":"20世纪80年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"achebe","author_name":"钦努阿·阿契贝",
"year_display":"1987年（作者页 B106 注记：Britannica 列举——出版年通说待核）","year_sort":1987,
"background":["作者页（B106）：Britannica 列举《荒原蚁丘》；另有《瓦解》《再也不得安宁》《神箭》《人民公敌》。","Britannica（B106）：阿契贝——'检视英国帝国主义对尼日利亚传统的冲击'；2007年布克国际奖。","题材（通说待核）：虚构的卡angan军政权下的三个朋友——谎言与国家的崩坏。"],
"outline":["（通说待核——B106未载剧情）军政权下的知识分子三重奏。","（通说待核）'蚁丘'：权力与废墟的意象。"],
"characters":[{"name":"萨姆/克里斯托弗/伊肯","identity":"三个朋友","note":"（通说待核，B106未载）"}],
"themes":["后殖民国家的权力病（B106 语境）。",
 "知识分子的责任（通说待核）。",
 "'帝国冲击'的延续书写（B106：检视英国帝国主义）。"],
"influence":[{"text":"Britannica：2007年布克国际奖（B106）。","source":"B106"},{"text":"Britannica：'检视英国帝国主义对尼日利亚传统的冲击'（B106）。","source":"B106"}],
"reading":{"difficulties":["虚构西非国家（卡angan说待核）。","《瓦解》三部曲的延伸。"],
 "editions":["《荒原蚁丘》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"阿契贝后期首选。"},
"pending":["人物名核对（B106未载）。","1987年出版（Doubleday说）待核。","虚构国名（Kangan说）待核。"],
"sources":["B106"],"year_source":"B106","author_source":"B106","related_works":[rid("zhexu" if "zhexu" in existing else "kanbujian3"),"kanbujian3","zise"],
"svg":G("《荒原蚁丘》权力废墟图",[{"title":"军政权","text":"谎言的国家（通说）","color":"antagonist"},{"title":"三个朋友","text":"知识分子的分岔（通说）","color":"main"},{"title":"蚁丘","text":"废墟的意象（通说）","color":"gold"},{"title":"后殖民","text":"帝国的延续（B106）","color":"family"}])},
]
for w in works:
    if w['id'] in existing:
        print('skip existing', w['id'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

# 作者页挂链（替换 title-only 条目）
def link(aid, wid, repl_title_kw=None):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        idx = None
        if repl_title_kw:
            for i, m in enumerate(j['major_works']):
                if m.get('title') and repl_title_kw in m['title']:
                    idx = i; break
        note = j['major_works'][idx]['note'] if idx is not None else '（零成本批33）'
        if idx is not None:
            j['major_works'][idx] = {"work_id": wid, "note": note}
        else:
            j['major_works'].append({"work_id": wid, "note": "（零成本批33）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

link('alexievich', 'qieernuobei', '切尔诺贝利')
link('alexievich', 'xinpifawabing')  # 新增
link('atwood', 'mangcike', '盲刺客')
link('atwood', 'zhengyan', '证言')
link('akutagawa', 'hetong')  # 新增
link('balzac', 'ouyanigelangtai', '欧也妮')
link('austen', 'aimaa', '爱玛')
link('achebe', 'huangyanyiqiu', '荒原蚁丘')
print('BATCH33 DONE')
