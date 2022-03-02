from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/0970dd27e9141599aaccf.jpg",
                caption="⚡ **Skyla-Userbot berhasil diaktifkan**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - 8.0@Skyla-Userbot\n━━━━━━━━━━━━━━━\n➠ **Powered By:** @SkylaIND ",
                buttons=[(Button.url("ꜱᴜᴘᴘᴏʀᴛ", "https://t.me/skylasupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
