# ReCode by @yansesad
# FROM yansen-userbot <https://github.com/Yansesad/yansen-userbot>
# KONTOLLLLLLL

from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.galau(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAY KAMU GALAU YA? JANGAN GALAU LAGI YA SEMANGAT KONTOL**")


@register(outgoing=True, pattern="^\\.prenjon(?: |$)(.*)")
async def typewritter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**HAHAHA KASIAN UDAH PRENJON GAMON LAGI DARI PADA GAMONIN DIA MENDING JADIAN SAMA AKU DI JAMIN BAHAGIA HEHE.**"
    )


@register(outgoing=True, pattern="^\\.sikntl(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**KONTOL BUAT KAMU YANG UDAH DI JAGA TAPI MALAH DIA YANG KAMU BANGGAIN, INTINYA KAMU KONTOL**"
    )


@register(outgoing=True, pattern="^\\.badut(?: |$)(.*)")
async def typewriter(typew):
    typew.pattetn_match.group(1)
    await typew.edit(
        "**KAMU GALAU YA? YAUDA SEBENTAR AKU PAKE TOPENG BADUT AKU DULU. NAH UDAH, YUK CERITA KAMU KENAPA**"
    )


CMD_HELP.update(
    {
        "gabut2": "**modules** - `gabut2`\
            \n\n cmd : `.galau`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.prenjon`\
            \nUsage : Lihat Sendiri\
            \n\n cmd : `.badut`\
            \nUsage : Lihat Sendiri\
    "
    }
)
