#!/usr/bin/python
__author__ = 'bett0'
#
#Escrito para http://www.CommunitySec.com/
#
#python ipScanPort.py -l lista.txt
#

import urllib2
import socket
import optparse
import traceback

def http(ip):
    try:
        c = urllib2.urlopen("http://"+str(ip))
        print('[+] HTTP - {0}'.format(c.info()))
        c.close()
    except Exception, e:
        print('[-] HTTP  - {0}'.format(ip))

def ssh(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 22))
        print('[+] SSH - {0} {1}'.format(ip, str(s.recv(33333)) ))
        s.close()
    except Exception, e:
        print('[-] SSH  - {0} '.format(ip))

def ftp(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 21))
        print('[+] FTP - {0} {1}'.format(ip, str(s.recv(33333)) ))
        s.close()
    except Exception, e:
        print('[-] FTP - {0}'.format(ip))

def ms(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 445))
        print('[+] MS - {0} {1}'.format(ip, str(s.recv(33333)) ))
        s.close()
    except Exception, err:
        print('[-] MS - {0} '.format(ip))

def telnet(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 23))
        s.close()
        print('[+] Telnet - {0} {1}'.format(ip, str(s.recv(33333)) ))
    except Exception, err:
        print('[-] Telnet - {0} '.format(ip))

def dns(ip):
    try:
        socket.setdefaulttimeout(5)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 23))
        print('[+] DNS - {0} {1}'.format(ip, str(s.recv(33333)) ))
        s.close()
    except Exception, err:
        print('[-] DNS - {0} '.format(ip))

def main():
    try:
        pr = optparse.OptionParser(" python ipScanPort.py -l [IP's.txt]")
        pr.add_option('-l', '--lista', dest='list', type='string', help="Nombre del archivo donde estan las IP's")
        (opt, args) = pr.parse_args()
        if opt.list == None:
            print pr.parse_args()
            exit(0)
        else:
            with open(opt.list, 'r') as ips:
                for ip in ips.readlines():
                    print " IP : " + str(ip)
                    http(ip)
                    ssh(ip)
                    ftp(ip)
                    ms(ip)
                    telnet(ip)
                    dns(ip)
                    print('\n')
    except Exception, err:
        print('Error Main : {0}'.format(err))
        print traceback.format_exc()

if __name__ == '__main__':
    main()