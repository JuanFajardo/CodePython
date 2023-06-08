181.114.2.100

181.114.28.34
554/tcp open  rtsp
nmap -p 554 --open 181.114.28.0/24 -oN dahua_181.114.28.0


#!/bin/python3
import itertools
cadena = "SoyBett0"

for n in range(0, len(cadena)+1):
    texto = cadena[0:n]
    nuevo = itertools.permutations(texto)
    for permutacion in nuevo:
        print(''.join(permutacion))
    
    combinaciones = itertools.combinations(cadena, n)
    for combinacion in combinaciones:
        print(''.join(combinacion))

