from pyrogram import Client, filters

api_id = 7929455  # « API ID HERE
api_hash = "6b8b162661d8ac847c4bb62d43163bde"   # « API HASH HERE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Typing Effect - Using command - ".type Any Text Here"

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
	orig_text = msg.text.split(".type ", maxsplit=1)[1]
	text = orig_text
	tbp = "" # to be printed
	typing_symbol = "▒"

	while(tbp != orig_text):
		try:
			msg.edit(tbp + typing_symbol)
			sleep(0.02) # 50 ms

			tbp = tbp + text[0]
			text = text[1:]

			msg.edit(tbp)
			sleep(0.02)

		except FloodWait as e:
			sleep(e.x)

# Magic - Using Command - ".magic"

@app.on_message(filters.command("magic", prefixes=".") & filters.me)
def hack(_, msg):

	msg.edit("🤍")
	msg.edit("🤍🤍")
	msg.edit("🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💖💖🤍💖💖🤍🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍💖💖💖💖💖💖💖🤍\n🤍🤍💖💖💖💖💖🤍🤍\n🤍🤍🤍💖💖💖🤍🤍🤍\n🤍🤍🤍🤍💖🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡💛🤍💙💜🤍🤍\n🤍❤️❤️🖤💖🤎💚💛🤍\n🤍💙💜💛💚❤️🤎💙🤍\n🤍💖🤎🖤💖💙💛💖🤍\n🤍🤍💚❤️💜🖤💖🤍🤍\n🤍🤍🤍💖🤎💚🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💙🤍💜💙🤍🤍\n🤍🤎❤️🖤❤️🤎💙💛🤍\n🤍💙💛💚💚❤️🤎💙🤍\n🤍💜🤎🖤🧡💙💛🖤🤍\n🤍🤍🤎❤️💜🖤💚🤍🤍\n🤍🤍🤍💛🤎🖤🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡💛🤍💙💜🤍🤍\n🤍❤️❤️🖤💖🤎💚💛🤍\n🤍💙💜💛💚❤️🤎💙🤍\n🤍💖🤎🖤💖💙💛💖🤍\n🤍🤍💚❤️💜🖤💖🤍🤍\n🤍🤍🤍💖🤎💚🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️🤍❤️❤️🤍❤️❤️🤍❤️\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️🤍❤️❤️❤️❤️❤️🤍❤️\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️🤍❤️❤️❤️🤍❤️❤️\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️\n❤️❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️\n❤️❤️❤️❤️")
	msg.edit("❤️❤️❤️\n❤️❤️❤️\n❤️❤️❤️")
	msg.edit("❤️❤️\n❤️❤️")
	msg.edit("❤️")
	msg.edit("<b>I ❤️</b>")
	msg.edit("<b>I L ❤️</b>")
	msg.edit("<b>I LO ❤️</b>")
	msg.edit("<b>I LOV ❤️</b>")
	msg.edit("<b>I LOVE ❤️</b>")
	msg.edit("<b>I LOVE Y ❤️</b>")
	msg.edit("<b>I LOVE YO ❤️</b>")
	msg.edit("<b>I LOVE YOU❤️</b>")
	msg.edit("<b>I LOVE YOU ❤️</b>")
	msg.edit("<b>I LOVE YO ❤️</b>")
	msg.edit("<b>I LOVE Y ❤️</b>")
	msg.edit("<b>I LOVE ❤️</b>")
	msg.edit("<b>I LOV ❤️</b>")
	msg.edit("<b>I LO ❤️</b>")
	msg.edit("<b>I L ❤️</b>")
	msg.edit("<b>I ❤️</b>")
	msg.edit("<b>I ❤️ U</b>")
    
	sleep(0.1)
	msg.edit("<b>I ❤️ U!</b>")

app.run()
