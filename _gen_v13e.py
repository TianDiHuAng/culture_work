# -*- coding: utf-8 -*-
"""v13E：复用已核来源直写 6 部"""
import json, pathlib

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = {
"shengdansongge": {
  "id":"shengdansongge","title":"圣诞颂歌","original_title":"A Christmas Carol. In Prose. Being a Ghost Story of Christmas","region":"英国","era":"近代","era_detail":"19世纪",
  "genre":"中篇小说","genre_group":"小说","language":"英语","author_id":"dickens","author_name":"查尔斯·狄更斯",
  "year_display":"1843年（作者页 B120 口径：圣诞颂歌（1843））","year_sort":1843,
  "background":["作者页（B120）：狄更斯 major_works 载'圣诞颂歌（1843）'（B120 作者页定位，详见 dawei 条核对）。","题材（通说待核）：斯克鲁奇的三次'幽灵'之旅——过去/现在/未来的圣诞。"],
  "outline":["马里的鬼魂警告→三个圣诞幽灵→'早上好，先生'的转变（通说待核）。"],
  "characters":[{"name":"斯克鲁奇","identity":"吝啬鬼","note":"转变者（通说待核）"},{"name":"鲍勃·克拉奇特","identity":"职员","note":"小蒂姆的父亲（通说待核）"}],
  "themes":["圣诞的人道主义：'圣诞快乐'的现代发明（通说待核）。",
   "吝啬与重生（通说）。",
   "'幽灵故事'的圣诞传统（书副题——通说）。"],
  "influence":[{"text":"作者页：狄更斯圣诞书代表作（B120 作者页口径）。","source":"B120"},
   {"text":"'Merry Christmas'的现代流行与本书互证（通说待核）。","source":"B120"}],
  "reading":{"difficulties":["古体'幽灵故事'的语调。","维多利亚圣诞习俗。"],
   "editions":["《圣诞颂歌》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域）。"],
   "order":"狄更斯圣诞书系列之首（五部）。"},
  "pending":["1843年12月19日初版核对。","斯克鲁奇/克拉奇特人名核对。","'圣诞书'系列（五部说）待核。"],
  "sources":["B120"],"year_source":"B120","author_source":"B120","related_works":["wudugu'er","dawei","shuangchengji"],
  "svg":G("《圣诞颂歌》三幽灵图",[{"title":"过去的圣诞","text":"童年的 forgotten","color":"family"},{"title":"现在的圣诞","text":"克拉特家的晚餐","color":"main"},{"title":"未来的圣诞","text":"小蒂姆的空椅","color":"antagonist"},{"title":"重生","text":"'早上好'的转变","color":"gold"}])
},
"huangliangshanzhuang": {"id":"huangliangshanzhuang","title":"荒凉山庄","original_title":"Bleak House","region":"英国","era":"近代","era_detail":"19世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"dickens","author_name":"查尔斯·狄更斯",
  "year_display":"1853年（作者页 B120 口径：荒凉山庄（1853））","year_sort":1853,
  "background":["作者页（B120）：狄更斯 major_works 载'荒凉山庄（1853）'（B120 作者页定位，详见 dawei 条核对）。","题材（通说待核）：詹狄士案（Jarndyce v Jarndyce）——大法官法庭的旷日诉讼；雾与法律的双主题。"],
  "outline":["大法官法庭的'荒凉'：詹狄士案吞噬所有人（通说待核）。","双叙述：埃丝特第一人称与全知视角交替（结构通说待核）。"],
  "characters":[{"name":"埃丝特·萨默森","identity":"养女","note":"部分叙述者（通说待核）"},{"name":"德洛克夫人","identity":"贵妇","note":"秘密（通说待核）"}],
  "themes":["法律机器的荒诞（通说）。",
   "雾都的卫生与贫困（通说待核）。",
   "双叙述实验（通说待核）。"],
  "influence":[{"text":"作者页：狄更斯代表作谱系（B120 作者页口径）。","source":"B120"},
   {"text":"对大法官法庭的批判被认为推动司法改革（通说待核）。","source":"B120"}],
  "reading":{"difficulties":["双叙述切换。","法律术语。"],
   "editions":["《荒凉山庄》（上海译文出版社黄邦杰译本？——通说待核）。","英文原版（公有领域）。"],
   "order":"狄更斯中后期之作。"},
  "pending":["1852—53年连载与1853年出版核对。","埃丝特/德洛克夫人人名核对。","詹狄士案原型（Jennens案）待核。"],
  "sources":["B120"],"year_source":"B120","author_source":"B120","related_works":["wudugu'er","dawei","shuangchengji"],
  "svg":G("《荒凉山庄》雾法结构图",[{"title":"大法官法庭","text":"詹狄士案（通说）","color":"antagonist"},{"title":"雾","text":"伦敦的脏雾","color":"family"},{"title":"埃丝特","text":"第一人称的暖","color":"main"},{"title":"德洛克","text":"秘密的夫人","color":"gold"}])
},
"sangzhongweisheerming": {
  "id":"sangzhongweisheerming","title":"丧钟为谁而鸣","original_title":"For Whom the Bell Tolls","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"hemingway","author_name":"欧内斯特·海明威",
  "year_display":"1940年（作者页 B051/B024 口径：丧钟为谁而鸣（1940））","year_sort":1940,
  "background":["作者页（B051/B024）：海明威 major_works 载'丧钟为谁而鸣（1940）'（作者页定位，详见 laorenhai 条核对）。","书名（通说待核）：出自约翰·多恩布道词'No man is an Iland'。","题材（通说待核）：西班牙内战中的美国志愿者乔丹炸桥的三天。"],
  "outline":["炸桥任务的三天：玛丽亚、游击队、背叛（通说待核）。","结尾：乔丹等待最后的机关枪——'丧钟'的自我完成（通说待核）。"],
  "characters":[{"name":"罗伯特·乔丹","identity":"爆破手","note":"（通说待核）"},{"name":"玛丽亚","identity":"少女","note":"（通说待核）"},{"name":"皮拉尔","identity":"游击队夫人","note":"（通说待核）"}],
  "themes":["国际主义与死亡（通说）。",
   "西班牙内战的史诗化（通说待核）。",
   "多恩的钟声：人类共同体（书名通说待核）。"],
  "influence":[{"text":"作者页：海明威代表作（B051/B024 作者页口径）。","source":"B051"},
   {"text":"普利策奖推荐被否（1941年——通说待核）。","source":"B051"}],
  "reading":{"difficulties":["西班牙内战史。","西班牙语插入语。"],
   "editions":["《丧钟为谁而鸣》（上海译文出版社，通说待核）。","英文原版。"],
   "order":"海明威三连读之末。"},
  "pending":["1940年出版（Scribner说）核对。","乔丹/玛丽亚/皮拉尔人名核对。","多恩布道词出处核对。"],
  "sources":["B051","B024"],"year_source":"B051","author_source":"B051","related_works":["yongbiewuqi","taiyangzhaochangshengqi","zhanzheng"],
  "svg":G("《丧钟》三天结构图",[{"title":"炸桥","text":"三天的任务","color":"main"},{"title":"玛丽亚","text":"被救的姑娘","color":"family"},{"title":"皮拉尔","text":"游击队的灵魂","color":"gold"},{"title":"丧钟","text":"多恩的共同体（通说）","color":"plain"}])
},
"renjiantiantang": {
  "id":"renjiantiantang","title":"人间天堂","original_title":"This Side of Paradise","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"fitzgerald","author_name":"弗朗西斯·斯科特·菲茨杰拉德",
  "year_display":"1920年（作者页 B050/B023 口径：人间天堂（1920））","year_sort":1920,
  "background":["作者页（B050/B023）：菲茨杰拉德 major_works 载'人间天堂（1920）'——其处女作（作者页定位，详见 gaicibi 条核对）。","题材（通说待核）：艾莫里的普林斯顿岁月与'自我主义者'的成长——战后美国青年的精神图谱。"],
  "outline":["艾莫里·布莱恩：普林斯顿、战争、初恋与幻灭（通说待核）。"],
  "characters":[{"name":"艾莫里·布莱恩","identity":"青年","note":"自传性（通说待核）"},{"name":"罗莎琳德","identity":"名媛","note":"（通说待核）"}],
  "themes":["爵士时代的开篇（通说）。",
   "'自我主义者'的成长（通说待核）。",
   "普林斯顿与名媛文化（通说待核）。"],
  "influence":[{"text":"作者页：菲茨杰拉德处女作（B050/B023 作者页口径）。","source":"B050"},
   {"text":"使24岁的作者一夜成名（通说待核）。","source":"B050"}],
  "reading":{"difficulties":["青春文体（诗+信+日记混合）。","1910年代大学文化。"],
   "editions":["《人间天堂》（人民文学出版社/上海译文版本，通说待核）。","英文原版（公有领域渐近）。"],
   "order":"菲茨杰拉德起点，先于《盖茨比》。"},
  "pending":["1920年3月出版（Scribner说）与一周售罄说待核。","艾莫里/罗莎琳德人名核对。","自传成分（作者与泽尔达）待核。"],
  "sources":["B050","B023"],"year_source":"B050","author_source":"B050","related_works":["gaicibi","yesetainrou","renshijian"],
  "svg":G("《人间天堂》成长结构图",[{"title":"普林斯顿","text":"校园的诗","color":"family"},{"title":"战争","text":"训练营的间隙","color":"plain"},{"title":"罗莎琳德","text":"初恋的幻灭","color":"antagonist"},{"title":"人间天堂","text":"自我的重建","color":"main"}])
},
"funiyuzuyi": {"id":"funiyuzuyi","title":"弗兰妮与祖伊","original_title":"Franny and Zooey","region":"美国","era":"现当代","era_detail":"20世纪",
  "genre":"中篇二部合刊","genre_group":"小说","language":"英语","author_id":"salinger","author_name":"J.D.塞林格",
  "year_display":"1961年（作者页 B148 口径：弗兰妮与祖伊（1961））","year_sort":1961,
  "background":["作者页（B148）：塞林格 major_works 载'弗兰妮与祖伊（1961）'（B148 作者页定位，详见 maitian 条核对）。","题材（通说待核）：格拉斯家最小的两兄妹——弗兰妮的精神危机与祖伊的引导（《耶稣祈祷词》）。"],
  "outline":["《弗兰妮》：大学周末的崩溃；《祖伊》：浴室与客厅的对话（通说待核）。"],
  "characters":[{"name":"弗兰妮","identity":"大学生","note":"（通说待核）"},{"name":"祖伊","identity":"演员","note":"引导者（通说待核）"}],
  "themes":["'耶稣祈祷词'与灵性（通说待核）。",
   "表演与真实的对立（通说待核）。",
   "格拉斯家族的续章（通说）。"],
  "influence":[{"text":"作者页：塞林格格拉斯系列（B148 作者页口径）。","source":"B148"},
   {"text":"禅与'灵性'书写的延续（通说）。","source":"B148"}],
  "reading":{"difficulties":["宗教祷告词。","对话的密度。"],
   "editions":["《弗兰妮与祖伊》（人民文学出版社/译林出版社版本，通说待核）。","英文原版。"],
   "order":"《九故事》后读。"},
  "pending":["两篇首刊（《纽约客》1955/1957说）核对。","弗兰妮/祖伊人名核对。","'耶稣祈祷词'细节待核。"],
  "sources":["B148"],"year_source":"B148","author_source":"B148","related_works":["jiugushi","maitian","shoujie"],
  "svg":G("《弗兰妮与祖伊》对话结构图",[{"title":"弗兰妮","text":"崩溃的周末","color":"main"},{"title":"祖伊","text":"哥哥的引导","color":"family"},{"title":"耶稣祈祷词","text":"灵性的钥匙（通说）","color":"gold"},{"title":"表演","text":"与真实的对立","color":"plain"}])
},
"maikeK": {"id":"maikeK","title":"迈克尔·K的生活和时代","original_title":"Life & Times of Michael K","region":"南非","era":"现当代","era_detail":"20世纪",
  "genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"coetzee","author_name":"J.M.库切",
  "year_display":"1983年（作者页 B161 口径：迈克尔·K的生活与时代（1983））","year_sort":1983,
  "background":["作者页（B161）：库切 major_works 载'迈克尔·K的生活与时代（1983）'（B161 作者页定位，详见 chi 条核对）。","获奖（通说待核）：1983年英国布克奖。","题材（通说待核）：内战中园丁迈克尔·K带母亲骨灰回乡——'园丁'的生存哲学。"],
  "outline":["战乱中的迁徙：营地的规训与田园的南瓜（通说待核）。"],
  "characters":[{"name":"迈克尔·K","identity":"园丁","note":"兔唇的流浪者（通说待核）"},{"name":"医疗官","identity":"军官","note":"想'解密'他（通说待核）"}],
  "themes":["'园丁'的生存哲学（通说待核）。",
   "营地的规训（通说）。",
   "无名的内战（通说）。"],
  "influence":[{"text":"作者页：库切代表作（B161 作者页口径）。","source":"B161"},
   {"text":"1983年布克奖（通说待核）。","source":"B161"}],
  "reading":{"difficulties":["南非内战背景。","K的沉默。"],
   "editions":["《迈克尔·K的生活和时代》（人民文学出版社/浙江文艺出版社版本，通说待核）。","英文原版。"],
   "order":"先《耻》后本作。"},
  "pending":["1983年出版（Ravan Press说）与布克奖核对。","迈克尔·K人名核对。","营地医疗官独白待核。"],
  "sources":["B161"],"year_source":"B161","author_source":"B161","related_works":["chi","qiyuderenmin","wajie"],
  "svg":G("《迈克尔·K》迁徙结构图",[{"title":"迁徙","text":"骨灰的归乡","color":"main"},{"title":"营地","text":"规训的国家","color":"antagonist"},{"title":"南瓜","text":"园丁的城池","color":"gold"},{"title":"沉默","text":"K的抵抗","color":"family"}])
}
}

for wid, d in works.items():
    p = pathlib.Path(f"data/works/{wid}.json")
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    print("created work", wid)
print(len(works), "works created")
