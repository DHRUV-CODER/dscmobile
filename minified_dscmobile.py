h='op'
g='-'
f='*'
T='d'
S='#'
R=True
C=print
import websocket as U,colorama as A,json as L,threading as V,time
from getpass import getpass as W
import sys as H
A.init(R)
F=A.Fore.RED
M=A.Fore.LIGHTGREEN_EX
J=A.Fore.CYAN
B=A.Fore.RESET
G=A.Fore.LIGHTYELLOW_EX
N=A.Fore.CYAN+A.Style.BRIGHT
X=A.Fore.LIGHTGREEN_EX+A.Style.BRIGHT
I=A.Fore.RED+A.Style.BRIGHT
i=A.Fore.LIGHTYELLOW_EX+A.Style.BRIGHT
def Y(arg):return f"{X}\n[{arg}] {B}"
def Z(arg):return f"{I}\n[{arg}] {B}"
def D(arg):return f"{G}\n[{arg}] {B}"
a=M+A.Style.BRIGHT+ """
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
""" + B
b=f"{J}\nCredits: @DHRUV-CODER"+B
C(a,b)
C(D(S)+f"{I}Use it only on Bot accounts , Using it on Users account is {F}against Discord TOS"+D(S)+f"{J}Welcome , Using this CLI you can display your Bots status as mobile")
C('\n\nInstructions:\n'+D(f)+f"{G}Run the script till the time you want to display , press {F}ctrl+c{G} to gracefully close the session"+D(f)+f"{M}Have Fun , Flex hard{B}")
try:O=W(Y('+')+f"{G}Enter your Bot's Token here {F}[Hidden]{B}: {B}")
except:C('\n'+D(g)+f"{F}Keyboard Interrupt.{B}");H.exit()
if not O:C(Z(g)+'{R}Empty Input'+B);H.exit()
C(D(S)+f"{N}Running...{B}")
C(f"\n{I}[!]{N} Ctrl + C to exit.{B}")
def P(ws,request):ws.send(L.dumps(request))
def Q(ws):
	A=ws.recv()
	if A:return L.loads(A)
def c(interval,ws):
	while R:time.sleep(interval);A={h:1,T:'null'};P(ws,A)
E=U.WebSocket()
E.connect('wss://gateway.discord.gg/?v=6&encording=json')
K=Q(E)
d=K[T]['heartbeat_interval']/1000
V._start_new_thread(c,(d,E))
e={h:2,T:{'token':O,'properties':{'$os':'android','$browser':'Discord iOS','$device':'discord.py'}}}
P(E,e)
while R:
	try:
		K=Q(E)
		if not K:C(f"\n{G}[!] {I}Error Ocurred , Perhaps Invalid Token{B}");H.exit()
		input()
	except KeyboardInterrupt:C(f"\n{F}[!]{J} Keyboard Interrupt.{B}");E.close(status=1000);C(D('Session closed successfully'));H.exit()