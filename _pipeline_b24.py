# -*- coding: utf-8 -*-
"""批24：Britannica 新核 3 作家 4 部（皮兰德娄/比昂松/荷尔德林 B336-B338）——意大利现当代大缺口"""
import json, pathlib

newsrc = [
{"id":"B336","title":"Luigi Pirandello — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Luigi-Pirandello","type":"百科全书","verified":True,"covers":["pirandello","liugejuesesouzhao"],"note":"2026-11-21 核对：1867-06-28西西里阿格里真托生—1936-12-10罗马卒（69岁）；1934诺贝尔文学奖；Sei personaggi in cerca d'autore (1921)——'the most arresting presentation of the typical Pirandellian contrast between art, which is unchanging, and life, which is an inconstant flux'；1923巴黎演出使其名扬；'theatre within the theatre'（戏中戏）装置；影响法国戏剧、荒诞派（贝克特/尤涅斯库/热内）、阿努伊、萨特、T.S.艾略特诗剧；引文 'I think that life is a very sad piece of buffoonery'（1920）、'My art is full of bitter compassion for all those who deceive themselves'、身份'a person is one, no one and a hundred thousand, according to his appearance to this person or that'；Uno, nessuno e centomila (1925-26)——'the most original and the most typical of his novels'；妻子之病'determined the theme of his most characteristic work'；遗愿仅'a hearse of the poor, the horse and the coachman'"},
{"id":"B337","title":"Bjornstjerne Bjornson — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Bjornstjerne-Bjornson","type":"百科全书","verified":True,"covers":["bjornson","xinnuofusuobaken"],"note":"2026-11-21 核对：1832-12-08挪威Kvikne生—1910-04-26巴黎卒（77岁）；1903诺贝尔文学奖；与易卜生、基兰、约纳斯·李并称19世纪挪威文学'四大家'（'the four great ones'）；Synnøve Solbakken (1857)——农庄故事（英译名 Trust and Trial/Love and Life in Norway/Sunny Hill）；诗'Ja, vi elsker dette landet'为挪威国歌歌词；'his plays were influential in establishing social realism in Europe'；'saga material was turned into plays, contemporary material into novels or peasant tales'（轮作式写作）；卑尔根剧院艺术总监（1857-59，易卜生的继任者）；晚年自认社会主义者、致力于和平与国际谅解"},
{"id":"B338","title":"Friedrich Holderlin — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Friedrich-Holderlin","type":"百科全书","verified":True,"covers":["holderlin","xuboliweng"],"note":"2026-11-21 核对：1770-03-20内卡河畔劳芬生—1843-06-07图宾根卒（73岁）；Hyperion——'elegiac story of a disillusioned fighter for the liberation of Greece'（哀歌体的幻灭希腊解放战士故事），未完成；第二卷1799年出版（第一卷以断片刊于席勒《新塔莉亚》）；苏塞特·贡塔尔在书中以希腊名'Diotima'出现；早期颂歌献给自由/人性/和谐/友谊/自然（法国大革命理想）；1798-1801哀歌'Menons Klagen um Diotima'与'Brod und Wein'（面饼与酒）；晚期诗（1802-06）'Friedensfeier'/'Der Einzige'/'Patmos'——'apocalyptic visions of unique grandeur'（濒于疯狂的心智）；1802年自波尔多返——'suffering from an advanced stage of schizophrenia'，后住木匠家36年；生前几乎无闻、被遗忘近100年，20世纪初德国重新发现，今列最伟大的德语诗人——'especially admired for his uniquely expressive style'；'a prophet of spiritual renewal, of the return of the gods'"},
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
def find_work(aid, prefer=None):
    got = [p.stem for p in pathlib.Path('data/works').glob('*.json') if json.load(open(p, encoding='utf-8'))['author_id'] == aid]
    for pref in prefer or []:
        if pref in got: return pref
    return got[0] if got else 'leiyu'

rel_pir = [find_work('beckett', ['moluoyi']), 'yingtaoyuan', 'manchangdeheian']
rel_bj  = ['qieelvxing', find_work('ibsen'), 'qieelvxing']
rel_ho  = [find_work('goethe'), 'fushide' if 'fushide' in existing else 'leiyu', find_work('heine', [])]
rel_bj = list(dict.fromkeys(rel_bj)); rel_ho = list(dict.fromkeys(rel_ho))
print('rel:', rel_pir, rel_bj, rel_ho)

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"pirandello","name":"路易吉·皮兰德娄","foreign_name":"Luigi Pirandello（路易吉·皮兰德娄，1867-06-28—1936-12-10）","country":"意大利","birth":1867,"death":1936,"birth_year":1867,"death_year":1936,"era":"近代",
"summary":"皮兰德娄，西西里阿格里真托生，意大利剧作家与小说家——1934年诺贝尔文学奖（B336）。Sei personaggi in cerca d'autore（六个寻找剧作家的角色, 1921）——'the most arresting presentation of the typical Pirandellian contrast between art, which is unchanging, and life, which is an inconstant flux'（B336）——首创'戏中戏'（theatre within the theatre）装置（B336）。其妻之病'determined the theme of his most characteristic work'——对流动多变人格的探究（B336）。身份论：'a person is one, no one and a hundred thousand, according to his appearance to this person or that'（B336）。1936年遗愿仅'a hearse of the poor, the horse and the coachman'（B336）。",
"timeline":[
 {"year":1867,"text":"6月28日生于西西里阿格里真托（B336）。","src":"B336"},
 {"year":1921,"text":"《六个寻找剧作家的角色》罗马首演（B336：Sei personaggi in cerca d'autore (1921)）。","src":"B336"},
 {"year":1923,"text":"巴黎演出使其名扬欧洲（B336：Its 1923 Paris production made him widely known）。","src":"B336"},
 {"year":1934,"text":"获诺贝尔文学奖（B336）。","src":"B336"},
 {"year":1936,"text":"12月10日卒于罗马（B336）。","src":"B336"}],
"major_works":[
 {"work_id":"liugejuesesouzhao","note":"1921（B336）"},
 {"work_id":"yigewushiwan","note":"1925-26（B336）"},
 {"title":"恩里科四世","note":"（B336：Enrico IV (1922)——'the theme is madness, which lies just under the skin of ordinary life'）"}],
"style":["'戏中戏'装置的发明者（B336：theatre within the theatre）。",
 "艺术不变与生活流变之对立（B336）。",
 "'苦涩的怜悯'：'My art is full of bitter compassion for all those who deceive themselves'（B336）。"],
"status":"Britannica 定位皮兰德娄为1934年诺奖得主、荒诞派戏剧的先驱影响者（影响贝克特/尤涅斯库/热内/萨特——B336）。",
"sources":["B336"],"dates_source":"B336",
"pending":["六角色（父亲/母亲/继女）人名核对（B336未载）。","1921年罗马首演剧场（Valle Theatre说）待核。","《恩里科四世》剧情细节待核。"]},
{"id":"bjornson","name":"比奥恩斯彻讷·比昂松","foreign_name":"Bjørnstjerne Bjørnson（比奥恩斯彻讷·马丁尼乌斯·比昂松，1832-12-08—1910-04-26）","country":"挪威","birth":1832,"death":1910,"birth_year":1832,"death_year":1910,"era":"近代",
"summary":"比昂松，挪威Kvikne生，作家、剧作家与诗人——1903年诺贝尔文学奖（B337）。与易卜生、基兰、约纳斯·李并称19世纪挪威文学'四大家'（'the four great ones'——B337）。其诗'Ja, vi elsker dette landet'为挪威国歌歌词（B337）。'his plays were influential in establishing social realism in Europe'（B337）。写作如轮作：'saga material was turned into plays, contemporary material into novels or peasant tales'（B337）。1857-59年任卑尔根剧院艺术总监——易卜生的继任者（B337）。晚年自认社会主义者，致力于和平与国际谅解（B337）。",
"timeline":[
 {"year":1832,"text":"12月8日生于挪威Kvikne（B337）。","src":"B337"},
 {"year":1857,"text":"任卑尔根剧院艺术总监——易卜生的继任者；同年农庄故事 Synnøve Solbakken（B337）。","src":"B337"},
 {"year":1870,"text":"《诗集与歌集》初版（含后来成为国歌歌词的诗——B337：Digte og sange (1870)）。","src":"B337"},
 {"year":1903,"text":"获诺贝尔文学奖（B337）。","src":"B337"},
 {"year":1910,"text":"4月26日卒于巴黎（B337）。","src":"B337"}],
"major_works":[
 {"work_id":"xinnuofusuobaken","note":"1857农庄故事（B337）"},
 {"title":"快乐的男孩","note":"（B337：En glad gut (1860)——中译名待核）"},
 {"title":"破产","note":"（B337：En fallit (1875)——戏剧）"},
 {"title":"超越人力","note":"（B337：Over Ævne I og II (1883, 1895)——为他赢得国际声誉的 drama 说待核：'The two dramas that brought him an international reputation were thus written in self-imposed exile'）"}],
"style":["民族浪漫主义：'to stimulate national pride in Norway's history and achievements and to present ideals'（B337）。",
 "农庄故事（peasant tales）与社会现实主义剧作（B337）。",
 "'轮作式'写作：史诗素材入戏、当代素材入小说或农庄故事（B337）。"],
"status":"Britannica 定位比昂松为1903年诺奖得主、挪威'四大家'之一、欧洲社会现实主义的推动者（B337）。",
"sources":["B337"],"dates_source":"B337",
"pending":["Synnøve Solbakken 通行中译名待核。","国歌歌词采用年份（1860s-1906）待核。","'两部戏剧因自我放逐而写并带来国际声誉'指哪两部待核（B337指向 Over Ævne 但需核对）。"]},
{"id":"holderlin","name":"弗里德里希·荷尔德林","foreign_name":"Friedrich Hölderlin（弗里德里希·荷尔德林，1770-03-20—1843-06-07）","country":"德国","birth":1770,"death":1843,"birth_year":1770,"death_year":1843,"era":"近代",
"summary":"荷尔德林，内卡河畔劳芬生，德语诗人——'a prophet of spiritual renewal, of \"the return of the gods\"'（精神更新与'诸神回归'的先知——B338）。Hyperion——'elegiac story of a disillusioned fighter for the liberation of Greece'，第二卷1799年出版（B338）；书中苏塞特·贡塔尔以希腊名'Diotima'出现（B338）。1798-1801年哀歌《面饼与酒》（Brod und Wein）等（B338）。1802年自波尔多返回时已患重度精神分裂，其后36年住图宾根木匠家中（B338）。生前几乎无闻、被遗忘近100年，20世纪初被重新发现——今列最伟大的德语诗人，'especially admired for his uniquely expressive style'（B338）。",
"timeline":[
 {"year":1770,"text":"3月20日生于内卡河畔劳芬（B338）。","src":"B338"},
 {"year":1799,"text":"Hyperion 第二卷出版（第一卷断片刊于席勒《新塔莉亚》——B338）。","src":"B338"},
 {"year":1802,"text":"自波尔多返回，'suffering from an advanced stage of schizophrenia'（B338）。","src":"B338"},
 {"year":1843,"text":"6月7日卒于图宾根；此前在木匠家中住了36年（B338）。","src":"B338"}],
"major_works":[
 {"work_id":"xuboliweng","note":"（B338：Hyperion 第二卷1799）"},
 {"title":"面饼与酒","note":"（B338：Brod und Wein——1798-1801哀歌）"},
 {"title":"恩培多克勒之死","note":"（B338：Der Tod des Empedokles——约1798年起，三稿）"}],
"style":["颂歌语体：献给自由、人性、和谐、友谊与自然（B338）。",
 "'uniquely expressive style'——独一无二的抒情表达（B338）。",
 "希腊诸神为'real living forces whose presence manifests itself to humans in sun and earth, sea and sky'（B338）。"],
"status":"Britannica 定位荷尔德林为被遗忘百年后于20世纪初重新发现的德语大诗人（B338）。",
"sources":["B338"],"dates_source":"B338",
"pending":["Hyperion 通行中译名（《许珀里翁》/《徐培里翁》）待核。","'塔乌里岛航行'等未核实篇目不采。","1806年图宾根诊所细节待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"liugejuesesouzhao","title":"六个寻找剧作家的角色","original_title":"Sei personaggi in cerca d'autore","region":"意大利","era":"近代","era_detail":"20世纪20年代",
"genre":"戏剧","genre_group":"戏剧","language":"意大利语","author_id":"pirandello","author_name":"路易吉·皮兰德娄",
"year_display":"1921年（Britannica B336：Sei personaggi in cerca d'autore (1921)）","year_sort":1921,
"background":["Britannica（B336）：'the most arresting presentation of the typical Pirandellian contrast between art, which is unchanging, and life, which is an inconstant flux'——皮兰德娄式'艺术不变/生活流变'对立最惊人的呈现。","Britannica（B336）：被作者抛弃的角色登台，'with more vitality than the real actors'；本剧引入'theatre within the theatre'装置——被弃角色直面将要扮演他们的演员。","Britannica（B336）：1923年巴黎演出使其名扬；影响了法国戏剧、荒诞派（贝克特、尤涅斯库、热内）、阿努伊、萨特与T.S.艾略特诗剧。"],
"outline":["排练场上，六个被作者抛弃的角色闯入，要求剧团上演他们未曾完成的故事（B336：rejected characters...confront the actors who would portray them）。","戏中戏的层层展开：'真实'与'扮演'无法区分（剧情细节通说待核）。"],
"characters":[{"name":"父亲","identity":"六角色之首","note":"（通说待核，B336未载人名）"},{"name":"继女","identity":"六角色之一","note":"（通说待核，B336未载）"},{"name":"剧团经理","identity":"排练主持","note":"（通说待核，B336未载）"}],
"themes":["艺术不变与生活流变之对立（B336：art...unchanging / life...an inconstant flux）。","'戏中戏'：戏剧自身的主题化（B336：theatre within the theatre）。","身份的流动性（B336 作者论：'one, no one and a hundred thousand, according to his appearance to this person or that'）。"],
"influence":[{"text":"Britannica：影响法国戏剧、荒诞派（贝克特/尤涅斯库/热内）、阿努伊、萨特与T.S.艾略特诗剧（B336）。","source":"B336"},{"text":"Britannica：1923年巴黎演出使其名扬（B336）。","source":"B336"}],
"reading":{"difficulties":["元戏剧的套层结构。","皮兰德娄'幽默论'背景（B336：L'umorismo (1908)——论文）。"],
 "editions":["《六个寻找剧作家的角色》中译本（人民文学/上海译文等——通说待核）。","意大利文原版。"],
 "order":"皮兰德娄首选；再读《恩里科四世》（1922）。"},
"pending":["六角色人名核对（B336未载）。","1921年罗马首演剧场待核。","1923年巴黎制作（Pitoëff说）待核。"],
"sources":["B336"],"year_source":"B336","author_source":"B336","related_works":rel_pir,
"svg":G("《六个寻找剧作家的角色》元戏剧结构图",[{"title":"六角色","text":"被作者抛弃者（B336）","color":"main"},{"title":"演员","text":"扮演者被直面（B336）","color":"antagonist"},{"title":"戏中戏","text":"theatre within theatre（B336）","color":"gold"},{"title":"生活","text":"不变的Art/流变的生活","color":"family"}])},
{"id":"yigewushiwan","title":"一个、无、十万个","original_title":"Uno, nessuno e centomila","region":"意大利","era":"近代","era_detail":"20世纪20年代",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"pirandello","author_name":"路易吉·皮兰德娄",
"year_display":"1925-26年（Britannica B336：Uno, nessuno e centomila (1925-26)）","year_sort":1925,
"background":["Britannica（B336）：'the most original and the most typical of his novels'——皮兰德娄最具原创性、最典型的小说。","Britannica（B336）：小说探究'他人如何看待他与他如何看待自己'之别（exploring how others see him differently than he sees himself）。","Britannica（B336）：皮兰德娄身份论——'a person is one, no one and a hundred thousand, according to his appearance to this person or that'。"],
"outline":["主人公因妻子之镜发现自我在他人眼中分裂为'十万个'（剧情通说待核——B336未载细节）。","对'自我面具'的执念与自我抹除（通说待核）。"],
"characters":[{"name":"主人公（维塔利亚诺说）","identity":"银行职员","note":"（通说待核，B336未载人名）"}],
"themes":["他人之镜中的自我分裂（B336：how others see him differently）。","'一、无、十万'的身份算术（B336 书名与作者论）。","自我欺骗的怜悯（B336：'My art is full of bitter compassion for all those who deceive themselves'）。"],
"influence":[{"text":"Britannica：'the most original and the most typical of his novels'（B336）。","source":"B336"},{"text":"Britannica：妻子之病'determined the theme of his most characteristic work'（B336）。","source":"B336"}],
"reading":{"difficulties":["心理—哲学小说的抽象性。","'面具'（maschera）术语体系。"],
 "editions":["中译名待核（《一个，无，十万个》等）。","意大利文原版。"],
 "order":"皮兰德娄进阶；先读《六个寻找剧作家的角色》。"},
"pending":["主人公名（维塔利亚诺说）与妻子名核对（B336未载）。","中译名两说待核。","1925-26年连载出版细节待核。"],
"sources":["B336"],"year_source":"B336","author_source":"B336","related_works":["liugejuesesouzhao","xuboliweng","huanxiangjia" if "huanxiangjia" in existing else "leiyu"],
"svg":G("《一个、无、十万个》自我分裂图",[{"title":"镜子","text":"他人之眼（B336语境）","color":"gold"},{"title":"一个","text":"自认的我","color":"main"},{"title":"十万个","text":"他人眼中的我","color":"antagonist"},{"title":"面具","text":"自欺的怜悯（B336）","color":"family"}])},
{"id":"xinnuofusuobaken","title":"辛诺夫·索巴肯","original_title":"Synnøve Solbakken","region":"挪威","era":"近代","era_detail":"19世纪50年代",
"genre":"中篇小说","genre_group":"小说","language":"挪威语","author_id":"bjornson","author_name":"比奥恩斯彻讷·比昂松",
"year_display":"1857年（Britannica B337：Synnøve Solbakken (1857)——农庄故事）","year_sort":1857,
"background":["Britannica（B337）：Synnøve Solbakken (1857)——农庄故事（peasant tale）；英译名 Trust and Trial、Love and Life in Norway、Sunny Hill。","Britannica（B337）：比昂松'sought to stimulate national pride in Norway's history and achievements and to present ideals'。","Britannica（B337）：'saga material was turned into plays, contemporary material into novels or peasant tales'——'轮作式'写作。"],
"outline":["两个农庄之间的青年男女：家族宿怨与田园理想（情节通说待核——B337未载细节）。","和解与婚礼：挪威农庄的道德理想（通说待核）。"],
"characters":[{"name":"托尔（Thorbjörn说）","identity":"农庄青年","note":"（通说待核，B337未载人名）"},{"name":"辛诺夫","identity":"Solbakken农庄之女","note":"（书名人物，B337）"}],
"themes":["农庄故事与民族浪漫主义（B337：peasant tales；national pride）。"," ideals 的文学呈现（B337：to present ideals）。","宿怨与和解的乡土伦理（通说待核）。"],
"influence":[{"text":"Britannica：与《快乐的男孩》(1860)等构成农庄故事序列（B337 作品列表）。","source":"B337"},{"text":"Britannica：比昂松为挪威'四大家'之一（B337）。","source":"B337"}],
"reading":{"difficulties":["挪威乡土社会与路德宗背景（通说待核）。","'农庄故事'类型传统（通说待核）。"],
 "editions":["中译名待核（《辛诺夫·索巴肯》）。","挪威文原版。"],
 "order":"比昂松入门；与《快乐的男孩》对读。"},
"pending":["青年男主人名（Thorbjörn说）核对（B337未载）。","中译名待核。","1857年出版细节待核。"],
"sources":["B337"],"year_source":"B337","author_source":"B337","related_works":rel_bj,
"svg":G("《辛诺夫·索巴肯》农庄结构图",[{"title":"两个农庄","text":"宿怨与和解（通说）","color":"family"},{"title":"辛诺夫","text":"农庄之女（B337）","color":"main"},{"title":"理想","text":"'呈现理想'（B337）","color":"gold"},{"title":"民族自豪","text":"历史的骄傲（B337）","color":"antagonist"}])},
{"id":"xuboliweng","title":"许珀里翁","original_title":"Hyperion","region":"德国","era":"近代","era_detail":"18世纪90年代",
"genre":"书信体小说","genre_group":"小说","language":"德语","author_id":"holderlin","author_name":"弗里德里希·荷尔德林",
"year_display":"1799年（Britannica B338：Hyperion 第二卷1799年出版——第一卷以断片刊于席勒《新塔莉亚》）","year_sort":1799,
"background":["Britannica（B338）：Hyperion——'elegiac story of a disillusioned fighter for the liberation of Greece'（哀歌体的、幻想破灭的希腊解放战士故事）——未完成。","Britannica（B338）：苏塞特·贡塔尔在书中以希腊名'Diotima'出现。","Britannica（B338）：荷尔德林——'a prophet of spiritual renewal, of \"the return of the gods\"'；他把希腊诸神看作'real living forces whose presence manifests itself to humans in sun and earth, sea and sky'。"],
"outline":["希腊解放战士许珀里翁的幻灭：从革命理想退回美的回忆（B338：disillusioned fighter for the liberation of Greece；书信体情节通说待核）。","'狄奥蒂玛'：爱情与希腊理想的化身（B338：Susette Gontard under the Greek name of 'Diotima'）。"],
"characters":[{"name":"许珀里翁","identity":"书信体叙述者","note":"（B338 书名人物）"},{"name":"狄奥蒂玛","identity":"爱人","note":"（B338：Diotima——原型苏塞特·贡塔尔）"}],
"themes":["希腊理想与德国现实之落差（B336 无关——B338：disillusioned fighter 语境）。","'诸神回归'的精神更新预言（B338：a prophet of spiritual renewal）。","哀歌体：面饼与酒的乡土之爱（B338：Brod und Wein 同期哀歌）。"],
"influence":[{"text":"Britannica：'almost totally forgotten for nearly 100 years'后于20世纪初重新发现，今列最伟大的德语诗人（B338）。","source":"B338"},{"text":"Britannica：'especially admired for his uniquely expressive style'（B338）。","source":"B338"}],
"reading":{"difficulties":["书信体与哀歌语体的交叉。","德国观念论与希腊崇拜背景（通说待核）。"],
 "editions":["中译名待核（《许珀里翁》/《徐培里翁》）。","德文原版（公有领域）。"],
 "order":"荷尔德林首选；后接《面饼与酒》等诗。"},
"pending":["中译名两说待核。","第二卷1799（第一卷1797-98断片说）核对。","《恩培多克勒之死》三稿细节待核。"],
"sources":["B338"],"year_source":"B338","author_source":"B338","related_works":rel_ho,
"svg":G("《许珀里翁》理想幻灭图",[{"title":"许珀里翁","text":"幻灭的解放战士（B338）","color":"main"},{"title":"狄奥蒂玛","text":"希腊之名（B338）","color":"gold"},{"title":"诸神","text":"'回归'的预言（B338）","color":"family"},{"title":"现实","text":"德国的落差（通说）","color":"antagonist"}])},
]
for w in works:
    assert w['id'] not in existing, f'dup {w["id"]}'
for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

# 作者页挂链
for aid, wid in [("pirandello","liugejuesesouzhao"),("pirandello","yigewushiwan"),("bjornson","xinnuofusuobaken"),("holderlin","xuboliweng")]:
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B33x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
print('BATCH24 DONE')
