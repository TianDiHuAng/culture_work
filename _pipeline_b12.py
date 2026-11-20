# -*- coding: utf-8 -*-
"""流水线批次12（最后一批）：Britannica 新核 4 部 + 零成本直写 2 部"""
import json, pathlib

new_src = [
{"id":"B302","title":"Horace — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Horace-Roman-poet","type":"百科全书","verified":True,"covers":["horace","geti"],"note":"2026-11-21 核对：65 BC Venusia生—8 BC 11月27日罗马卒（葬于 Esquiline 近梅塞纳斯墓）；Odes——三卷88首 short poems 23 BC 出版；第四卷15首（最晚诗属13 BC）；'The third book, the Epistles to the Pisos, was also known……as the Ars poetica'（约19—18 BC）——'a series of insights into writing poetry, choosing genres, and combining genius with craftsmanship'；carpe diem——'pluck the day'或'seize the day'为贯穿主题；在菲力皮为布鲁图斯作战、失去家庭农场；经梅塞纳斯赞助成为'Augustus unofficial poet laureate'"},
{"id":"B303","title":"Gaius Petronius Arbiter — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Gaius-Petronius-Arbiter","type":"百科全书","verified":True,"covers":["petronius","sadiLikong"],"note":"2026-11-21 核对：卒于66 AD；'probably consul in ad 62 or 63'；被尼禄纳入内圈'as his director of elegance (arbiter elegantiae), whose word on all matters of taste was law'；Satyricon——'The longest and the best episode in the surviving portions……is the Cena Trimalchionis, or Banquet of Trimalchio (ch. 26–78)'；存世部分'probably represent about one-tenth of the complete work'；'Trimalchio is the quintessence of the parvenu'；散文与韵文混合；语言'pure, easy, and elegant'但如'written quickly and somewhat carelessly'——'In his book, as in his life, Petronius achieved fame by indolence'"},
{"id":"B304","title":"Juvenal — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Juvenal","type":"百科全书","verified":True,"covers":["youweinalisi","fengshishi"],"note":"2026-11-21 核对：生于'55–60? ce' Aquinum；卒'probably in or after 127'；图密善治下放逐（81–96）、96年返罗马；卷一发表于100—110之间、卷五提及127年；16首讽刺诗——'The Satires attack two main themes: the corruption of society in the city of Rome and the follies and brutalities of mankind'；名句：'bread and circuses'、'Who will guard the guards themselves?'、'a sound mind in a sound body, and a brave heart'、'Slow rises worth, by poverty oppressed'、'The greatest reverence is due to a child'；对薄伽丘、布瓦洛、拜伦的影响；'Juvenalian satire'以其名命名"},
{"id":"B305","title":"The Barber of Seville (play by Beaumarchais) — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/The-Barber-of-Seville-play","type":"百科全书","verified":True,"covers":["beaumarchais","saiweiliyadelifeishi"],"note":"2026-11-21 核对：'four-act farcical drama' performed and published in 1775 as Le Barbier de Séville（或 The Useless Precaution）；情节：Almaviva伯爵爱Rosine（Bartholo的监护少女）、以伪装（乐师Alonzo）与Figaro的帮助胜出并完婚；'The play achieved great popularity for its ingeniously constructed plot and lively wit'；是1816年罗西尼歌剧的基础；作者生平页 404——博马舍生平（1732—1799说）为通说待核"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new_src:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")
raw = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for s in raw:
    seen[s["id"]] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources:", len(out))

authors = {
"horace": {
  "id": "horace", "name": "贺拉斯", "foreign_name": "Horace（昆图斯·霍拉提乌斯·弗拉库斯，公元前65年12月—公元前8年11月27日）",
  "country": "古罗马", "birth": -65, "death": -8, "birth_year": -65, "death_year": -8, "era": "古代",
  "summary": "贺拉斯（昆图斯·霍拉提乌斯·弗拉库斯），维努西亚生，'a leading Latin lyric poet and satirist of the Augustan Age'（奥古斯都时代拉丁抒情诗与讽刺诗的领军者——Britannica），作品把希腊抒情形式移植入拉丁语。曾为布鲁图斯在菲力皮作战、失去家庭农场，经梅塞纳斯赞助而 rise 至'Augustus' unofficial poet laureate'（奥古斯都的非官方桂冠诗人——Britannica）。Odes 三卷88首 short poems 23 BC 出版；第四卷15首（最晚诗属13 BC——B302）。《诗艺》（约19—18 BC）——'a series of insights into writing poetry, choosing genres, and combining genius with craftsmanship'（B302）。carpe diem（'pluck the day'/'seize the day'）为贯穿主题（B302）。",
  "timeline": [
    {"year": -65, "text": "12月生于维努西亚（B302：Born December 65 BC in Venusia, Italy）。", "src": "B302"},
    {"year": -42, "text": "菲力皮之战为布鲁图斯而战，战后失农场（B302 语境）。", "src": "B302"},
    {"year": -23, "text": "Odes 三卷88首出版（B302：published three books, comprising 88 short poems, in 23 bc）。", "src": "B302"},
    {"year": -13, "text": "第四卷15首（最晚诗属13 BC——B302）。", "src": "B302"},
    {"year": -8, "text": "11月27日卒于罗马（B302：died Nov. 27, 8 BC in Rome）。", "src": "B302"}],
  "major_works": [
    {"work_id": "geti", "note": "抒情诗集（B302：三卷88首23 BC+第四卷15首）"},
    {"title": "诗艺", "note": "（B302：Ars Poetica，约19—18 BC）"},
    {"title": "讽刺诗集、书信集", "note": "（B302：Satires, Epistles）"}],
  "style": [
    "'leading Latin lyric poet and satirist of the Augustan Age'（B302）。",
    "把希腊抒情形式移植入拉丁语（B302 语境：adapted Greek lyric forms into Latin）。",
    "carpe diem——'seize the day'（B302：贯穿主题）。"],
  "status": "Britannica 定位贺拉斯为奥古斯都时代拉丁抒情诗与讽刺诗领军者、'奥古斯都的非官方桂冠诗人'（B302）。",
  "sources": ["B302"], "dates_source": "B302",
  "pending": ["'carpe diem'出自《颂歌》第1.11的原文核对。", "第四卷15首年份核对。", "梅塞纳斯赞助关系（B302 已载）展开核对。"]
},
"petronius": {
  "id": "petronius", "name": "佩特罗尼乌斯", "foreign_name": "Petronius Arbiter（佩特罗尼乌斯·阿尔比特尔，卒于公元66年）",
  "country": "古罗马", "birth": None, "death": 66, "birth_year": None, "death_year": 66, "era": "古代",
  "summary": "佩特罗尼乌斯（可能名 Titus Petronius Niger），罗马贵族——任执政官（'probably consul in ad 62 or 63'——B303）后为尼禄的'director of elegance (arbiter elegantiae), whose word on all matters of taste was law'（趣味裁定者——B303）；66年因诬陷谋反被迫自尽（B303）。被视为《萨蒂利孔》的作者：'The longest and the best episode in the surviving portions of the Satyricon is the Cena Trimalchionis, or Banquet of Trimalchio (ch. 26–78)'（特里马尔奇奥的宴会——B303）；存世部分'probably represent about one-tenth of the complete work'（B303）；'Trimalchio is the quintessence of the parvenu'（暴发户的典型——B303）。",
  "timeline": [
    {"year": 62, "text": "约62或63年任执政官（B303：probably consul in ad 62 or 63）。", "src": "B303"},
    {"year": 66, "text": "因诬陷谋反而被迫自尽（B303：forced suicide in 66 CE after a false conspiracy accusation）。", "src": "B303"},
    {"year": None, "text": "《萨蒂利孔》写作年代与成书不确（通说待核）。", "src": "B303"}],
  "major_works": [
    {"work_id": "sadiliKong", "note": "小说（存世残篇）（B303：Satyricon）"}],
  "style": [
    "'arbiter elegantiae'：趣味裁定者（B303）。",
    "散文与韵文混合（B303：mixture of prose and verse）。",
    "语言'pure, easy, and elegant'（B303）——'achieved fame by indolence'（B303）。"],
  "status": "Britannica 定位佩特罗尼乌斯为罗马贵族、《萨蒂利孔》的'公认'作者——生年不详、66年自尽（B303）。",
  "sources": ["B303"], "dates_source": "B303",
  "pending": ["作者全名（Titus Petronius Niger说）待核。", "《萨蒂利孔》残篇（第15、16卷部分）细节待核。", "特里马尔奇奥宴会（第26—78章）细节核对。"]
},
"youweinalisi": {
  "id": "youweinalisi", "name": "尤维纳利斯", "foreign_name": "Juvenal（德基穆斯·尤尼乌斯·尤维纳利斯，约公元55/60—约127年后）",
  "country": "古罗马", "birth": 57, "death": 127, "birth_year": 57, "death_year": 127, "era": "古代",
  "summary": "尤维纳利斯（Decimus Junius Juvenalis），意大利阿奎南姆生（B304：Born '55–60? ce' in Aquinum）——罗马讽刺诗人，16首讽刺诗'the corruption of society in the city of Rome and the follies and brutalities of mankind'（谴责罗马社会的腐败与人类的愚蠢残忍——B304）。图密善治下被放逐（81—96）、96年返罗马（B304）；卷一发表于100—110之间（B304）。其尖锐警句与对薄伽丘、布瓦洛、拜伦的影响使其成为'最有力量的罗马讽刺诗人'，'Juvenalian satire'以其名命名（B304 语境）。",
  "timeline": [
    {"year": 57, "text": "约生于阿奎南姆（B304：Born '55–60? ce' in Aquinum, Italy）。", "src": "B304"},
    {"year": 96, "text": "图密善死后返罗马（B304：banishment under Domitian (81–96 ce); return to Rome in 96）。", "src": "B304"},
    {"year": 100, "text": "卷一发表于100—110之间（B304）。", "src": "B304"},
    {"year": 127, "text": "约卒（B304：probably in or after 127；卷五提及127年）。", "src": "B304"}],
  "major_works": [
    {"work_id": "fengshishi", "note": "讽刺诗集（B304：16首 Satires）"}],
  "style": [
    "' Juvenalian satire'以其名命名（B304 语境）。",
    "警句的锋利（B304：biting epigrams）。",
    "'面包与马戏''谁来监督监督者'等警句（B304）。"],
  "status": "Britannica 定位尤维纳利斯为罗马讽刺诗人——对后世讽刺文学影响深远（B304 语境）。",
  "sources": ["B304"], "dates_source": "B304",
  "pending": ["16首讽刺诗篇目核对。", "放逐原因（演员潘托米姆斯事件说）待核。", "名句原文逐条核对。"]
},
"beaumarchais": {
  "id": "beaumarchais", "name": "博马舍", "foreign_name": "Pierre-Augustin Caron de Beaumarchais（皮埃尔-奥古斯丁·卡龙·德·博马舍，1732—1799，生卒通说待核）",
  "country": "法国", "birth": 1732, "death": 1799, "birth_year": 1732, "death_year": 1799, "era": "近代",
  "summary": "博马舍，法国钟表匠出身的剧作家与冒险家（生卒通说待核）。'four-act farcical drama'《塞维利亚的理发师》'performed and published in 1775'（B305）——'The play achieved great popularity for its ingeniously constructed plot and lively wit'（以精巧的情节与活泼的机智大获成功——B305）；是1816年罗西尼歌剧的基础（B305）。费加罗三部曲（《理发师》《费加罗的婚礼》《有罪的母亲》——通说待核）。",
  "timeline": [
    {"year": 1732, "text": "生于巴黎（1732年说——通说待核）。", "src": "B305"},
    {"year": 1775, "text": "《塞维利亚的理发师》上演并出版（B305：performed and published in 1775）。", "src": "B305"},
    {"year": 1799, "text": "卒（1799年5月18日说——通说待核）。", "src": "B305"}],
  "major_works": [
    {"work_id": "saiweiliyadelifeishi", "note": "喜剧（B305：1775）"},
    {"title": "费加罗的婚礼", "note": "（1784年说——通说待核）"},
    {"title": "有罪的母亲", "note": "（通说待核）"}],
  "style": [
    "'ingeniously constructed plot and lively wit'（B305：精巧情节与活泼机智）。",
    "费加罗三部曲：仆人的智慧喜剧（通说待核）。",
    "钟表匠出身的'冒险家'（通说待核）。"],
  "status": "Britannica 作品页确认《塞维利亚的理发师》1775年演出出版、'achieved great popularity'（B305）；作者生平（1732—1799说）为通说待核。",
  "sources": ["B305"], "dates_source": "B305",
  "pending": ["生卒年（1732—1799）与巴黎出生核对。", "费加罗三部曲（1784《费加罗的婚礼》说）核对。", "莫扎特《费加罗的婚礼》歌剧（1786）待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"geti": {
  "id":"geti","title":"歌集","original_title":"Carmina（Odes，颂歌集三卷+第四卷）","region":"古罗马","era":"古代","era_detail":"奥古斯都时代",
  "genre":"抒情诗集","genre_group":"诗歌","language":"拉丁语","author_id":"horace","author_name":"贺拉斯（昆图斯·霍拉提乌斯·弗拉库斯）",
  "year_display":"三卷88首23 BC出版、第四卷15首13 BC（Britannica：published three books, comprising 88 short poems, in 23 bc）","year_sort":-23,
  "background":["Britannica（B302）：'he turned, in the most active period of his poetical life, to the Odes, of which he published three books, comprising 88 short poems, in 23 bc'；第四卷——'a fourth book of 15 Odes, mainly of a more serious (and political) character'。","carpe diem——'pluck the day'或'seize the day'为贺拉斯贯穿主题（B302）。"],
  "outline":["希腊抒情形式的拉丁化：阿尔凯奥斯体、萨福体（通说待核）。","名句：carpe diem（及时行乐/抓住今天）（B302：concept defined as 'pluck the day' or 'seize the day'）。"],
  "characters":[{"name":"贺拉斯","identity":"抒情诗人","note":"'Augustus' unofficial poet laureate'（B302）"}],
  "themes":["carpe diem（B302）。",
   "友谊、美酒、爱国的颂歌（通说待核）。",
   "希腊形式的拉丁移植（B302 语境：adapted Greek lyric forms into Latin）。"],
  "influence":[{"text":"Britannica：'a leading Latin lyric poet and satirist of the Augustan Age'（B302）。","source":"B302"},
   {"text":"Britannica：'Augustus unofficial poet laureate'（B302）。","source":"B302"}],
  "reading":{"difficulties":["拉丁语阿尔凯奥斯体与萨福体。","罗马政治背景（奥古斯都时代）。"],
   "editions":["《贺拉斯诗选》（人民文学出版社，通说待核）。","拉丁文原版（公有领域）。"],
   "order":"与《诗艺》合读。"},
  "pending":["88首+15首的总数核对。","carpe diem 原句（1.11）核对。","梅塞纳斯赞助（B302 已载）展开核对。"],
  "sources":["B302"],"year_source":"B302","author_source":"B302","related_works":["aeneid","shenqu","qingtongqishi"],
  "svg":G2("《歌集》结构图",[{"title":"三卷88首","text":"23 BC（B302）","color":"main"},{"title":"第四卷","text":"15首（13 BC）","color":"gold"},{"title":"carpe diem","text":"抓住今天","color":"family"},{"title":"梅塞纳斯","text":"赞助人（B302）","color":"plain"}])
},
"sadiliKong": {
  "id":"sadiliKong","title":"萨蒂利孔","original_title":"Satyricon","region":"古罗马","era":"古代","era_detail":"尼禄时代（1世纪）",
  "genre":"小说（存世残篇）","genre_group":"小说","language":"拉丁语","author_id":"petronius","author_name":"佩特罗尼乌斯（'arbiter elegantiae'）",
  "year_display":"成书年代不确（约1世纪——通说待核）；作者卒于66年（Britannica：died in ad 66）","year_sort":60,
  "background":["Britannica（B303）：'The longest and the best episode in the surviving portions of the Satyricon is the Cena Trimalchionis, or Banquet of Trimalchio (ch. 26–78)'；存世部分'probably represent about one-tenth of the complete work'。","作者（B303）：'welcomed by Nero into his inner circle as his director of elegance (arbiter elegantiae), whose word on all matters of taste was law'。"],
  "outline":["恩科尔皮乌斯与 Giton 的流浪——特里马尔奇奥的宴会（第26—78章）（B303）。","'Trimalchio is the quintessence of the parvenu'（暴发户的典型——B303）。"],
  "characters":[{"name":"特里马尔奇奥","identity":"暴发户","note":"'quintessence of the parvenu'（B303）"},{"name":"恩科尔皮乌斯","identity":"叙述者","note":"（通说待核）"}],
  "themes":["暴发户的讽刺（B303）。",
   "散文与韵文混合（B303：mixture of prose and verse）。",
   "尼禄时代的'趣味'与虚伪（B303 语境：arbiter elegantiae）。"],
  "influence":[{"text":"Britannica：'In his book, as in his life, Petronius achieved fame by indolence'（B303）。","source":"B303"},
   {"text":"作者页：'pure, easy, and elegant'的语言（B303）。","source":"B303"}],
  "reading":{"difficulties":["残篇的断裂。","拉丁俗语。"],
   "editions":["《萨蒂利孔》（人民文学出版社/上海译文版本，通说待核）。","拉丁文原版（公有领域）。"],
   "order":"古典讽刺进阶之作。"},
  "pending":["宴会章节（26—78）细节核对。","残篇比例（十分之一说——B303 已载）核对。","费里尼电影（1969年 Fellini Satyricon）待核。"],
  "sources":["B303"],"year_source":"B303","author_source":"B303","related_works":["bianxingji_ovid","aeneid","嘉莉妹妹"] ,
  "svg":G2("《萨蒂利孔》宴会结构图",[{"title":"宴会","text":"特里马尔奇奥（B303）","color":"antagonist"},{"title":"暴发户","text":"parvenu 的典型","color":"main"},{"title":"散文与韵文","text":"混合文体（B303）","color":"gold"},{"title":"残篇","text":"十分之一（B303）","color":"family"}])
},
"fengshishi": {
  "id":"fengshishi","title":"讽刺诗集","original_title":"Saturae（16首 Satires）","region":"古罗马","era":"古代","era_detail":"1—2世纪",
  "genre":"讽刺诗集","genre_group":"诗歌","language":"拉丁语","author_id":"youweinalisi","author_name":"尤维纳利斯（Decimus Junius Juvenalis）",
  "year_display":"卷一发表于100—110年间（Britannica：Book One issued between 100 and 110；卷五提及127年）","year_sort":100,
  "background":["Britannica（B304）：'The Satires attack two main themes: the corruption of society in the city of Rome and the follies and brutalities of mankind'（谴责罗马社会的腐败与人类的愚蠢残忍——B304）。","名句（B304）：'bread and circuses'（面包与马戏）、'Who will guard the guards themselves?'（谁来监督监督者）、'a sound mind in a sound body, and a brave heart'、'Slow rises worth, by poverty oppressed'、'The greatest reverence is due to a child'。","'Juvenalian satire'以其名命名（B304 语境）——对薄伽丘、布瓦洛、拜伦的影响（B304 语境）。"],
  "outline":["16首讽刺诗：罗马的腐败、富有与世袭贵族（B304：the vice, crime, misuse of wealth, and cult of hereditary nobility）。"],
  "characters":[{"name":"尤维纳利斯","identity":"讽刺诗人","note":"（B304）"}],
  "themes":["罗马的腐败与人类的残忍（B304）。",
   "'面包与马戏'（B304 名句）。",
   "'谁来监督监督者'（B304 名句）。"],
  "influence":[{"text":"Britannica：'Juvenalian satire'以其名命名——对后世讽刺文学影响（B304 语境）。","source":"B304"},
   {"text":"Britannica：警句流传（'bread and circuses'等——B304）。","source":"B304"}],
  "reading":{"difficulties":["罗马社会史。","讽刺的修辞（sermo）。"],
   "editions":["《尤维纳利斯讽刺诗》（人民文学出版社，通说待核）。","拉丁文原版（公有领域）。"],
   "order":"罗马讽刺诗首选。"},
  "pending":["16首篇目（第三首《罗马之夜》等）核对。","放逐原因（潘托米姆斯事件说）待核。","名句拉丁原文逐条核对。"],
  "sources":["B304"],"year_source":"B304","author_source":"B304","related_works":["fengshishi","luoshengmen","guanchangxianxingji"],
  "svg":G2("《讽刺诗集》名句结构图",[{"title":"面包与马戏","text":"名句（B304）","color":"gold"},{"title":"谁来监督监督者","text":"名句（B304）","color":"main"},{"title":"罗马的腐败","text":"两大主题之一（B304）","color":"antagonist"},{"title":"Juvenalian","text":"以其名命名的讽刺","color":"family"}])
},
"saiweiliyadelifeishi": {
  "id":"saiweiliyadelifeishi","title":"塞维利亚的理发师","original_title":"Le Barbier de Séville; ou, la Précaution inutile","region":"法国","era":"近代","era_detail":"18世纪",
  "genre":"四幕喜剧","genre_group":"戏剧","language":"法语","author_id":"beaumarchais","author_name":"博马舍（Pierre-Augustin Caron de Beaumarchais，生平通说待核）",
  "year_display":"1775年演出并出版（Britannica：performed and published in 1775）","year_sort":1775,
  "background":["Britannica（B305）：'four-act farcical drama'，'performed and published in 1775'；情节：Almaviva伯爵爱Rosine（Bartholo医生欲娶之而将其锁于家）——伪装（乐师Alonzo）与Figaro的帮助下胜出并完婚。","'The play achieved great popularity for its ingeniously constructed plot and lively wit'（B305）；'was the basis of the 1816 opera' Il barbiere di Siviglia by Rossini（B305）。"],
  "outline":["Almaviva的伪装求爱：音乐师Alonzo、醉兵——Figaro的机智（B305 语境）。","Bartholo的阻挠与婚约的达成（B305 语境）。"],
  "characters":[{"name":"费加罗","identity":"理发师","note":"（B305）"},{"name":"阿玛维瓦伯爵","identity":"伯爵","note":"（B305）"},{"name":"罗西娜","identity":"少女","note":"（B305：Rosine）"}],
  "themes":["'精巧的情节与活泼的机智'（B305）。",
   "仆人的智慧（Figaro——B305 语境）。",
   "启蒙时代的反讽（通说待核）。"],
  "influence":[{"text":"Britannica：'The play achieved great popularity for its ingeniously constructed plot and lively wit'（B305）。","source":"B305"},
   {"text":"Britannica：1816年罗西尼歌剧的基础（B305）。","source":"B305"}],
  "reading":{"difficulties":["法语喜剧对白。","费加罗三部曲顺序。"],
   "editions":["《塞维利亚的理发师》（收于博马舍戏剧集，通说待核）。","法文原版（公有领域）。"],
   "order":"费加罗三部曲之首（理发师→婚礼→有罪的母亲）。"},
  "pending":["1775年2月首演（Comédie-Française说）核对。","Rosine/Bartholo人名核对。","《费加罗的婚礼》1784年说待核。"],
  "sources":["B305"],"year_source":"B305","author_source":"B305","related_works":["fuhiu","bukeerxi","tangjihede"],
  "svg":G2("《理发师》智斗结构图",[{"title":"Almaviva","text":"伪装的伯爵","color":"main"},{"title":"Figaro","text":"机智的理发师（B305）","color":"gold"},{"title":"Bartholo","text":"锁住少女的医生","color":"antagonist"},{"title":"罗西娜","text":"被监护者","color":"family"}])
},
"beidezhe": {
  "id":"beidezhe","title":"背德者","original_title":"L'Immoraliste（The Immoralist）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"gide","author_name":"安德烈·纪德",
  "year_display":"1902年（作者页 B275 口径：L'Immoraliste (1902)——创作盛期之作）","year_sort":1902,
  "background":["作者页（B275）：纪德 major_works 载'L'Immoraliste (1902)'——'the page lists it among works from his great creative period'（创作盛期——B275）；问题（B275 问答）：'the point at which concern for the self must be superseded by moral principles'（对自我的关切何时须被道德原则取代）。","纪德（B275）：1947年诺奖；'probed individual freedom and moral ambiguity'。"],
  "outline":["米歇尔的北非觉醒与自我放纵——'背德'的自白（通说待核）。","玛尔塞拉的病与死（通说待核）。"],
  "characters":[{"name":"米歇尔","identity":"学者","note":"（通说待核）"},{"name":"玛尔塞拉","identity":"妻子","note":"（通说待核）"}],
  "themes":["自我的觉醒与'背德'（B275：moral ambiguity 语境）。",
   "'自我关切与道德原则'的边界（B275 问答）。",
   "北非的身体苏醒（通说待核）。"],
  "influence":[{"text":"作者页：纪德创作盛期之作（B275 作者页口径）。","source":"B275"},
   {"text":"Britannica：纪德1947年诺奖（B275 作者级）。","source":"B275"}],
  "reading":{"difficulties":["'背德'的伦理阅读。","殖民地北非背景。"],
   "editions":["《背德者》（人民文学出版社/上海译文版本，通说待核）。","法文原版（Gallimard）。"],
   "order":"先《窄门》后本作（两极对照）。"},
  "pending":["1902年出版（Mercure de France说）核对。","米歇尔/玛尔塞拉人名核对。","与《窄门》的对位（作者婚姻语境——B275 已载）待核。"],
  "sources":["B275"],"year_source":"B275","author_source":"B275","related_works":["weibizaozhe","xianzhi","duoluo"],
  "svg":G2("《背德者》觉醒结构图",[{"title":"北非","text":"身体的苏醒","color":"family"},{"title":"米歇尔","text":"自我的放纵","color":"main"},{"title":"玛尔塞拉","text":"病与死","color":"antagonist"},{"title":"背德","text":"道德的边界（B275）","color":"gold"}])
},
"baoliququ": {
  "id":"baoliququ","title":"暴力夺取","original_title":"The Violent Bear It Away","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"oconnor","author_name":"弗兰纳里·奥康纳",
  "year_display":"1960年（作者页 B291 口径：The Violent Bear It Away (1960)）","year_sort":1960,
  "background":["作者页（B291）：奥康纳 major_works 载'The Violent Bear It Away (1960)'（B291 作者页定位，详见 haorennanxun 条核对）。","题材（通说待核）：少年塔沃特与叔公老梅森的'先知'使命——世俗教育与先知书的对撞。"],
  "outline":["老梅森去世——塔沃特拒绝先知使命却终被'暴力'夺取（通说待核）。"],
  "characters":[{"name":"塔沃特","identity":"少年","note":"（通说待核）"},{"name":"老梅森","identity":"叔公","note":"先知（通说待核）"}],
  "themes":["先知的'暴力'使命（书名通说——出自《马太福音》语境待核）。",
   "世俗教育与宗教召唤的对撞（通说待核）。",
   "南方哥特（B291 作者级语境）。"],
  "influence":[{"text":"作者页：奥康纳第二部长篇（B291 作者页口径）。","source":"B291"},
   {"text":"作者页：'violence……preparing them to accept their moment of grace'（B291 作者自述）。","source":"B291"}],
  "reading":{"difficulties":["先知书意象。","双重叙事（雷拜与塔沃特）。"],
   "editions":["《暴力夺取》（新星出版社《慧血：奥康纳作品集》，通说待核）。","英文原版。"],
   "order":"先《慧血》后本作。"},
  "pending":["1960年出版（Farrar, Straus说）核对。","塔沃特/老梅森人名核对。","书名出处（《马太福音》11:12说）待核。"],
  "sources":["B291"],"year_source":"B291","author_source":"B291","related_works":["huixue","haorennanxun","juwairen"],
  "svg":G2("《暴力夺取》先知结构图",[{"title":"老梅森","text":"先知的遗嘱","color":"family"},{"title":"塔沃特","text":"拒绝的少年","color":"main"},{"title":"暴力","text":"夺取的恩典","color":"antagonist"},{"title":"书名","text":"马太福音语境（待核）","color":"gold"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
