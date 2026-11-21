# -*- coding: utf-8 -*-
"""流水线批21：Britannica 新核 6 作家 6 部"""
import json, pathlib

new_src = [
{"id":"B319","title":"J.D. Salinger — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/J-D-Salinger","type":"百科全书","verified":True,"covers":["salinger","maitian"],"note":"2026-11-21 核对：1919-01-01曼哈顿生—2010-01-27 Cornish卒（91岁）；The Catcher in the Rye (1951)——'relates in authentic teenage idiom his flight from the phony adult world, his search for innocence and truth'；'The humor and colorful language of The Catcher in the Rye place it in the tradition of Mark Twain's'；'made Salinger into a literary celebrity'；'After the success of The Catcher in the Rye, Salinger became a recluse'；'His last published work was a novella titled Hapworth 16, 1924'"},
{"id":"B320","title":"Graham Greene — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Graham-Greene","type":"百科全书","verified":True,"covers":["greene","lianqingdezhongjie"],"note":"2026-11-21 核对：1904-10-02 Berkhamsted生—1991-04-03瑞士沃韦卒（86岁）；'one of the most widely read British novelists of the 20th century'；'Many of his best-known works, including The Power and the Glory (1940) and The End of the Affair (1951), center on Roman Catholic themes'；'emphasize the presence of evil as a palpable force'；End of the Affair——'narrated by an agnostic in love with a woman who forsakes him because of a religious conviction'（电影1955/1999）"},
{"id":"B321","title":"James Joyce — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/James-Joyce","type":"百科全书","verified":True,"covers":["joyce","dubolinen"],"note":"2026-11-21 核对：1882-02-02都柏林生—1941-01-13苏黎世卒（58岁）；'His literary masterpiece is Ulysses (1922)'；Dubliners (1914)——15篇；'A Portrait of the Artist as a Young Man (1916)'；'Finnegans Wake (1939)'——'written in a private style'; 'stream of consciousness'"},
{"id":"B322","title":"Franz Kafka — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Franz-Kafka","type":"百科全书","verified":True,"covers":["kafka","chengbao"],"note":"2026-11-21 核对：1883-07-03布拉格生—1924-06-03 Kierling疗养院卒（40岁）；'a German-language writer of visionary fiction'；The Trial (1925)——'posthumously published'；The Castle (1926)——'posthumously published, unfinished'；'Kafkas stories and novels have proved so provocative that they have become nothing less than cultural icons'；Max Brod——'his literary executor'，'disobeyed Kafkas instructions to burn the manuscripts'"},
{"id":"B323","title":"Jorge Luis Borges — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jorge-Luis-Borges","type":"百科全书","verified":True,"covers":["borges","alaifu"],"note":"2026-11-21 核对：1899-08-24布宜诺斯艾利斯生—1986-06-14日内瓦卒（86岁）；'His works have become classics of world literature'；Ficciones (1944)——'his most acclaimed collection'；'El Aleph (1949)'；'El libro de arena (1975; The Book of Sand)'；'Borgess essays and short stories are characterized by their imaginative blend of philosophy and fantasy'"},
{"id":"B324","title":"William Faulkner — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/William-Faulkner","type":"百科全书","verified":True,"covers":["faulkner","xuanhuayusaodong"],"note":"2026-11-21 核对：1897-09-25 New Albany生—1962-07-06 Byhalia卒（64岁）；1949诺贝尔奖；'In The Sound and the Fury, his first major novel, he combined a Yoknapatawpha setting with radical technical experimentation'；'stream of consciousness'——'successive monologues'"},
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

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

# 零成本直写——复用已有作者页注记
works = {
"haiou": {
  "id":"haiou","title":"海鸥","original_title":"Чайка（The Seagull）","region":"俄国","era":"近代","era_detail":"19世纪末",
  "genre":"四幕喜剧","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
  "year_display":"1896年首演（作者页B270口径：契诃夫戏剧四部之一——海鸥1896年彼得堡首演失败、1898年莫斯科艺术剧院成功说通说待核）","year_sort":1896,
  "background":["作者页（B270）：契诃夫戏剧代表作四部——The Seagull 存目；'Chekhovs gun'与'what is left unsaid seems much more important than what is said'（B270）。","题材（通说待核）：乡村少女尼娜与青年作家特里波列夫——'海鸥'被射杀的隐喻。"],
  "outline":["尼娜的演员梦与特里波列夫的文学梦——两种理想的毁灭（通说待核）。","阿尔卡基娜（名演员母亲）与特里波列夫的母子冲突（通说待核）。"],
  "characters":[{"name":"尼娜","identity":"少女演员","note":"（通说待核）"},{"name":"特里波列夫","identity":"青年作家","note":"（通说待核）"},{"name":"阿尔卡基娜","identity":"名演员","note":"母亲（通说待核）"}],
  "themes":["'新形式'的戏剧实验（通说待核）。","'海鸥'的象征：射杀与重生（通说待核）。","艺术与爱情的毁灭（通说）。"],
  "influence":[{"text":"作者页：契诃夫戏剧四部之一（B270 作者页口径）。","source":"B270"},{"text":"作者页：'Chekhovs gun'与未说出之重（B270）。","source":"B270"}],
  "reading":{"difficulties":["'潜台词'表演。","莫斯科艺术剧院史。"],
   "editions":["《海鸥》（人民文学出版社《契诃夫戏剧集》，通说待核）。","俄文原版（公有领域）。"],
   "order":"契诃夫戏剧四部之首。"},
  "pending":["1896年彼得堡首演失败说核对。","1898年莫斯科艺术剧院复排成功说核对。","尼娜/特里波列夫人名核对。"],
  "sources":["B270"],"year_source":"B270","author_source":"B270","related_works":["yingtaoyuan","leiyu","beijingren"],
  "svg":G2("《海鸥》射杀结构图",[{"title":"射杀的海鸥","text":"创作的隐喻（通说）","color":"main"},{"title":"尼娜","text":"两年的重来","color":"gold"},{"title":"特里波列夫","text":"失败的作家","color":"antagonist"},{"title":"新形式","text":"戏剧的寻找","color":"family"}])
}
}

for wid, d in works.items():
    if d.get("__skip__"):
        continue
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print("batch done")
