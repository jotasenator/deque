
#simularemos una cola de entrada a un restaurante
from collections import deque
import time

class queues:

	def __init__(self):

		self.c = deque()

	def pop(self):

		return self.c.popleft()

	def pull(self,data):

		return self.c.append(data)

	def mostrar(self):

		return self.c

miembros_cola = queues()

reservacion = int(input('Cuantas personas tienen reservadas para hoy por la noche?: '))
capacidad = int(input('Cual es la capacidad del restaurant?: '))

contador1 = 0

while reservacion > contador1:

	persona = input('Teclee el nombre de la siguiente persona que entra al restaurant: ')

	if persona.isalpha():

	
		if len(miembros_cola.mostrar()) == capacidad:

			miembros_cola.pop()

		miembros_cola.pull(persona)

		print(miembros_cola.mostrar())

		contador1 +=1

	else:

		continue

print('Salgan en orden por favor...')


contador2 = 0

while capacidad>contador2:

	time.sleep(1)

	miembros_cola.pop()

	if len(miembros_cola.mostrar()) == 0:

		print('Ahora que no hay nadie vamos a limpiar el local')
		break

	print(miembros_cola.mostrar())
	contador2 += 1
	

	














