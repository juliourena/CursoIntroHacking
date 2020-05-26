# Programacion 101

# Variables 
numero = 1
texto = "informacion"
verdadero = True 
falso = False

# Condiciones
edad = sys.argv[1]
if edad > 17:
	print("Eres mayor de Edad.")
else:
	print("Eres menor de Edad.")

# Loops (Codigo que se repite hasta que la condicion se cumple)
frutas = ["Manzana","Pera","Uva"]
for fruta in frutas:
	print("Esta fruta es una " + fruta)

# Todo junto
frutas = ["Manzana","Pera","Uva"]
for fruta in frutas:
	if fruta == "Uva":
		print("La" + fruta + " me gusta")
	else:
		print("La" + fruta + " no me gusta")

# For # 2
numeros = list(range(1,11))
for num in numeros:
	print(num)

# Metodos (Repositorios de codigo que cumplen una funcion)
def MayorEdad(edad):
	if edad > 17:
		print("Eres mayor de Edad.")
	else:
		print("Eres menor de Edad.")

# Modulos 
import sys

def MayorEdad(edad):
	if edad > 17:
		print("Eres mayor de Edad.")
	else:
		print("Eres menor de Edad.")

# Toma el argumento pasado al programa.
# Ejemplo: python3 programa.py 19
MayorEdad(sys.argv[1])
