# Twitch-Minecraft bot
### Installation
- Get the latest release - https://github.com/jdayamx/twitch_minecraft_bot/releases/latest
- Install module `pip install mcrcon`
- configure file config.json
`
{
  "twitch": {
    "nickname": "Your nickname here",
    "token": "oauth:Your token here",
    "channel": "Your channel here"
  },
  "rcon": {
    "host": "Your minecraft host server here",
    "port": 25575,
    "password": "Your minecraft rcon password here",
    "command_template": "title @a actionbar {\"text\":\"{user} says: {message}\", \"color\":\"green\"}"
  }
}
`
- run bot `python twitch_bot.py`
