import asyncio

from ..utils import admin_cmd, remove_plugin
import os
from pathlib import Path
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "extra"

@catub.cat_cmd(
    pattern="cd ?(.*)",
    command=("cd", plugin_category),
    info={
        "header": "Countdown time in seconds",
        "usage": "{tr}cd <number>",
    },
)
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


@catub.cat_cmd(
    pattern="tc ?(.*)",
    command=("tc", plugin_category),
    info={
        "header": "checks number in truecaller database",
        "usage": "{tr}tc <number>",
    },
)
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

@catub.cat_cmd(
 pattern="bc ?(.*)",
 command=("bc", plugin_category),
 info={
  "header": "Text to binary",
  "usage": [
   "{tr}bc <Text>",
   "{tr}bc <reply to a text>",
  ],
  "examples": ["{tr}bc Hello world"],
 }
)
async def textUtilsBot(e):
 "convert text to binary"
 if e.fwd_from:
  return
 reply_to = await reply_id(e)
 args = e.pattern_match.group(1)
 if not args:
  if e.is_reply:
   reply = await e.get_reply_message()
   args = reply.text
  else:
   await edit_delete(e, "No input found")

 eris = await edit_or_reply(e, "converting text to binary")
 res = await e.client.inline_query(
  "textUtilsBot", args,
 )

 try:
  await res[2].click(
   e.chat_id,
   hide_via=True,
   reply_to=reply_to,
  )
  await eris.delete()
 except Exception as fx:
  await eris.edit(f"{fx}")
