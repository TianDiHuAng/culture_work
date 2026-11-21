# -*- coding: utf-8 -*-
"""流水线批次13：中世纪/民族史诗 4 部（佚名/编纂者，无作者页）"""
import json, pathlib

new_src = [
{"id":"B301","title":"Beowulf — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Beowulf","type":"百科全书","verified":True,"covers":["beaowufu"],"note":"2026-11-21 核对：'It is preserved in a single manuscript that dates to circa 1000'（Cotton MS Vitellius A XV）；'is believed to have been composed between 700 and 750'；'The work deals with events of the early 6th century'；'The poem did not appear in print until 1815'；'the highest achievement of Old English literature and the earliest European vernacular epic'；格伦德尔12年恐怖；与母亲在洞穴搏杀'a sword'；火龙——'Beowulf is mortally wounded from a bite in the neck'；威格拉夫继任；海葬于barrow；'the fear that, without Beowulf, Geatland will be invaded'"},
{"id":"B306","title":"La Chanson de Roland — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/La-Chanson-de-Roland","type":"百科全书","verified":True,"covers":["luolanzhige"],"note":"2026-11-21 核对：'probably the earliest (c. 1100) chanson de geste'且'considered the masterpiece of the genre'；'The poem takes the historical Battle of Roncesvalles (Roncevaux) in 778 as its subject'；'Ganelon plots with the Saracens to achieve his stepsons destruction'；'the rear guard is surrounded at the pass of Roncesvalles by an overwhelming Saracen force'；'the personality clash between the recklessly courageous Roland and his more prudent friend Oliver'；'Roland, whose judgment is clouded by his personal preoccupation with renown, rejects Olivers advice to blow his horn'"},
{"id":"B307","title":"Nibelungenlied — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Nibelungenlied","type":"百科全书","verified":True,"covers":["nibolungenzhige"],"note":"2026-11-21 核对：'written about 1200 by an unknown Austrian from the Danube region'；三份13世纪主要手稿 A(Munich)/B(St. Gall)/C(Donaueschingen)——'B as the most trustworthy'；中古高地德语；Siegfried'is determined to woo Kriemhild'；隐身斗篷代 Gunther 出赛；Hagen'learns Siegfrieds one vulnerable spot and then strikes the fatal blow'；'Hagen, fearing that her influence will grow, sinks the treasure in the Rhine'；'with Siegfrieds sword, she slays the bound and defenseless Hagen'；'Probably no literary work has given more to Germanic arts than the Nibelungenlied'；源自437年匈人灭勃艮第王国（Worms）的历史"},
{"id":"B308","title":"Kalevala — Encyclopaedia Britannica","author":"The Editors of Enclopaedia Britannica","year":"持续更新","url":"https://www.britannica.com/topic/Kalevala","type":"百科全书","verified":True,"covers":["kalewala"],"note":"2026-11-21 核对：Elias Lönnrot 编，'published the folk material in two editions (32 cantos, 1835; enlarged into 50 cantos, 1849)'；'compiled from old Finnish ballads, lyrical songs, and incantations that were a part of Finnish oral tradition'；Väinämöinen——'a powerful seer with supernatural origins'、'a master of the kantele'；'Kalevala……is a poetic name for Finland, meaning land of heroes'；芬兰民族史诗—— fostering 'the Finnish national spirit'、'translated into at least 20 languages'、启发了Gallen-Kallela绘画与西贝柳斯音乐、Longfellow《海华沙之歌'}；"},
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

works = {
"beaowufu": {
  "id":"beaowufu","title":"贝奥武甫","original_title":"Beowulf","region":"英国","era":"古代","era_detail":"盎格鲁-撒克逊时代",
  "genre":"英雄史诗","genre_group":"诗歌","language":"古英语","author_id":None,"author_name":"佚名（Anglo-Saxon 匿名诗人）",
  "year_display":"创作约700—750年间；存世唯一手稿约1000年（Britannica）","year_sort":-700,
  "background":["Britannica（B301）：'the highest achievement of Old English literature and the earliest European vernacular epic'（古英语文学的最高成就、最早的欧洲俗语史诗）。","手稿（B301）：'preserved in a single manuscript that dates to circa 1000'（Cotton MS Vitellius A XV）；创作'between 700 and 750'；1815年才首次印刷（B301）。"],
  "outline":["第一部分：贝奥武甫为丹麦王赫罗斯加除怪——格伦德尔12年恐怖（B301：For 12 years the creature terrorizes Heorot）、扭断其臂（B301）、杀死其母于洞穴（B301：They struggle in her dry cave at the mere's bottom）。","第二部分：老王贝奥武甫与火龙——毒牙致命（B301：mortally wounded from a bite in the neck）；威格拉夫继任（B301：names Wiglaf his successor）；海葬于barrow（B301）。","恐惧：'without Beowulf, Geatland will be invaded by nearby tribes'（B301）。"],
  "characters":[{"name":"贝奥武甫","identity":"耶阿特王子→老王","note":"（B301）"},{"name":"格伦德尔","identity":"沼泽怪物","note":"12年恐怖（B301）"},{"name":"火龙","identity":"守宝龙","note":"最后的敌人（B301）"},{"name":"威格拉夫","identity":"继任者","note":"（B301）"}],
  "themes":["英雄与死亡的史诗（B301）。",
   "'最高成就、最早俗语史诗'（B301）。",
   "氏族社会与继任危机（B301：Geatland 恐惧）。"],
  "influence":[{"text":"Britannica：'the highest achievement of Old English literature and the earliest European vernacular epic'（B301）。","source":"B301"},
   {"text":"托尔金《魔戒》与其研究（通说待核——B301 未载）。","source":"B301"}],
  "reading":{"difficulties":["古英语头韵体（中译转转）。","族谱与盾形纹章（氏族谱）。"],
   "editions":["《贝奥武甫》（人民文学出版社/译林出版社版本，通说待核）。","英文原版（公有领域）。"],
   "order":"西方史诗源头之一（先于《神曲》传统）。"},
  "pending":["创作年代（700—750 vs 8世纪说）核对。","3182行说（通说）待核。","托尔金1936年讲座《贝奥武甫：怪物与批评家》待核。"],
  "sources":["B301"],"year_source":"B301","author_source":"B301","related_works":["iliad","aeneid","hakebei"],
  "svg":G2("《贝奥武甫》三战结构图",[{"title":"格伦德尔","text":"12年恐怖（B301）","color":"antagonist"},{"title":"其母","text":"洞穴之战","color":"family"},{"title":"火龙","text":"老王的终战","color":"gold"},{"title":"海葬","text":"barrow的告别","color":"main"}])
},
"luolanzhige": {
  "id":"luolanzhige","title":"罗兰之歌","original_title":"La Chanson de Roland","region":"法国","era":"古代","era_detail":"中世纪",
  "genre":"武功歌（英雄史诗）","genre_group":"诗歌","language":"古法语","author_id":None,"author_name":"佚名（传统署名 Turold，图罗尔德——待核）",
  "year_display":"约1100年（Britannica：probably the earliest (c. 1100) chanson de geste）","year_sort":1100,
  "background":["Britannica（B306）：'probably the earliest (c. 1100) chanson de geste'且'considered the masterpiece of the genre'（最早的武功歌、该文类的杰作——B306）。","题材（B306）：'The poem takes the historical Battle of Roncesvalles (Roncevaux) in 778 as its subject'——把778年龙塞沃小规模冲突史诗化。"],
  "outline":["加奈隆通敌：'plots with the Saracens to achieve his stepsons destruction'（B306）。","后军被围：'surrounded at the pass of Roncesvalles by an overwhelming Saracen force'（B306）。","罗兰拒绝吹号：'rejects Olivers advice to blow his horn'（B306）——直至太迟。"],
  "characters":[{"name":"罗兰","identity":"骑士","note":"'recklessly courageous'（B306）"},{"name":"奥利维埃","identity":"挚友","note":"'more prudent friend'（B306）"},{"name":"加奈隆","identity":"继子/叛徒","note":"（B306）"}],
  "themes":["罗兰与奥利维埃的性格对撞（B306）。",
   "封臣忠诚与家族复仇（通说待核）。",
   "十字军语境前的圣战书写（通说待核）。"],
  "influence":[{"text":"Britannica：'considered the masterpiece of the genre'（武功歌的杰作——B306）。","source":"B306"},
   {"text":"Britannica：'probably the earliest (c. 1100) chanson de geste'（B306）。","source":"B306"}],
  "reading":{"difficulties":["武功歌的十音节诗行。","778年史实与虚构的边界。"],
   "editions":["《罗兰之歌》（人民文学出版社杨宪益译本，通说待核）。","古法文原版（公有领域）。"],
   "order":"中世纪史诗首选（先《罗兰之歌》后《尼伯龙根之歌》）。"},
  "pending":["牛津本（Bodleian Digby 23说）与 Turold 署名待核。","'Aoi'程式语核对。","号角 Olifant 名核对。"],
  "sources":["B306"],"year_source":"B306","author_source":"B306","related_works":["iliad","shenqu","aeneid"],
  "svg":G2("《罗兰之歌》龙塞沃结构图",[{"title":"加奈隆","text":"通敌的继父（B306）","color":"antagonist"},{"title":"罗兰","text":"骁勇的拒绝吹号","color":"main"},{"title":"奥利维埃","text":"明智的劝告","color":"gold"},{"title":"龙塞沃","text":"778年的山口","color":"family"}])
},
"nibolungenzhige": {
  "id":"nibolungenzhige","title":"尼伯龙根之歌","original_title":"Das Nibelungenlied（Der Nibelunge Not）","region":"德国","era":"古代","era_detail":"中世纪（约1200）",
  "genre":"英雄史诗","genre_group":"诗歌","language":"中古高地德语","author_id":None,"author_name":"佚名（'an unknown Austrian from the Danube region'——B307）",
  "year_display":"约1200年（Britannica：written about 1200 by an unknown Austrian from the Danube region）","year_sort":1200,
  "background":["Britannica（B307）：'written about 1200 by an unknown Austrian from the Danube region'（约1200年由多瑙河流域的无名奥地利人写就）。","手稿（B307）：三份13世纪主要手稿——A(Munich)/B(St. Gall)/C(Donaueschingen)，'B as the most trustworthy'。","地位（B307）：'Probably no literary work has given more to Germanic arts than the Nibelungenlied'。"],
  "outline":["上卷：齐格弗里德娶克里姆希尔德——隐身斗篷助恭特赢比武（B307：Gunther goes through the motions of deeds actually performed by Siegfried in a cloak of invisibility）。","哈根识破弱点并' strikes the fatal blow'（B307）；'sinks the treasure in the Rhine'（莱茵沉宝——B307）。","下卷：克里姆希尔德'with Siegfrieds sword, she slays the bound and defenseless Hagen'（复仇——B307）。"],
  "characters":[{"name":"齐格弗里德","identity":"屠龙英雄","note":"（B307）"},{"name":"克里姆希尔德","identity":"复仇者","note":"（B307）"},{"name":"哈根","title":"哈根","identity":"忠臣·杀手","note":"（B307）"}],
  "themes":["复仇与荣誉的毁灭链（B307）。",
   "尼伯龙根宝物：'sinks the treasure in the Rhine'（B307）。",
   "437年勃艮第王国覆灭的历史内核（B307 语境：Hunnish overthrow……437 CE）。"],
  "influence":[{"text":"Britannica：'Probably no literary work has given more to Germanic arts than the Nibelungenlied'（B307）。","source":"B307"},
   {"text":"瓦格纳《尼伯龙根的指环》受其启发（B307 语境：inspired works like Wagners Der Ring des Nibelungen）。","source":"B307"}],
  "reading":{"difficulties":["中古高地德语与尼伯龙根人名。","39歌（Aventiure）结构。"],
   "editions":["《尼伯龙根之歌》（人民文学出版社，通说待核）。","中古高地德语原版（公有领域）。"],
   "order":"日耳曼史诗首选（对照《贝奥武甫》）。"},
  "pending":["39歌（Aventiuren）核对。","哈根沉宝地点（莱茵河说）核对。","克里姆希尔德/布伦希尔特人名核对。"],
  "sources":["B307"],"year_source":"B307","author_source":"B307","related_works":["gelintonghua","shenqu","huashenboshi"],
  "svg":G2("《尼伯龙根之歌》复仇链图",[{"title":"齐格弗里德","text":"致命弱点（B307）","color":"main"},{"title":"哈根","text":"致命一击","color":"antagonist"},{"title":"克里姆希尔德","text":"持剑复仇（B307）","color":"gold"},{"title":"莱茵沉宝","text":"永远的秘藏","color":"family"}])
},
"kalewala": {
  "id":"kalewala","title":"卡勒瓦拉","original_title":"Kalevala","region":"芬兰","era":"近代","era_detail":"19世纪",
  "genre":"民族史诗（编纂）","genre_group":"诗歌","language":"芬兰语","author_id":None,"author_name":"埃利亚斯·伦罗特（Elias Lönnrot）编纂——芬兰民间口传歌谣辑录",
  "year_display":"1835年初版（32篇）、1849年定版（50篇）（Britannica：two editions (32 cantos, 1835; enlarged into 50 cantos, 1849)）","year_sort":1849,
  "background":["Britannica（B308）：'compiled from old Finnish ballads, lyrical songs, and incantations that were a part of Finnish oral tradition'——从芬兰口传传统辑录。","两版（B308）：32 cantos (1835)；enlarged into 50 cantos (1849)。","地位（B308）：'Kalevala, Finnish national epic'——fostering 'the Finnish national spirit'、'translated into at least 20 languages'、启发 Gallen-Kallela 绘画与 Sibelius 音乐、Longfellow《海华沙之歌》（B308）。"],
  "outline":["维纳莫宁——'the old and wise'、'a powerful seer with supernatural origins'、'a master of the kantele, the Finnish harplike stringed instrument'（B308）。","伊尔马利宁锻造'sampo'（神磨）（B308 语境：tales including the forging of the sampo）。","'Kalevala……a poetic name for Finland, meaning land of heroes'（B308）。"],
  "characters":[{"name":"维纳莫宁","identity":"先知歌者","note":"'old and wise'（B308）"},{"name":"伊尔马利宁","identity":"铁匠","note":"锻 sampo（B308 语境）"}],
  "themes":["口传传统的辑录与民族史诗（B308）。",
   "'卡勒瓦拉'：英雄之地（B308：land of heroes）。",
   "sampo 的锻造与争夺（通说待核）。"],
  "influence":[{"text":"Britannica：芬兰民族史诗——fostering 'the Finnish national spirit'（B308）。","source":"B308"},
   {"text":"Britannica：'translated into at least 20 languages'；启发 Sibelius 音乐与 Longfellow《海华沙之歌》（B308）。","source":"B308"}],
  "reading":{"difficulties":["芬兰语史诗韵律（卡勒瓦拉体）。","神话谱系。"],
   "editions":["《卡勒瓦拉》（人民文学出版社/上海译文版本，通说待核）。","芬兰文原版（公有领域）。"],
   "order":"芬兰文学首选。"},
  "pending":["50篇（cantos）结构核对。","'sampo'锻造情节核对。"," Lönnrot 各次田野采集（1831—35说）待核。"],
  "sources":["B308"],"year_source":"B308","author_source":"B308","related_works":["shijing","bainian","conglinzhihue"],
  "svg":G2("《卡勒瓦拉》英雄谱图",[{"title":"维纳莫宁","text":"先知与琴师（B308）","color":"main"},{"title":"伊尔马利宁","text":"锻 sampo 的铁匠","color":"gold"},{"title":"勒明凯宁","text":"浪子（通说待核）","color":"family"},{"title":"卡勒瓦拉","text":"英雄之地（B308）","color":"plain"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
