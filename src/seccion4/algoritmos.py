# Algortimo 1
facil = int (input("Ingrese el puntaje en el nivel facil: "))
normal = int (input("Ingrese el puntaje en el nivel normal: "))
dificil = int (input("Ingrese el puntaje en el nivel dificil: "))
puntaje_total = facil + normal + dificil
print ("tu puntaje total es:", puntaje_total)

# Algoritmo 2
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

total_segundos = horas * 3600 + minutos * 60 + segundos

print("Tiempo total en segundos:", total_segundos)

# Algoritmo 3
a1 = int(input("Daño ataque 1: "))
a2 = int(input("Daño ataque 2: "))
a3 = int(input("Daño ataque 3: "))

total = a1 + a2 + a3

print("Daño total:", total)

# Algoritmo 4 
e1 = int(input("Exp misión 1: "))
e2 = int(input("Exp misión 2: "))
e3 = int(input("Exp misión 3: "))

total = e1 + e2 + e3

print("Experiencia total:", total)

# Algoritmo 5
vida_max = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))

porcentaje = (vida_actual / vida_max) * 100

print("Vida restante:", porcentaje, "%")

# Algoritmo 6 
o1 = int(input("Oro misión 1: "))
o2 = int(input("Oro misión 2: "))
o3 = int(input("Oro misión 3: "))

total = o1 + o2 + o3

print("Oro total:", total)

# Algoritmo 7
distancia = float(input("Distancia: "))
tiempo = float(input("Tiempo: "))

velocidad = distancia / tiempo

print("Velocidad promedio:", velocidad)

# Algoritmo 8
m1 = float(input("Mejora 1: "))
m2 = float(input("Mejora 2: "))
m3 = float(input("Mejora 3: "))

total = m1 + m2 + m3

print("Costo total:", total)

# Algoritmo 9
total_mision = float(input("Tiempo total misión: "))
transcurrido = float(input("Tiempo transcurrido: "))

restante = total_mision - transcurrido

print("Tiempo restante:", restante)

# Algoritmo 10
j1 = float(input("Nivel jugador 1: "))
j2 = float(input("Nivel jugador 2: "))
j3 = float(input("Nivel jugador 3: "))

promedio = (j1 + j2 + j3) / 3

print("Nivel promedio:", promedio)

# Algoritmo 11
daño_base = float(input("Daño base: "))
multiplicador = float(input("Multiplicador crítico: "))

daño_critico = daño_base * multiplicador

print("Daño crítico:", daño_critico)

# Algoritmo 12
minutos_totales = int(input("Minutos jugados: "))

horas = minutos_totales // 60
minutos = minutos_totales % 60

print("Horas:", horas)
print("Minutos:", minutos)

# Algoritmo 13
total = int(input("Total de misiones: "))
completadas = int(input("Misiones completadas: "))

porcentaje = (completadas / total) * 100

print("Porcentaje completado:", porcentaje, "%")

# Algoritmo 14
o1 = float(input("Objeto 1: "))
o2 = float(input("Objeto 2: "))
o3 = float(input("Objeto 3: "))

total = o1 + o2 + o3

print("Costo total:", total)

# Algoritmo 15
p1 = float(input("Partida 1: "))
p2 = float(input("Partida 2: "))
p3 = float(input("Partida 3: "))

promedio = (p1 + p2 + p3) / 3

print("Tiempo promedio:", promedio)