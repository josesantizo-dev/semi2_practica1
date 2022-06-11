import os
from reader import Reader
import mysql.connector

from creacion import *
from querys import * 

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	# os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Crear modelos")
	print ("\t2 - Cargar datos")
	print ("\t3 - Hacer consultas")
	print ("\t9 - salir")
 

conexion = mysql.connector.connect(user='admin',password='0Vg*8tUKs1&D',host='paggodev.c9uo6erahpmy.us-east-2.rds.amazonaws.com',database='semi1',port='3306')

while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":

		cursor = conexion.cursor()

		print('BORRANDO TEMPORAL')
		cursor.execute(DROP_TABLES, ())

		print('CREANDO TEMPORAL')
		cursor.execute(TEMPORAL_CREATION, ())

		print('BORRANDO REPRODUCCION')
		cursor.execute(DROP_REPRODUCCION, ())

		print('BORRANDO ARTISTA')
		cursor.execute(DROP_ARTISTA, ())

		print('CREANDO ARTISTA')
		cursor.execute(CREAR_ARTISTA, ())

		print('BORRANDO GENERO')
		cursor.execute(DROP_GENERO, ())

		print('CREANDO GENERO')
		cursor.execute(CREAR_GENERO, ())

		print('BORRANDO CANCION')
		cursor.execute(DROP_CANCION, ())

		print('CREANDO CANCION')
		cursor.execute(CREAR_CANCION, ())

		print('CREANDO REPRODUCCION')
		cursor.execute(CREAR_REPRODUCCION, ())

		cursor.close()

		
	elif opcionMenu=="2":

		cursor = conexion.cursor()

		print('LLENANDO TEMPORAL')
		with Reader.openWithName("songs_normalize.csv") as file:
			for line in file:
        			
					print(line[0])
					cursor.execute(LLENADO_TEMPORAL, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14], line[15], line[16], line[17]))

		print('LLENANDO ARTISTA')
		cursor.execute(LLENAR_ARTISTA, ())

		print('LLENANDO GENERO')
		cursor.execute(LLENAR_GENERO, ())

		print('LLENANDO CANCION')
		cursor.execute(LLENAR_CANCION, ())

		print('LLENANDO REPRODUCCION')
		cursor.execute(LLENAR_REPRODUCCION, ())

		conexion.commit()
		cursor.close()

	elif opcionMenu=="3":
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="9":
		conexion.close()
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")