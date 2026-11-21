# -*- coding: utf-8 -*-
"""批23：零成本二作 5 部（复用 B325-B329 已核数据：炼狱/玻璃动物园/乔瓦尼的房间/路/犹大）"""
import json, pathlib

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}

works = [
# 1. 阿瑟·米勒《萨勒姆的女巫》
{"id":"salemwunv","title":"萨勒姆的女巫","original_title":"The Crucible","region":"美国","era":"现当代","era_detail":"20世纪50年代",
"genre":"戏剧","genre_group":"戏剧","language":"英语","author_id":"amiller","author_name":"阿瑟·米勒",
"year_display":"1953年（Britannica B325：The Crucible (1953)——based on the Salem witch trials, seen as echoing McCarthyism；获Tony奖）","year_sort":1953,
"background":["Britannica（B325）：The Crucible——以塞勒姆审巫案为题材，被视为对麦卡锡主义的回应（'based on the Salem witch trials, seen as echoing McCarthyism'）；获Tony奖。","作者页（B325）：米勒把'普通人'置于悲剧中心；本剧与其《推销员之死》（1949）为同一时期两大名作。","历史背景（通说待核）：1692年马萨诸塞州塞勒姆村审巫事件。"],
"outline":["塞勒姆审巫事件：少女们的指控蔓延为猎巫狂潮（审巫史实细节通说待核——B325未载剧情）。","诚实者在拒绝诬告中赴死——个人良知与集体狂热（通说待核）。"],
"characters":[{"name":"约翰·普罗克特","identity":"农夫","note":"（通说待核，B325未载）"},{"name":"艾比盖尔","identity":"指控者","note":"（通说待核，B325未载）"}],
"themes":["审巫狂热与政治迫害的互文（B325：seen as echoing McCarthyism）。","个人良知对抗集体狂热（通说待核）。","'名'与'命'：名声社会的道德困境（通说待核）。"],
"influence":[{"text":"Britannica：The Crucible (1953) 获Tony奖（B325）。","source":"B325"},{"text":"Britannica：被视为对麦卡锡主义的回应（B325）。","source":"B325"}],
"reading":{"difficulties":["1692年塞勒姆审巫史。","清教社区语境。"],
 "editions":["《萨勒姆的女巫》（人民文学出版社《阿瑟·米勒戏剧集》等版本——通说待核）。","英文原版。"],
 "order":"与《推销员之死》并读：米勒两大高峰。"},
"pending":["约翰·普罗克特/艾比盖尔人名核对（B325未载）。","中译名两说（《萨勒姆的女巫》/《炼狱》）待核。","1953年首演细节（Martin Beck Theatre说）待核。"],
"sources":["B325"],"year_source":"B325","author_source":"B325","related_works":["tuixiaoyuanzhisi","leiyu","yingtaoyuan"],
"svg":G("《萨勒姆的女巫》狂热结构图",[{"title":"指控","text":"审巫的蔓延（通说）","color":"antagonist"},{"title":"普罗克特","text":"良知与赴死（通说）","color":"main"},{"title":"麦卡锡主义","text":"现实的回声（B325）","color":"gold"},{"title":"塞勒姆","text":"1692年（通说）","color":"family"}])},
# 2. 田纳西·威廉斯《玻璃动物园》
{"id":"bolidongwuyuan","title":"玻璃动物园","original_title":"The Glass Menagerie","region":"美国","era":"现当代","era_detail":"20世纪40年代",
"genre":"戏剧（回忆剧）","genre_group":"戏剧","language":"英语","author_id":"twilliams","author_name":"田纳西·威廉斯",
"year_display":"1944年（Britannica B326：The Glass Menagerie (1944)；1945年百老汇首演说通说待核）","year_sort":1944,
"background":["Britannica（B326）：'In it Williams portrayed a declassed Southern family living in a tenement.'——剧中描写一个没落的南方家庭蜗居廉价公寓。","作者页（B326）：威廉斯流派 Southern gothic；'plays reveal a world of human frustration in which sex and violence underlie an atmosphere of romantic gentility'。","题材（通说待核）：跛足女儿劳拉与她的玻璃动物收藏、母亲阿曼达的过往执念、儿子汤姆的出走。"],
"outline":["没落南方家庭：母亲温德的过去、女儿的封闭与玻璃动物、儿子的出走（细节通说待核——B326未载剧情）。","'绅士访客'来访与幻想的破灭（通说待核）。"],
"characters":[{"name":"阿曼达","identity":"母亲","note":"（通说待核，B326未载）"},{"name":"劳拉","identity":"跛足女儿","note":"（通说待核，B326未载）"},{"name":"汤姆","identity":"儿子/叙述者","note":"（通说待核，B326未载）"}],
"themes":["'没落'家庭与廉价公寓（B326：declassed Southern family living in a tenement）。","玻璃动物园：易碎的自我庇护（通说待核）。","回忆剧的形式——叙述者穿梭记忆（通说待核）。"],
"influence":[{"text":"Britannica：The Glass Menagerie (1944)——威廉斯成名作（作者页定位：此后1947年即以《欲望号街车》获普利策——B326）。","source":"B326"},{"text":"Britannica：Southern gothic 流派标注（B326）。","source":"B326"}],
"reading":{"difficulties":["回忆剧的叙述结构。","大萧条时代圣路易斯背景（通说待核）。"],
 "editions":["《玻璃动物园》中译本（人民文学/上海译文等——通说待核）。","英文原版。"],
 "order":"威廉斯入门首选，再读《欲望号街车》。"},
"pending":["1944年首演（芝加哥说）与1945百老汇说核对。","阿曼达/劳拉/汤姆人名核对（B326未载）。","'回忆剧'（memory play）术语归属待核。"],
"sources":["B326"],"year_source":"B326","author_source":"B326","related_works":["yuwanghaojieche","leiyu","xinshigudeLieshou"],
"svg":G("《玻璃动物园》庇护结构图",[{"title":"劳拉","text":"玻璃动物般的易碎（通说）","color":"main"},{"title":"阿曼达","text":"过时的门第执念（通说）","color":"antagonist"},{"title":"廉价公寓","text":"'没落家庭的蜗居'（B326）","color":"family"},{"title":"出走","text":"汤姆的逃离（通说）","color":"gold"}])},
# 3. 詹姆斯·鲍德温《乔瓦尼的房间》
{"id":"qiaowandefangjian","title":"乔瓦尼的房间","original_title":"Giovanni's Room","region":"美国","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"jbaldwin","author_name":"詹姆斯·鲍德温",
"year_display":"1956年（Britannica B327：Giovanni's Room (1956)——Knopf拒稿后由Dial Press接受）","year_sort":1956,
"background":["Britannica（B327）：Giovanni's Room——被 Knopf 以同性恋题材为由退稿，后由 Dial Press 接受出版。","作者页（B327）：鲍德温首作《向苍天呼吁》（1953）为其'semiautobiographical first and finest novel'；本剧为转向巴黎与性向题材的第二作。","题材（通说待核）：美国青年大卫在巴黎与意大利酒保乔瓦尼的感情——自我否认与毁灭。"],
"outline":["大卫在巴黎与乔瓦尼的恋情及其自我否认（情节通说待核——B327未载剧情）。","订婚的未婚妻与两个'房间'的抉择（通说待核）。"],
"characters":[{"name":"大卫","identity":"美国青年","note":"（通说待核，B327未载）"},{"name":"乔瓦尼","identity":"酒保","note":"（通说待核，B327未载）"}],
"themes":["自我否认与身份的囚室（通说待核）。","1950年代同性恋题材的出版史（B327：Knopf拒稿、Dial Press接受）。","流亡巴黎的美国人（通说待核）。"],
"influence":[{"text":"Britannica：Giovanni's Room 出版史——Knopf退稿、Dial Press接受（B327）。","source":"B327"},{"text":"Britannica：鲍德温小说列表第二作（B327）。","source":"B327"}],
"reading":{"difficulties":["1950年代性向语境。","巴黎美国流亡者圈。"],
 "editions":["《乔瓦尼的房间》中译本（人民文学/上海译文等——通说待核）。","英文原版。"],
 "order":"鲍德温第二作；与《向苍天呼吁》对照读。"},
"pending":["大卫/乔瓦尼/赫拉人名核对（B327未载）。","1956年出版（Dial Press说）待核。","退稿信内容（'发育不良'说）待核。"],
"sources":["B327"],"year_source":"B327","author_source":"B327","related_works":["xiangtianhuhan","zise","kanbujian3"],
"svg":G("《乔瓦尼的房间》囚室结构图",[{"title":"大卫","text":"自我否认（通说）","color":"main"},{"title":"乔瓦尼","text":"巴黎的房间（通说）","color":"gold"},{"title":"退稿","text":"出版史1956（B327）","color":"family"},{"title":"未婚妻","text":"两个房间（通说）","color":"antagonist"}])},
# 4. 科马克·麦卡锡《路》
{"id":"lu","title":"路","original_title":"The Road","region":"美国","era":"现当代","era_detail":"21世纪初",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"mccarthy","author_name":"科马克·麦卡锡",
"year_display":"2006年（Britannica B328：The Road (2006)——获2007年普利策奖）","year_sort":2006,
"background":["Britannica（B328）：The Road——后末日故事，写父子在未指明的灾变后求生（'Post-apocalyptic tale of a father and son surviving an unspecified disaster'）；获2007年普利策奖。","Britannica（B328）：批评界在其中发现'a new emotional depth and a note of redemption'（新的情感深度与救赎的音符）。","作者页（B328）：麦卡锡此前以《血色子午线》(1985)'hailed as his masterpiece'——本作为其赢得大众声誉阶段的顶点。"],
"outline":["父子推着购物车沿公路南行：寒冷、饥饿与同类的威胁（B328：father and son surviving an unspecified disaster；行程细节通说待核）。","'带着火'前行——善在废墟中的延续（'火'意象通说待核）。"],
"characters":[{"name":"父亲","identity":"无名","note":"（通说待核，B328未载名字）"},{"name":"儿子","identity":"无名","note":"（通说待核，B328未载）"}],
"themes":["废墟中的父子之情（B328：new emotional depth）。","'救赎的音符'——末日中的善（B328：a note of redemption）。","'死亡不可避免'的底色（B328 讣闻语境：a sense of the inevitability of death）。"],
"influence":[{"text":"Britannica：The Road (2006)——2007年普利策奖（B328）。","source":"B328"},{"text":"Britannica：'a new emotional depth and a note of redemption'（B328）。","source":"B328"}],
"reading":{"difficulties":["极简文风与无标点对话（风格通说待核）。","后末日类型传统。"],
 "editions":["《路》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"麦卡锡入门首选；进阶读《血色子午线》。"},
"pending":["父子无名设定核对（B328未载名字）。","2006年出版（Knopf说）待核。","'火'意象说法待核。","2009年电影改编待核。"],
"sources":["B328"],"year_source":"B328","author_source":"B328","related_works":["xueseziwuxian","wuhao","xinshigudeLieshou"],
"svg":G("《路》父子结构图",[{"title":"父亲","text":"护子的最后旅程（B328语境）","color":"main"},{"title":"儿子","text":"'带着火'（通说）","color":"gold"},{"title":"公路","text":"向南的求生（B328）","color":"family"},{"title":"灾变","text":"未指明的末日（B328）","color":"antagonist"}])},
# 5. 阿摩司·奥兹《犹大》
{"id":"youda","title":"犹大","original_title":"Ha-Beśorah ʿal-pi Yehudah（Judas）","region":"以色列","era":"现当代","era_detail":"21世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"希伯来语","author_id":"aoz","author_name":"阿摩司·奥兹",
"year_display":"2014年（Britannica B329：Judas (2014)——received the German Internationaler Literaturpreis in 2015）","year_sort":2014,
"background":["Britannica（B329）：Judas——获2015年德国 Internationaler Literaturpreis（国际文学奖）。","作者页（B329）：奥兹——'in whose works Israeli society is unapologetically scrutinized'；回忆录《爱与黑暗的故事》(2002)后重返小说。","题材（通说待核）：耶路撒冷的青年学者与神秘老人家中'犹太人犹大'的隐居者——对犹大形象的翻案与以色列建国争论。"],
"outline":["青年学者入住老人宅邸——与隐居老人及其照护者的三角（情节通说待核——B329未载剧情）。","'犹大'的重新解读：从叛徒到另一层含义（翻案论述通说待核）。"],
"characters":[{"name":"什穆埃尔","identity":"青年学者","note":"（通说待核，B329未载）"},{"name":"格罗法纳斯老人","identity":"隐居者","note":"（通说待核，B329未载）"}],
"themes":["犹大形象的翻案（通说待核）。","以色列建国路线之争——'毫不留情的审视'（B329：unapologetically scrutinized）。","1959-60年代耶路撒冷（时代背景通说待核）。"],
"influence":[{"text":"Britannica：Judas (2014)——2015年 Internationaler Literaturpreis（B329）。","source":"B329"},{"text":"Britannica：奥兹作品对以色列社会的审视定位（B329）。","source":"B329"}],
"reading":{"difficulties":["犹大在基督教与犹太传统中的双重形象。","以色列建国史争论。"],
 "editions":["《犹大》中译本（译林出版社——通说待核）。","希伯来文原版。"],
 "order":"奥兹进阶；先读回忆录《爱与黑暗的故事》。"},
"pending":["什穆埃尔/格罗法纳斯人名核对（B329未载）。","2014年出版（Keter说）待核。","'翻案'论述细节待核。"],
"sources":["B329"],"year_source":"B329","author_source":"B329","related_works":["aiyuheandegushi","ezhihua","renshijian"],
"svg":G("《犹大》翻案结构图",[{"title":"犹大","text":"叛徒的另一面（通说）","color":"gold"},{"title":"青年学者","text":"入宅的局外人（通说）","color":"main"},{"title":"老人宅","text":"隐居的秘密（通说）","color":"family"},{"title":"建国争论","text":"社会的审视（B329）","color":"antagonist"}])},
]
for w in works:
    assert w['id'] not in existing, f'duplicate id {w["id"]}'
    assert 'ed_marker' not in w, 'bug'
    works_ok = w
for w in works:
    if 'ed_marker' in w: del w['ed_marker']

for w in works:
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

# 作者页 major_works 补挂
link = {"amiller":"salemwunv","twilliams":"bolidongwuyuan","jbaldwin":"qiaowandefangjian","mccarthy":"lu","aoz":"youda"}
notes = {"salemwunv":"1953（B325）","bolidongwuyuan":"1944（B326）","qiaowandefangjian":"1956（B327）","lu":"2006——2007普利策奖（B328）","youda":"2014——2015国际文学奖（B329）"}
for aid, wid in link.items():
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        j['major_works'].append({"work_id": wid, "note": notes[wid]})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)
print('BATCH23 DONE')
