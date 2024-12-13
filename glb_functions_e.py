# Función para calcular el promedio
def lc_e_calcular_promedio(valores):
    """
    Calcula el promedio de una lista de valores.

    :param valores: Lista de valores numéricos.
    :return: Promedio de los valores.
    """
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

# Función para calcular la mediana
def lc_e_calcular_mediana(valores):
    """
    Calcula la mediana de una lista de valores.

    :param valores: Lista de valores numéricos.
    :return: Mediana de los valores.
    """
    valores_ordenados = sorted(valores)
    n = len(valores_ordenados)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (valores_ordenados[n // 2 - 1] + valores_ordenados[n // 2]) / 2
    else:
        return valores_ordenados[n // 2]

# Función para calcular la desviación estándar
def lc_e_calcular_desviacion_estandar(valores):
    """
    Calcula la desviación estándar de una lista de valores.

    :param valores: Lista de valores numéricos.
    :return: Desviación estándar de los valores.
    """
    if len(valores) == 0:
        return 0
    promedio = lc_e_calcular_promedio(valores)
    varianza = sum((x - promedio) ** 2 for x in valores) / len(valores)
    return varianza ** 0.5

# Función para calcular cuartiles
def lc_e_calcular_cuartil(valores, percentil):
    """
    Calcula un cuartil específico de una lista de valores.

    :param valores: Lista de valores numéricos.
    :param percentil: Percentil a calcular (entre 0 y 1).
    :return: Valor del cuartil correspondiente.
    """
    if len(valores) == 0:
        return 0
    valores_ordenados = sorted(valores)
    indice = int(len(valores_ordenados) * percentil)
    return valores_ordenados[indice]

# Función para calcular la covarianza
def lc_e_calcular_covarianza(x, y):
    """
    Calcula la covarianza entre dos listas de valores.

    :param x: Lista de valores de la primera variable.
    :param y: Lista de valores de la segunda variable.
    :return: Covarianza entre las dos variables.
    """
    if len(x) != len(y) or len(x) == 0:
        return 0
    promedio_x = lc_e_calcular_promedio(x)
    promedio_y = lc_e_calcular_promedio(y)
    return sum((x[i] - promedio_x) * (y[i] - promedio_y) for i in range(len(x))) / len(x)
