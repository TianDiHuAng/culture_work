# -*- coding: utf-8 -*-
"""批66：零成本 8 部（埃克斯蓬托/大教堂里的爆炸/我们不能付钱/米斯特拉尔回忆录/故事集/生活的艺术/狂热者/蜜蜂...)"""
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
{"id":"ekesipengtuo","title":"埃克蓬托","original_title":"Ex Ponto","region":"南斯拉夫","era":"近代","era_detail":"20世纪10年代末",
"genre":"散文诗集","genre_group":"散文","language":"塞尔维亚-克罗地亚语","author_id":"andric","author_name":"伊沃·安德里奇",
"year_display":"1918年（Britannica B376：Ex Ponto (1918)——'a contemplative, lyrical prose work written during his internment by Austro-Hungarian authorities'）","year_sort":1918,
"background":["Britannica（B376）：Ex Ponto——'a contemplative, lyrical prose work written during his internment by Austro-Hungarian authorities'（一战奥匈拘禁期的沉思散文）。","Britannica（B376）：'His works are written soberly, in language of great beauty and purity.'","题材（通说待核）：拘禁期的信札式散文——母亲的祈祷与'波'的意象。"],
"outline":["（通说待核）拘禁中的信札：致母亲与故人。","（通说待核）'埃克蓬托'：海之外的罗马地名（通说待核）。"],
"characters":[{"name":"拘禁者'我'","identity":"写信人","note":"（B376 语境）"}],
"themes":["拘禁的沉思（B376：contemplative, lyrical）。",
 "'优美纯净的语言'（B376）。",
 "母与海的意象（通说待核）。"],
"influence":[{"text":"Britannica：'a contemplative, lyrical prose work'（B376）。","source":"B376"},{"text":"Britannica：1961诺奖（B376 交叉）。","source":"B376"}],
"reading":{"difficulties":["信札散文的文体。","一战拘禁史。"],
 "editions":["《埃克蓬托》中译名（《异乡人》）待核。","塞尔维亚-克罗地亚语原版（公有领域）。"],
 "order":"安德里奇起点；与《德里纳河上的桥》对读。"},
"pending":["'埃克蓬托'地名含义核对（通说）。","1918年出版细节待核。","信札收件人核对（通说）。"],
"sources":["B376"],"year_source":"B376","author_source":"B376","related_works":["derinahe","telafunikejishi","moluoyi"],
"svg":G("《埃克蓬托》拘禁沉思图",[{"title":"拘禁","text":"一战的海岸（B376）","color":"antagonist"},{"title":"信札","text":"沉思的散文（B376）","color":"main"},{"title":"母亲","text":"祈祷的远方（通说）","color":"gold"},{"title":"纯净","text":"'优美'的语言（B376）","color":"family"}])},
{"id":"datangtangdelibaozha","title":"大教堂里的爆炸","original_title":"El siglo de las luces","region":"古巴","era":"近代","era_detail":"20世纪60年代",
"genre":"历史小说","genre_group":"小说","language":"西班牙语","author_id":"carpentier","author_name":"阿莱霍·卡彭铁尔",
"year_display":"1962年（作者页注记：Britannica——Explosion in a Cathedral (1962)——历史小说——'prompted Nobel Prize calls that never materialized'）","year_sort":1962,
"background":["作者页注记：大教堂里的爆炸——'（Britannica：Explosion in a Cathedral (1962)——历史小说 on the French Revolution's impact on the Caribbean——'prompted Nobel Prize calls that never materialized'）'。","Britannica（B373）：卡彭铁尔——'marvelous American reality'。","题材（通说待核）：加勒比与法国大革命——'启蒙的世纪'的爆炸。"],
"outline":["（通说待核）哈瓦那三姐弟与维克多·于格斯的远征。","（通说待核）'启蒙'的火与大教堂的爆炸。"],
"characters":[{"name":"维克多·于格斯","identity":"法国使节","note":"（通说待核）"},{"name":"索菲亚","identity":"姐姐","note":"（通说待核）"}],
"themes":["法国大革命冲击加勒比（B注记）。",
 "'启蒙的世纪'的反讽（书名直译——通说待核）。",
 "历史与'神奇'（B373 交叉）。"],
"influence":[{"text":"Britannica：'prompted Nobel Prize calls'（作者页注记）。","source":"B373"},{"text":"Britannica：魔幻现实主义定位（B373 交叉）。","source":"B373"}],
"reading":{"difficulties":["加勒比革命史。","'巴洛克'句法（通说待核）。"],
 "editions":["《大教堂里的爆炸》中译名（《启蒙世纪》）待核。","西班牙文原版。"],
 "order":"卡彭铁尔历史篇；与《这个世界的王国》对读。"},
"pending":["于格斯/索菲亚人名核对（通说）。","1962年出版细节待核。","'诺奖呼声'说核对（作者页注记）。"],
"sources":["B373"],"year_source":"B373","author_source":"B373","related_works":["zhegeshijiedewanguo","xiaoyindejiti","sangeshouqiangshou"],
"svg":G("《大教堂里的爆炸》革命火种图",[{"title":"爆炸","text":"启蒙的火（书名）","color":"antagonist"},{"title":"加勒比","text":"革命的航路（通说）","color":"main"},{"title":"于格斯","text":"远征的使节（通说）","color":"gold"},{"title":"巴洛克","text":"句法的火药（通说）","color":"family"}])},
{"id":"wumenbuzhifu","title":"我们不能付钱？我们不付！","original_title":"Non si paga, non si paga!","region":"意大利","era":"近代","era_detail":"20世纪70年代",
"genre":"戏剧","genre_group":"戏剧","language":"意大利语","author_id":"dariofo","author_name":"达里奥·福",
"year_display":"1974年（Britannica B383：We Can't Pay? We Won't Pay! (Non si paga, non si paga!)）","year_sort":1974,
"background":["Britannica（B383）：We Can't Pay? We Won't Pay! (1974)——剧作列表。","Britannica（B383）：福——'a theatrical caricaturist with a flair for social agitation'。","题材（通说待核）：物价暴涨的'自助'超市——两个主妇的'掏空'与藏匿。"],
"outline":["（通说待核）'不付钱'的超市行动与藏匿的 goods。","（通说待核）警察的搜寻与'怀孕'的假肚。"],
"characters":[{"name":"安东尼娅","identity":"主妇","note":"（通说待核，B383未载）"},{"name":"乔瓦娜","identity":"主妇","note":"（通说待核）"}],
"themes":["'不付钱'的抗议（书名语境——通说待核）。",
 "物价与家庭（通说待核）。",
 "commedia dell'arte 的当代（B383 交叉）。"],
"influence":[{"text":"Britannica：We Can't Pay? We Won't Pay! (1974)（B383）。","source":"B383"},{"text":"Britannica：1997诺奖（B383 交叉）。","source":"B383"}],
"reading":{"difficulties":["闹剧的节奏。","1970年代意大利物价。"],
 "editions":["《我们不能付钱？我们不付！》中译名（《拒不付账》）待核。","意大利文原版。"],
 "order":"达里奥·福喜剧首选；与《意外死亡》对读。"},
"pending":["安东尼娅/乔瓦娜人名核对（通说）。","1974年首演细节待核。","'自助'超市细节待核。"],
"sources":["B383"],"year_source":"B383","author_source":"B383","related_works":["yigewuzhengfuzhisi","huajishenmiju","richu"],
"svg":G("《我们不付钱》超市抗议图",[{"title":"不付钱","text":"物价的反抗（书名）","color":"gold"},{"title":"主妇","text":"藏匿的肚子（通说）","color":"main"},{"title":"警察","text":"搜查的闹剧（通说）","color":"antagonist"},{"title":"超市","text":"'自助'的反转（通说）","color":"family"}])},
{"id":"misitelanghuiyilu","title":"米斯特拉尔回忆录","original_title":"Moun espelido（Mes origines）","region":"法国","era":"近代","era_detail":"20世纪初",
"genre":"回忆录","genre_group":"散文","language":"奥克语（普罗旺斯语）","author_id":"fmistral","author_name":"弗雷德里克·米斯特拉尔",
"year_display":"1906年（Britannica B362：Moun espelido（Mes origines, 1906; Memoirs of Mistral）——'his best-known work'）","year_sort":1906,
"background":["Britannica（B362）：Moun espelido——'his best-known work'（其最知名之作）。","Britannica（B362）：米斯特拉尔——1904诺奖；Félibrige 创始人。","题材（通说待核）：'我的镜子'（Moun espelido 直译）——童年、Félibrige 与语志业。"],
"outline":["（通说待核）'我的镜子'：马亚纳的童年与语言觉醒。","（通说待核）'Félibrige'七人组（通说待核）。"],
"characters":[{"name":"米斯特拉尔","identity":"回忆者","note":"（B362 语境）"}],
"themes":["'我的镜子'（书名直译——通说待核）。",
 "语言复兴的自述（B362：Félibrige）。",
 "诺奖资金的博物馆（B362 交叉）。"],
"influence":[{"text":"Britannica：'his best-known work'（B362）。","source":"B362"},{"text":"Britannica：1904诺奖（B362 交叉）。","source":"B362"}],
"reading":{"difficulties":["奥克语自述（读译本）。","'Félibrige'的史。"],
 "editions":["《米斯特拉尔回忆录》中译名（《我的出身》）待核。","奥克语原版（公有领域）。"],
 "order":"米斯特拉尔自传；与《米蕾伊》对读。"},
"pending":["'Moun espelido'直译（我的镜子）核对。","1906年出版细节待核。","'七人组'细节待核。"],
"sources":["B362"],"year_source":"B362","author_source":"B362","related_works":["mileiyi","luonhezhege","yigenanzhidewei"],
"svg":G("《米斯特拉尔回忆录》镜子结构图",[{"title":"镜子","text":"'我的出身'（书名）","color":"gold"},{"title":"马亚纳","text":"童年的村（B362）","color":"main"},{"title":"Félibrige","text":"复兴的社团（B362）","color":"family"},{"title":"语言","text":"普罗旺斯的业（B362）","color":"antagonist"}])},
{"id":"gushiji","title":"故事集","original_title":"Racconti","region":"意大利","era":"近代","era_detail":"20世纪60年代（死后出版）",
"genre":"短篇集（死后）","genre_group":"故事集","language":"意大利语","author_id":"lampedusa","author_name":"朱塞佩·托马西·迪·兰佩杜萨",
"year_display":"1961年（Britannica B349：Racconti ('Stories', 1961, posthumous)——含未完成长篇首章与自传短篇——部分译为 Two Stories and a Memory (1962)）","year_sort":1961,
"background":["Britannica（B349）：Racconti (1961, posthumous)——'includes an unfinished novel's first chapter and a short memoir'——部分译为 Two Stories and a Memory (1962)。","Britannica（B349）：兰佩杜萨——《豹》作者——'only completed novel'。","题材（通说待核）：《利高雷塔》与《教授与美人鱼》等——猫与孤儿的短篇。"],
"outline":["（通说待核）《利高雷塔》：小孤儿与黑猫的故事。","（通说待核）未完成长篇的首章（I gioielli说——通说待核）。"],
"characters":[{"name":"利高雷塔","identity":"黑猫","note":"（通说待核）"},{"name":"孤女","identity":"短篇主角","note":"（通说待核）"}],
"themes":["'死后出版'的遗珠（B349）。",
 "猫与孤儿的寓言（通说待核）。",
 "西西里的挽歌（B349 语境）。"],
"influence":[{"text":"Britannica：Racconti (1961, posthumous)（B349）。","source":"B349"},{"text":"Britannica：《豹》为'only completed novel'（B349 交叉）。","source":"B349"}],
"reading":{"difficulties":["遗稿的编定。","'猫'的寓言调子。"],
 "editions":["《故事集》中译名（《兰佩杜萨短篇集》）待核。","意大利文原版。"],
 "order":"《豹》后的补篇。"},
"pending":["篇目（利高雷塔/教授与美人鱼说）核对（通说）。","1961年出版（Feltrinelli说）待核。","未完成长篇名待核。"],
"sources":["B349"],"year_source":"B349","author_source":"B349","related_works":["bao","mingnuzhuan","xinnuofusuobaken"],
"svg":G("《故事集》遗珠结构图",[{"title":"遗珠","text":"死后的出版（B349）","color":"gold"},{"title":"利高雷塔","text":"猫的寓言（通说）","color":"main"},{"title":"孤儿","text":"短篇的孩子（通说）","color":"family"},{"title":"西西里","text":"挽歌的调子（B349语境）","color":"antagonist"}])},
{"id":"shenghuodedesu","title":"生活的艺术","original_title":"The Importance of Living","region":"中国","era":"近代","era_detail":"20世纪30年代",
"genre":"文化论著","genre_group":"散文","language":"英语","author_id":"linyutang","author_name":"林语堂",
"year_display":"1937年（作者页注记：Britannica——生活的艺术 (1937)——'英文中国介绍'）","year_sort":1937,
"background":["作者页注记：生活的艺术 (1937)——'英文中国介绍（Britannica）'（与《吾国与吾民》1935 并列）。","Britannica：林语堂——向西方介绍中国的作家（作者页语境）。","题材（通说待核）：'闲适哲学'——躺椅、茶与烟的'生活的艺术'。"],
"outline":["（通说待核）'醒觉'与'人类的快乐'诸章。","（通说待核）'闲适'与'玩物'的辩护。"],
"characters":[{"name":"（文化论著无人物）","identity":"——","note":"文化随笔"}],
"themes":["'闲适哲学'（通说待核）。",
 "'英文中国介绍'（B注记）。",
 "茶、烟与躺椅的仪式（通说待核）。"],
"influence":[{"text":"Britannica：'英文中国介绍'（作者页注记）。","source":src_of('linyutang')},{"text":"Britannica：林语堂《吾国与吾民》（作者页交叉）。","source":src_of('linyutang')}],
"reading":{"difficulties":["英文的'闲适'语体。","中国生活细节的英译。"],
 "editions":["《生活的艺术》（湖南文艺等——通说待核）。","1937年Reynal & Hitchcock说待核。"],
 "order":"林语堂英文第二作；与《吾国与吾民》对读。"},
"pending":["1937年出版细节待核。","章节结构核对（通说）。","'美国畅销榜'说（通说）待核。"],
"sources":[src_of('linyutang')],"year_source":src_of('linyutang'),"author_source":src_of('linyutang'),"related_works":["wuguoyuwumin","gududemigong","rensheng"],
"svg":G("《生活的艺术》闲适结构图",[{"title":"闲适","text":"生活的哲学（书名）","color":"gold"},{"title":"茶与烟","text":"日常的仪式（通说）","color":"main"},{"title":"英文","text":"世界的读者（B注记）","color":"family"},{"title":"躺椅","text":"'快活'的姿势（通说）","color":"antagonist"}])},
{"id":"kuangrezhe","title":"狂热者","original_title":"Die Schwärmer","region":"奥地利","era":"近代","era_detail":"20世纪20年代初",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"musil","author_name":"罗伯特·穆齐尔",
"year_display":"1920年（Britannica B353：Die Schwärmer (1920; The Enthusiasts)——'were performed in Berlin and Vienna'——中译名待核）","year_sort":1920,
"background":["Britannica（B353）：Die Schwärmer——'a play'——'were performed in Berlin and Vienna'（柏林维也纳上演）。","Britannica（B353）：穆齐尔——'monumental unfinished novel'（《没有个性的人》）作者（交叉）。","题材（通说待核）：'狂热者'的对话剧——理性与狂热的舞台实验。"],
"outline":["（通说待核）'对话体'的舞台：理性与激情的辩者。","（通说待核）'狂热者'的群像（人物通说待核）。"],
"characters":[{"name":"辩者群像","identity":"——","note":"（通说待核，B353未载）"}],
"themes":["'狂热'与理性（书名语境——通说待核）。",
 "对话剧的形式（B353：a play）。",
 "《没有个性的人》的前奏（B353 交叉）。"],
"influence":[{"text":"Britannica：'were performed in Berlin and Vienna'（B353）。","source":"B353"},{"text":"Britannica：穆齐尔巨著（B353 交叉）。","source":"B353"}],
"reading":{"difficulties":["对话剧的抽象。","维也纳文化圈（通说待核）。"],
 "editions":["《狂热者》中译名（《狂热者们》）待核。","德文原版（公有领域状态待核）。"],
 "order":"穆齐尔戏剧侧写；与《没有个性的人》对读。"},
"pending":["1920年上演细节待核。","人物与结构核对（通说）。","中译名两说待核。"],
"sources":["B353"],"year_source":"B353","author_source":"B353","related_works":["meiyougexingderen","zenodeyishi","shengriwanhui"],
"svg":G("《狂热者》对话结构图",[{"title":"狂热","text":"理性的舞台（书名）","color":"gold"},{"title":"对话剧","text":"辩者的群像（通说）","color":"main"},{"title":"柏林维也纳","text":"上演的城市（B353）","color":"family"},{"title":"前奏","text":"巨著的预演（B353交叉）","color":"antagonist"}])},
{"id":"ganbugou","title":"干谷","original_title":"干谷","region":"中国","era":"近代","era_detail":"20世纪30年代",
"genre":"短篇小说","genre_group":"小说","language":"汉语","author_id":"shencongwen","author_name":"沈从文",
"year_display":"作者页注记：Britannica 语境（湘西短篇——年份通说待核）","year_sort":1930,
"background":["作者页注记：干谷——'（Britannica 语境——湘西短篇）'——篇目口径待核。","Britannica：沈从文——京派小说家（作者页语境）。","题材（通说待核）：湘西的少女与隐士——'干谷'的静与火。"],
"outline":["（通说待核）干谷的隐居者与白耳一族。","（通说待核）'火'与'静'的湘西辩证。"],
"characters":[{"name":"幺幺","identity":"少女","note":"（通说待核）"},{"name":"隐士","identity":"谷中人","note":"（通说待核）"}],
"themes":["湘西的'干谷'（书名语境——通说待核）。",
 "少女与隐士（通说待核）。",
 "'水'与'火'的意象（通说待核）。"],
"influence":[{"text":"Britannica：沈从文短篇传统（作者页语境——待核）。","source":src_of('shencongwen')},{"text":"Britannica：《边城》为代表作（作者页交叉）。","source":src_of('shencongwen')}],
"reading":{"difficulties":["湘西口语与文言的混合。","'干谷'的地名虚构。"],
 "editions":["《干谷》（人民文学出版社《沈从文全集》等——通说待核）。","1930年代刊物发表说待核。"],
 "order":"沈从文短篇侧选；与《边城》对读。"},
"pending":["篇目归属核对（'干谷'是否为沈作——通说待核）。","发表年份与刊物待核。","人物名核对（通说）。"],
"sources":[src_of('shencongwen')],"year_source":src_of('shencongwen'),"author_source":src_of('shencongwen'),"related_works":["biancheng","bianshanchi","nongmin"],
"svg":G("《干谷》湘西辩证图",[{"title":"干谷","text":"静的谷（书名）","color":"gold"},{"title":"少女","text":"火的注视（通说）","color":"main"},{"title":"隐士","text":"谷中的时代（通说）","color":"family"},{"title":"湘西","text":"水的世界（作者页语境）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批66）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('ekesipengtuo','andric','埃克蓬托'),('datangtangdelibaozha','carpentier','大教堂里的爆炸'),('wumenbuzhifu','dariofo','我们不能付钱'),('misitelanghuiyilu','fmistral','米斯特拉尔回忆录'),('gushiji','lampedusa','故事集'),('shenghuodedesu','linyutang','生活的艺术'),('kuangrezhe','musil','狂热者'),('ganbugou','shencongwen','干谷')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH66 DONE')
