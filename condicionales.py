#-*- coding: utf-8 -*-

print("Cual Es Tu Calificación: ")

calificacion = int(input())

if(calificacion < 6):
	print("Reprobado")
elif(calificacion > 10):
	print("calificacion invalida")
else:
	print("Aprobado")
	