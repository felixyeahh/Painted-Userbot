from asyncio import sleep
from pyrogram import *


@Client.on_message(filters.command("heart", prefixes = ".")&filters.me)
def heart(_, msg):
	try:
		for _ in range(20):
			for heart in ['❤ㅤ', '️🧡ㅤ', '💛ㅤ', '💚ㅤ', '💙ㅤ', '💜ㅤ']:
				msg.edit_text(heart)
				sleep(0.5)
	except ValueError:
		msg.edit_text("〰 Не хватает аргументов.")

@Client.on_message(filters.command("clock", prefixes = ".")&filters.me)
def clock(_, msg):
	try:
		for _ in range(20):
			for clock in ['🕛', '🕐', '🕑' ,'🕒', '🕓', '🕔', '🕕', '🕖', '🕗', '🕘', '🕙']:
				msg.edit_text(clock)
				sleep(0.5)
	except ValueError:
		msg.edit_text("〰 Не хватает аргументов.")

@Client.on_message(filters.command("moon", prefixes = ".")&filters.me)
def moon(_, msg):
	try:
		for _ in range(20):
			for moon in ['🌕ㅤ', '🌖ㅤ', '🌗ㅤ', '🌘ㅤ', '🌑ㅤ' ,'🌒ㅤ', '🌓ㅤ', '🌔ㅤ']:
				msg.edit_text(moon)
				sleep(0.5)
	except ValueError:
		msg.edit_text("〰 Не хватает аргументов.")
