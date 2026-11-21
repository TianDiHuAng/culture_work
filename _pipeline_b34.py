# -*- coding: utf-8 -*-
"""批34：零成本 4 部（B309/B290/B109/B039 注记 + 书名查重）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 波德莱尔《巴黎的忧郁》(B309)
{"id":"balideyouyu","title":"巴黎的忧郁","original_title":"Le Spleen de Paris（Petits poèmes en prose）","region":"法国","era":"近代","era_detail":"19世纪60年代",
"genre":"散文诗集","genre_group":"诗歌","language":"法语","author_id":"baudelaire","author_name":"夏尔·波德莱尔",
"year_display":"1868年（Britannica B309：Petits poèmes en prose (1868)——《恶之花》作者页口径）","year_sort":1868,
"background":["Britannica（B309）：Petits poèmes en prose——'the most successful and innovative early experiment in prose poetry'（散文诗最早、最成功、最具创新性的实验）。","Britannica（B309）：波德莱尔《恶之花》(1857)——'perhaps the most important and influential poetry collection published in Europe in the 19th century'——本集为其姊妹篇。","题材（通说待核）：巴黎人群像——穷苦人、老人、寡妇、狗与镜子。"],
"outline":["（通说待核——B309未载篇目）五十篇散文诗的城市速写。","（通说待核）《穷人》式的苦难清单与'现代生活的画家'目光。"],
"characters":[{"name":"抒情'我'","identity":"城市漫游者","note":"（通说待核）"}],
"themes":["散文诗的形式发明（B309）。",
 "都市人群与'无聊'（书名 Le Spleen——通说待核）。",
 "现代性的美学（B309 语境）。"],
"influence":[{"text":"Britannica：'the most successful and innovative early experiment in prose poetry'（B309）。","source":"B309"},{"text":"Britannica：《恶之花》的19世纪影响力定位（B309 交叉）。","source":"B309"}],
"reading":{"difficulties":["散文诗与格律诗的边界。","第二帝国巴黎的城市史（通说待核）。"],
 "editions":["《巴黎的忧郁》中译本（人民文学/上海译文等——通说待核）。","法文原版（公有领域）。"],
 "order":"《恶之花》后读；散文诗源流首选。"},
"pending":["篇目（《穷人的眼睛》等）核对（B309未载）。","1868年死后出版细节待核。","'五十篇'数量待核。"],
"sources":["B309"],"year_source":"B309","author_source":"B309","related_works":["diyuzhiji","ezhihua","wuguigu"],
"svg":G("《巴黎的忧郁》城市速写图",[{"title":"散文诗","text":"形式的发明（B309）","color":"gold"},{"title":"巴黎人群","text":"城市的众生（通说）","color":"main"},{"title":"Spleen","text":"无聊与忧郁（通说）","color":"antagonist"},{"title":"漫游者","text":"现代生活的目光（通说）","color":"family"}])},
# 2. 巴恩斯《10 1/2章世界史》(B290)
{"id":"shizhangshijieshi","title":"10 1/2章世界史","original_title":"A History of the World in 10½ Chapters","region":"英国","era":"现当代","era_detail":"20世纪80年代末",
"genre":"长篇小说（章节体）","genre_group":"小说","language":"英语","author_id":"barnes","author_name":"朱利安·巴恩斯",
"year_display":"1989年（Britannica B290：A History of the World in 10½ Chapters (1989)）","year_sort":1989,
"background":["Britannica（B290）：A History of the World in 10½ Chapters (1989)——作者页列举。","Britannica（B290）：巴恩斯 Flaubert's Parrot (1984)——'a humorous mixture of biography, fiction, and literary criticism'——本作延续其文体实验。","Britannica（B290）：The Sense of an Ending——'uses an unreliable narrator to explore the subjects of memory and aging'（2011布克奖）。"],
"outline":["（通说待核——B290未载篇目）以挪亚方舟木虫为'第1章'的世界史碎片。","（通说待核）'半章'：论爱与历史的插叙。"],
"characters":[{"name":"众声叙述者","identity":"章节体","note":"（通说待核）"}],
"themes":["历史的不可靠叙述（B290：《终结的感觉》unreliable narrator 语系）。",
 "挪亚方舟的戏仿（通说待核）。",
 "爱与幸存（通说待核）。"],
"influence":[{"text":"Britannica：巴恩斯2011布克奖（B290）。","source":"B290"},{"text":"Britannica：'biography, fiction, and literary criticism'的混合文体（B290 交叉）。","source":"B290"}],
"reading":{"difficulties":["章节体的松散性。","历史与虚构的边界。"],
 "editions":["《10 1/2章世界史》中译本（译林等——通说待核）。","英文原版。"],
 "order":"巴恩斯文体实验首选；后接《终结的感觉》。"},
"pending":["'第半章'细节核对（通说）。","1989年出版（Jonathan Cape说）待核。","章节名核对（B290未载）。"],
"sources":["B290"],"year_source":"B290","author_source":"B290","related_works":["zhongjiendeganjue","leiyu","aiyuheandegushi"],
"svg":G("《10½章世界史》章节体图",[{"title":"章节体","text":"世界史的碎片（B290）","color":"main"},{"title":"挪亚方舟","text":"戏仿的开端（通说）","color":"gold"},{"title":"半章","text":"论爱与历史（通说）","color":"family"},{"title":"不可靠","text":"叙述的底色（B290语系）","color":"antagonist"}])},
# 3. 芥川龙之介《一个傻瓜的一生》(B109)
{"id":"yigeshaguadeyisheng","title":"一个傻瓜的一生","original_title":"或阿呆的一生","region":"日本","era":"近代","era_detail":"20世纪20年代",
"genre":"中篇小说（自传体）","genre_group":"小说","language":"日语","author_id":"akutagawa","author_name":"芥川龙之介",
"year_display":"1927年（Britannica B109：芥川后期转向自传性——本作1927年——'自传性告白'（通说待核））","year_sort":1927,
"background":["Britannica（B109）：芥川'后期转向自传性'；1927年35岁自杀震惊文坛——本作为其绝笔期作品。","作者页注记：'自传性告白'（通说待核——B109未载本作名）。","Britannica（B109）：绝笔讽刺《河童》(1927)映照抑郁——与本作同年。"],
"outline":["（通说待核）断章体的自传：'傻瓜'对一生的清点。","（通说待核）'倦怠'与'电石灯'意象的临终目光。"],
"characters":[{"name":"'傻瓜'","identity":"自传之'我'","note":"（通说待核）"}],
"themes":["自传性的临终告白（B109：后期转向自传性）。",
 "倦怠与怀疑（通说待核）。",
 "与《河童》同年的精神轨迹（B109 语境）。"],
"influence":[{"text":"Britannica：35岁自杀震惊文坛（B109）。","source":"B109"},{"text":"Britannica：后期自传性转向（B109）。","source":"B109"}],
"reading":{"difficulties":["断章体（无连续情节）。","大正—昭和初的文坛语境。"],
 "editions":["《一个傻瓜的一生》中译本（人民文学/上海译文等——通说待核）。","日文原版（公有领域状态待核）。"],
 "order":"芥川绝笔期；与《河童》连读。"},
"pending":["篇名写法（或阿呆的一生）核对。","1927年发表（《文艺春秋》后说）待核。","断章数量核对（通说）。"],
"sources":["B109"],"year_source":"B109","author_source":"B109","related_works":["hetong","luoshengmen","renshijian"],
"svg":G("《一个傻瓜的一生》断章图",[{"title":"断章","text":"一生的清点（通说）","color":"main"},{"title":"自传","text":"晚期的转向（B109）","color":"gold"},{"title":"倦怠","text":"怀疑的目光（通说）","color":"antagonist"},{"title":"1927","text":"绝笔之年（B109）","color":"family"}])},
# 4. 巴尔扎克《贝姨》(B039)
{"id":"beiyi","title":"贝姨","original_title":"La Cousine Bette","region":"法国","era":"近代","era_detail":"19世纪40年代",
"genre":"长篇小说","genre_group":"小说","language":"法语","author_id":"balzac","author_name":"奥诺雷·德·巴尔扎克",
"year_display":"1846年（作者页 B039 注记：后期巨著——出版年通说待核）","year_sort":1846,
"background":["作者页（B039）注记：《幻灭（1837—43）、贝姨（1846）》——'后期巨著（Britannica）'。","Britannica（B039）：'《人间喜剧》约90部、人物复现法'——本作属后期。","Britannica（B039）：'偏执狂'人物塑造论——贝姨的嫉妒为经典例（通说待核）。"],
"outline":["（通说待核——B039未载剧情）贝姨的隐秘复仇：嫉妒如何拆毁一个家族。","（通说待核）瓦莱里与于洛家的欲望链条。"],
"characters":[{"name":"贝特（贝姨）","identity":"乡下表姐","note":"（通说待核，B039未载）"},{"name":"于洛男爵","identity":"浪荡子","note":"（通说待核，B039未载）"}],
"themes":["嫉妒的毁灭性（B039：'偏执狂'人物论——通说待核）。",
 "七月王朝的堕落（通说待核）。",
 "《人间喜剧》的人物复现（B039）。"],
"influence":[{"text":"Britannica：'公认史上最伟大小说家之一'（B039 作者级）。","source":"B039"},{"text":"Britannica：《人间喜剧》体系（B039）。","source":"B039"}],
"reading":{"difficulties":["七月王朝巴黎社会。","人物复现的前情（《高老头》等）。"],
 "editions":["《贝姨》中译本（人民文学/上海译文等——通说待核）。","法文原版（公有领域）。"],
 "order":"巴尔扎克后期首选；与《欧也妮·葛朗台》对读。"},
"pending":["1846年出版细节核对（通说）。","贝特/于洛/瓦莱里人名核对（B039未载）。","'偏执狂'论与贝姨的关系待核。"],
"sources":["B039"],"year_source":"B039","author_source":"B039","related_works":["gaolaotou","ouyeni","mengya"],
"svg":G("《贝姨》嫉妒复仇图",[{"title":"贝姨","text":"隐秘的复仇（通说）","color":"main"},{"title":"嫉妒","text":"毁灭的引擎（B039语境）","color":"antagonist"},{"title":"于洛家","text":"欲望的链条（通说）","color":"family"},{"title":"复现","text":"《人间喜剧》网络（B039）","color":"gold"}])},
]
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (title/id dup):', w['id'], w['title'])
        continue
    pathlib.Path(f"data/works/{w['id']}.json").write_text(json.dumps(w, ensure_ascii=False, indent=2), encoding='utf-8')
    print('work', w['id'])

def link(aid, wid, kw=None):
    p = pathlib.Path(f'data/authors/{aid}.json')
    j = json.loads(p.read_text(encoding='utf-8'))
    if not any(m.get('work_id') == wid for m in j['major_works']):
        done = False
        if kw:
            for i, m in enumerate(j['major_works']):
                if m.get('title') and kw in m['title']:
                    j['major_works'][i] = {"work_id": wid, "note": m['note']}
                    done = True; break
        if not done:
            j['major_works'].append({"work_id": wid, "note": "（零成本批34）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

link('baudelaire', 'balideyouyu', '巴黎的忧郁')
link('barnes', 'shizhangshijieshi', '10 1/2章')
link('akutagawa', 'yigeshaguadeyisheng', '一个傻瓜的一生')
link('balzac', 'beiyi', '贝姨')
print('BATCH34 DONE')
