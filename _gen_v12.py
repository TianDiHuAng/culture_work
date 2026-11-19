# -*- coding: utf-8 -*-
"""v12：安妮日记 + 1来源"""
import json, pathlib

new_src = [
{"id":"B271","title":"Anne Frank — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Anne-Frank","type":"百科全书","verified":True,"covers":["annefrank","anniriji"],"note":"2026-11-20 核对：1929-06-12法兰克福生—1945年2/3月贝尔根-贝尔森集中营卒（15岁，伤寒）；'On June 12, 1942, she received a red-and-white plaid diary for her 13th birthday'；'the Franks went into hiding on July 6, 1942, in the backroom office and warehouse'；藏匿者8人（范丹夫妇与彼得、弗利茨·费佛等）；最后一篇1944-08-01；'published as Anne Frank: The Diary of a Young Girl (originally in Dutch, 1947)'；'became a classic of war literature, personalizing the Holocaust'；'translated into more than 65 languages……the most widely read diary of the Holocaust'；名句'I still believe, in spite of everything, that people are really good at heart.'"},
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
"annefrank": {
  "id": "annefrank", "name": "安妮·弗兰克", "foreign_name": "Anne Frank（安妮·弗兰克，1929-06-12—1945年2/3月）",
  "country": "荷兰", "birth": 1929, "death": 1945, "birth_year": 1929, "death_year": 1945, "era": "现当代",
  "summary": "安妮·弗兰克，法兰克福出生的犹太少女——'a Jewish teenager whose diary of her family's two years spent in hiding from the Nazis in Amsterdam became one of the most famous accounts of the Holocaust'（其日记成为纳粹大屠杀最著名的记录之一——Britannica）。1942年6月12日13岁生日收到红白格子日记本（B271）；7月6日全家藏匿于阿姆斯特丹'后屋'（B271）；藏匿者共8人（B271）；最后一篇日记写于1944年8月1日（B271）；1945年2/3月死于贝尔根-贝尔森集中营（伤寒——B271）。日记由父亲奥托保存并出版（B271 语境）。",
  "timeline": [
    {"year": 1929, "text": "6月12日生于法兰克福（Britannica：Born June 12, 1929, Frankfurt am Main）。", "src": "B271"},
    {"year": 1942, "text": "6月12日获赠日记本；7月6日全家藏匿（B271）。", "src": "B271"},
    {"year": 1944, "text": "8月1日写下最后一篇日记（B271）。", "src": "B271"},
    {"year": 1945, "text": "2/3月死于贝尔根-贝尔森（伤寒）（B271）。", "src": "B271"},
    {"year": 1947, "text": "日记以《安妮日记》出版（荷兰文）（B271：originally in Dutch, 1947）。", "src": "B271"}],
  "major_works": [
    {"work_id": "anniriji", "note": "日记（Britannica：1947）"}],
  "style": [
    "'classic of war literature, personalizing the Holocaust'（B271：使大屠杀个人化）。",
    "少女视角的日常与深刻并置（B271 语境）。",
    "对人性之善的坚持（B271 名句：'I still believe, in spite of everything, that people are really good at heart.'）。"],
  "status": "Britannica 定位安妮为大屠杀受害者中最广为人知者（probably the best known of Holocaust victims——B271）；其日记为大屠杀文献中被阅读最广者（B271）。",
  "sources": ["B271"], "dates_source": "B271",
  "pending": ["'密室'（Secret Annex）名称与普林森格拉赫特街263号地址待核。", "日记版本史（A/B版与'Definitive Edition'）待核。", "出卖者之谜（学界新说）待核。"]
}
}

for aid, d in authors.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created author", aid)

works = {
"anniriji": {
  "id":"anniriji","title":"安妮日记","original_title":"Het Achterhuis（The Diary of a Young Girl）","region":"荷兰","era":"现当代","era_detail":"20世纪",
  "genre":"日记","genre_group":"散文","language":"荷兰语","author_id":"annefrank","author_name":"安妮·弗兰克",
  "year_display":"1947年荷兰文初版（Britannica：originally in Dutch, 1947）","year_sort":1947,
  "background":["Britannica（B271）：'On June 12, 1942, she received a red-and-white plaid diary for her 13th birthday'；'the Franks went into hiding on July 6, 1942, in the backroom office and warehouse'——与范丹一家三口及费佛共8人藏于'后屋'。","地位（B271）：'became a classic of war literature, personalizing the Holocaust'；'translated into more than 65 languages……the most widely read diary of the Holocaust'。"],
  "outline":["1942—1944年的密室日记：成长、初恋（彼得）、恐惧与希望（通说）。","名句：'I still believe, in spite of everything, that people are really good at heart.'（'尽管这一切，我仍然相信人心本善'——B271 引用；中译为本库试译）。"],
  "characters":[{"name":"安妮","identity":"日记作者","note":"13—15岁"},{"name":"彼得·范丹","identity":"藏匿少年","note":"初恋对象（通说待核）"}],
  "themes":["'使大屠杀个人化'（B271：personalizing the Holocaust）。",
   "密室中的成长（通说）。",
   "对人性之善的信念（B271 名句）。"],
  "influence":[{"text":"Britannica：'translated into more than 65 languages……the most widely read diary of the Holocaust'（B271）。","source":"B271"},
   {"text":"Britannica：'became a classic of war literature'（B271）。","source":"B271"}],
  "reading":{"difficulties":["日记体与编辑痕迹（B271 语境：父亲整理）。","大屠杀历史背景。"],
   "editions":["《安妮日记》（人民文学出版社/译林出版社版本，通说待核）。","英文版（公有领域渐近）。"],
   "order":"对照《古拉格群岛》《二手时间》：三种'个人记录'。"},
  "pending":["荷兰文书名 Het Achterhuis（'后屋'）核对。","日记三版本（A/B/C）细节待核。","密室地址（Prinsengracht 263）待核。"],
  "sources":["B271"],"year_source":"B271","author_source":"B271","related_works":["gulage","ershoushijian","fengzhonglvli"],
  "svg":{"type":"grid","width":680,"height":340,"caption":"《安妮日记》密室结构图",
    "cards":[{"title":"后屋","text":"两年的藏匿（B271）","color":"family"},{"title":"日记","text":"13岁生日礼物","color":"main"},{"title":"彼得","text":"初恋与希望","color":"gold"},{"title":"人心本善","text":"名句（B271）","color":"plain"}]}
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
