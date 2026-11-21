# -*- coding: utf-8 -*-
"""批35：零成本 8 部（B053/B137/B130/B150/B092 作者页注记 + 书名查重）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def find_work(aid, prefer=None):
    got = [p.stem for p in pathlib.Path('data/works').glob('*.json') if json.load(open(p, encoding='utf-8'))['author_id'] == aid]
    for pref in prefer or []:
        if pref in got: return pref
    return got[0] if got else None

def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

gmx = find_work('garcia-marquez', ['bainianduguo', 'bainian']) or 'leiyu'
ish = find_work('ishiguro', ['changriiliuheng', 'changrijiangliu']) or 'leiyu'
cam = find_work('camus', ['jumianren', 'juren']) or 'huoluan'
print('base works:', gmx, ish, cam)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 马尔克斯《一桩事先张扬的凶杀案》
{"id":"yizhuangxiongshaan","title":"一桩事先张扬的凶杀案","original_title":"Crónica de una muerte anunciada","region":"哥伦比亚","era":"现当代","era_detail":"20世纪80年代初",
"genre":"中篇小说","genre_group":"小说","language":"西班牙语","author_id":"garcia-marquez","author_name":"加西亚·马尔克斯",
"year_display":"1981年（作者页 B053 注记：Britannica 列举后期双璧之一）","year_sort":1981,
"background":["作者页（B053）注记：《霍乱时期的爱情（1985）、一桩事先张扬的凶杀案（1981）》——'后期双璧（Britannica 列举）'。","Britannica（B053）：马尔克斯——1982诺奖；'20世纪最伟大作家之一、与博尔赫斯并列最知名拉美作家'之评。","题材（通说待核）：全镇人人知晓却未能阻止的凶杀——宿命与集体共谋。"],
"outline":["（通说待核——B053未载剧情）被张扬的凶杀与事后的追述。","（通说待核）新娘、兄弟与受害者之间的一夜。"],
"characters":[{"name":"圣地亚哥·纳萨尔","identity":"受害者","note":"（通说待核，B053未载）"},{"name":"安赫拉·维卡里奥","identity":"新娘","note":"（通说待核，B053未载）"}],
"themes":["'事先张扬'：集体共谋的宿命（通说待核）。",
 "新闻式纪实的叙事（B053：记者出身语境）。",
 "荣誉杀人（通说待核）。"],
"influence":[{"text":"Britannica：1982年诺贝尔文学奖（B053）。","source":"B053"},{"text":"Britannica：'后期双璧'之注记（作者页 B053）。","source":"B053"}],
"reading":{"difficulties":["倒叙的 journalistic 结构。","加勒比海岸哥伦比亚（通说待核）。"],
 "editions":["《一桩事先张扬的凶杀案》中译本（南海出版公司等——通说待核）。","西班牙文原版。"],
 "order":"马尔克斯进阶；与《百年孤独》对读。"},
"pending":["人名核对（圣地亚哥·纳萨尔等——通说）。","1981年出版细节待核。","1987年电影改编说待核。"],
"sources":["B053"],"year_source":"B053","author_source":"B053","related_works":[gmx,"huoluan","ershoushijian"],
"svg":G("《一桩事先张扬的凶杀案》宿命结构图",[{"title":"张扬","text":"全镇皆知的秘密（通说）","color":"antagonist"},{"title":"凶杀","text":"宿命的完成（通说）","color":"main"},{"title":"追述","text":"记者式的还原（B053语境）","color":"gold"},{"title":"荣誉","text":"集体的共谋（通说）","color":"family"}])},
# 2. 马尔克斯《活着为了讲述》
{"id":"huozheweijiangshu","title":"活着为了讲述","original_title":"Vivir para contarla","region":"哥伦比亚","era":"现当代","era_detail":"21世纪初",
"genre":"回忆录","genre_group":"散文","language":"西班牙语","author_id":"garcia-marquez","author_name":"加西亚·马尔克斯",
"year_display":"2002年（Britannica B053：wrote a memoir about his first 30 years——回忆录第一卷）","year_sort":2002,
"background":["Britannica（B053）：'回忆录第一卷（Britannica：wrote a memoir about his first 30 years）'——关于其最初30年。","Britannica（B053）：马尔克斯 1927-03-06 阿拉卡塔卡生——外祖父乃'千日战争'上校；记者出身、巴黎驻外（作者页）。","题材（通说待核）：阿拉卡塔卡童年、记者生涯与《百年孤独》之前的世界。"],
"outline":["（通说待核——B053未载细节）从阿拉卡塔卡到作家的前30年。","（通说待核）外祖父的上校往事与'千日战争'。"],
"characters":[{"name":"马尔克斯","identity":"叙述者","note":"（B053 memoir 语境）"}],
"themes":["记忆与虚构的边界（通说待核）。",
 "《百年孤独》的前史（B053：马孔多原型语境）。",
 "记者的眼睛（B053：记者出身）。"],
"influence":[{"text":"Britannica：1982诺奖（B053）。","source":"B053"},{"text":"Britannica：'回忆录第一卷'（作者页 B053）。","source":"B053"}],
"reading":{"difficulties":["三部曲式的未完成结构（第一卷说）。","哥伦比亚政治史。"],
 "editions":["《活着为了讲述》中译本（南海出版公司等——通说待核）。","西班牙文原版。"],
 "order":"读罢《百年孤独》后的回溯。"},
"pending":["2002年出版细节待核。","'第一卷'后续计划待核。","外祖母的讲故事细节待核。"],
"sources":["B053"],"year_source":"B053","author_source":"B053","related_works":[gmx,"yizhuangxiongshaan","leiyu"],
"svg":G("《活着为了讲述》记忆结构图",[{"title":"阿拉卡塔卡","text":"童年的原型（B053）","color":"family"},{"title":"记者","text":"事实的眼睛（B053）","color":"gold"},{"title":"前30年","text":"回忆录第一卷（B053）","color":"main"},{"title":"讲述","text":"活着的目的（书名）","color":"antagonist"}])},
# 3. 黑塞《玻璃球游戏》
{"id":"boliuqiuyouxi","title":"玻璃球游戏","original_title":"Das Glasperlenspiel","region":"德国","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"hesse","author_name":"赫尔曼·黑塞",
"year_display":"1943年（Britannica B137：玻璃球游戏 (1943)）","year_sort":1943,
"background":["Britannica（B137）：《玻璃球游戏》(1943)——Britannica 列举。","Britannica（B137）：黑塞1946诺奖；主题——'个人挣脱既定文明寻找精神自我'。","Britannica（B137）：1960s-70s 英语青年崇拜。"],
"outline":["（通说待核——B137未载剧情）卡斯塔里亚学园与'玻璃球游戏'的极致精神游戏。","（通说待核）克乃希特的出走：精神游戏与现实的和解。"],
"characters":[{"name":"克乃希特","identity":"游戏大师","note":"（通说待核，B137未载）"},{"name":"约瑟夫","identity":"音乐导师","note":"（通说待核，B137未载）"}],
"themes":["'个人挣脱既定文明寻找精神自我'（B137）。",
 "精神游戏与责任的冲突（通说待核）。",
 "音乐与数学的综合（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：1946诺贝尔文学奖（B137）。","source":"B137"},{"text":"Britannica：1960s-70s 英语青年崇拜（B137）。","source":"B137"}],
"reading":{"difficulties":["虚构学园制度（卡斯塔里亚）。","三部传记+诗的框架。"],
 "editions":["《玻璃球游戏》中译本（上海译文等——通说待核）。","德文原版。"],
 "order":"黑塞收官之作；与《荒原狼》对读。"},
"pending":["克乃希特人名与结局核对（通说）。","1943年出版（两卷说）待核。","'卡斯塔里亚'细节待核。"],
"sources":["B137"],"year_source":"B137","author_source":"B137","related_works":["xinshigudeLieshou","demian","leiyu"],
"svg":G("《玻璃球游戏》精神游戏图",[{"title":"玻璃球游戏","text":"极致的精神综合（通说）","color":"gold"},{"title":"克乃希特","text":"游戏大师的出走（通说）","color":"main"},{"title":"卡斯塔里亚","text":"学园的围墙（通说）","color":"family"},{"title":"现实","text":"挣脱的召唤（B137）","color":"antagonist"}])},
# 4. 黑塞《德米安》
{"id":"demian","title":"德米安","original_title":"Demian","region":"德国","era":"近代","era_detail":"20世纪10年代末",
"genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"hesse","author_name":"赫尔曼·黑塞",
"year_display":"1919年（Britannica B137：德米安 (1919)）","year_sort":1919,
"background":["Britannica（B137）：德米安 (1919)——Britannica 列举。","Britannica（B137）：'荣格弟子心理分析影响《德米安》'。","Britannica（B137）：黑塞主题——'个人挣脱既定文明寻找精神自我'。"],
"outline":["（通说待核——B137未载剧情）辛克莱的少年世界：光明世界与黑暗世界的分裂。","（通说待核）德米安的引路：'该隐记号'与自我的觉醒。"],
"characters":[{"name":"辛克莱","identity":"少年","note":"（通说待核，B137未载）"},{"name":"德米安","identity":"引路人","note":"（B137 书名人物）"}],
"themes":["两个世界的分裂（通说待核）。",
 "荣格式心理分析的影响（B137）。",
 "'挣脱既定文明'的青春版（B137）。"],
"influence":[{"text":"Britannica：'荣格弟子心理分析影响'（B137）。","source":"B137"},{"text":"Britannica：1960s-70s 青年崇拜（B137 语境）。","source":"B137"}],
"reading":{"difficulties":["原型意象（该隐/阿布拉克萨斯——通说待核）。","一战前后的精神语境。"],
 "editions":["《德米安》中译本（人民文学/上海译文等——通说待核）。","德文原版。"],
 "order":"黑塞入门首选之一；先于《荒原狼》。"},
"pending":["辛克莱人名核对（B137未载）。","'辛克莱笔名'出版说（无政府主义者埃里希·玛丽亚·辛克莱化名说——通说）待核。","1919年出版细节待核。"],
"sources":["B137"],"year_source":"B137","author_source":"B137","related_works":["xinshigudeLieshou","bianxingji","boliuqiuyouxi"],
"svg":G("《德米安》觉醒结构图",[{"title":"光明世界","text":"家庭的庇护（通说）","color":"family"},{"title":"黑暗世界","text":"禁忌的引力（通说）","color":"antagonist"},{"title":"德米安","text":"引路者（B137）","color":"gold"},{"title":"觉醒","text":"'挣脱'的开始（B137）","color":"main"}])},
# 5. 石黑一雄《克拉拉与太阳》
{"id":"kelarayutaiyang","title":"克拉拉与太阳","original_title":"Klara and the Sun","region":"英国","era":"现当代","era_detail":"21世纪20年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"ishiguro","author_name":"石黑一雄",
"year_display":"2021年（Britannica B130：Klara and the Sun——科幻题材）","year_sort":2021,
"background":["Britannica（B130）：Klara and the Sun——'科幻题材（Britannica：Never Let Me Go, Klara and the Sun）'。","Britannica（B130）：石黑一雄2017诺奖——'uncovered the abyss beneath our illusory sense of connection with the world'；主题'记忆、悔恨、身份、不可靠叙述者'。","题材（通说待核）：人工智能'人工智能朋友'克拉拉观看世界与爱。"],
"outline":["（通说待核——B130未载剧情）机器人克拉拉与病弱少女乔西的陪伴。","（通说待核）太阳的疗愈神话：AF 的信仰。"],
"characters":[{"name":"克拉拉","identity":"人工智能朋友（AF）","note":"（B130 书名人物）"},{"name":"乔西","identity":"少女","note":"（通说待核，B130未载）"}],
"themes":["连接的幻觉（B130：illusory sense of connection）。",
 "爱的机器化（通说待核）。",
 "不可靠叙述者——机器之眼（B130 主题语系）。"],
"influence":[{"text":"Britannica：2017诺奖（B130）。","source":"B130"},{"text":"Britannica：'科幻题材'定位（B130）。","source":"B130"}],
"reading":{"difficulties":["机器人视点的语感。","基因定制社会（通说待核）。"],
 "editions":["《克拉拉与太阳》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"石黑一雄新读者首选；与《莫失莫忘》对读。"},
"pending":["乔西人名核对（B130未载）。","2021年出版（Faber说）待核。","'AF'术语细节待核。"],
"sources":["B130"],"year_source":"B130","author_source":"B130","related_works":[ish,"bianxingji","leiyu"],
"svg":G("《克拉拉与太阳》机器之眼图",[{"title":"克拉拉","text":"机器的凝视（B130）","color":"main"},{"title":"乔西","text":"被陪伴的少女（通说）","color":"family"},{"title":"太阳","text":"信仰的疗愈（通说）","color":"gold"},{"title":"连接","text":"幻觉与深渊（B130）","color":"antagonist"}])},
# 6. 莫里森《爵士》
{"id":"jueshi","title":"爵士","original_title":"Jazz","region":"美国","era":"现当代","era_detail":"20世纪90年代初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"morrison","author_name":"托妮·莫里森",
"year_display":"1992年（Britannica B150：爵士 (1992)）","year_sort":1992,
"background":["Britannica（B150）：爵士 (1992)——Britannica 列举。","Britannica（B150）：莫里森——'首位获诺贝尔文学奖的黑人女性（1993）'；1988普利策（宠儿）。","题材（通说待核）：1920年代哈莱姆——情杀与'爵士'节奏的叙述。"],
"outline":["（通说待核——B150未载剧情）维奥莱特与乔的婚姻裂痕、被杀的多卡斯。","（通说待核）叙述者作为'爵士乐'的即兴变奏。"],
"characters":[{"name":"乔","identity":"丈夫","note":"（通说待核，B150未载）"},{"name":"维奥莱特","identity":"妻子","note":"（通说待核，B150未载）"}],
"themes":["爵士乐结构与叙事（书名语境——通说待核）。",
 "大迁徙后的城市黑人生活（通说待核）。",
 "记忆与医疗式的叙述（B150 语境）。"],
"influence":[{"text":"Britannica：1993诺奖——首位黑人女性（B150）。","source":"B150"},{"text":"Britannica：1988普利策（宠儿）——本作为其后的城市篇（B150 交叉）。","source":"B150"}],
"reading":{"difficulties":["爵士乐的即兴叙事。","1920年代哈莱姆史。"],
 "editions":["《爵士》中译本（人民文学/南海等——通说待核）。","英文原版。"],
 "order":"莫里森进阶；与《宠儿》对读。"},
"pending":["乔/维奥莱特/多卡斯人名核对（B150未载）。","1992年出版（Knopf说）待核。","'三部曲'（《宠儿》《爵士》《天堂》）说法待核。"],
"sources":["B150"],"year_source":"B150","author_source":"B150","related_works":["chonger","suoluomanzhige","tuyuzhizideneizi"],
"svg":G("《爵士》即兴叙事图",[{"title":"爵士乐","text":"叙述的节奏（通说）","color":"gold"},{"title":"情杀","text":"三角的崩裂（通说）","color":"antagonist"},{"title":"哈莱姆","text":"大迁徙的城市（通说）","color":"family"},{"title":"叙述者","text":"即兴的变奏（通说）","color":"main"}])},
# 7. 莫里森《所罗门之歌》
{"id":"suoluomanzhige","title":"所罗门之歌","original_title":"Song of Solomon","region":"美国","era":"现当代","era_detail":"20世纪70年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"morrison","author_name":"托妮·莫里森",
"year_display":"1977年（Britannica B150：所罗门之歌 (1977)）","year_sort":1977,
"background":["Britannica（B150）：所罗门之歌 (1977)——Britannica 列举。","Britannica（B150）：莫里森——'首位获诺贝尔文学奖的黑人女性（1993）'；兰登书屋15年编辑。","题材（通说待核）：奶娃·戴德的家寻之旅——飞人所罗门的家神话。"],
"outline":["（通说待核——B150未载剧情）奶娃从密歇根到弗吉尼亚的寻根。","（通说待核）'飞人'传说与家族的名字史。"],
"characters":[{"name":"奶娃（Milkman）","identity":"主人公","note":"（通说待核，B150未载）"},{"name":"彼拉多","identity":"姑姑","note":"（通说待核，B150未载）"}],
"themes":["寻根与飞离（通说待核）。",
 "名字与家族史（通说待核）。",
 "黑人神话的再造（B150 语境）。"],
"influence":[{"text":"Britannica：1993诺奖（B150）。","source":"B150"},{"text":"Britannica：1977年全美书评界奖说待核（B150未载）。","source":"B150"}],
"reading":{"difficulties":["家族叙事的多代结构。","圣经与非洲 diaspora 意象。"],
 "editions":["《所罗门之歌》中译本（人民文学/南海等——通说待核）。","英文原版。"],
 "order":"莫里森中期首选；与《宠儿》对读。"},
"pending":["奶娃/彼拉多人名核对（B150未载）。","1977年出版（Knopf说）与获奖情况待核。","'飞人'传说的细节待核。"],
"sources":["B150"],"year_source":"B150","author_source":"B150","related_works":["chonger","jueshi","xiangtianhuhan"],
"svg":G("《所罗门之歌》寻根结构图",[{"title":"寻根","text":"南方之旅（通说）","color":"main"},{"title":"飞人","text":"家族的神话（通说）","color":"gold"},{"title":"名字","text":"戴德家的遗产（通说）","color":"family"},{"title":"飞离","text":"逃离与坠落（通说）","color":"antagonist"}])},
# 8. 加缪《堕落》
{"id":"duoluo","title":"堕落","original_title":"La Chute","region":"法国","era":"现当代","era_detail":"20世纪50年代",
"genre":"中篇小说","genre_group":"小说","language":"法语","author_id":"camus","author_name":"阿尔贝·加缪",
"year_display":"1956年（Britannica B092：堕落 (1956)——Britannica 列举）","year_sort":1956,
"background":["Britannica（B092）：La Chute (1956)——Britannica 列举（《局外人》《西西弗神话》《鼠疫》《反抗者》《堕落》）。","Britannica（B092）：加缪——'荒诞→反抗'主题；1957诺奖（44岁）；与萨特决裂。","题材（通说待核）：阿姆斯特丹酒吧的'法官-忏悔者'克拉芒斯的自白。"],
"outline":["（通说待核——B092未载剧情）克拉芒斯的独白：从巴黎律师到阿姆斯特丹的自我审判。","（通说待核）'第二人称'的忏悔：把每个人拖入共谋。"],
"characters":[{"name":"克拉芒斯","identity":"法官-忏悔者","note":"（通说待核，B092未载）"}],
"themes":["自白与审判（通说待核）。",
 "'荒诞→反抗'之后的人性暗面（B092 主题语境）。",
 "现代的无辜与罪（通说待核）。"],
"influence":[{"text":"Britannica：1957诺奖（B092）。","source":"B092"},{"text":"Britannica：'荒诞→反抗'主题（B092）。","source":"B092"}],
"reading":{"difficulties":["独白体的绕行结构。","存在主义语境（与萨特决裂——B092）。"],
 "editions":["《堕落》中译本（上海译文/人民文学等——通说待核）。","法文原版。"],
 "order":"加缪后期首选；与《局外人》对读。"},
"pending":["克拉芒斯人名核对（B092未载）。","1956年出版（Gallimard说）待核。","'审判者与忏悔者'细节待核。"],
"sources":["B092"],"year_source":"B092","author_source":"B092","related_works":[cam,"huoluan","fushide"],
"svg":G("《堕落》自白结构图",[{"title":"克拉芒斯","text":"法官-忏悔者（通说）","color":"main"},{"title":"自白","text":"审判他人即审判自身（通说）","color":"gold"},{"title":"阿姆斯特丹","text":"下坠的圈层（通说）","color":"family"},{"title":"荒诞→反抗","text":"加缪的主线（B092）","color":"antagonist"}])},
]
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批35）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

link('garcia-marquez', 'yizhuangxiongshaan', '一桩事先张扬')
link('garcia-marquez', 'huozheweijiangshu', '活着为了讲述')
link('hesse', 'boliuqiuyouxi', '玻璃球游戏')
link('hesse', 'demian', '德米安')
link('ishiguro', 'kelarayutaiyang', '克拉拉')
link('morrison', 'jueshi', '爵士')
link('morrison', 'suoluomanzhige', '所罗门之歌')
link('camus', 'duoluo', '堕落')
print('BATCH35 DONE')
