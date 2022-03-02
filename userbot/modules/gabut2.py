from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.skyla(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku skyla`")
    sleep(3)
    await typew.edit("`9999999 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di ytta, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.syg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


CMD_HELP.update({
    "gabut2": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.skyla`\
    \n↳ : perkenalan skyla\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.syg`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
    \n↳ : Jan Lupa Semangat."
})
