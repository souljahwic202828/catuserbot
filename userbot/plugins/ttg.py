# made by eris for CatUserbot

import random
from userbot import catub

from ..helpers.utils import _catutils
from ..core.managers import edit_or_reply

plugin_category = "fun"

@catub.cat_cmd(
    pattern="ttg ?(.*)",
    command=("ttg", plugin_category),
    info={
        "header": "create a gif with text, using @text2gifBot",
        "usage": [
            "{tr}ttg <text> ; (1-28)",
        ],
    },
)
async def ttg(e):
    "make a gif with text"
    if e.fwd_from:
        return
    bot = "@text2gifBot"
    c = random.randint(0, 27)
    args = e.pattern_match.group(1)
    if not args:
        args = "give some text"
    if ";" in args:
    	fx = args.split(";")
    	args = fx[0].strip()
    	c = int(fx[1].strip()) - 1
    r3d = await edit_or_reply(e, "`Making gif with your text...`")
    try:
        results = await e.client.inline_query(
            bot, args,
        )
        p = await results[c].click(
            e.chat_id,
            reply_to=e.reply_to_msg_id if e.is_reply else None,
        )
        await r3d.delete()
        await _catutils.unsavegif(e, p)
    except IndexError:
        return await r3d.edit("`Enter a value between 1-28`")    
    except Exception as fn:
        return await r3d.edit(f"`{fn}`")
