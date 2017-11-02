import urllib
import re
import sys
import time

cont = 0
for i in range (306, 3994):
    cont = cont + 1 
    link = "http://www.milanuncios.bo/usuarios/perfil.php/?id="+str(i)
    html = urllib.urlopen(link).read()
    html = str(html.rstrip('\r\n'))
    if len(html) < 70000 :
        nombre = re.findall(r'<title>(.*?)milnauncios.bo</title>', html)
        telefono = re.findall(r'<i class="material-icons dp48">stay_primary_portrait</i>(.*?)</span>', html, re.IGNORECASE)
        datos = re.findall(r'<p>(.*?)</p>', html, re.IGNORECASE)
        
        sys.stdout.write( "insert into [TABLA] values('', '" + str(i) + "', " )
        sys.stdout.write( " '" + str(nombre[0])[0:len(str(nombre[0]))-3].upper() + "', " )
        sys.stdout.write( " '" + str(telefono[0]).strip('                        ') + "', "  )
        sys.stdout.write( " '" )
        for d in datos:
            sys.stdout.write( d.replace("En milanuncios desde ", "") + "; "  )
        sys.stdout.write( "' );" )
        print ""
    if cont == 500:
        cont = 0
        time.sleep(180)
        
