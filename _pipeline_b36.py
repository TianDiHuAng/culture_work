# -*- coding: utf-8 -*-
"""批36：零成本 7 部二作（B336/B340/B348×2/B350/B130/B137 注记 + 书名查重）"""
import json, pathlib

existing = {p.stem for p in pathlib.Path('data/works').glob('*.json')}
titles = set()
for p in pathlib.Path('data/works').glob('*.json'):
    j = json.loads(p.read_text(encoding='utf-8'))
    titles.add(j['title'])

def G(caption, cards):
    return {"type": "grid", "width": 680, "height": 340, "caption": caption, "cards": cards}

works = [
# 1. 皮兰德娄《恩里科四世》
{"id":"enrikesishi","title":"恩里科四世","original_title":"Enrico IV","region":"意大利","era":"近代","era_detail":"20世纪20年代",
"genre":"戏剧","genre_group":"戏剧","language":"意大利语","author_id":"pirandello","author_name":"路易吉·皮兰德娄",
"year_display":"1922年（Britannica B336：Enrico IV (1922)）","year_sort":1922,
"background":["Britannica（B336）：Enrico IV——'the theme is madness, which lies just under the skin of ordinary life'（主题是疯狂，它就藏在日常生活的表皮之下）。","Britannica（B336）：主人公选择'retirement into unreality in preference to life'（宁愿退入非现实而不愿生活）。","Britannica（B336）：皮兰德娄——1934诺奖；'theatre within the theatre'的发明者。"],
"outline":["（通说待核——B336未载剧情）假扮'恩里科四世'的疯狂者维持疯狂十二年后醒来。","（通说待核）'退入非现实'的选择：清醒者的疯狂辩护。"],
"characters":[{"name":"恩里科四世","identity":"假疯者","note":"（B336 书名人物）"},{"name":"玛蒂尔达","identity":"伯爵夫人","note":"（通说待核，B336未载）"}],
"themes":["疯狂与清醒的倒置（B336：madness...under the skin）。",
 "'退入非现实'的存在选择（B336）。",
 "面具与身份（B336 作者论语系）。"],
"influence":[{"text":"Britannica：'the theme is madness...'（B336）。","source":"B336"},{"text":"Britannica：皮兰德娄1934诺奖（B336）。","source":"B336"}],
"reading":{"difficulties":["疯狂与清醒的辩证。","中世纪扮演的舞台机制。"],
 "editions":["《恩里科四世》中译本（人民文学等——通说待核）。","意大利文原版。"],
 "order":"皮兰德娄进阶；与《六个寻找剧作家的角色》对读。"},
"pending":["剧情细节核对（通说）。","1922年首演细节待核。","玛蒂尔达人名待核。"],
"sources":["B336"],"year_source":"B336","author_source":"B336","related_works":["liugejuesesouzhao","yigewushiwan","leiyu"],
"svg":G("《恩里科四世》面具结构图",[{"title":"假疯","text":"清醒的疯狂（B336）","color":"main"},{"title":"退入非现实","text":"拒绝生活（B336）","color":"gold"},{"title":"宫廷","text":"中世纪的舞台（通说）","color":"family"},{"title":"面具","text":"身份的倒置（B336语境）","color":"antagonist"}])},
# 2. 尤涅斯库《椅子》
{"id":"yizi","title":"椅子","original_title":"Les Chaises","region":"法国","era":"现当代","era_detail":"20世纪50年代初",
"genre":"戏剧","genre_group":"戏剧","language":"法语","author_id":"ionesco","author_name":"欧仁·尤涅斯库",
"year_display":"1952年（Britannica B340：Les Chaises (1952)）","year_sort":1952,
"background":["Britannica（B340）：Les Chaises (1952)——剧作列表（剧情细节通说待核）。","Britannica（B340）：尤涅斯库——'道具的滑稽增殖直至淹没演员'（'humorous multiplication of objects on stage until they overwhelm the actors'）。","Britannica（B340）：其戏剧呈现'the absurdity of bourgeois life, the meaninglessness of social conventions'。"],
"outline":["（通说待核——B340未载剧情）老夫妇向越来越满的'椅子'宣讲世界真相。","（通说待核）椅子的增殖：道具淹没演员（B340）。"],
"characters":[{"name":"老夫妇","identity":"宣讲者","note":"（通说待核，B340未载）"},{"name":"演说家","identity":"哑角","note":"（通说待核，B340未载）"}],
"themes":["道具的增殖美学（B340）。",
 "存在的空转（B340：futile and mechanical nature）。",
 "'缺席的观众'与无人的真理（通说待核）。"],
"influence":[{"text":"Britannica：荒诞派开创者之一（B340）。","source":"B340"},{"text":"Britannica：'道具滑稽增殖'（B340）。","source":"B340"}],
"reading":{"difficulties":["无人物的满台道具调度。","'演说家'的哑剧性（通说待核）。"],
 "editions":["《椅子》中译本（人民文学《荒诞派戏剧集》等——通说待核）。","法文原版。"],
 "order":"尤涅斯库第二作；与《秃头歌女》《犀牛》对读。"},
"pending":["剧情细节核对（通说）。","1952年首演（Théâtre de la Huchette说）待核。","演说家角色细节待核。"],
"sources":["B340"],"year_source":"B340","author_source":"B340","related_works":["toutougeonv","dengdaigou","xiniu"],
"svg":G("《椅子》增殖结构图",[{"title":"椅子","text":"道具的淹没（B340）","color":"antagonist"},{"title":"老夫妇","text":"空转的宣讲（通说）","color":"main"},{"title":"演说家","text":"缺席的真理（通说）","color":"gold"},{"title":"荒诞","text":"意义的失落（B340）","color":"family"}])},
# 3. 莫拉维亚《两个女人》
{"id":"lianggenvren","title":"两个女人","original_title":"La ciociara","region":"意大利","era":"现当代","era_detail":"20世纪50年代",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"moravia","author_name":"阿尔贝托·莫拉维亚",
"year_display":"1957年（Britannica B348：La ciociara (1957; Two Women)）","year_sort":1957,
"background":["Britannica（B348）：La ciociara——'tells of an adaptation to post-World War II Italian life'（讲述对战后意大利生活的适应）。","Britannica（B348）：莫拉维亚——'He was a major figure in 20th-century Italian literature.'。","题材（通说待核）：战争末期的母女流亡——乔恰里亚乡间的逃难与暴力。"],
"outline":["（通说待核——B348未载剧情）母女从罗马逃往乔恰里亚乡间。","（通说待核）战争的暴行与幸存。"],
"characters":[{"name":"切塞拉","identity":"母亲","note":"（通说待核，B348未载）"},{"name":"罗塞塔","identity":"女儿","note":"（通说待核，B348未载）"}],
"themes":["战后的适应（B348：adaptation to post-World War II Italian life）。",
 "战争的性暴力（通说待核）。",
 "母女的保护与错位（通说待核）。"],
"influence":[{"text":"Britannica：'He was a major figure in 20th-century Italian literature.'（B348）。","source":"B348"},{"text":"Britannica：莫拉维亚多部改编为电影（B348 交叉——1960年德西卡电影说待核）。","source":"B348"}],
"reading":{"difficulties":["二战末意大利战线。","'乔恰里亚'地名（原书名 La ciociara）。"],
 "editions":["《两个女人》中译名（《乔恰里亚女人》两说——通说待核）。","意大利文原版。"],
 "order":"莫拉维亚中期首选。"},
"pending":["切塞拉/罗塞塔人名核对（B348未载）。","1960年德西卡电影说待核。","中译名两说待核。"],
"sources":["B348"],"year_source":"B348","author_source":"B348","related_works":["lengmoederen","shuncongzhe","bao"],
"svg":G("《两个女人》逃难结构图",[{"title":"母女","text":"战时的逃亡（通说）","color":"main"},{"title":"乔恰里亚","text":"乡间的暴力（通说）","color":"antagonist"},{"title":"战后","text":"生活的适应（B348）","color":"gold"},{"title":"保护","text":"错位的爱（通说）","color":"family"}])},
# 4. 莫拉维亚《烦闷》
{"id":"fanmen","title":"烦闷","original_title":"La noia","region":"意大利","era":"现当代","era_detail":"20世纪60年代初",
"genre":"长篇小说","genre_group":"小说","language":"意大利语","author_id":"moravia","author_name":"阿尔贝托·莫拉维亚",
"year_display":"1960年（Britannica B348：La noia (1960; The Empty Canvas)）","year_sort":1960,
"background":["Britannica（B348）：La noia——'a painter unable to find meaning either in love or work'（一个在爱与工作中都找不到意义的画家）。","Britannica（B348）：莫拉维亚——'known for his fictional portrayals of social alienation'。","题材（通说待核）：画家ino的'烦闷'——存在性无聊与占有式爱情。"],
"outline":["（通说待核——B348未载剧情）画家的空白画布：创作与欲望的双重瘫痪。","（通说待核）与塞西莉亚的关系：占有的测试。"],
"characters":[{"name":"画家（诺伊说）","identity":"主人公","note":"（通说待核，B348未载）"},{"name":"塞西莉亚","identity":"少女","note":"（通说待核，B348未载）"}],
"themes":["烦闷作为存在状况（B348：unable to find meaning）。",
 "创作力的瘫痪（通说待核）。",
 "占有的失败（通说待核）。"],
"influence":[{"text":"Britannica：'a painter unable to find meaning either in love or work'（B348）。","source":"B348"},{"text":"Britannica：'social alienation'（B348 作者级定位）。","source":"B348"}],
"reading":{"difficulties":["'烦闷'（noia）的哲学界定。","罗马艺术圈背景（通说待核）。"],
 "editions":["《烦闷》中译名（《冷漠的钟点》两说——通说待核）。","意大利文原版。"],
 "order":"莫拉维亚后期首选。"},
"pending":["主人公名核对（B348未载）。","1963年电影改编说待核。","中译名两说待核。"],
"sources":["B348"],"year_source":"B348","author_source":"B348","related_works":["shuncongzhe","lengmoederen","zenodeyishi"],
"svg":G("《烦闷》空白画布图",[{"title":"空白画布","text":"创作的瘫痪（通说）","color":"main"},{"title":"烦闷","text":"noia 的存在状况（B348）","color":"gold"},{"title":"占有","text":"爱的失败（通说）","color":"antagonist"},{"title":"疏离","text":"社会的异化（B348）","color":"family"}])},
# 5. 伯尔《女士及众生相》
{"id":"nvshijizhongshengxiang","title":"女士及众生相","original_title":"Gruppenbild mit Dame","region":"德国","era":"现当代","era_detail":"20世纪70年代初",
"genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"boll","author_name":"海因里希·伯尔",
"year_display":"1971年（Britannica B350：Group Portrait with Lady (1971)——'his longest novel'）","year_sort":1971,
"background":["Britannica（B350）：Group Portrait with Lady——'his longest novel'——'a panorama of German life'（德国生活全景）——通过莱妮·普法伊弗尔周围的人。","Britannica（B350）：伯尔——1972诺奖；'rubble literature'代表；'the eras leading humanist interpreter of Germanys WWII experience'。","题材（通说待核）：以'采访拼贴'还原一个普通女性的一生。"],
"outline":["（通说待核——B350未载剧情）叙述者通过采访莱妮周围的人拼出她的肖像。","（通说待核）莱妮：被社会放逐却坚守人性的女性。"],
"characters":[{"name":"莱妮·普法伊弗尔","identity":"女主人公","note":"（B350：Leni Pfeiffer）"},{"name":"叙述者","identity":"采访者","note":"（通说待核，B350未载）"}],
"themes":["德国生活的全景（B350：a panorama of German life）。",
 "'众生相'的集体叙事（书名语境）。",
 "个人责任与历史（B350：personal responsibility）。"],
"influence":[{"text":"Britannica：1972年诺贝尔文学奖（B350）。","source":"B350"},{"text":"Britannica：'his longest novel'（B350）。","source":"B350"}],
"reading":{"difficulties":["采访拼贴文体。","德国20世纪史（一战至70年代——通说待核）。"],
 "editions":["《女士及众生相》中译名（《以妇女为中心的群像》两说——通说待核）。","德文原版。"],
 "order":"伯尔长篇收官；与《小丑之见》对读。"},
"pending":["莱妮·普法伊弗尔人名核对（B350拼写）。","1971年出版细节待核。","'采访拼贴'结构待核。"],
"sources":["B350"],"year_source":"B350","author_source":"B350","related_works":["xiaochou","katarinabulum","leiyu"],
"svg":G("《女士及众生相》拼贴肖像图",[{"title":"莱妮","text":"肖像的中心（B350）","color":"main"},{"title":"众生","text":"德国生活全景（B350）","color":"family"},{"title":"采访","text":"拼贴的方法（通说）","color":"gold"},{"title":"放逐","text":"社会的偏见（通说）","color":"antagonist"}])},
# 6. 石黑一雄《被掩埋的巨人》
{"id":"beiyanmaidejuren","title":"被掩埋的巨人","original_title":"The Buried Giant","region":"英国","era":"现当代","era_detail":"21世纪10年代",
"genre":"长篇小说","genre_group":"小说","language":"英语","author_id":"ishiguro","author_name":"石黑一雄",
"year_display":"2015年（Britannica B130：被掩埋的巨人 (2015)——'记忆与遗忘'）","year_sort":2015,
"background":["Britannica（B130）：《被掩埋的巨人》(2015)——'记忆与遗忘（Britannica 列举）'。","Britannica（B130）：石黑一雄2017诺奖——'uncovered the abyss beneath our illusory sense of connection with the world'；主题'记忆、悔恨、身份'。","题材（通说待核）：后亚瑟王不列颠——'母龙'的气息使大地遗忘。"],
"outline":["（通说待核——B130未载剧情）老夫妇渡河寻子：集体遗忘之谜。","（通说待核）'巨人的坟墓'：被掩埋的记忆终将醒来。"],
"characters":[{"name":"埃克索/比特丽丝","identity":"老夫妇","note":"（通说待核，B130未载）"}],
"themes":["记忆与遗忘（B130）。",
 "集体创伤的掩埋（通说待核）。",
 "爱的考验（书名语境——通说待核）。"],
"influence":[{"text":"Britannica：2017诺奖（B130）。","source":"B130"},{"text":"Britannica：'记忆、悔恨、身份'主题（B130）。","source":"B130"}],
"reading":{"difficulties":["寓言化的中世纪设定。","记忆伦理的多重声音。"],
 "editions":["《被掩埋的巨人》中译本（上海译文等——通说待核）。","英文原版。"],
 "order":"石黑一雄寓言篇；与《克拉拉与太阳》对读。"},
"pending":["埃克索/比特丽丝人名核对（B130未载）。","2015年出版（Faber说）待核。","'母龙魁瑞格'细节待核。"],
"sources":["B130"],"year_source":"B130","author_source":"B130","related_works":["kelarayutaiyang","leiyu","huoluan"],
"svg":G("《被掩埋的巨人》遗忘结构图",[{"title":"迷雾","text":"大地的遗忘（通说）","color":"antagonist"},{"title":"老夫妇","text":"寻子的旅程（通说）","color":"main"},{"title":"巨人","text":"被掩埋的记忆（B130）","color":"gold"},{"title":"爱","text":"记忆的考验（通说）","color":"family"}])},
# 7. 黑塞《纳尔齐斯与歌尔德蒙》
{"id":"naerqisi","title":"纳尔齐斯与歌尔德蒙","original_title":"Narziss und Goldmund","region":"德国","era":"近代","era_detail":"20世纪30年代初",
"genre":"长篇小说","genre_group":"小说","language":"德语","author_id":"hesse","author_name":"赫尔曼·黑塞",
"year_display":"1930年（Britannica B137：纳尔齐斯与歌尔德蒙 (1930)）","year_sort":1930,
"background":["Britannica（B137）：纳尔齐斯与歌尔德蒙 (1930)——Britannica 列举。","Britannica（B137）：黑塞主题——'个人挣脱既定文明寻找精神自我'。","题材（通说待核）：修道院里的两个朋友——精神与感官的两条道路。"],
"outline":["（通说待核——B137未载剧情）纳尔齐斯的静观之路与歌尔德蒙的流浪之路。","（通说待核）艺术与死亡：歌尔德蒙的木雕与终点。"],
"characters":[{"name":"纳尔齐斯","identity":"修士/理性","note":"（B137 书名人物）"},{"name":"歌尔德蒙","identity":"流浪者/感官","note":"（B137 书名人物）"}],
"themes":["精神与感官的双重道路（通说待核）。",
 "'挣脱既定文明'（B137）。",
 "友谊的镜像结构（书名语境）。"],
"influence":[{"text":"Britannica：1946诺贝尔文学奖（B137）。","source":"B137"},{"text":"Britannica：黑塞代表作序列（B137：《悉达多》《荒原狼》《玻璃球游戏》等）。","source":"B137"}],
"reading":{"difficulties":["中世纪修道院背景。","'双重道路'的哲学结构。"],
 "editions":["《纳尔齐斯与歌尔德蒙》中译名（《纳尔奇斯与歌尔德蒙》）待核。","德文原版。"],
 "order":"黑塞中期首选；与《德米安》对读。"},
"pending":["1930年出版（S. Fischer说）待核。","剧情细节核对（通说）。","译名两说待核。"],
"sources":["B137"],"year_source":"B137","author_source":"B137","related_works":["xinshigudeLieshou","demian","boliuqiuyouxi"],
"svg":G("《纳尔齐斯与歌尔德蒙》双路图",[{"title":"纳尔齐斯","text":"静观之路（B137）","color":"family"},{"title":"歌尔德蒙","text":"流浪之路（B137）","color":"main"},{"title":"友谊","text":"镜像的结构（书名）","color":"gold"},{"title":"艺术","text":"感官的救赎（通说）","color":"antagonist"}])},
]
for w in works:
    if w['id'] in existing or w['title'] in titles:
        print('SKIP (dup):', w['id'], w['title'])
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
            j['major_works'].append({"work_id": wid, "note": "（零成本批36）"})
    p.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding='utf-8')
    print('linked', aid, '->', wid)

# 只有新页才挂链；先确认
created = [w['id'] for w in works if w['id'] not in existing and w['title'] not in titles]
print('created:', created)
if 'enrikesishi' in created: link('pirandello', 'enrikesishi', '恩里科四世')
if 'yizi' in created: link('ionesco', 'yizi', '椅子')
if 'lianggenvren' in created: link('moravia', 'lianggenvren', '两个女人')
if 'fanmen' in created: link('moravia', 'fanmen', '烦闷')
if 'nvshijizhongshengxiang' in created: link('boll', 'nvshijizhongshengxiang', '女士及众生相')
if 'beiyanmaidejuren' in created: link('ishiguro', 'beiyanmaidejuren', '被掩埋的巨人')
if 'naerqisi' in created: link('hesse', 'naerqisi', '纳尔齐斯')
print('BATCH36 DONE')
