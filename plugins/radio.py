#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from pyrogram import Client, filters
from pyrogram.types import Message
from utils import mp, RADIO, USERNAME
from config import Config
from config import STREAM
CHAT=Config.CHAT
ADMINS=Config.ADMINS

async def is_admin(_, client, message: Message):
    admins = await mp.get_admins(CHAT)
    if message.from_user is None and message.sender_chat:
        return True
    if message.from_user.id in admins:
        return True
    else:
        return False

admin_filter=filters.create(is_admin)   


@Client.on_message(filters.command(["radio", f"radio@{USERNAME}"]) & admin_filter & (filters.chat(CHAT) | filters.private))
async def radio(client, message: Message):
    if Config.CPLAY:
        if 3 in RADIO:
            k=await message.reply_text("It seems channel play is enabled and playlist is not empty.\nUse /clearplaylist to empty the playlist.")
            await mp.delete(k)
            await mp.delete(message)
            return
        else:
            await mp.start_radio()
            k=await message.reply_text(f"Channel Play from <code>{STREAM}</code> started.")
            await mp.delete(k)
            await mp.delete(message)
            return
    if 1 in RADIO:
        k=await message.reply_text("Kindly stop existing Radio Stream /stopradio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.start_radio()
    k=await message.reply_text(f"Started Radio: <code>{STREAM}</code>")
    await mp.delete(k)
    await mp.delete(message)

@Client.on_message(filters.command(['stopradio', f"stopradio@{USERNAME}"]) & admin_filter & (filters.chat(CHAT) | filters.private))
async def stop(_, message: Message):
    if Config.CPLAY:
        if 3 not in RADIO:
            k=await message.reply_text("It seems channel play is enabled and playlist is empty.\nUse /radio to restart the playout.")
            await mp.delete(k)
            await mp.delete(message)
            return
        else:
            k=await message.reply_text("It seems channel play is enabled.\nUse /clearplaylist to clear the playlist.")
            await mp.delete(k)
            await mp.delete(message)
            return 
    if 0 in RADIO:
        k=await message.reply_text("Kindly start Radio First /radio")
        await mp.delete(k)
        await mp.delete(message)
        return
    await mp.stop_radio()
    k=await message.reply_text("Radio stream ended.")
    await mp.delete(k)
    await mp.delete(message)
