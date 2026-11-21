# -*- coding: utf-8 -*-
"""批37：零成本 7 部二作（肖洛霍夫/斯坦贝克×2/霍桑/纪德/福克纳/福楼拜 作者页注记 + 书名查重）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def src_of(aid):
    j = json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))
    return j['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

S_SHO, S_ST, S_HA, S_GI, S_FA, S_FL = src_of('sholokhov'), src_of('steinbeck'), src_of('hawthorne'), src_of('gide'), src_of('faulkner'), src_of('flaubert')
print('srcs:', S_SHO, S_ST, S_HA, S_GI, S_FA, S_FL)

works = [
# 1. 肖洛霍夫《一个人的遭遇》
{"id":"yigerendeyu","title":"一个人的遭遇","original_title":"Судьба человека","region":"苏联","era":"现当代","era_detail":"20世纪50年代",
"genre":"短篇小说","genre_group":"小说","language":"俄语","author_id":"sholokhov","author_name":"米哈伊尔·肖洛霍夫",
"year_display":"1957年（Britannica B098：一个人的遭遇——Britannica 列举）","year_sort":1957,
"background":["作者页（B098）注记：一个人的遭遇 (1957)——'二战短篇经典（Britannica 列举）'。","Britannica（B098）：肖洛霍夫——哥萨克作家；1965诺贝尔；《静静的顿河》四部(1928-40)为苏联最广泛阅读的小说。","题材（通说待核）：卫国战争中失去一切的司机索科洛夫——战俘营与重逢。"],
"outline":["（通说待核——B098未载剧情）索科洛夫的自述：战俘、逃亡与领养孤儿。","（通说待核）'遭遇'：命运的清单与继续活下去。"],
"characters":[{"name":"索科洛夫","identity":"司机/老兵","note":"（通说待核，B098未载）"},{"name":"万尼亚","identity":"孤儿","note":"（通说待核，B098未载）"}],
"themes":["战争创伤的个人史（通说待核）。",
 "战俘的屈辱与尊严（通说待核）。",
 "领养：创伤后的救赎（通说待核）。"],
"influence":[{"text":"Britannica：肖洛霍夫1965诺贝尔文学奖（B098）。","source":"B098"},{"text":"Britannica：《静静的顿河》——'苏联最广泛阅读的小说'（B098 交叉）。","source":"B098"}],
"reading":{"difficulties":["卫国战争史。","第一人称战争叙事传统。"],
 "editions":["《一个人的遭遇》中译本（人民文学等——通说待核）。","俄文原版。"],
 "order":"肖洛霍夫短篇首选；与《静静的顿河》对读。"},
"pending":["索科洛夫/万尼亚人名核对（B098未载）。","1957年发表（《真理报》说）待核。","1959年电影改编说待核。"],
"sources":[S_SHO],"year_source":S_SHO,"author_source":S_SHO,"related_works":["jingjingdedunhe","tuyuzhizideneizi","laorenhai"],
"svg":G("《一个人的遭遇》创伤结构图",[{"title":"索科洛夫","text":"失去一切的士兵（通说）","color":"main"},{"title":"战俘营","text":"屈辱与尊严（通说）","color":"antagonist"},{"title":"万尼亚","text":"领养的救赎（通说）","color":"gold"},{"title":"遭遇","text":"命运清单（书名）","color":"family"}])},
# 2. 斯坦贝克《人鼠之间》
{"id":"renshuzhijian","title":"人鼠之间","original_title":"Of Mice and Men","region":"美国","era":"现当代","era_detail":"20世纪30年代",
"genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"steinbeck","author_name":"约翰·斯坦贝克",
"year_display":"1937年（作者页注记：Britannica——人鼠之间 (1937)）","year_sort":1937,
"background":["作者页注记：人鼠之间 (1937)——'短篇经典（Britannica）'。","Britannica：斯坦贝克——加州农业劳工书写传统（作者页语境——待核）。","题材（通说待核）：流动工人莱尼与乔治的'农场梦'与悲剧结局。"],
"outline":["（通说待核）两个流动工人的友谊：大块头莱尼与监护人乔治。","（通说待核）'驯兔的农场'梦与意外杀人。"],
"characters":[{"name":"莱尼","identity":"大力但智弱","note":"（通说待核）"},{"name":"乔治","identity":"同伴","note":"（通说待核）"}],
"themes":["流浪劳工的生存（通说待核）。",
 "'农场梦'的破灭（通说待核）。",
 "友谊与 mercy 杀（通说待核）。"],
"influence":[{"text":"Britannica：斯坦贝克1962诺奖（作者页语境——待核）。","source":S_ST},{"text":"Britannica：《愤怒的葡萄》作者级定位（作者页交叉）。","source":S_ST}],
"reading":{"difficulties":["大萧条加州农业史。","'小剧场'式的章节结构（通说待核）。"],
 "editions":["《人鼠之间》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"斯坦贝克入门首选；后接《愤怒的葡萄》《伊甸之东》。"},
"pending":["莱尼/乔治全名核对（通说）。","1937年出版（Covici-Friede说）待核。","与彭斯诗'To a Mouse'书名关系待核。"],
"sources":[S_ST],"year_source":S_ST,"author_source":S_ST,"related_works":["nuhuodeputao","yidianzhidong","jialinmeimei"],
"svg":G("《人鼠之间》农场梦图",[{"title":"莱尼","text":"柔软的大力（通说）","color":"main"},{"title":"乔治","text":"监护的承诺（通说）","color":"family"},{"title":"农场梦","text":"'驯兔'的乌托邦（通说）","color":"gold"},{"title":"结局","text":"梦的崩塌（通说）","color":"antagonist"}])},
# 3. 霍桑《七个尖角的阁楼》
{"id":"jianjiaogelou","title":"七个尖角的阁楼","original_title":"The House of the Seven Gables","region":"美国","era":"近代","era_detail":"19世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"hawthorne","author_name":"纳撒尼尔·霍桑",
"year_display":"1851年（作者页注记：Britannica 列举——七个尖角的阁楼 (1851)）","year_sort":1851,
"background":["作者页注记：七个尖角的阁楼 (1851)——'Britannica 列举'。","Britannica：霍桑——《红字》作者、罗曼司（romance）文体（作者页语境——待核）。","题材（通说待核）：品钦家族的老宅诅咒——巫审时代的遗产与现在的偿还。"],
"outline":["（通说待核）莫尔上校的诅咒与品钦家族的没落。","（通说待核）赫普齐芭与克利福德：老宅中的兄妹。"],
"characters":[{"name":"赫普齐芭","identity":"老宅居民","note":"（通说待核）"},{"name":"克利福德","identity":"受害者","note":"（通说待核）"}],
"themes":["祖辈之罪的遗传（通说待核）。",
 "老宅作为家族史的建筑（书名语境）。",
 "清教遗产的清算（霍桑作者级主题——通说待核）。"],
"influence":[{"text":"Britannica：霍桑美国罗曼司传统的代表（作者页语境——待核）。","source":S_HA},{"text":"Britannica：《红字》为代表作（作者页交叉）。","source":S_HA}],
"reading":{"difficulties":["塞勒姆巫审史。","罗曼司与小说的文体差异（霍桑自序——通说待核）。"],
 "editions":["《七个尖角的阁楼》中译名（《有七个尖角阁的房子》两说）待核。","英文原版（公有领域）。"],
 "order":"霍桑第二作；与《红字》对读。"},
"pending":["赫普齐芭/克利福德人名核对（通说）。","1851年出版（Ticknor & Fields说）待核。","'七个尖角'宅邸原型（特纳-英格索尔宅）待核。"],
"sources":[S_HA],"year_source":S_HA,"author_source":S_HA,"related_works":["hongzi","fushide","leiyu"],
"svg":G("《七个尖角的阁楼》诅咒结构图",[{"title":"老宅","text":"七个尖角（书名）","color":"family"},{"title":"诅咒","text":"巫审的遗产（通说）","color":"antagonist"},{"title":"兄妹","text":"宅中的幸存者（通说）","color":"main"},{"title":"偿还","text":"罪与时间的和解（通说）","color":"gold"}])},
# 4. 纪德《田园交响曲》
{"id":"tianyuanjiaoxiangqu","title":"田园交响曲","original_title":"La Symphonie pastorale","region":"法国","era":"近代","era_detail":"20世纪10年代末",
"genre":"中篇小说","genre_group":"小说","language":"法语","author_id":"gide","author_name":"安德烈·纪德",
"year_display":"1919年（作者页注记：Britannica——The Pastoral Symphony）","year_sort":1919,
"background":["作者页注记：田园交响曲——'Britannica：The Pastoral Symphony'。","Britannica（B275）：纪德——1947诺奖；《背德者》《窄门》为姊妹篇（作者页语境）。","题材（通说待核）：牧师日记——收养盲女热特吕德与'慈善'的自欺。"],
"outline":["（通说待核）牧师的日记体自白：以善之名的感情。","（通说待核）热特吕德复明后的幻灭。"],
"characters":[{"name":"牧师","identity":"日记叙述者","note":"（通说待核）"},{"name":"热特吕德","identity":"盲女","note":"（通说待核）"}],
"themes":["'慈善'的自欺（通说待核）。",
 "日记体的不可靠叙述（通说待核）。",
 "信仰与欲望（B275 纪德主题语境）。"],
"influence":[{"text":"Britannica：纪德1947诺奖（B275 交叉）。","source":S_GI},{"text":"Britannica：The Pastoral Symphony 列举（作者页注记）。","source":S_GI}],
"reading":{"difficulties":["日记体的双重声音。","新教牧师语境。"],
 "editions":["《田园交响曲》中译本（人民文学/上海译文等——通说待核）。","法文原版。"],
 "order":"纪德三部曲（《背德者》《窄门》本作）对读。"},
"pending":["热特吕德人名核对（通说）。","1919年出版细节待核。","日记日期结构待核。"],
"sources":[S_GI],"year_source":S_GI,"author_source":S_GI,"related_works":["beidechezhe","zhaimen","leiyu"],
"svg":G("《田园交响曲》自欺结构图",[{"title":"日记","text":"牧师的自我辩护（通说）","color":"main"},{"title":"盲女","text":"善的受托者（通说）","color":"gold"},{"title":"复明","text":"幻灭的开启（通说）","color":"antagonist"},{"title":"信仰","text":"与欲望的博弈（B275语境）","color":"family"}])},
# 5. 福克纳《押沙龙，押沙龙！》
{"id":"yalongshalong","title":"押沙龙，押沙龙！","original_title":"Absalom, Absalom!","region":"美国","era":"现当代","era_detail":"20世纪30年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"faulkner","author_name":"威廉·福克纳",
"year_display":"1936年（作者页注记：通说待核——Britannica 未载年份）","year_sort":1936,
"background":["作者页注记：押沙龙，押沙龙！——'（通说待核）'——Britannica 未载本作细节。","Britannica（B324）：福克纳1949诺奖；The Sound and the Fury——'radical technical experimentation'（交叉）。","题材（通说待核）：萨德本百年的兴衰——家族史的多重讲述。"],
"outline":["（通说待核）萨德本：从西印度到密西西比种植园的'宏伟设计'。","（通说待核）多重叙述者拼图：昆丁与洛斯的追述。"],
"characters":[{"name":"托马斯·萨德本","identity":"家族创建者","note":"（通说待核）"},{"name":"昆丁","identity":"讲述者之一","note":"（通说待核）"}],
"themes":["家族史的讲述政治（通说待核）。",
 "种族与血统的诅咒（通说待核）。",
 "南方历史的多声部（B324 约克纳帕塔法语境）。"],
"influence":[{"text":"Britannica：1949诺奖（B324）。","source":S_FA},{"text":"Britannica：'radical technical experimentation'（B324 交叉）。","source":S_FA}],
"reading":{"difficulties":["多重叙述嵌套。","美国南方种植园史。"],
 "editions":["《押沙龙，押沙龙！》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"福克纳进阶；与《喧哗与骚动》对读。"},
"pending":["1936年出版（Random House说）待核。","萨德本人名与情节细节核对（通说）。","圣经押沙龙原型的对应关系待核。"],
"sources":[S_FA],"year_source":S_FA,"author_source":S_FA,"related_works":["xuanhuayusaodong","kanbujian3","leiyu"],
"svg":G("《押沙龙，押沙龙！》讲述结构图",[{"title":"萨德本","text":"'宏伟设计'（通说）","color":"antagonist"},{"title":"多重讲述","text":"历史的拼图（通说）","color":"main"},{"title":"百年","text":"家族的兴衰（书名语境）","color":"gold"},{"title":"诅咒","text":"血统与种族（通说）","color":"family"}])},
# 6. 福楼拜《情感教育》
{"id":"qingganjiaoyu","title":"情感教育","original_title":"L'Éducation sentimentale","region":"法国","era":"近代","era_detail":"19世纪60年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"flaubert","author_name":"居斯塔夫·福楼拜",
"year_display":"1869年（作者页注记：Britannica 记'七月王朝史家的必读书'（per Georges Sorel——Britannica 转述））","year_sort":1869,
"background":["作者页注记：情感教育 (1869)——'七月王朝史家的必读书'（per Georges Sorel——Britannica 转述）。","Britannica（B-Bot）：福楼拜——'1857包法利夫人'（作者页语境——待核）。","题材（通说待核）：弗雷德里克·莫罗的浪漫教育与1848革命的时代幻灭。"],
"outline":["（通说待核）弗雷德里克与阿尔努夫人：延宕的爱情。","（通说待核）1848年革命的围观与幻灭。"],
"characters":[{"name":"弗雷德里克·莫罗","identity":"青年","note":"（通说待核）"},{"name":"阿尔努夫人","identity":"恋慕对象","note":"（通说待核）"}],
"themes":["'情感的教育'：延宕与空转（通说待核）。",
 "1848革命的时代画卷（Sorel 评语语境）。",
 "浪漫主义的祛魅（通说待核）。"],
"influence":[{"text":"Britannica：'七月王朝史家的必读书'（per Georges Sorel——作者页注记）。","source":S_FL},{"text":"Britannica：福楼拜为现代小说文体的奠基者（作者页语境——待核）。","source":S_FL}],
"reading":{"difficulties":["1848革命史。","'零度写作'的客观文体（通说待核）。"],
 "editions":["《情感教育》中译本（人民文学/上海译文等——通说待核）。","法文原版（公有领域）。"],
 "order":"福楼拜第二作；与《包法利夫人》对读。"},
"pending":["弗雷德里克/阿尔努人名核对（通说）。","1869年出版细节待核。","Sorel 评语原文出处待核。"],
"sources":[S_FL],"year_source":S_FL,"author_source":S_FL,"related_works":["baofalifuren","baofali","mengya"],
"svg":G("《情感教育》幻灭结构图",[{"title":"弗雷德里克","text":"延宕的一生（通说）","color":"main"},{"title":"1848","text":"革命的围观（Sorel评语语境）","color":"gold"},{"title":"阿尔努夫人","text":"不可得的爱（通说）","color":"antagonist"},{"title":"教育","text":"幻灭的课程（书名）","color":"family"}])},
# 7. 斯坦贝克《伊甸之东》
{"id":"yidianzhidong","title":"伊甸之东","original_title":"East of Eden","region":"美国","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"steinbeck","author_name":"约翰·斯坦贝克",
"year_display":"1952年（作者页注记：Britannica——伊甸之东 (1952)）","year_sort":1952,
"background":["作者页注记：伊甸之东 (1952)——'家族史诗（Britannica）'。","Britannica：斯坦贝克——1962诺奖（作者页语境——待核）。","题材（通说待核）：特拉斯克与汉密尔顿两家——该隐与亚伯的重演与'timshel'。"],
"outline":["（通说待核）加州萨利纳斯谷的两家三代。","（通说待核）该隐-亚伯原型的重演：善与恶的选择。"],
"characters":[{"name":"亚当·特拉斯克","identity":"农场主","note":"（通说待核）"},{"name":"凯茜","identity":"恶的化身","note":"（通说待核）"}],
"themes":["该隐与亚伯的重演（书名语境——通说待核）。",
 "'timshel'（'你可以'）：自由意志（通说待核）。",
 "家族史诗与加州土地（通说待核）。"],
"influence":[{"text":"Britannica：斯坦贝克代表作序列（作者页注记）。","source":S_ST},{"text":"Britannica：1962诺奖（作者页语境——待核）。","source":S_ST}],
"reading":{"difficulties":["双家族多代结构。","圣经原型（创世记4章）。"],
 "editions":["《伊甸之东》中译本（人民文学等——通说待核）。","英文原版。"],
 "order":"斯坦贝克收官；与《愤怒的葡萄》对读。"},
"pending":["亚当/凯茜人名核对（通说）。","1952年出版（Viking说）待核。","'timshel'译文细节待核。"],
"sources":[S_ST],"year_source":S_ST,"author_source":S_ST,"related_works":["nuhuodeputao","renshuzhijian","laorenhai"],
"svg":G("《伊甸之东》原型重演图",[{"title":"两家","text":"加州的史诗（通说）","color":"family"},{"title":"该隐与亚伯","text":"原型的重演（书名）","color":"gold"},{"title":"'timshel'","text":"'你可以'的选择（通说）","color":"main"},{"title":"凯茜","text":"恶的化身（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批37）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

if 'yigerendeyu' in created: link('sholokhov', 'yigerendeyu', '一个人的遭遇')
if 'renshuzhijian' in created: link('steinbeck', 'renshuzhijian', '人鼠之间')
if 'jianjiaogelou' in created: link('hawthorne', 'jianjiaogelou', '七个尖角的阁楼')
if 'tianyuanjiaoxiangqu' in created: link('gide', 'tianyuanjiaoxiangqu', '田园交响曲')
if 'yalongshalong' in created: link('faulkner', 'yalongshalong', '押沙龙')
if 'qingganjiaoyu' in created: link('flaubert', 'qingganjiaoyu', '情感教育')
if 'yidianzhidong' in created: link('steinbeck', 'yidianzhidong', '伊甸之东')
print('BATCH37 DONE')
