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

### Compilation
For create a compile version you need:
- linux  `pip install pyinstaller` and make dist `pyinstaller --onefile twitch_bot.py`
- windows `C:\Python\python.exe -m pip install pyinstaller` and make dist `C:\Python\Scripts\pyinstaller.exe --onefile twitch_bot.py`
File created in subdirectory dist, copy file from dist folder to main folder near `twitch_bot.py`.

### Command sample
- Spawn zombie `execute as @a at @s run summon minecraft:zombie ~ ~ ~ {CustomName:\"\\\"{user}\\\"\",CustomNameVisible:1b,ArmorItems:[{},{},{},{id:\"minecraft:leather_helmet\",Count:1b}]}` put in your config  "command_template": "COMMAND_HERE"
- Spawn bee `execute as @a at @s run summon minecraft:bee ~ ~ ~ {CustomName:\"\\\"{user}\\\"\",CustomNameVisible:1b,ArmorItems:[{},{},{},{id:\"minecraft:leather_helmet\",Count:1b}]}`
