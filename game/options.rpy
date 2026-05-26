## 此文件包含有可自定义您游戏的设置。
## ...

define config.name = _("Powder")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _p("""
""")
define build.name = "Powder"

## 音效和音乐
define config.has_sound = True
define config.has_music = True
define config.has_voice = True

# 开启自动语音功能（放在顶层，不要放在 init python 里）
define config.auto_voice = "voice/{id}.ogg"

## 转场
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

## 窗口管理
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

## 默认设置
default preferences.text_cps = 30
default preferences.afm_time = 10

## 存档目录
define config.save_directory = "Powder-1772725068"

## 图标
define config.window_icon = "gui/window_icon.png"

## 构建配置
init python:
    # 以下函数接受文件模式...
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    # 如果需要，可以取消注释
    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')

    # 添加 sound 文件夹到搜索路径（放在 init python 内部是正确的）
    import os
    config.searchpath.append(os.path.join(config.gamedir, "sound"))

# Google Play 密钥等（如果有）
# define build.google_play_key = "..."
# define build.itch_project = "..."