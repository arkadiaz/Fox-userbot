# Sky Not
# by @Zxyune
# FROM Skyla-Userbot <https://github.com/SkylaIND/Skyla-Userbot>

from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.ti(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("JADI PETINGGI DI VIRTUAL KO BANGGA")


@register(outgoing=True, pattern="^.su(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("KU KIRA SUHU TERNYATA BABU GROUP SURUH SEBAR LINK, MENDING LU SEBARIN STICKER SEDOT WC DAPET DUIT ANJ")


@register(outgoing=True, pattern="^.jl(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("TERKENAL LU JELEK ANJ CUMAN GARA-GARA PROMOSI NGANGKANG DI OS")


@register(outgoing=True, pattern="^.kr(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**KU KIRA KERAS TERNYATA LEMBEK KE KERTAS**"
    )


@register(outgoing=True, pattern="^.se(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JADI SUGEST AJA BANGGA ANJ, EMANG EMAK BAPAK LU KALAU MENINGGAL BUTUH DI SUGGEST**")


@register(outgoing=True, pattern="^.tl(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TITLE BANYAK NYALI KENDOR**")


@register(outgoing=True, pattern="^.sk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SOK SOK AN BUAT CIRLCE KETEMU REAL LANGSUNG DOWN**")


@register(outgoing=True, pattern="^.cx(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CIRCLE EX PALING OP😎**")


@register(outgoing=True, pattern="^.ro(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GAK KERAS ADU ROASTING MENDING LANGSUNG KETEMUAN AJA BIAR BERASA**"
    )


@register(outgoing=True, pattern="^.tk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TETE LU KENDOR GA ENAK**")


@register(outgoing=True, pattern="^.kj(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KEK LAGI MANTEP AJA LU, MUKA KAYA UBIN BENGKEL AJA BELAGU**")


@register(outgoing=True, pattern="^.gk(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GADULU KONTOL LU KECIL**")


@register(outgoing=True, pattern="^.gl(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GADULU KONTOL LU BURIK**")


@register(outgoing=True, pattern="^.gr(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GADULU MEMEK LU BAU TERASI**")


@register(outgoing=True, pattern="^.jt(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN NGOMONG MULUT BAU TAI**")


@register(outgoing=True, pattern="^.pn(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**JAKA SEMBUNG BAWA GOLOL GAK NYAMBUNG GOBLOK**"
    )


@register(outgoing=True, pattern="^.ow(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU GAK GUNA JADI OWNER ANJ KALAU CUMAN MINTA VCS GRATIS SAMA TALENT**")


@register(outgoing=True, pattern="^.kc(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KU CUPU NIH SENGGOL DONG KAK😎**")


@register(outgoing=True, pattern="^.kd(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KALAU DIKIT-DIKIT BAPERAN GAUSAH MAIN TELE ANJ**")


CMD_HELP.update(
    {
        "roasting": ".ti\
\nUsage: Nyindir Petinggi.\
\n\n.su\
\nUsage: Nyindir Suhu.\
\n\n.jl\
\nUsage: Nyindir Promosi.\
\n\n.kr\
\nUsage: Nyindir Nyali.\
\n\n.se\
\nUsage: Nyindir Kang Suggest.\
\n\n.tl\
\nUsage: Nyindir Title.\
\n\n.sk\
\nUsage: Nyali Anak Circle.\
\n\n.cx\
\nUsage: Circle Paling Op.\
\n\n.ro\
\nUsage: Adu Roasting."
    }
)

CMD_HELP.update(
    {
        "roasting2": ".tk\
\nUsage: Anu Nya Kendor.\
\n\n.kj\
\nUsage: Muka Ubin Bengkel.\
\n\n.gk\
\nUsage: Anu Nya Kecil.\
\n\n.gl\
\nUsage: Anu Nya Burik.\
\n\n.gr\
\nUsage: Anu Nya Bau Terasi.\
\n\n.jt\
\nUsage: Mulut Bau Tai.\
\n\n.pn\
\nUsage: Pantun Goblok.\
\n\n.ow\
\nUsage: Gak Guna Jadi Owner.\
\n\n.kc\
\nUsage: Orang Cupu.\
\n\n.kd\
\nUsage: Bocah Baperan.\
\n\n**Klo mau Req, kosa kata dari lu Hubungi @Zxyune**\
    "
    }
)
