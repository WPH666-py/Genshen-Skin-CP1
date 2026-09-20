# -*- coding: utf-8 -*-
"""
原神CP1 · 米提亚×沃雅妮莎 —— DeepKing 皮肤(手工校色版)

DeepKing 支持两种接入方式:

  A. 在「设置 → 界面皮肤」粘贴本仓库地址 —— DeepKing 抓 skin.json + CSS 变量,
     按内置规则自动推导 32 槽位调色板。这条路的「亮色」精确取自
     src/client/genshin-cp1.module.css, 「暗色」由其内置算法从亮色派生。

  B. 直接用本文件: 下面两套调色板是**逐槽位手工校色**的结果, 不经过任何推导,
     结果与设计意图完全一致(暗色保留素材里「共舞」夜景的蓝紫, 而非派生的灰色)。

安装器(genshin-cp1 deepking)会把本调色板写成 genshin-cp1.skin.json,
并生成可视化预览 genshin-cp1-preview.html, 方便导入前先看效果。
"""
from . import _color as col

SKIN_ID = "genshin-cp1-mitiya-voyanisa"
SKIN_NAME = "原神CP1 · 米提亚×沃雅妮莎"
SKIN_DESC = ("米提亚与沃雅妮莎的蓝调同人主题: 日景青蓝取自「比心」, "
             "夜景蓝紫取自「共舞」。33 槽位逐项校色, 亮/暗双套。")

# ─────────────────────────────────────────────── 亮色 · 日景(比心)
LIGHT = {
    "bg": "#ffffff",
    "bgText": "#16243a",
    "sidebarBg": "#eaf4fc",
    "sidebarText": "#1d3350",
    "sidebarHover": "#dcebf9",
    "sidebarSelected": "#c3ddf3",
    "sidebarHeader": "#7590a8",
    "editorBg": "#ffffff",
    "tabsBg": "#eef6fd",
    "tabBg": "#e4f0fa",
    "tabText": "#54708c",
    "tabActiveBg": "#ffffff",
    "tabActiveText": "#16243a",
    "aiBg": "#f2f8fd",
    "aiText": "#16243a",
    "aiTabText": "#54708c",
    "userBubbleBg": "#cfe4f7",
    "userBubbleText": "#16243a",
    "aiBubbleBg": "#ffffff",
    "aiBubbleText": "#16243a",
    "aiBubbleBorder": "#c2dbf0",
    "systemBubbleBg": "#fff8e6",
    "systemBubbleText": "#8a6a00",
    "inputBg": "#ffffff",
    "inputText": "#16243a",
    "inputBorder": "#a9cde9",
    "accent": "#3f8fd8",
    "accentText": "#ffffff",
    "border": "#c2dbf0",
    "chipBg": "#dbeafa",
    "chipText": "#2b5f8f",
    "chipBorder": "#a9cde9",
}

# ─────────────────────────────────────────────── 暗色 · 夜景(共舞)
DARK = {
    "bg": "#121c2b",
    "bgText": "#e4eefb",
    "sidebarBg": "#182740",
    "sidebarText": "#c4d7ec",
    "sidebarHover": "#22344f",
    "sidebarSelected": "#2d4463",
    "sidebarHeader": "#7b93ad",
    "editorBg": "#121c2b",
    "tabsBg": "#16243a",
    "tabBg": "#182740",
    "tabText": "#8ba3bd",
    "tabActiveBg": "#22344f",
    "tabActiveText": "#e4eefb",
    "aiBg": "#182740",
    "aiText": "#e4eefb",
    "aiTabText": "#8ba3bd",
    "userBubbleBg": "#2f4a74",
    "userBubbleText": "#eef4fc",
    "aiBubbleBg": "#1d2f4c",
    "aiBubbleText": "#e4eefb",
    "aiBubbleBorder": "#2f4661",
    "systemBubbleBg": "#3a3118",
    "systemBubbleText": "#e8d9a0",
    "inputBg": "#1a2b45",
    "inputText": "#e4eefb",
    "inputBorder": "#2f4661",
    "accent": "#63a6e6",
    "accentText": "#0d1726",
    "border": "#2f4661",
    "chipBg": "#2a3f63",
    "chipText": "#c9dcf2",
    "chipBorder": "#4a6b96",
}

PALETTE_SLOTS = (
    "bg", "bgText", "sidebarBg", "sidebarText", "sidebarHover", "sidebarSelected",
    "sidebarHeader", "editorBg", "tabsBg", "tabBg", "tabText", "tabActiveBg",
    "tabActiveText", "aiBg", "aiText", "aiTabText", "userBubbleBg", "userBubbleText",
    "aiBubbleBg", "aiBubbleText", "aiBubbleBorder", "systemBubbleBg", "systemBubbleText",
    "inputBg", "inputText", "inputBorder", "accent", "accentText", "border",
    "chipBg", "chipText", "chipBorder",
)


def definition(mascot_light=None, mascot_dark=None, source=None):
    """返回完整的 DeepKing SkinDefinition(手工校色版)。"""
    skin = {
        "id": SKIN_ID,
        "name": SKIN_NAME,
        "builtin": False,
        "description": SKIN_DESC,
        "palettes": {"light": dict(LIGHT), "dark": dict(DARK)},
    }
    if source:
        skin["source"] = source
    if mascot_light or mascot_dark:
        skin["mascot"] = {
            "light": mascot_light or mascot_dark,
            "dark": mascot_dark or mascot_light,
        }
    return skin


def validate():
    """自检: 槽位齐全、色值合法、亮暗确实一浅一深、文字对比度够。"""
    problems = []
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        missing = [k for k in PALETTE_SLOTS if k not in pa]
        extra = [k for k in pa if k not in PALETTE_SLOTS]
        if missing:
            problems.append("%s 缺少槽位: %s" % (label, ", ".join(missing)))
        if extra:
            problems.append("%s 多余槽位: %s" % (label, ", ".join(extra)))
        for k, v in pa.items():
            if not col.is_hex(v):
                problems.append("%s.%s 不是合法 # 十六进制: %r" % (label, k, v))
    if not col.is_light_color(LIGHT["bg"]):
        problems.append("light.bg 不是浅色: %s" % LIGHT["bg"])
    if col.is_light_color(DARK["bg"]):
        problems.append("dark.bg 不是深色: %s" % DARK["bg"])
    # 正文对比度: 深色底上的亮字, 用亮度差做粗判
    for label, pa in (("light", LIGHT), ("dark", DARK)):
        for fg, bg in (("bgText", "bg"), ("sidebarText", "sidebarBg"),
                       ("aiBubbleText", "aiBubbleBg"), ("tabText", "tabsBg")):
            lf = sum(col.to_rgb(pa[fg])) / 3.0
            lb = sum(col.to_rgb(pa[bg])) / 3.0
            if abs(lf - lb) < 60:
                problems.append("%s: %s 与 %s 亮度太接近(%d), 文字可能看不清"
                                % (label, fg, bg, abs(lf - lb)))
    return problems
