from src.calculadora import calcular_promedio, calcular_desviacion_estandar
from tests.excepcion import NoSePuedeCalcular


def main():
    elementos = []

    # Ingresar números hasta que el usuario decida parar
    while True:
        entrada = input("Ingresa un número (o 'fin' para terminar): ")

        if entrada.lower() == 'fin':
            break

        try:
            numero = float(entrada)  # Convertir la entrada a float
            elementos.append(numero)  # Agregar el número a la lista
        except ValueError:
            print("TypeError" 
                  "\n""Por favor, ingresa un número válido.")

    try:
        promedio =  calcular_promedio(elementos)
        print(f"Promedio: {promedio}")

        desviacion_estandar = calcular_desviacion_estandar(elementos)
        print(f"Desviación Estándar: {desviacion_estandar}")
    except NoSePuedeCalcular as e:
        print(e)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
