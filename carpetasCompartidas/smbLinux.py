import nmap
import os
import datetime
import mysql.connector
from smbprotocol.connection import Connection
from smbprotocol.exceptions import SMBException

def is_writable(path):
    try:
        file = "\\bett0.txt"
        path_full = path + file
        with open(path_full, "w") as f:
            pass
        os.remove(path_full)
        return "SI"
    except:
        return "NO"

def file_sharing(ip):
    try:
	    connection = mysql.connector.connect( host="192.168.1.69", database="carpetas", user="bett0", password="bett0")
	    
        conn = Connection(ip, username="bett0", password="bett0")
        conn.connect()
        
		cursor = connection.cursor()
        share = conn.tree_connect("/")
        for entry in share.list_directory(''):
            if entry.file_attributes.is_directory:
                folder_name = entry.file_name.decode("utf-8")
                path = rf'\\{ip}\{folder_name}'
                binder = []  # No se manejan los binders con smbprotocol
                files = []  # No se manejan los archivos con smbprotocol
                timer = str(datetime.datetime.now())
                write = is_writable(path)
                sql = "INSERT INTO compartidos(ip, link, carpetas, archivos, fecha, escritura) VALUES(%s, %s, %s, %s, %s, %s)"
		        cursor.execute(sql, (ip, str(path), str(binder), str(file), timer, write))
        		connection.commit()
        cursor.close()

    except SMBException as e:
    	print(f"\t\t \t -- {ip} {e}")
    finally:
        conn.disconnect()
	connection.close()
	
lista = [
    '192.168.1.0/24',
    #'192.168.2.0/24'
]

miIps = ["192.168.1.8"]
def main():
    nm = nmap.PortScanner()
    for lst in lista:
        print("Escaneando VLAN: " + lst + " en: " + str(datetime.datetime.now()))
        lan = nm.scan(hosts=str(lst), arguments='-p 445 --open')
        ips = lan['scan']
        for ip in ips:
            print('\t [+] ... ' + ip)
            if ip not in miIps:  # Tu IP para que no saque tu info XD
                file_sharing(ip)

if __name__ == "__main__":
    main()
