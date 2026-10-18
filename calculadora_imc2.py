# Proyecto: Calculadora de IMC
# Actividad: Fundamentos de Python - Semana 2

# 1. Solicitar los datos al usuario
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad en años: "))
peso = float(input("Ingresa tu peso en kilogramos: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# 2. Calcular el Índice de Masa Corporal
imc = peso / (estatura ** 2)

# 3. Mostrar los resultados
print("\n--- RESULTADOS DEL CÁLCULO ---")
print("Nombre:", nombre)
print("Edad:", edad, "años")
print("Peso:", peso, "kg")
print("Estatura:", estatura, "m")
print("Índice de Masa Corporal (IMC):", round(imc, 2), "kg/m²")