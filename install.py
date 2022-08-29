import os 
import time


 # you need to add check root previllage


# os.system("sudo apt-grt update")
os.system("sudo apt-get install hostapd")
time.sleep(2)
os.system("sudo apt-get install dnsmask")
time.sleep(1)

os.system("mkdir /root/accesspoint")

