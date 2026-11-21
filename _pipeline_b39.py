# -*- coding: utf-8 -*-
"""批39：零成本 12 部二作（雨果×2/莱蒙托夫/屠格涅夫/肖洛霍夫/契诃夫/比昂松/卡尔杜齐/卡波特/卡佛/塞万提斯/冰心）"""
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

S_HU, S_LM, S_TU, S_SH, S_CH, S_BJ, S_CD, S_CA, S_CE, S_BI = (src_of(x) for x in ['hugo','lermontov','turgenev','sholokhov','chikefu','bjornson','carducci','capote','cervantes','bingxin'])
print('srcs:', S_HU, S_LM, S_TU, S_SH, S_CH, S_BJ, S_CD, S_CA, S_CE, S_BI)

works = [
{"id":"chengfaji","title":"惩罚集","original_title":"Les Châtiments","region":"法国","era":"近代","era_detail":"19世纪50年代",
"genre":"诗集","genre_group":"诗歌","language":"法语","author_id":"hugo","author_name":"维克多·雨果",
"year_display":"1853年（作者页注记：Britannica 列举——惩罚集（1853））","year_sort":1853,
"background":["作者页注记：惩罚集 (1853)、静观集 (1856)——'诗集两峰（Britannica 列举）'。","Britannica：雨果——1851年政变后流亡（作者页语境——待核）。","题材（通说待核）：对拿破仑三世的 satire 檄文——流亡者的政治怒火。"],
"outline":["（通说待核——Britannica未载篇目）政变黑史的诗体清算。","（通说待核）'黑夜'与'黎明'的道德对位。"],
"characters":[{"name":"抒情'我'","identity":"流亡者/先知","note":"（通说待核）"}],
"themes":["政治讽刺诗的巅峰（通说待核）。",
 "流亡伦理（1851政变语境——通说待核）。",
 "诗的人民性（通说待核）。"],
"influence":[{"text":"Britannica：'诗集两峰'（作者页注记）。","source":S_HU},{"text":"Britannica：雨果为浪漫主义领袖（作者页语境）。","source":S_HU}],
"reading":{"difficulties":["1851年十二月政变史。","讽刺诗的用典。"],
 "editions":["《惩罚集》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"雨果诗歌首选之一；与《静观集》对读。"},
"pending":["篇目（《4.v.o.》《黑夜》等）核对（Britannica未载）。","1853年出版（Brussels说）待核。","'流亡'细节待核。"],
"sources":[S_HU],"year_source":S_HU,"author_source":S_HU,"related_works":["baise shijie" if False else "jingjingdedunhe","lesmiserables" if "lesmiserables" in existing else "balideyouyu","diyuzhiji"],
"svg":G("《惩罚集》檄文结构图",[{"title":"政变","text":"历史的黑夜（通说）","color":"antagonist"},{"title":"流亡","text":"诗的立场（通说）","color":"main"},{"title":"檄文","text":"怒火的清算（B注记）","color":"gold"},{"title":"黎明","text":"人民的名字（通说）","color":"family"}])},
{"id":"jingguanji","title":"静观集","original_title":"Les Contemplations","region":"法国","era":"近代","era_detail":"19世纪50年代",
"genre":"诗集","genre_group":"诗歌","language":"法语","author_id":"hugo","author_name":"维克多·雨果",
"year_display":"1856年（作者页注记：Britannica 列举——静观集 (1856)）","year_sort":1856,
"background":["作者页注记：静观集 (1856)——'诗集两峰（Britannica 列举）'。","Britannica：雨果——浪漫主义领袖（作者页语境）。","题材（通说待核）：《昔日与今日》——以亡女莱奥波尔蒂娜为轴的生死之思。"],
"outline":["（通说待核）从'昔日'到'今日'：丧女之痛的两卷结构。","（通说待核）冥想与通灵的诗学。"],
"characters":[{"name":"抒情'我'","identity":"父亲/冥想者","note":"（通说待核）"}],
"themes":["丧女的哀歌（通说待核）。",
 "生死两卷的对称（通说待核）。",
 "浪漫主义的冥想诗（B注记语境）。"],
"influence":[{"text":"Britannica：'诗集两峰'（作者页注记）。","source":S_HU},{"text":"Britannica：雨果诗歌地位（作者页语境）。","source":S_HU}],
"reading":{"difficulties":["两卷结构的年代错位。","通灵诗学（《她的名字》等——通说待核）。"],
 "editions":["《静观集》中译本（人民文学等——通说待核）。","法文原版（公有领域）。"],
 "order":"雨果诗歌第二峰；与《惩罚集》对读。"},
"pending":["篇目核对（Britannica未载）。","1856年出版细节待核。","莱奥波尔蒂娜细节待核。"],
"sources":[S_HU],"year_source":S_HU,"author_source":S_HU,"related_works":["chengfaji","jingjingdedunhe","diyuzhiji"],
"svg":G("《静观集》生死对称图",[{"title":"昔日","text":"丧女之前（通说）","color":"family"},{"title":"今日","text":"冥想的诗学（通说）","color":"main"},{"title":"哀歌","text":"父亲的眼泪（通说）","color":"gold"},{"title":"通灵","text":"彼岸的问候（通说）","color":"antagonist"}])},
{"id":"emo","title":"恶魔","original_title":"Демон（The Demon）","region":"俄国","era":"近代","era_detail":"19世纪30-40年代",
"genre":"长诗","genre_group":"诗歌","language":"俄语","author_id":"lermontov","author_name":"米哈伊尔·莱蒙托夫",
"year_display":"作者页注记：Britannica 列举 Demon（成稿年份通说待核——生前未全刊）","year_sort":1841,
"background":["作者页注记：恶魔（The Demon）、假面舞会、姆采里——'诗与剧（Britannica 列举）'。","Britannica：莱蒙托夫——《当代英雄》作者（作者页语境）。","题材（通说待核）：天界'恶魔'对格鲁吉亚少女塔玛拉的爱——否定精神的挽歌。"],
"outline":["（通说待核）恶魔的飞翔与坠落：爱与毁灭。","（通说待核）塔玛拉的祈祷与死亡。"],
"characters":[{"name":"恶魔","identity":"否定之灵","note":"（B 书名人物）"},{"name":"塔玛拉","identity":"格鲁吉亚公主","note":"（通说待核）"}],
"themes":["'否定精神'的浪漫主义（通说待核）。",
 "拜伦式英雄的俄国变体（通说待核）。",
 "高加索的东方想象（通说待核）。"],
"influence":[{"text":"Britannica：Demon 列举（作者页注记）。","source":S_LM},{"text":"Britannica：莱蒙托夫为普希金之后最重要俄国诗人（作者页语境——待核）。","source":S_LM}],
"reading":{"difficulties":["浪漫主义长诗的语体。","圣经'堕落天使'原型。"],
 "editions":["《恶魔》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"莱蒙托夫诗歌首选；与《童僧》《姆采里》并读。"},
"pending":["成稿年份（1829-1841多稿说）待核。","塔玛拉人名核对（通说）。","生前刊印状态待核。"],
"sources":[S_LM],"year_source":S_LM,"author_source":S_LM,"related_works":["dangdaiyingxiong","pushkin-shiqing" if "pushkin-shiqing" in existing else "diyuzhiji","xuboliweng"],
"svg":G("《恶魔》否定结构图",[{"title":"恶魔","text":"否定的精灵（B注记）","color":"main"},{"title":"塔玛拉","text":"爱的瞬间（通说）","color":"gold"},{"title":"坠落","text":"毁灭的吻（通说）","color":"antagonist"},{"title":"高加索","text":"东方的舞台（通说）","color":"family"}])},
{"id":"luoting","title":"罗亭","original_title":"Рудин","region":"俄国","era":"近代","era_detail":"19世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"turgenev","author_name":"伊万·屠格涅夫",
"year_display":"1856年（作者页注记：Britannica——罗亭 (1856)）","year_sort":1856,
"background":["作者页注记：罗亭、贵族之家、前夜——'（Britannica 列举）'；B141：'1856《罗亭》1859《贵族之家》1860《前夜》'。","Britannica（B141）：屠格涅夫——《父与子》(1862)作者（交叉）。","题材（通说待核）：'多余人'罗亭——言辞的英雄与行动的侏儒。"],
"outline":["（通说待核）罗亭在达里娅庄园的雄辩与娜塔莉亚的考验。","（通说待核）'在哪里使用我的力量？'的失败回答。"],
"characters":[{"name":"罗亭","identity":"多余人","note":"（B141 书名人物）"},{"name":"娜塔莉亚","identity":"少女","note":"（通说待核）"}],
"themes":["'多余人'谱系（B141 语境）。",
 "言辞与行动的分裂（通说待核）。",
 "1840年代思想史（通说待核）。"],
"influence":[{"text":"Britannica：1856《罗亭》（B141 作者页注记）。","source":S_TU},{"text":"Britannica：屠格涅夫为俄国文学'四大家'语境（作者页交叉）。","source":S_TU}],
"reading":{"difficulties":["'多余人'文学谱系。","贵族庄园的沙龙语境。"],
 "editions":["《罗亭》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"屠格涅夫长篇首选之一；与《父与子》对读。"},
"pending":["罗亭/娜塔莉亚人名核对（通说）。","1856年发表（《现代人》说）待核。","结尾1848巴黎殉难细节待核。"],
"sources":[S_TU],"year_source":S_TU,"author_source":S_TU,"related_works":["fuyuzi","lierenbiji","dangdaiyingxiong"],
"svg":G("《罗亭》多余人结构图",[{"title":"罗亭","text":"言辞的英雄（B141）","color":"main"},{"title":"雄辩","text":"沙龙的光辉（通说）","color":"gold"},{"title":"考验","text":"行动的缺席（通说）","color":"antagonist"},{"title":"娜塔莉亚","text":"被辜负的爱情（通说）","color":"family"}])},
{"id":"beikaiyundechunudi","title":"被开垦的处女地","original_title":"Поднятая целина","region":"苏联","era":"现当代","era_detail":"20世纪30-50年代",
"genre":"长篇小说","genre_group":"小说","language":"俄语","author_id":"sholokhov","author_name":"米哈伊尔·肖洛霍夫",
"year_display":"1932-60年（作者页注记：Britannica——被开垦的处女地 (1932—60)）","year_sort":1932,
"background":["作者页注记：被开垦的处女地 (1932—60)——'集体化小说（Britannica）'。","Britannica（B098）：肖洛霍夫——1965诺奖；哥萨克作家。","题材（通说待核）：顿河集体化运动——农业集体化的村庄两卷。"],
"outline":["（通说待核）集体化：富农清算与集体农庄建立。","（通说待核）梅霍夫村的两条路线。"],
"characters":[{"name":"达维多夫","identity":"工人工作队长","note":"（通说待核）"},{"name":"梅霍夫村","identity":"集体化的舞台","note":"（通说待核）"}],
"themes":["集体化的叙事（B注记：集体化小说）。",
 "哥萨克社会的转型（B098 语境）。",
 "政策文学的内部张力（通说待核）。"],
"influence":[{"text":"Britannica：1965诺贝尔文学奖（B098）。","source":S_SH},{"text":"Britannica：《静静的顿河》——苏联最广泛阅读（B098 交叉）。","source":S_SH}],
"reading":{"difficulties":["农业集体化史。","'政策文学'的评价史。"],
 "editions":["《被开垦的处女地》中译本（人民文学等——通说待核）。","俄文原版。"],
 "order":"肖洛霍夫第二作；与《静静的顿河》《一个人的遭遇》对读。"},
"pending":["达维多夫人名核对（通说）。","两部年份（1932/1960）核对（B注记）。","'剽窃疑云'与本作关系待核（B098 载《静静的顿河》相关——本作不涉）。"],
"sources":[S_SH],"year_source":S_SH,"author_source":S_SH,"related_works":["jingjingdedunhe","yigerendeyu","nongmin"],
"svg":G("《被开垦的处女地》集体化图",[{"title":"集体化","text":"村庄的转型（B注记）","color":"main"},{"title":"顿河","text":"哥萨克的土地（B098）","color":"family"},{"title":"路线","text":"政策的张力（通说）","color":"antagonist"},{"title":"工作队","text":"外来者与村庄（通说）","color":"gold"}])},
{"id":"sanzimei","title":"三姊妹","original_title":"Три сестры（Three Sisters）","region":"俄国","era":"近代","era_detail":"20世纪初",
"genre":"戏剧","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
"year_display":"1901年（作者页注记：Britannica 列举——三姊妹 (1901)）","year_sort":1901,
"background":["作者页注记：海鸥（1896）、三姊妹 (1901)——'戏剧双峰（Britannica 列举）'。","Britannica（B270）：契诃夫——'Chekhovs gun'与'what is left unsaid'。","题材（通说待核）：普罗佐洛夫家三姊妹的'到莫斯科去'——岁月的流逝。"],
"outline":["（通说待核）三姊妹的莫斯科梦与就地扎根。","（通说待核）军旅的撤离与姐妹的坚守。"],
"characters":[{"name":"奥尔加/玛莎/伊琳娜","identity":"三姊妹","note":"（通说待核）"},{"name":"图森巴赫","identity":"求婚者","note":"（通说待核）"}],
"themes":["'到莫斯科去'的幻梦（通说待核）。",
 "时间的流逝与忍受（通说待核）。",
 "'未说出之重'（B270）。"],
"influence":[{"text":"Britannica：'戏剧双峰'（作者页注记）。","source":S_CH},{"text":"Britannica：契诃夫戏剧传统与莫斯科艺术剧院（B270 语境——待核）。","source":"B270"}],
"reading":{"difficulties":["'潜台词'与静止戏剧。","俄国军官社会。"],
 "editions":["《三姊妹》（人民文学出版社《契诃夫戏剧集》——通说待核）。","俄文原版（公有领域）。"],
 "order":"契诃夫戏剧之三；与《海鸥》《樱桃园》对读。"},
"pending":["三姊妹名字核对（通说）。","1901年首演（莫斯科艺术剧院说）待核。","结尾'生活还没有过去'台词待核。"],
"sources":[S_CH],"year_source":S_CH,"author_source":S_CH,"related_works":["haiou","yingtaoyuan","wanyaniuju"],
"svg":G("《三姊妹》流逝结构图",[{"title":"莫斯科","text":"永远的远方（通说）","color":"gold"},{"title":"三姊妹","text":"岁月的忍受（通说）","color":"main"},{"title":"军旅","text":"撤离的空虚（通说）","color":"antagonist"},{"title":"潜台词","text":"未说出之重（B270）","color":"family"}])},
{"id":"pochan","title":"破产","original_title":"En fallit（The Bankrupt）","region":"挪威","era":"近代","era_detail":"19世纪70年代",
"genre":"戏剧","genre_group":"戏剧","language":"挪威语","author_id":"bjornson","author_name":"比奥恩斯彻讷·比昂松",
"year_display":"1875年（Britannica B337：En fallit (1875)——戏剧）","year_sort":1875,
"background":["Britannica（B337）：En fallit (1875)——戏剧（'The Bankrupt'）。","Britannica（B337）：'his plays were influential in establishing social realism in Europe'。","题材（通说待核）：银行家特勒丹的破产——商业诚信的社会剧。"],
"outline":["（通说待核——B337未载剧情）破产者的道德清算。","（通说待核）'诚实的破产'与商业社会。"],
"characters":[{"name":"特勒丹","identity":"银行家","note":"（通说待核，B337未载）"}],
"themes":["商业伦理的社会剧（B337：social realism）。",
 "破产的道德性（书名语境——通说待核）。",
 "19世纪挪威资本主义（通说待核）。"],
"influence":[{"text":"Britannica：'influential in establishing social realism in Europe'（B337）。","source":"B337"},{"text":"Britannica：1903诺奖（B337 交叉）。","source":"B337"}],
"reading":{"difficulties":["北欧商业社会语境。","'社会剧'的形式。"],
 "editions":["《破产》中译本（人民文学等——通说待核）。","挪威文原版。"],
 "order":"比昂松戏剧首选；与《编辑》对读。"},
"pending":["特勒丹人名核对（B337未载）。","1875年首演细节待核。","与易卜生社会问题的关系待核。"],
"sources":["B337"],"year_source":"B337","author_source":"B337","related_works":["xinnuofusuobaken","peierjinte","jianghu"],
"svg":G("《破产》社会剧结构图",[{"title":"破产","text":"商业的道德（B337）","color":"antagonist"},{"title":"特勒丹","text":"诚实的重建（通说）","color":"main"},{"title":"社会剧","text":"现实主义的推动（B337）","color":"gold"},{"title":"家庭","text":"信用的牵连（通说）","color":"family"}])},
{"id":"sadansong","title":"撒旦颂","original_title":"Inno a Satana","region":"意大利","era":"近代","era_detail":"19世纪60年代",
"genre":"长诗","genre_group":"诗歌","language":"意大利语","author_id":"carducci","author_name":"焦苏埃·卡尔杜齐",
"year_display":"1863年（Britannica B345：Inno a Satana (1863)）","year_sort":1863,
"background":["Britannica（B345）：Inno a Satana——'showing his republican, anticlerical feeling'（共和反教权情绪）。","Britannica（B345）：卡尔杜齐——1906诺奖；'one of the most influential literary figures of his age'。","题材（通说待核）：'撒旦'作为反叛与理性的隐喻——对教会罗马的挑战。"],
"outline":["（通说待核）'撒旦'的意象：不是恶魔而是叛逆的理性与美。","（通说待核）从瓦尔斯到人类进步的颂歌。"],
"characters":[{"name":"撒旦（意象）","identity":"反叛与理性","note":"（B345：hymn to Satan——意象细节通说待核）"}],
"themes":["共和反教权的政治诗（B345）。",
 "'撒旦'的翻案（通说待核）。",
 "古典异教的荣光（B345：Odi barbare 语境交叉）。"],
"influence":[{"text":"Britannica：'his hymn to Satan, showing his republican, anticlerical feeling'（B345）。","source":"B345"},{"text":"Britannica：1906诺奖（B345 交叉）。","source":"B345"}],
"reading":{"difficulties":["'撒旦'的隐喻系统。","意大利统一运动史。"],
 "editions":["《撒旦颂》中译本（人民文学等——通说待核）。","意大利文原版（公有领域）。"],
 "order":"卡尔杜齐政治诗首选；与《野蛮颂》对读。"},
"pending":["意象细节核对（通说）。","1863年发表细节待核。","'颂歌'结构待核。"],
"sources":["B345"],"year_source":"B345","author_source":"B345","related_works":["yemanli","diyuzhiji","chengfaji"],
"svg":G("《撒旦颂》反叛结构图",[{"title":"撒旦","text":"理性的反叛（B345语境）","color":"main"},{"title":"教会","text":"被挑战的罗马（通说）","color":"antagonist"},{"title":"进步","text":"人类的颂歌（通说）","color":"gold"},{"title":"共和","text":"政治的信念（B345）","color":"family"}])},
{"id":"biedeshengyin","title":"别的声音，别的房间","original_title":"Other Voices, Other Rooms","region":"美国","era":"现当代","era_detail":"20世纪40年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"capote","author_name":"杜鲁门·卡波特",
"year_display":"1948年（Britannica B332：Other Voices, Other Rooms (1948)——处女作）","year_sort":1948,
"background":["Britannica（B332）：Other Voices, Other Rooms——'a sensitive, partly autobiographical portrayal of a boy's search for his father'（一个男孩寻找父亲的敏感的、部分自传性的描写）。","Britannica（B332）：卡波特处女作长篇。","题材（通说待核）：少年乔尔在南方老宅的寻父之旅。"],
"outline":["（通说待核）被弃少年赴南方破败庄园寻父。","（通说待核）'别的声音'：宅中的怪人与自我确认。"],
"characters":[{"name":"乔尔·诺克斯","identity":"寻父少年","note":"（通说待核，B332未载）"}],
"themes":["寻父与身份（B332：boy's search for his father）。",
 "南方哥特（B332 语境——待核）。",
 "青春的自我认识（通说待核）。"],
"influence":[{"text":"Britannica：'partly autobiographical portrayal of a boy's search for his father'（B332）。","source":"B332"},{"text":"Britannica：卡波特处女作（B332）。","source":"B332"}],
"reading":{"difficulties":["南方哥特氛围。","半自传的传记对应。"],
 "editions":["《别的声音，别的房间》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"卡波特首作；与《蒂凡尼的早餐》《冷血》对读。"},
"pending":["乔尔·诺克斯人名核对（B332未载）。","1948年出版（Random House说）待核。","'别的房间'意象细节待核。"],
"sources":["B332"],"year_source":"B332","author_source":"B332","related_works":["lengxue","difannidezaocan","jianjiaogelou"],
"svg":G("《别的声音，别的房间》寻父图",[{"title":"乔尔","text":"寻父的少年（B332）","color":"main"},{"title":"老宅","text":"南方的哥特（通说）","color":"family"},{"title":"父亲","text":"缺席的目标（B332）","color":"antagonist"},{"title":"自我","text":"青春的确认（通说）","color":"gold"}])},
{"id":"datangyuan","title":"大教堂","original_title":"Cathedral","region":"美国","era":"现当代","era_detail":"20世纪80年代初",
"genre":"短篇小说集","genre_group":"故事集","language":"英语","author_id":"carver","author_name":"雷蒙德·卡佛",
"year_display":"1984年（作者页注记：Britannica——Cathedral (1984)）","year_sort":1984,
"background":["作者页注记：大教堂——'（Britannica：1984）'。","Britannica：卡佛——极简主义（minimalism）代表（作者页语境——待核）。","题材（通说待核）：普通人的失语与片刻的敞开——盲人与'大教堂'的共绘。"],
"outline":["（通说待核）同名篇：'我'与盲人共绘大教堂。","（通说待核）中产失业者的黄昏。"],
"characters":[{"name":"'我'","identity":"失语者","note":"（通说待核）"},{"name":"盲人（罗伯特说）","identity":"来访者","note":"（通说待核）"}],
"themes":["极简主义与'空缺'（作者页语境——通说待核）。",
 "日常语流的转机（通说待核）。",
 "观看与看见（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：Cathedral (1984)（作者页注记）。","source":src_of('carver')},{"text":"Britannica：卡佛'极简主义'定位（作者页语境——待核）。","source":src_of('carver')}],
"reading":{"difficulties":["极简句法的留白。","1980年代美国失业潮背景（通说待核）。"],
 "editions":["《大教堂》中译本（人民文学/南海等——通说待核）。","英文原版。"],
 "order":"卡佛中期首选；与《当我们谈论爱情时我们在谈论什么》对读。"},
"pending":["同名篇细节核对（通说）。","1984年出版（Knopf说）待核。","'极简主义'标签的学术争议待核。"],
"sources":[src_of('carver')],"year_source":src_of('carver'),"author_source":src_of('carver'),"related_works":["zhufan" if "zhufan" in existing else "leiyu","wuhao","ershisou"],
"svg":G("《大教堂》敞开结构图",[{"title":"盲人","text":"看不见的引导（通说）","color":"gold"},{"title":"共绘","text":"纸上 closures（通说）","color":"main"},{"title":"失语","text":"日常的空缺（通说）","color":"antagonist"},{"title":"敞开","text":"极简的转机（B注记语境）","color":"family"}])},
{"id":"xunjiexiaoshuo","title":"训诫小说集","original_title":"Novelas ejemplares","region":"西班牙","era":"近代","era_detail":"17世纪初",
"genre":"短篇小说集","genre_group":"故事集","language":"西班牙语","author_id":"cervantes","author_name":"米格尔·德·塞万提斯",
"year_display":"1613年（作者页注记：Britannica——训诫小说集 (1613)——'有些篇章接近《堂吉诃德》的微缩水准'）","year_sort":1613,
"background":["作者页注记：训诫小说集 (1613)——'有些篇章接近《堂吉诃德》的微缩水准'（Britannica：attain a level close to that...）。","Britannica：塞万提斯——《堂吉诃德》作者（作者页语境）。","题材（通说待核）：十二篇'训诫'小说——流浪汉、爱情与道德教训。"],
"outline":["（通说待核）十二篇的多样性：吉普赛人、两犬对话、英国西班牙女子。","（通说待核）'训诫'与写实的平衡。"],
"characters":[{"name":"众篇人物","identity":"——","note":"（通说待核）"}],
"themes":["'微缩的堂吉诃德'（Britannica 引语——注记）。",
 "流浪汉小说传统（通说待核）。",
 "道德训诫与世俗写作（通说待核）。"],
"influence":[{"text":"Britannica：'有些篇章接近《堂吉诃德》的微缩水准'（作者页注记）。","source":S_CE},{"text":"Britannica：塞万提斯为现代小说开创者之一（作者页语境）。","source":S_CE}],
"reading":{"difficulties":["黄金世纪西班牙语。","'训诫'（ejemplar）的含义。"],
 "editions":["《训诫小说集》中译本（人民文学等——通说待核）。","西班牙文原版（公有领域）。"],
 "order":"《堂吉诃德》后的延伸阅读。"},
"pending":["篇目（《吉普赛姑娘》《狗的对话》等）核对（通说）。","1613年出版（Madrid说）待核。","'十二篇'数量核对。"],
"sources":[S_CE],"year_source":S_CE,"author_source":S_CE,"related_works":["tangjihuade","teluoyiluosi" if False else "leiyu","luoting"],
"svg":G("《训诫小说集》微缩结构图",[{"title":"十二篇","text":"微缩的堂吉诃德（B注记）","color":"gold"},{"title":"流浪汉","text":"西班牙的街头（通说）","color":"main"},{"title":"训诫","text":"道德与写实（通说）","color":"family"},{"title":"黄金世纪","text":"语言的巅峰（通说）","color":"antagonist"}])},
{"id":"jixiaoduzhe","title":"寄小读者","original_title":"寄小读者","region":"中国","era":"近代","era_detail":"20世纪20年代",
"genre":"通讯散文集","genre_group":"散文","language":"汉语","author_id":"bingxin","author_name":"冰心",
"year_display":"1926年（Britannica：1926——作者页注记）","year_sort":1926,
"background":["作者页注记：寄小读者——'（Britannica：1926）'。","Britannica：冰心——现代中国女作家（作者页语境）。","题材（通说待核）：1923-26赴美通讯——'爱的哲学'与儿童读者。"],
"outline":["（通说待核）二十九封通讯：从上海到威尔斯利。","（通说待核）'爱的哲学'：母爱、童心与自然。"],
"characters":[{"name":"'我'","identity":"通讯作者","note":"（通说待核）"}],
"themes":["'爱的哲学'（通说待核）。",
 "儿童文学的开创（B注记语境）。",
 "白话文的柔美实验（通说待核）。"],
"influence":[{"text":"Britannica：寄小读者 (1926)（作者页注记）。","source":S_BI},{"text":"Britannica：冰心为中国现代文学代表作家（作者页语境）。","source":S_BI}],
"reading":{"difficulties":["通讯体与散文的边界。","'新文学'早期的语言实验。"],
 "editions":["《寄小读者》（人民文学出版社《冰心全集》等——通说待核）。","1926年北新书局说待核。"],
 "order":"冰心散文首选；与《繁星》《春水》对读。"},
"pending":["通讯篇数（二十九封说）核对（通说）。","1926年结集细节待核。","'爱的哲学'提法出处待核。"],
"sources":[S_BI],"year_source":S_BI,"author_source":S_BI,"related_works":["fanxing","chunshui","chengfaji"],
"svg":G("《寄小读者》通讯结构图",[{"title":"二十九封","text":"越洋的通讯（通说）","color":"main"},{"title":"爱的哲学","text":"母爱与童心（通说）","color":"gold"},{"title":"儿童","text":"最初的读者（B注记）","color":"family"},{"title":"白话","text":"柔美的实验（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批39）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('chengfaji','hugo','惩罚集'),('jingguanji','hugo','静观集'),('emo','lermontov','恶魔'),('luoting','turgenev','罗亭'),('beikaiyundechunudi','sholokhov','被开垦的处女地'),('sanzimei','chikefu','三姊妹'),('pochan','bjornson','破产'),('sadansong','carducci','撒旦颂'),('biedeshengyin','capote','别的声音'),('datangyuan','carver','大教堂'),('xunjiexiaoshuo','cervantes','训诫'),('jixiaoduzhe','bingxin','寄小读者')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH39 DONE')
