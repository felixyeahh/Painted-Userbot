from pyrogram import *
import random

@Client.on_message(filters.command("emoji", prefixes = ".")&filters.me)
def emojicmd(_, msg):
		c = msg.text.split(" ")
		emoji = ['😀', '😃', '😄', '😁', '😆', '😅', '🤣', '🥰', '😇', '😊',
				 '😉', '🙃', '🙂', '😂', '😍', '🤩', '😘', '😗', '☺', '😚',
				 '😙', '🤗', '🤑', '😝', '🤪', '😜', '😛', '😋', '🤭', '🤫',
				 '🤔', '🤐', '🤨', '😐', '😑', '😌', '🤥', '😬', '🙄', '😒',
				 '😏', '😶', '😔', '😪', '🤤', '😴', '😷', '🤒', '🤕', '🤢',
				 '🤯', '🤮', '🤠', '🤧', '🥳', '🥵', '😎', '🥶', '🤓', '🥴',
				 '🧐', '😵', '😕', '😳', '😢', '😲', '😥', '😯', '😰', '😮',
				 '😨', '😧', '🙁', '😦', '😟', '🥺', '😭', '😫', '😱', '🥱',
				 '😖', '😤', '😣', '😡', '😞', '😠', '😓', '🤬', '😩', '😈', '👿']
		d =[]
		e = len(c)
		for i in range(e):
				rand = random.choice(emoji)
				d.extend((c[i], rand))
		f = len(d) - 1
		d.pop(f)
		t = "".join(d)
		msg.edit_text(t)
