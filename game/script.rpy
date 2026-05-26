# 角色初始化 #---------------------------------------------------------------------------------------------------
define narrator_nvl = Character(None, kind = nvl) 
define mc = Character("小黄", color="#ffcc00")
define f1 = Character("顺子", color="#2f8451")
define f2 = Character("江帅", color="#0080ff")
define cold = Character("冷峻", color="#ff453e")
define counselor = Character("辅导员", color="#03e1fe")
define police = Character("缉毒警察", color="#03e1fe")

transform credits_roll:
    # 起始：文字顶部对齐屏幕底部（文字完全在屏幕下方，看不见）
    ypos 1.02
    yanchor 0.0
    # 40 秒内匀速移动到屏幕顶部之外（文字顶部到 ypos = -1.0）
    linear 20.0 ypos -1.0

screen credits_screen(text):
    frame:
        background Solid("#00000080")
        xfill True
        yfill True
        vbox:
            xalign 0.5
            at credits_roll
            text text:
                text_align 0.0
                xalign 0.0
                color "#ffffff"
                size 50
                font "HanChanJinShuSong_Pro_Soft.otf"
                line_spacing 5

# 图像资源 #-------------------------------------------------------------------------------------------------------
image bg bar_night1 = "images/bg/bg_bar_night1.webp"
image bg bar_night2 = "images/bg/bg_bar_night2.png"
image bg bar_night_bottle1 = "images/bg/bg_bar_night_bottle1.jpg"
image bg class_small_none1 = "images/bg/bg_class_small_none1.png"
image bg campus_road_wet1 = "images/bg/bg_campus_road_wet1.jpg"
image bg campus_road_sunny1 = "images/bg/bg_campus_road_sunny1.jpg"
image bg campus_road_sunny2 = "images/bg/bg_campus_road_sunny2.jpg"
image bg_campus_road_sunny2 = "images/bg/bg_campus_road_sunny2.jpg"
image bg campus_road_sunny3 = "images/bg/bg_campus_road_sunny3.jpg"
image bg dorm_corridor_sunlight1 = "images/bg/bg_dorm_corridor_sunlight1.jpg"
image bg dorm_inside_dark1 = "images/bg/bg_dorm_inside_dark1.jpg"
image bg dorm_inside_dark2 = "images/bg/bg_dorm_inside_dark2.jpg"
image bg dorm_inside_light1 = "images/bg/bg_dorm_inside_light1.jpg"
image bg book1 = "images/bg/bg_book1.jpg"
image bg campus_building1 = "images/bg/bg_campus_building1.jpg"
image bg campus_building2 = "images/bg/bg_campus_building2.jpg"
image bg announcement1 = "images/bg/bg_announcement1.jpg"
image bg class_outside1 = "images/bg/bg_class_outside1.jpg"
image bg playground1 = "images/bg/bg_playground1.jpg"
image bg playground1 pixel = "images/bg/bg_playground1_pixel.png"
image bg canteen = "images/bg/bg_canteen1.jpg"
image bg canteen1 = "images/bg/bg_canteen1.jpg"
image bg canteen2 = "images/bg/bg_canteen2.jpg"
image bg canteen_food_disgust1 = "images/bg/bg_canteen_food_disgust1.png"
image bg canteen_food_normal1 = "images/bg/bg_canteen_food_normal1.jpg"
image bg chocolate1 = "images/bg/bg_chocolate1.jpg"
image bg dorm_chocolate1 = "images/bg/bg_dorm_chocolate1.jpg"
image bg library_outside = "images/bg/bg_library_outside.png"
image bg drug_choclote = "images/bg/bg_chocolate1.jpg"
image bg dorm_desk_choclote = "images/bg/bg_dorm_desk_choclote.jpg"

# 角色立绘位置 #-----------------------------------------------------------------------------------------------------
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

# 角色立绘资源 #---------------------------------------------------------------------------------------------------
image Jiangshuai ciallo1:
    "images/char/Jiangshuai_ciallo1.png"
    xanchor 0.5 
    yanchor 0.82
    xpos 0.5 
    ypos 1.0
    zoom 0.65

image Jiangshuai handsOnHips1:
    "images/char/Jiangshuai_handsOnHips1.png"
    xanchor 0.5 
    yanchor 0.73
    xpos 0.5 
    ypos 1.0
    zoom 0.4

image Jiangshuai shrug1:
    "images/char/Jiangshuai_shrug1.png"
    xanchor 0.5 
    yanchor 0.65
    xpos 0.5
    ypos 1.0
    zoom 0.45

image Jiangshuai scratchHead1:
    "images/char/Jiangshuai_scratchHead1.png"
    xanchor 0.5 
    yanchor 0.8
    xpos 0.5 
    ypos 1.0
    zoom 0.45

image Jiangshuai coverHead1:
    "images/char/Jiangshuai_coverHead1.png"
    xanchor 0.5 
    yanchor 0.8
    xpos 0.5 
    ypos 1.0
    zoom 0.6

image Jiangshuai UwU1:
    "images/char/Jiangshuai_UwU1.png"
    xanchor 0.5 
    yanchor 0.8
    xpos 0.5 
    ypos 1.0
    zoom 0.55

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
    zoom 0.45

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

image Zhiyuan glance1:
    "images/char/Zhiyuan_glance1.png"
    xanchor 0.5 
    yanchor 0.9
    xpos 0.5 
    ypos 1.0
    zoom 0.5

image Zhiyuan smile1:
    "images/char/Zhiyuan_smile1.png"
    xanchor 0.5 
    yanchor 0.9
    xpos 0.5 
    ypos 1.0
    zoom 0.6

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
    yanchor 0.8
    xpos 0.5 
    ypos 1.0
    zoom 0.45

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

image Zishun running1:
    "images/char/Zishun_running1.png"
    xanchor 0.5 
    yanchor 0.75
    xpos 0.5 
    ypos 1.0
    zoom 0.6

# 游戏开始 #-----------------------------------------------------------------------------------------------------------
label start:
    # --- 开场：解离感强烈的 NVL 模式 ---
    scene black
    show text "本作品为实验性作品，旨在社会实践与禁毒科普教育，\n不含任何诱导违法行为的内容。\n画面表现、剧情节奏与角色刻画等方面还有提升空间，\n欢迎大家批评指正" with Dissolve(3)
    pause 2.0
    scene black with Dissolve(3)

    window hide

    play sound "heartbeats.mp3"

    narrator_nvl "疼……像一把烧红的碎玻璃，从鼻腔一路扎进脑髓{w=0.2}"
    narrator_nvl "眼球胀得发烫，工业漂白粉的腥味呛得胃里翻涌{w=0.2}"
    narrator_nvl "但这股极苦的铁锈感底下……{w=0.1}是前所未有的清醒{w=0.2}"
    nvl clear
    
    narrator_nvl "保持冷静{w=0.2}"
    narrator_nvl "这是哪里 我来做什么{w=0.2}"
    narrator_nvl "仔细回想——{w=0.2}"
    narrator_nvl "那个号码是——{w=0.2}"
    nvl clear
    # --- 强力转场：利用签到码作为现实锚点 ---
    # 【音效：粉笔断裂声 + 手机急促震动】

    stop music

    with hpunch # 画面剧烈摇晃
    
    f1 "「小黄，别睡了！签到码要过期了，快！」"

    # --- 回到正常叙事（ADV模式） ---
    # --- 第一幕：下课 ---
    window show

    scene bg book1 with dissolve
    scene bg class_small_none1 with dissolve
    mc "「签到！签到码是……0721」"
    mc "「啊，签上了……」"

    play music relaxed2 loop

    "糟了糟了，怎么睡着了"
    "完了，资料都被口水泡烂了。黑板上的字好像在游"

    show Zishun supportFrame1 with dissolve
    f1 "「昨晚没睡好吗？」"

    mc "「别提了，昨晚找那个Bug熬到半夜，最后发现分号打成中文的」"
    
    show Zishun rubChin1 with dissolve
    f1 "「事已至此，先吃饭吧」"
    
    scene bg campus_building2 with dissolve
    scene bg_campus_road_sunny2 with dissolve
    "日复一日的路，日复一日的景，日复一日的声响"
    "去年夏天，我对大学生活的幻想还是五彩缤纷"
    "可蓝鲸大学跟我的高中，真有那么不同吗？"
    "新鲜感像水一样流走了，剩下的只有枯燥"
    "对校园每一条路都烂熟于心，对未来每一步却越来越陌生"

# --- 第二幕：食堂聚餐与来自冷哥的邀请 ----------------------------------------------------------------------------------------
    scene bg canteen1 with fade

    play music happy_material loop fadein 0.5
    
    #（背景音：嘈杂的食堂人声，餐盘碰撞声）
    play sound "canteen.mp3" 
    
    show Zishun crossArms1 at right with dissolve
    f1 "「小黄，你最近是不是在跟冷哥搞什么项目？看你整天神神秘秘的」"

    mc "「啊？没有啊，就是偶尔聊聊天。冷哥说可以给我点儿职业规划的建议」"

    show Jiangshuai ciallo1 at left with dissolve
    f2 "「ciallo~ 冷哥？就是那个已经拿到大厂offer的冷峻？」"
    f2 "「小黄你路子这么野？这种大佬你都搭得上」"

    show Zishun rubChin1 at right with dissolve
    f1 "「确实，冷哥是真神。大二就把竞赛奖拿到手软，大三直接进大厂实习」"
    f1 "「听说他现在已经在带项目了，工资比我们辅导员都高」"

    mc "「是啊，他说当年大一的时候也很迷茫，所以现在想多帮帮我们这些后辈」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「诶，他有没有说具体怎么帮你？」"
    
    mc "「他说有机会可以引荐一些圈子里的人认识，说大学不能只读书，要铺人脉」"

    show Zishun crossArms1 at right with dissolve
    f1 "「这话不假。冷哥肯定不光是靠成绩才走到今天的」"

    stop music

    play sound "phone_message.mp3"

    "手机突然震动了一下。"

    mc "「嗯？冷哥的消息……」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你这个学长也太上心了。吃饭都忘不掉你」"

    mc "「他说……今晚有个局，希望我过去」"

    show Zishun supportFrame1 at right with dissolve
    f1 "「今晚？什么局？」"

    mc "「说是经验分享会，认识几个创业的前辈。地点在……{w=0.5}Powder Bar。晚上十一点」"

    f1 "「十一点？还在酒吧？」"

    show Jiangshuai coverHead1 at left with dissolve
    f2 "「我去，冷哥的局都这么硬核的吗？半夜去酒吧听分享会？」"

    play music happy_material loop
    mc "「确实有点为难。你们觉得要去吗？」"

    show Zishun crossArms1 at right with dissolve
    f1 "「我说不去」"

    mc "「嗯？为啥不去」"

    f1 "「说不上来，心里没底」"

    show Jiangshuai handsOnHips1 at left with dissolve    
    f2 "「我说去」"
    
    f1 "「为啥去呢？」"

    f2 "「为啥不去呢？」"

    show Zishun lookUp1 at right with dissolve
    f1 "「刚才不说了吗？心里没底」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你别光说没底，你说不去有啥好处啊」"
    show Jiangshuai ciallo1 at left with dissolve
    f2 "「你说不去，我还想让小黄带我一个呢」"

    show Zishun supportFrame1 at right with dissolve
    f1 "「那你倒是说，去有啥好处？」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「你就倒是说，去有啥坏处吧」"

    f1 "「正经分享会谁约在半夜？正经前辈谁约在酒吧？」"
    f1 "「他要是真有心帮你，为什么不能约在下午的咖啡厅？非要半夜？」"

    show Jiangshuai coverHead1 at left with dissolve
    f2 "「小情侣约会吗这是？这是高端分享会，大佬都是很忙的，只有深夜才挤得出时间」"
    f2 "「冷哥什么人？大厂offer、竞赛大奖、项目带飞」"
    f2 "「冷哥一句话，顶你吭哧吭哧学半年。他愿意带你进圈子，多少人求都求不来」"
    show Jiangshuai ciallo1 at left with dissolve
    f2 "「酒吧怎么了？985 985，就是要在酒吧舞啊」"

    show Zishun rubChin1 at right with dissolve
    f1 "「……{w=0.5}这事儿我们说也没用，看小黄自己吧」"
    
    mc "「我想……」"
    mc "「先吃饭吧」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「唉！」"

    stop music

# --- 第三幕：化粪池爆炸与决心赴约 ----------------------------------------------------------------------------------------
    scene bg library_outside with fade

    play music 空の夕 loop fadein 0.5
    "啊~~~{w=0.2}从图书馆出来，情不自禁地伸了个懒腰"
    "对了，冷哥消息还没回……{w=0.2}已经十点多了吗"
    "校园里已经没什么人了，路灯下偶尔有几个夜归的学生"
    "是凉爽的夏夜，可供人无忧的安眠{w=0.2}"
    "去不去？"
    "自从在学生会的活动中相识，冷哥一直是一个值得信赖的前辈"
    "国奖颁奖台上的他、给我递微积分资料的他、深夜给我指导的他"
    "冷哥好像总是在我的低谷出现，让快烂掉的我又看到了方向"
    "可是11点……真的可以吗？回来还要报备"
    "所以……"
    "11点果然还是太晚了，而且还在酒吧，感觉不太安全"
    "还是拒绝吧！"
    
    stop music
    
    play sound "phone_calling.mp3"

    pause(2)

    "江帅？这时候打电话干什么？"

    stop sound

    mc "「喂，江帅？怎么了？」"

    f2 "「报告寝室长，大事不妙了！」"

    mc "「到底咋了？」"

    f2 "「那个……我有个好消息，和一个坏消息。你想先听哪一个？」"

    mc "「别废话了……直接说坏消息吧」"

    play music funny1 loop
    f2 "「我们寝室{color=#ffcc00}化粪池炸了{/color}」"

    mc "「什么……玩意？」" 

    f2 "「{color=#ffcc00}化粪池{w=0.5}炸了{/color}」"

    mc "「这还能有好消息吗？」"

    f2 "「好消息就是我们俩都逃生了，你就放心吧！就是你在阳台上挂的衣服……{w=0.3}呵呵，我们没有抢救成功」"

    mc "「根本就没想抢救吧！」"

    f2 "「怎么说呢……总之阿姨让我们今晚尽量别回寝室了，学校现在在安排住宿。不过回来也睡不了，粪围感太强了」"

    mc "「行，我知道了」"
    
    stop music

    "受不了了，{w=0.5}这学校还能住一点吗？"
    "本来正打算爬上床结束这疲惫的一天，现在却无家可归"

    play music 空の夕 loop fadein 0.5
    
    "{w=1}呆呆站在原地，大脑一片空白……{w=0.25}要去哪里？"
    "一旦计划被打乱，迷茫与焦虑就会爬上大脑"
    "保持冷静，不要慌张"

    $ goToBar = 0
    while goToBar == 0:
        menu:
            "所以，要去哪里？"
            "图书馆":
                "图书馆吗？{w=0.25}不行，走回头路不是我的风格"
            "寝室":
                "回寝室吗？{w=0.25}很有胆量的选择啊"
                "泰戈尔说什么来着，生活以痛吻我，我要报之以歌"
                "不过生活拿粪投我，我还是稍微避避吧……"
            "Powder Bar":
                $ goToBar = 1

    stop music

    "对了，去分享会！"

    play sound "phoning2.mp3"
    play sound "phone_calling.mp3"

    pause 2.0

    stop sound

    cold "「喂，小黄？」"

    mc "「喂，冷哥，那个分享会还在吗……」"

    cold "「当然在啊。{w=0.3}我已经在包间了，Powder Bar二楼，门口有人接你」"
    cold "「前辈们都等着呢，别紧张，就当来喝杯饮料聊聊天{w=0.3}哈哈」"

    mc "「OK，我马上过去」"

    scene black with dissolve          # 先清空所有背景，淡入纯黑
    window hide
    nvl clear
    narrator_nvl "其实这辈子还没去过酒吧，有点紧张……"
    narrator_nvl "但是顾虑太多会让行动变得沉重"
    narrator_nvl "更何况，冷哥这次分享会的含金量看来确实很高"
    narrator_nvl "感谢{color=#ffcc00}化粪池{/color}，让我有了一个冒险的理由"
    nvl clear
    window show
    
# ---  第四幕：酒吧分享会 ----------------------------------------------------------------------------------------
    "打了个滴，不久就到了Powder Bar"

    play music 疑惑 loop

    scene bg bar_night1 with fade
    scene bg bar_night2 with hpunch
    
    "葡萄美酒夜光杯，冷哥的局果然不一般"
    "烟味、酒味、笑声混在一起。昏黄灯光摇曳，晃得人眼睛发酸"

    show Zhiyuan glance1 with dissolve
    cold "「小黄！这边！快坐我旁边！」"

    mc "「冷哥……不好意思，我来晚了」"

    show Zhiyuan crossArms1 with dissolve
    cold "「不晚不晚！正好赶上分享高潮！」"

    show Zhiyuan towerHands1 with dissolve
    cold "「来，我给你介绍——」"
    cold "「这位是做AI创业的张总，那位是字节跳动前产品经理」"

    scene bg bar_night_bottle1 with dissolve

    "大家笑着点头"
    "第一次参加这种局，不知道说什么好，呆呆数着酒瓶"
    "除了冷哥还有几个不认识的人，看头发像摸爬滚打多年的程序员"
    "资源触达……赛道红利……人脉即杠杆——大佬们的词汇，顺着大脑表面滑过去……"
    "听得很清楚，却什么也没留下来。{w=0.1}悟了一点，又好像完全没悟"

    scene bg bar_night2 with fade

    show Zhiyuan handsOnHips1 with dissolve

    cold "「小黄，你有潜力！{w=0.3}来，我们干一杯！」"

    scene bg bar_night_bottle1 with dissolve
    
    "冷哥拿的那瓶酒刚才出现过吗？突然感觉有点不对劲"
    "他眼里柔和了昏黄灯光，闪过一丝异样眼神"
    "突然觉得有点不舒服"
    "说起来，刚进来就有点头痛，是酒精的原因吗？可能还是昨晚没睡好"

    mc "「谢谢冷哥，今天有点头晕，我喝这个度数少的吧」"

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
    stop music
    mc "「冷哥，干杯！」"

    play sound "clinking2.mp3"

    play sound "heartbeats.mp3"

    "酒液带着一丝奇怪的甜味，先是顺着舌尖滑下去，然后忽然在喉咙里炸开"
    "头皮有点发麻，冷哥的话也听不到了"
    "胃里瞬间升起一股热流，像掺了铁锈的牛奶，想吐又吐不出来"
    "但这股极苦的铁锈感后面……{w=0.1}是前所未有的清醒"
    "我来这干嘛来着？……"

    scene black with dissolve

    scene bg bar_night2 with Dissolve(5)

    mc "「冷哥，这啥酒啊？是不是有点问题？……」"
    mc "「怎么感觉自己轻飘飘的……」"
    mc "「WOC，这酒里面{size=+10}有东西{/size}」"

    show Zhiyuan rubChin1 with dissolve
    cold "「哎别急，刚刚啊，我只是在杯壁抹了一丁点」"
    show Zhiyuan smile1 with dissolve
    cold "「但是如果直接吸进去的话，你就觉得……人就非常开心」"

    play music 疑念 loop

    mc "「抹什么？吸什么？{w=0.5}冷哥，你……」"
    
    "背上冒出一阵冷汗，夹杂着溢出的快感"
    "冷哥拆开一个纸包，露出白色的粉末"

    show Zhiyuan handsOnHips1 with dissolve
    cold "「来，你先粘点在嘴巴上，尝一下味道。以后再慢慢教你这些」"
    
    "冷哥把沾了粉末的手指伸来"
    "后退的力气都没了"
    "这种全身融化的感觉……确实很舒服，真不想从里面出来"

    play sound "heartbeats.mp3"

    menu:
        "要再试一下吗？"
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

    show Zhiyuan smile1 with dissolve

    cold "「对，粘点在牙齿边边上{w=0.5}吸气」"

    mc "「啊啊啊……这个感觉！」"
    
    cold "「以后你就跟着我，我这有的是现货。你放心，平时搞点儿，不会影响学习」"

    stop music

    "眼前的场景随着视线流动，放大，变幻"
    "已经听不清冷哥说啥了，也听不了，看不了，思考不了"
    "就这样摊一辈子吧"
    
    scene black
   
    stop music

    "在生命洪流最丰沛的时候，要及时关上时间的阀门{w=1}"

# ---  第五幕：寝室 --------------------------------------------------------------------------------------------------
    scene bg dorm_inside_light1 with fade
    
    play music blithe1 loop

    show Jiangshuai ciallo1 with dissolve
    f2 "「小黄，昨晚打电话咋没接啊？我们住校内的宾馆，那条件比寝室好多了」"
    
    mc "「昨晚……去分享会了」"
    
    show Jiangshuai UwU1 at left with dissolve
    f2 "「分享会？你果然去分享会了！好啊，开小灶不带上我」"

    show Zishun supportFrame1 at right with dissolve
    f1 "「没出什么事吧？感觉你状态不太好」"

    mc "「没有没有，就是没睡够……」"

    show Jiangshuai shrug1 at left with dissolve
    f2 "「跟着冷哥能有啥事了？肯定是在冷哥家深夜交心了。{w=0.3}小黄，苟富贵，莫相忘！」"

    scene black with fade
    scene bg dorm_inside_dark1 with dissolve
    
    play music mysterious1 loop
    "不知道怎么回的寝室。昨晚的事就当做一场梦吧"
    "可是手里已经不自觉掏出了“电子烟”{w=0.1}说是电子烟，其实掺杂了{color=#ff453e}合成大麻素{/color}"
    "冷哥说，这个东西对身体没什么伤害，偶尔抽抽放松一下还是可以的"
    "这肯定是毒品啊，不该碰"
    "但是现在全身的骨头感觉在被针刺。每动一下，那些针就在肉里搅动，又痒又痛，想挠又挠不到"
    "只有手里的东西可以缓解"
    "怎么办？他们都睡了，动静也不会太大"
    "再不抽就要死了"
    "没关系……就一口……没事……"
    scene black with Dissolve(2)

# ---  第六幕：和顺子一起校园跑 ----------------------------------------------------------------------------------------
    play music relaxed2 loop

    scene bg playground1 with hpunch

    show Zishun running1 with fade

    f1 "「小黄，你身体还好吗？看你摇摇晃晃的，要不今天别跑了吧」"
    
    mc "「跑个步能有啥事了」"

    scene black with dissolve
    scene bg playground1 with dissolve
    
    play sound "heartbeats.mp3"

    mc "「顺子，你等等我……」"

    show Zishun crossArms1 with dissolve
    f1 "「怎么又停了？都8分配了，乐跑都记不了了」"

    mc "「8分配？有这么慢吗」"

    stop music

    show Zishun supportFrame1 with dissolve
    f1 "「我拉你起来。{w=0.5}我去，你心率都200了……别跑了，再跑要猝死了！」"

    scene bg playground1 pixel with fade

    "身子完全垮了，感觉自己脚上拖了两个哑铃一样沉重"
    "跑道像液体一样起伏，世界是个巨大的像素RPG……"
    "明明才两圈"

    scene black with Dissolve(1)

# ---  第七幕：和冷哥见面----------------------------------------------------------------------------------------
    scene bg class_outside1 with dissolve

    play music mysterious1 loop

    "现在这个点，这里没有什么人"
    "那次'分享会'后，我再也没有联系过冷哥。之前他给我打过一次电话，我没接"
    "我不知道是不想接还是不敢接。我似乎还在逃避那一晚的真实经历——一想起那夜的霓虹灯就反胃"
    "可是，为什么我又在这里呢？为什么我又约冷哥在这里见面了？"
    "电子烟已经吸完了，还是没忍住……能再带来这样东西的人，只有他"

    play music 疑惑 loop fadein 0.5

    show Zhiyuan glance1 with dissolve
    cold "「小黄，来这么早啊」"

    show Zhiyuan crossArms1 with dissolve
    cold "「给你打电话也不接，学长我也会担心的。看你变得这么憔悴」"

    show Zhiyuan rubChin1 with dissolve
    cold "「货已经没了，是不是」"
    
    show Zhiyuan smile1 with dissolve
    cold "「还{w=0.2}是{w=0.2}很{w=0.2}想{w=0.2}要{w=0.2}吧？」"

    mc "「……」"

    show Zhiyuan crossArms1 with dissolve
    cold "「废话也不说了，看看这个吧」" 

    scene bg drug_choclote with dissolve
    mc "「巧克力？」"

    cold "「嘿嘿，这可比巧克力刺激多了」"
    cold "「电子烟平时不方便吧？换成巧克力就不会有人起疑了」"

    mc "「难道查不出来吗？」"

    cold "「巧克力啊！你吃巧克力别人查什么」" 
    cold "「嘿嘿，咱们亲兄弟，明算账。一片500」"

    mc "「你那时候在酒吧明明说是免费的？！」"

    cold "「酒吧里倒是免费的没错。但你出了新手村还想领新手福利吗？」"
    cold "「为了这批货，我可损失了几个兄弟」"

    mc "「你这不都是涨价套路么」"

    cold "「一分钱一分货。你以为你那点电子烟就已经是极致体验了吗？」"
    cold "「这玩意可没那么简单。刚接触的人都是{color=#ff453e}鼻吸{/color}，吸收率只有20%%」"
    cold "「等你再吸几次，{color=#ff453e}鼻吸{/color}就不爽了，到时候你就会去{color=#ff453e}烫吸{/color}，让毒品热雾化，通过鼻腔快速吸入肺部。顺着毛细血管进入血液循环"
    cold "「还没完呢，{color=#ff453e}烫吸{/color}的吸收率也没到一半，你迟早会觉得不够。这时候还要再爽，就只能{color=#ff453e}注射{/color}」"
    cold "「没点人引路，你就只能自己摸索，你会往胳膊上、腿上等四肢的每一寸皮肤下死手，看着它们慢慢坏死」"
    cold "「等每一寸皮肤都坏死，就只有一个地方可以注射了」"

    mc "「哪里？」"

    cold "「脖子」"
    cold "「这就叫作{color=#ff453e}开天窗{/color}，也是吸毒的最后阶段。等那时候，你就知道什么叫飞升极乐世界了！」"

    cold "「我能告诉你这么多，也不怕你不吸」"
    cold "「谁不知道这玩意不好？意志力在毒瘾面前算个屁！哼哼」"

# ---  第八幕：和江帅一起吃饭 ---------------------------------------------------------------------------------------------------
    scene bg canteen2 with fade

    play music happy_material loop

    show Jiangshuai scratchHead1 with dissolve
    f2 "「吃这么少？有心事啊」"
    
    mc "「没什么，我不怎么饿」"

    scene bg canteen_food_normal1 with dissolve
    scene bg canteen_food_disgust1 with dissolve 

    stop music

    "味同嚼蜡，难以下咽"
    "正常美食能带来50%% - 100%%的多巴胺提升，但是毒品带来的多巴胺提升可能是正常食物的{color=#ff453e}数十倍甚至上百倍{/color}"
    "加上电子烟抽多了，{color=#ff453e}唾液分泌不出来，口干舌燥{/color}，喝再多水都没用"
    "感觉自己像一头在农场里吃草的牛"

    scene bg canteen2 with dissolve
    play music happy_material loop
    
    show Jiangshuai scratchHead1 with dissolve
    f2 "「听说最近缉毒警察要来我们学校了」"
    
    mc "「什么？！你怎么知道的」"
    
    show Jiangshuai shrug1 with dissolve
    f2 "「下周一的讲座啊！你怎么大惊小怪的」"

    mc "「他们……只做讲座吗？」"

    show Jiangshuai UwU1 with dissolve
    f2 "「我又不是缉毒警察，我哪知道」"
    f2 "「话说你最近不看手机的吗？前几天微信上突然找我借钱，我以为啥急事就给你打了，你领的倒挺快。问你啥事你又不吱声了」"
    f2 "「你要不用手机了就给我，我去帮你换俩不锈钢脸盆。你一个我一个」"

    mc "「滚你的吧」"

    "原来我还找江帅借过钱，我究竟还做了什么事……{w=0.25}不行，想不起来"
    "这不就跟被夺舍了一样吗……"
    "江帅是不是已经知道我的事了？感觉他刚才说话的眼神有点怪怪的"
    "虽然江帅不像是能看出什么端倪的人，还是小心点比较好……"

    stop music

    show Jiangshuai scratchHead1 with dissolve
    f2 "「小黄，感觉你最近有点奇怪啊」"
    
    pause 2.0

# ---  第九幕：突击查寝（上部分） ---------------------------------------------------------------------------------------------------
    scene bg dorm_inside_light1 with fade

    play music mysterious1 loop

    show Zishun supportFrame1 at center with dissolve
    f1 "「小黄，你不能再逃课了！」"
    f1 "「你现在天天魂不守舍，活着没点人样！」"
    f1 "「你生活的激情呢？」"
    
    mc "「顺子，你怎么越来越像我老爹了」"
    
    show Zishun crossArms1 at right with dissolve
    show Jiangshuai scratchHead1 at left with dissolve

    f2 "「小黄，他想当你爹，我不想，所以那500块你打算啥时候还」"

    mc "「等下个月我发生活费吧！现在手头有点紧」"

    f2 "「反正你手头一直很紧就是了」"

    stop music

    mc "「别东拉西扯了！」"

    play sound "draw_curtain.mp3"
    
    scene black with dissolve
    
    "发明床下帘的人真是个天才"
    "感觉最近性格变得很{color=#ff453e}狂躁{/color}，不像以前的自己了"
    "不管了，已经迫不及待想试试那个巧克力了"
    
    scene bg dorm_desk_choclote with dissolve

    play sound "being_knocked1.mp3"

    "怎么看都不像是毒品啊……{w=0.5}闻着也不像"

    play sound "being_knocked1.mp3"

    "轻轻捏了一小块"

    play sound "being_knocked1.mp3"

    "然后放在舌头上——"

    play sound "draw_curtain.mp3"

    scene bg dorm_inside_light1 with dissolve

    mc "「不是，谁在{size=+10}敲门{/size}啊？！」"

    play music blithe1 loop
    
    counselor "「614开门，查寝~」"

    mc "「呵，这学校还查上寝了」"

    scene bg dorm_inside_light1 with fade

    stop music

    play sound "heartbeats.mp3"

    "怎么回事——{w=0.2}把手转动的那一刻，感觉整个世界都静止了"
    "顺子他们怎么不开门？怎么就我听到了敲门声？{w=0.2}难道是幻听？"
    "不对啊刚刚没吃下去，不会发作啊"
    "对了，也没有查寝的通知才对，查寝也不应该在深夜吧"
    "冷汗直流"
        
    # 时间回溯：插叙室友是如何举报的
    scene black

    show text "{size=+10}时间回到昨天{/size}" with Dissolve(2)

    with Pause(1.0)

# ---  第十幕：顺子和江帅在食堂聚餐 ---------------------------------------------------------------------------------
label scene_10:
    scene bg canteen1 with fade

    play music happy_material loop fadein 2.0
    # 背景音效：食堂嘈杂人声、碗筷碰撞声

    show Zishun supportFrame1 at right with dissolve
    f1 "「江帅，你有没有觉得小黄最近怪怪的？」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「你也发现了？我还以为就我一个人这么想」"

    show Zishun rubChin1 at right
    f1 "「他这周逃了三次专业课了，辅导员已经在群里问情况」"

    show Jiangshuai shrug1 at left
    f2 "「而且他脸色越来越差，黑眼圈快掉到嘴角了。上回一起吃饭，他扒了两口就去厕所吐了」"

    show Zishun crossArms1 at right
    f1 "「还有上次找我借了800块，说是买参考书，叽里咕噜说一大堆，结果我问了书店，根本没那本书」"

    show Jiangshuai handsOnHips1 at left
    f2 "「他也找我借过500，到现在都没还。我问他要，他就说下个月，但眼看着他越来越瘦，花钱却越来越大手大脚」"

    stop music
    scene bg campus_road_sunny3 with fade

    show Jiangshuai handsOnHips1 at left with dissolve
    show Zishun crossArms1 at right with dissolve

    f2 "「你说……他是不是碰了什么东西？」"

    play music mysterious1 loop fadein 2.0

    show Zishun supportFrame1 at right
    f1 "「你是说……」"

    f2 "「{color=#ff453e}毒品{/color}。我表哥以前就是这样，先是大把掉头发，然后金额越借越大，最后进了戒毒所」"

    show Zishun rubChin1 at right
    f1 "「可他以前不是挺上进的啊。冷哥介绍的项目，他这么珍惜……」"

    show Jiangshuai ciallo1 at left
    f2 "「问题就出在那个冷哥身上！我偷偷看到小黄微信聊天记录，冷哥发了一堆什么{color=#ff453e}“巧克力”{/color}{color=#ff453e}“电子烟”{/color}{color=#ff453e}“新人优惠”{/color}，还让他别声张」"

    f2 "「而且小黄上周半夜在阳台抽一种很奇怪的电子烟，味道发甜，但不是水果味——是{color=#ff453e}化学味的甜{/color}」"

    show Zishun crossArms1 at right
    f1 "「不行，这不能拖着。他自己已经控制不住了，再下去人就毁了」"

    show Jiangshuai shrug1 at left
    f2 "「可是咱们直接跟他说，他肯定翻脸。你没看他现在脾气大得很吗」"

    f1 "「那就不跟他说，直接找能管他的人」"

    f2 "「找辅导员？」"

    f1 "「对。辅导员有经验，学校也有禁毒联络员。我们不用自己冒险，只要把看到的、听到的如实告诉辅导员就行」"

    f2 "「可是……冷哥那边会不会报复啊？他认识那么多社会人……」"

    f1 "「怕什么？我们是为了保护同学。辅导员会保密，而且举报吸毒是每个公民的义务」"
    f1 "「你忘了那个讲座了？缉毒警察说了，学生群体发现可疑情况，{color=#ffcc00}第一时间报告老师或拨打110{/color}」"

    show Jiangshuai scratchHead1 at left
    f2 "「……行！你说得对。再拖下去要大事不妙」"

    f1 "「吃完饭我就给辅导员打电话。你这几天也留意一下，把小黄借钱的转账记录、反常行为的时间点整理出来」"

    show Jiangshuai ciallo1 at left
    f2 "「好。就这么办」"

    stop music

    scene black with dissolve

    show text "{size=+10}当小黄打开门……{/size}"

    with Pause(1.0)

# ---  第十一幕：突击查寝（下部分） ---------------------------------------------------------------------------------
    # 回到开门后的画面
    scene bg dorm_inside_light1 with dissolve
    
    play music 真相 loop

    counselor "「小黄，别紧张。我们接到举报，怀疑你涉嫌持有和吸食毒品，需要配合调查」"

    mc "「什……什么？我没有！」"

    # 警察扫视桌面，发现巧克力

    scene bg dorm_desk_choclote with dissolve

    "警察扫了一眼桌面，拿起那盒巧克力。"

    police "「这是什么东西？」"

    mc "「就……就是普通巧克力啊……」"

    police "「普通巧克力？待会带回去检查一下」"

    mc "「……」"

    # 在宿舍直接告知冷哥已被捕
    scene bg dorm_inside_light1 with dissolve

    counselor "「小黄，还有一件事要告诉你——冷峻已经被缉毒警察抓获了」"
    counselor "「他在审讯中已经全部交代，包括他诱骗你吸毒、卖给你毒品巧克力的事」"

    mc "「什么……？冷哥他……！」"

    police "「你桌上的巧克力，型号和包装与冷峻供述的完全一致。证据确凿」"

    # 顺子和江帅站在门口，神色复杂
    show Zishun supportFrame1 at right with dissolve
    show Jiangshuai UwU1 at left with dissolve

    f1 "「小黄……对不起，是我们举报的。但我们真的不想看着你毁掉自己」"

    mc "「妈的，你们都装糖阴我是吧！」"

    f2 "「你骂我也好，恨我也罢，总比哪天看到你死在外面的强」"

    mc "「你们……！」"

    stop music

    # 终止对话，直接带走
    counselor "「好了，先不说这些。小黄，跟我们走吧」"
    
    play music mysterious2 loop
    
    scene black with dissolve
    
    show text "{size=+20}BAD END{/size}" with Dissolve(2)

    pause 2.0

    scene black with Dissolve(2)
    # 也可以显示自定义图片，例如：
    # show bg_badend with dissolve

    # 停留2秒，让玩家看到结局
    
    return

label trueEnd:
# ---  第十二幕：拒绝喝酒 ------------------------------------------------------------------------------------
    scene bg bar_night2 with dissolve
    
    stop music

    mc "「冷哥，不好意思，我今天不太舒服，就不喝了。」"
    
    show Zhiyuan crossArms1 with dissolve
    cold "「怎么？不给面子啊？就一小口，不会怎么样的」"

    mc "「真的不行，我酒精过敏。改天我请你喝咖啡吧！」"

    "冷哥眼神里闪过一丝失望，但很快又恢复了笑容。"

    play music 疑惑

    show Zhiyuan crossArms1 with dissolve
    cold "「行吧，那你喝饮料。来，尝尝这个果汁。」"

    "他递过来一杯橙色的液体。我摇了摇头，站起来。"

    mc "「冷哥，我突然想起来明天一早还有实验课，我现在头痛的厉害，得先走了。谢谢你的邀请」"

    show Zhiyuan handsOnHips1 with dissolve
    cold "「这么早？分享会还没结束呢……」"

    mc "「真对不住，下次一定。」"

    "没有再给他挽留的机会，快步走出了酒吧包间。"
    "身后传来冷哥和几个前辈的笑声，后背发凉。"

    scene black with dissolve
    
    stop music

    "夜风吹在脸上，好凉"
    "手机震动了一下，是冷哥发来的消息：「小黄，你太紧张了，下次我单独请你」"

    pause 2.0

# ---  第十三幕：冷哥被抓，食堂聚餐反思 ----------------------------------------------------------------------------------
    scene black with dissolve

    show text "{size=+10}半个月后……{/size}" with dissolve

    pause 1.5

    scene bg campus_road_wet1 with dissolve
    "半个月后的一天中午，我刚从图书馆出来，手机上弹出一条新闻推送"
    "缉毒警察破获了一起校园贩毒案，主犯冷峻被刑事拘留"
    "新闻标题刺眼而冰冷：「名校学长借分享会之名，诱骗多名学生吸毒」"
    "配图里，冷哥穿着橙色拘留服，低着头，再也看不出当初那个意气风发的样子"

    "我的手微微发抖，不是因为害怕，而是后怕。"

    mc "「如果那天我没坚持拒绝……现在穿这身衣服的，会不会也有我一个？」"

    scene bg canteen2 with dissolve

    play music happy_material loop fadein 1.0

    "食堂里，顺子和江帅看到我，招手让我过去。"

    show Zishun supportFrame1 at right with dissolve
    f1 "「小黄，你看到新闻了吗？」"

    mc "「看到了。冷哥……呸，冷峻被抓了。」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「我靠，真是他啊？我还以为只是重名」"
    f2 "「听说他贩卖的毒品里含有{color=#ff453e}“芬太尼”{/color}，好几个人吸过量差点死了」"

    mc "「有那么严重吗？」"

    show Zishun crossArms1 at right
    f1 "「新闻里说了，有一个大二的学长，被他用同样的套路骗到酒吧，第一次就吸过量，直接送ICU抢救了」"

    mc "「……那个学长活下来了吗？」"

    show Jiangshuai shrug1 at left
    f2 "「命保住了，但医生说神经系统已经受损，可能一辈子都要做康复治疗」"

    "眼前仿佛出现了一个模糊的身影——那个学弟可能也像我一样，曾经以为冷哥是值得信赖的前辈"

    show Zishun lookUp1 at right
    f1 "「小黄，你知道最可怕的是什么吗？辅导员上午来宿舍，说冷峻在审讯时交代，他第一次在酒吧给你倒的酒里，掺了{color=#ff453e}“GHB”{/color}」"

    mc "「{color=#ff453e}“GHB”{/color}？」"

    show Jiangshuai handsOnHips1 at left
    f2 "「就是{color=#ff453e}“神仙水”{/color}，无色无味，喝下去十几分钟就会昏迷。他本来想把你完全控制了再下手」"

    "后背瞬间被冷汗浸透。那天如果不是我坚持不喝，现在躺在医院的可能就是我"

    # 插入一段回忆闪回（可选，用文字描述）
    scene bg bar_night2 with dissolve
    scene bg bar_night_bottle1 with dissolve

    "脑海里又浮现出那夜酒吧的昏黄灯光，冷哥递过来那杯酒时，眼神里一闪而过的异样……"

    scene bg canteen2 with dissolve

    mc "「我……我当时只是觉得不对劲，没想到会这么危险」"

    show Zishun supportFrame1 at right
    f1 "「所以你做到了很多人做不到的事——在那种场合说不」"
    f1 "「辅导员说，冷峻案里还有好几个学生，一开始都在犹豫，最后碍于面子糊里糊涂喝了那杯酒，结果再也回不了头」"

    show Jiangshuai scratchHead1 at left
    f2 "「小黄，说实话，当时你要真喝了，我和顺子可能也不会怪你，但……我们肯定会后悔一辈子」"
    f2 "「还好你够清醒」"

    mc "「我想还是你们平时总在我耳朵边上嘀咕'酒吧不靠谱、学长太殷勤'，让我潜意识里留了个心眼」"

    show Zishun crossArms1 at right
    f1 "「哈哈，那看来我们比辅导员还管用」"

    # 场景转换到校园小路，三人边走边聊
    scene bg campus_road_sunny1 with dissolve
    
    stop music

    show Zishun rubChin1 at right with dissolve
    f1 "「小黄，你说冷哥以前那么好的人，怎么就变成这样了？」"

    mc "「可能……他一开始也只是想“试试”，觉得能控制住，结果越陷越深，最后要靠卖毒品来维持自己的毒瘾」"

    show Jiangshuai scratchHead1 at left with dissolve
    f2 "「所以毒品这东西，一次都不能试，试试就逝世啊」"

    stop music

    show Zishun crossArms1 at right with dissolve
    f1 "「对，永远不要相信自己能控制住它，它只会把人拖进深渊！」"

    window hide

    scene black with Dissolve(4)
    show text "{size=+20}TRUE END{/size}" with Dissolve(4)
    pause 4.0
    scene black with Dissolve(4)