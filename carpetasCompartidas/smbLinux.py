

#!/bin/python3

# Para escanear y recolectar la informacion de las carpetas compartidas en una red local
# Por cuestion de manipulacion se esta guardando todos los datos en un sql
# Se registra la ruta completa las carpetas de esa ruta los archivos y si tiene permiso o no de escritura. 
# Creacion de los datos de la tabla
#create database red;
#create table compartidos( id serial, ip varchar(15), link text, carpetas text, archivos text, fecha date, escritura varchar(5));
#Ejecucion
#python3 smbWin.py 192.168.1.0/24

#!/bin/python3

import nmap
import win32net
import os
import sys
import datetime
import sqlite3

conn = sqlite3.connect('soyBett0.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS compartidos (
        id INTEGER PRIMARY KEY,
        ip TEXT, link TEXT, carpetas TEXT, archivos TEXT, fecha DATE, escritura TEXT
    )
''')
conn.commit()

    
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
  #cursor = conn.cursor()
  try:
    folders, _, _ = win32net.NetShareEnum(ip, 0)
    for folder  in folders:
      route = folder['netname']
      print("\t\t\t "+route)
      for paths, binders, files in os.walk(rf'\\{ip}\{route}'):
        path    = paths
        binder  = binders
        file    = files 
        timer   = str( datetime.datetime.now() )
        write   = isWritable( path )
        
        cursor.execute("INSERT INTO compartidos(ip, link, carpetas, archivos, fecha, escritura) VALUES (?, ?, ?, ?, ?, ?)", (ip, str(path), str(binder), str(file), timer, write) )
        
        #sql = "INSERT INTO compartidos(ip, link, carpetas, archivos, fecha, escritura) VALUES("+ip+", "+str(path)+", "+str(binder)+", "+str(file)+", "+timer+", "+write+")"
        #print(sql)
        
        conn.commit()
  except sqlite3.Error as e:
    print(f"[-] ERROR: --{ip}")
    print(e)
  conn.close()
  
print("By SoyBett0")
print("===========") 
                      
#Tus direcciones IP que no quieres que escane
lists = ['192.168.1.100']

def main():
  nm = nmap.PortScanner()
  print(str(sys.argv[1]))
  list = str(sys.argv[1])
  print("Escaneando VLAN: "+ list + " en: " + str( datetime.datetime.now() ) )
  lan = nm.scan(hosts=str(list), arguments='-p 445 --open')
  ips = lan['scan']
  for ip in ips:
    print('\t [.]... ' + ip)
    if ip not in lists:  #Tus Ip's
      print('\t\t [+] -->>' + ip)
      fileSharing( str(ip) )
     
if __name__ == "__main__":
  main()
  