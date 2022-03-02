# Sky Not
# ReCode by @Zxyune
# FROM Skyla-Userbot <https://github.com/Cangcimenn/Skyla-Userbot>
# Kosakata gombal

from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.go(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**MAU GOMBAL NIH**")
    sleep(1)
    await typew.edit("**pasangan yang beruntung jika bersama**")
    sleep(1)
    await typew.edit("**yaitu kalau cowo nya humoris cewe nya cuek,**")
    sleep(1)
    await typew.edit("**cowonya royal cewe nya baik,**")
    sleep(1)
    await typew.edit("**dan yang lebih beruntung**")
    sleep(1)
    await typew.edit("**jika cowo nya aku, cewe nya kamu**")


# gombal


@register(outgoing=True, pattern="^.jk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**AKU MAU NANYA NIH!!**")
    sleep(1)
    await typew.edit("**Kenapa kamu sama gojek beda?**")
    sleep(1)
    await typew.edit("**Mau tau gaaaa...**")
    sleep(1)
    await typew.edit("**Karena Kalau ojek itu jauh dekat ongkosnya beda**")
    sleep(1)
    await typew.edit("**Tapi kalo kamu jauh deket cantiknya sama**")
    sleep(1)
    await typew.edit("**Eaaaaa bisaa aja kamuuu...**")


# Create by myself @localheart

CMD_HELP.update(
    {
        "gombal": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.go`\
    \n↳ : Kata Gombal.\
    \n\n`.jk`\
    \n↳ : Kamu tau ga."
    }
)
