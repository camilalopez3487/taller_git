import numpy as np

dimension = 2
tamaño = 8
decrement = 0.9
matriz = np.asarray([np.random.random(dimension) for _ in range(tamaño)])
print(matriz)
minimo = np.amin(matriz[:,0])

# Dividimos el valor inicial de "decrement" entre el número de iteraciones
decrement_step = decrement / 100

prev_stddev = 0
for i in range(100):
  # Restamos el valor del decremento en cada iteración
  decrement -= decrement_step

  # Aquí iría el código para hacer que los valores converjan hacia el mínimo
  # utilizando el valor de "decrement" actual

  # Calculamos la desviación estándar de los valores de la matriz
  stddev = np.std(matriz)

  # Si la desviación estándar ha disminuido respecto a la iteración anterior,
  # entonces aumentamos la velocidad a la que se actualizan los valores de la
  # matriz reduciendo el valor de "decrement"
  if stddev < prev_stddev:
    decrement -= decrement_step
  # Si la desviación estándar no ha disminuido, entonces reducimos la velocidad
  # a la que se actualizan los valores de la matriz aumentando el valor de
  # "decrement"
  else:
    decrement += decrement_step

  # Almacenamos la desviación estándar actual para compararla en la siguiente
  # iteración del bucle
  prev_stddev = stddev
