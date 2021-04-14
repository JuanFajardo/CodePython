import phonenumbers

from phonenumbers import carrier
from phonenumbers import geocoder

x = input(" Numero de Celular : +591*** ")

number = phonenumbers.parse(x)

print(geocoder.description_for_number(number, 'en'))
print(carrier.name_for_number(number, 'en'))
