from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.jamet(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOII**")
    sleep(1.5)
    await typew.edit("**JAMET TELE**")
    sleep(1.5)
    await typew.edit("**CUMA MAU BILANG**")
    sleep(1.5)
    await typew.edit("**GAUSAH SO ASIK**")
    sleep(1.5)
    await typew.edit("**EMANG KENAL?**")
    sleep(1.5)
    await typew.edit("**GAUSAH REPLY**")
    sleep(1.5)
    await typew.edit("**KITA BUKAN KAWAN**")
    sleep(1.5)
    await typew.edit("**GASUKA PC ANJING**")
    sleep(1.5)
    await typew.edit("**BOCAH KAMPUNG**")
    sleep(1.5)
    await typew.edit("**MENTAL TEMPE**")
    sleep(1.5)
    await typew.edit("**LEMBEK KALI BAHð**")


@register(outgoing=True, pattern=r"^\.pp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**PASANG PP DULU JAMET,BIAR ORANG-ORANG PADA TAU BETAPA HINA NYA MUKA LU ð**"
    )


@register(outgoing=True, pattern=r"^\.dp(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU HINA, GAUSAH SOK KERAS YA JAMET!!**")


@register(outgoing=True, pattern=r"^\.so(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAB SAMA GUA JAMET, LU BABU GA LEVEL!!**")


@register(outgoing=True, pattern=r"^\.nb(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAEN BOT MULU JAMET , KESANNYA NORAK GOBLOK!!!**")


@register(outgoing=True, pattern=r"^\.met(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**NAMANYA JUGA JAMET TELE CAPER SANA SINI BUAT CARI NAMA BHAHAHA**"
    )


@register(outgoing=True, pattern=r"^\.war(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR PALAK BAPAK KAU WAR, SOK KERAS BANGET GOBLOK, DI TONGKRONGAN JADI BABU, DI TELE SOK JAGOAN...**"
    )


@register(outgoing=True, pattern=r"^\.wartai(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**WAR WAR TAI ANJING, KETRIGGER MINTA SHARELOK LU KIRA MAU COD-AN GOBLOK, BACOTAN LU AJA KGA ADA KERAS KERASNYA TOLOL**"
    )


@register(outgoing=True, pattern=r"^\.kismin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**CUIHHHH, MAKAN AJA MASIH NGEMIS LO GOBLOK, JANGAN SO NINGGI YA JAMET GA KEREN LU KEK GITU JAMET!!**"
    )


@register(outgoing=True, pattern=r"^\.ded(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MATI AJA LU GOBLOK, GAGUNA LU HIDUP DI BUMI**")


@register(outgoing=True, pattern=r"^\.sokab(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**SOKAB BET LU GOBLOK, KAGA ADA ISTILAH NYA BAWAHAN TEMENAN AMA BOS AHAHAHA!!**"
    )


@register(outgoing=True, pattern=r"^\.gembel(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**MUKA BAPAK LU KEK KELAPA SAWIT ANJING, GA USAH NGATAIN ORANG, MUKA LU AJA KEK JAMET FACEBOOK!!**"
    )


@register(outgoing=True, pattern=r"^\.cuih(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GAK KEREN LO KEK BEGITU GOBLOK, KELUARGA LU BAWA SINI GUA LUDAHIN SATU-SATU, SETDAH!!!**"
    )


CMD_HELP.update(
    {
        "war": "**Plugin : **`war`\
        \n\n  â¢  **Syntax :** `.jamet`\
        \n  â¢  **Function : **Menghina Jamet telegram\
        \n\n  â¢  **Syntax :** `.pp`\
        \n  â¢  **Function : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  â¢  **Syntax :** `.dp`\
        \n  â¢  **Function : **Menghina Jamet muka hina!\
        \n\n  â¢  **Syntax :** `.so`\
        \n  â¢  **Function : **Ngeledek orang sokab\
        \n\n  â¢  **Syntax :** `.nb`\
        \n  â¢  **Function : **Ngeledek orang norak baru pake bot\
        \n\n  â¢  **Syntax :** `.so`\
        \n  â¢  **Function : **Ngeledek orang sokab\
        \n\n  â¢  **Syntax :** `.skb`\
        \n  â¢  **Function : **Ngeledek orang sokab versi 2\
        \n\n  â¢  **Syntax :** `.met`\
        \n  â¢  **Function : **Ngeledek si jamet caper\
        \n\n  â¢  **Syntax :** `.war`\
        \n  â¢  **Function : **Ngeledek orang so keras ngajak war\
        \n\n  â¢  **Syntax :** `.wartai`\
        \n  â¢  **Function : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  â¢  **Syntax :** `.kismin`\
        \n  â¢  **Function : **Ngeledek orang kismin so jagoan di tele\
        \n\n  â¢  **Syntax :** `.ded`\
        \n  â¢  **Function : **Nyuruh orang mati aja goblok wkwk\
        \n\n  â¢  **Syntax :** `.sokab`\
        \n  â¢  **Function : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  â¢  **Syntax :** `.gembel`\
        \n  â¢  **Function : **Ngeledek bapaknya si jamet\
        \n\n  â¢  **Syntax :** `.cuih`\
        \n  â¢  **Function : **Ngeludahin keluarganya satu satu wkwk\
        \n\n**Klo mau Req, kosa kata dari lu Hubungi @Kayzuuuuu**\
    "
    }
)
