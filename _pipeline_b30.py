# -*- coding: utf-8 -*-
"""批30：Britannica 新核 3 作家 4 部（洛尔卡x2/穆西尔/夸西莫多 B353-B355）"""
import json, pathlib

newsrc = [
{"id":"B353","title":"Robert Musil — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Robert-Musil","type":"百科全书","verified":True,"covers":["musil","meiyougexingderen"],"note":"2026-11-21 核对：1880-11-06奥地利克拉根福生—1942-04-15日内瓦卒（61岁）；'Austrian-German novelist, best known for his monumental unfinished novel'——Der Mann ohne Eigenschaften（没有个性的人, 1930-43）——1924年开始——'a witty and urbane view of life in the glittering world of the Austro-Hungarian Empire, told from the viewpoint of Ulrich, a fictionalized Musil'（机智而摩登地看奥匈帝国的浮华世界，叙述者为乌尔里希——虚构的穆西尔）；第一部1930年出版、第二部部分1933年、'a remaining portion was published posthumously in 1943'；剧作 Die Schwärmer (1920)、Vinzenz (1924)——柏林维也纳上演；1908柏林大学博士；一战奥军服役；1938年纳粹吞并后逃瑞士"},
{"id":"B354","title":"Salvatore Quasimodo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Salvatore-Quasimodo","type":"百科全书","verified":True,"covers":["quasimodo","shunxijiandeyewan"],"note":"2026-11-21 核对：1901-08-20西西里Modica生（铁路职工之子）—1968-06-14那不勒斯卒（66岁）；1959诺贝尔文学奖；'Originally a leader of the Hermetic poets, he became, after World War II, a powerful poet commenting on modern social issues.'；师从翁加雷蒂与蒙塔莱起步；1930年代'the dry, sophisticated style and abstruse symbolism of Hermeticism'；隐逸期终于 Poesie (1938) 与 Ed è subito sera (1942; And Suddenly Its Evening)；Acque e terre (1930)、Oboe sommerso (1932)、Odore di eucalyptus (1933)、Erato e Apollion (1936)；战后 Giorno dopo giorno (1947)——'Many of his poems recalled the injustices of the fascist regime, the horrors of the war, and Italian guilt.'——'simple in language, exhibit a concrete and immediate imagery'；La terra impareggiabile (1958) 题词——'I say that the dead slay the living'（埃斯库罗斯）；译希腊抒情诗 (1940)、希腊悲剧家 (1963)、卡图卢斯/奥维德/维吉尔、莎剧六种、莫里哀《答尔丢夫》、E.E.卡明斯与聂鲁达"},
{"id":"B355","title":"Federico Garcia Lorca — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Federico-Garcia-Lorca","type":"百科全书","verified":True,"covers":["lorca","jipusaiyaoqu"],"note":"2026-11-21 核对：1898-06-05格拉纳达省Fuente Vaqueros生—1936-08-18/19格拉纳达省Víznar与Alfacar之间卒（38岁）；1936-08-16被国民军逮捕、未经审判——'driven to a remote hillside outside town and shot'（国民军'abhorred his homosexuality and his liberal views'）；'the most important Spanish poet and playwright of the 20th century'——开启了西班牙戏剧'second Golden Age'；Romancero gitano（吉普赛谣曲, 1921-27写/1928出版）——18首谣曲——'sold out within a year; many readers mistook Lorca for a Gypsy'；Bodas de sangre（血婚, 1933）、Yerma (1934)、La casa de Bernarda Alba (1936)；Poet in New York——1929-30纽约古巴之行；1927纪year与阿尔贝蒂/希伦/萨利纳斯等纪念贡戈拉逝世300周年——此后被称'Generation of 1927'；Llanto por Ignacio Sánchez Mejías (1935)——悼斗牛士"},
]
raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in newsrc:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
srcs = json.load(open('sources.json', encoding='utf-8'))
have = {s['id'] for s in srcs}
srcs.extend(s for s in newsrc if s['id'] not in have)
pathlib.Path('sources.json').write_text(json.dumps(srcs, ensure_ascii=False, indent=1), encoding='utf-8')
print('sources:', len(srcs))

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
def rid(*cands):
    for c in cands:
        if c and c in existing: return c
    return 'leiyu'

rel_yao = [rid('diyuzhiji'), rid('ershisou'), rid('huangliang')]
rel_xh = [rid('jipusaiyaoqu'), rid('yuwanghaojieche'), rid('leiyu')]
rel_mg = [rid('zenodeyishi'), rid('yigewushiwan'), rid('fushide')]
rel_qs = [rid('wuguigu'), rid('diyuzhiji'), rid('ezhihua')]
print('rel:', rel_yao, rel_xh, rel_mg, rel_qs)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"lorca","name":"费德里科·加西亚·洛尔卡","foreign_name":"Federico García Lorca（费德里科·加西亚·洛尔卡，1898-06-05—1936-08-18/19）","country":"西班牙","birth":1898,"death":1936,"birth_year":1898,"death_year":1936,"era":"近代",
"summary":"洛尔卡，格拉纳达省Fuente Vaqueros生，西班牙诗人与剧作家——'the most important Spanish poet and playwright of the 20th century'（20世纪最重要的西班牙诗人与剧作家——B355），开启了西班牙戏剧'second Golden Age'（B355）。Romancero gitano（吉普赛谣曲, 1928）——18首谣曲，'sold out within a year; many readers mistook Lorca for a Gypsy'（B355）。Bodas de sangre（血婚, 1933）、Yerma (1934)、La casa de Bernarda Alba (1936)（B355）。1927年与阿尔贝蒂等纪念贡戈拉逝世300周年——'Generation of 1927'（B355）。1936年8月16日被国民军逮捕、未经审判——'driven to a remote hillside outside town and shot'（B355）——国民军'abhorred his homosexuality and his liberal views'（B355）。",
"timeline":[
 {"year":1898,"text":"6月5日生于格拉纳达省Fuente Vaqueros（B355）。","src":"B355"},
 {"year":1928,"text":"Romancero gitano——18首谣曲，一年内售罄（B355）。","src":"B355"},
 {"year":1933,"text":"Bodas de sangre（血婚）（B355）。","src":"B355"},
 {"year":1936,"text":"8月16日被捕，18/19日在Víznar与Alfacar之间被枪杀（B355）。","src":"B355"}],
"major_works":[
 {"work_id":"jipusaiyaoqu","note":"1928（B355）"},
 {"work_id":"xuehun","note":"1933（B355）"},
 {"title":"叶尔玛","note":"（B355：Yerma (1934)）"},
 {"title":"贝尔纳达·阿尔巴的家","note":"（B355：La casa de Bernarda Alba (1936)）"}],
"style":["安达卢西亚谣曲传统与先锋并置（B355：Romancero gitano 语系）。",
 "'深歌'诗学（B355：Poema del cante jondo, 1921-25写/1931出版）。",
 "民间悲剧三部曲（B355：血婚/叶尔玛/阿尔巴之家）。"],
"status":"Britannica 定位洛尔卡为20世纪最重要的西班牙诗人剧作家、'27一代'核心、1936年被杀（B355）。",
"sources":["B355"],"dates_source":"B355",
"pending":["卒日两说（8月18/19——B355 口径）保留待核。","Poet in New York 出版年（1940死后说）待核。","'27一代'成员名单核对（B355载Alberti/Guillén/Salinas）。"]},
{"id":"musil","name":"罗伯特·穆齐尔","foreign_name":"Robert Musil（罗伯特·穆齐尔，1880-11-06—1942-04-15）","country":"奥地利","birth":1880,"death":1942,"birth_year":1880,"death_year":1942,"era":"近代",
"summary":"穆齐尔，奥地利克拉根福生，奥地利-德语小说家——'best known for his monumental unfinished novel'（Der Mann ohne Eigenschaften, 没有个性的人, 1930-43——B353）——'a witty and urbane view of life in the glittering world of the Austro-Hungarian Empire, told from the viewpoint of Ulrich, a fictionalized Musil'（B353）。第一部1930年出版、第二部部分1933年、'a remaining portion was published posthumously in 1943'（B353）。剧作 Die Schwärmer (1920) 等在柏林维也纳上演（B353）。1908年柏林大学博士；一战奥军服役；1938年纳粹吞并奥地利后流亡瑞士（B353）。",
"timeline":[
 {"year":1880,"text":"11月6日生于克拉根福（B353）。","src":"B353"},
 {"year":1908,"text":"获柏林大学博士学位（B353）。","src":"B353"},
 {"year":1930,"text":"《没有个性的人》第一部出版（B353）。","src":"B353"},
 {"year":1938,"text":"纳粹吞并奥地利后流亡瑞士（B353）。","src":"B353"},
 {"year":1942,"text":"4月15日卒于日内瓦；1943年遗稿出版（B353）。","src":"B353"}],
"major_works":[
 {"work_id":"meiyougexingderen","note":"1930-43（B353）"},
 {"title":"狂热者","note":"（B353：Die Schwärmer (1920)——中译名待核）"}],
"style":["'机智而摩登'的奥匈帝国浮华世界（B353：witty and urbane）。",
 "'没有个性'——对性格概念的怀疑（书名语境——通说待核）。",
 "未完成巨构（B353：monumental unfinished）。"],
"status":"Britannica 定位穆齐尔为未完成巨著《没有个性的人》的作者（B353）。",
"sources":["B353"],"dates_source":"B353",
"pending":["Young Törless (1906) 未见于本页——不采其详情。","乌尔里希全名与'平行行动'情节核对（B353未载）。","'没有个性的人'通行译名（《没有个性的人》）待核。"]},
{"id":"quasimodo","name":"萨瓦多尔·夸西莫多","foreign_name":"Salvatore Quasimodo（萨瓦多尔·夸西莫多，1901-08-20—1968-06-14）","country":"意大利","birth":1901,"death":1968,"birth_year":1901,"death_year":1968,"era":"现当代",
"summary":"夸西莫多，西西里 Modica 生（铁路职工之子），意大利诗人——1959年诺贝尔文学奖（B354）。'Originally a leader of the Hermetic poets, he became, after World War II, a powerful poet commenting on modern social issues.'（由隐逸派领袖转为战后社会议题的强力诗人——B354）。师从翁加雷蒂与蒙塔莱起步；1930年代'the dry, sophisticated style and abstruse symbolism of Hermeticism'；隐逸期终于 Poesie (1938) 与 Ed è subito sera（瞬息间是夜晚, 1942）（B354）。战后 Giorno dopo giorno (1947)——'Many of his poems recalled the injustices of the fascist regime, the horrors of the war, and Italian guilt.'（B354）——'simple in language, exhibit a concrete and immediate imagery'（B354）。译希腊抒情诗与悲剧家、莎剧六种、聂鲁达等（B354）。",
"timeline":[
 {"year":1901,"text":"8月20日生于西西里 Modica（B354）。","src":"B354"},
 {"year":1930,"text":"Acque e terre——第一部诗集（B354）。","src":"B354"},
 {"year":1942,"text":"Ed è subito sera（瞬息间是夜晚）——隐逸期收束（B354）。","src":"B354"},
 {"year":1947,"text":"Giorno dopo giorno——战后社会诗歌转向（B354）。","src":"B354"},
 {"year":1959,"text":"获诺贝尔文学奖（B354）。","src":"B354"},
 {"year":1968,"text":"6月14日卒于那不勒斯（B354）。","src":"B354"}],
"major_works":[
 {"work_id":"shunxijiandeyewan","note":"1942（B354）"},
 {"title":"日复一日","note":"（B354：Giorno dopo giorno (1947)——中译名待核）"}],
"style":["隐逸派：'干涩、精微的风格与晦涩的象征'（B354）。",
 "战后转向：'语言朴素、意象具体直接'（B354）。",
 "翻译家：希腊抒情诗/悲剧、莎士比亚（B354）。"],
"status":"Britannica 定位夸西莫多为1959年诺奖得主、隐逸派领袖→战后社会诗人（B354）。",
"sources":["B354"],"dates_source":"B354",
"pending":["Ed è subito sera 通行译名（《瞬息间是夜晚》）待核。","'Lé quá'等篇目未载——不采。","1959诺奖授奖词待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"jipusaiyaoqu","title":"吉普赛谣曲","original_title":"Romancero gitano","region":"西班牙","era":"近代","era_detail":"20世纪20年代",
"genre":"诗集","genre_group":"诗歌","language":"西班牙语","author_id":"lorca","author_name":"费德里科·加西亚·洛尔卡",
"year_display":"1928年（Britannica B355：Romancero gitano——1921-27年写、1928年出版——18首谣曲）","year_sort":1928,
"background":["Britannica（B355）：18首谣曲——'sold out within a year; many readers mistook Lorca for a Gypsy'（一年内售罄；许多读者误以为洛尔卡是吉普赛人）。","Britannica（B355）：洛尔卡——'the most important Spanish poet and playwright of the 20th century'。","Britannica（B355）：1927年纪念贡戈拉逝世300周年的群体——此后被称为'Generation of 1927'。"],
"outline":["谣曲体（romance传统）与现代意象的融合：月光、吉普赛、血与刀（B355 语系——具体篇目通说待核）。","《月亮，月亮》等篇目（篇名通说待核——B355未载）。"],
"characters":[{"name":"抒情'我'","identity":"谣曲叙述者","note":"（通说待核）"}],
"themes":["安达卢西亚民间谣曲的现代化（B355 语系）。",
 "吉普赛世界的边缘与暴力（B355：读者误认语境）。",
 "贡戈拉传统的再创造（B355：Generation of 1927）。"],
"influence":[{"text":"Britannica：一年内售罄——洛尔卡成名（B355）。","source":"B355"},{"text":"Britannica：'27一代'的确立（B355）。","source":"B355"}],
"reading":{"difficulties":["西班牙谣曲格律（romance 八音节体——通说待核）。","安达卢西亚意象系统。"],
 "editions":["《吉普赛谣曲》中译本（人民文学/上海译文等——通说待核）。","西班牙文原版。"],
 "order":"洛尔卡诗歌首选；后接《诗人在纽约》。"},
"pending":["具体篇目（月/风/普雷希奥萨等）核对（B355未载）。","1928年出版（Revista de Occidente说）待核。","'误认为吉普赛人'细节仅 B355 口径。"],
"sources":["B355"],"year_source":"B355","author_source":"B355","related_works":rel_yao,
"svg":G("《吉普赛谣曲》安达卢西亚图",[{"title":"谣曲","text":"民间体的现代转化（B355）","color":"main"},{"title":"月光","text":"安达卢西亚意象（通说）","color":"gold"},{"title":"吉普赛","text":"边缘的世界（B355）","color":"family"},{"title":"'27一代","text":"贡戈拉的传统（B355）","color":"antagonist"}])},
{"id":"xuehun","title":"血婚","original_title":"Bodas de sangre","region":"西班牙","era":"近代","era_detail":"20世纪30年代初",
"genre":"悲剧","genre_group":"戏剧","language":"西班牙语","author_id":"lorca","author_name":"费德里科·加西亚·洛尔卡",
"year_display":"1933年（Britannica B355：Bodas de sangre (1933)）","year_sort":1933,
"background":["Britannica（B355）：Bodas de sangre——洛尔卡民间悲剧三部曲之一（与 Yerma 1934、La casa de Bernarda Alba 1936 并列——B355 作品列表）。","Britannica（B355）：洛尔卡帮助开启了西班牙戏剧'second Golden Age'。","题材（通说待核）：婚礼当夜新娘与旧爱私奔——血缘与激情的死亡追逐。"],
"outline":["婚礼与私奔：两个男人与一个女人（情节通说待核——B355未载）。","月亮与乞妇的插场（超自然插场说通说待核）。"],
"characters":[{"name":"新娘","identity":"三部曲女性","note":"（通说待核，B355未载名）"},{"name":"莱昂纳多","identity":"旧爱","note":"（通说待核，B355未载）"}],
"themes":["激情与婚姻制度的冲突（通说待核）。",
 "民间悲剧的现代形式（B355：second Golden Age 语境）。",
 "安达卢西亚的宿命观（通说待核）。"],
"influence":[{"text":"Britannica：'the most important Spanish poet and playwright of the 20th century'（B355）。","source":"B355"},{"text":"Britannica：西班牙戏剧'second Golden Age'（B355）。","source":"B355"}],
"reading":{"difficulties":["西班牙民间悲剧传统。","歌队与超自然插场（通说待核）。"],
 "editions":["《血婚》中译本（人民文学《洛尔卡戏剧集》等——通说待核）。","西班牙文原版。"],
 "order":"洛尔卡戏剧首选；三部曲连读。"},
"pending":["莱昂纳多/母亲人名核对（B355未载）。","1933年首演细节待核。","月亮/乞妇插场细节待核。"],
"sources":["B355"],"year_source":"B355","author_source":"B355","related_works":rel_xh,
"svg":G("《血婚》悲剧三角图",[{"title":"新娘","text":"婚姻与激情（通说）","color":"main"},{"title":"旧爱","text":"血的冲动（通说）","color":"antagonist"},{"title":"新郎","text":"制度的一方（通说）","color":"family"},{"title":"月亮","text":"超自然插场（通说）","color":"gold"}])},
{"id":"meiyougexingderen","title":"没有个性的人","original_title":"Der Mann ohne Eigenschaften","region":"奥地利","era":"近代","era_detail":"20世纪30年代",
"genre":"长篇小说（未完成）","genre_group":"小说","language":"德语","author_id":"musil","author_name":"罗伯特·穆齐尔",
"year_display":"1930-43年（Britannica B353：Der Mann ohne Eigenschaften (1930-43)——第一部1930、第二部部分1933、遗稿1943）","year_sort":1930,
"background":["Britannica（B353）：'monumental unfinished novel'——'a witty and urbane view of life in the glittering world of the Austro-Hungarian Empire, told from the viewpoint of Ulrich, a fictionalized Musil'。","Britannica（B353）：第一部1930年出版、第二部部分1933年、'a remaining portion was published posthumously in 1943'。","Britannica（B353）：穆齐尔一战服役、1938年流亡瑞士。"],
"outline":["乌尔里希——'虚构的穆齐尔'——在奥匈帝国浮华世界中的游历（B353：viewpoint of Ulrich）。","'平行行动'：帝国的自我庆典与乌托邦（情节通说待核——B353未载）。"],
"characters":[{"name":"乌尔里希","identity":"主角/试验者","note":"（B353：Ulrich, a fictionalized Musil）"},{"name":"阿加特","identity":"第二部人物","note":"（通说待核，B353未载）"}],
"themes":["'没有个性'：对人格概念的拆解（通说待核）。",
 "奥匈帝国的浮华与虚无（B353：glittering world）。",
 "试验生活（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：'monumental unfinished novel'（B353）。","source":"B353"},{"text":"Britannica：1943年遗稿出版（B353）。","source":"B353"}],
"reading":{"difficulties":["未完成的开放结构。","1913年前后奥匈史与'平行行动'（通说待核）。"],
 "editions":["《没有个性的人》中译本（人民文学等——通说待核）。","德文原版。"],
 "order":"穆齐尔唯一巨著；分部慢读。"},
"pending":["'平行行动'（Parallelaktion）细节核对（B353未载）。","阿加特/克拉丽瑟人名核对（B353未载）。","中译本分卷（第一部/第二部）细节待核。"],
"sources":["B353"],"year_source":"B353","author_source":"B353","related_works":rel_mg,
"svg":G("《没有个性的人》帝国浮华图",[{"title":"乌尔里希","text":"'虚构的穆齐尔'（B353）","color":"main"},{"title":"奥匈帝国","text":"浮华的世界（B353）","color":"gold"},{"title":"'没有个性'","text":"人格的拆解（通说）","color":"family"},{"title":"未完成","text":"1930-43（B353）","color":"antagonist"}])},
{"id":"shunxijiandeyewan","title":"瞬息间是夜晚","original_title":"Ed è subito sera","region":"意大利","era":"现当代","era_detail":"20世纪40年代初",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"quasimodo","author_name":"萨瓦多尔·夸西莫多",
"year_display":"1942年（Britannica B354：Ed è subito sera (1942; And Suddenly Its Evening)——隐逸期收束）","year_sort":1942,
"background":["Britannica（B354）：Ed è subito sera——隐逸期终于 Poesie (1938) 与本集（1942）。","Britannica（B354）：夸西莫多师从翁加雷蒂与蒙塔莱起步；'gradually became a leader of the Hermetic poets'；1930年代'the dry, sophisticated style and abstruse symbolism of Hermeticism'。","Britannica（B354）：战后转向——Giorno dopo giorno (1947)——'Many of his poems recalled the injustices of the fascist regime, the horrors of the war, and Italian guilt.'"],
"outline":["西西里乡村的哀歌：'每个人孤独地站在世界的心上'（名句通说待核——B354未载原文）。","干涩精微的隐逸语体（B354：dry, sophisticated style and abstruse symbolism）。"],
"characters":[{"name":"抒情'我'","identity":"隐逸诗人","note":"（B354 语系）"}],
"themes":["隐逸派的晦涩象征（B354）。",
 "西西里与流亡的心象（通说待核）。",
 "战前的静默与战后的爆发（B354：转向语境）。"],
"influence":[{"text":"Britannica：1959年诺贝尔文学奖（B354）。","source":"B354"},{"text":"Britannica：'Originally a leader of the Hermetic poets...'（B354）。","source":"B354"}],
"reading":{"difficulties":["隐逸派的省略与浓缩。","西西里方言地名（通说待核）。"],
 "editions":["《瞬息间是夜晚》中译本（人民文学/译林等——通说待核）。","意大利文原版。"],
 "order":"夸西莫多首选；后接《日复一日》(1947)。"},
"pending":["通行译名（《瞬息间是夜晚》/《而倏然已是黄昏》）待核。","名句原文核对（B354未载）。","1942年出版（Mondadori说）待核。"],
"sources":["B354"],"year_source":"B354","author_source":"B354","related_works":rel_qs,
"svg":G("《瞬息间是夜晚》隐逸结构图",[{"title":"黄昏","text":"骤至的夜（B354书名）","color":"main"},{"title":"隐逸派","text":"干涩精微的象征（B354）","color":"gold"},{"title":"西西里","text":"乡村的哀歌（通说）","color":"family"},{"title":"战后","text":"转向社会的诗（B354）","color":"antagonist"}])},
]
for w in works:
    if w['id'] in existing:
        print('skip existing', w['id'])
for w in works:
    if w['id'] in existing:
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

for aid, wid in [("lorca","jipusaiyaoqu"),("lorca","xuehun"),("musil","meiyougexingderen"),("quasimodo","shunxijiandeyewan")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B35x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH30 DONE')
