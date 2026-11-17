# PROGRESS — 中外文学名著导读库

任务状态：**IN_PROGRESS**（无人值守模式；不确定处选保守方案并记入 DECISIONS.md）

## 目标
静态网站"中外文学名著导读库"：60 部作品（中外各 30），作品页固定 8 节结构、作家页、每部 1 张 SVG、总览页（筛选）、作家索引、文学史时间线。

## 阶段状态

- [x] 阶段0 初始化：目录骨架、works_list.md、git init —— 完成
- [x] 阶段1 来源库：sources.json **99 条、98 条 verified**（Britannica 为主，辅以英文维基、央视/求是/人民网/中国作家网/中新网/书格等；每条均实际打开页面核对）—— 完成（2026-11-18）
- [x] 阶段2 校验工具：tools/check.py + build.py + svggen.py 全部通过（2026-11-18）
- [ ] 阶段3 内容：60 部作品页 + 作家页 + SVG，**每部完成后 git 提交**（进度明细见下）——已完成 40/60：中国 30 部全部完成；外国已完成 iliad(+homer)、odyssey、yisuo(+aesop)、oedipus(+sophocles)、shenqu(+dante)、shiritan(+boccaccio)、kantebolei(+chaucer)、hamlet(+shakespeare)、tangjihede(+cervantes)、geliefo(+swift)
- [ ] 阶段4 聚合页：作品总览（国别/时代/体裁筛选）、作家索引、时间线、导航、REPORT.md

## 阶段3 进度明细（每完成一部在此打勾并提交）

### 中国（30）
- [ ] 1 shijing 诗经
- [ ] 2 chuci 楚辞（离骚）
- [ ] 3 lunyu 论语
- [ ] 4 zhuangzi 庄子
- [ ] 5 shiji 史记
- [ ] 6 tangshi300 唐诗三百首
- [ ] 7 songci300 宋词三百首
- [ ] 8 doueyuan 窦娥冤
- [ ] 9 xixiangji 西厢记
- [ ] 10 mudanting 牡丹亭
- [ ] 11 sanguo 三国演义
- [ ] 12 shuihu 水浒传
- [ ] 13 xiyouji 西游记
- [ ] 14 liaozhai 聊斋志异
- [ ] 15 rulin 儒林外史
- [ ] 16 honglou 红楼梦
- [ ] 17 laocan 老残游记
- [ ] 18 nahan 呐喊
- [ ] 19 ziye 子夜
- [ ] 20 jia 家
- [ ] 21 luotuo 骆驼祥子
- [ ] 22 leiyu 雷雨
- [ ] 23 biancheng 边城
- [ ] 24 weicheng 围城
- [ ] 25 aiqing 艾青诗选
- [ ] 26 pingfan 平凡的世界
- [ ] 27 bailuyuan 白鹿原
- [ ] 28 huozhe 活着
- [ ] 29 honggaoliang 红高粱家族
- [ ] 30 santi 三体

### 外国（30）
- [ ] 31 iliad 伊利亚特
- [ ] 32 odyssey 奥德赛
- [ ] 33 yisuo 伊索寓言
- [ ] 34 oedipus 俄狄浦斯王
- [ ] 35 shenqu 神曲
- [ ] 36 shiritan 十日谈
- [ ] 37 kantebolei 坎特伯雷故事
- [ ] 38 hamlet 哈姆雷特
- [ ] 39 tangjihede 堂吉诃德
- [ ] 40 geliefo 格列佛游记
- [ ] 41 fushide 浮士德
- [ ] 42 aoman 傲慢与偏见
- [ ] 43 hongyuhei 红与黑
- [ ] 44 gaolaotou 高老头
- [ ] 45 balimingwuyuan 巴黎圣母院
- [ ] 46 beican 悲惨世界
- [ ] 47 baofali 包法利夫人
- [ ] 48 zuiyufa 罪与罚
- [ ] 49 zhanzheng 战争与和平
- [ ] 50 wanou 玩偶之家
- [ ] 51 hakebei 哈克贝利·费恩历险记
- [ ] 52 mauposangxuan 莫泊桑短篇小说选
- [ ] 53 qikefuxuan 契诃夫短篇小说选
- [ ] 54 waerdenghu 瓦尔登湖
- [ ] 55 bianxingji 变形记
- [ ] 56 gaicibi 了不起的盖茨比
- [ ] 57 laorenhai 老人与海
- [ ] 58 yijiubasi 一九八四
- [ ] 59 bainian 百年孤独
- [ ] 60 xueguo 雪国

## 规则备忘（硬性）
- 不编造出版年份、人名、情节细节、评论引文；查不到 → 作品页"待核实"节。
- 引文 ≤2 句并标版本；现代译本有版权，不大段搬用。
- 情节概括到"读者需要的程度"，不逐章复述。
- 评价写明是谁的观点；争议列各方说法。
- 同一问题连续失败 3 次 → 记入 BLOCKERS.md 并跳过。

## 收尾
全部阶段完成后：本文件写 `ALL_DONE`。
