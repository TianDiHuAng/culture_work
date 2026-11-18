# -*- coding: utf-8 -*-
"""追加5条Britannica来源并重建sources.json"""
import json, pathlib

new = [
{"id":"B201","title":"Anna Karenina (novel by Tolstoy) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Anna-Karenina-novel","type":"百科全书","verified":True,"covers":["annakaleni","tolstoy"],"note":"2026-11-19 核对：1875—1877年连载；considered one of the pinnacles of world literature；情节句与题词引文均摘自该页"},
{"id":"B202","title":"The Brothers Karamazov (novel by Dostoyevsky) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica (revised by Kathleen Kuiper)","year":"持续更新","url":"https://www.britannica.com/topic/The-Brothers-Karamazov","type":"百科全书","verified":True,"covers":["kalamasuofu","dostoevsky"],"note":"2026-11-19 核对：1879—80年；search for faith, for God—the central idea of the work；generally regarded as Dostoyevsky's masterpiece"},
{"id":"B203","title":"George Orwell — Animal Farm and Nineteen Eighty-four — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/George-Orwell/Animal-Farm-and-Nineteen-Eighty-four","type":"百科全书","verified":True,"covers":["dongwunongchang","orwell"],"note":"2026-11-19 核对：In 1944 Orwell finished writing Animal Farm；appeared in August 1945；All animals are equal, but some animals are more equal than others."},
{"id":"B204","title":"Great Expectations (novel by Dickens) — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica (revised by Adam Augustyn)","year":"持续更新","url":"https://www.britannica.com/topic/Great-Expectations-novel-by-Dickens","type":"百科全书","verified":True,"covers":["yuandaqiancheng","dickens"],"note":"2026-11-19 核对：1860—61年连载、1861年成书；a search for true identity；萧伯纳评 most compactly perfect book"},
{"id":"B205","title":"Never Let Me Go (novel by Ishiguro) — Encyclopaedia Britannica","author":"The Information Architects of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Never-Let-Me-Go-by-Ishiguro","type":"百科全书","verified":True,"covers":["bielmerangzou","ishiguro"],"note":"2026-11-19 核对：2005年出版；human clones are created to serve as organ donors for non-clones；克隆故事警示基因工程伦理"},
]

raw_path = pathlib.Path("_sources_raw.jsonl")
with raw_path.open("a", encoding="utf-8") as f:
    for s in new:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")

raw = [json.loads(l) for l in raw_path.read_text(encoding="utf-8").splitlines() if l.strip()]
seen = {}
for s in raw:
    seen[s["id"]] = s
out = [seen[k] for k in sorted(seen)]
pathlib.Path("sources.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("sources.json rebuilt:", len(out))
