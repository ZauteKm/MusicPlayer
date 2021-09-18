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
from utils import USERNAME, GET_MESSAGE, PROGRESS
from config import Config
ADMINS=Config.ADMINS
CACHE={}
from pyrogram.errors import BotInlineDisabled

async def in_convo(_, client, message):
    try:
        k=Config.CONV.get(message.reply_to_message.message_id)
    except:
        return False
    if k and k == "START":
        return True
    else:
        return False

async def in_co_nvo(_, client, message):
    try:
        k=Config.CONV.get(message.reply_to_message.message_id)
    except:
        return False
    if k and k == "PLAYLIST":
        return True
    else:
        return False
async def is_reply(_, client, message):
    if Config.REPLY_MESSAGE:
        return True
    else:
        return False

start_filter=filters.create(in_convo)   
playlist_filter=filters.create(in_co_nvo) 
reply_filter=filters.create(is_reply)


@Client.on_message(filters.private & filters.chat(1328074332) & start_filter)
async def get_start(client, message):
    m=message.reply_to_message.message_id
    link=GET_MESSAGE.get(m)
    k=await client.send_message(chat_id="GetAPlayListBot", text=link)
    del Config.CONV[m]
    Config.CONV[k.message_id] = "PLAYLIST"
    command, user, url = link.split(" ", 3)
    GET_MESSAGE[k.message_id] = user


@Client.on_message(filters.private & filters.chat(1328074332) & playlist_filter)
async def get_starhhhht(client, message):
    m=message.reply_to_message.message_id
    user=GET_MESSAGE.get(m)
    nva=message
    if nva.text:
        error=nva.text
        if "PeerInvalid" in error:
            PROGRESS[int(user)]="peer"
        elif "kicked" in error:
            PROGRESS[int(user)]="kicked"
        elif "nosub" in error:
            PROGRESS[int(user)]="nosub"
        elif "Invalid Url" in error:
            PROGRESS[int(user)]="urlinvalid"
        else:
            PROGRESS[int(user)]=error
    elif nva.document:
        ya=await nva.download()
        PROGRESS[int(user)]=ya
    else:
        PROGRESS[int(user)]="Unknown Error"
    await client.read_history(1328074332)
    del GET_MESSAGE[m]
    del Config.CONV[m]

@Client.on_message(reply_filter & filters.private & ~filters.bot & filters.incoming & ~filters.service & ~filters.me & ~filters.chat([777000, 454000]))
async def reply(client, message): 
    try:
        inline = await client.get_inline_bot_results(USERNAME, "ORU_MANDAN_PM_VANNU")
        m=await client.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
        old=CACHE.get(message.chat.id)
        if old:
            await client.delete_messages(message.chat.id, [old["msg"], old["s"]])
        CACHE[message.chat.id]={"msg":m.updates[1].message.id, "s":message.message_id}
    except BotInlineDisabled:
        for admin in ADMINS:
            try:
                await client.send_message(chat_id=admin, text=f"Hey,\nIt seems you have disabled Inline Mode for @{USERNAME}\n\nA Nibba is spaming me in PM, enable inline mode for @{USERNAME} from @Botfather to reply him.")
            except Exception as e:
                print(e)
                pass
    except Exception as e:
        print(e)
        pass
