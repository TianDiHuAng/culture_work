# -*- coding: utf-8 -*-
"""流水线批15：零成本直写 5 部 + mauposangxuan 作者关联修复"""
import json, pathlib

# mauposangxuan 关联新莫泊桑作者页
p = pathlib.Path("data/works/mauposangxuan.json")
d = json.loads(p.read_text(encoding="utf-8"))
d["author_id"] = "maupassant"
d["author_source"] = "B310"
p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
print("mauposangxuan linked to maupassant")

def G2(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"huersuoge": {
  "id":"huersuoge","title":"赫尔索格","original_title":"Herzog","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"bellow","author_name":"索尔·贝娄",
  "year_display":"1964年出版（通说待核；作者页 B298 口径：major_works 载'赫尔索格、洪堡的礼物'——Herzog, Humboldt's Gift）","year_sort":1964,
  "background":["作者页（B298）：贝娄 major_works 载'赫尔索格、洪堡的礼物'（B298 作者页定位，详见 aojimaqi 条核对）。","作者（B298）：1976诺奖——'for the human understanding and subtle analysis of contemporary culture'；'cultural sophistication and the wisdom of the streets'。","题材（通说待核）：中世纪学者摩西·赫尔索格遭双重背叛（妻与挚友）后狂写'不寄出的信'。"],
  "outline":["给尼采、艾森豪威尔等人的'不寄出的信'——思想史的清算（通说待核）。"],
  "characters":[{"name":"摩西·赫尔索格","identity":"学者","note":"（通说待核）"},{"name":"瓦伦丁·格斯贝奇","identity":"挚友","note":"（通说待核）"}],
  "themes":["书信体的清算（通说待核）。",
   "知识分子在60年代的失位（通说）。",
   "'心'与'脑'的和解（通说待核）。"],
  "influence":[{"text":"作者页：贝娄代表作谱系（B298 作者页口径）。","source":"B298"},
   {"text":"作者页：1976诺奖——'human understanding and subtle analysis'（B298 作者级）。","source":"B298"}],
  "reading":{"difficulties":["书信体与意识的交错。","60年代思想史背景。"],
   "editions":["《赫尔索格》（人民文学出版社/上海译文版本，通说待核）。","英文原版。"],
   "order":"先《奥吉·玛琪》后本作。"},
  "pending":["1964年出版（Viking说）核对。","摩西·赫尔索格/格斯贝奇人名核对。","'不寄出的信'情节细节待核。"],
  "sources":["B298"],"year_source":"B298","author_source":"B298","related_works":["aojimaqi","meiguoren","yuehankelisituofu"],
  "svg":G2("《赫尔索格》书信结构图",[{"title":"不寄出的信","text":"写给世界","color":"main"},{"title":"背叛","text":"妻与挚友","color":"antagonist"},{"title":"赫尔索格","text":"中世纪学者","color":"gold"},{"title":"和解","text":"乡居的宁静","color":"family"}])
},
"woMenzhong": {
  "id":"woMenzhong","title":"我们中的一个","original_title":"One of Ours","region":"美国","era":"近代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"cather","author_name":"薇拉·凯瑟",
  "year_display":"1922年（Britannica：One of Ours (1922), which won the Pulitzer Prize——B292）","year_sort":1922,
  "background":["Britannica（B292）：'One of Ours (1922), which won the Pulitzer Prize, and A Lost Lady (1923) mourned the passing of the pioneer spirit.'（哀悼拓荒者精神的消逝——B292）。","作者（B292）：'With O Pioneers! (1913) and My Ántonia (1918)'——边疆主题代表；'unique regionalism'。"],
  "outline":["克劳德·惠勒从内布拉斯加农场走向一战战场——'pioneer spirit'的战后余响（通说待核）。"],
  "characters":[{"name":"克劳德·惠勒","identity":"农场青年","note":"（通说待核）"}],
  "themes":["拓荒精神的消逝（B292：mourned the passing of the pioneer spirit）。",
   "一战的美国农村面孔（通说待核）。",
   "寻找意义（通说待核）。"],
  "influence":[{"text":"Britannica：'One of Ours (1922), which won the Pulitzer Prize'（B292）。","source":"B292"},
   {"text":"作者页：凯瑟'unique regionalism'（B292 作者级）。","source":"B292"}],
  "reading":{"difficulties":["一战史。","农场叙事的舒缓节奏。"],
   "editions":["《我们中的一个》（中译本信息待核）。","英文原版（公有领域）。"],
   "order":"凯瑟战争题材之作。"},
  "pending":["1922年出版（Alfred A. Knopf说）核对。","克劳德·惠勒人名核对。","普利策奖1923年颁奖说（B292 作1922出版）核对。"],
  "sources":["B292"],"year_source":"B292","author_source":"B292","related_works":["wodeandongnia","atuopaozhe","erzhanyihuilu"],
  "svg":G2("《我们中的一个》战场图",[{"title":"农场","text":"内布拉斯加","color":"family"},{"title":"一战","text":"克劳德的从军","color":"main"},{"title":"拓荒者","text":"精神的消逝（B292）","color":"gold"},{"title":"普利策","text":"1922年作品（B292）","color":"plain"}])
},
"huohuadezhuangyuan": {
  "id":"huohuadezhuangyuan","title":"霍华德庄园","original_title":"Howards End","region":"英国","era":"现当代","era_detail":"20世纪初",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"forster","author_name":"E.M.福斯特",
  "year_display":"1910年（Britannica：Howards End (1910)——'brought Forster his first major success'）","year_sort":1910,
  "background":["Britannica（B282）：Howards End——'a more ambitious novel that brought Forster his first major success'；主题——'an alliance between the Schlegel sisters, Margaret and Helen, who embody the liberal imagination at its best'，与 Ruth Wilcox 'whose house stays close to the earth'——对照'commerce-minded Wilcox family'。","作者（B282）：'The values of truthfulness and kindness dominate Forster's later thinking'。"],
  "outline":["施莱格尔姐妹与威尔科克斯家：文化/商业的联姻（B282 语境）。","'Only connect'（唯有连接——作者座右铭，通说待核）。"],
  "characters":[{"name":"玛格丽特","identity":"姐姐","note":"'liberal imagination'（B282）"},{"name":"海伦","identity":"妹妹","note":"（B282）"},{"name":"亨利·威尔科克斯","identity":"商人","note":"（通说待核）"}],
  "themes":["'唯有连接'（通说待核——Only connect）。",
   "文化与商业的婚姻（B282）。",
   "房子与土地（B282：house stays close to the earth）。"],
  "influence":[{"text":"Britannica：'brought Forster his first major success'（B282）。","source":"B282"},
   {"text":"Britannica：1992年 Merchant Ivory 电影改编（通说待核）。","source":"B282"}],
  "reading":{"difficulties":["爱德华时代阶级背景。","'连接'的哲学。"],
   "editions":["《霍华德庄园》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"先本作后《印度之行》。"},
  "pending":["1910年出版（Edward Arnold说）核对。","施莱格尔/威尔科克斯人名核对。","1992年电影（Merchant Ivory）待核。"],
  "sources":["B282"],"year_source":"B282","author_source":"B282","related_works":["yinduzhixing","aosailuo","嘉莉妹妹"],
  "svg":G2("《霍华德庄园》连接结构图",[{"title":"施莱格尔姐妹","text":"liberal imagination（B282）","color":"main"},{"title":"威尔科克斯家","text":"commerce-minded","color":"antagonist"},{"title":"霍华德庄园","text":"贴近土地的房子","color":"gold"},{"title":"唯有连接","text":"作者的座右铭（通说）","color":"family"}])
},
"hushejie": {
  "id":"hushejie","title":"蝮蛇结","original_title":"Le Noeud de vipères（Vipers' Tangle）","region":"法国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"mauriac","author_name":"弗朗索瓦·莫里亚克",
  "year_display":"1932年（Britannica：Le Noeud de vipères (1932; Vipers' Tangle...)——'often considered Mauriac's masterpiece'）","year_sort":1932,
  "background":["Britannica（B289）：'Le Noeud de vipères (1932; Vipers' Tangle...) is often considered Mauriac's masterpiece.'（常被视为莫里亚克的杰作——B289）；作者（B289）：1952诺奖、1933法兰西学院；'somber, austere psychological dramas'。","文体（通说待核）：书信体——老律师路易的'复仇'日记写给妻子（死后寄出）。"],
  "outline":["路易的日记：对妻室的怨恨清算——与最后的和解（通说待核）。"],
  "characters":[{"name":"路易","identity":"老律师","note":"（通说待核）"},{"name":"伊莎","identity":"妻子","note":"（通说待核）"}],
  "themes":["怨恨的'蝮蛇结'（书名通说待核）。",
   "书信体的忏悔（通说待核）。",
   "天主教的救赎（B289 语境：Catholic novelist）。"],
  "influence":[{"text":"Britannica：'often considered Mauriac's masterpiece'（B289）。","source":"B289"},
   {"text":"Britannica：1952年诺贝尔文学奖（B289 作者级）。","source":"B289"}],
  "reading":{"difficulties":["书信体独白。","天主教语境。"],
   "editions":["《蝮蛇结》（广西师范大学出版社，通说待核）。","法文原版（公有领域渐近）。"],
   "order":"先《爱的荒漠》后本作。"},
  "pending":["1932年出版（Grasset说）核对。","路易/伊莎人名核对。","'蝮蛇结'的题解待核。"],
  "sources":["B289"],"year_source":"B289","author_source":"B289","related_works":["aidewangmo","taileisi","嘉莉妹妹"],
  "svg":G2("《蝮蛇结》怨恨结构图",[{"title":"日记","text":"写给亡妻","color":"main"},{"title":"怨恨","text":"蝮蛇之结","color":"antagonist"},{"title":"路易","text":"老律师","color":"gold"},{"title":"和解","text":"最后的宽恕","color":"family"}])
},
"yumaoGuan": {
  "id":"yumaoGuan","title":"羽毛冠","original_title":"A Crown of Feathers","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"短篇小说集","genre_group":"小说","language":"英语（意第绪语转译）","author_id":"singer","author_name":"艾萨克·巴什维斯·辛格",
  "year_display":"1973年（作者页 B312 口径：A Crown of Feathers (1973; National Book Award)）","year_sort":1973,
  "background":["作者页（B312）：辛格 major_works 载'A Crown of Feathers (1973; National Book Award)'（B312 作者页定位，详见 shagua 条核对）。","作者（B312）：1978诺奖——意第绪语写作；'blending irony, wit, and wisdom with the occult and grotesque'。"],
  "outline":["意第绪语短篇集：魔鬼、傻瓜与神秘主义（通说待核）。"],
  "characters":[{"name":"意第绪世界的人们","identity":"群像","note":"（通说待核）"}],
  "themes":["'羽毛冠'的称号之争（通说待核——同名篇）。",
   "神秘与怪诞（B312：occult and grotesque）。",
   "意第绪文学的现代（通说待核）。"],
  "influence":[{"text":"作者页：辛格 major_works——A Crown of Feathers (1973; National Book Award)（B312）。","source":"B312"},
   {"text":"作者页：辛格1978年诺奖（B312 作者级定位）。","source":"B312"}],
  "reading":{"difficulties":["意第绪文化语境。","神秘主义篇章。"],
   "editions":["《羽毛冠》（中译本信息待核）。","英文原版（Farrar, Straus）。"],
   "order":"先《傻瓜吉姆佩尔》后本作。"},
  "pending":["1973年出版（Farrar, Straus and Giroux说）核对。","同名篇情节待核。","国家图书奖（1973——B312 已载）核对。"],
  "sources":["B312"],"year_source":"B312","author_source":"B312","related_works":["shagua","haorennanxun","luoshengmen"],
  "svg":G2("《羽毛冠》神秘结构图",[{"title":"羽毛冠","text":"称号之争（通说）","color":"main"},{"title":"魔鬼","text":"occult（B312）","color":"antagonist"},{"title":"意第绪","text":"语言的家园","color":"gold"},{"title":"怪诞","text":"grotesque（B312）","color":"family"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
