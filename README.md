# Telegram Voice Chat Bot with Channel Support.

A Telegram Bot to Play Audio in Voice Chats.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/ZauteKm/tgvc-musicplayer)

# Heroku Vars:
1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `BOT_TOKEN` : @Botfather
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/generate-pyrogram-session-string#main.py)
5. `CHAT` : ID of Channel/Group where the bot plays Music.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
7. `ADMINS` : ID of users who can use admin commands.
8. `STREAM_URL` : Stream URL of radio station to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically.)  
- To play a song just send the audio file to Bot or reply  to an audio with `/play` to start playing it in the voice chat.
- Use /help to know about other commands.

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist to
- ensure smooth playing
- Show current playing position of the audio

## Credits 
- This one is completly based on work of [Dash Eclipse's](https://github.com/dashezup) [tgvc-userbot](https://github.com/callsmusic/tgvc-userbot). I just added Bot and Channel support.

