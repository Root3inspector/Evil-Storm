#!bin/bash


if (($EUID != root))
  then echo "Please run as root"
  exit

  else 
  sudo apt-get install hostapd
  sleep 1
  sudo apt-get install dnsmask
  sleep 2
  sudo apt-get install gnome-terminal
  sleep 2
  sudo apt-get install dnsspoof
  sleep 3
  echo "[+]creating Folder"
  mkdir /root/accesspoint
  echo "[+] Fineched"

fi

exit

