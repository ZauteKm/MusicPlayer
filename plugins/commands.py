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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam MusicPlayer which plays music in Channels and Groups 24*7.\n\nI can even Stream Youtube Live in Your Voicechat.\n\nDeploy Your Own bot from source code below.\n\nHit /help to know about available commands.</b>"
HELP = """
**Common Commands:**
/play **[song name]/[yt link]**: Reply to an audio file.
/dplay **[song name]:** Play music from Deezer.
/yplay: To play all the songs of a youtube playlist.
/splay <code>song name</code> to play a song from Jio Saavn or
<code>/splay -a album name</code> to play all the songs from a jiosaavn album or
/cplay <channel username or channel id> to play music from a telegram channel.
/player:  Show current playing song.
/upload: Uploads current playing song as audio file.
/help: Show help for commands.
/playlist: Shows the playlist

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2.
**/cplay** Play music from a channel's music files.
**/yplay** Play music from a youtube playlist.
**/join**  Join voice chat.
**/leave**  Leave current voice chat
**/shuffle** Shuffle Playlist.
**/vc**  Check which VC is joined.
**/stop**  Stop playing.
**/radio** Start Radio.
**/stopradio** Stops Radio Stream.
**/clearplaylist** Clear the playlist.
**/export** Export current playlist for future use.
**/import** Import a previously exported playlist.
**/replay**  Play from the beginning.
**/clean** Remove unused RAW PCM files.
**/pause** Pause playing.
**/resume** Resume playing.
**/volume** Change volume(0-200).
**/mute**  Mute in VC.
**/unmute**  Unmute in VC.
**/restart**  Update and restarts the Bot.
"""




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("🔥 Source Code 🔥", url='https://github.com/ZauteKm/MusicPlayer'),
    ],
    [
        InlineKeyboardButton('👥 Group', url='https://t.me/iZaute/5'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/iZaute/6'),
    ],
    [
        InlineKeyboardButton('🆘 Help & Commands 🆘', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("🔥 Source Code 🔥", url='https://github.com/ZauteKm/MusicPlayer'),
        ],
        [
            InlineKeyboardButton('👥 Group', url='https://t.me/iZaute/5'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/iZaute/6'),
        ],
        [
            InlineKeyboardButton('🔰 How to Deploy 🔰', url='https://t.me/c/josprojects/131'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
