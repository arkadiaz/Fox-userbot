from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sadgirl(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu ganteng`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


@register(outgoing=True, pattern="^.pc(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pc doang`")
    sleep(2)
    await typew.edit("`Ga di bales`")
    sleep(1)
    await typew.edit("`Pas di pc taunya bot`")


CMD_HELP.update(
    {
        "gabut4": "πΎπ€π’π’ππ£π: `sadgirl`\
    \nβ³ : Cobain Aja\
    \n\nπΎπ€π’π’ππ£π: `.pc`\
    \nβ³ : Cobain Aja."
    }
)
