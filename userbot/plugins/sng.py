from userbot import catub
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import reply_id


@catub.cat_cmd(
	pattern="sng ?(.*)",
	command=("sng", "misc"),
	info={
		"header": "Get Songs from @LyBot quickly",
		"usage": [
			"{tr}uta <song_name>",
			"{tr}uta <reply to a song name>",
		],
		"examples": ["{tr}uta Dancin krono"],
	}
)
async def lybot(e):
	"Get your song asap!!"
	if e.fwd_from:
		return
	reply_to = await reply_id(e)
	args = e.pattern_match.group(1)
	if not args:
		if e.is_reply:
			reply = await e.get_reply_message()
			args = reply.text
		else:
			await edit_delete(e, "`No input found`")

	eris = await edit_or_reply(e, "`....`")
	res = await e.client.inline_query(
		"lybot", args,
	)

	try:
		await res[0].click(
			e.chat_id,
			hide_via=True,
			reply_to=reply_to,
		)
		await eris.delete()
	except Exception as fx:
		await eris.edit(f"`{fx}`")
