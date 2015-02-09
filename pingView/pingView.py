#!/usr/bin/python
__author__ = 'bett0'
#
#python pingView.py 192.168.1.
#

from subprocess import Popen, PIPE
from optparse import OptionParser
import sys

ip = str(sys.argv[1])

def ping(ip):
    try:
        f = open('lista.tx', 'a')
        for i in range(1,255):
            ipp = ip+'.'+str(i)
            subprocess = Popen(['ping', '-c 1 ', ipp], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            (stdout, stderr) = subprocess.communicate(input=None)
            if 'bytes from ' in stdout:
                ip = stdout.split()[1]
                print(ip)
                f.write(ip)
        f.close()
    except Exception, err:
        print('Error {0}'.format(err))

def main():
    pr = OptionParser(" python pingView.py -r [IP / 192.168.1]")
    pr.add_option("-r", "--rango" ,dest='ip', type='string', help='El rango de escaneo es de /24')
    (opts, args) = pr.parse_args()
    if opts.ip == None:
        print pr.usage
        exit(0)
    else:
        ping(opts.ip)

if __name__ == '__main__':
    main()


