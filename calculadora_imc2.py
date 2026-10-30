# Calculadora de IMC
# Fundamentos de Python - Entrega final

def solicitar_texto(mensaje):
    """Solicita un texto y evita campos vacíos."""
    while True:
        dato = input(mensaje).strip()

        if dato:
            return dato.title()

        print("Error: este campo no puede estar vacío.")


def solicitar_numero(mensaje, entero=False):
    """Solicita un número válido y positivo."""
    while True:
        dato = input(mensaje).strip()

        if not dato:
            print("Error: este campo no puede estar vacío.")
            continue

        try:
            if entero:
                numero = int(dato)
            else:
                numero = float(dato)

            if numero <= 0:
                print("Error: ingrese un número mayor que cero.")
                continue

            return numero

        except ValueError:
            print("Error: debe ingresar un valor numérico válido.")


def main():
    print("=" * 40)
    print("       CALCULADORA DE IMC")
    print("=" * 40)

    nombres = solicitar_texto("Ingrese sus nombres: ")
    apellidos = solicitar_texto("Ingrese sus apellidos: ")
    edad = solicitar_numero("Ingrese su edad: ", entero=True)
    peso = solicitar_numero("Ingrese su peso en kg: ")
    estatura = solicitar_numero("Ingrese su estatura en metros: ")

    imc = peso / (estatura ** 2)

    print("\n" + "=" * 40)
    print("       REPORTE DE RESULTADOS")
    print("=" * 40)

    print(f"Nombre completo: {nombres} {apellidos}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso:.2f} kg")
    print(f"Estatura: {estatura:.2f} m")
    print(f"Índice de Masa Corporal (IMC): {imc:.2f}")

    print("=" * 40)
    print("Cálculo realizado correctamente.")


if __name__ == "__main__":
    main()
