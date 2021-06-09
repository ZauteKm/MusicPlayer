# Music Player - v2

- An Telegram Bot to Play Radio/Music in Channel or Group Voice Chats.

## How to deploy 

Click the below button to watch the video tutorial on deploying

<a href="https://youtu.be/FGZr-V2lCo8"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/FGZr-V2lCo8"><img src="https://img.shields.io/youtube/views/FGZr-V2lCo8?style=social">

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/InFoJosTel/VCMusicPlayer)

# Configs Vars:
1. `API_ID` : Get From [my.telegram.org](https://my.telegram.org) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot).
2. `API_HASH` : Get from [my.telegram.org](https://my.telegram.org) or [@UseTGzKBot](https://telegram.dog/UseTGzKBot).
3. `BOT_TOKEN` : [@Botfather](https://t.me/BotFather).
4. `SESSION_STRING` : Generate From here [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://replit.com/@ZauteKm/GenerateStringSession)
5. `CHAT` : ID of Channel/Group where the bot plays Music. Channel ID Get From [@UseTGidBot](https://t.me/UseTGidBot).
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group
7. `ADMINS` : ID of users who can use admin commands.
8. `STREAM_URL` : Stream URL of radio station to stream when the bot starts or with /radio command.

- Enable the worker after deploy the project to Heroku.
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy. 
- 24x7 Music even if heroku restarts, radio stream restarts automatically.  
- To play a song just send the audio file to Bot or reply to an audio with `/play` to start playing it in the voice chat.
- To download audio you can use [@ZKSongBot](http://t.me/ZKSongBot) or `/song` command to the bot.
- Use `/help` to know about other commands & its usage.

**Features**

- Playlist, queue, 24x7 radio stream.
- Loop one track when there is only one track in the playlist.
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing.
- Show current playing position of the audio
- Control with buttons and commands.
- Download songs from YouTube as audio.

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/UsePyrogramBot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## Run On VPS (The Hard Way)

```sh
$ git clone https://github.com/InFoJosTel/VCMusicPlayer
$ cd VCMusicPlayer
$ sudo apt-get install ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
```
Edit **config.py** with your own values.

```sh
$ python3 main.py
```
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
