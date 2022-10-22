import os
from config.style import *
from config.style import *
from config.nmap_start import start,restart
import sys

if os.path.exists("data/")!=True:
  print (red+"data Directory Not Found. Plz update Tools")
  print (yellow+"For Updation Run ::- "+head+"python3 setup.py")
  quit()

if len(sys.argv) > 1:
  cmd=sys.argv
  #print ("All Flags",cmd)
  
  cmd.remove(sys.argv[0])
  #print (cmd)
  if "-h" in cmd[0] or "--help" in cmd[0]:
    os.system(" cat config/data/help.txt")
  elif "--update" in cmd[0] or "-u" in cmd[0]:
    os.system("python setup.py")
  else:
    start(" ".join(cmd))
else:
  os.system("clear")

  print(yellow)
  os.system("figlet Nmap Web")
  print(white)
  
  print(cyan+'''Copyright © Nmap.org || All Rights Are Reserved By Nmap.org \n \nAuthor ::- Atul Dattatray Dubal \n''')
  
  print("Starting At @",date +"\n\n",white)

  
  while True:
    print (head+'''1) Start\n \n2) Update \n\n3) Help\n\n4) Exit \n'''+yellow)
  
    choice = input("What You Want To Do ::- ")
    if choice=="1" or choice=="":
      IP = input("Enter IP ADDRESS to Perform Nmap Scan ::- ")
      Flags=input("Enter Flags For Better Result ::- ")
      filename="nmap_web.xml"
      cmd = str(IP)+str(Flags)
      start(cmd)
      
    elif choice=="2":
      os.system("python setup.py")
      restart()
    elif choice=="3":
      os.system(" cat config/data/help.txt")
      restart()
    elif choice=="4":
      quit()
    else:
      print(bold+red+"\n[ Error ] :"+white+red+"choose correct option"+bold+" \'Invalid Option\' \n"+white)
      loop==1
      
     
    
    