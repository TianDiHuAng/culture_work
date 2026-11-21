# -*- coding: utf-8 -*-
"""批73：Britannica 新核 2 作家 2 部（福尔斯 B399/热内 B400）"""
import json, pathlib

newsrc = [
{"id":"B399","title":"John Fowles — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/John-Fowles","type":"百科全书","verified":True,"covers":["fowles","faguozhongweidenvren"],"note":"2026-11-21 核对：1926-03-31英国Leigh-on-Sea, Essex生—2005-11-05多塞特Lyme Regis卒（79岁）；The French Lieutenant's Woman（法国中尉的女人, 1969，电影1981）——'arguably Fowles's best-known work'——19世纪英国爱情故事——'combined elements of the Victorian novel with postmodern works and featured alternate endings'（维多利亚小说与后现代的混合、多重结局）；The Magus (1965，修订1977，电影1968)——希腊海岛；The Collector (1963，电影1965)——'about a shy man who kidnaps a girl in a hapless search for love'；A Maggot (1985)——最后一部长篇——'centred on a group of travelers in the 1700s and the mysterious events that occur during their journey'；'combine psychological probings—chiefly of sex and love—with an interest in social and philosophical issues'；1950牛津毕业——在希腊/法国/英国教书"},
{"id":"B400","title":"Jean Genet — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jean-Genet","type":"百科全书","verified":True,"covers":["genet","xianhuashengmu"],"note":"2026-11-21 核对：1910-12-19巴黎生—1986-04-15巴黎卒（75岁）；'a French criminal and social outcast turned writer'（法国罪犯与被弃者转作家）；'transformed erotic and often obscene subject matter into a poetic vision of the universe'；Notre-Dame des Fleurs（鲜花圣母, 1943）——1942年因盗窃囚于Fresnes狱中写——'vividly portray[s] the prewar Montmartre underworld of thugs, pimps, and perverts'；Querelle de Brest (1947，电影1982)；The Maids (1947)；The Thief's Journal (1949)；The Balcony (1956)；The Blacks (1958)；The Screens (1961)；'This Theatre of Hatred attempts to wrest the maximum dramatic power from a social or political situation'；'a rebel and an anarchist of the most extreme sort, rejected almost all forms of social discipline'；10岁窃案入 Mettray 少管所；'pardoned in advance'（第十次定罪后作家代表团请愿获赦）；萨特/科克托/波伏瓦赏识其才（Saint Genet 一书页未提——不采）"},
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
{"id":"fowles","name":"约翰·福尔斯","foreign_name":"John Fowles（约翰·福尔斯，1926-03-31—2005-11-05）","country":"英国","birth":1926,"death":2005,"birth_year":1926,"death_year":2005,"era":"现当代",
"summary":"福尔斯，英国Leigh-on-Sea生，小说家——2005年卒于Lyme Regis（B399）。The French Lieutenant's Woman（法国中尉的女人, 1969，电影1981）——'arguably Fowles's best-known work'——19世纪英国爱情故事——'combined elements of the Victorian novel with postmodern works and featured alternate endings'（维多利亚小说与后现代的混合、多重结局——B399）。The Collector (1963)——'about a shy man who kidnaps a girl in a hapless search for love'（B399）。'combine psychological probings—chiefly of sex and love—with an interest in social and philosophical issues'（B399）。",
"timeline":[
 {"year":1926,"text":"3月31日生于英国Leigh-on-Sea（B399）。","src":"B399"},
 {"year":1963,"text":"The Collector（收藏家）（B399）。","src":"B399"},
 {"year":1969,"text":"《法国中尉的女人》（B399）。","src":"B399"},
 {"year":2005,"text":"11月5日卒于Lyme Regis（B399）。","src":"B399"}],
"major_works":[
 {"work_id":"faguozhongweidenvren","note":"1969（B399）"},
 {"title":"收藏家","note":"（B399：The Collector (1963)——中译名待核）"},
 {"title":"魔术师","note":"（B399：The Magus (1965)——中译名待核）"}],
"style":["'维多利亚小说与后现代的混合'（B399：combined elements...）。",
 "'多重结局'（B399：featured alternate endings）。",
 "'心理探询（性与爱）+社会哲学关切'（B399）。"],
"status":"Britannica 定位福尔斯为《法国中尉的女人》作者（B399）。",
"sources":["B399"],"dates_source":"B399",
"pending":["《法国中尉的女人》通行译名待核。","'多重结局'细节（两种结局说——通说）待核。","萨拉人物细节待核（B399未载）。"]},
{"id":"genet","name":"让·热内","foreign_name":"Jean Genet（让·热内，1910-12-19—1986-04-15）","country":"法国","birth":1910,"death":1986,"birth_year":1910,"death_year":1986,"era":"近代",
"summary":"热内，巴黎生，法国作家——'a French criminal and social outcast turned writer'（罪犯与被弃者转作家——B400）；'transformed erotic and often obscene subject matter into a poetic vision of the universe'（把情色甚至猥亵题材转化为宇宙的诗性图景——B400）。Notre-Dame des Fleurs（鲜花圣母, 1943）——1942年囚于Fresnes狱中写——'vividly portray[s] the prewar Montmartre underworld'（B400）。The Maids (1947)、The Balcony (1956)、The Screens (1961)（B400）。'This Theatre of Hatred attempts to wrest the maximum dramatic power from a social or political situation'（'憎恨的剧场'——B400）。'pardoned in advance'（第十次定罪后作家代表团请愿获终身赦免——B400）。",
"timeline":[
 {"year":1910,"text":"12月19日生于巴黎（B400）。","src":"B400"},
 {"year":1942,"text":"Fresnes狱中开始写作（《鲜花圣母》——B400）。","src":"B400"},
 {"year":1947,"text":"The Maids 与 Querelle de Brest（B400）。","src":"B400"},
 {"year":1949,"text":"第十次定罪后获'预先赦免'（B400：pardoned in advance）。","src":"B400"},
 {"year":1986,"text":"4月15日卒于巴黎（B400）。","src":"B400"}],
"major_works":[
 {"work_id":"xianhuashengmu","note":"1943（B400）"},
 {"title":"女仆","note":"（B400：Les Bonnes (1947)——中译名待核）"},
 {"title":"小偷日记","note":"（B400：Journal du voleur (1949)——中译名待核）"}],
"style":["'情色与猥亵题材的诗性宇宙'（B400：poetic vision of the universe）。",
 "'憎恨的剧场'（B400：Theatre of Hatred）。",
 "'最极端的反叛与无政府主义'（B400：anarchist of the most extreme sort）。"],
"status":"Britannica 定位热内为'罪犯转作家'、憎恨剧场的创造者（B400）。",
"sources":["B400"],"dates_source":"B400",
"pending":["《鲜花圣母》通行译名（《玫瑰花与播音婢》两说——待核）。","'预先赦免'细节核对（B400口径）。","萨特《圣热内》说——B400页未提（不采）。"]},
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

works = [
{"id":"faguozhongweidenvren","title":"法国中尉的女人","original_title":"The French Lieutenant's Woman","region":"英国","era":"现当代","era_detail":"20世纪60年代末",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"fowles","author_name":"约翰·福尔斯",
"year_display":"1969年（Britannica B399：The French Lieutenant's Woman (1969; filmed 1981)——'arguably Fowles's best-known work'）","year_sort":1969,
"background":["Britannica（B399）：'combined elements of the Victorian novel with postmodern works and featured alternate endings'（维多利亚小说与后现代的混合、多重结局）。","Britannica（B399）：'arguably Fowles's best-known work'——19世纪英国爱情故事。","Britannica（B399）：福尔斯——'combine psychological probings—chiefly of sex and love—with an interest in social and philosophical issues'。"],
"outline":["（通说待核——B399未载剧情）萨拉·伍德拉夫与化石学家查尔斯的维多利亚恋情。","（通说待核）'多重结局'：叙述者的两难选择（B399：featured alternate endings）。"],
"characters":[{"name":"萨拉·伍德拉夫","identity":"'法国中尉的女人'","note":"（通说待核，B399未载）"},{"name":"查尔斯·史密森","identity":"化石学家","note":"（通说待核）"}],
"themes":["'维多利亚小说与后现代的混合'（B399）。",
 "'多重结局'（B399：alternate endings）。",
 "'性与爱的心理探询'（B399：psychological probings）。"],
"influence":[{"text":"Britannica：'arguably Fowles's best-known work'（B399）。","source":"B399"},{"text":"Britannica：1981年电影改编（B399）。","source":"B399"}],
"reading":{"difficulties":["叙述者闯入（第13章——通说待核）。","维多利亚习俗与达尔文主义（通说待核）。"],
 "editions":["《法国中尉的女人》中译本（人民文学/百花等——通说待核）。","英文原版。"],
 "order":"福尔斯代表作；与《收藏家》对读。"},
"pending":["萨拉/查尔斯人名核对（通说）。","1969年出版（Jonathan Cape说）待核。","'两种结局'细节待核（通说）。"],
"sources":["B399"],"year_source":"B399","author_source":"B399","related_works":["aimaa","kasiteqiaoshizhang","fudi"],
"svg":G("《法国中尉的女人》多重结局图",[{"title":"萨拉","text":"码头的谜（通说）","color":"main"},{"title":"多重结局","text":"'alternate endings'（B399）","color":"gold"},{"title":"维多利亚","text":"与后现代的混合（B399）","color":"family"},{"title":"化石","text":"时间的层理（通说）","color":"antagonist"}])},
{"id":"xianhuashengmu","title":"鲜花圣母","original_title":"Notre-Dame des Fleurs","region":"法国","era":"近代","era_detail":"20世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"genet","author_name":"让·热内",
"year_display":"1943年（Britannica B400：Notre-Dame des Fleurs (1943)——1942年Fresnes狱中写）","year_sort":1943,
"background":["Britannica（B400）：'vividly portray[s] the prewar Montmartre underworld of thugs, pimps, and perverts'（生动描绘战前蒙马特的黑社会——恶棍、皮条客与'变态者'）。","Britannica（B400）：'transformed erotic and often obscene subject matter into a poetic vision of the universe'（把情色甚至猥亵题材转化为宇宙的诗性图景）。","Britannica（B400）：热内——'a French criminal and social outcast turned writer'；1942年囚于 Fresnes 狱中写。"],
"outline":["（通说待核——B400未载剧情）圣母神像与死去的'娇美'达令：狱中的想象葬礼。","（通说待核）蒙马特黑社会的'圣徒传'式颠倒。"],
"characters":[{"name":"'娇美'达令","identity":"死者/神像","note":"（通说待核，B400未载）"},{"name":"圣母","identity":"狱中幻象","note":"（通说待核）"}],
"themes":["'黑社会的圣徒传'（通说待核）。",
 "'情色题材的诗性宇宙'（B400）。",
 "葬礼作为创作（通说待核）。"],
"influence":[{"text":"Britannica：'vividly portray[s] the prewar Montmartre underworld'（B400）。","source":"B400"},{"text":"Britannica：'poetic vision of the universe'（B400）。","source":"B400"}],
"reading":{"difficulties":["'颠倒'的圣徒传语体。","狱中写作的伦理。"],
 "editions":["《鲜花圣母》中译名（《玫瑰奇迹》）待核。","法文原版。"],
 "order":"热内首选；与《小偷日记》对读。"},
"pending":["'娇美'达令名核对（Divine说——通说）。","1943年出版（Morihien私下印说）待核。","'蒙马特'细节待核。"],
"sources":["B400"],"year_source":"B400","author_source":"B400","related_works":["wuzhizidezi" if "wuzhizidezi" in existing else "leiyu","qiaowandefangjian","zenodeyishi"],
"svg":G("《鲜花圣母》狱中幻象图",[{"title":"圣母","text":"狱中的幻象（通说）","color":"gold"},{"title":"葬礼","text":"想象的仪式（通说）","color":"main"},{"title":"蒙马特","text":"黑社会的圣传（B400）","color":"antagonist"},{"title":"诗性","text":"'宇宙的图景'（B400）","color":"family"}])},
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
        j['major_works'].insert(0, {"work_id": wid, "note": "（B39x/B40x 本作）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

for wid, aid in [('faguozhongweidenvren','fowles'), ('xianhuashengmu','genet')]:
    if wid in created:
        link(aid, wid)
print('BATCH73 DONE')
