# -*- coding: utf-8 -*-
"""批82：零成本 10 部（耶路撒冷/历史/冬天的故事集/魔术师/苔依丝/新婚诗人的日记/自由或死亡/日落/图像诗/残篇?）"""
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
{"id":"jierusalem","title":"耶路撒冷","original_title":"Jerusalem: The Emanation of the Giant Albion","region":"英国","era":"近代","era_detail":"19世纪初",
"genre":"长诗（预言书）","genre_group":"诗歌","language":"英语","author_id":"blake","author_name":"威廉·布莱克",
"year_display":"1804-?20年（Britannica B397：Jerusalem (1804-?20)）","year_sort":1804,
"background":["Britannica（B397）：Jerusalem (1804-?20)——布莱克预言书之一（年份区间口径）。","Britannica（B397）：Milton 中的'Jerusalem'歌词——'which has become a kind of second national anthem in Britain'。","题材（通说待核）：'巨灵阿尔比恩'的分离与合一——预言书的收束。"],
"outline":["（通说待核——B397未载细节）阿尔比恩（英国）的'四大原力'分离与合一。","（通说待核）'耶路撒冷'：内在天国的降临。"],
"characters":[{"name":"阿尔比恩","identity":"巨灵/英国","note":"（通说待核）"}],
"themes":["'合一'的预言（通说待核）。",
 "'彩色印刷'的自印（B397 交叉）。",
 "'英国'的神话化（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：Milton 中'Jerusalem'歌词——'second national anthem'（B397 交叉）。","source":"B397"},{"text":"Britannica：预言书序列（B397 交叉）。","source":"B397"}],
"reading":{"difficulties":["'原力'（Zoas）体系。","自创神话的词汇。"],
 "editions":["《耶路撒冷》中译名（《耶路撒冷》）待核。","英文原版（公有领域）。"],
 "order":"布莱克预言书收官；先读《弥尔顿》。"},
"pending":["'1804-?20'年份口径核对（B397）。","'100版'彩色印刷细节待核（通说）。","'原力'体系待核（通说）。"],
"sources":["B397"],"year_source":"B397","author_source":"B397","related_works":["milaerdun","tianzhenyujiy","songge1819"],
"svg":G("《耶路撒冷》合一结构图",[{"title":"阿尔比恩","text":"巨灵的合一（通说）","color":"main"},{"title":"耶路撒冷","text":"内在的天国（书名）","color":"gold"},{"title":"分离","text":"'原力'的分裂（通说）","color":"antagonist"},{"title":"英国","text":"绿色的圣地（通说）","color":"family"}])},
{"id":"lishisimon","title":"历史","original_title":"Histoire","region":"法国","era":"近代","era_detail":"20世纪60年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"csimon","author_name":"克洛德·西蒙",
"year_display":"1967年（Britannica B391：Histoire (1967)——'循环四部'之一）","year_sort":1967,
"background":["Britannica（B391）：Histoire——与 La Route des Flandres/L'Herbe/La Palace 构成循环四部（人物事件反复）。","Britannica（B391）：风格——'lacking all punctuation and heavy with 1,000-word sentences'——'to capture the very progression of life'。","题材（通说待核）：'历史'与家族记忆：母亲的房产与旧照。"],
"outline":["（通说待核）'我'继承房产与父亲照片的'历史'。","（通说待核）'无标点'的记忆流（B391）。"],
"characters":[{"name":"'我'","identity":"继承人","note":"（通说待核）"}],
"themes":["'历史'：记忆与房产（书名语境——通说待核）。",
 "'千词长句'（B391）。",
 "循环四部的人物复现（B391）。"],
"influence":[{"text":"Britannica：'循环四部'之一（B391）。","source":"B391"},{"text":"Britannica：1985诺奖（B391 交叉）。","source":"B391"}],
"reading":{"difficulties":["'无标点'的长句。","家族照的解读。"],
 "editions":["《历史》中译名（《历史》）待核。","法文原版。"],
 "order":"西蒙循环四部之三。"},
"pending":["1967年出版细节待核。","'房产'细节核对（通说）。","'四部循环'结构核对（B391已载）。"],
"sources":["B391"],"year_source":"B391","author_source":"B391","related_works":["fulandegonglu","gudujisuozao","niuyuesanbuqu"],
"svg":G("《历史》记忆结构图",[{"title":"历史","text":"记忆的房产（书名）","color":"main"},{"title":"照片","text":"父的层理（通说）","color":"gold"},{"title":"长句","text":"'千词'的流（B391）","color":"antagonist"},{"title":"循环","text":"四部的复现（B391）","color":"family"}])},
{"id":"dongtiandegushiji","title":"冬天的故事集","original_title":"Winter's Tales","region":"丹麦","era":"近代","era_detail":"20世纪40年代",
"genre":"短篇小说集","genre_group":"故事集","language":"英语","author_id":"dinesen","author_name":"伊萨克·迪内森",
"year_display":"1942年（Britannica B388：Winter's Tales (1942; Vinter-eventyr)）","year_sort":1942,
"background":["Britannica（B388）：Winter's Tales——作品列表（与 Seven Gothic Tales 1934 并列）。","Britannica（B388）：迪内森——'highly polished narratives in the Romantic tradition'——'eros and dreams'。","题材（通说待核）：二战期间出版的'冬夜'故事集。"],
"outline":["（通说待核）'冬天的故事'：被占领丹麦的暗夜讲述。","（通说待核）'eros 与梦'的延续（B388）。"],
"characters":[{"name":"众讲述者","identity":"框架人物","note":"（通说待核）"}],
"themes":["'冬夜'的讲述（书名语境——通说待核）。",
 "'eros 与梦'（B388）。",
 "占领时代的寓言（通说待核）。"],
"influence":[{"text":"Britannica：Winter's Tales (1942)（B388）。","source":"B388"},{"text":"Britannica：'Romantic tradition'（B388 交叉）。","source":"B388"}],
"reading":{"difficulties":["'冬夜'的框架。","占领丹麦的语境（通说待核）。"],
 "editions":["《冬天的故事集》中译名（《冬天的故事》）待核。","英文原版。"],
 "order":"迪内森中期；与《七篇哥特故事》对读。"},
"pending":["篇目核对（B388未载）。","1942年出版细节待核。","'占领丹麦'影射待核。"],
"sources":["B388"],"year_source":"B388","author_source":"B388","related_works":["qipiangetegushi","zouchufeizhou","xiaoyinhewo"],
"svg":G("《冬天的故事集》冬夜讲述图",[{"title":"冬夜","text":"讲述的火光（书名）","color":"gold"},{"title":"故事","text":"'eros 与梦'（B388）","color":"main"},{"title":"占领","text":"暗夜的丹麦（通说）","color":"antagonist"},{"title":"浪漫","text":"'传统'的打磨（B388）","color":"family"}])},
{"id":"moshushi","title":"魔术师","original_title":"The Magus","region":"英国","era":"现当代","era_detail":"20世纪60年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"fowles","author_name":"约翰·福尔斯",
"year_display":"1965年（Britannica B399：The Magus (1965; revised ed. 1977; filmed 1968)——希腊海岛）","year_sort":1965,
"background":["Britannica（B399）：The Magus——'set on a Greek island, about an English schoolteacher who befriends a mysterious local man'（希腊海岛：英国教师结识神秘当地人）——修订版1977——电影1968。","Britannica（B399）：福尔斯——'combine psychological probings—chiefly of sex and love—with an interest in social and philosophical issues'。","题材（通说待核）：康奇斯的'上帝游戏'——心理'戏法'。"],
"outline":["（通说待核）尼古拉斯·厄菲与康奇斯的'游戏'：'神岛'的表演。","（通说待核）'魔术师'：心理'戏法'的导演。"],
"characters":[{"name":"康奇斯","identity":"'魔术师'","note":"（通说待核，B399未载）"},{"name":"尼古拉斯·厄菲","identity":"英国教师","note":"（通说待核）"}],
"themes":["'上帝游戏'的心理表演（通说待核）。",
 "海岛的'迷'（B399：mysterious local man）。",
 "'性与爱'的探询（B399）。"],
"influence":[{"text":"Britannica：'revised ed. 1977; filmed 1968'（B399）。","source":"B399"},{"text":"Britannica：'psychological probings'（B399）。","source":"B399"}],
"reading":{"difficulties":["'上帝游戏'的层。","希腊海岛的地理。"],
 "editions":["《魔术师》中译名（《魔法师》）待核。","英文原版。"],
 "order":"福尔斯第二作；与《法国中尉的女人》对读。"},
"pending":["康奇斯/厄菲人名核对（通说）。","1965年出版细节与1977修订版待核。","'上帝游戏'术语待核。"],
"sources":["B399"],"year_source":"B399","author_source":"B399","related_works":["faguozhongweidenvren","shoucangjia","moluoyi"],
"svg":G("《魔术师》上帝游戏图",[{"title":"康奇斯","text":"'魔术师'的导演（通说）","color":"gold"},{"title":"游戏","text":"心理的表演（通说）","color":"main"},{"title":"海岛","text":"希腊的舞台（B399）","color":"family"},{"title":"教师","text":"被考验的人（通说）","color":"antagonist"}])},
{"id":"taiyisi","title":"苔依丝","original_title":"Thaïs","region":"法国","era":"近代","era_detail":"19世纪90年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"france","author_name":"阿纳托尔·法朗士",
"year_display":"1890年（Britannica B392：Thaïs (1890)——作品列表）","year_sort":1890,
"background":["Britannica（B392）：Thaïs——作品列表（1890）。","Britannica（B392）：法朗士——1921诺奖；'古典的优雅'语境（作者级——通说待核）。","题材（通说待核）：修士帕夫努与亚历山大城名妓苔依丝——'拯救'的反讽。"],
"outline":["（通说待核）修士的'拯救'之旅：沙漠与亚历山大。","（通说待核）苔依丝的'忏悔'与修士的幻梦。"],
"characters":[{"name":"帕夫努","identity":"修士","note":"（通说待核）"},{"name":"苔依丝","identity":"名妓","note":"（B392 书名人物）"}],
"themes":["'拯救'的反讽（通说待核）。",
 "亚历山大的奢华（通说待核）。",
 "'灵'与'肉'的辩证（通说待核）。"],
"influence":[{"text":"Britannica：Thaïs (1890)（B392）。","source":"B392"},{"text":"Britannica：马斯奈歌剧 Thaïs（1894说）待核——不采。","source":"B392"}],
"reading":{"difficulties":["亚历山大城的宗教史。","'圣徒传'的反讽（通说待核）。"],
 "editions":["《苔依丝》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"法朗士早期；与《企鹅岛》对读。"},
"pending":["帕夫努/苔依丝人名核对（通说）。","1890年出版细节待核。","'沙漠'细节待核。"],
"sources":["B392"],"year_source":"B392","author_source":"B392","related_works":["qiedao","zhushenkele","xunjiexiaoshuo"],
"svg":G("《苔依丝》拯救反讽图",[{"title":"苔依丝","text":"名妓的忏悔（通说）","color":"main"},{"title":"修士","text":"'拯救'的反讽（通说）","color":"antagonist"},{"title":"亚历山大","text":"奢华之城（通说）","color":"gold"},{"title":"沙漠","text":"苦修的幻梦（通说）","color":"family"}])},
{"id":"xinhunshirenriji","title":"一个新婚诗人的日记","original_title":"Diario de un poeta recién casado","region":"西班牙","era":"近代","era_detail":"20世纪10年代末",
"genre":"日记体诗集","genre_group":"诗歌","language":"西班牙语","author_id":"jrjimenez","author_name":"胡安·拉蒙·希梅内斯",
"year_display":"1917年（Britannica B401：Diario de un poeta recién casado (1917)——1948年重刊为 Diario de un poeta y mar）","year_sort":1917,
"background":["Britannica（B401）：Diario de un poeta recién casado (1917)——1948年重刊为 Diario de un poeta y mar——'la poesía desnuda'（裸体诗）的转折——'remove all extraneous elements and write freer, purer verse without formal metres'。","Britannica（B401）：希梅内斯——1956诺奖。","题材（通说待核）：新婚航程（美-西）的日记——'海'的现代诗。"],
"outline":["（通说待核）'新婚'航程：纽约-加的斯的日记诗。","（通说待核）'裸体诗'的宣言实践（B401）。"],
"characters":[{"name":"诗人（'我'）","identity":"新婚航行者","note":"（B401 语境）"}],
"themes":["'裸体诗'的转折（B401：la poesía desnuda）。",
 "'海'的现代意象（重刊题名——B401）。",
 "婚姻与诗（通说待核）。"],
"influence":[{"text":"Britannica：'remove all extraneous elements...'（B401）。","source":"B401"},{"text":"Britannica：1956诺奖（B401 交叉）。","source":"B401"}],
"reading":{"difficulties":["日记诗的'裸'语体。","纽约现代主义接触（通说待核）。"],
 "editions":["《一个新婚诗人的日记》中译名（《一个新婚诗人的日记》）待核。","西班牙文原版（公有领域状态待核）。"],
 "order":"希梅内斯转折之作；与《小银和我》对读。"},
"pending":["1948年重刊题名核对（B401：Diario de un poeta y mar）。","1917年出版细节待核。","'纽约'段细节待核。"],
"sources":["B401"],"year_source":"B401","author_source":"B401","related_works":["xiaoyinhewo","chunjiuji","ezhihua"],
"svg":G("《新婚诗人的日记》裸诗结构图",[{"title":"日记","text":"航程的诗（书名）","color":"main"},{"title":"裸体诗","text":"'去掉多余要素'（B401）","color":"gold"},{"title":"海","text":"重刊的题名（B401）","color":"family"},{"title":"婚姻","text":"新婚的航行（通说）","color":"antagonist"}])},
{"id":"ziyouhuosiwang","title":"自由或死亡","original_title":"O Kapetán Mikhális","region":"希腊","era":"近代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"希腊语","author_id":"kazantzakis","author_name":"尼科斯·卡赞扎基斯",
"year_display":"1950年（Britannica B410：Freedom or Death (O Kapetán Mikhális, 1950)——'a depiction of Cretan Greeks' struggle against their Ottoman overlords in the 19th century'）","year_sort":1950,
"background":["Britannica（B410）：Freedom or Death——'a depiction of Cretan Greeks' struggle against their Ottoman overlords in the 19th century'（19世纪克里特希腊人反抗奥斯曼的斗争）。","Britannica（B410）：卡赞扎基斯——'a major contribution to modern Greek literature'。","题材（通说待核）：'米哈利斯队长'与祖父的家史——克里特起义。"],
"outline":["（通说待核）'队长米哈利斯'：义军与土耳其人的宿仇。","（通说待核）'自由或死亡'：克里特的座右铭。"],
"characters":[{"name":"米哈利斯队长","identity":"起义首领","note":"（B410 书名人物——O Kapetán Mikhális）"},{"name":"'爷爷'","identity":"叙述者的祖父","note":"（通说待核）"}],
"themes":["'自由或死亡'（书名语境——通说待核）。",
 "克里特反抗奥斯曼（B410）。",
 "家史与民族史（通说待核）。"],
"influence":[{"text":"Britannica：'a depiction of Cretan Greeks' struggle...'（B410）。","source":"B410"},{"text":"Britannica：'a major contribution to modern Greek literature'（B410 作者级）。","source":"B410"}],
"reading":{"difficulties":["克里特起义史（通说待核）。","'自由或死亡'口号。"],
 "editions":["《自由或死亡》中译名（《米哈利斯队长》）待核。","希腊文原版。"],
 "order":"卡赞扎基斯民族篇；与《希腊人左巴》对读。"},
"pending":["米哈利斯队长人名核对（B410书名希腊文）。","1950年出版细节待核。","'祖父'原型说待核。"],
"sources":["B410"],"year_source":"B410","author_source":"B410","related_works":["xilarenzuoba","jidudezuihouyouhuo","dulidemen"],
"svg":G("《自由或死亡》起义结构图",[{"title":"自由或死亡","text":"克里特的座右铭（书名）","color":"gold"},{"title":"米哈利斯队长","text":"起义的首领（B410）","color":"main"},{"title":"奥斯曼","text":"宗主的枷锁（B410）","color":"antagonist"},{"title":"家史","text":"祖父的讲述（通说）","color":"family"}])},
{"id":"riluo","title":"日落","original_title":"Закат（Sunset）","region":"俄国","era":"近代","era_detail":"20世纪20年代",
"genre":"戏剧","genre_group":"戏剧","language":"俄语","author_id":"babel","author_name":"伊萨克·巴别尔",
"year_display":"1927年（Britannica B402：Zakat (Sunset, 1927)——'his only successful stage play'，含 Benya Krik）","year_sort":1927,
"background":["Britannica（B402）：Zakat (Sunset, 1927)——'his only successful stage play, featuring Benya Krik'（唯一成功的舞台剧——含本亚·克里克）。","Britannica（B402）：巴别尔——'aphoristic precision...metaphoric extravagance'。","题材（通说待核）：本亚·克里克的'家庭'戏——摩尔多万卡的日与夜。"],
"outline":["（通说待核）克里克家：'王'的黄昏与长兄的接棒。","（通说待核）'日落'：敖德萨的黄昏意象（书名语境——通说待核）。"],
"characters":[{"name":"本亚·克里克","identity":"'王'","note":"（B402：Benya Krik——'a mock Jewish messiah'）"},{"name":"父亲","identity":"旧一代","note":"（通说待核）"}],
"themes":["'日落'：两代的交替（书名语境——通说待核）。",
 "'唯一成功的舞台剧'（B402）。",
 "敖德萨黑帮的剧场化（B402 交叉：Tales of Odessa）。"],
"influence":[{"text":"Britannica：'his only successful stage play'（B402）。","source":"B402"},{"text":"Britannica：'Benya Krik——mock Jewish messiah'（B402 交叉）。","source":"B402"}],
"reading":{"difficulties":["'敖德萨'方言。","'家庭戏'的权力。"],
 "editions":["《日落》中译名（《日落》）待核。","俄文原版。"],
 "order":"巴别尔戏剧首选；与《骑兵军》对读。"},
"pending":["1927年首演（Baku说）待核。","克里克家细节核对（通说）。","'唯一成功'口径核对（B402已载）。"],
"sources":["B402"],"year_source":"B402","author_source":"B402","related_works":["qibingjun","aodesagushi","wuhhaotuchang"],
"svg":G("《日落》两代交替图",[{"title":"日落","text":"敖德萨的黄昏（书名）","color":"gold"},{"title":"本亚","text":"'王'的接棒（B402）","color":"main"},{"title":"父亲","text":"旧代的余晖（通说）","color":"antagonist"},{"title":"舞台","text":"'唯一成功'（B402）","color":"family"}])},
{"id":"tuxiangshi","title":"图像诗","original_title":"Calligrammes","region":"法国","era":"近代","era_detail":"20世纪10年代末",
"genre":"诗集（视觉诗）","genre_group":"诗歌","language":"法语","author_id":"apollinaire","author_name":"纪尧姆·阿波利奈尔",
"year_display":"1918年（Britannica B403：Calligrammes (1918)——'dominated by images of war'——诗即图像）","year_sort":1918,
"background":["Britannica（B403）：Calligrammes——'dominated by images of war'（战争意象主导）——诗即图像（版式排布）。","Britannica（B403）：阿波利奈尔——1918年11月9日卒于巴黎（西班牙流感）。","题材（通说待核）：'丽丽的雨'《哭泣的姑娘》等——战争与'图像'诗。"],
"outline":["（通说待核）'图像诗'（calligram）：文字排布成'埃菲尔铁塔'等。","（通说待核）战争意象的主导（B403：dominated by images of war）。"],
"characters":[{"name":"诗人-画工","identity":"版式实验者","note":"（B403 语境）"}],
"themes":["'图像诗'：文字排布成图（B403：poems that are images via typographical arrangement）。",
 "战争意象（B403：dominated by images of war）。",
 "'视觉'与'听觉'（通说待核）。"],
"influence":[{"text":"Britannica：'poems that are images via typographical arrangement'（B403）。","source":"B403"},{"text":"Britannica：'dominated by images of war'（B403）。","source":"B403"}],
"reading":{"difficulties":["版式的'看'与'读'。","一战意象（通说待核）。"],
 "editions":["《图像诗》中译名（《画诗》）待核。","法文原版（公有领域状态待核）。"],
 "order":"阿波利奈尔收官；与《醇酒集》对读。"},
"pending":["篇目（《哭泣的姑娘》说——通说）核对。","1918年出版细节待核。","'calligram'术语核对。"],
"sources":["B403"],"year_source":"B403","author_source":"B403","related_works":["chunjiuji","balideyouyu","diyuzhiji"],
"svg":G("《图像诗》视觉结构图",[{"title":"图像","text":"诗即图像（B403）","color":"gold"},{"title":"战争","text":"意象的主导（B403）","color":"antagonist"},{"title":"版式","text":"文字的排布（B403）","color":"main"},{"title":"1918","text":"卒年之书（B403）","color":"family"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批82）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('jierusalem','blake','耶路撒冷'),('lishisimon','csimon','历史'),('dongtiandegushiji','dinesen','冬天的故事集'),('moshushi','fowles','魔术师'),('taiyisi','france','苔依丝'),('xinhunshirenriji','jrjimenez','一个新婚诗人的日记'),('ziyouhuosiwang','kazantzakis','自由或死亡'),('riluo','babel','日落'),('tuxiangshi','apollinaire','图像诗')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH82 DONE')
