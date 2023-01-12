# UNO Bot

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](./LICENSE)

Telegram Bot that allows you to play the popular card game UNO via inline queries. The bot currently runs as [@unobot](http://telegram.me/unobot).

To run the bot yourself, you will need: 
- Python (tested with 3.4+)
- The [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) module
- [Pony ORM](https://ponyorm.com/)

## Setup
- Get a bot token from [@BotFather](http://telegram.me/BotFather) and change configurations in `config.json`.
- Convert all language files from `.po` files to `.mo` by executing the bash script `compile.sh` located in the `locales` folder.
  Another option is: `find . -maxdepth 2 -type d -name 'LC_MESSAGES' -exec bash -c 'msgfmt {}/unobot.po -o {}/unobot.mo' \;`.
- Use `/setinline` and `/setinlinefeedback` with BotFather for your bot.
- Use `/setcommands` and submit the list of commands in commandlist.txt
- Install requirements (using a `virtualenv` is recommended): `pip install -r requirements.txt`

## Run on Vps

- Clone Repository `https://github.com/Rexashh/unobottelegram && cd unobottelegram`
- bash script compile.sh :
- open locales `cd locales`
- bash `bash compile.sh`
- install req `pip install -r requirement.txt`
- build screen `screen -S uno`
- RUNING with `python3 bot.py`

You can change some gameplay parameters like turn times, minimum amount of players and default gamemode in `config.json`.
Current gamemodes available: classic, fast and wild. Check the details with the `/modes` command.

Code documentation is minimal but there.

I'm just a kangers not a maker

Original repos : 
[Jhoker](https://github.com/jh0ker/mau_mau_bot)
