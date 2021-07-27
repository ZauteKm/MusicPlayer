# VCMusicPlayer v3.0

- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.
- A Telegram Bot to Play Audio in Voice Chats With Youtube and Deezer support.
- Supports Live streaming from YouTube.


## NOTE:

- Make sure you have started a VoiceChat in your Group before deploying.

## Deploy to VPS
```sh
git clone https://github.com/LushaiMusic/VCMusicPlayer
cd VCMusicPlayer
pip3 install -r requirements.txt
# <Create Variables appropriately>
python3 main.py
```


## Deploy to Qovery

<p align="left">
  <a href="https://qovery.com">
     <img height="30px" src="https://img.shields.io/badge/Deploy%20To%20Qovery-blueviolet?style=for-the-badge&logo=qovery">
  </a>
</p>


## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/LushaiMusic/VCMusicPlayer)

<a href="https://youtu.be/FKaAU4Pr2bw"><img src="https://img.shields.io/badge/How%20to%20Deploy%20on%20Heroku-blue.svg?logo=Youtube"></a>

<a href="https://youtu.be/FKaAU4Pr2bw"><img src="https://img.shields.io/youtube/views/FKaAU4Pr2bw?style=social">


## Configs Vars:
1. `API_ID` : [my.telegram.org](https://my.telegram.org/app)
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org/app)
3. `BOT_TOKEN` : Get From [@Botfather](https://telegram.dog/BotFather)
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/GenerateStringSession)
5. `CHAT` : ID of Channel/Group where the bot plays Music.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
7. `ADMINS` : ID of users who can use admin commands.
8. `ARQ_API` : Get it for free from [@ARQRobot](https://telegram.dog/ARQRobot), This is required for /dplay to work.
9. `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command. Some Streaming Links [Click here.](https://t.me/c/1481808444/143)
10. `MAXIMUM_DURATION` : Maximum duration of song to play.(Optional)
11. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature. 
12. `ADMIN_ONLY` : Pass `Y` If you want to make /play and /dplay commands only for admins of `CHAT`. By default /play and /dplay is available for all.

- Enable the worker after deploy the project to Heroku
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy.(24*7 Music even if heroku restarts, radio stream restarts automatically.)  
- To play a song use /play as a reply to audio file or a youtube link.
- Use /play <song name> to play song from youtube and /dplay <song name> to play from Deezer.
- Use /help to know about other commands.

## Features
- Playlist, queue
- Supports Live streaming from youtube
- Supports both deezer and youtube to search songs.
- Play from telegram file supported.
- Starts Radio after if no songs in playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing
- Automatic restart even if heroku restarts.

#### Support
Join Now Telegram [VC Music Live Sets](https://t.me/c/1481808444/131)

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/UsePyrogramBot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## License
```sh
VC Music Player, Telegram Voice Chat Userbot
Copyright (C) 2021  Zaute Km

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
```

## Credits

- [Zaute Km](https://github.com/ZauteKm) [Dev]
- [Dash Eclipse](https://github.com/dashezup) [For tgvc_userbot]
- [Marshal X](https://github.com/MarshalX) [For pytgcalls]
