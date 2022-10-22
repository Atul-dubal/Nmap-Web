import datetime

class bcolors:
    HEADER = '\033[95m'    #voilet
    OKBLUE = '\033[94m'    #blue
    OKCYAN = '\033[96m'    #cyan
    OKGREEN = '\033[92m'   #green
    WARNING = '\033[93m'   #yellow
    FAIL = '\033[91m'     # red
    ENDC = '\033[0m'      #white
    BOLD = '\033[1m'      #white bold
    UNDERLINE = '\033[4m'  #white underline 
    
color=bcolors()

white=color.ENDC
head=color.HEADER
blue=color.OKBLUE
cyan=color.OKCYAN
green=color.OKGREEN
red=color.FAIL
yellow=color.WARNING
bold=color.BOLD
underline=color.UNDERLINE

#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)


date=datetime.datetime.now()

#print(blue+str(date()))
date1 =str(date.hour)+"-"+str(date.minute)+"-"+str(date.second)+white
date=bold+green+"["+cyan+str(date)+green+bold+"]"