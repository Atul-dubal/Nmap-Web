import os 
import os.path
from os.path import *
from config.check_package import *
from config.style import color

#os.system("clear")
#atul=open("data/package.txt","a")
#print(os.path.exists("config/data/package"))
required_packages=["python","nmap","xsltproc","apache2","figlet"]

already_install=os.path.exists("config/data/package.txt")
data_path=os.path.exists("data")
newly_install=False

def reinstall_packages():
  
  for pkg in required_packages:
    newly_install=check_package(pkg)
    already_install=False
    os.system("touch config/data/package.txt")

if already_install==False or data_path==False:
  from config.reset import *
  reinstall_packages()

if newly_install==True or already_install==True and data_path==True:
  if already_install==False:
    os.system(" touch config/data/package.txt")
  
  packa=open("config/data/package.txt","w") 
  #for pkg in required_packages:
  packa.write("required_packages")
  print (date,"All Required Packages Are Now Installed ")
  
  print (date,bold+yellow+"Now Tool Is  Successfully Installed")
else:
  quit

figlet=os.system("figlet Nmap Web")
if figlet!=0:
  reinstall_packages()
  figlet=os.system("figlet Nmap Web")
  
print (green,"\nNow Tool Is Ready To Use \nUse Command ::-"+head+"python3 nmap_web.py\n")
