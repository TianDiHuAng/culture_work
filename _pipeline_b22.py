# -*- coding: utf-8 -*-
"""批22：来源修复（B315/316/317 撞号重建 B330-B335）+ Britannica 新核 5 作家 5 部（B325-B329）"""
import json, pathlib, re

# ============ A. 修复来源 ============
srcs = json.load(open('sources.json', encoding='utf-8'))
by_id = {s['id']: s for s in srcs}

# 移除重复/错位条目（B315=奥尼尔重复B272、B316=格林重复B320、B322=卡夫卡重复B317）
for bad in ['B315', 'B316', 'B322']:
    assert bad in by_id, bad
srcs = [s for s in srcs if s['id'] not in ('B315', 'B316', 'B322')]

repairs = [
{"id":"B330","title":"Emile Zola — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Emile-Zola","type":"百科全书","verified":True,"covers":["zola","nana","mengya"],"note":"2026-11-21 重核（原B315被覆盖后重建）：1840-04-02巴黎生—1902-09-28巴黎卒（62岁）；'the leading French novelist of the late 19th century, founder of literary naturalism'；'20-novel Rougon-Macquart cycle'（1871—1893）；'J'accuse' 1898-01-13刊于L'Aurore——'prosecuted for libel and found guilty'；Nana 在 Notable Works 列表"},
{"id":"B331","title":"Carson McCullers — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Carson-McCullers","type":"百科全书","verified":True,"covers":["mccalles","xinshigudeLieshou"],"note":"2026-11-21 重核（原B315被覆盖后重建）：原名 Lula Carson Smith；1917-02-19佐治亚州哥伦布生—1967-09-29纽约Nyack卒（50岁）；'depict the inner lives of lonely people'；The Heart Is a Lonely Hunter (1940)——四小镇居民：痴爱音乐的少女、失败的社会主义者、黑人医生、咖啡馆鳏夫；'I live with the people I create and it has always made my essential loneliness less keen.'；The Member of the Wedding (1946)——百老汇演出逾一年（田纳西·威廉斯鼓励其改编为舞台剧）"},
{"id":"B332","title":"Truman Capote — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Truman-Capote","type":"百科全书","verified":True,"covers":["capote","lengxue"],"note":"2026-11-21 重核（原B316被覆盖后重建）：1924-09-30新奥尔良生—1984-08-25洛杉矶卒（59岁）；In Cold Blood——'nonfiction novel'——'a chilling account of the murders of four members of the Clutter family, committed in Holcomb, Kansas in 1959'（Britannica 口径 1965：1965年《纽约客》连载并成书——1966年单行本说通说待核）；Other Voices, Other Rooms (1948)——'a sensitive, partly autobiographical portrayal of a boy's search for his father'；Breakfast at Tiffany's (1958)——Holly Golightly 'a young fey café society girl'"},
{"id":"B333","title":"J.D. Salinger — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/J-D-Salinger","type":"百科全书","verified":True,"covers":["salinger","maitian","jiugushi"],"note":"2026-11-21 重核（原B316被覆盖后重建）：1919-01-01曼哈顿生—2010-01-27 Cornish卒（91岁）；The Catcher in the Rye (1951)——'relates in authentic teenage idiom his flight from the phony adult world, his search for innocence and truth'；'The humor and colorful language of The Catcher in the Rye place it in the tradition of Mark Twain's'；'After the success of The Catcher in the Rye, Salinger became a recluse'；'His last published work was a novella titled Hapworth 16, 1924'"},
{"id":"B334","title":"Ralph Ellison — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Ralph-Ellison","type":"百科全书","verified":True,"covers":["ellison","kanbujian3"],"note":"2026-11-21 重核（原B317被覆盖后重建）：1913-03-01俄克拉何马城生（出生证年份被涂改为1914——'the year appears to have been altered from 1913 on the document'）—1994-04-16曼哈顿卒（81岁，胰腺癌）；Invisible Man (1952)——'a naive and idealistic (and, significantly, nameless) Southern Black youth'——'won the 1953 National Book Award for fiction'——'the first Black author to win that honor'；Shadow and Act (1964)；开场引文 'I am an invisible man... I am invisible, understand, simply because people refuse to see me.'"},
{"id":"B335","title":"Richard Wright — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Richard-Wright","type":"百科全书","verified":True,"covers":["wright","tuyuzhizideneizi"],"note":"2026-11-21 重核（原B317被覆盖后重建）：1908-09-04密西西比州种植园生—1960-11-28巴黎卒；Native Son (1940)——'a disturbing and brutally honest novel'；Black Boy (1945)——自传；'the first African American writer to gain a large white readership'"},
]

newsrc = [
{"id":"B325","title":"Arthur Miller — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Arthur-Miller-American-playwright","type":"百科全书","verified":True,"covers":["amiller","tuixiaoyuanzhisi"],"note":"2026-11-21 核对：1915-10-17纽约生—2005-02-10康涅狄格州Roxbury卒（89岁）；Death of a Salesman (1949)——'one of the most famous American plays of its period'——'the tragedy of Willy Loman, a man destroyed by false values that are in large part the values of his society'——'won a Tony Award for best play and a Pulitzer Prize for drama'；'the common man'置于悲剧中心；引文 'In fact, it is the common man who knows this fear best.'；All My Sons (1947)——第一部重要剧作获Tony奖；The Crucible (1953)——塞勒姆审巫案呼应麦卡锡主义，获Tony奖"},
{"id":"B326","title":"Tennessee Williams — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Tennessee-Williams","type":"百科全书","verified":True,"covers":["twilliams","yuwanghaojieche"],"note":"2026-11-21 核对：原名 Thomas Lanier Williams；1911-03-26密西西比州Columbus生—1983-02-25纽约卒（71岁）；'whose plays reveal a world of human frustration in which sex and violence underlie an atmosphere of romantic gentility'；A Streetcar Named Desire (1947)——'a study of the mental and moral ruin of Blanche DuBois, another former Southern belle'——获普利策戏剧奖；The Glass Menagerie (1944)——'In it Williams portrayed a declassed Southern family living in a tenement.'；Cat on a Hot Tin Roof (1955)——普利策奖；流派 Southern gothic；'His works won four Drama Critics' awards'"},
{"id":"B327","title":"James Baldwin — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/James-Baldwin","type":"百科全书","verified":True,"covers":["jbaldwin","xiangtianhuhan"],"note":"2026-11-21 核对：1924-08-02纽约生—1987-12-01法国Saint-Paul de Vence卒（63岁，胃癌）；Go Tell It on the Mountain (1953)——'semiautobiographical first and finest novel'——取材少年讲道岁月；'Those three years in the pulpit…that is what turned me into a writer.'；Giovanni's Room (1956)——Knopf拒稿后Dial Press接受；Notes of a Native Son (1955)；The Fire Next Time (1963)"},
{"id":"B328","title":"Cormac McCarthy — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Cormac-McCarthy","type":"百科全书","verified":True,"covers":["mccarthy","xueseziwuxian"],"note":"2026-11-21 核对：1933-07-20罗得岛州Providence生—2023-06-13新墨西哥州Santa Fe卒（89岁）；Blood Meridian (1985)——'a violent frontier tale loosely based on historical events'——'a critical sensation, hailed as his masterpiece'——14岁少年加入美墨边境（1840年代）无法无天的剥头皮团伙，头目'the judge'；Harold Bloom：'the ultimate Western, not to be surpassed'；首印不足1500册；引文 'There's no such thing as life without bloodshed.'；All the Pretty Horses (1992)——National Book Award；The Road (2006)——2007普利策奖；Border Trilogy (1992-98)；1981 MacArthur fellowship"},
{"id":"B329","title":"Amos Oz — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Amos-Oz","type":"百科全书","verified":True,"covers":["aoz","aiyuheandegushi"],"note":"2026-11-21 核对：原名 Amos Klausner；1939-05-04耶路撒冷生—2018-12-28卒（79岁）；'an Israeli novelist, short-story writer, and essayist in whose works Israeli society is unapologetically scrutinized'；回忆录 Sipur ʿal ahavah ve-ḥoshekh（A Tale of Love and Darkness, 2002）——'drew wide critical acclaim'；1967六日战争后投身以色列和平运动；'Oz felt himself unable to share the optimistic outlook and ideological certainties of Israel's founding generation'；Judas (2014)——2015 Internationaler Literaturpreis"},
]

srcs.extend(repairs)
srcs.extend(newsrc)
seen = {}
for s in srcs:
    seen[s['id']] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path('sources.json').write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf-8')
print('sources:', len(out))

# ============ B. 重指既有文件 + 引文修正 ============
REPOINT = {
 'nana': ('B315','B330'), 'zola': ('B315','B330'),
 'xinshigudeLieshou': ('B315','B331'), 'mccalles': ('B315','B331'),
 'lengxue': ('B316','B332'), 'capote': ('B316','B332'),
 'salinger': ('B316','B333'),
 'kanbujian3': ('B317','B334'), 'ellison': ('B317','B334'),
 'tuyuzhizideneizi': ('B317','B335'), 'wright': ('B317','B335'),
}
for stem, (old, new) in REPOINT.items():
    for d in ['data/works', 'data/authors']:
        p = pathlib.Path(d) / f'{stem}.json'
        if p.exists():
            t = p.read_text(encoding='utf-8')
            t = t.replace(old, new)
            # 引文修正——被原页面覆盖后重核，短语不在 Britannica 上
            t = t.replace('explore the spiritual isolation of misfits and outcast characters', 'depict the inner lives of lonely people')
            t = t.replace('the story of an unnamed Black man', "a naive and idealistic (and, significantly, nameless) Southern Black youth")
            t = t.replace('无名黑人的故事', '无名南方黑人青年的成长故事')
            p.write_text(t, encoding='utf-8')
            print('repointed', stem, old, '->', new)

# 冷血年份：Britannica 口径 1965（1966单行本说入 pending）
for stem in ['lengxue', 'capote']:
    p = pathlib.Path('data/works') / f'{stem}.json'
    if not p.exists():
        p = pathlib.Path('data/authors') / f'{stem}.json'
    t = p.read_text(encoding='utf-8')
    t = t.replace('In Cold Blood (1966)', 'In Cold Blood (1965)')
    t = t.replace('In Cold Blood (1966年)', 'In Cold Blood (1965)')
    t = t.replace('1966年（作者页 B332 口径：In Cold Blood (1965)）', '1965年（Britannica B332：In Cold Blood (1965)——1965年《纽约客》连载并成书；1966年1月单行本说通说待核）')
    t = t.replace('"year_sort": 1966', '"year_sort": 1965')
    t = t.replace('In Cold Blood 1966', 'In Cold Blood 1965')
    t = t.replace('1966年出版', '1965年成书（Britannica B332 口径；1966年1月单行本说待核）')
    p.write_text(t, encoding='utf-8')

# 艾里森出生年 1914→1913（Britannica：出生证被涂改）
for rel in ['data/authors/ellison.json', 'data/works/kanbujian3.json']:
    p = pathlib.Path(rel)
    t = p.read_text(encoding='utf-8')
    t = t.replace('Born March 1, 1914', 'Born March 1, 1913（出生证年份被涂改为1914）')
    t = t.replace('1914-03-01', '1913-03-01')
    p.write_text(t, encoding='utf-8')
p = pathlib.Path('data/authors/ellison.json')
j = json.loads(p.read_text(encoding='utf-8'))
if j.get('birth') == 1914: j['birth'] = 1913
if j.get('birth_year') == 1914: j['birth_year'] = 1913
p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')

# 冷血 year_sort 数字修正（JSON 层）
for rel in ['data/works/lengxue.json']:
    j = json.loads(pathlib.Path(rel).read_text(encoding='utf-8'))
    if j.get('year_sort') == 1966:
        j['year_sort'] = 1965
    j['pending'] = list(dict.fromkeys((j.get('pending') or []) + ['1966年1月单行本出版说（Random House）核对——Britannica B332 口径为1965年。']))
    pathlib.Path(rel).write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')

# 全局断言：B315/B316/B322 不再被 data/ 引用
leftover = []
for p in list(pathlib.Path('data/works').glob('*.json')) + list(pathlib.Path('data/authors').glob('*.json')):
    t = p.read_text(encoding='utf-8')
    for bad in ['B315', 'B316', 'B322']:
        if bad in t:
            leftover.append((str(p), bad))
assert not leftover, leftover
print('repoint OK, no leftover B315/B316/B322')

# ============ C. 新作家页 ×5 ============
def A(id_, name, fn, country, b, d, by, dy, era, summary, timeline, works_, style, status, src, pend):
    return {"id": id_, "name": name, "foreign_name": fn, "country": country, "birth": b, "death": d,
            "birth_year": by, "death_year": dy, "era": era, "summary": summary, "timeline": timeline,
            "major_works": works_, "style": style, "status": status, "sources": [src], "dates_source": src, "pending": pend}

authors = [
A("amiller", "阿瑟·米勒", "Arthur Miller（阿瑟·米勒，1915-10-17—2005-02-10）", "美国", 1915, 2005, 1915, 2005, "现当代",
  "米勒，纽约生，美国剧作家。Death of a Salesman (1949)——'one of the most famous American plays of its period'（B325）——'the tragedy of Willy Loman, a man destroyed by false values that are in large part the values of his society'（B325），获Tony奖最佳剧作与普利策戏剧奖（B325）。米勒主张把'普通人'置于悲剧的中心——'In fact, it is the common man who knows this fear best.'（B325）。The Crucible (1953) 以塞勒姆审巫案呼应麦卡锡主义（B325）。",
  [{"year": 1915, "text": "10月17日生于纽约（B325）。", "src": "B325"},
   {"year": 1947, "text": "All My Sons——第一部重要剧作，获Tony奖（B325）。", "src": "B325"},
   {"year": 1949, "text": "Death of a Salesman——Tony最佳剧作+普利策戏剧奖（B325）。", "src": "B325"},
   {"year": 1953, "text": "The Crucible——塞勒姆审巫案呼应麦卡锡主义，获Tony奖（B325）。", "src": "B325"},
   {"year": 2005, "text": "2月10日卒于康涅狄格州Roxbury（B325）。", "src": "B325"}],
  [{"work_id": "tuixiaoyuanzhisi", "note": "1949（B325）"},
   {"title": "都是我的儿子", "note": "（B325：All My Sons, 1947）"},
   {"title": "炼狱/萨勒姆的女巫", "note": "（B325：The Crucible, 1953——中译名待核）"}],
  ["把'普通人'置于悲剧中心（B325）。",
   "'false values'的社会批判（B325）。",
   "现实主义戏剧与心理闪回结合（通说待核）。"],
  "Britannica 定位米勒为美国剧作家，《推销员之死》为其最著名剧作（B325）。",
  "B325",
  ["《推销员之死》1949-02-10 Morosco Theatre首演日期待核。","威利·洛曼自杀结局细节核对（B325未载）。","《炼狱》通行中译名（《萨勒姆的女巫》）待核。"]),
A("twilliams", "田纳西·威廉斯", "Tennessee Williams（田纳西·威廉斯，原名 Thomas Lanier Williams，1911-03-26—1983-02-25）", "美国", 1911, 1983, 1911, 1983, "现当代",
  "威廉斯，原名 Thomas Lanier Williams，密西西比州哥伦布生，美国剧作家——'whose plays reveal a world of human frustration in which sex and violence underlie an atmosphere of romantic gentility'（B326）。The Glass Menagerie (1944)——'In it Williams portrayed a declassed Southern family living in a tenement.'（B326）。A Streetcar Named Desire (1947)——'a study of the mental and moral ruin of Blanche DuBois, another former Southern belle'（B326），获普利策戏剧奖。Cat on a Hot Tin Roof (1955) 再获普利策奖（B326）。流派：Southern gothic（B326）。",
  [{"year": 1911, "text": "3月26日生于密西西比州哥伦布（B326）。", "src": "B326"},
   {"year": 1944, "text": "The Glass Menagerie——没落的南方家庭（B326）。", "src": "B326"},
   {"year": 1947, "text": "A Streetcar Named Desire——普利策戏剧奖（B326）。", "src": "B326"},
   {"year": 1955, "text": "Cat on a Hot Tin Roof——再获普利策奖（B326）。", "src": "B326"},
   {"year": 1983, "text": "2月25日卒于纽约（B326）。", "src": "B326"}],
  [{"work_id": "yuwanghaojieche", "note": "1947（B326）"},
   {"title": "玻璃动物园", "note": "（B326：The Glass Menagerie, 1944）"},
   {"title": "热铁皮屋顶上的猫", "note": "（B326：Cat on a Hot Tin Roof, 1955）"}],
  ["'浪漫门面之下的性与暴力'（B326）。",
   "南方哥特（Southern gothic——B326 流派标注）。",
   "'没落'人物与心理脆弱性（B326：declassed / mental ruin）。"],
  "Britannica 定位威廉斯为美国剧作家，两度普利策奖得主，流派 Southern gothic（B326）。",
  "B326",
  ["1947年首演剧场（Ethel Barrymore Theatre说）待核。","斯坦利/斯黛拉人名核对（B326正文仅载布兰奇）。","1951年电影改编（马龙·白兰度）待核。"]),
A("jbaldwin", "詹姆斯·鲍德温", "James Baldwin（詹姆斯·鲍德温，1924-08-02—1987-12-01）", "美国", 1924, 1987, 1924, 1987, "现当代",
  "鲍德温，纽约生，美国作家与散文家。Go Tell It on the Mountain (1953)——'semiautobiographical first and finest novel'（半自传性的第一部也是最优秀的长篇——B327），取材其少年讲道岁月——'Those three years in the pulpit…that is what turned me into a writer.'（B327）。Giovanni's Room (1956) 被 Knopf 以同性恋题材为由退稿，后由 Dial Press 接受（B327）。散文集 Notes of a Native Son (1955)、The Fire Next Time (1963)（B327）。",
  [{"year": 1924, "text": "8月2日生于纽约（B327）。", "src": "B327"},
   {"year": 1953, "text": "Go Tell It on the Mountain——半自传性首作（B327）。", "src": "B327"},
   {"year": 1956, "text": "Giovanni's Room——Knopf退稿后Dial Press接受（B327）。", "src": "B327"},
   {"year": 1963, "text": "The Fire Next Time——民权运动语境散文（B327）。", "src": "B327"},
   {"year": 1987, "text": "12月1日卒于法国Saint-Paul de Vence（B327）。", "src": "B327"}],
  [{"work_id": "xiangtianhuhan", "note": "1953（B327）"},
   {"title": "乔瓦尼的房间", "note": "（B327：Giovanni's Room, 1956）"},
   {"title": "下一次将是烈火", "note": "（B327：The Fire Next Time, 1963）"}],
  ["讲道岁月的语言节奏（B327 语境）。",
   "种族、宗教与性向的交织书写（B327 语境）。",
   "散文的公共声音（B327：essays）。"],
  "Britannica 定位鲍德温为美国作家；Giovanni's Room 因题材被Knopf退稿（B327）。",
  "B327",
  ["约翰/加布里埃尔等人物名核对（B327正文未载）。","1953年出版（Knopf说）待核。","'民权活动家'定位补充来源待核。"]),
A("mccarthy", "科马克·麦卡锡", "Cormac McCarthy（科马克·麦卡锡，1933-07-20—2023-06-13）", "美国", 1933, 2023, 1933, 2023, "现当代",
  "麦卡锡，罗得岛州普罗维登斯生，美国小说家。Blood Meridian (1985)——'a violent frontier tale loosely based on historical events'（B328）——'a critical sensation, hailed as his masterpiece'（B328）——写14岁少年加入1840年代美墨边境无法无天的剥头皮团伙，头目'the judge'（B328）。首印不足1500册（B328）。All the Pretty Horses (1992) 获 National Book Award（B328）；The Road (2006) 获2007年普利策奖（B328）。1981年获 MacArthur fellowship（B328）。",
  [{"year": 1933, "text": "7月20日生于罗得岛州普罗维登斯（B328）。", "src": "B328"},
   {"year": 1981, "text": "获 MacArthur fellowship（B328）。", "src": "B328"},
   {"year": 1985, "text": "Blood Meridian——'hailed as his masterpiece'，首印不足1500册（B328）。", "src": "B328"},
   {"year": 1992, "text": "All the Pretty Horses——National Book Award（B328）。", "src": "B328"},
   {"year": 2007, "text": "The Road 获普利策奖（B328）。", "src": "B328"},
   {"year": 2023, "text": "6月13日卒于新墨西哥州Santa Fe（B328）。", "src": "B328"}],
  [{"work_id": "xueseziwuxian", "note": "1985（B328）"},
   {"title": "所有漂亮的马", "note": "（B328：All the Pretty Horses, 1992——中译名待核）"},
   {"title": "路", "note": "（B328：The Road, 2006——2007普利策奖）"}],
  ["暴力的哲学化书写（B328 语境）。",
   "西部神话的改写（B328：Border Trilogy——rewrote and challenged myths of the American West）。",
   "极简标点与古语词汇（通说待核）。"],
  "Britannica 定位麦卡锡为美国小说家；Blood Meridian 被誉为其杰作、Bloom 称'终极西部小说'（B328）。",
  "B328",
  ["少年'the kid'人名核对（B328只称'a 14-year-old boy'）。","法官 Judge Holden 全名待核。","1985年出版（Random House说）待核。","极简标点风格说法待核（B328未载）。"]),
A("aoz", "阿摩司·奥兹", "Amos Oz（阿摩司·奥兹，原名 Amos Klausner，1939-05-04—2018-12-28）", "以色列", 1939, 2018, 1939, 2018, "现当代",
  "奥兹，原名 Amos Klausner，耶路撒冷生，以色列小说家、短篇与散文作家——'in whose works Israeli society is unapologetically scrutinized'（以色列社会在他的作品中被毫不留情地审视——B329）。回忆录 Sipur ʿal ahavah ve-ḥoshekh（爱与黑暗的故事, 2002）——'drew wide critical acclaim'（B329）。1967年六日战争后投身以色列和平运动（B329）——'Oz felt himself unable to share the optimistic outlook and ideological certainties of Israel's founding generation'（B329）。Judas (2014) 获2015年 Internationaler Literaturpreis（B329）。",
  [{"year": 1939, "text": "5月4日生于耶路撒冷（原名 Amos Klausner——B329）。", "src": "B329"},
   {"year": 1967, "text": "六日战争后投身以色列和平运动（B329）。", "src": "B329"},
   {"year": 2002, "text": "回忆录《爱与黑暗的故事》——'drew wide critical acclaim'（B329）。", "src": "B329"},
   {"year": 2015, "text": "Judas 获 Internationaler Literaturpreis（B329）。", "src": "B329"},
   {"year": 2018, "text": "12月28日卒（B329）。", "src": "B329"}],
  [{"work_id": "aiyuheandegushi", "note": "回忆录（B329：2002）"},
   {"title": "我的米海尔", "note": "（B329：My Michael, 1968）"},
   {"title": "犹大", "note": "（B329：Judas, 2014——2015国际文学奖）"}],
  ["以色列社会的'毫不留情的审视'（B329）。",
   "对建国一代乐观意识形态的疏离（B329）。",
   "个人史与国族史的互文（B329 回忆录语境）。"],
  "Britannica 定位奥兹为以色列小说家/短篇/散文作家；1967年后和平运动活跃人士（B329）。",
  "B329",
  ["卒地核对（Britannica 页未载卒地）。","母亲芳尼娅·克劳斯纳自杀细节待核（B329未载）。","2002年出版社（Keter说）待核。"]),
]
for a in authors:
    pathlib.Path(f"data/authors/{a['id']}.json").write_text(json.dumps(a, ensure_ascii=False, indent=2), encoding='utf-8')
    print('author', a['id'])

# ============ D. 新作品 ×5 ============
def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

def mk(id_, title, orig, region, era, ed, genre, gg, lang, aid, aname, yd, ys, bg, outline, chars, themes, inf, read, pend, rel, svg):
    return {"id":id_,"title":title,"original_title":orig,"region":region,"era":era,"era_detail":ed,
"genre":genre,"genre_group":gg,"language":lang,"author_id":aid,"author_name":aname,"year_display":yd,"year_sort":ys,
"background":bg,"outline":outline,"characters":chars,"themes":themes,"influence":inf,"reading":read,"pending":pend,
"sources":["B"+id_],"year_source":"B","author_source":"B","related_works":rel,"svg":svg}

works = []
def add(wid, sid, **kw):
    d = mk(kw['id'], kw['title'], kw['orig'], kw['region'], kw['era'], kw['ed'], kw['genre'], kw['gg'], kw['lang'],
           kw['aid'], kw['aname'], kw['yd'], kw['ys'], kw['bg'], kw['outline'], kw['chars'], kw['themes'],
           kw['inf'], kw['read'], kw['pend'], kw['rel'], kw['svg'])
    d['sources'] = [sid]; d['year_source'] = sid; d['author_source'] = sid
    works.append(d)

add(None, "B325",
 id="tuixiaoyuanzhisi", title="推销员之死", orig="Death of a Salesman", region="美国", era="现当代", ed="20世纪40年代",
 genre="戏剧（两幕）", gg="戏剧", lang="英语", aid="amiller", aname="阿瑟·米勒",
 yd="1949年（Britannica B325：Death of a Salesman (1949)——'won a Tony Award for best play and a Pulitzer Prize for drama'）", ys=1949,
 bg=["Britannica（B325）：Death of a Salesman——'one of the most famous American plays of its period'（其时代最著名的美国剧作之一）。","Britannica（B325）：'the tragedy of Willy Loman, a man destroyed by false values that are in large part the values of his society'——威利·洛曼的悲剧：一个被'错误价值'毁掉的人，而这些价值大部分正是他的社会所奉行的。","米勒把'普通人'置于悲剧中心（B325：Miller believed in placing 'the common man' at the center of tragedy）。"],
 outline=["推销员威利·洛曼的最后一日与一生闪回：他被自己与社会共同奉行的'错误价值'所毁（B325：destroyed by false values that are in large part the values of his society）。","剧终的死亡细节（自杀说——通说待核，B325未载）。"],
 chars=[{"name":"威利·洛曼（Willy Loman）","identity":"推销员","note":"B325 点名主角"},{"name":"比夫（Biff）","identity":"长子","note":"（通说待核，B325未载）"},{"name":"琳达（Linda）","identity":"妻子","note":"（通说待核，B325未载）"}],
 themes=["'错误价值'的社会批判：美国梦的幻灭（B325 语境——false values that are... values of his society）。","普通人作为悲剧主角（B325：'In fact, it is the common man who knows this fear best.'）。","时间线与闪回的心理剧结构（通说待核）。"],
 inf=[{"text":"Britannica：'one of the most famous American plays of its period'（B325）。","source":"B325"},
      {"text":"Britannica：获Tony奖最佳剧作与普利策戏剧奖（B325）。","source":"B325"}],
 read={"difficulties":["现实、回忆与幻想交织的时间线。","美国梦与推销员职业的时代语境。"],
   "editions":["《推销员之死》中译本（人民文学/上海译文等版本——通说待核）。","英文原版（公有领域状态待核）。"],
   "order":"米勒首选；可与《炼狱》（1953）对读。"},
 pend=["1949年2月首演剧场（Morosco Theatre说）与日期待核（B325未载）。","威利·洛曼自杀结局、比夫/哈皮/琳达人名核对。","1951年电影改编待核。"],
 rel=["leiyu","manchangdeheian","yingtaoyuan"],
 svg=G("《推销员之死》幻灭结构图",[{"title":"威利·洛曼","text":"被'错误价值'毁掉的人（B325）","color":"main"},{"title":"美国梦","text":"社会共奉的价值","color":"antagonist"},{"title":"普通人","text":"悲剧的中心（B325）","color":"gold"},{"title":"闪回","text":"一生与最后一日","color":"family"}]))

add(None, "B326",
 id="yuwanghaojieche", title="欲望号街车", orig="A Streetcar Named Desire", region="美国", era="现当代", ed="20世纪40年代",
 genre="戏剧", gg="戏剧", lang="英语", aid="twilliams", aname="田纳西·威廉斯",
 yd="1947年（Britannica B326：A Streetcar Named Desire (1947)——获普利策戏剧奖）", ys=1947,
 bg=["Britannica（B326）：'It is a study of the mental and moral ruin of Blanche DuBois, another former Southern belle.'——本剧是对布兰奇·杜波依斯——另一位没落南方佳丽——精神与道德毁灭的研究。","Britannica（B326）：威廉斯的戏剧'揭示了一个人类挫折的世界，在浪漫的门面之下暗涌着性与暴力'（whose plays reveal a world of human frustration in which sex and violence underlie an atmosphere of romantic gentility）。","作者页（B326）：威廉斯两度普利策奖（1947本剧、1955《热铁皮屋顶上的猫》），流派 Southern gothic。"],
 outline=["没落南方佳丽布兰奇投奔妹妹——与妹夫斯坦利的冲突步步升级，终于精神与道德的双重毁灭（B326：a study of the mental and moral ruin of Blanche DuBois；新奥尔良场景与冲突细节通说待核）。","结局：布兰奇被送走（'送走'细节通说待核）。"],
 chars=[{"name":"布兰奇·杜波依斯（Blanche DuBois）","identity":"没落南方佳丽","note":"B326 点名主角"},{"name":"斯坦利（Stanley）","identity":"妹夫","note":"（通说待核，B326正文未载全名）"},{"name":"斯黛拉（Stella）","identity":"妹妹","note":"（通说待核，B326未载）"}],
 themes=["精神与道德的毁灭（B326：mental and moral ruin）。","浪漫门面之下的性与暴力（B326：sex and violence underlie an atmosphere of romantic gentility）。","旧南方的没落与'南方哥特'（B326：former Southern belle；Southern gothic）。"],
 inf=[{"text":"Britannica：A Streetcar Named Desire (1947) 获普利策戏剧奖（B326）。","source":"B326"},
      {"text":"Britannica：'His works won four Drama Critics' awards and were widely translated and performed around the world.'（B326）。","source":"B326"}],
 read={"difficulties":["'欲望''公墓'等站名的象征体系（通说待核）。","南方没落贵族与新移民工业城市的阶级冲突（通说待核）。"],
   "editions":["《欲望号街车》中译本（人民文学/上海译文等——通说待核）。","英文原版。"],
   "order":"威廉斯首选；可与《玻璃动物园》（1944）对读。"},
 pend=["1947年首演剧场（Ethel Barrymore Theatre说）待核。","斯坦利·科瓦尔斯基/斯黛拉人名核对。","1951年电影改编（马龙·白兰度）待核。","'欲望号/公墓号'街车象征细节待核。"],
 rel=["leiyu","manchangdeheian","xinshigudeLieshou"],
 svg=G("《欲望号街车》毁灭结构图",[{"title":"布兰奇","text":"精神与道德的毁灭（B326）","color":"main"},{"title":"斯坦利","text":"新世界的暴力（通说）","color":"antagonist"},{"title":"欲望号街车","text":"浪漫门面之下的暗涌（B326）","color":"gold"},{"title":"旧南方","text":"没落的佳丽","color":"family"}]))

add(None, "B327",
 id="xiangtianhuhan", title="向苍天呼吁", orig="Go Tell It on the Mountain", region="美国", era="现当代", ed="20世纪50年代",
 genre="长篇小说", gg="小说", lang="英语", aid="jbaldwin", aname="詹姆斯·鲍德温",
 yd="1953年（Britannica B327：Go Tell It on the Mountain (1953)——'semiautobiographical first and finest novel'）", ys=1953,
 bg=["Britannica（B327）：Go Tell It on the Mountain——鲍德温'semiautobiographical first and finest novel'（半自传性的第一部也是最优秀的长篇）。","Britannica（B327）：小说取材鲍德温少年时期的讲道岁月——'Those three years in the pulpit…that is what turned me into a writer.'（正是讲坛上的那三年把我变成了作家）。","题材（通说待核）：哈莱姆黑人少年约翰一日一夜间的宗教觉醒与家族史闪回。"],
 outline=["少年约翰一日一夜的宗教觉醒与格里格斯家族三代人的罪与救赎（家族结构通说待核——B327未载人物名）。","父亲加布里埃尔的过往与约翰的身份追问（通说待核）。"],
 chars=[{"name":"约翰（John）","identity":"少年","note":"（通说待核，B327未载人名）"},{"name":"加布里埃尔（Gabriel）","identity":"父亲","note":"（通说待核，B327未载）"}],
 themes=["宗教觉醒：讲坛岁月的书写（B327：draws on his years as a teenage preacher）。","黑人家庭三代与身份追问（通说待核）。","写作的起点——'讲坛上的那三年把我变成了作家'（B327）。"],
 inf=[{"text":"Britannica：'semiautobiographical first and finest novel'（B327）。","source":"B327"},
      {"text":"Britannica：鲍德温散文 The Fire Next Time (1963) 处于民权运动语境（B327 作品列表）。","source":"B327"}],
 read={"difficulties":["哈莱姆黑人教会语境与非裔大迁徙背景（通说待核）。","宗教语言与黑人灵歌传统（通说待核）。"],
   "editions":["《向苍天呼吁》中译本（人民文学/译林等——通说待核）。","英文原版。"],
   "order":"鲍德温首选；可与《看不见的人》（1952）对读。"},
 pend=["约翰·格里姆斯/加布里埃尔/伊丽莎白人名核对（B327未载）。","1953年出版（Knopf说）待核。","'一日一夜'结构说法待核。"],
 rel=["kanbujian3","tuyuzhizideneizi","zise"],
 svg=G("《向苍天呼吁》觉醒结构图",[{"title":"约翰","text":"一日一夜的觉醒（通说）","color":"main"},{"title":"讲坛","text":"'把我变成了作家'（B327）","color":"gold"},{"title":"加布里埃尔","text":"父亲的罪（通说）","color":"antagonist"},{"title":"哈莱姆","text":"家族三代（通说）","color":"family"}]))

add(None, "B328",
 id="xueseziwuxian", title="血色子午线", orig="Blood Meridian", region="美国", era="现当代", ed="20世纪80年代",
 genre="长篇小说", gg="小说", lang="英语", aid="mccarthy", aname="科马克·麦卡锡",
 yd="1985年（Britannica B328：Blood Meridian (1985)——'a critical sensation, hailed as his masterpiece'）", ys=1985,
 bg=["Britannica（B328）：Blood Meridian——'a violent frontier tale loosely based on historical events'（一部松散取材于史实的暴力边境故事）——'a critical sensation, hailed as his masterpiece'（评论界的轰动，被誉为其杰作）。","Britannica（B328）：小说写一个14岁少年加入1840年代美墨边境'无法无天的剥头皮团伙'，头目为'the judge'（法官）。","Britannica（B328）：首印不足1500册；Harold Bloom 称之为'the ultimate Western, not to be surpassed'（终极西部小说，不可超越）。"],
 outline=["14岁少年沿美墨边境加入剥头皮团伙的远征（B328：a 14-year-old boy joining a gang of lawless scalp hunters along the U.S.-Mexico border in the 1840s）。","'法官'作为暴力哲学的化身——对暴力的辩护与少年的挣扎（哲学化阐释通说待核；'the judge'为B328所载）。"],
 chars=[{"name":"少年（the kid）","identity":"14岁少年","note":"B328：'a 14-year-old boy'（人名the kid通说待核）"},{"name":"法官（the judge）","identity":"团伙头目","note":"B328：'the judge'（全名Judge Holden通说待核）"}],
 themes=["暴力与生命：'There's no such thing as life without bloodshed.'（B328 引文）。","西部神话的改写（B328 作者语境：Border Trilogy——rewrote and challenged myths of the American West）。","文明的边界与'恶'的化身——法官（通说待核）。"],
 inf=[{"text":"Britannica：'a critical sensation, hailed as his masterpiece'（B328）。","source":"B328"},
      {"text":"Britannica：Harold Bloom——'the ultimate Western, not to be surpassed'（B328）。","source":"B328"}],
 read={"difficulties":["暴力描写的强度与古语词汇（风格通说待核）。","1840年代美墨边境史（墨西哥战争、剥头皮贸易——通说待核）。"],
   "editions":["《血色子午线》中译本（上海译文等——通说待核）。","英文原版。"],
   "order":"麦卡锡代表作；先读可后接《所有漂亮的马》（1992）。"},
 pend=["少年'the kid'人名、法官 Judge Holden 全名核对（B328只称'the judge'）。","1985年出版（Random House说）待核。","'首印不足1500册'细节仅B328所载。","极简标点风格说法待核（B328未载）。"],
 rel=["tuyuzhizideneizi","kanbujian3","xinshigudeLieshou"],
 svg=G("《血色子午线》暴力结构图",[{"title":"少年","text":"14岁加入远征（B328）","color":"main"},{"title":"法官","text":"暴力的化身（B328）","color":"antagonist"},{"title":"剥头皮团伙","text":"1840年代边境（B328）","color":"family"},{"title":"血色子午线","text":"'终极西部小说'（B328）","color":"gold"}]))

add(None, "B329",
 id="aiyuheandegushi", title="爱与黑暗的故事", orig="Sipur ʿal ahavah ve-ḥoshekh（A Tale of Love and Darkness）", region="以色列", era="现当代", ed="21世纪初",
 genre="回忆录", gg="散文", lang="希伯来语", aid="aoz", aname="阿摩司·奥兹",
 yd="2002年（Britannica B329：Sipur ʿal ahavah ve-ḥoshekh (2002)——'drew wide critical acclaim'）", ys=2002,
 bg=["Britannica（B329）：回忆录《爱与黑暗的故事》(2002)——'drew wide critical acclaim'（获得评论界广泛赞誉）。","Britannica（B329）：奥兹——'an Israeli novelist, short-story writer, and essayist in whose works Israeli society is unapologetically scrutinized'（以色列社会在他的作品中被毫不留情地审视）。","Britannica（B329）：'Oz felt himself unable to share the optimistic outlook and ideological certainties of Israel's founding generation'——奥兹自觉无法分享以色列建国一代的乐观与意识形态确定性。"],
 outline=["耶路撒冷童年的家庭记忆与母亲之死（母亲自杀细节通说待核——B329未载）。","个人成长与以色列建国史的互文：建国一代的意识形态与作者的疏离（B329 引文）。"],
 chars=[{"name":"奥兹（Amos Klausner）","identity":"作者/叙述者","note":"B329：memoir 自传体"},{"name":"母亲","identity":"回忆录核心人物","note":"（通说待核：芳尼娅·克劳斯纳——B329未载）"}],
 themes=["以色列社会的'毫不留情的审视'（B329：unapologetically scrutinized）。","建国一代的乐观与作者的自我疏离（B329 引文）。","爱与黑暗：家庭创伤与国族叙事的交织（通说待核）。"],
 inf=[{"text":"Britannica：回忆录'drew wide critical acclaim'（B329）。","source":"B329"},
      {"text":"Britannica：Judas (2014) 获2015年 Internationaler Literaturpreis（B329）。","source":"B329"}],
 read={"difficulties":["以色列建国史与耶路撒冷分治背景（通说待核）。","希伯来文学的家族记忆传统（通说待核）。"],
   "editions":["《爱与黑暗的故事》中译本（译林出版社——通说待核）。","希伯来文原版。"],
   "order":"奥兹首选；可后接《犹大》（2014）。"},
 pend=["母亲芳尼娅·克劳斯纳自杀细节核对（B329未载）。","2002年出版（Keter说）待核。","2015年电影改编（娜塔莉·波特曼执导说）待核。","卒地待核（B329页未载）。"],
 rel=["renshijian","ezhihua","huoluan"],
 svg=G("《爱与黑暗的故事》互文结构图",[{"title":"耶路撒冷","text":"童年的城（通说）","color":"family"},{"title":"母亲","text":"爱与黑暗的核心（通说）","color":"antagonist"},{"title":"建国一代","text":"'无法分享的乐观'（B329）","color":"main"},{"title":"审视","text":"'毫不留情'（B329）","color":"gold"}]))

for d in works:
    pathlib.Path(f"data/works/{d['id']}.json").write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', d['id'])
print('BATCH22 DONE')
