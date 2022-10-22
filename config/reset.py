import os
from config.style import * 

rmv_dir = os.system("rm -rf data")
mk_dir = os.system("mkdir data")
mk_cach = os.system("mkdir data/cache")

if mk_dir != 0:
  os.system("rm -rf data")
  os.system("mkdir data")
print(date+" data Directory is Successful Created")

if mk_cach != 0:
  os.system("rm -rf data")
  os.system("mkdir data && mkdir data/cache")
print(date,"Cache Directory is Successful Created")
