import random
from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "extra"

@catub.cat_cmd(
    pattern="ttg ?(.*)",
    command=("ttg", plugin_category),
    info={
        "header": "create a gif with text, using @text2gifBot",
        "usage": [
            "{tr}ttg <text;(1-28)> ",
        ],
    },
)
async def ttg(e):
    "make a gif with text"
    if e.fwd_from:
        return
    bot = "@text2gifBot"
    c = None
    args = e.pattern_match.group(1)
    if not args:
        args = "give some text"
    if ";" in args:
    	fx = args.split(";")
    	args = fx[0].strip()
    	c = int(fx[1].strip())
    if not c or c>28:
        c = random.randint(1, 28)
    r3d = await edit_or_reply(e, "`...`")
    try:
        results = await e.client.inline_query(
            bot, args,
        )
        await r3d.delete()
        await results[c].click(
            e.chat_id,
            reply_to=e.reply_to_msg_id if e.is_reply else None,
        )
    except Exception as fn:
        await r3d.edit(f"`{fn}`")
        return
    # made by eris. for cat ub