import os 


def start(cmd):
  nmap_result=os.system("nmap "+str(cmd)+" -oX data/nmap_web.xml ")
  if nmap_result==0:
    server=os.system("xsltproc data/nmap_web.xml -o data/nmap_web.php && cd data/") 
    server2=os.system("php -S localhost:2206 & > data/cache/.cache")
    if server==0 and server2==0:
      os.system("ls > data/cache/.cache && sleep 5")
      os.system("xdg-open http://localhost:2206/nmap_web.php ")
    
  
def restart():
    back=input("You Want To Go Back ? [Y/N] ")
    if back=="y" or back=="Y" or back=="":
      os.system("python3 nmap_web.py")
    else:
      quit()
    