#python pip -r requirets.txt
from os import system,path
from termcolor import cprint,colored

system("clear"),print("""\033[90m
___  ____       _       _   _                    
|  \/  (_)     | |     | | | |                   
| .  . |_ _ __ | |__   | |_| |_   _ _ __   __ _  
| |\/| | | '_ \| '_ \  |  _  | | | | '_ \ / _` | 
| |  | | | | | | | | | | | | | |_| | | | | (_| | 
\_|  |_/_|_| |_|_| |_| \_| |_/\__,_|_| |_|\__, | 
                                           __/ | 
                                          |___/  
\033[00m\033[91m
   __  ____       __       __  __                     
   /  |/  (_)___  / /_     / / / /_  ______  ____ _    
  / /|_/ / / __ \/ __ \   / /_/ / / / / __ \/ __ `/    
 / /  / / / / / / / / /  / __  / /_/ / / / / /_/ /     
/_/  /_/_/_/ /_/_/ /_/  /_/ /_/\__,_/_/ /_/\__, /      
                                          /____/       
\033[00m\033[90m
.___  ___.  __  .__   __.  __    __      __    __   __    __  .__   __.   _______    
|   \/   | |  | |  \ |  | |  |  |  |    |  |  |  | |  |  |  | |  \ |  |  /  _____|   
|  \  /  | |  | |   \|  | |  |__|  |    |  |__|  | |  |  |  | |   \|  | |  |  __     
|  |\/|  | |  | |  . `  | |   __   |    |   __   | |  |  |  | |  . `  | |  | |_ |    
|  |  |  | |  | |  |\   | |  |  |  |    |  |  |  | |  `--'  | |  |\   | |  |__| |    
|__|  |__| |__| |__| \__| |__|  |__|    |__|  |__|  \______/  |__| \__|  \______| \033[00m\n""")
End="\n"+"\033[95m\033[01m#"*50+"\033[00m\n"

def pather(file,cloner):
	if path.exists(file):  cprint("[++] "+file+ " already installed","green",attrs=["bold"])
	else:	system(f"sudo git clone {cloner}"),cprint("[++] "+file+" installed successfully","green",attrs=["bold"],end=End)

cprint("[+] Installing MHung...","cyan",attrs=["bold"]),pather("0.1ArafaDoS","https://github.com/mhungdzai/mhungdzais1.git")
cprint("[+] Installing slowloris...","cyan",attrs=["bold"]),system("sudo pip3 install slowloris"),cprint("[++] slowloris installed successfully","green",attrs=["bold"],end=End)
cprint("[+] Installing goldeneye...","cyan",attrs=["bold"]),system("sudo apt install goldeneye"),cprint("[++] goldeneye installed successfully","green",attrs=["bold"],end=End)
cprint("[+] Installing torshammer...","cyan",attrs=["bold"]),pather("torshammer","https://github.com/mhungdzai/mhungdzais1.git")
cprint("[+] Installing XERXES...","cyan",attrs=["bold"]),pather("XERXES","https://github.com/mhungdzai/mhungdzais1.git"),system("cd XERXES&&gcc -o xerxes xerxes.c&&cd ..")
rudy_issue="\033[96m[!] If rudy isn't installed, use a VPN like openvpn or nipe and run this command ' sudo npm install -g rudyjs '\033[00m"
cprint("[+] Installing rudy...","cyan",attrs=["bold"]),system("sudo npm install -g rudyjs"),cprint("[++] rudy installed successfully\n","green",attrs=["bold"],end=rudy_issue+End)
cprint("\n"+" "*5+"#"*5+" "*3,"white",attrs=["bold"],end=""),cprint("This tool is designed for ethical purpose, I'm not responsible for any unethical activity","blue",attrs=["bold","blink"],end=""),cprint(" "*3+"#"*5+"\n","white",attrs=["bold"])

#By: Nguyen Minh Hung(MHung)
#Age: 17