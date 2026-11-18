# PROGRESS — 中外文学名著导读库

任务状态：**ALL_DONE**（无人值守模式；不确定处选保守方案并记入 DECISIONS.md）

> **v3 状态（2026-11-19）**：v1（60 部）→ v2（101 部）→ **v3 完成：175 部作品 / 139 位作家 / 216 条来源（215 verified）/ 25 国家地区；check 全部通过；已提交并推送 GitHub。** 以下为 v1 阶段明细（历史存档）。

## 目标
静态网站"中外文学名著导读库"：60 部作品（中外各 30），作品页固定 8 节结构、作家页、每部 1 张 SVG、总览页（筛选）、作家索引、文学史时间线。

## 阶段状态

- [x] 阶段0 初始化：目录骨架、works_list.md、git init —— 完成
- [x] 阶段1 来源库：sources.json **99 条、98 条 verified**（Britannica 为主，辅以英文维基、央视/求是/人民网/中国作家网/中新网/书格等；每条均实际打开页面核对）—— 完成（2026-11-18）
- [x] 阶段2 校验工具：tools/check.py + build.py + svggen.py 全部通过（2026-11-18）
- [x] 阶段3 内容：60 部作品页 + 55 篇作家页 + 60 张 SVG，逐部 git 提交（46 次提交）——全部完成：中国 30 部全部完成；外国已完成 iliad(+homer)、odyssey、yisuo(+aesop)、oedipus(+sophocles)、shenqu(+dante)、shiritan(+boccaccio)、kantebolei(+chaucer)、hamlet(+shakespeare)、tangjihede(+cervantes)、geliefo(+swift)
- [x] 阶段4 聚合页：作品总览（筛选）、作家索引、时间线、导航、about、REPORT.md —— 完成

## 阶段3 进度明细（每完成一部在此打勾并提交）

### 中国（30）
- [x] 1 shijing 诗经
- [x] 2 chuci 楚辞（离骚）
- [x] 3 lunyu 论语
- [x] 4 zhuangzi 庄子
- [x] 5 shiji 史记
- [x] 6 tangshi300 唐诗三百首
- [x] 7 songci300 宋词三百首
- [x] 8 doueyuan 窦娥冤
- [x] 9 xixiangji 西厢记
- [x] 10 mudanting 牡丹亭
- [x] 11 sanguo 三国演义
- [x] 12 shuihu 水浒传
- [x] 13 xiyouji 西游记
- [x] 14 liaozhai 聊斋志异
- [x] 15 rulin 儒林外史
- [x] 16 honglou 红楼梦
- [x] 17 laocan 老残游记
- [x] 18 nahan 呐喊
- [x] 19 ziye 子夜
- [x] 20 jia 家
- [x] 21 luotuo 骆驼祥子
- [x] 22 leiyu 雷雨
- [x] 23 biancheng 边城
- [x] 24 weicheng 围城
- [x] 25 aiqing 艾青诗选
- [x] 26 pingfan 平凡的世界
- [x] 27 bailuyuan 白鹿原
- [x] 28 huozhe 活着
- [x] 29 honggaoliang 红高粱家族
- [x] 30 santi 三体

### 外国（30）
- [x] 31 iliad 伊利亚特
- [x] 32 odyssey 奥德赛
- [x] 33 yisuo 伊索寓言
- [x] 34 oedipus 俄狄浦斯王
- [x] 35 shenqu 神曲
- [x] 36 shiritan 十日谈
- [x] 37 kantebolei 坎特伯雷故事
- [x] 38 hamlet 哈姆雷特
- [x] 39 tangjihede 堂吉诃德
- [x] 40 geliefo 格列佛游记
- [x] 41 fushide 浮士德
- [x] 42 aoman 傲慢与偏见
- [x] 43 hongyuhei 红与黑
- [x] 44 gaolaotou 高老头
- [x] 45 balimingwuyuan 巴黎圣母院
- [x] 46 beican 悲惨世界
- [x] 47 baofali 包法利夫人
- [x] 48 zuiyufa 罪与罚
- [x] 49 zhanzheng 战争与和平
- [x] 50 wanou 玩偶之家
- [x] 51 hakebei 哈克贝利·费恩历险记
- [x] 52 mauposangxuan 莫泊桑短篇小说选
- [x] 53 qikefuxuan 契诃夫短篇小说选
- [x] 54 waerdenghu 瓦尔登湖
- [x] 55 bianxingji 变形记
- [x] 56 gaicibi 了不起的盖茨比
- [x] 57 laorenhai 老人与海
- [x] 58 yijiubasi 一九八四
- [x] 59 bainian 百年孤独
- [x] 60 xueguo 雪国

## 规则备忘（硬性）
- 不编造出版年份、人名、情节细节、评论引文；查不到 → 作品页"待核实"节。
- 引文 ≤2 句并标版本；现代译本有版权，不大段搬用。
- 情节概括到"读者需要的程度"，不逐章复述。
- 评价写明是谁的观点；争议列各方说法。
- 同一问题连续失败 3 次 → 记入 BLOCKERS.md 并跳过。

## 收尾
**ALL_DONE** —— v1 四阶段于 2026-11-18 完成（60 作品/55 作家/来源100条）；v2 扩充于 2026-11-19 完成（+41 部 → 101 作品/82 作家/130 条来源）；**v3 扩充于 2026-11-19 完成：新增 74 部作品 + 57 位作家 → 总计 175 作品 / 139 作家 / 25 国家地区 / sources.json 216 条（215 verified）/ check 全部通过（0 错误）/ 已提交并推送 GitHub（TianDiHuAng/culture_work）。**
