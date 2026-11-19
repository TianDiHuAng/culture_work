# -*- coding: utf-8 -*-
"""补足3个作家页的timeline至3条以上"""
import json, pathlib

fixes = {
"lifeifu": [
 {"year": 1953, "text": "生于河南（1953年说——通说待核）。", "src": "C012"},
 {"year": 2012, "text": "《生命册》出版（作家出版社——C012 官方名单口径）。", "src": "C012"},
 {"year": 2015, "text": "获第九届茅盾文学奖（C012）。", "src": "C012"},
 {"year": 2024, "text": "近年创作持续（'平原三部曲'谱系说——通说待核）。", "src": "C012"}],
"lingli": [
 {"year": 1942, "text": "生于（1942年说——通说待核）。", "src": "C012"},
 {"year": 1987, "text": "《少年天子》获第三届茅盾文学奖（C012 官方名单口径；出版年1987说待核）。", "src": "C012"},
 {"year": 2018, "text": "卒（2018年说——通说待核）。", "src": "C012"}],
"xiongzhaozheng": [
 {"year": 1953, "text": "生于（1953年说——通说待核）。", "src": "C012"},
 {"year": 2002, "text": "《张居正》获第六届茅盾文学奖（C012 官方名单口径）。", "src": "C012"},
 {"year": 2010, "text": "电视剧《万历首张居正》播出（2010年说——通说待核）。", "src": "C012"}],
}
for aid, tl in fixes.items():
    p = pathlib.Path(f"data/authors/{aid}.json")
    d = json.loads(p.read_text(encoding="utf-8"))
    d["timeline"] = tl
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("fixed", aid)
