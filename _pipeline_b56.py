# -*- coding: utf-8 -*-
"""批56：零成本 8 部（黄昏/民族轶事/丰乳肥臀/继承者/旋律与对位/吾国与吾民/论俗语/三故事）"""
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
{"id":"huanghun","title":"黄昏","original_title":"Вечер（Evening）","region":"俄国","era":"近代","era_detail":"20世纪10年代",
"genre":"诗集","genre_group":"诗歌","language":"俄语","author_id":"akhmatova","author_name":"安娜·阿赫玛托娃",
"year_display":"1912年（作者页注记：Britannica——黄昏 (1912)——早期）","year_sort":1912,
"background":["作者页注记：黄昏 (1912)、念珠 (1914)——'早期（Britannica）'。","Britannica：阿赫玛托娃——俄国女诗人（作者页语境）。","题材（通说待核）：首部诗集——爱情短诗与'黄昏'的色调。"],
"outline":["（通说待核）46首短诗的首集。","（通说待核）'我披上右手的手套'（不采为引文）。"],
"characters":[{"name":"抒情'我'","identity":"女诗人","note":"（通说待核）"}],
"themes":["爱情短诗的首集（B注记语境）。",
 "'黄昏'的色调（书名——通说待核）。",
 "阿克梅派前奏（流派说待核）。"],
"influence":[{"text":"Britannica：黄昏 (1912)——早期（作者页注记）。","source":src_of('akhmatova')},{"text":"Britannica：《安魂曲》为代表作（作者页交叉）。","source":src_of('akhmatova')}],
"reading":{"difficulties":["首集的格律。","'阿克梅派'归属（待核）。"],
 "editions":["《黄昏》中译本（人民文学等——通说待核）。","俄文原版（公有领域）。"],
 "order":"阿赫玛托娃首集；后接《念珠》。"},
"pending":["篇数（46首说）核对（通说）。","1912年出版细节待核。","'阿克梅派'归属核对。"],
"sources":[src_of('akhmatova')],"year_source":src_of('akhmatova'),"author_source":src_of('akhmatova'),"related_works":["nianzhu","anhusiqu" if "anhusiqu" in existing else "leiyu","ezhihua"],
"svg":G("《黄昏》首集结构图",[{"title":"黄昏","text":"爱情的光线（书名）","color":"gold"},{"title":"首集","text":"46首短诗（通说）","color":"main"},{"title":"早期","text":"B注记的位置","color":"family"},{"title":"阿克梅","text":"流派的序曲（通说）","color":"antagonist"}])},
{"id":"minzuyishi","title":"民族轶事","original_title":"Episodios nacionales","region":"西班牙","era":"近代","era_detail":"19世纪70年代—20世纪初",
"genre":"历史小说系列（46部）","genre_group":"小说","language":"西班牙语","author_id":"galdos","author_name":"贝尼托·佩雷斯·加尔多斯",
"year_display":"1873-1912年（Britannica B370：Episodios nacionales——46-novel historical series covering 1805-1874）","year_sort":1873,
"background":["Britannica（B370）：'innovatively recreated Spain's 19th-century history'——46部系列覆盖1805-1874。","Britannica（B370）：加尔多斯——'the greatest Spanish novelist since Cervantes'。","题材（通说待核）：从特拉法尔加到王政复现——西班牙19世纪的编年。"],
"outline":["（通说待核）五个系列的分期（通说待核）。","（通说待核）'萨尔瓦多·蒙萨尔维'等贯穿人物。"],
"characters":[{"name":"蒙萨尔维","identity":"贯穿人物","note":"（通说待核）"}],
"themes":["'民族轶事'：历史的小说化（B370）。",
 "西班牙19世纪的编年（B370：1805-1874）。",
 "巴尔扎克式的人物复现（B370 对照）。"],
"influence":[{"text":"Britannica：46-novel series（B370）。","source":"B370"},{"text":"Britannica：'recreated Spain's 19th-century history'（B370）。","source":"B370"}],
"reading":{"difficulties":["46部的体量。","西班牙编年史（通说待核）。"],
 "editions":["《民族轶事》中译名（《国民轶事》）待核。","西班牙文原版（公有领域）。"],
 "order":"加尔多斯历史篇；选读首尾各两部。"},
"pending":["46部书单核对（通说）。","'贯穿人物'说待核。","1873年首部（La batalla de los Arapiles说）待核。"],
"sources":["B370"],"year_source":"B370","author_source":"B370","related_works":["fortunata","nongmin","meiguobuqu"],
"svg":G("《民族轶事》编年结构图",[{"title":"46部","text":"西班牙的编年（B370）","color":"main"},{"title":"历史","text":"1805-1874（B370）","color":"gold"},{"title":"轶事","text":"个人的入口（书名）","color":"family"},{"title":"现实","text":"小说的化用（B370）","color":"antagonist"}])},
{"id":"fengrufeibi","title":"丰乳肥臀","original_title":"丰乳肥臀","region":"中国","era":"近代","era_detail":"20世纪90年代",
"genre":"长篇小说","genre_group":"小说","language":"汉语","author_id":"moyan","author_name":"莫言",
"year_display":"1995年（作者页注记：Britannica 列举——丰乳肥臀 (1995)）","year_sort":1995,
"background":["作者页注记：丰乳肥臀 (1995)、檀香刑 (2001)——'重要长篇（Britannica 列举）'。","Britannica：莫言——2012诺奖（作者页交叉——待核）。","题材（通说待核）：上官鲁氏与九个子女——从抗战到90年代的母系史诗。"],
"outline":["（通说待核）母亲与金童：多子女的世纪苦难。","（通说待核）'丰乳肥臀'：母性身体的纪念碑。"],
"characters":[{"name":"上官鲁氏","identity":"母亲","note":"（通说待核）"},{"name":"金童","identity":"独子","note":"（通说待核）"}],
"themes":["母性史诗（书名语境——通说待核）。",
 "20世纪中国的家族史（通说待核）。",
 "'重要长篇'（B注记）。"],
"influence":[{"text":"Britannica：'重要长篇'（作者页注记）。","source":src_of('moyan')},{"text":"Britannica：莫言2012诺奖（作者页交叉——待核）。","source":src_of('moyan')}],
"reading":{"difficulties":["高密东北乡世系。","'魔幻乡土'的语体（通说待核）。"],
 "editions":["《丰乳肥臀》（作家出版社等——通说待核）。","1995年《大家》连载说待核。"],
 "order":"莫言长篇首选；与《檀香刑》《红高粱》对读。"},
"pending":["上官鲁氏人名核对（通说）。","1995年出版细节待核。","'母系史诗'说法待核。"],
"sources":[src_of('moyan')],"year_source":src_of('moyan'),"author_source":src_of('moyan'),"related_works":["tanxiangxing","honggaoliang" if "honggaoliang" in existing else "kanbujian3","nongmin"],
"svg":G("《丰乳肥臀》母性史诗图",[{"title":"母亲","text":"身体的纪念碑（通说）","color":"main"},{"title":"九子女","text":"世纪的分岔（通说）","color":"family"},{"title":"丰乳肥臀","text":"命名的大地（书名）","color":"gold"},{"title":"高密","text":"魔幻的乡土（通说）","color":"antagonist"}])},
{"id":"jichengzhe","title":"继承者","original_title":"The Inheritors","region":"英国","era":"近代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"golding","author_name":"威廉·戈尔丁",
"year_display":"1955年（作者页注记：Britannica 列举——继承者 (1955)——塔尖 (1964)）","year_sort":1955,
"background":["作者页注记：继承者 (1955)、塔尖 (1964)——'（Britannica 列举）'。","Britannica：戈尔丁——《蝇王》作者、1983诺奖（作者页交叉——待核）。","题材（通说待核）：尼安德特人的'我们'视角——智利人（现代智人）的到来。"],
"outline":["（通说待核）'我们'的集体视点：洛卡的族人。","（通说待核）'新人'的暴力与'我们'的消亡。"],
"characters":[{"name":"洛卡","identity":"尼安德特长老","note":"（通说待核）"}],
"themes":["视点的倒转：'我们'是猎人眼中的'他者'（通说待核）。",
 "文明的暴力（B注记语境——与《蝇王》对读）。",
 "'继承'的反讽（书名语境）。"],
"influence":[{"text":"Britannica：列举（作者页注记）。","source":src_of('golding')},{"text":"Britannica：1983诺奖（作者页交叉——待核）。","source":src_of('golding')}],
"reading":{"difficulties":["集体第一人称。","史前人类学的想象（通说待核）。"],
 "editions":["《继承者》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"戈尔丁第二作；与《蝇王》对读。"},
"pending":["洛卡人名核对（通说）。","1955年出版细节待核。","'集体视点'技巧细节待核。"],
"sources":[src_of('golding')],"year_source":src_of('golding'),"author_source":src_of('golding'),"related_works":["yingwang","guojideyishi","wumingdeqiude"],
"svg":G("《继承者》视点倒转图",[{"title":"'我们'","text":"尼安德特人（通说）","color":"main"},{"title":"'新人'","text":"智利的暴力（通说）","color":"antagonist"},{"title":"继承","text":"世界的易主（书名）","color":"gold"},{"title":"视点","text":"倒转的技巧（通说）","color":"family"}])},
{"id":"xuanlvyuduwei","title":"旋律与对位","original_title":"Point Counter Point","region":"英国","era":"近代","era_detail":"20世纪20年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"huxley","author_name":"阿道司·赫胥黎",
"year_display":"1928年（作者页注记：Britannica 列举——旋律与对位 (1928)）","year_sort":1928,
"background":["作者页注记：旋律与对位 (1928)、加数加 (1936)——'小说（Britannica 列举）'。","Britannica：赫胥黎——《美丽新世界》作者（作者页交叉）。","题材（通说待核）：多线人物的'对位'——音乐化的小说结构。"],
"outline":["（通说待核）伦敦知识圈的群像：菲利普·夸尔斯的'音乐化'小说理论。","（通说待核）'对位'：情节的复调。"],
"characters":[{"name":"菲利普·夸尔斯","identity":"小说家","note":"（通说待核）"},{"name":"莫兰德","identity":"漫画家","note":"（通说待核）"}],
"themes":["'对位法'的小说结构（书名语境——通说待核）。",
 "知识圈的讽刺（通说待核）。",
 "'小说中的小说'（通说待核）。"],
"influence":[{"text":"Britannica：Point Counter Point (1928)（作者页注记）。","source":src_of('huxley')},{"text":"Britannica：《美丽新世界》为代表作（作者页交叉）。","source":src_of('huxley')}],
"reading":{"difficulties":["多线复调。","1920年代英国知识圈。"],
 "editions":["《旋律与对位》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"赫胥黎现实主义篇；与《美丽新世界》对读。"},
"pending":["夸尔斯/莫兰德人名核对（通说）。","1928年出版细节待核。","'音乐化'结构说法待核。"],
"sources":[src_of('huxley')],"year_source":src_of('huxley'),"author_source":src_of('huxley'),"related_works":["meilixinxshijie" if "meilixinxshijie" in existing else "leiyu","meiguobuqu","weite"],
"svg":G("《旋律与对位》复调结构图",[{"title":"对位","text":"复调的结构（书名）","color":"gold"},{"title":"群像","text":"知识圈的讽刺（通说）","color":"main"},{"title":"小说中的小说","text":"元叙事（通说）","color":"family"},{"title":"1928","text":"B注记之年","color":"antagonist"}])},
{"id":"wuguoyuwumin","title":"吾国与吾民","original_title":"My Country and My People","region":"中国","era":"近代","era_detail":"20世纪30年代",
"genre":"文化论著","genre_group":"散文","language":"英语","author_id":"linyutang","author_name":"林语堂",
"year_display":"1935年（作者页注记：Britannica——吾国与吾民 (1935)、生活的艺术 (1937)——'英文中国介绍'）","year_sort":1935,
"background":["作者页注记：吾国与吾民 (1935)、生活的艺术 (1937)——'英文中国介绍（Britannica）'。","Britannica：林语堂——向西方介绍中国的作家（作者页语境）。","题材（通说待核）：中国人的性格、心灵与理想——英文世界中国观的名著。"],
"outline":["（通说待核）'中国人的心灵'与'人生的理想'两编。","（通说待核）老庄与孔孟的性格分析。"],
"characters":[{"name":"（文化论著无人物）","identity":"——","note":"文化随笔"}],
"themes":["向英文世界介绍中国（B注记）。",
 "'心灵与理想'的民族自省（通说待核）。",
 "幽默与闲适的哲学（作者页语境——待核）。"],
"influence":[{"text":"Britannica：'英文中国介绍'（作者页注记）。","source":src_of('linyutang')},{"text":"Britannica：林语堂《京华烟云》等（作者页交叉——待核）。","source":src_of('linyutang')}],
"reading":{"difficulties":["英文写作中的中国术语。","1930年代的国际语境。"],
 "editions":["《吾国与吾民》（湖南文艺等——通说待核）。","1935年Reynal & Hitchcock说待核。"],
 "order":"林语堂英文首选；后接《生活的艺术》。"},
"pending":["1935年出版细节待核。","两编结构核对（通说）。","'赛珍珠序'说待核。"],
"sources":[src_of('linyutang')],"year_source":src_of('linyutang'),"author_source":src_of('linyutang'),"related_works":["jinghuayanyun" if "jinghuayanyun" in existing else "leiyu","xiaoshuoshilue","gududemigong"],
"svg":G("《吾国与吾民》介绍结构图",[{"title":"吾国","text":"英文里的中国（书名）","color":"main"},{"title":"心灵","text":"民族的自省（通说）","color":"gold"},{"title":"幽默","text":"闲适的哲学（作者页语境）","color":"family"},{"title":"1935","text":"B注记之年","color":"antagonist"}])},
{"id":"lunsuyu","title":"论俗语","original_title":"De vulgari eloquentia","region":"意大利","era":"古代","era_detail":"14世纪初",
"genre":"语言学论著","genre_group":"散文","language":"拉丁语","author_id":"dante","author_name":"但丁",
"year_display":"作者页注记：Britannica 列举——论俗语（俗语理论——成书年份通说待核——约1303-05说）","year_sort":1304,
"background":["作者页注记：论俗语——'俗语理论（Britannica 列举）'。","Britannica：但丁——《神曲》以俗语写成（作者页交叉）。","题材（通说待核）：为俗语辩护——'光辉的俗语'（vulgare illustre）的探求。"],
"outline":["（通说待核）二卷：俗语优于拉丁语与'光辉俗语'的探求。","（通说待核）第二卷（未完成）：诗的俗语用法。"],
"characters":[{"name":"（论著无人物）","identity":"——","note":"语言学论著"}],
"themes":["'光辉的俗语'（通说待核）。",
 "拉丁语与俗语之辩（B注记语境）。",
 "意大利语的形成（通说待核）。"],
"influence":[{"text":"Britannica：'俗语理论'（作者页注记）。","source":src_of('dante')},{"text":"Britannica：《神曲》的俗语写作（作者页交叉）。","source":src_of('dante')}],
"reading":{"difficulties":["中世纪语言学。","'光辉俗语'的概念。"],
 "editions":["《论俗语》中译本（人民文学等——通说待核）。","拉丁文原版（公有领域）。"],
 "order":"但丁语言论；与《新生》《帝制论》对读。"},
"pending":["二卷结构核对（通说）。","约1303-05成书年份待核。","'光辉俗语'细节待核。"],
"sources":[src_of('dante')],"year_source":src_of('dante'),"author_source":src_of('dante'),"related_works":["xinshengbutan","dizhilun","laokong"],
"svg":G("《论俗语》语言结构图",[{"title":"俗语","text":"辩护的对象（书名）","color":"main"},{"title":"光辉","text":"'vulgare illustre'（通说）","color":"gold"},{"title":"拉丁","text":"对照的语言（通说）","color":"antagonist"},{"title":"意大利语","text":"形成的理论（通说）","color":"family"}])},
{"id":"sangushi","title":"三故事","original_title":"Trois contes","region":"法国","era":"近代","era_detail":"19世纪70年代",
"genre":"短篇小说集","genre_group":"故事集","language":"法语","author_id":"flaubert","author_name":"居斯塔夫·福楼拜",
"year_display":"1877年（作者页注记：Britannica 列举——三故事 (1877)）","year_sort":1877,
"background":["作者页注记：三故事 (1877)——'历史小说与短篇杰作（Britannica 列举）'。","Britannica：福楼拜——文体家（作者页交叉）。","题材（通说待核）：《一颗简单的心》《圣朱利安传奇》《希罗狄亚》三篇。"],
"outline":["（通说待核）全福的一生：从女仆到鹦鹉的圣像化。","（通说待核）中世纪传奇与圣经故事的改写。"],
"characters":[{"name":"全福","identity":"女仆","note":"（通说待核）"},{"name":"圣朱利安","identity":"传奇骑士","note":"（通说待核）"}],
"themes":["'简单的心'的圣徒化（通说待核）。",
 "三时代的结构（古/中世纪/圣经——通说待核）。",
 "'短篇杰作'（B注记）。"],
"influence":[{"text":"Britannica：'短篇杰作'（作者页注记）。","source":src_of('flaubert')},{"text":"Britannica：福楼拜文体（作者页交叉）。","source":src_of('flaubert')}],
"reading":{"difficulties":["三篇的时代跨度。","'圣徒传'的戏仿（通说待核）。"],
 "editions":["《三故事》中译名（《三个故事》）待核。","法文原版（公有领域）。"],
 "order":"福楼拜短篇首选；与《包法利夫人》对读。"},
"pending":["三篇标题核对（通说）。","1877年出版细节待核。","'鹦鹉'细节待核。"],
"sources":[src_of('flaubert')],"year_source":src_of('flaubert'),"author_source":src_of('flaubert'),"related_works":["salangbo","qingganjiaoyu","mengya"],
"svg":G("《三故事》三时代结构图",[{"title":"简单的心","text":"女仆的圣像（通说）","color":"main"},{"title":"三时代","text":"古/中世纪/圣经（通说）","color":"gold"},{"title":"文体","text":"'杰作'的凝练（B注记）","color":"family"},{"title":"鹦鹉","text":"祭坛的传奇（通说）","color":"antagonist"}])},
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批56）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('huanghun','akhmatova','黄昏'),('minzuyishi','galdos','民族轶事'),('fengrufeibi','moyan','丰乳肥臀'),('jichengzhe','golding','继承者'),('xuanlvyuduwei','huxley','旋律与对位'),('wuguoyuwumin','linyutang','吾国与吾民'),('lunsuyu','dante','论俗语'),('sangushi','flaubert','三故事')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH56 DONE')
