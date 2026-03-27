define narrator_nvl = Character(None, kind = nvl) 
define mc = Character("小黄", color="#ffcc00")
define f1 = Character("李正", color="#7c7dbe")
define f2 = Character("尹平", color="#7c7dbe")

# 图像定义保持不变
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

image Huang normal :
    "images/char/Huang_normal.png"
    xanchor 0.5 
    yanchor 0.7
    xpos 0.5 
    ypos 1.0
    zoom 0.8
image Huang thinking :
    "images/char/Huang_thinking.png"
    xanchor 0.5 
    yanchor 0.6 
    xpos 0.5 
    ypos 0.8
    zoom 0.8

label start:
    # --- 开场：解离感强烈的 NVL 模式 ---
    window hide
    # 【播放心跳声及重低音效】
    narrator_nvl "疼。{w=0.4}"
    narrator_nvl "像一把烧红的碎玻璃，顺着鼻子直接扎进脑子。{w=0.5}"
    narrator_nvl "眼球发胀，那种工业漂白粉的味道呛得人想吐。{w=0.5}"
    narrator_nvl "但这股极苦的铁锈感后面……{w=0.3}是前所未有的清醒。{w=0.5}"
    
    nvl clear
    
    narrator_nvl "保持冷静，把杯子放下。{w=0.4}"
    narrator_nvl "这是哪里？我来做什么？{w=0.5}"
    narrator_nvl "仔细回想——{w=0.5}"
    narrator_nvl "那个号码是——{w=0.5}"

    # --- 强力转场：利用签到码作为现实锚点 ---
    # 【音效：粉笔断裂声 + 手机急促震动】
    with hpunch # 画面剧烈摇晃
    f1 "「小黄，别睡了！签到码要过期了，快签到」"

    # --- 回到正常叙事（ADV模式） ---
    # --- 第一幕：下课 ---
    window show
    scene bg class_small_none1 with dissolve
    mc "「签到！签到码是……0721」"
    mc "「啊，签上了……」"
    "糟糕糟糕，怎么睡着了，资料都被口水浸透了"
    "手心全是冷汗。感觉黑板上的字在融化"

    show Huang normal with dissolve
    f1 "「昨晚没睡好吗？」"
    mc "「唉，昨晚找那个 Bug 找了大半夜，最后发现是分号打成中文字符了，受不了了」"
    
    show Huang thinking
    f1 "「嘿嘿，那很难受了」"
    f1 "「不过你这么拼，期末绩点不冲个 4.5 说不过去」"

    mc "「4.5 真的能改变什么吗……」"
    mc "「我只是受不了……这种每天都像死循环的日子」"

    show Huang normal
    f1 "「我们大学生都是这样的，别想那么多了。走吧」"

    mc "「不对不对。怎么能都是这样？生活需要激情，爷们需要战斗！」"
    "感受到了异样的目光，好像说得太大声了"

    show Huang thinking
    f1 "「emmm，我承认你刚刚抢签到的样子是挺激情的啦」"

    mc "「不和你说那么多了，吃饭去！」"
    
    scene bg campus_building2 with dissolve
    scene bg_campus_road_sunny2 with dissolve
    "每天都在走同样的路，看到同样的风景，听到同样的声音"
    "去年的这个暑假，我对大学生活的幻想还充满绮丽的色彩和无限的可能"
    "但是，蓝鲸大学与我的高中真的有什么差别吗？"
    "一旦新鲜感散去，就发现大学生活过是高中生活的一个升级版，甚至是一个更无聊的版本"
    "对大学的生活越来越熟悉，对未来的道路却越来越陌生了"

    # --- 第二幕：食堂聚餐与来自冷哥的邀请 ---
    #scene bg canteen with fade
    #（背景音：嘈杂的食堂人声，餐盘碰撞声）
    f1 "「小黄，你最近是不是在跟冷哥搞什么项目？看你整天神神秘秘的」"

    mc "「啊？没有啊，就是偶尔聊聊天。冷哥说可以给我一些职业规划的建议」"

    f2 "「冷哥？就是那个已经拿到大厂offer的冷峻？」"
    f2 "「小黄你路子这么野？这种大佬你都认识」"

    f1 "「确实，冷哥是真厉害。大二就把竞赛大奖拿了个遍，大三直接进大厂实习」"
    f1 "「听说他现在已经在带项目了，工资比我们辅导员都高」"

    mc "「是啊，他说当年大一的时候也很迷茫，所以现在想多帮帮我们这些后辈」"

    f2 "「诶，他有没有说具体怎么帮你？」"

    mc "「他说有机会可以引荐一些圈子里的人认识，说大学不能只读书，要拓展人脉」"

    f1 "「这话倒是不假。冷哥肯定不只是靠成绩才成功的」"

    "手机突然震动了一下。"

    mc "「嗯？冷哥的消息……」"

    "我顺手点开，把手机放在桌上"

    f2 "「你这个学长也太殷勤了。吃饭都忘不掉你」"

    mc "「他说……今晚有个局，希望我过去」"

    f1 "「今晚？什么局？」"

    mc "「他说是经验分享会，认识几个创业的前辈。地点在……」"
    mc "「Powder Bar。晚上十一点」"

    f1 "「十一点？还在酒吧？」"

    f2 "「我去，冷哥的局都这么硬核的吗？半夜去酒吧听分享会？」"
    mc "「确实有点为难。你们觉得要去吗？」"

    f1 "「我说不去」"

    mc "「嗯？为啥不去」"

    f1 "「不知道，心里没底」"
    
    f2 "「我说去」"
    
    f1 "「为啥去呢？」"

    f2 "「为啥不去呢？」"

    f1 "「刚才不说了吗？心里没底」"

    f2 "「你别光说没底，你说不去有啥好处啊」"
    f2 "「你说不去，我还想让小黄带我一个呢」"

    f1 "「那你倒是说，去有啥好处？」"

    f2 "「你就倒是说，去有啥坏处吧」"

    f1 "「正经的分享会，谁约在半夜？正经的前辈，谁约在酒吧？」"
    f1 "「他要是真有心帮你，为什么不能约在下午的咖啡厅？非要半夜？」"

    f2 "「这是高端分享会，不是小情侣约会。繁忙的大佬都是在深夜才挤得出时间」"
    f2 "「冷哥什么人？大厂offer、竞赛大奖、项目带飞」"
    f2 "「冷哥一句话，顶你吭哧吭哧学半年。他愿意带你进圈子，多少人求都求不来」"
    f2 "「酒吧怎么了？985 985，就是要在酒吧舞啊！」"

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
    f2 "「唉！」"
    # --- 第三幕：化粪池爆炸与决心赴约 ---
    #scene bg campus_road_night
    "啊~~~"
    "从图书馆出来，情不自禁地伸了个懒腰"
    "对了，冷哥消息还没回"
    "已经22点多了吗……"
    "校园里已经没什么人了，路灯下偶尔有几个夜归的学生"
    "11点果然还是太晚了，而且还在酒吧，感觉不太安全"
    "还是拒绝吧！"
    #电话声
    "尹平？这时候打电话干什么，要我带泡面吗？"
    mc "「喂，尹平？怎么了？」"

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
                "图书馆吗？不行，走回头路不是我的风格。"
            "寝室":
                "回寝室吗？很有胆量的选择啊。"
                "是啊，生活以痛吻我，我要报之以歌。"
                "不过生活拿粪投我，我还是稍微避避吧……"
            "Powder Bar":
                $ goToBar = 1

    "对了，去酒吧！"
    return
