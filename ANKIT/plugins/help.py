# By < XNKIT >
# // SPAMMERBOT MADE BY ©XNKIT™ //


from . import *
from .. import worker, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "yigitcanb3y"

@worker.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    tatti=f"Sᴘᴀᴍᴍᴇʀ Bᴏᴛ Fᴏʀ {ALIVE_NAME} \nMᴀᴅᴇ Bʏ @yigitcanb3y"
    await event.reply(tatti,
                    buttons=[
                        [Button.inline("Kontrol et.",data="helpme")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="BEN BİR SPAM BOTUM SORUN OLURSA SUPPORT GURUBUNA GELEBİLİRSİN"
    await event.edit(text,
                     buttons=[
                         [Button.inline("ιиƒο", data="lu")],
                         [Button.inline("ϲοммαи∂ѕ", data="2")],
                         [Button.inline("Kapat", data="3")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    uuu="ϲοммαи∂ѕ ϐυττοиѕ ϐєℓοω "
    await event.edit(uuu,
                     buttons=[
                         [Button.inline("ѕραм", data="spam")],
                         [Button.inline("ϐιgѕραм", data="bigspam")],
                         [Button.inline("υѕραм", data="uspam")],
                         [Button.inline("мѕραм", data="mspam")],
                         [Button.inline("Geri", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="3"))
async def ex(event):
    text3="Menü kapatıldı."
    await event.edit(text3,
                     buttons=[
                         [Button.inline("яєορєи", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="lu"))
async def ex(event):
    text4="Yardım"
    await event.edit(text4,
                     buttons=[
                         [Button.url("Wᴇʙsɪᴛᴇ", url="https://github.com/Yigitcanb3y")],
                         [Button.url("ᴛᴇʟᴇɢʀᴀᴍ", url="https://t.me/redbyteteam")],
                         [Button.url("ᴛᴇʟᴇɢʀᴀᴍ", url="https://t.me/yigitcanb3y")],
                         [Button.inline("Geri", data="helpme")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="spam"))
async def ex(event):
    texi="➽ /spam number text \nMaximum /spam 99 text."
    await event.edit(texi,
                     buttons=[
                         [Button.inline("Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="bigspam"))
async def ex(event):
    tut="➽ /bigspam number text \nMinimum /bigspam 101 text \nMaximum /bigspam 9999 text."
    await event.edit(tut,
                     buttons=[
                         [Button.inline("Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="uspam"))
async def ex(event):
    tempu="➽ Spam bot. Limit yok."
    await event.edit(tempu,
                     buttons=[
                         [Button.inline("Geri", data="2")]
                     ])

@worker.on(events.callbackquery.CallbackQuery(data="mspam"))
async def ex(event):
    achdh="➽ Spam bot. Limit yok"
    await event.edit(achdh,
                     buttons=[
                         [Button.inline("Geri", data="2")]
                     ])
