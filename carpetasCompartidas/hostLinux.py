#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import tkinter as tk
import subprocess
import mysql.connector
from datetime import datetime

cn = mysql.connector.connect( host="192.168.1.8", database="carpetas", user="bett0", password="123")
ips = "192.168.1.0/24"


def window(msj):	
	root = tk.Tk()
	root.title("SoyBett0")
	root.geometry("300x200")
	label = tk.Label(root, text=msj)	
	label.pack(padx=20, pady=50)
	root.mainloop()
	
def agregar(ip, mac, estado):
	cursor = cn.cursor()
	fecha = datetime.now()
	sql = "INSERT INTO direcciones(ip, mac, fecha, estado) VALUES(%s, %s, %s, %s)"
	cursor.execute(sql, (ip, mac, fecha, estado))
	cn.commit()
	cursor.close()
        
def lista():
	cursor = cn.cursor()
	query = "SELECT * FROM direcciones"
	cursor.execute(query)
	datos = cursor.fetchall()
	cursor.close()
	return datos

    
def verificar(ip, mac, estado):
	#estado = Intruso, Agregar
	if(estado == "Agregar"):
		agregar(ip, mac, estado)
		print("ya se ingreso los hosts ")		
	elif(estado == "SoyBett0"):
		datos = lista()
		contador = 0
		for fila in datos:
			if str(ip) in str(fila) and str(mac) in str(fila) and "Agregar" in str(fila):
				contador = 69
				pass
		if contador == 0:
			agregar(ip, mac, "INTRUSO")
			#window("La direccion "+str(ip)+":"+str(mac)+" es INTRUSO")
			print("La direccion "+str(ip)+" - "+str(mac)+" es INTRUSO")
	else:
		print("Un gusto XD")
		
	
def arp_scan(ips, estado):
	salida = subprocess.check_output(["/sbin/arp-scan", ips, "-q", "-x"])
	salida = salida.decode("utf-8")
	datos = salida.split('\n')
	for dato in datos:
		if len(dato) > 16:
			ip = dato.split('\t')[0]
			mac =dato.split('\t')[1]
			verificar(ip, mac, estado)
	print("Revision terminada ")		
			

if __name__ == "__main__":
    arp_scan(ips, sys.argv[1])
    cn.close()
    


