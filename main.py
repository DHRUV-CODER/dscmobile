import websocket  # pip install websocket-client
import colorama as c  # pip install colorama
import json
import threading
import time
from getpass import getpass  # To hide the token
import sys

c.init(True)

R = c.Fore.RED
G = c.Fore.LIGHTGREEN_EX
C = c.Fore.CYAN
W = c.Fore.RESET
Y = c.Fore.LIGHTYELLOW_EX
BCyan = c.Fore.CYAN + c.Style.BRIGHT
BGreen = c.Fore.LIGHTGREEN_EX + c.Style.BRIGHT
BRed = c.Fore.RED + c.Style.BRIGHT
BYellow = c.Fore.LIGHTYELLOW_EX + c.Style.BRIGHT


def plus_box_green(arg):
    return f"{BGreen}\n[{arg}] {W}"


def plus_box_red(arg):
    return f"{BRed}\n[{arg}] {W}"


def plus_box_yellow(arg):
    return f"{Y}\n[{arg}] {W}"



TITLE = G + c.Style.BRIGHT + """
▓█████▄   ██████  ▄████▄      ███▄ ▄███▓ ▒█████   ▄▄▄▄    ██▓ ██▓    ▓█████ 
▒██▀ ██▌▒██    ▒ ▒██▀ ▀█     ▓██▒▀█▀ ██▒▒██▒  ██▒▓█████▄ ▓██▒▓██▒    ▓█   ▀ 
░██   █▌░ ▓██▄   ▒▓█    ▄    ▓██    ▓██░▒██░  ██▒▒██▒ ▄██▒██▒▒██░    ▒███   
░▓█▄   ▌  ▒   ██▒▒▓▓▄ ▄██▒   ▒██    ▒██ ▒██   ██░▒██░█▀  ░██░▒██░    ▒▓█  ▄ 
░▒████▓ ▒██████▒▒▒ ▓███▀ ░   ▒██▒   ░██▒░ ████▓▒░░▓█  ▀█▓░██░░██████▒░▒████▒
 ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░   ░ ▒░   ░  ░░ ▒░▒░▒░ ░▒▓███▀▒░▓  ░ ▒░▓  ░░░ ▒░ ░
 ░ ▒  ▒ ░ ░▒  ░ ░  ░  ▒      ░  ░      ░  ░ ▒ ▒░ ▒░▒   ░  ▒ ░░ ░ ▒  ░ ░ ░  ░
 ░ ░  ░ ░  ░  ░  ░           ░      ░   ░ ░ ░ ▒   ░    ░  ▒ ░  ░ ░      ░   
   ░          ░  ░ ░                ░       ░ ░   ░       ░      ░  ░   ░  ░
 ░               ░                                     ░                    
""" + W

CREDITS = f"{C}\nCredits: @DHRUV-CODER" + W

print(TITLE, CREDITS)

print(plus_box_yellow("#") + f"{BRed}Use it only on Bot accounts , Using it on Users account is {R}against Discord TOS" +
      plus_box_yellow('#') + f"{C}Welcome , Using this CLI you can display your Bots status as mobile")
print("\n\nInstructions:\n"+plus_box_yellow('*') + f"{Y}Run the script till the time you want to display , press {R}ctrl+c{Y} to gracefully close the session" +
      plus_box_yellow('*') + f"{G}Have Fun , Flex hard{W}")
try:
    TOKEN = getpass(plus_box_green("+") +
                    f"{Y}Enter your Bot's Token here {R}[Hidden]{W}: {W}")
except:
    print('\n' + plus_box_yellow("-") + f'{R}Keyboard Interrupt.{W}')
    sys.exit()

if not TOKEN:
    print(plus_box_red("-") + "{R}Empty Input" + W)
    sys.exit()

print(plus_box_yellow("#")+f"{BCyan}Running...{W}")
print(f'\n{BRed}[!]{BCyan} Ctrl + C to exit.{W}')


def send_json_request(ws, request):
    ws.send(json.dumps(request))


def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)


def heartbeat(interval, ws):
    # print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        # print("Heartbeat sent")


ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

payload = {
    "op": 2,
    "d": {
        "token": TOKEN,
        "properties": {
            '$os': "android",
            '$browser': 'Discord iOS',
            '$device': 'discord.py',
        }
    }
}

send_json_request(ws, payload)

while True:
    try:
        event = recieve_json_response(ws)
        if not event:
            print(f"\n{Y}[!] {BRed}Error Ocurred , Perhaps Invalid Token{W}")
            sys.exit()
        input()
    except KeyboardInterrupt:
        print(f'\n{R}[!]{C} Keyboard Interrupt.{W}')
        ws.close(status=1000)
        print(plus_box_yellow("Session closed successfully"))
        sys.exit()
