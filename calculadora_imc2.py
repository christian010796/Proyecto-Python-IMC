# Calculadora de Índice de Masa Corporal (IMC)
# Fundamentos de Python - Semana 3
# Reto: Formateo y Estética de Datos

print("=" * 45)
print("       CALCULADORA DE IMC")
print("=" * 45)

# Solicitar los datos personales
nombres = input("Ingrese sus nombres: ").strip().title()
apellidos = input("Ingrese sus apellidos: ").strip().title()

# Solicitar peso y estatura
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

# Calcular el Índice de Masa Corporal
imc = peso / (estatura ** 2)

# Mostrar el reporte final
print("\n" + "=" * 45)
print("          REPORTE DE RESULTADOS")
print("=" * 45)

print(f"Nombre completo : {nombres} {apellidos}")
print(f"Peso            : {peso:.2f} kg")
print(f"Estatura        : {estatura:.2f} m")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

print("=" * 45)
print("     Cálculo realizado correctamente.")
print("=" * 45)
