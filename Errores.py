#-*- coding: utf-8 -*-

try:
	print(5/"dasda")
except Exception as err:
	print("El Programa tuvo un error " + str(err))
finally:
	print('Adios')