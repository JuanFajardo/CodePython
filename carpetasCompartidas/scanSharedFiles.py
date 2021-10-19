#!/bin/python3
# Para escanear y recolectar la informacion de las carpetas compartidas en una red local
# Por cuestion de manipulacion se esta guardando todos los datos en un sql
# Se registra la ruta completa las carpetas de esa ruta los archivos y si tiene permiso o no de escritura. 
# Creacion de los datos de la tabla
#create database red;
#create table compartidos( id serial, ip varchar(15), link text, carpetas text, archivos text, fecha date, escritura varchar(5));

import nmap
import pip install pywin32pip install pywin32
import logging
import os
import datetime
logging.basicConfig(level=logging.DEBUG,filename='bett0.sql',filemode='w')

def isWritable(ruta):
  try:
    file = "\\h.txt" 
    path = os.path.join(ruta, file)
    fd = os.open( path, os.O_RDWR|os.O_CREAT )
    os.close( fd )
    os.remove(path)

    return "SI"
  except:
    return "NO"
  
def sharedFiles(remotehost):
  try:#12732886
    shares, _, _ = win32net.NetShareEnum(remotehost, 0)
    for share  in shares:
      rute = share['netname']
      for roots, dirs, files in os.walk(rf'\\{remotehost}\{rute}'):
        ruta  = roots
        direc = dirs
        archi = files
        reloj  = str(datetime.datetime.now())
        SePuedeEscribir = isWritable(ruta)
        if SePuedeEscribir == "SI":
          break
        sql = rf"insert into compartidos(ip, link, carpetas, archivos, fecha, escritura) values($|${remotehost}$|$, $|${ruta}$|$, $|${direc}$|$, $|${archi}$|$, $|${reloj}$|$, $|${SePuedeEscribir}$|$);"
        logging.info(sql)
  except:
    reloj  = str(datetime.datetime.now())
    sql = rf"insert into compartidos(ip, link, carpetas, archivos, fecha, escritura) values($|${remotehost}$|$, $|$null$|$, $|$null$|$, $|$null$|$, $|${reloj}$|$, $|$null$|$);"
    logging.error(sql)
    print("--- NO : " + remotehost)

nm = nmap.PortScanner()
listas = [#Debes añadir tu red o redes
          '192.168.1.0/24', '192.168.2.0/24'
          ]

if __name__ == "__main__":
  for lista in listas:
    aa = nm.scan(hosts=str(lista), arguments='-p 445 --open')
    ips = aa['scan']
    for remotehost in ips:
      if remotehost != "192.168.24.87":
        sharedFiles(remotehost)

#'192.168.27.42': {'hostnames': [{'name': '31A5898531A.bg.com.bo', 'type': 'PTR'}], 'addresses': {'ipv4': '192.168.27.42'}, 'vendor': {}, 'status': {'state': 'up', 'reason': 'echo-reply'}}, 
