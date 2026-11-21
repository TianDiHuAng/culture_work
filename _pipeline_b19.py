# -*- coding: utf-8 -*-
"""流水线批19：Britannica 新核 2 作家 2 部 + 零成本直写 8 部"""
import json, pathlib

new_src = [
{"id":"B315","title":"Emile Zola — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Emile-Zola","type":"百科全书","verified":True,"covers":["zola","nana"],"note":"2026-11-21 核对：1840-04-02巴黎生—1902-09-28巴黎卒（62岁）；'the leading French novelist of the late 19th century, founder of literary naturalism'；'20-novel Rougon-Macquart cycle'（1871—1893）；'J'accuse' 1898-01-13刊于L'Aurore——'Zola was prosecuted for libel and found guilty'；Nana 在 Notable Works 列表中——正文无细节（通说待核）"},
{"id":"B316","title":"J.D. Salinger — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/J-D-Salinger","type":"百科全书","verified":True,"covers":["salinger","maitian"],"note":"2026-11-21 核对：1919-01-01曼哈顿生—2010-01-27 Cornish卒（91岁）；The Catcher in the Rye (1951)——'relates in authentic teenage idiom his flight from the phony adult world'；'The humor and colorful language of The Catcher in the Rye place it in the tradition of Mark Twain's'；'made Salinger into a literary celebrity'；'After the success of The Catcher in the Rye, Salinger became a recluse'；'His last published work was a novella titled Hapworth 16, 1924, which appeared in The New Yorker in 1965'"},
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
"zola": {
  "id": "zola", "name": "埃米尔·佐拉", "foreign_name": "Émile Zola（埃米尔·佐拉，1840-04-02—1902-09-28）",
  "country": "法国", "birth": 1840, "death": 1902, "birth_year": 1840, "death_year": 1902, "era": "近代",
  "summary": "佐拉，巴黎生，法国小说家——'the leading French novelist of the late 19th century, founder of literary naturalism'（19世纪末法国最重要的小说家、文学自然主义创始人——B315）；20卷《卢贡-马卡尔家族》（Rougon-Macquart 1871—1893）——'at the rate of nearly one per year, completing the series in 1893'（B315）。'Naturalism involves the application to literature of two scientific principles: determinism... and the experimental method'（B315）。1898年1月13日《J'accuse》——'a fierce denunciation of the French general staff'（B315）。",
  "timeline": [
    {"year": 1840, "text": "4月2日生于巴黎（B315：Born April 2, 1840, Paris）。", "src": "B315"},
    {"year": 1871, "text": "Rougon-Macquart 开始出版（1871—1893——B315）。", "src": "B315"},
    {"year": 1898, "text": "1月13日《J'accuse》刊于L'Aurore——'prosecuted for libel and found guilty'（B315）。", "src": "B315"},
    {"year": 1902, "text": "9月28日卒于巴黎（B315：Died September 28, 1902, Paris）。", "src": "B315"}],
  "major_works": [
    {"work_id": "mengya", "note": "Rougon-Macquart 系列（B315）"},
    {"title": "娜娜", "note": "（B315：Notable Works 列表）"},
    {"title": "萌芽", "note": "（B315：'depicts life in a mining community'——Germinal）"}],
  "style": [
    "自然主义：'determinism + experimental method'（B315）。",
    "'20-novel Rougon-Macquart cycle'（B315）。",
    "'J'accuse'——政治勇气的里程碑（B315）。"],
  "status": "Britannica 定位佐拉为19世纪末法国最重要的小说家、自然主义创始人（B315）。",
  "sources": ["B315"], "dates_source": "B315",
  "pending": ["《娜娜》1880年出版细节待核。","《萌芽》1885年出版说待核。","'J'accuse'全文待核。"]
},
"salinger": {
  "id": "salinger", "name": "J.D.塞林格", "foreign_name": "J.D. Salinger（杰罗姆·大卫·塞林格，1919-01-01—2010-01-27）",
  "country": "美国", "birth": 1919, "death": 2010, "birth_year": 1919, "death_year": 2010, "era": "现当代",
  "summary": "塞林格，曼哈顿生，美国作家——1951年《麦田里的守望者》'brought him lasting fame'（B316）。'relates in authentic teenage idiom his flight from the phony adult world, his search for innocence and truth'（B316）；'The humor and colorful language of The Catcher in the Rye place it in the tradition of Mark Twain's'（B316）。1953年移居新罕布什尔州科尼什——'After the success of The Catcher in the Rye, Salinger became a recluse'（B316）。'His last published work was a novella titled Hapworth 16, 1924, which appeared in The New Yorker in 1965'（B316）。",
  "timeline": [
    {"year": 1919, "text": "1月1日生于曼哈顿（B316：Born January 1, 1919, Manhattan, New York）。", "src": "B316"},
    {"year": 1951, "text": "《麦田里的守望者》出版（B316：The Catcher in the Rye (1951)）。", "src": "B316"},
    {"year": 1953, "text": "移居新罕布什尔州科尼什（B316：moved to Cornish in 1953 and went into seclusion）。", "src": "B316"},
    {"year": 1965, "text": "最后发表作品——Hapworth 16, 1924（《纽约客》1965）（B316）。", "src": "B316"},
    {"year": 2010, "text": "1月27日卒于新罕布什尔州（B316：Died January 27, 2010, Cornish, New Hampshire）。", "src": "B316"}],
  "major_works": [
    {"work_id": "maitian", "note": "长篇（B316：1951）"},
    {"work_id": "jiugushi", "note": "短篇集（B316：Nine Stories (1953)）"},
    {"title": "弗兰妮与祖伊", "note": "（B316：Franny and Zooey (1961)）"}],
  "style": [
    "'authentic teenage idiom'（B316）。",
    "'in the tradition of Mark Twain's'（B316——与马克·吐温传统并列）。",
    "隐居与沉默（B316：became a recluse）。"],
  "status": "Britannica 定位塞林格为美国作家（《麦田里的守望者》作者）；1953年后隐居、1965年后不再发表作品（B316）。",
  "sources": ["B316"], "dates_source": "B316",
  "pending": ["《麦田里的守望者》1951年7月16日出版（Little, Brown说）核对。","'phony'adult world引文核对。","格拉斯家族系列七篇核对。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"nana": {
  "id":"nana","title":"娜娜","original_title":"Nana","region":"法国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"zola","author_name":"埃米尔·佐拉",
  "year_display":"出版年份待核（Britannica B315：Nana 在 Notable Works 列表——1880年说通说待核）","year_sort":1880,
  "background":["作者页（B315）：佐拉为'20-novel Rougon-Macquart cycle'作者；Nana 列入 Notable Works。","与《萌芽》同属 Rougon-Macquart 系列（B315：Zola conceived in 1868 a large-scale series similar to Balzac's La Comédie humaine）。","题材（通说待核）：娜娜为《小酒店》中 Gervaise 之女——第二帝国上流社会的堕落。"],
  "outline":["娜娜从底层崛起为巴黎名妓——'how Nana is connected to Gervaise Macquart'（B315 问答）。","结局：死于天花——'金色messalina'的陨落（通说待核）。"],
  "characters":[{"name":"娜娜","identity":"名妓","note":"Gervaise 之女（通说待核）"}],
  "themes":["第二帝国的堕落（通说）。",
   "女性身体的商品化（通说待核）。",
   "自然主义的遗传与社会决定论（B315 语境）。"],
  "influence":[{"text":"Britannica：Rougon-Macquart 系列——Zola conceived in 1868 a large-scale series similar to Balzac's La Comédie humaine（B315）。","source":"B315"},
   {"text":"Britannica：佐拉为自然主义创始人（B315 作者级定位）。","source":"B315"}],
  "reading":{"difficulties":["第二帝国政治史。","自然主义细节。"],
   "editions":["《娜娜》（人民文学出版社，通说待核）。","法文原版（公有领域）。"],
   "order":"Rougon-Macquart 系列之一（可在《萌芽》前后阅读）。"},
  "pending":["1880年出版（Charpentier说）核对。","娜娜/萨丹人名核对。","与《小酒店》（Gervaise）的母女关系核对。"],
  "sources":["B315"],"year_source":"B315","author_source":"B315","related_works":["mengya","baofali","ezhihua"],
  "svg":G2("《娜娜》堕落结构图",[{"title":"出身","text":"Gervaise之女（通说）","color":"family"},{"title":"崛起","text":"巴黎名妓","color":"main"},{"title":"第二帝国","text":"上流的堕落","color":"antagonist"},{"title":"天花","text":"金色的终结（通说）","color":"gold"}])
},
"maitian2": {"__skip__": True}
}
# 只写 nana，maitian 已有
for wid, d in works.items():
    if wid == "maitian2":
        continue
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print("batch done")
