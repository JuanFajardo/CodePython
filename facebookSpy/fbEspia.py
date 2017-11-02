import mechanize
import ast
import json
import re
import urllib
import time
import traceback
import sys
from BeautifulSoup import BeautifulSoup

#!/bin/python

__author__ = 'Bett0'

"""
Facebook Espia v2.0 By Juan Fajardo

apt-get install python-mechanize
apt-get install python-beautifulsoup

./python fbEspia.py

Debian Jessie - Python 2.7.X
"""

class FbEspia:
    def __init__(self, HOST, USER, PASW, DB, FILECOOKIE):
        self.host = HOST
        self.user = USER
        self.pasw = PASW
        self.db = DB
        self.filecookie = FILECOOKIE

    def pagina(self, url):
        self.asignarCookie(self.filecookie)
        html = self.br.open(url).read()
        return html

    # Datos por su identificador ==> nameID()
    def nombreID(self, cadena):
        nameFull = re.findall(r'<title id="pageTitle">(.*?)</title>', cadena)
        return str(nameFull[0])

    def profileID(self, cadena):
        id = re.findall(r'data-profileid="(.*?)" type="button"', cadena)[0]
        return id

    def datosID(self, cadena):
        datas = re.findall(r'<div class="_50f3">(.*?)</div>', cadena)
        datos = []
        for data in datas:
            datos.append(data)
        return datos


    #Datos de Busqueda de Celular  ==> nameBC()
    def personalesBC(self, cadena):
        datas = re.findall(r'<div class="_52eh">(.*?)</div></div>', cadena)
        completo = ""
        datos = []
        for link in datas:
            completo = re.findall(r'([A-Z].*?)<',link)[0] + re.findall(r'>(.*?)<',link)[0]
            datos.append(completo)
        for link in datas:
            completo = re.findall(r'([A-Z].*?)<',link)[0] + re.findall(r'>(.*?)<',link)[0]
            datos.append(link)
        return datos

    def nombreBC(self, cadena):
        nameFull = re.findall(r'<div class="_5d-5">(.*?)</div>', cadena)
        return str(nameFull[0])

    def nombreLinkBC(self, cadena):
        nameLink = re.findall(r'<div class="_gll"><a href="(.*?)"><div class="_6a _6b _5d-4">', cadena) #Cadena html[25]
        return str(nameLink[0])

    def celularBC(self, cadena):
        numberPhone = re.findall(r'&quot;591(\d{1,9})&quot;', cadena)
        return str(numberPhone[0])

    def fotoBC(self, cadena, path):
        photo = re.findall(r'img class="img" src="(.*?)" width="100" height="100" alt=""', cadena)[0]
        photo = str(photo).replace("&amp;", "&", 2)
        photographi = urllib.urlopen(photo)
        path = path+"/"+self.celularBC(cadena)+"_"+self.nombreBC(cadena)+".jpg" #Link #Nombre
        document = open(path,'w')
        document.write(photographi.read())
        document.close()
        return self.celularBC(cadena)+"_"+self.nombreBC(cadena)+".jpg"


    #Inicio de Graph
    # Amigos Graph
    def amigosGraph(self, id):
        url = "https://www.facebook.com/search/" + id + "/friends"
        html = self.pagina(url)
        datas = re.findall(r'<div class="clearfix _zw">(.*?)</div></div></div></div></div></div>', str(html))
        for link in datas:
            print link
            print ""


    def asignarCookie(self, archivoCookie):
        archivo = open(archivoCookie, 'r')
        datas = dict()
        datas = json.loads(archivo.read())

        cookie01 = mechanize.Cookie(0, str(datas[0]['name']), str(datas[0]['value']), None, False, str(datas[0]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie02 = mechanize.Cookie(0, str(datas[1]['name']), str(datas[1]['value']), None, False, str(datas[1]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie03 = mechanize.Cookie(0, str(datas[2]['name']), str(datas[2]['value']), None, False, str(datas[2]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie04 = mechanize.Cookie(0, str(datas[3]['name']), str(datas[3]['value']), None, False, str(datas[3]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie05 = mechanize.Cookie(0, str(datas[4]['name']), str(datas[4]['value']), None, False, str(datas[4]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie06 = mechanize.Cookie(0, str(datas[5]['name']), str(datas[5]['value']), None, False, str(datas[5]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie07 = mechanize.Cookie(0, str(datas[6]['name']), str(datas[6]['value']), None, False, str(datas[6]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie08 = mechanize.Cookie(0, str(datas[7]['name']), str(datas[7]['value']), None, False, str(datas[7]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie09 = mechanize.Cookie(0, str(datas[8]['name']), str(datas[8]['value']), None, False, str(datas[8]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie10 = mechanize.Cookie(0, str(datas[9]['name']), str(datas[9]['value']), None, False, str(datas[9]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie11 = mechanize.Cookie(0, str(datas[10]['name']), str(datas[10]['value']), None, False, str(datas[10]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)
        cookie12 = mechanize.Cookie(0, str(datas[11]['name']), str(datas[11]['value']), None, False, str(datas[11]['domain']), False, False, '/', True, False, None, True, None, None, {}, False)

        self.cookie = mechanize.CookieJar()
        self.cookie.set_cookie(cookie01)
        self.cookie.set_cookie(cookie02)
        self.cookie.set_cookie(cookie03)
        self.cookie.set_cookie(cookie04)
        self.cookie.set_cookie(cookie05)
        self.cookie.set_cookie(cookie06)
        self.cookie.set_cookie(cookie07)
        self.cookie.set_cookie(cookie08)
        self.cookie.set_cookie(cookie09)
        self.cookie.set_cookie(cookie10)
        self.cookie.set_cookie(cookie11)
        self.cookie.set_cookie(cookie12)

        self.br = mechanize.Browser()
        self.br.set_cookiejar(self.cookie)
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)

        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        self.br.addheaders= [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def server(self):
        print("{0}".format(self.host))


if __name__ == '__main__':
    #Direccion donde se guaradara la fotgrafia
    linkFoto = "/home/bett0/Proyectos/PycharmProjects/Python/FacebookEspia/fotos"

    #Cookies de Session sacado con cookie Master(Chrome)
    cookieCel0 = "/home/bett0/Proyectos/PycharmProjects/Python/FacebookEspia/CelBett0.txt"

    #Datos de inicitio
    bett0 = FbEspia('localhost', 'root', '123', 'facebookEspia', cookieCel0)


    #10 Por dia con retraso de 3 minutos #Entel 718,  723,  724,  738,  6792, 6794, 6793 #Tigo  7572, 7573, 7616, 7617, 7747, 7786, 7862, 7863
    #Viva  6045, 6046, 6047, 7043, 7042, 7044, 7943, 7944

    numerosmalos = []
    for cel in range(72400110, 72400150):
    # ID NombreCel celular Link Foto NombreID datosCel DastoIdl
        html0 = bett0.pagina('https://www.facebook.com/search.php?q=591'+str(cel))
        try:
            profileID = html0.find("No se encontraron resultados.")
            if profileID<0:
                nombreCel  = bett0.nombreBC(html0)
                link    = bett0.nombreLinkBC(html0)
                celular = bett0.celularBC(html0)
                foto    = bett0.fotoBC(html0,linkFoto)
                datosCel = bett0.personalesBC(html0)


                html1 = bett0.pagina(link)
                nombreID =  bett0.nombreID(html1)
                ID =  bett0.profileID(html1)
                datosIdl = bett0.datosID(html1)
                respuesta = ("insert into __TABLA__ values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '|', ".format(str(ID), str(celular), str(nombreCel), str(link), str(foto), str(nombreID)))
                for datos in datosCel:
                    respuesta = respuesta + "'" + datos +"', "
                for datos in datosIdl:
                    respuesta = respuesta + "'" + datos +"', "
                respuesta = respuesta + " ''); "

                print(respuesta)
                time.sleep(60)
            else:
                numerosmalos.append(cel)
                time.sleep(30)
        except Exception, err:
            print("-- {0} \n -- {1}\n\n".format(str(err), traceback.format_exc()))
            print("-----{}".format(str(cel)))

    sys.stdout.write('--')
    for numero in numerosmalos:
        sys.stdout.write(str(numero)+' ')

