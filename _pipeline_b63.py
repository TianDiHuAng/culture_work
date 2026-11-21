# -*- coding: utf-8 -*-
"""批63：Britannica 新核 2 作家 2 部（帕慕克 B384/品特 B385）"""
import json, pathlib

newsrc = [
{"id":"B384","title":"Orhan Pamuk — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Orhan-Pamuk","type":"百科全书","verified":True,"covers":["pamuk","wodemizijiaohong"],"note":"2026-11-21 核对：1952-06-07伊斯坦布尔生（在世）；2006诺贝尔文学奖——委员会称其'who in the quest for the melancholic soul of his native city [of Istanbul] has discovered new symbols for the clash and interlacing of cultures'（在探寻故乡伊斯坦布尔忧郁灵魂中发现了文化冲突与交织的新象征）；Benim adım kırmızı（我的名字叫红, 1998）——'one of his mysteries'（未提IMPAC奖——不采）；Kar（雪, 2002）——流亡德国的土耳其诗人赴偏远小镇（转述）；İstanbul (2004)——'a partly fictionalized memoir'；Beyaz kale（白城堡, 1985）——'brought international fame'；Kara kitap（黑书, 1990）；纯真博物馆 (2008)——真实博物馆2012年开馆、Netflix剧2026年2月首播；2005年'.denigrating Turkishness'指控撤销——2011年'was ordered to compensate the six plaintiffs'（亚美尼亚/库尔德言论）；Cevdet Bey (1982)首作；The Naive and Sentimental Novelist (2010)；A Strangeness in My Mind (2014)"},
{"id":"B385","title":"Harold Pinter — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Harold-Pinter","type":"百科全书","verified":True,"covers":["pinter","shengriwanhui"],"note":"2026-11-21 核对：1930-10-10伦敦生——2008-12-24伦敦卒（78岁）；2005诺贝尔文学奖；2007法国荣誉军团骑士；The Birthday Party (1958首演)——首部多幕剧——'puzzled the London audiences and lasted only a week'——确立'comedy of menace'（威胁的喜剧）；The Caretaker (1960)——'secured his reputation'——'wheedling, garrulous old tramp comes to live with two neurotic brothers'；The Homecoming (1965)——教授带妻回全男性家庭；Betrayal (1978)——后期成功之作（1983自改电影）；'understatement, small talk, reticence—and even silence'；'disjointed and oddly ambivalent conversation that is punctuated by resonant silences'；'Pinteresque'形容其口语风格；'dialogue is called perhaps the key to his originality'；流派 Theatre of the Absurd；犹太裁缝之子、伦敦东区；RADA 1948读两学期；艺名 David Baron 至1959；剧本 The Servant (1963)/The Go-Between (1970)/The French Lieutenant's Woman (1981)"},
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
{"id":"pamuk","name":"奥尔罕·帕慕克","foreign_name":"Orhan Pamuk（奥尔罕·帕慕克，1952-06-07—）","country":"土耳其","birth":1952,"death":None,"birth_year":1952,"death_year":None,"era":"现当代",
"summary":"帕慕克，伊斯坦布尔生，土耳其小说家——2006年诺贝尔文学奖——委员会称其'who in the quest for the melancholic soul of his native city [of Istanbul] has discovered new symbols for the clash and interlacing of cultures'（在探寻故乡的忧郁灵魂中发现文化冲突与交织的新象征——B384）。My Name Is Red（我的名字叫红, 1998）（B384）；Snow（雪, 2002）——流亡德国的土耳其诗人赴偏远小镇（B384）；İstanbul（伊斯坦布尔, 2004）——'a partly fictionalized memoir'（B384）。The White Castle (1985)——'brought international fame'（B384）。2005年'denigrating Turkishness'指控撤销、2011年被判赔偿六原告（B384）。",
"timeline":[
 {"year":1952,"text":"6月7日生于伊斯坦布尔（B384）。","src":"B384"},
 {"year":1985,"text":"The White Castle——国际名声（B384）。","src":"B384"},
 {"year":1998,"text":"《我的名字叫红》（B384）。","src":"B384"},
 {"year":2006,"text":"获诺贝尔文学奖（B384）。","src":"B384"},
 {"year":2006,"text":"'侮辱土耳其性'指控撤销；2011年判赔六原告（B384）。","src":"B384"}],
"major_works":[
 {"work_id":"wodemizijiaohong","note":"1998（B384）"},
 {"title":"雪","note":"（B384：Kar (2002)）"},
 {"title":"纯真博物馆","note":"（B384：The Museum of Innocence (2008)——真实博物馆2012年开馆）"}],
"style":["'伊斯坦布尔的忧郁灵魂'（B384 诺奖引语）。",
 "文化'冲突与交织'的新象征（B384）。",
 "细密画的'声音'实验（书名语境——通说待核）。"],
"status":"Britannica 定位帕慕克为2006诺奖得主、伊斯坦布尔的书写者（B384）。",
"sources":["B384"],"dates_source":"B384",
"pending":["《我的名字叫红》IMPAC都柏林奖说待核（B384未提——不采）。","'赫拉特细密画'细节待核（通说）。","2005-2011案件细节核对（B384口径）。"]},
{"id":"pinter","name":"哈罗德·品特","foreign_name":"Harold Pinter（哈罗德·品特，1930-10-10—2008-12-24）","country":"英国","birth":1930,"death":2008,"birth_year":1930,"death_year":2008,"era":"现当代",
"summary":"品特，伦敦东区（犹太裁缝之子）生，英国剧作家——2005年诺贝尔文学奖（B385）；2007法国荣誉军团骑士（B385）。The Birthday Party（生日晚会, 1958）——首部多幕剧——'puzzled the London audiences and lasted only a week'——确立'comedy of menace'（威胁的喜剧——B385）。The Caretaker (1960)——'secured his reputation'（B385）。Betrayal (1978)（B385）。'understatement, small talk, reticence—and even silence'；'disjointed and oddly ambivalent conversation that is punctuated by resonant silences'；'Pinteresque'（B385）。流派：荒诞派（B385）。",
"timeline":[
 {"year":1930,"text":"10月10日生于伦敦（B385）。","src":"B385"},
 {"year":1958,"text":"《生日晚会》首演——仅演一周，后成经典（B385）。","src":"B385"},
 {"year":1960,"text":"The Caretaker——声誉确立（B385）。","src":"B385"},
 {"year":2005,"text":"获诺贝尔文学奖（B385）。","src":"B385"},
 {"year":2008,"text":"12月24日卒于伦敦（B385）。","src":"B385"}],
"major_works":[
 {"work_id":"shengriwanhui","note":"1958（B385）"},
 {"title":"看管人","note":"（B385：The Caretaker (1960)——中译名待核）"},
 {"title":"背叛","note":"（B385：Betrayal (1978)）"}],
"style":["'威胁的喜剧'（B385：comedy of menace）。",
 "'轻描淡写、闲谈、缄默——甚至沉默'（B385）。",
 "'Pinteresque'：'共鸣的沉默'点断的对话（B385）。"],
"status":"Britannica 定位品特为2005诺奖得主、荒诞派'沉默'戏剧的代表（B385）。",
"sources":["B385"],"dates_source":"B385",
"pending":["《生日晚会》通行译名（《生日聚会》）待核。","'comedy of menace'术语出处（Esslin说——通说待核）。","电影剧本清单细节（B385已载）核对。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"wodemizijiaohong","title":"我的名字叫红","original_title":"Benim adım kırmızı","region":"土耳其","era":"现当代","era_detail":"20世纪90年代末",
"genre":"长篇小说","genre_group":"小说","language":"土耳其语","author_id":"pamuk","author_name":"奥尔罕·帕慕克",
"year_display":"1998年（Britannica B384：Benim adım kırmızı (1998; My Name Is Red)——'one of his mysteries'）","year_sort":1998,
"background":["Britannica（B384）：'one of his mysteries'（其'悬疑'小说之一——直译口径）。","Britannica（B384）：帕慕克——2006诺奖——'the melancholic soul of his native city'与'文化冲突与交织的新象征'。","题材（通说待核）：16世纪伊斯坦布尔细密画作坊的连环凶案——'谋杀者'与'红色'的自述章。"],
"outline":["（通说待核）被谋杀的细密画家与'凶手'的自述章（作者自述章节——通说待核）。","（通说待核）东西方画法之争：'法兰克风格'的透视与失明。"],
"characters":[{"name":"黑","identity":"返乡者","note":"（通说待核，B384未载）"},{"name":"姨父","identity":"画坊主持","note":"（通说待核）"}],
"themes":["文化'冲突与交织'（B384 诺奖引语）。",
 "'声音'：非人叙事者（树、狗、红、凶手——通说待核）。",
 "细密画与失明（通说待核）。"],
"influence":[{"text":"Britannica：2006诺奖（B384）。","source":"B384"},{"text":"Britannica：'one of his mysteries'（B384）。","source":"B384"}],
"reading":{"difficulties":["多声部'声音'章。","奥斯曼细密画史。"],
 "editions":["《我的名字叫红》中译本（上海人民出版社等——通说待核）。","土耳其文原版。"],
 "order":"帕慕克代表作；后接《雪》。"},
"pending":["'黑'/姨父人名核对（通说）。","1998年出版细节待核。","IMPAC都柏林奖（2003说）待核——B384未提。"],
"sources":["B384"],"year_source":"B384","author_source":"B384","related_works":["calvino" if "calvino" in existing else "leiyu","jingyu","aiyuheandegushi"],
"svg":G("《我的名字叫红》声音结构图",[{"title":"红色","text":"'我的名字叫红'（书名）","color":"gold"},{"title":"细密画","text":"东西方的画法之争（通说）","color":"main"},{"title":"凶手","text":"自述的章节（通说）","color":"antagonist"},{"title":"忧郁","text":"伊斯坦布尔的灵魂（B384）","color":"family"}])},
{"id":"shengriwanhui","title":"生日晚会","original_title":"The Birthday Party","region":"英国","era":"现当代","era_detail":"20世纪50年代末",
"genre":"戏剧","genre_group":"戏剧","language":"英语","author_id":"pinter","author_name":"哈罗德·品特",
"year_display":"1958年（Britannica B385：The Birthday Party——1958首演——'puzzled the London audiences and lasted only a week'）","year_sort":1958,
"background":["Britannica（B385）：首部多幕剧——'puzzled the London audiences and lasted only a week'——确立'comedy of menace'（威胁的喜剧）。","Britannica（B385）：'disjointed and oddly ambivalent conversation that is punctuated by resonant silences'——'Pinteresque'。","题材（通说待核）：海滨寄宿屋的生日聚会——两个'来客'与斯坦利的审讯。"],
"outline":["（通说待核）戈德堡与麦卡恩的'审讯'：生日庆典的颠倒。","（通说待核）梅格的'生日'与斯坦利的崩解。"],
"characters":[{"name":"斯坦利","identity":"寄宿者/前钢琴师","note":"（通说待核，B385未载）"},{"name":"戈德堡","identity":"来客","note":"（通说待核）"}],
"themes":["'威胁的喜剧'（B385：comedy of menace）。",
 "'共鸣的沉默'（B385：resonant silences）。",
 "身份的审讯（通说待核）。"],
"influence":[{"text":"Britannica：'comedy of menace'的确立（B385）。","source":"B385"},{"text":"Britannica：2005诺奖（B385 交叉）。","source":"B385"}],
"reading":{"difficulties":["'沉默'的读法。","'威胁'的日常化。"],
 "editions":["《生日晚会》中译名（《生日聚会》）待核。","英文原版。"],
 "order":"品特首选；后接《看管人》《背叛》。"},
"pending":["斯坦利/戈德堡人名核对（通说）。","1958年首演（Lyric Hammersmith说）待核。","'一剧一周'细节核对（B385已载）。"],
"sources":["B385"],"year_source":"B385","author_source":"B385","related_works":["dengdaigou","toutougeonv","yizi"],
"svg":G("《生日晚会》威胁结构图",[{"title":"生日","text":"颠倒的庆典（书名）","color":"gold"},{"title":"来客","text":"审讯的威胁（通说）","color":"antagonist"},{"title":"沉默","text":"'共鸣的沉默'（B385）","color":"main"},{"title":"寄宿屋","text":"海滨的盒子（通说）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B38x/B385 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('wodemizijiaohong','pamuk'), ('shengriwanhui','pinter')]:
    if wid in created:
        link(aid, wid)
print('BATCH63 DONE')
