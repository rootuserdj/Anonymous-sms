import requests
from os import system
system("clear")

#colours
red = "\033[91;1m"
green = "\033[92;1m"
yellow = "\033[93;1m"
blue = "\033[94;1m"




#banner


print(red +"                ███████╗███╗   ███╗███████╗")
print(red +"                ██╔════╝████╗ ████║██╔════╝")
print(red +"                ███████╗██╔████╔██║███████╗")
print(red +"                ╚════██║██║╚██╔╝██║╚════██║")
print(red +"                ███████║██║ ╚═╝ ██║███████║")
print(red +"                ╚══════╝╚═╝     ╚═╝╚══════╝")


print(blue +"      ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ ")
print(blue +"      ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗")
print(blue +"      ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝")
print(blue +"      ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")
print(blue +"      ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║")
print(blue +"      ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
print(red +"     <<═══════════════════════════════════════════════>>")
print(green +"     <═══════════════> Made By HACKERDJ <══════════════>")
print(red +"     <<═══════════════════════════════════════════════>>")
                                                  
print( green +"")
                                                  




num = input("[+] Enter The Mobile Number With Contry Code: ")

print(yellow +"")

msg = input("[+] Enter The Text Message: ")

resp = requests.post('https://textbelt.com/text', {
  'phone': num,
  'message': msg,
  'key': 'textbelt',
})
try:
    resp.json()
    print(green + " Message Sent Sucessful")
except:
    print("First You Have To Install requests: pip install requests ")

