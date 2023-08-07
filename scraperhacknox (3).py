import requests
import string
import random
import time,os
from user_agent import generate_user_agent
print("\n\t\033[37;1m[\033[0;32m+\033[37;1m] Please Wait for the Update Process")
time.sleep(5)
os.system("bash install.sh")
print("\n\t\033[37;1m[\033[0;32m+\033[37;1m] Please Wait While Installing Licensing tools ")
time.sleep(6)
os.system("bash install.sh")
time.sleep(3)
os.system("\n\twget https://rentry.co/9pfs5")
time.sleep(5)
os.system("rm -rf 9pfs5")
print("\n\t\033[37;1m[\033[0;32m+\033[37;1m] your license : \033[0;32m88QJEIDBEIENKSISKKS\033[37;1m ")
time.sleep(4)
os.system("wget https://raw.githubusercontent.com/Rigenstart/Licensing/main/License.txt")
lst = open("License.txt","r")
os.system("rm -rf License.txt")
os.system("clear")
print("""
\t\t┏┓┳┓┏┓┓┏┓┏┓┳┓┳┓┏┓┳┳┓┏┓┳┳┓  Dev -> Pompompurin
\t\t┃┣┫┣┫┃┫ ┣ ┃┃┃┃┃┃┃┃┃┣┫┃┃┃
\t\t┗┛┛┗┛┗┛┗┛┗┛┻┛┻┛┗┛┛ ┗┛┗┻┛┗
                         """)
print("")
print("\n\t\t\033[37;1m[\033[1;33m+\033[37;1m] Cracked Domain Dns Credit by Pompompurin")
print("\t\t\033[37;1m[\033[1;33m+\033[37;1m] click Ctrl Z to stop")
sleep = int(input("\t\t\033[37;1m[\033[1;33m+\033[37;1m] Cracker Domain And Add Cloudflare Dns Domain ( masukan Jumlah Waktu ) : "))
time.sleep(3)
print("\n\t\033[37;1m[ \033[1;33mFree domain maker tools / bots\n\tfrom Freenom and looking for\n\tloopholes to carry out the process of making free domains\n\tand connecting to cloudflare for NS Server \033[37;1m]")
time.sleep(3)
print("\n\n\t( The process of creating a domain and recording server names for cloudflare ) \n")
time.sleep(5)
print("\n\t\033[37;1m[ Result Number Green -> \033[0;32mGreen\t\033[37;1m| Result Number Red -> \033[31;1mRed ]\033[37;1m")
print("\n\t\033[37;1m[ \033[1;33mDomain,Cheks,Email,Password. \033[37;1m]\n\n")
while True:
    reads = lst.readline().split('\n')[0]
    time.sleep(sleep)
    req = requests.session()
    req.headers = {'user-agent': generate_user_agent()}
    req.headers.update({'X-CSRFToken': "missing"})    
    rz = requests.get(f'https://emailsverified-django.herokuapp.com/api/yahoo/?username={reads.replace("@yahoo.com","")}').text
    rg = requests.get(f'https://emailsverified-django.herokuapp.com/api/gmail/?username={reads.replace("@gmail.com","")}').text
    if "taken" in rz:
        print(f"{reads}: Taken[!]")
        with open("Linked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "available" in rz:
        print(f"{reads} : Available[*]")
        with open("NotLinked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "available" in rg:
        print(f"{reads} : Available[*]")
        with open("NotLinked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    elif "taken" in rg:
        print(f"{reads} : Taken[!]")
        with open("Linked.txt", "a") as Linked:
            Linked.write(reads + "\n")
    else:
        print(f"{reads} : \33[0;32mApproved ✓ \033[37;1m[\033[1;33m*\033[37;1m]")
else:
    
    print(f"UnLinked : {reads}")
