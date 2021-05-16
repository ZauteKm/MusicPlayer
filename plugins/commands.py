from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "Hello, [{}](tg://user?id={})\n\n I am Music Player bot which plays music in Channels and Groups 24*7"
HELP = """**Common Commands**:

**/play**  Reply with an audio to play/queue it, or show playlist
**/player**  Show current playing time of current track
**/help** Show help for commands
**/playlist** Shows the playlist.

**Admin Commands**:
**/skip** [n] ...  Skip current or n where n >= 2
**/join**  Join voice chat of current group
**/leave**  Leave current voice chat
**/vc**  Check which VC is joined
**/stop**  Stop playing
**/radio** Start Radio
**/stopradio** Stops Radio Stream
**/replay**  Play from the beginning
**/clean** Remove unused RAW PCM files
**/pause** Pause playing
**/resume** Resume playing
**/mute**  Mute the VC userbot
**/unmute**  Unmute the VC userbot
**/restart** Restarts the Bot
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('Support Channel', url='https://t.me/ZauteKm'),
        InlineKeyboardButton('Support Group', url='https://t.me/joinchat/7gSUxv6vgQE3M2Fl'),
    ],
    [
        InlineKeyboardButton('Bugs?', url='https://t.me/zautebot'),
        InlineKeyboardButton('Source', url='https://github.com/ZauteKm/tgvc-musicplayer'),
    ],
    [
        InlineKeyboardButton('Help', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    await message.reply_text(HELP)
