import socket
import re
import time
import json
from mcrcon import MCRcon

# Завантаження налаштувань з файлу config.json
def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

config = load_config()

# Налаштування Twitch
TWITCH_SERVER = "irc.chat.twitch.tv"
TWITCH_PORT = 6667
TWITCH_NICKNAME = config['twitch']['nickname']
TWITCH_TOKEN = config['twitch']['token']
TWITCH_CHANNEL = f"#{config['twitch']['channel']}"

# Налаштування RCON для Minecraft
MINECRAFT_RCON_HOST = config['rcon']['host']
MINECRAFT_RCON_PORT = config['rcon']['port']
MINECRAFT_RCON_PASSWORD = config['rcon']['password']
RCON_COMMAND_TEMPLATE = config['rcon']['command_template']

def send_rcon_command(command):
    try:
        with MCRcon(MINECRAFT_RCON_HOST, MINECRAFT_RCON_PASSWORD) as mcr:
            response = mcr.command(command)
            print(f"RCON Response: {response}")
    except Exception as e:
        print(f"RCON Error: {e}")

def connect_to_twitch():
    sock = socket.socket()
    sock.connect((TWITCH_SERVER, TWITCH_PORT))
    sock.send(f"PASS {TWITCH_TOKEN}\r\n".encode("utf-8"))
    sock.send(f"NICK {TWITCH_NICKNAME}\r\n".encode("utf-8"))
    sock.send(f"JOIN {TWITCH_CHANNEL}\r\n".encode("utf-8"))
    return sock

def main():
    sock = connect_to_twitch()
    while True:
        try:
            response = sock.recv(2048).decode("utf-8")
            if response.startswith("PING"):
                sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                match = re.search(r":(\w+)!.* PRIVMSG #[^ ]+ :(.*)\r\n", response)
                if match:
                    username, message = match.groups()
                    print(f"{username}: {message}")
                    rcon_command = RCON_COMMAND_TEMPLATE.replace("{user}", username).replace("{message}", message)
                    send_rcon_command(rcon_command)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)
            sock = connect_to_twitch()

if __name__ == "__main__":
    main()