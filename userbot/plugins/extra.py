import asyncio

from ..utils import admin_cmd, remove_plugin
import os
from pathlib import Path
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "extra"

@borg.on(admin_cmd(pattern=r"cd (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    total = event.pattern_match.group(1)
    if not total:
        await event.edit("What I am Supposed to do. Gime time in seconds")
        return
    t = int(total)
    await event.edit(f"Counter Starting for {total} seconds")
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        await event.edit(str(timer))
        await asyncio.sleep(1)
        t -= 1
    await event.reply(f"Countdown for {total} seconds completed")



@bot.on(admin_cmd(pattern=r"cid(?: |$)(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await event.edit("What I am Supposed to check, Give Number")
        return
    catevent = await event.edit(f"Searching for the number.......")
    chat = "@RespawnRobot"
    reply_id_ = await reply_id(event)
    async with event.client.conversation(chat) as conv:
        try:
            start_msg = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(args)
            await asyncio.sleep(5)
            check = await conv.get_response()
            details = check.text
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit("```Please unblock (@RespawnRobot) and try again```")
            return
        await catevent.delete()
        await event.client.send_message(event.chat_id, details, reply_to=reply_id_,)
    await event.client.delete_messages(conv.chat_id, [start_msg.id, check.id])

