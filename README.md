# Twitch-Minecraft bot
### Installation python for Windows
- Download python https://www.python.org/downloads/windows/
- Install python in directory `C:\python` use custom installation case
- Run `Win + R` and type `cmd` after type `cd C:\python`
- Run command `python.exe -m pip install --upgrade pip`
- Run command `python.exe -m pip install mcrcon`
- Download and unpack twitchbot as sample in `C:\python\twitch_minecraft_bot-start`
- Run command `cd C:\python\twitch_minecraft_bot-start`
- Make all configuration in `config.json`
- Run bot `C:\python\python.exe twitch_bot.py`

### Installation
- Get the latest release - https://github.com/jdayamx/twitch_minecraft_bot/releases/latest
- Install module `pip install mcrcon`
- configure file config.json
```
{
  "twitch": {
    "nickname": "Your nickname here",
    "token": "oauth:Your ACCESS TOKEN here",
    "channel": "Your channel here"
  },
  "rcon": {
    "host": "Your minecraft host server here",
    "port": 25575,
    "password": "Your minecraft rcon password here",
    "command_template": "title @a actionbar {\"text\":\"{user} says: {message}\", \"color\":\"green\"}"
  }
}
```
- run bot `python twitch_bot.py`
### Get Auth tiken
- Visit https://twitchtokengenerator.com/
- enable chat:read button
- click on "Generate Token!"
- copy "ACCESS TOKEN" to config.json file
