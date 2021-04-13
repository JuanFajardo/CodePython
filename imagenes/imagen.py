#!/bin/python3
#Manipulacion de imagenes

datos = {
'5521486':'01/08/2006',
'3666846':'05/12/2005'
}

cis  = [
'5521486',
'3666846'
]

from PIL import Image, ImageFont, ImageDraw

count = 1
for i in cis:
	date_begin = "Fecha Ingreso            " + str(datos[i])

	background = 'fondo.png'
	my_background = Image.open(background)

	img_1 = r'img-'+str(count).zfill(3)+'.jpg'
	img_2 = r'img'+str(count).zfill(3)+'.png'

	img_load = Image.open(img_1)
	#Izquierda Arriba Derecha Abajo (Derecha Abajo, deben ser mayores)
	img_crop = img_load.crop((1,1,1275,780))

	img_editable = ImageDraw.Draw(img_crop)
	txt_font = ImageFont.truetype('ARIALBD1.TTF', 12)

	img_editable.text((875,318), date_begin, (0, 0, 0), font=txt_font)
	img_editable.text((550,880), date_begin, (0, 0, 0), font=txt_font)

	my_background.paste(img_crop, (0,0))
	my_background.paste(img_crop, (0,800))

	# Mostrar
	my_background.show()
	input("")
	# Guardar
	#my_background.save(img_2)

	count = count + 1
