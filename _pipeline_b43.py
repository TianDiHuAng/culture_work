# -*- coding: utf-8 -*-
"""批43：Britannica 新核席勒 B366——3 部（强盗/阴谋与爱情/堂卡洛斯）+ 威廉退尔(4部)"""
import json, pathlib

newsrc = [
{"id":"B366","title":"Friedrich Schiller — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Friedrich-Schiller","type":"百科全书","verified":True,"covers":["schiller","qiangdao"],"note":"2026-11-21 核对：全名 Johann Christoph Friedrich von Schiller；1759-11-10符腾堡Marbach生—1805-05-09魏玛卒（45岁）；'a leading German dramatist, poet, and literary theorist'——代表作 Die Räuber (1781)、Wallenstein 三部曲 (1800-01)、Maria Stuart (1801)、Wilhelm Tell (1804)；军事学院8年——'adolescence under the rule of a petty tyrant confronted Schiller with the problem of the use and abuse of power'；Die Räuber——Karl Moor 为'sublime criminal'——'a scathing indictment of a society that could drive so fundamentally noble a character to a career of crime'——1782-01-13曼海姆民族剧院首演'created a sensation...a milestone in the history of the German theatre'；因未经许可赴首演被公爵禁写剧本、夜逃斯图加特；Fiesco (1783)——'a republican tragedy'——'ambition in action, and ultimately defeated'；Kabale und Liebe (1784)——'the revolt of elemental human feeling against the artificialities of convention'——'combine to make Kabale und Liebe great theatre'；Don Carlos (1787)——第一部素体诗主要剧作——'the complex, brooding, and tragic figure of King Philip'——与歌德 Iphigenie 确立素体诗为德语诗剧媒介（Lessing Nathan der Weise 1779 已用）；'An die Freude'（欢乐颂）——贝多芬第九交响曲合唱乐章采用；1794与歌德订交——'a union of opposites'；耶拿历史教授；Geschichte des dreissigjährigen Krieges (1791-93)——为《华伦斯坦》提供素材；1790娶 Charlotte von Lengefeld；终身与疾病搏斗"},
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
{"id":"schiller","name":"弗里德里希·席勒","foreign_name":"Friedrich Schiller（弗里德里希·席勒，全名 Johann Christoph Friedrich von Schiller，1759-11-10—1805-05-09）","country":"德国","birth":1759,"death":1805,"birth_year":1759,"death_year":1805,"era":"近代",
"summary":"席勒，符腾堡Marbach生，德国剧作家、诗人与文学理论家——'a leading German dramatist, poet, and literary theorist'（B366）。Die Räuber（强盗, 1781）——Karl Moor 为'sublime criminal'——'a scathing indictment of a society that could drive so fundamentally noble a character to a career of crime'（B366）——1782年1月13日曼海姆首演'a milestone in the history of the German theatre'（B366）。Kabale und Liebe（阴谋与爱情, 1784）——'the revolt of elemental human feeling against the artificialities of convention'（B366）。Don Carlos (1787)——与歌德《伊菲革涅亚》确立素体诗为德语诗剧媒介（B366）。'An die Freude'（欢乐颂）——被贝多芬第九交响曲采用（B366）。1794年与歌德订交——'a union of opposites'（B366）。Wallenstein 三部曲 (1800-01)、Maria Stuart (1801)、Wilhelm Tell (1804)（B366）。",
"timeline":[
 {"year":1759,"text":"11月10日生于符腾堡Marbach（B366）。","src":"B366"},
 {"year":1781,"text":"Die Räuber（强盗）出版；1782曼海姆首演——德国剧场史里程碑（B366）。","src":"B366"},
 {"year":1784,"text":"Kabale und Liebe（阴谋与爱情）（B366）。","src":"B366"},
 {"year":1787,"text":"Don Carlos——第一部素体诗主要剧作（B366）。","src":"B366"},
 {"year":1794,"text":"与歌德订交——'union of opposites'（B366）。","src":"B366"},
 {"year":1805,"text":"5月9日卒于魏玛（B366）。","src":"B366"}],
"major_works":[
 {"work_id":"qiangdao","note":"1781（B366）"},
 {"work_id":"yinmouyuaiqing","note":"1784（B366）"},
 {"work_id":"tangkaluosi","note":"1787（B366）"},
 {"title":"威廉·退尔","note":"（B366：Wilhelm Tell (1804)）"},
 {"title":"华伦斯坦","note":"（B366：Wallenstein 三部曲 (1800-01)）"}],
"style":["'权力之滥用'的终身主题（B366：the use and abuse of power）。",
 "'崇高罪犯'的道德辩证（B366：sublime criminal）。",
 "素体诗德语诗剧的确立者之一（B366）。"],
"status":"Britannica 定位席勒为德国最重要的剧作家/诗人/理论家之一、魏玛古典主义双星之一（B366——与歌德并称语境）。",
"sources":["B366"],"dates_source":"B366",
"pending":["《威廉·退尔》《华伦斯坦》《玛丽亚·斯图亚特》剧情细节待核（B366仅列名）。","1782年首演剧场名（Mannheim National Theatre——B366 已载）。","《欢乐颂》创作年（1785说）待核。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"qiangdao","title":"强盗","original_title":"Die Räuber","region":"德国","era":"近代","era_detail":"18世纪80年代初",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"schiller","author_name":"弗里德里希·席勒",
"year_display":"1781年（Britannica B366：Die Räuber (1781)——1782-01-13曼海姆首演'a milestone in the history of the German theatre'）","year_sort":1781,
"background":["Britannica（B366）：'a stirring protest against stifling convention and corruption in high places'——Karl Moor 被代表为'sublime criminal'。","Britannica（B366）：'a scathing indictment of a society that could drive so fundamentally noble a character to a career of crime'。","Britannica（B366）：首演'created a sensation'——'a milestone in the history of the German theatre'。"],
"outline":["（B366）卡尔·穆尔被弟弗兰茨构陷而落草——'暴力与无政府不是可行替代'的发现与自首。","（B366）'以法律与道德之名写作'的辩护与控诉并存。"],
"characters":[{"name":"卡尔·穆尔","identity":"强盗首领/'崇高罪犯'","note":"（B366：Karl Moor——sublime criminal）"},{"name":"弗兰茨","identity":"恶弟","note":"（B366：villainous younger brother）"}],
"themes":["对压制性惯例与上层腐败的抗议（B366）。",
 "暴力不能改良社会（B366：violence and anarchy do not offer a workable alternative）。",
 "狂飙突进的爆发力（时代语境——通说待核）。"],
"influence":[{"text":"Britannica：德国剧场史里程碑（B366）。","source":"B366"},{"text":"Britannica：'sublime criminal'——浪漫主义反英雄原型（B366）。","source":"B366"}],
"reading":{"difficulties":["狂飙突进语境。","五幕的激情独白。"],
 "editions":["《强盗》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"席勒首作；与《阴谋与爱情》对读。"},
"pending":["1782-01-13首演细节（B366已载日期）剧场核对。","'狂飙突进'归属说法待核。","穆尔父子名核对（B366 载 Karl/Franz/Count Moor）。"],
"sources":["B366"],"year_source":"B366","author_source":"B366","related_works":["yinmouyuaiqing","fushide","leiyu"],
"svg":G("《强盗》控诉结构图",[{"title":"卡尔·穆尔","text":"'崇高罪犯'（B366）","color":"main"},{"title":"社会","text":"逼良为盗的控诉（B366）","color":"antagonist"},{"title":"弗兰茨","text":"构陷的恶弟（B366）","color":"gold"},{"title":"自首","text":"法律的归顺（B366）","color":"family"}])},
{"id":"yinmouyuaiqing","title":"阴谋与爱情","original_title":"Kabale und Liebe","region":"德国","era":"近代","era_detail":"18世纪80年代",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"schiller","author_name":"弗里德里希·席勒",
"year_display":"1784年（Britannica B366：Kabale und Liebe (1784)）","year_sort":1784,
"background":["Britannica（B366）：'the revolt of elemental human feeling against the artificialities of convention'——'the vigour of its social criticism'。","Britannica（B366）：贵族青年与平民之恋——'combine to make Kabale und Liebe great theatre'。","题材（通说待核）：斐迪南与露易丝——宫廷阴谋下的毒酒悲剧。"],
"outline":["（B366）'原始人性情感对人工惯例的反叛'——贵族青年与平民少女之恋（B366：love of a young aristocrat for a girl of humble origin）。","（通说待核）宰相之父的阴谋与毒杀结局。"],
"characters":[{"name":"斐迪南","identity":"贵族青年","note":"（通说待核，B366未载名）"},{"name":"露易丝","identity":"乐师之女","note":"（通说待核，B366未载）"}],
"themes":["阶级壁垒与爱情（B366：social criticism）。",
 "'人工惯例'的反抗（B366）。",
 "市民悲剧的德语高峰（通说待核）。"],
"influence":[{"text":"Britannica：'great theatre'（B366）。","source":"B366"},{"text":"Britannica：曼海姆驻场剧作家时期作品（B366 语境）。","source":"B366"}],
"reading":{"difficulties":["18世纪德国等级社会。","市民悲剧（bürgerliches Trauerspiel）传统（通说待核）。"],
 "editions":["《阴谋与爱情》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"席勒代表作；与《强盗》对读。"},
"pending":["斐迪南/露易丝人名核对（B366未载）。","1784年首演细节待核。","'市民悲剧'归类说法待核。"],
"sources":["B366"],"year_source":"B366","author_source":"B366","related_works":["qiangdao","tangkaluosi","leiyu"],
"svg":G("《阴谋与爱情》阶级冲突图",[{"title":"斐迪南","text":"贵族的反叛（通说）","color":"main"},{"title":"露易丝","text":"平民的爱情（通说）","color":"gold"},{"title":"阴谋","text":"宫廷的毒计（通说）","color":"antagonist"},{"title":"反叛","text":"'原始情感对惯例'（B366）","color":"family"}])},
{"id":"tangkaluosi","title":"堂卡洛斯","original_title":"Don Carlos","region":"德国","era":"近代","era_detail":"18世纪80年代末",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"schiller","author_name":"弗里德里希·席勒",
"year_display":"1787年（Britannica B366：Don Carlos——第一部素体诗主要剧作）","year_sort":1787,
"background":["Britannica（B366）：西班牙宫廷剧——腓力二世、伊丽莎白·德·瓦卢瓦与爱上继母的堂卡洛斯——'broad political implications'。","Britannica（B366）：'the complex, brooding, and tragic figure of King Philip'。","Britannica（B366）：与歌德《伊菲革涅亚》'definitely established it [blank verse] as the recognized medium of German poetic drama'（Lessing《智者纳坦》1779 已用素体诗）。"],
"outline":["（B366）父子冲突从家庭扩展到政治：佛兰德的自由（'broad political implications'）。","（通说待核）波萨侯爵的理想主义与宗教裁判所。"],
"characters":[{"name":"腓力二世","identity":"西班牙国王","note":"（B366：King Philip——'complex, brooding, and tragic figure'）"},{"name":"堂卡洛斯","identity":"王子","note":"（B366 书名人物——爱上继母）"},{"name":"伊丽莎白","identity":"继母/王后","note":"（B366：Elizabeth of Valois）"}],
"themes":["家庭与政治的双重冲突（B366）。",
 "自由的政治理想（波萨台词——通说待核）。",
 "素体诗的德语确立（B366）。"],
"influence":[{"text":"Britannica：'established...as the recognized medium of German poetic drama'（B366）。","source":"B366"},{"text":"Britannica：'wealth of exciting and moving scenes'（B366）。","source":"B366"}],
"reading":{"difficulties":["16世纪西班牙宫廷史。","素体诗（Blankvers）语感。"],
 "editions":["《堂卡洛斯》中译名（《唐·卡洛斯》两说）待核。","德文原版（公有领域）。"],
 "order":"席勒过渡之作；后接《华伦斯坦》《威廉·退尔》。"},
"pending":["中译名两说待核。","1787年出版细节待核。","波萨侯爵与宗教裁判所细节待核（通说）。"],
"sources":["B366"],"year_source":"B366","author_source":"B366","related_works":["qiangdao","yinmouyuaiqing","fushide"],
"svg":G("《堂卡洛斯》双重冲突图",[{"title":"腓力二世","text":"'阴郁的悲剧形象'（B366）","color":"antagonist"},{"title":"堂卡洛斯","text":"爱上继母的王子（B366）","color":"main"},{"title":"伊丽莎白","text":"瓦卢瓦的王后（B366）","color":"family"},{"title":"政治","text":"家庭的延展（B366）","color":"gold"}])},
{"id":"weimateer","title":"威廉·退尔","original_title":"Wilhelm Tell","region":"德国","era":"近代","era_detail":"19世纪初",
"genre":"戏剧","genre_group":"戏剧","language":"德语","author_id":"schiller","author_name":"弗里德里希·席勒",
"year_display":"1804年（Britannica B366：Wilhelm Tell (1804)——代表作列举）","year_sort":1804,
"background":["Britannica（B366）：Wilhelm Tell (1804)——'best remembered for such dramas as...'之首。","Britannica（B366）：席勒晚年与疾病搏斗时期作品（'a losing battle, fought with superb fortitude'）。","题材（通说待核）：瑞士传统英雄退尔射苹果起义——三州同盟。"],
"outline":["（通说待核——B366未载剧情）盖斯勒的苹果考验与瑞士起义。","（通说待核）吕特利誓言。"],
"characters":[{"name":"威廉·退尔","identity":"弓箭手","note":"（B366 书名人物）"},{"name":"盖斯勒","identity":"奥地利总督","note":"（通说待核）"}],
"themes":["反抗暴政（通说待核）。",
 "瑞士建国传说（通说待核）。",
 "晚年的抒情与政治合一（B366 语境）。"],
"influence":[{"text":"Britannica：席勒代表作之一（B366）。","source":"B366"},{"text":"Britannica：与罗西尼歌剧（1829说）待核——不采。","source":"B366"}],
"reading":{"difficulties":["瑞士史传说层。","五幕群像结构。"],
 "editions":["《威廉·退尔》中译本（人民文学等——通说待核）。","德文原版（公有领域）。"],
 "order":"席勒收官之作。"},
"pending":["1804年首演（Weimar说）待核。","射苹果场景细节待核（通说）。","'吕特利誓言'细节待核。"],
"sources":["B366"],"year_source":"B366","author_source":"B366","related_works":["qiangdao","tangkaluosi","fushide"],
"svg":G("《威廉·退尔》起义结构图",[{"title":"退尔","text":"射苹果的传奇（通说）","color":"main"},{"title":"盖斯勒","text":"暴政的帽子（通说）","color":"antagonist"},{"title":"三州","text":"同盟的誓言（通说）","color":"family"},{"title":"起义","text":"自由的瑞士（通说）","color":"gold"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B366 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid, kw in [('qiangdao','schiller','强盗'),('yinmouyuaiqing','schiller','阴谋与爱情'),('tangkaluosi','schiller','堂卡洛斯'),('weimateer','schiller','威廉·退尔')]:
    if wid in created:
        link(aid, wid, kw)
print('BATCH43 DONE')
