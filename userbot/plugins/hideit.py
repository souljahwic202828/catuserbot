from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id

plugin_category = "extra"


@catub.cat_cmd(
    pattern="hde ?(.*)",
    command=("hde", plugin_category),
    info={
        "header": "Hides the message via @hideitbot",
        "usage": "{tr}hde <text>",
    },
)
async def hideit(event):
    "Hide your message through @HideitBot"
    if event.fwd_from:
        return
    bot = "@hideitbot"
    hidetxt = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if not hidetxt:
            return await edit_delete(
                event, "__What should I hide through bot? Give some text.__"
            )
    results = await event.client.inline_query(bot, hidetxt)
    await results[0].click(event.chat_id, reply_to=reply_to_id)
    await event.delete()