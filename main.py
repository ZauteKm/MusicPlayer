from pyrogram import Client, idle, filters
import os
from threading import Thread
import sys
from config import Config
from utils.vc import mp
import asyncio


CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
async def main():
    async with bot:
        await mp.startupradio()
        await asyncio.sleep(5)
        await mp.startupradio()

def stop_and_restart():
        bot.stop()
        os.execl(sys.executable, sys.executable, *sys.argv)
    
bot.run(main())
bot.start()
@bot.on_message(filters.command("restart") & filters.user(Config.ADMINS))
def restart(client, message):
    message.reply_text("Restarting...")
    Thread(
        target=stop_and_restart
        ).start()

idle()
bot.stop()
