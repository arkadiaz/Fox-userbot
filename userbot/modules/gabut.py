from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Salam


@register(outgoing=True, pattern="^.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")


# Menjawab Salam


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`𝙃𝙖𝙞 𝙂𝙪𝙮𝙨 , 𝙋𝙚𝙧𝙠𝙚𝙣𝙖𝙡𝙠𝙖𝙣 𝙉𝙖𝙢𝙖 𝙂𝙬 {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`𝙂𝙬 𝙏𝙞𝙣𝙜𝙜𝙖𝙡 𝘿𝙞 {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`𝙎𝙖𝙡𝙖𝙢 𝙆𝙚𝙣𝙖𝙡...`")
    sleep(2)
    await event.edit("`𝙐𝙙𝙖𝙝 𝙂𝙞𝙩𝙪 𝘼𝙟𝙖 :𝙫`")


# Perkenalan


CMD_HELP.update({
    "gabut": "**Modules** - `Gabut`\
    \n\n Cmd : `.p`\
    \nUsage : Untuk Memberi Salam\
    \n\n Cmd : `.l`\
    \nUsage : Untuk Menjawab salam\
    \n\n Cmd : `.istigfar`\
    \nUsage : Untuk Beristighfar\
    \n\n Cmd : `.perkenalan`\
    \nUsage : Untuk Memperkenalkan diri."
})
