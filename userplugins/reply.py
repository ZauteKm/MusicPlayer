
from pyrogram import Client, filters
from utils import USERNAME
from config import Config
ADMINS=Config.ADMINS
from pyrogram.errors import BotInlineDisabled
@Client.on_message(filters.private & ~filters.bot & filters.incoming & ~filters.service)
async def reply(client, message): 
    try:
        inline = await client.get_inline_bot_results(USERNAME, "ORU_MANDAN_PM_VANNU")
        await client.send_inline_bot_result(
            message.chat.id,
            query_id=inline.query_id,
            result_id=inline.results[0].id,
            hide_via=True
            )
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
