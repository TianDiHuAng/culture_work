# -*- coding: utf-8 -*-
"""批45：Britannica 新核 2 作家 4 部（施托姆×2 B367/莱辛×2 B368）"""
import json, pathlib

newsrc = [
{"id":"B367","title":"Theodor Woldsen Storm — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Theodor-Woldsen-Storm","type":"百科全书","verified":True,"covers":["storm","yinmenghu"],"note":"2026-11-21 核对：1817-09-14石勒苏益格胡苏姆生—1888-07-04 Hademarschen卒（70岁）；'an outstanding representative of German poetic Realism'——该运动旨在'the portrayal of the positive values of everyday life'；'his novellas are among the finest in German literature'——成熟期'subtler psychological insight, greater realism, and a wider scope of themes'；律师/法官生涯：胡苏姆执业至1853（丹麦占领后迁波茨坦）、Heiligenstadt 任法官、1864返胡苏姆、1880退休；Immensee (1850)——'a moving story of the vanished happiness of childhood'——'a haunting nostalgia'——首部中篇、最受欢迎、框架叙事；Der Schimmelreiter (1888；The Rider on the White Horse / The Dykemaster)——'his last and greatest novella'——'its forceful hero and terse, objective style'——'vivid imagination and great narrative verve'——1888年4月刊于 Deutsche Rundschau；Gedichte (1852)——'love, nature, and an intense love of homeland'；Im Schloss (1861)、Tiefe Schatten (1865，丧妻后)、Pole Poppenspäler (1874)、Aquis submersus (1875历史中篇)；蒙森1838-43与其合著 Liederbuch dreier Freunde（B363 交叉）"},
{"id":"B368","title":"Gotthold Ephraim Lessing — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Gotthold-Ephraim-Lessing","type":"百科全书","verified":True,"covers":["lessing","zhainazhitan"],"note":"2026-11-21 核对：1729-01-22萨克森Kamenz生—1781-02-15 Braunschweig卒（52岁）；'He helped free German drama from the influence of classical and French models and wrote plays of lasting importance.'；Miss Sara Sampson 1755首演——德语文学第一部重要市民悲剧（bürgerliches Trauerspiel）；Minna von Barnhelm (1767)——'marks the birth of classical German comedy'；Laokoon (1766)——'Lessing attempted to fundamentally define the separate functions of painting and of poetry'；Hamburgische Dramaturgie (1767-69)——104篇短论——评50余场演出——'emphasizing pity and compassion and influencing the Sturm und Drang movement'；Emilia Galotti (1772)；Nathan der Weise (1779)——'His final drama...advocates for religious tolerance during the Crusades'——'The play suggests that ethical conduct, rather than dogma or prejudice, should determine the value of a religion.'；1746莱比锡学神学、1748避债逃柏林；Breslau任陶恩齐恩将军秘书(1760)；与伏尔泰争吵被腓特烈大帝拒图书馆馆长；友门德尔松与尼柯莱"},
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

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

authors = [
{"id":"storm","name":"特奥多尔·施托姆","foreign_name":"Theodor Woldsen Storm（特奥多尔·施托姆，1817-09-14—1888-07-04）","country":"德国","birth":1817,"death":1888,"birth_year":1817,"death_year":1888,"era":"近代",
"summary":"施托姆，石勒苏益格胡苏姆生，德国小说家与诗人——'an outstanding representative of German poetic Realism'（德国诗意现实主义的杰出代表——B367）——该运动旨在'the portrayal of the positive values of everyday life'（B367）。'his novellas are among the finest in German literature'（B367）。Immensee（茵梦湖, 1850）——'a moving story of the vanished happiness of childhood'——'a haunting nostalgia'（B367）；Der Schimmelreiter（白马骑士, 1888）——'his last and greatest novella'——'its forceful hero and terse, objective style'（B367）。律师与法官生涯：1853年因丹麦占领迁出胡苏姆（B367）。",
"timeline":[
 {"year":1817,"text":"9月14日生于胡苏姆（B367）。","src":"B367"},
 {"year":1850,"text":"Immensee（茵梦湖）——首部中篇（B367）。","src":"B367"},
 {"year":1853,"text":"丹麦占领下迁往波茨坦（B367）。","src":"B367"},
 {"year":1888,"text":"Der Schimmelreiter 4月刊于 Deutsche Rundschau；7月4日卒（B367）。","src":"B367"}],
"major_works":[
 {"work_id":"yinmenghu","note":"1850（B367）"},
 {"work_id":"baimaqishi","note":"1888（B367）"},
 {"title":"诗集","note":"（B367：Gedichte (1852)）"}],
"style":["诗意现实主义（B367：German poetic Realism）。",
 "框架叙事与'消逝的童年'（B367：frame-narrative——Immensee）。",
 "'简洁客观的风格'与'丰富的叙事活力'（B367：terse, objective style / narrative verve）。"],
"status":"Britannica 定位施托姆为德国诗意现实主义代表、德语中篇（Novelle）大师（B367）。",
"sources":["B367"],"dates_source":"B367",
"pending":["《白马骑士》通行译名（《白马骑士》/《骑白马的人》）待核。","与蒙森合作的 Liederbuch（B363 交叉）细节待核。","'诗意现实主义'术语出处待核。"]},
{"id":"lessing","name":"戈特霍尔德·埃夫莱姆·莱辛","foreign_name":"Gotthold Ephraim Lessing（戈特霍尔德·埃夫莱姆·莱辛，1729-01-22—1781-02-15）","country":"德国","birth":1729,"death":1781,"birth_year":1729,"death_year":1781,"era":"近代",
"summary":"莱辛，萨克森Kamenz生，德国剧作家与批评家——'He helped free German drama from the influence of classical and French models and wrote plays of lasting importance.'（B368）。Miss Sara Sampson (1755)——德语文学第一部重要市民悲剧（B368）；Minna von Barnhelm (1767)——'marks the birth of classical German comedy'（B368）；Laokoon (1766)——界定绘画与诗歌的边界（B368）；Hamburgische Dramaturgie (1767-69)——104篇剧评——'emphasizing pity and compassion and influencing the Sturm und Drang movement'（B368）；Nathan der Weise（智者纳坦, 1779）——'advocates for religious tolerance during the Crusades'——'ethical conduct, rather than dogma or prejudice, should determine the value of a religion.'（B368）。",
"timeline":[
 {"year":1729,"text":"1月22日生于Kamenz（B368）。","src":"B368"},
 {"year":1755,"text":"Miss Sara Sampson——第一部重要市民悲剧（B368）。","src":"B368"},
 {"year":1766,"text":"Laokoon——诗画界限（B368）。","src":"B368"},
 {"year":1767,"text":"Minna von Barnhelm——古典德国喜剧的诞生（B368）。","src":"B368"},
 {"year":1779,"text":"Nathan der Weise（智者纳坦）——最后一部戏剧（B368）。","src":"B368"},
 {"year":1781,"text":"2月15日卒于Braunschweig（B368）。","src":"B368"}],
"major_works":[
 {"work_id":"zhainazhitan","note":"1779（B368）"},
 {"work_id":"laokong","note":"1766（B368）"},
 {"title":"明娜·冯·巴尔赫姆","note":"（B368：Minna von Barnhelm (1767)）"},
 {"title":"爱米丽雅·迦洛蒂","note":"（B368：Emilia Galotti (1772)）"}],
"style":["德国戏剧的解放者：摆脱古典与法国范式（B368）。",
 "市民悲剧的开创（B368：bürgerliches Trauerspiel）。",
 "宗教宽容的倡导（B368：Nathan）。"],
"status":"Britannica 定位莱辛为德国文学经典化关键人物、市民悲剧与戏剧批评的奠基者（B368）。",
"sources":["B368"],"dates_source":"B368",
"pending":["《智者纳坦》通行译名两说（/《智者纳旦》）待核。","'指环寓言'细节待核（B368未载）。","'Laokoon'中译名（《拉奥孔》）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"yinmenghu","title":"茵梦湖","original_title":"Immensee","region":"德国","era":"近代","era_detail":"19世纪50年代初",
"genre":"中篇小说","genre_group":"小说","language":"德语","author_id":"storm","author_name":"特奥多尔·施托姆",
"year_display":"1850年（Britannica B367：Immensee (1850)——首部中篇、最受欢迎）","year_sort":1850,
"background":["Britannica（B367）：'a moving story of the vanished happiness of childhood'——'a haunting nostalgia'——首部中篇与最受欢迎的故事。","Britannica（B367）：'an outstanding representative of German poetic Realism'。","题材（通说待核）：莱因哈德与伊丽莎白的童年恋歌——多年后的茵梦湖畔重逢。"],
"outline":["（通说待核）框架叙事：老人回忆青年时代的湖畔夏日。","（通说待核）'茵梦湖'：忘不掉的湖与歌。"],
"characters":[{"name":"莱因哈德","identity":"老学者（回忆者）","note":"（通说待核，B367未载）"},{"name":"伊丽莎白","identity":"初恋","note":"（通说待核，B367未载）"}],
"themes":["'消逝的童年幸福'（B367：vanished happiness of childhood）。",
 "'萦绕的乡愁'（B367：haunting nostalgia）。",
 "框架叙事的时间结构（B367：frame-narrative——搜索口径）。"],
"influence":[{"text":"Britannica：'his most popular story'（B367 搜索口径）。","source":"B367"},{"text":"Britannica：诗意现实主义代表（B367）。","source":"B367"}],
"reading":{"difficulties":["框架叙事的时间层。","民歌穿插（《荷花》等——通说待核）。"],
 "editions":["《茵梦湖》中译本（人民文学/上海译文等——通说待核）。","德文原版（公有领域）。"],
 "order":"施托姆首选；与《白马骑士》对读。"},
"pending":["莱因哈德/伊丽莎白人名核对（B367未载）。","1850年发表细节待核。","英文译名 Immensee (Eng. trans. 1863) 待核。"],
"sources":["B367"],"year_source":"B367","author_source":"B367","related_works":["baimaqishi","dadidechengzhang","yuanshili"],
"svg":G("《茵梦湖》乡愁结构图",[{"title":"茵梦湖","text":"忘不掉的湖（书名）","color":"gold"},{"title":"童年","text":"消逝的幸福（B367）","color":"main"},{"title":"重逢","text":"多年后的注视（通说）","color":"family"},{"title":"乡愁","text":"'萦绕的怀想'（B367）","color":"antagonist"}])},
{"id":"baimaqishi","title":"白马骑士","original_title":"Der Schimmelreiter","region":"德国","era":"近代","era_detail":"19世纪80年代末",
"genre":"中篇小说","genre_group":"小说","language":"德语","author_id":"storm","author_name":"特奥多尔·施托姆",
"year_display":"1888年（Britannica B367：Der Schimmelreiter (1888)——'his last and greatest novella'）","year_sort":1888,
"background":["Britannica（B367）：'his last and greatest novella'——'its forceful hero and terse, objective style'——'vivid imagination and great narrative verve'。","Britannica（B367）：1888年4月刊于 Deutsche Rundschau——作家卒前最后作品。","题材（通说待核）：北海堤防工程师豪克·海恩——白马上骑者的传说与堤坝之战。"],
"outline":["（通说待核）豪克修堤的'野心'与村人的敌意。","（通说待核）'白马骑士'幽灵传说与最后的堤决。"],
"characters":[{"name":"豪克·海恩","identity":"堤长","note":"（通说待核，B367未载）"},{"name":"白马","identity":"幽灵坐骑","note":"（书名意象——通说待核）"}],
"themes":["人与海的工程之战（通说待核）。",
 "传说与写实的双重奏（书名语境——通说待核）。",
 "'客观简洁'的风格（B367：terse, objective style）。"],
"influence":[{"text":"Britannica：'last and greatest novella'（B367）。","source":"B367"},{"text":"Britannica：'great narrative verve'（B367）。","source":"B367"}],
"reading":{"difficulties":["北海堤防工程史。","幽灵传说的叙事层。"],
 "editions":["《白马骑士》中译名（《骑白马的人》两说——通说待核）。","德文原版（公有领域）。"],
 "order":"施托姆收官之作；与《茵梦湖》对读。"},
"pending":["豪克·海恩人名核对（B367未载）。","1888年4月刊期核对（B367已载）。","'幽灵'结尾细节待核。"],
"sources":["B367"],"year_source":"B367","author_source":"B367","related_works":["yinmenghu","xinshigudeLieshou","fushide"],
"svg":G("《白马骑士》海堤结构图",[{"title":"豪克","text":"修堤的工程师（通说）","color":"main"},{"title":"白马","text":"幽灵的传说（书名）","color":"gold"},{"title":"北海","text":"堤坝之战（通说）","color":"antagonist"},{"title":"客观","text":"'简洁的风格'（B367）","color":"family"}])},
{"id":"zhainazhitan","title":"智者纳坦","original_title":"Nathan der Weise","region":"德国","era":"近代","era_detail":"18世纪70年代末",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"lessing","author_name":"戈特霍尔德·埃夫莱姆·莱辛",
"year_display":"1779年（Britannica B368：Nathan der Weise (1779)——'His final drama'）","year_sort":1779,
"background":["Britannica（B368）：'advocates for religious tolerance during the Crusades'——十字军东征背景的宗教宽容剧。","Britannica（B368）：'The play suggests that ethical conduct, rather than dogma or prejudice, should determine the value of a religion.'","Britannica（B366）交叉：莱辛此剧已用素体诗（Nathan der Weise [1779]——B366）。"],
"outline":["（通说待核——B368未载剧情）'三指环'寓言：犹太商人纳坦的裁决。","（通说待核）圣殿骑士、苏丹萨拉丁与失散的家庭。"],
"characters":[{"name":"纳坦","identity":"犹太商人","note":"（B368 书名人物——'the Wise'）"},{"name":"萨拉丁","identity":"苏丹","note":"（通说待核）"}],
"themes":["宗教宽容（B368：religious tolerance）。",
 "'行为而非教条决定宗教的价值'（B368）。",
 "启蒙的'人类之爱'（通说待核）。"],
"influence":[{"text":"Britannica：'advocates for religious tolerance'（B368）。","source":"B368"},{"text":"Britannica：素体诗的早期示范（B366 交叉）。","source":"B366"}],
"reading":{"difficulties":["十字军东征背景。","'指环寓言'的薄伽丘底本（通说待核）。"],
 "editions":["《智者纳坦》中译名（《智者纳旦》两说——通说待核）。","德文原版（公有领域）。"],
 "order":"莱辛戏剧收官；与《拉奥孔》对读。"},
"pending":["'三指环'寓言细节核对（通说）。","1779年出版/首演细节待核。","中译名两说待核。"],
"sources":["B368"],"year_source":"B368","author_source":"B368","related_works":["laokong","tangkaluosi","fushide"],
"svg":G("《智者纳坦》宽容结构图",[{"title":"三指环","text":"真伪难辨的信仰（通说）","color":"gold"},{"title":"纳坦","text":"'智者'的裁决（B368）","color":"main"},{"title":"十字军","text":"宽容的舞台（B368）","color":"antagonist"},{"title":"行为","text":"'伦理高于教条'（B368）","color":"family"}])},
{"id":"laokong","title":"拉奥孔","original_title":"Laokoon: oder über die Grenzen der Malerei und Poesie","region":"德国","era":"近代","era_detail":"18世纪60年代",
"genre":"美学论著","genre_group":"散文","language":"德语","author_id":"lessing","author_name":"戈特霍尔德·埃夫莱姆·莱辛",
"year_display":"1766年（Britannica B368：Laokoon (1766)——'Lessing attempted to fundamentally define the separate functions of painting and of poetry'）","year_sort":1766,
"background":["Britannica（B368）：'fundamentally define the separate functions of painting and of poetry'（界定绘画与诗歌各自的功能）。","Britannica（B368）：莱辛——德国批评传统的奠基（Hamburgische Dramaturgie 交叉）。","题材（通说待核）：以'拉奥孔'群雕与维吉尔史诗的对比——'动作'vs'物体'的媒介论。"],
"outline":["（通说待核）雕塑的'最富孕育性瞬间'（通说待核——莱辛概念）。","（通说待核）温克尔曼'高贵的单纯'之辨。"],
"characters":[{"name":"（论著无人物）","identity":"——","note":"美学论著"}],
"themes":["诗与画的媒介界限（B368）。",
 "时间艺术与空间艺术（通说待核）。",
 "新古典主义的批评（通说待核）。"],
"influence":[{"text":"Britannica：'define the separate functions of painting and of poetry'（B368）。","source":"B368"},{"text":"Britannica：影响狂飙突进的批评传统（B368 交叉——dramaturgie）。","source":"B368"}],
"reading":{"difficulties":["美学概念的德语术语。","古典雕刻的图像学。"],
 "editions":["《拉奥孔》中译本（人民文学/商务等——通说待核）。","德文原版（公有领域）。"],
 "order":"莱辛批评首选；与《汉堡剧评》对读。"},
"pending":["'最富孕育性的瞬间'说法核对（通说——莱辛原话）。","1766年出版细节待核。","温克尔曼论战细节待核。"],
"sources":["B368"],"year_source":"B368","author_source":"B368","related_works":["zhainazhitan","balideyouyu","xunjiexiaoshuo"],
"svg":G("《拉奥孔》媒介界限图",[{"title":"诗","text":"时间的艺术（通说）","color":"main"},{"title":"画","text":"空间的艺术（通说）","color":"gold"},{"title":"拉奥孔","text":"雕塑的瞬间（B368）","color":"family"},{"title":"界限","text":"媒介的分化（B368）","color":"antagonist"}])},
]
created = []
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    created.append(w['id'])
    print('work', w['id'])

def link(aid, wid):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].insert(0, {"work_id": wid, "note": "（B36x/B37x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('yinmenghu','storm'), ('baimaqishi','storm'), ('zhainazhitan','lessing'), ('laokong','lessing')]:
    if wid in created:
        link(aid, wid)
print('BATCH45 DONE')
