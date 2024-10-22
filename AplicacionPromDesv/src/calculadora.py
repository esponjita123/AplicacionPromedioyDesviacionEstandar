from tests.excepcion import NoSePuedeCalcular


def calcular_promedio(elementos):
    """Calcula el promedio de una lista de números."""
    if not elementos:
        raise NoSePuedeCalcular("NoSePuedeCalcular")
    if len(elementos) == 1:
        return elementos[0]
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")

    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    """Calcula la desviación estándar de una lista de números."""
    if not elementos:
        raise NoSePuedeCalcular("NoSePuedeCalcular")
    if len(elementos) == 1:
        return 0.0
    if any(not isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")

    promedio = calcular_promedio(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)
    return varianza ** 0.5
