# -*- coding: utf-8 -*-
"""批65：Britannica 新核塞弗尔特 B386（披光）+ 零成本 8 部（特拉夫尼克纪事/支票簿/母性的诗/惨败/非洲人/艰难之活/第三书/1794年）"""
import json, pathlib

newsrc = [
{"id":"B386","title":"Jaroslav Seifert — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jaroslav-Seifert","type":"百科全书","verified":True,"covers":["seifert","pishangguang"],"note":"2026-11-21 核对：1901-09-23布拉格生（奥匈帝国波希米亚）—1986-01-10布拉格卒（84岁）；1984诺贝尔文学奖——'the first Czech to win the Nobel Prize for Literature'；早期'proletarian poetry'——后转向'so-called pure poetry'的抒情要素；最常写'历史与捷克-斯洛伐克的其他方面'；1929年'第二共产党'分裂说（'broke with the Communist Party'）；谴责1968年苏联入侵；'among the first to sign' Charter 77（1977年1月，抗议胡萨克统治）；记者至1950年；约30卷诗集+儿童文学；1966年'民族诗人'称号；1981年回忆录；诗集：Město v slzách（1920）、Na vlnách T.S.F.（1925）、Slavík zpívá špatně（1926）、Zhasněte světla（1938）、Světlem oděná（1940）、Přílba hlíny（1945）"},
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
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def src_of(aid):
    return json.load(open(f'data/authors/{aid}.json', encoding='utf-8'))['sources'][0]

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"seifert","name":"雅罗斯拉夫·塞弗尔特","foreign_name":"Jaroslav Seifert（雅罗斯拉夫·塞弗尔特，1901-09-23—1986-01-10）","country":"捷克","birth":1901,"death":1986,"birth_year":1901,"death_year":1986,"era":"近代",
"summary":"塞弗尔特，布拉格生，捷克诗人——1984年诺贝尔文学奖——'the first Czech to win the Nobel Prize for Literature'（首位获诺奖的捷克人——B386）。早期'proletarian poetry'——后转向'so-called pure poetry'的抒情要素（B386）；最常写'历史与捷克-斯洛伐克的其他方面'（B386）。1929年'broke with the Communist Party'（B386）；谴责1968年苏联入侵；'among the first to sign' Charter 77（七七宪章，1977年1月）（B386）。记者至1950年；约30卷诗集（B386）；1966年'民族诗人'称号（B386）。",
"timeline":[
 {"year":1901,"text":"9月23日生于布拉格（B386）。","src":"B386"},
 {"year":1920,"text":"首部诗集 Město v slzách（泪水中的城市）（B386）。","src":"B386"},
 {"year":1929,"text":"与共产党决裂（B386）。","src":"B386"},
 {"year":1977,"text":"'七七宪章'首批签名者（B386）。","src":"B386"},
 {"year":1984,"text":"获诺贝尔文学奖——首位捷克得主（B386）。","src":"B386"},
 {"year":1986,"text":"1月10日卒于布拉格（B386）。","src":"B386"}],
"major_works":[
 {"work_id":"pishangguang","note":"1940（B386：Světlem oděná——中译名待核）"},
 {"title":"泪水中的城市","note":"（B386：Město v slzách (1920)——首部诗集——中译名待核）"},
 {"title":"铺满泥土的头盔","note":"（B386：Přílba hlíny (1945)——中译名待核）"}],
"style":["从'无产阶级诗'到'纯诗'的抒情（B386）。",
 "捷克历史与日常的诗歌书写（B386）。",
 "'七七宪章'的道德立场（B386）。"],
"status":"Britannica 定位塞弗尔特为1984诺奖得主、首位捷克诺奖作家、宪章首批签名者（B386）。",
"sources":["B386"],"dates_source":"B386",
"pending":["Světlem oděná 通行译名（《披光》/《被光所装扮》）待核。","'30卷'总数核对（B386：roughly 30）。","1981年回忆录名待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

S_AN, S_EC, S_GM, S_KE, S_LC, S_PA, S_RB, S_RY = (src_of(x) for x in ['andric','echegaray','gmistral','kertesz','leclezio','pavese','rabelais','reymont'])
print('srcs ok')

works = [
{"id":"pishangguang","title":"披光","original_title":"Světlem oděná","region":"捷克","era":"近代","era_detail":"20世纪40年代初",
"genre":"诗集","genre_group":"诗歌","language":"捷克语","author_id":"seifert","author_name":"雅罗斯拉夫·塞弗尔特",
"year_display":"1940年（Britannica B386：Světlem oděná (1940; Robed in Light)——中译名待核）","year_sort":1940,
"background":["Britannica（B386）：Světlem oděná (1940; Robed in Light)——诗集列表。","Britannica（B386）：塞弗尔特——从'proletarian poetry'转向'so-called pure poetry'的抒情要素。","Britannica（B386）：最常写'历史与捷克-斯洛伐克的其他方面'——本集处于占领前夕（1940说待核）。"],
"outline":["（通说待核——B386未载篇目）'披光'的布拉格抒情：母爱与城市。","（通说待核）占领年代的暗影（时代背景通说待核）。"],
"characters":[{"name":"抒情'我'","identity":"捷克诗人","note":"（B386 语境）"}],
"themes":["'纯诗'的抒情要素（B386：so-called pure poetry）。",
 "布拉格与母性（通说待核）。",
 "历史与个人的对位（B386：the history...of Czechoslovakia）。"],
"influence":[{"text":"Britannica：1984诺奖——'first Czech'（B386）。","source":"B386"},{"text":"Britannica：'so-called pure poetry'（B386）。","source":"B386"}],
"reading":{"difficulties":["捷克语（读译本）。","'纯诗'论语境（通说待核）。"],
 "editions":["《披光》中译名（《被光所装扮》）待核。","捷克文原版（公有领域状态待核）。"],
 "order":"塞弗尔特中期；与《泪水中的城市》对读。"},
"pending":["1940年出版细节待核。","篇目核对（B386未载）。","中译名两说待核。"],
"sources":["B386"],"year_source":"B386","author_source":"B386","related_works":["shiqishoushi","xianrenji","nianzhu"],
"svg":G("《披光》抒情结构图",[{"title":"光","text":"'披光'的布拉格（书名）","color":"gold"},{"title":"纯诗","text":"抒情的转向（B386）","color":"main"},{"title":"母爱","text":"城市的日常（通说）","color":"family"},{"title":"占领","text":"历史的暗影（通说）","color":"antagonist"}])},
# 零成本
{"id":"telafunikejishi","title":"特拉夫尼克纪事","original_title":"Travnička hronika","region":"南斯拉夫","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"塞尔维亚-克罗地亚语","author_id":"andric","author_name":"伊沃·安德里奇",
"year_display":"1945年（Britannica B376：Travnička hronika (1945; Bosnian Story)）","year_sort":1945,
"background":["Britannica（B376）：Travnička hronika——'shows Bosnia through French, Austrian, and Ottoman consuls in Travnik during Napoleon's era'（拿破仑时代特拉夫尼克的三领事视角）。","Britannica（B376）：'language of great beauty and purity'。","题材（通说待核）：法/奥/奥斯曼三领事的波斯尼亚博弈。"],
"outline":["（通说待核）三领事视角的'纪事'：达维勒与外交的迷局。","（通说待核）'纪事'体与波斯尼亚的耐心。"],
"characters":[{"name":"达维勒","identity":"法国领事","note":"（通说待核，B376未载）"}],
"themes":["三帝国的外交博弈（B376）。",
 "'纪事'的文体（书名语境——通说待核）。",
 "波斯尼亚的'耐心'（通说待核）。"],
"influence":[{"text":"Britannica：与《德里纳河上的桥》同年（1945——B376）。","source":"B376"},{"text":"Britannica：1961诺奖（B376 交叉）。","source":"B376"}],
"reading":{"difficulties":["拿破仑时代外交史。","'纪事'的编年腔。"],
 "editions":["《特拉夫尼克纪事》中译名（《波斯尼亚故事》）待核。","塞尔维亚-克罗地亚语原版。"],
 "order":"安德里奇第二作；与《德里纳河上的桥》对读。"},
"pending":["达维勒人名核对（通说）。","1945年出版细节待核。","'三领事'细节待核。"],
"sources":["B376"],"year_source":"B376","author_source":"B376","related_works":["derinahe","sangeshouqiangshou","fudi"],
"svg":G("《特拉夫尼克纪事》三领事图",[{"title":"三领事","text":"法/奥/奥斯曼（B376）","color":"gold"},{"title":"特拉夫尼克","text":"波黑的舞台（书名）","color":"main"},{"title":"拿破仑","text":"时代的风（B376）","color":"antagonist"},{"title":"纪事","text":"编年的文体（通说）","color":"family"}])},
{"id":"zhipiaobu","title":"支票簿","original_title":"El libro talonario","region":"西班牙","era":"近代","era_detail":"19世纪70年代",
"genre":"戏剧","genre_group":"戏剧","language":"西班牙语","author_id":"echegaray","author_name":"何塞·埃切加赖",
"year_display":"1874年（Britannica B369：El libro talonario（'The Checkbook'）——'His first play...not produced until 1874, when he was 42'）","year_sort":1874,
"background":["Britannica（B369）：El libro talonario——'His first play, El libro talonario (The Checkbook), was not produced until 1874, when he was 42'。","Britannica（B369）：此后平均'一年两部'。","题材（通说待核）：支票簿的金钱与爱情悲剧（处女作情节通说待核）。"],
"outline":["（通说待核）处女作的情节细节核对。","（通说待核）42岁'重启'人生（数学家→剧作家）。"],
"characters":[{"name":"（待核）","identity":"——","note":"（通说待核，B369未载）"}],
"themes":["处女作：政坛转向戏剧（B369）。",
 "情节剧的起点（B369：melodramatic 交叉）。",
 "'42岁'的传奇（B369）。"],
"influence":[{"text":"Britannica：'His first play'（B369）。","source":"B369"},{"text":"Britannica：1904诺奖（B369 交叉）。","source":"B369"}],
"reading":{"difficulties":["处女作的戏剧史定位。","'支票簿'标题的直译。"],
 "editions":["《支票簿》中译名（《记账簿》）待核。","西班牙文原版（公有领域）。"],
 "order":"埃切加赖起点；对照《疯子还是圣徒》。"},
"pending":["剧情细节核对（通说）。","1874年首演剧场待核。","中译名两说待核。"],
"sources":["B369"],"year_source":"B369","author_source":"B369","related_works":["fengzihaishishengt","yinmouyuaiqing","leiyu"],
"svg":G("《支票簿》处女作结构图",[{"title":"支票簿","text":"金钱的戏剧（书名）","color":"gold"},{"title":"42岁","text":"戏剧的起点（B369）","color":"main"},{"title":"数学家","text":"政坛的转身（B369）","color":"family"},{"title":"情节剧","text":"melodramatic（B369）","color":"antagonist"}])},
{"id":"muxingdeshi","title":"母性的诗","original_title":"Ternura","region":"智利","era":"近代","era_detail":"20世纪20年代",
"genre":"诗集","genre_group":"诗歌","language":"西班牙语","author_id":"gmistral","author_name":"加夫列拉·米斯特拉尔",
"year_display":"1924年（Britannica B343：Ternura (1924, 1945扩；'Tenderness')——中译名待核）","year_sort":1924,
"background":["Britannica（B343）：Ternura——'Tenderness'——1924年初版、1945年扩充——'evidence a broader interest'。","Britannica（B343）：米斯特拉尔——1945诺奖——'love of children and of the downtrodden remained her principal themes'。","题材（通说待核）：母性诗与摇篮曲——'对孩子的爱'的凝集。"],
"outline":["（通说待核）摇篮曲与童谣的集。","（通说待核）1945年扩充版的新篇。"],
"characters":[{"name":"抒情'我'","identity":"教师/母亲形象","note":"（B343 语系）"}],
"themes":["'对孩子的爱'（B343：love of children）。",
 "'温柔'（Ternura）的题意（书名——通说待核）。",
 "摇篮曲的民间体（通说待核）。"],
"influence":[{"text":"Britannica：Ternura (1924, 1945扩)（B343）。","source":"B343"},{"text":"Britannica：1945诺奖（B343 交叉）。","source":"B343"}],
"reading":{"difficulties":["摇篮曲的韵。","'母性'主题的界定。"],
 "editions":["《母性的诗》中译名（《温柔》）待核。","西班牙文原版。"],
 "order":"米斯特拉尔母性篇；与《荒凉》对读。"},
"pending":["1924年初版细节待核。","1945年扩充篇目待核。","中译名两说待核。"],
"sources":["B343"],"year_source":"B343","author_source":"B343","related_works":["huangliang","tala","ershisou"],
"svg":G("《母性的诗》温柔结构图",[{"title":"温柔","text":"Ternura 的题意（B343）","color":"gold"},{"title":"摇篮曲","text":"童谣的集（通说）","color":"main"},{"title":"教师","text":"对孩子的爱（B343）","color":"family"},{"title":"扩充","text":"1945的新篇（B343）","color":"antagonist"}])},
{"id":"canbai","title":"惨败","original_title":"A kudarc","region":"匈牙利","era":"近代","era_detail":"20世纪80年代",
"genre":"长篇小说","genre_group":"小说","language":"匈牙利语","author_id":"kertesz","author_name":"凯尔泰斯·伊姆雷",
"year_display":"1988年（Britannica B379：A kudarc / Fiasco (1988)）","year_sort":1988,
"background":["Britannica（B379）：Fiasco (1988)——作品列表（《无命运的一生》之后）。","Britannica（B379）：凯尔泰斯——2002诺奖。","题材（通说待核）：'惨败'——作家K·的审查与'第二本书'的失败（通说待核）。"],
"outline":["（通说待核）作家K与审查：'惨败'作为文学命运。","（通说待核）与《无命运的一生》的互文（通说待核）。"],
"characters":[{"name":"作家K","identity":"叙述者","note":"（通说待核）"}],
"themes":["审查与写作（通说待核）。",
 "'惨败'的书名反讽（书名语境）。",
 "三部曲的中篇（通说待核）。"],
"influence":[{"text":"Britannica：Fiasco (1988)（B379）。","source":"B379"},{"text":"Britannica：2002诺奖（B379 交叉）。","source":"B379"}],
"reading":{"difficulties":["三部曲的顺序。","社会主义审查语境（通说待核）。"],
 "editions":["《惨败》中译名（《失败》）待核。","匈牙利文原版。"],
 "order":"凯尔泰斯三部曲之二。"},
"pending":["作家K细节核对（通说）。","1988年出版细节待核。","'三部曲'说法待核。"],
"sources":["B379"],"year_source":"B379","author_source":"B379","related_works":["wumingyundesheng","weiweichushenghaizidewange","moluoyi"],
"svg":G("《惨败》审查结构图",[{"title":"惨败","text":"文学的反讽（书名）","color":"gold"},{"title":"作家K","text":"审查下的写作（通说）","color":"main"},{"title":"三部曲","text":"与《无命运》互文（通说）","color":"family"},{"title":"1988","text":"B注记之年","color":"antagonist"}])},
{"id":"feizhouren","title":"非洲人","original_title":"L'Africain","region":"法国","era":"现当代","era_detail":"21世纪初",
"genre":"回忆录","genre_group":"散文","language":"法语","author_id":"leclezio","author_name":"让-马里·古斯塔夫·勒克莱齐奥",
"year_display":"2004年（Britannica B381：L'Africain (2004)——memoir of reunion with his father after WWII）","year_sort":2004,
"background":["Britannica（B381）：L'Africain——'memoir of reunion with his father after WWII'（二战后与父亲重逢的回忆录）。","Britannica（B381）：勒克莱齐奥——2008诺奖；Onitsha (1991)——'semiautobiographical, inspired by his childhood in Nigeria'（交叉）。","题材（通说待核）：尼日利亚童年与父亲的医生岁月——'非洲人'的自我命名。"],
"outline":["（通说待核）战后与医生父亲的奥尼查重逢。","（通说待核）'非洲人'：自我的地理发现。"],
"characters":[{"name":"父亲","identity":"战地医生","note":"（B381：reunion with his father）"},{"name":"小勒克莱齐奥","identity":"孩子","note":"（通说待核）"}],
"themes":["'非洲人'的自我命名（书名语境——通说待核）。",
 "父子重逢（B381）。",
 "尼日利亚童年（B381：Onitsha 交叉）。"],
"influence":[{"text":"Britannica：L'Africain (2004)（B381）。","source":"B381"},{"text":"Britannica：2008诺奖（B381 交叉）。","source":"B381"}],
"reading":{"difficulties":["殖民地尼日利亚语境。","回忆录的'地理自传'。"],
 "editions":["《非洲人》中译本（人民文学等——通说待核）。","法文原版。"],
 "order":"勒克莱齐奥回忆录；与《奥尼查》对读。"},
"pending":["父亲名（乔治·勒克莱齐奥说）待核。","2004年出版细节待核。","与 Onitsha 的互文待核。"],
"sources":["B381"],"year_source":"B381","author_source":"B381","related_works":["sha","susongbifu","gududemigong"],
"svg":G("《非洲人》重逢结构图",[{"title":"重逢","text":"二战后的父子（B381）","color":"gold"},{"title":"非洲人","text":"自我的命名（书名）","color":"main"},{"title":"奥尼查","text":"童年的镇（B381交叉）","color":"family"},{"title":"医生","text":"父亲的战场（通说）","color":"antagonist"}])},
{"id":"jiananzhihuo","title":"艰难之活","original_title":"Lavorare stanca","region":"意大利","era":"近代","era_detail":"20世纪30年代",
"genre":"诗集","genre_group":"诗歌","language":"意大利语","author_id":"pavese","author_name":"切萨雷·帕韦泽",
"year_display":"1936年（Britannica B374：Lavorare stanca (1936; Hard Labor)——首部抒情诗集——1935出狱后）","year_sort":1936,
"background":["Britannica（B374）：Lavorare stanca——'first lyric poetry volume, after his 1935 prison release'（1935年出狱后的首部抒情诗集）。","Britannica（B374）：帕韦泽——'the novel considered his best'为《月亮与篝火》（交叉）。","题材（通说待核）：《成熟之男》等短诗——'Hard Labor'的题意（通说待核）。"],
"outline":["（通说待核）出狱后的短诗：Langhe 的村与海。","（通说待核）'艰苦劳动'（Hard Labor）的题意。"],
"characters":[{"name":"抒情'我'","identity":"出狱的诗人","note":"（B374 语境）"}],
"themes":["出狱后的第一书（B374）。",
 "'艰难之活'的题意（书名——通说待核）。",
 "Langhe 乡村（通说待核）。"],
"influence":[{"text":"Britannica：'first lyric poetry volume, after his 1935 prison release'（B374）。","source":"B374"},{"text":"Britannica：1950年自杀（B374 交叉）。","source":"B374"}],
"reading":{"difficulties":["短诗的口语。","'Hard Labor'的翻译。"],
 "editions":["《艰难之活》中译名（《劳动使人疲惫》）待核。","意大利文原版（公有领域状态待核）。"],
 "order":"帕韦泽诗歌首选；与《月亮与篝火》对读。"},
"pending":["篇目（《成熟之男》说）核对（通说）。","1936年出版细节待核。","英译 Hard Labor (1976——B374)核对。"],
"sources":["B374"],"year_source":"B374","author_source":"B374","related_works":["yueliangyuhuoyan","shenghuodezhiye","wuguigu"],
"svg":G("《艰难之活》出狱结构图",[{"title":"出狱","text":"1935年的自由（B374）","color":"antagonist"},{"title":"短诗","text":"Langhe 的村与海（通说）","color":"main"},{"title":"艰难","text":"'Hard Labor'（书名）","color":"gold"},{"title":"写作","text":"诗的起点（通说）","color":"family"}])},
{"id":"disanshu","title":"第三书","original_title":"Tiers livre des faits et dits héroïques du noble Pantagruel","region":"法国","era":"古代","era_detail":"16世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"rabelais","author_name":"弗朗索瓦·拉伯雷",
"year_display":"1546年（Britannica B365：Tiers livre (1546)——'Rabelais's most profound work'）","year_sort":1546,
"background":["Britannica（B365）：Tiers livre——'Rabelais's most profound work'——Pantagruel 'has now deepened into a Stoico-Christian inerrant sage'；Panurge 'a lover of self and deluded by the devil, is now an adept at making black seem white'。","Britannica（B365）：献给纳瓦拉王后玛格丽特——旋即被索邦斥为异端——逃亡梅斯（B365）。","Britannica（B365）：'ends enigmatically with a mock eulogy in which hemp is praised for its myriad uses'。"],
"outline":["Panurge 的婚姻咨询：神学家/医生/怀疑论者/掷签（B365：He consults...all to no effect because of his self-love）。","'神瓶'之旅的决定与'大麻'的颂歌收尾（B365）。"],
"characters":[{"name":"庞大固埃","identity":"'斯多葛-基督教'的圣人（B365）","note":"B365：Stoico-Christian inerrant sage"},{"name":"巴汝奇","identity":"自爱的咨询者","note":"（B365：a lover of self...making black seem white）"}],
"themes":["'自爱'的咨询循环（B365：because of his self-love）。",
 "'最深刻的作品'（B365：most profound work）。",
 "'大麻'的滑稽颂（B365：mock eulogy）。"],
"influence":[{"text":"Britannica：'Rabelais's most profound work'（B365）。","source":"B365"},{"text":"Britannica：索邦斥为异端与逃亡（B365 交叉）。","source":"B365"}],
"reading":{"difficulties":["咨询结构的多声部。","斯多葛-基督教语汇（B365）。"],
 "editions":["《第三书》中译名（《巨人传》第三部——通说待核）。","法文原版（公有领域）。"],
 "order":"《巨人传》第三部；接《第四书》。"},
"pending":["'神瓶'咨询细节核对（B365已载梗概）。","1546年出版（royal privilège说）待核。","'大麻'收尾的解读待核。"],
"sources":["B365"],"year_source":"B365","author_source":"B365","related_works":["jurenzhuan","xunjiexiaoshuo","mingnuzhuan"],
"svg":G("《第三书》咨询结构图",[{"title":"咨询","text":"自爱的循环（B365）","color":"main"},{"title":"神瓶","text":"旅途的决定（B365）","color":"gold"},{"title":"'最深刻'","text":"Britannica 之评（B365）","color":"family"},{"title":"大麻","text":"滑稽的颂歌（B365）","color":"antagonist"}])},
{"id":"1794nian","title":"1794年","original_title":"Rok 1794","region":"波兰","era":"近代","era_detail":"20世纪10-20年代",
"genre":"历史小说（三卷）","genre_group":"小说","language":"波兰语","author_id":"reymont","author_name":"弗拉迪斯拉夫·莱蒙特",
"year_display":"1913-18年（Britannica B342：Rok 1794, 3 vol. (1913-18)——'depicts Poland at the start of the partitions in the late 18th century'）","year_sort":1913,
"background":["Britannica（B342）：Rok 1794 三卷（1913-18）——'depicts Poland at the start of the partitions in the late 18th century'（波兰被瓜分初期）。","Britannica（B342）：莱蒙特——1924诺奖。","题材（通说待核）：柯希丘什科起义前夜——1794年的华沙。"],
"outline":["（通说待核）三卷的起义编年：最后的波兰。","（通说待核）柯希丘什科的'克拉科夫宣誓'（通说待核）。"],
"characters":[{"name":"柯希丘什科","identity":"起义领袖","note":"（通说待核）"}],
"themes":["瓜分初期的波兰（B342）。",
 "起义的编年（书名语境——通说待核）。",
 "历史小说的三卷（B342）。"],
"influence":[{"text":"Britannica：Rok 1794 (1913-18)（B342）。","source":"B342"},{"text":"Britannica：1924诺奖（B342 交叉）。","source":"B342"}],
"reading":{"difficulties":["柯希丘什科起义史。","三卷的编年。"],
 "editions":["《1794年》中译名（《最后的波兰》）待核。","波兰文原版（公有领域）。"],
 "order":"莱蒙特历史篇；与《农民》《福地》对读。"},
"pending":["三卷卷名核对（通说）。","1913-18出版细节待核（B342口径）。","柯希丘什科细节待核。"],
"sources":["B342"],"year_source":"B342","author_source":"B342","related_works":["nongmin","fudi","meiguobuqu"],
"svg":G("《1794年》起义编年图",[{"title":"1794","text":"瓜分初期的波兰（B342）","color":"main"},{"title":"起义","text":"最后的挣扎（通说）","color":"gold"},{"title":"三卷","text":"编年的结构（B342）","color":"family"},{"title":"诺奖","text":"1924（B342交叉）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批65）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('pishangguang','seifert','披光'),('telafunikejishi','andric','特拉夫尼克纪事'),('zhipiaobu','echegaray','支票簿'),('muxingdeshi','gmistral','母性的诗'),('canbai','kertesz','惨败'),('feizhouren','leclezio','非洲人'),('jiananzhihuo','pavese','艰难之活'),('disanshu','rabelais','第三书'),('1794nian','reymont','1794年')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH65 DONE')
