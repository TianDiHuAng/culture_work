# -*- coding: utf-8 -*-
"""流水线批次6：零成本2部 + Britannica新核（金瓶梅等）"""
import json, pathlib

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"fennigendeshoulingye": {
  "id":"fennigendeshoulingye","title":"芬尼根的守灵夜","original_title":"Finnegans Wake","region":"爱尔兰","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语（多语混杂）","author_id":"joyce","author_name":"詹姆斯·乔伊斯",
  "year_display":"1939年（作者页 B093 口径：芬尼根的守灵夜（1939））","year_sort":1939,
  "background":["作者页（B093）：乔伊斯 major_works 载'芬尼根的守灵夜（1939）'（B093 作者页定位，详见 youlisisi 条核对）。","文体（通说待核）：多语言梦语——riverrun 开篇与'here comes everybody'（通说待核）。"],
  "outline":["都柏林酒馆老板 Humphrey Earwicker 一家的梦循环——开篇与结尾相连（riverrun，once upon a time——通说待核）。"],
  "characters":[{"name":"HCE","identity":"酒馆老板","note":"Here Comes Everybody（通说待核）"},{"name":"ALP","identity":"妻子","note":"河的化身（通说待核）"}],
  "themes":["梦的语言：诸语的河流（通说待核）。",
   "循环结构：结尾接开头（通说待核）。",
   "所有历史的夜海（通说）。"],
  "influence":[{"text":"作者页：乔伊斯最后的长篇（B093 作者页口径）。","source":"B093"},
   {"text":"被誉为最难读的英语小说之一（通说待核）。","source":"B093"}],
  "reading":{"difficulties":["多语言造词。","环形结构——可从任意处读起。"],
   "editions":["《芬尼根的守灵夜》（上海译文出版社戴从容译本（第一卷），通说待核）。","英文原版（公有领域渐近）。"],
   "order":"乔伊斯终局：先《都柏林人》《尤利西斯》后本作。"},
  "pending":["1939年出版（Faber & Faber/London与Viking说）核对。","riverrun 首词与环形结尾核对。","戴从容译本信息待核。"],
  "sources":["B093"],"year_source":"B093","author_source":"B093","related_works":["youlisisi","dubolinen","luoshengmen"],
  "svg":G("《守灵夜》环形结构图",[{"title":"riverrun","text":"开篇即结尾","color":"main"},{"title":"HCE与ALP","text":"夫妻的梦","color":"family"},{"title":"诸语","text":"多语言的河流","color":"gold"},{"title":"夜海","text":"所有历史","color":"plain"}])
},
"wanyaniayjiu": {
  "id":"wanyaniayjiu","title":"万尼亚舅舅","original_title":"Дядя Ваня（Uncle Vanya）","region":"俄国","era":"近代","era_detail":"19世纪末",
  "genre":"四幕剧","genre_group":"戏剧","language":"俄语","author_id":"chikefu","author_name":"安东·契诃夫",
  "year_display":"1897年出版（作者页 B270 口径：Uncle Vanya (1897)）","year_sort":1897,
  "background":["作者页（B270）：契诃夫 major works 存目含'Uncle Vanya (1897)'（B270 作者页定位）。","题材（通说待核）：乡村庄园——万尼亚舅舅为教授'牺牲'半生后的觉醒与未遂的枪击。"],
  "outline":["教授到来：万尼亚的幻灭、叶列娜的美、阿斯特罗夫的森林演说（通说待核）。"],
  "characters":[{"name":"万尼亚舅舅","identity":"庄园管理者","note":"被牺牲者（通说待核）"},{"name":"阿斯特罗夫","identity":"医生","note":"森林演说（通说待核）"},{"name":"叶列娜","identity":"教授妻子","note":"（通说待核）"}],
  "themes":["'被牺牲的'人生（通说待核）。",
   "森林：契诃夫的生态先声（通说待核）。",
   "无事的结尾：'休息'（通说待核）。"],
  "influence":[{"text":"作者页：契诃夫戏剧存目（B270 作者页口径）。","source":"B270"},
   {"text":"作者页：'契诃夫之枪'与未说出之重（B270）。","source":"B270"}],
  "reading":{"difficulties":["乡村庄园语境。","'潜台词'表演。"],
   "editions":["《万尼亚舅舅》（人民文学出版社《契诃夫戏剧集》，通说待核）。","俄文原版（公有领域）。"],
   "order":"契诃夫戏剧四部之二。"},
  "pending":["1897年出版、1899年首演说核对。","万尼亚/阿斯特罗夫/叶列娜人名核对。","森林演说原文待核。"],
  "sources":["B270"],"year_source":"B270","author_source":"B270","related_works":["yingtaoyuan","haiou","leiyu"],
  "svg":G("《万尼亚舅舅》庄园结构图",[{"title":"庄园","text":"半生的牺牲","color":"main"},{"title":"教授","text":"投机的功名","color":"antagonist"},{"title":"森林演说","text":"阿斯特罗夫（通说）","color":"gold"},{"title":"休息","text":"无事的结尾","color":"family"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
