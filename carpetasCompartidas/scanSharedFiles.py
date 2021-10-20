#!/bin/python3

# Para escanear y recolectar la informacion de las carpetas compartidas en una red local
# Por cuestion de manipulacion se esta guardando todos los datos en un sql
# Se registra la ruta completa las carpetas de esa ruta los archivos y si tiene permiso o no de escritura. 
# Creacion de los datos de la tabla
#create database red;
#create table compartidos( id serial, ip varchar(15), link text, carpetas text, archivos text, fecha date, escritura varchar(5));

import nmap
import win32net
import logging
import os
import datetime

logging.basicConfig(level=logging.DEBUG,filename= str( datetime.datetime.now().strftime("%d%m%Y%H%M%a") )+".sql",filemode='w')
    
def isWritable(path):
  try:
    file = "\\bett0.txt"
    pathFull = path + file
    fileInShared = os.open( pathFull, os.O_RDWR|os.O_CREAT )
    os.close( fileInShared )
    os.remove( pathFull )
    return "SI"
  except:
    return "NO"
  
def fileSharing(ip):
  try:
    folders, _, _ = win32net.NetShareEnum(ip, 0)
    for folder  in folders:
      route = folder['netname']
      for paths, binders, files in os.walk(rf'\\{ip}\{route}'):
        path    = paths
        binder  = binders
        file    = files 
        timer   = str( datetime.datetime.now() )
        write   = isWritable( path )
        sql     = rf"insert into compartidos(ip, link, carpetas, archivos, fecha, escritura) values($|${ip}$|$, $|${path}$|$, $|${binder}$|$, $|${file}$|$, $|${timer}$|$, $|${write}$|$);"
        logging.info(sql)
  except:
    timer = str(datetime.datetime.now())
    sql   = rf"insert into compartidos(ip, link, carpetas, archivos, fecha, escritura) values($|${ip}$|$, $|$null$|$, $|$null$|$, $|$null$|$, $|${timer}$|$, $|$null$|$);"
    logging.error(sql)
    print("\t\t [-] NO " + ip)

print(" __  __  ___  _  _ ___ _____ ___  ___   ___  ___    ___   _   ___ ___ ___ _____ _   ___    ___ ___  __  __ ___  _   ___ _____ ___ ___   _   ___  ")
print("|  \/  |/ _ \| \| |_ _|_   _/ _ \| _ \ |   \| __|  / __| /_\ | _ | _ | __|_   _/_\ / __|  / __/ _ \|  \/  | _ \/_\ | _ |_   _|_ _|   \ /_\ / __| ")
print("| |\/| | (_) | .` || |  | || (_) |   / | |) | _|  | (__ / _ \|   |  _| _|  | |/ _ \\__ \ | (_| (_) | |\/| |  _/ _ \|   / | |  | || |) / _ \\__ \ ")
print("|_|  |_|\___/|_|\_|___| |_| \___/|_|_\ |___/|___|  \___/_/ \_|_|_|_| |___| |_/_/ \_|___/  \___\___/|_|  |_|_|/_/ \_|_|_\ |_| |___|___/_/ \_|___/ ")
print(" ")
print(" ")
print("By Bett0 V1")
print(" ")
print(" ")                          

lists = [
          '192.168.1.0/24', '192.168.2.0/24'
         ]

def main():
  nm = nmap.PortScanner()  
  for list in lists:
      print("Escaneando VLAN: "+ list + " en: " + str( datetime.datetime.now() ) )
      lan = nm.scan(hosts=str(list), arguments='-p 445 --open')
      ips = lan['scan']
      for ip in ips:
        print('\t [+] ... ' + ip)
        if ip != "192.168.1.69":  #Tu Ip para que no saque tu info XD
          fileSharing(ip)
     

if __name__ == "__main__":
  main()
