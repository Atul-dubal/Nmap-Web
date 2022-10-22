import os
from config.style import *
package_installation_fail_time=1

def check_package(package_name):
  global package_installation_fail_time
  is_install=os.system("dpkg -s "+package_name+" >> data/cache/.cache")
  if is_install==0:
    
    x=(os.system("dpkg -s "+package_name+" | grep Version > data/cache/.cache"))
    f=open("data/cache/.cache","r");
    f=f.read()
    print(date,package_name," Is Already Installed 😇 with ",f)
    return True
  else:
    print (date,red+bold+package_name+" Is Not Installed")
    print(date,yellow+package_name," Installation Starting ....."+white)
    os.system("apt install "+package_name )
    if os.system("dpkg -s "+package_name+" | grep Version >> data/cache/.cache")==0:
      return True
    else:
     
      quit()