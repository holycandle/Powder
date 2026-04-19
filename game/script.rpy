# 角色初始化 #
define narrator_nvl = Character(None, kind = nvl) 
define mc = Character("小黄", color="#ffcc00")
define f1 = Character("顺子", color="#2f8451")
define f2 = Character("江帅", color="#ff453e")
define cold = Character("冷哥", color="#0080ff")

# 图像资源 #
image bg bar_night1 = "images/bg/bg_bar_night1.webp"
image bg class_small_none1 = "images/bg/bg_class_small_none1.jpg"
image bg campus_road_wet1 = "images/bg/bg_campus_road_wet1.jpg"
image bg campus_road_sunny1 = "images/bg/bg_campus_road_sunny1.jpg"
image bg campus_road_sunny2 = "images/bg/bg_campus_road_sunny2.jpg"
image bg dorm_corridor_sunlight1 = "images/bg/bg_dorm_corridor_sunlight1.jpg"
image bg book1 = "images/bg/bg_book1.jpg"
image bg campus_building1 = "images/bg/bg_campus_building1.jpg"
image bg campus_building2 = "images/bg/bg_campus_building2.jpg"
image bg announcement1 = "images/bg/bg_announcement1.jpg"
image bg class_outside1 = "images/bg/bg_class_outside1.jpg"
image bg playground1 = "images/bg/bg_playground1.jpg"

# 角色立绘位置 #
transform center:          # 默认居中
    xalign 0.5

transform left:            # 左侧（留出足够对话空间）
    xalign 0.15

transform right:           # 右侧（留出足够对话空间）
    xalign 0.85

transform left_far:        # 更靠左（需要更宽松构图时使用）
    xalign 0.05

transform right_far:       # 更靠右
    xalign 0.95

# 角色立绘资源 #
image Jiangshuai ciallo1:
    "images/char/Jiangshuai_ciallo1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.45

image Jiangshuai ciallo2:
    "images/char/Jiangshuai_ciallo2.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.45

image Jiangshuai handsOnHips1:
    "images/char/Jiangshuai_handsOnHips1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.8

image Jiangshuai shrug1:
    "images/char/Jiangshuai_shrug1.png"
    xanchor 0.5 
    yanchor 0.65
    xpos 0.3 
    ypos 1.0
    zoom 0.45

image Jiangshuai scratchHead1:
    "images/char/Jiangshuai_scratchHead1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.8

image Zhiyuan crossArms1:
    "images/char/Zhiyuan_crossArms1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.45

image Zhiyuan handsOnHips1:
    "images/char/Zhiyuan_handsOnHips1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.5

image Zhiyuan rubChin1:
    "images/char/Zhiyuan_rubChin1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5
    ypos 1.0
    zoom 0.45

image Zhiyuan towerHands1:
    "images/char/Zhiyuan_towerHands1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.4

image Zishun crossArms1:
    "images/char/Zishun_crossArms1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.5

image Zishun lookUp1:
    "images/char/Zishun_lookUp1.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.8

image Zishun rubChin1:
    "images/char/Zishun_rubChin1.png"
    xanchor 0.5 
    yanchor 0.65
    xpos 0.5
    ypos 1.0
    zoom 0.5

image Zishun supportFrame1:
    "images/char/Zishun_supportFrame1.png"
    xanchor 0.5 
    yanchor 0.75
    xpos 0.5 
    ypos 1.0
    zoom 0.45

# 游戏开始 #
label start:
    # --- 开场：解离感强烈的 NVL 模式 ---
    window hide
    # 【播放心跳声及重低音效】
    narrator_nvl "疼{w=0.4}"
    narrator_nvl "像一把烧红的碎玻璃，顺着鼻子直接扎进脑子{w=0.5}"
    narrator_nvl "眼球发胀，那种工业漂白粉的味道呛得人想吐{w=0.5}"
    narrator_nvl "但这股极苦的铁锈感后面……{w=0.3}是前所未有的清醒{w=0.5}"
    nvl clear
    
    narrator_nvl "保持冷静{w=0.4}"
    narrator_nvl "这是哪里 我来做什么{w=0.5}"
    narrator_nvl "仔细回想——{w=0.5}"
    narrator_nvl "那个号码是——{w=0.5}"
    nvl clear
    # --- 强力转场：利用签到码作为现实锚点 ---
    # 【音效：粉笔断裂声 + 手机急促震动】
    with hpunch # 画面剧烈摇晃
    f1 "「小黄，别睡了！签到码要过期了，快签到」"

    # --- 回到正常叙事（ADV模式） ---
    # --- 第一幕：下课 ---
    window show

    scene bg book1 with dissolve
    scene bg class_small_none1 with dissolve
    mc "「签到！签到码是……0721」"
    mc "「啊，签上了……」"
    "糟糕糟糕，怎么睡着了，资料都被口水浸透了"
    "手心全是冷汗。感觉黑板上的字在融化"

    show Zishun supportFrame1 with dissolve
    f1 "「昨晚没睡好吗？」"
    mc "「唉，昨晚找那个 Bug 找了大半夜，最后发现是分号打成中文字符了，受不了了」"
    
    show Zishun rubChin1 with dissolve
    f1 "「嘿嘿，那很难受了」"
    f1 "「不过你这么拼，期末绩点不冲个 4.5 说不过去」"

    mc "「4.5 真的能改变什么吗……」"
    mc "「我只是受不了……这种每天都像死循环的日子」"

    show Zishun supportFrame1 with dissolve
    f1 "「我们大学生都是这样的，别想那么多了。走吧」"

    mc "「不对不对。怎么能都是这样？生活需要激情，爷们需要战斗！」"
    "感受到了异样的目光，好像说得太大声了"

    show Zishun crossArms1 with dissolve
    f1 "「emmm，我承认你刚刚抢签到的样子是挺激情的啦」"

    mc "「不和你说那么多了，吃饭去！」"
    
    scene bg campus_building2 with dissolve
    scene bg_campus_road_sunny2 with dissolve
    "每天都在走同样的路，看到同样的风景，听到同样的声音"
    "去年的这个暑假，我对大学生活的幻想还充满绮丽的色彩和无限的可能"
    "但是，蓝鲸大学与我的高中真的有什么差别吗？"
    "一旦新鲜感散去，就发现大学生活过是高中生活的一个升级版，甚至是一个更无聊的版本"
    "对大学的生活越来越熟悉，对未来的道路却越来越陌生了"

# --- 第二幕：食堂聚餐与来自冷哥的邀请 ----------------------------------------------------------------------------------------
    #scene bg canteen with fade
    #（背景音：嘈杂的食堂人声，餐盘碰撞声）
    show Zishun crossArms1 at right with dissolve
    f1 "「小黄，你最近是不是在跟冷哥搞什么项目？看你整天神神秘秘的」"

    mc "「啊？没有啊，就是偶尔聊聊天。冷哥说可以给我一些职业规划的建议」"

    show Jiangshuai ciallo2 at left with dissolve
    f2 "「ciallo~冷哥？就是那个已经拿到大厂offer的冷峻？」"
    f2 "「小黄你路子这么野？这种大佬你都认识」"

    show Zishun rubChin1 at right with dissolve
    f1 "「确实，冷哥是真厉害。大二就把竞赛大奖拿了个遍，大三直接进大厂实习」"
    f1 "「听说他现在已经在带项目了，工资比我们辅导员都高」"

    mc "「是啊，他说当年大一的时候也很迷茫，所以现在想多帮帮我们这些后辈」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「诶，他有没有说具体怎么帮你？」"

    mc "「他说有机会可以引荐一些圈子里的人认识，说大学不能只读书，要拓展人脉」"

    show Zishun crossArms1 at right with dissolve
    f1 "「这话倒是不假。冷哥肯定不只是靠成绩才成功的」"

    "手机突然震动了一下。"

    mc "「嗯？冷哥的消息……」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你这个学长也太殷勤了。吃饭都忘不掉你」"

    mc "「他说……今晚有个局，希望我过去」"

    show Zishun supportFrame1 at right with dissolve
    f1 "「今晚？什么局？」"

    mc "「他说是经验分享会，认识几个创业的前辈。地点在……」"
    mc "「Powder Bar。晚上十一点」"

    f1 "「十一点？还在酒吧？」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「我去，冷哥的局都这么硬核的吗？半夜去酒吧听分享会？」"

    mc "「确实有点为难。你们觉得要去吗？」"

    show Zishun crossArms1 at right with dissolve
    f1 "「我说不去」"

    mc "「嗯？为啥不去」"

    f1 "「不知道，心里没底」"

    show Jiangshuai crossArms1 at left with dissolve    
    f2 "「我说去」"
    
    f1 "「为啥去呢？」"

    f2 "「为啥不去呢？」"

    show Zishun lookUp1 at right with dissolve
    f1 "「刚才不说了吗？心里没底」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你别光说没底，你说不去有啥好处啊」"
    show Jiangshuai ciallo1 at left
    f2 "「你说不去，我还想让小黄带我一个呢」"

    show Zishun supportFrame1 at right with dissolve
    f1 "「那你倒是说，去有啥好处？」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你就倒是说，去有啥坏处吧」"

    f1 "「正经分享会谁约在半夜？正经前辈谁约在酒吧？」"
    f1 "「他要是真有心帮你，为什么不能约在下午的咖啡厅？非要半夜？」"

    show Jiangshuai handsOnHips1 at left with dissolve
    f2 "「这是高端分享会，不是小情侣约会。繁忙的大佬都是深夜才挤得出时间」"
    f2 "「冷哥什么人？大厂offer、竞赛大奖、项目带飞」"
    f2 "「冷哥一句话，顶你吭哧吭哧学半年。他愿意带你进圈子，多少人求都求不来」"
    show Jiangshuai ciallo2 at left with dissolve
    f2 "「酒吧怎么了？985 985，就是要在酒吧舞啊」"

    show Zishun rubChin1 at right with dissolve
    f1 "「……」"
    f1 "「这事儿我们说也没用，看小黄自己吧」"
    
    mc "「我想……」"
    "去不去？"
    "自从在学生会的活动中相识，冷哥一直是一个值得信赖的前辈"
    "国奖颁奖台上的他、给我递微积分资料的他、深夜给我指导的他"
    "冷哥好像总是在我的低谷出现，让快烂掉的我又看到了方向"
    "可是11点……真的可以吗？回来还要报备"
    "所以……"
    mc "「先吃饭吧」"

    show Jiangshuai_shrug1 at left with dissolve
    f2 "「唉！」"

# --- 第三幕：化粪池爆炸与决心赴约 ----------------------------------------------------------------------------------------
    #scene bg campus_road_night
    "啊~~~"
    "从图书馆出来，情不自禁地伸了个懒腰"
    "对了，冷哥消息还没回"
    "已经十点多了吗……"
    "校园里已经没什么人了，路灯下偶尔有几个夜归的学生"
    "11点果然还是太晚了，而且还在酒吧，感觉不太安全"
    "还是拒绝吧！"
    #电话声
    "蒋帅？这时候打电话干什么，要我带泡面吗？"
    mc "「喂，蒋帅？怎么了？」"

    f2 "「报告寝室长，大事不妙了！」"

    mc "「到底咋了？」"

    f2 "「那个……我有个好消息，和一个坏消息。你想先听哪一个？」"

    mc "「别废话了。直接说坏消息吧」"

    f2 "「哦，我们寝室化粪池炸了」"

    mc "「什么……玩意？」"

    f2 "「化粪池炸了」"

    mc "「这还能有好消息吗！？」"

    f2 "「好消息就是我们俩都逃生了，你就放心吧！就是你在阳台上挂的衣服……呵呵，我们没有抢救成功」"

    mc "「根本就没想抢救吧！」"

    f2 "「怎么说呢……总之阿姨让我们今晚尽量别回寝室了，学校现在在安排住宿。不过回来也睡不了，粪围感太强了」"

    mc "「行，我知道了……」"
    "受不了了"
    "这学校还能住一点吗？"
    "明明正打算洗个澡爬上床结束这疲惫的一天，结果现在无家可归"
    "呆呆站在原地，大脑一片空白"
    "要去哪里？"
    "一旦计划被打乱，迷茫与焦虑就会爬上大脑"
    "不对不对。保持冷静，不要慌张"

    $ goToBar = 0
    while goToBar == 0:
        menu:
            "所以，要去哪里？"
            "图书馆":
                "图书馆吗？不行，走回头路不是我的风格"
            "寝室":
                "回寝室吗？很有胆量的选择啊"
                "泰戈尔说什么来着，生活以痛吻我，我要报之以歌"
                "不过生活拿粪投我，我还是稍微避避吧……"
            "Powder Bar":
                $ goToBar = 1

    "对了，去分享会！"
    # 电话铃声
    mc "「喂，冷哥，那个分享会还在吗……」"

    cold "「小黄！当然在啊！」"
    cold "「我已经在包间了！Powder Bar二楼，门口有人接你」"
    cold "「前辈们都等着呢，别紧张，就当来喝杯饮料聊聊天{w=0.3}哈哈」"

    mc "「Okay，我马上过去」"
    scene black with dissolve          # 先清空所有背景，淡入纯黑
    window hide
    narrator_nvl "其实这辈子还没去过酒吧，有点紧张……"
    narrator_nvl "但是，喜欢这份紧张"
    narrator_nvl "探索未知前的那股心灵盲动，总是比那些未知本身让我着迷"
    narrator_nvl "顾虑太多会让行动变得沉重"
    narrator_nvl "更何况，冷哥这次分享会的含金量看来确实很高"
    narrator_nvl "感谢化粪池，让我有了一个冒险的理由"
    window show
    
# ---  第四幕：酒吧分享会 ----------------------------------------------------------------------------------------
    "打了个滴，不久就到了Powder Bar"
    scene bg bar_night1 with hpunch
    "葡萄美酒夜光杯，冷哥的局果然不一般"
    "烟味、酒味、笑声混在一起"
    "昏黄灯光摇曳，晃得人眼睛发酸，可能因为平时在寝室都不开灯"

    show Zhiyuan towerHands1 with dissolve
    cold "小黄！这边！快坐我旁边！"
    mc "冷哥……不好意思，我来晚了。"
    cold "不晚不晚！正好赶上分享高潮！"

    # 快速介绍（保持节奏）
    cold "来，我给你介绍——"
    cold "这位是做AI创业的张总，那位是字节跳动前产品经理。"

    "大家笑着点头。"
    "第一次参加这种局，不知道说什么好，手指不自觉握紧了杯子"
    "除了冷哥还有几个不认识的人，看头发像摸爬滚打多年的程序员"
    "资源触达……赛道红利……人脉即杠杆——大佬们的词汇，顺着平滑的大脑表面，一滴一滴滑过去……"
    "听得很清楚，却什么也没留下来。{w=0.3}悟了一点，又好像完全没悟"

    scene black with dissolve
    scene bg bar_night1

    show Zhiyuan handsOnHips1 with dissolve
    cold "小黄，你有潜力！"
    cold "来，干一杯！"

    "冷哥拿着那瓶开着的酒，要给我倒酒。不过那瓶酒刚才是不是都没人动过？"
    "他举着杯，眼里柔和了昏黄灯光，闪过一丝异样眼神"
    "突然觉得有点不舒服"
    "说起来，刚进来就有点头痛，是酒精的原因吗？"
    "可能还是昨晚没睡好，感觉今天一天都怪怪的"

    mc "谢谢冷哥，我喝这个"

    "拿了另一瓶鸡尾酒，倒在酒杯里"
    "陌生场合不要轻易接受陌生人的饮料，尤其是酒精饮料，这个道理还是懂的"
    "冷哥可以放心，但这不舒服的环境让人放心不了"
    "更何况，今天这状态也不想喝酒……"
    
    menu:
        "真的要喝吗？"
        "先喝一口意思意思一下":
            jump badEnd
        "不安全，还是不喝了":
            jump trueEnd
    return

label badEnd:
    mc "「冷哥，干杯！」"

    "抿了一小口"
    "酒液带着一丝奇怪的甜味，先是顺着舌尖滑下去，然后忽然在喉咙里炸开"
    "头皮有点发麻，冷哥的话也听不到了"
    "胃里瞬间升起一股热流，像掺了铁锈的牛奶，想吐又吐不出来"
    "但这股极苦的铁锈感后面……{w=0.3}是前所未有的清醒"
    "我来这干嘛来着？……"

    scene black with dissolve
    scene bg bar_night1 with Dissolve(2.0)

    mc "「冷哥，这啥酒啊？是不是有点问题？……」"
    mc "「怎么感觉自己轻飘飘的……」"
    mc "「WOC，这酒里面有东西」"

    show Zhiyuan rubChin1 with dissolve
    cold "「哎别急，刚刚啊，我只是在杯壁抹了一丁点」"
    cold "「但是如果，直接吸进去的话你就觉得……人就非常开心」"

    mc "「抹什么？吸什么？」"
    mc "「冷哥，你……」"
    
    "已经语无伦次了，只能感觉到背上冒出一阵冷汗，夹杂着溢出的快感"
    "冷哥拆开一个纸包，露出白色的粉末"

    show Zhiyuan handsOnHips1 with dissolve
    cold "「来，你先粘点在嘴巴上，尝一下味道」"
    cold "「以后再慢慢教你这些」"
    
    "冷哥把沾了粉末的手指伸来"
    "后退的力气都没了"
    "这种全身融化的感觉……确实很舒服，真不想从里面出来"
    menu:
        "要再试一下吗"
        "再试一下":
            "我又抿了一口。"
            "这次甜味更明显，像糖浆一样裹住舌头。"
            "视线边缘开始发软，灯光变得更暖。"
            "心跳好像比刚才快了一点。"
        "再试一下":
            "我又抿了一口。"
            "这次甜味更明显，像糖浆一样裹住舌头。"
            "视线边缘开始发软，灯光变得更暖。"
            "心跳好像比刚才快了一点。"
        "再试一下":
            "我又抿了一口。"
            "这次甜味更明显，像糖浆一样裹住舌头。"
            "视线边缘开始发软，灯光变得更暖。"
            "心跳好像比刚才快了一点。"    

    show Zhiyuan crossArms1 with dissolve
    cold "对，粘点在牙齿边边上"
    cold "吸气"
    
    mc "「WOC爽」"
    
    cold "「以后你就跟着我，我这有的是现货。你放心，平时搞点儿，不会影响学习」"
    "摊在沙发上，任由眼前的场景随着视线流动，放大，变幻"
    "已经听不清冷哥说啥了，也听不了，看不了，思考不了"
    "就这样摊一辈子吧"

# ---  第五幕：寝室 ----------------------------------------------------------------------------------------
    #scene bg dorm_inside1 with fade
    f2 "小黄，昨晚打电话咋没接啊？我们住校内的宾馆，那条件比寝室好多了"
    
    mc "昨晚……去分享会了"
    
    f2 "分享会？你果然去分享会了！好啊，开小灶不带上我"

    f1 "没出什么事吧？感觉你状态不太好"

    mc "没有没有……就是没睡够……"

    f2 "跟着冷哥能有啥事了？肯定是在冷哥家深夜交心了。小黄，苟富贵，莫相忘！"

    mc "呵呵呵……"

    #scene bg dorm_inside2_black with dissolve

    "不知道怎么回的寝室"
    "昨晚的事就当做一场梦吧"
    "可是手里已经不自觉掏出了“电子烟”"
    "说是电子烟，其实是掺杂了合成大麻素的上头电子烟"
    "冷哥说，这个东西对身体没什么伤害，偶尔抽抽放松一下还是可以的"
    "其实我知道，这是毒品，不该碰"
    "但是现在全身的骨头感觉在被针刺。每动一下，那些针就在肉里搅动，又痒又痛，想挠又挠不到"
    "只有手里的东西可以缓解"
    "怎么办？他们都睡了，动静也不会太大"
    "再不抽就要死了"
    "没关系……就一口……没事……"
    
# ---  第六幕：和顺子一起校园跑 ----------------------------------------------------------------------------------------
    #模糊摇晃的画面
    scene bg playground1 with hpunch
    f1 "「小黄，你身体还好吗？看你摇摇晃晃的，要不今天别跑了吧」"
    
    mc "「没事没事」"
    
    mc "「顺子，你等等我……」"

    f1 "「怎么又停了？都8分配了」"

    mc "「对不起……我……最近状态不太好」"

    f1 "「我拉你起来。我去，你心率都200了……别跑了，再跑要猝死了！」"

    "怎么办……身子完全垮了"
    "感觉自己脚上拖了两个哑铃一样沉重"
    "跑道像液体一样起伏，世界是个巨大的像素RPG……"
    "明明才两圈"
# ---  第七幕：和冷哥通话----------------------------------------------------------------------------------------
    scene bg campus_outside1 with dissolve
    "现在这个点，这里没有什么人"
    "那次'分享会'后，我再也没有联系过冷哥。之前他给我打过一次电话，我没接"
    "我不知道是不想接还是不敢接。我似乎还在逃避那一晚的真实经历——一想起那夜的霓虹灯就反胃"
    "可是，为什么我又在这里呢？为什么我又约冷哥在这里见面了？"
    "电子烟已经吸完了，还是没忍住……能再带来这样东西的人，只有他"

    cold "「小黄，来这么早啊」"
    show Zhiyuan handsOnHips1 with dissolve
    
    mc "「早上好」"

    show Zhiyuan crossArms1 with dissolve
    cold "「给你打电话也不接，学长我也会担心的。看你变得这么憔悴」"
    cold "「货已经没了，是不是」"
    show Zhiyuan rubChin1 with dissolve
    cold "「还是很想要吧？」"

    mc "「……」"

    show Zhiyuan crossArms1 with dissolve
    cold "「废话也不说了，看看这个吧」" 

    #scene bg drug_choclote with dissolve
    mc "「巧克力？」"

    cold "「嘿嘿，这可比巧克力刺激多了」"
    cold "「电子烟平时不方便吧？换成巧克力就不会有人起疑了」"

    mc "「冷哥，你真为我着想」"
     
    cold "「嘿嘿，咱们亲兄弟，明算账。一片500」"

    mc "「你那时候在酒吧明明说是免费的？！」"

    cold "「酒吧里倒是免费的没错。但你出了新手村还想领新手福利吗？」"
    cold "「为了这批货，我可损失了几个兄弟」"

    mc "「你这不都是涨价套路么」"

    cold "「一分钱一分货。你以为你那点电子烟就已经是极致体验了吗？too young too simple」"
    cold "「这玩意可没那么简单。刚接触的人，先是鼻吸，吸收率只有20%」"
    cold "「等你再吸几次，鼻吸就满足不了你，到时候你就会去烫吸，让热雾化的D品通过鼻腔快速吸入肺部。顺着毛细血管进入血液循环"
    cold "「还没完呢，烫吸的吸收率也没到一半，你迟早会觉得不够。这时候，你就要去注射」"
    cold "「没点人引路，你就只能自己摸索，那可就危险了，你会往胳膊上、腿上等四肢的每一寸皮肤下死手，看着它们慢慢坏死」"
    cold "「等每一寸皮肤都坏死，就只有一个地方可以注射了」"

    mc "「哪……哪里？」"

    cold "「脖子」"
    cold "「这叫作“开天窗”。吸D的最后阶段。等那时候，你就知道什么叫飞升极乐世界了！」"

    cold "「我能告诉你这么多，也不怕你不吸」"
    cold "「谁不知道这玩意不好？意志力在D瘾面前算个屁！哼哼」"


# ---  第八幕：和江帅一起吃饭 ---------------------------------------------------------------------------------------------------
    f2 "「小黄，今天吃这么少？有心事啊」"
    mc "「啊……没……什么，我不怎么饿」"

    "味同嚼蜡，难以下咽"
    "正常美食能带来50% - 100%的多巴胺提升，但是毒品带来的多巴胺提升可能是正常食物的数十倍甚至上百倍"
    "加上电子烟抽多了，唾液分泌减少，口干舌燥"
    "感觉自己像一头在农场里吃草的牛"
    
    f2 "「听说最近缉毒警察要来我们学校了」"
    
    mc "「什么？！你怎么知道的」"
    
    f2 "「下周一的讲座啊！你怎么大惊小怪的」"

    mc "「只做讲座吗？」"

    f2 "「我又不是缉毒警察，我哪知道」"
    f2 "「话说你最近不看手机的吗？前几天微信上突然找我借钱，我以为啥急事就给你打了，你领的倒挺快。问你啥事你又不吱声了」"
    f2 "「你要不用手机了就给我，我去帮你换俩不锈钢脸盆。你一个我一个」"

    mc "「……」"

    "原来我还找江帅借过钱，我究竟还做了什么事……不行，想不起来"
    "这不就跟被夺舍了一样吗……"
    "话说江帅是不是已经知道我的事了，感觉他刚才说话的眼神有点怪怪的"
    "旁敲侧击非君子所为，直言不讳乃丈夫作风"
    "江帅这人，不是君子，也不是丈夫，但也不像是能看出什么端倪的人"
    "还是小心点比较好……"

    f2 "「小黄，感觉你最近疑神疑鬼的啊」"
# ---  第九幕：突击查寝 ---------------------------------------------------------------------------------------------------
    #scene bg dorm_ceiling1 with fade
    #闹铃声
    
    return


label trueEnd:

    return
