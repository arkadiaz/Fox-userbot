""" Userbot module for other small commands. """
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Halo {DEFAULTUSER} Jika Anda Tidak Tau Semua Perintah Bot Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/laz1yy)"
        "\n[Repo](https://github.com/arkadiaz/Fox-Userbot)"
        "\n[Instagram](instagram.com/bm_bd_)"
    )


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://telegra.ph/VarsUserbot-02-02)"
    )


CMD_HELP.update(
    {
        "helper": "`.lhelp`\
\nUsage: Bantuan Untuk Fox-Userbot.\
\n`.vars`\
\nUsage: Melihat Daftar Vars."
    }
)
