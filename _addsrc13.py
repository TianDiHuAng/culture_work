# -*- coding: utf-8 -*-
"""v4批次：追加13条已核实来源并重建sources.json"""
import json, pathlib

new = [
{"id":"B206","title":"Yu Dafu — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Yu-Dafu","type":"百科全书","verified":True,"covers":["yudafu","chenlun"],"note":"2026-11-19 核对：1896-12-07—1945-09-17；创造社创始成员；首部小说集 Chenlun (1921; Sinking)；'Chenlun became a popular success in China because of its frank treatment of sex'"},
{"id":"B207","title":"Guo Moruo — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Guo-Moruo","type":"百科全书","verified":True,"covers":["guomoruo","nvshen"],"note":"2026-11-19 核对：1892年11月生—1978-06-12卒；诗集 Nü shen (1921; Goddess)；'laid the first cornerstone for the development of new verse in China'"},
{"id":"B208","title":"Pai Hsien-yung — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Pai-Hsien-yung","type":"百科全书","verified":True,"covers":["baixianyung","taibeiren"],"note":"2026-11-19 核对：台湾现代主义文学领军人物；'author of Yu-yüan ching-meng (1982; Wandering in the Garden, Waking from a Dream), remained influential'；该页未载生卒年——1937年生为通说待核"},
{"id":"B209","title":"Thomas Mann — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Thomas-Mann","type":"百科全书","verified":True,"covers":["thomasmann","mosha"],"note":"2026-11-19 核对：1875-06-06—1955-08-12；1929诺贝尔奖；魔山主题句 'the sanatorium comes to be the spiritual reflection of the possibilities and dangers of the actual world'；布登勃洛克之家四代家族"},
{"id":"B210","title":"William Faulkner — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/William-Faulkner","type":"百科全书","verified":True,"covers":["faulkner","xuanhuayusaodong"],"note":"2026-11-19 核对：1897-09-25—1962-07-06；1949诺贝尔奖；'In The Sound and the Fury, his first major novel, he combined a Yoknapatawpha setting with radical technical experimentation'"},
{"id":"B211","title":"Dazai Osamu — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Dazai-Osamu","type":"百科全书","verified":True,"covers":["dazaiosamu","renjianshige"],"note":"2026-11-19 核对：1909-06-19—1948-06-13；'Ningen shikkaku (1948; No Longer Human)'；'His dark, wry tone perfectly captured the confusion of postwar Japan'"},
{"id":"B212","title":"Doris Lessing — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Doris-Lessing","type":"百科全书","verified":True,"covers":["lessing","jinsebiji"],"note":"2026-11-19 核对：1919-10-22—2013-11-17；2007诺贝尔奖；'The Golden Notebook (1962), in which a woman writer attempts to come to terms with the life of her times'"},
{"id":"B213","title":"Salman Rushdie — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Salman-Rushdie","type":"百科全书","verified":True,"covers":["rushdie","wuzhizidezi"],"note":"2026-11-19 核对：1947-06-19生于孟买；'Rushdie received the Booker Prize in 1981 for Midnight's Children'；'The novel subsequently won the Booker of Bookers (1993) and the Best of the Booker (2008)'"},
{"id":"B214","title":"Stefan Zweig — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Stefan-Zweig","type":"百科全书","verified":True,"covers":["zweig","moshengnvrendelaixin"],"note":"2026-11-19 核对：1881-11-28—1942-02-23；'Zweig's interest in psychology and the teachings of Sigmund Freud led to his most characteristic work, the subtle portrayal of character'；该页未提《陌生女人来信》——作品年份1922为通说待核"},
{"id":"B215","title":"Jean-Paul Sartre — Encyclopaedia Britannica","author":"The Editors of Encyclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/biography/Jean-Paul-Sartre","type":"百科全书","verified":True,"covers":["sartre","exin"],"note":"2026-11-19 核对：1905-06-21—1980-04-15；'During his years of teaching in Le Havre, Sartre published La Nausée (1938; Nausea)'；'Man is condemned to be free'；1964年获诺贝尔奖并公开拒绝"},
{"id":"B216","title":"Wang Anyi — Wikipedia (EN)","author":"Wikipedia contributors","year":"持续更新","url":"https://en.wikipedia.org/wiki/Wang_Anyi","type":"百科全书","verified":True,"covers":["wanganyi","changhenge"],"note":"2026-11-19 核对：1954-03-06生于南京；《长恨歌》1995/1996；2000年第五届茅盾文学奖；2017年 Newman Prize；中国作协副主席（2006起）；复旦教授；'Wang Qiyao is a metaphor for Shanghai'；被誉为张爱玲传人（wiki口径）"},
{"id":"B217","title":"Jia Pingwa — Wikipedia (EN)","author":"Wikipedia contributors","year":"持续更新","url":"https://en.wikipedia.org/wiki/Jia_Pingwa","type":"百科全书","verified":True,"covers":["jiapingwa","qinqiang"],"note":"2026-11-19 核对：1952-02-21生于陕西丹凤；《秦腔》2005年出版（首刊《收获》，作家出版社）；2008年第七届茅盾文学奖；2006首届红楼梦奖；《废都》1993年出版后被禁17年（2009解禁）"},
{"id":"B218","title":"Shi Tiesheng — Wikipedia (EN)","author":"Wikipedia contributors","year":"持续更新","url":"https://en.wikipedia.org/wiki/Shi_Tiesheng","type":"百科全书","verified":True,"covers":["shitiesheng","woyuditan"],"note":"2026-11-19 核对：1951-01-04北京—2010-12-31；1972年21岁双腿瘫痪；《我与地坛》(1991)——China Daily 转述：'Many critics have considered I and the Temple of Earth as one of the best Chinese prose essays of the 20th century'"},
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
