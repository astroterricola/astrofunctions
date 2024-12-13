# -*- coding: utf-8 -*-
def lc_promedio(lista):
    """
    Entrega el promedio de los datos de una lista de datos.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        prom: Promedio en float.
    """
    x = sum(lista)
    prom = x / len(lista)
    return prom

def lc_mediana(lista):
    """
    Función que regresa el valor correspondiente a la mediana de un grupo numérico.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        media: Valor numérico correspondiente a la mediana.
    """
    lista = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        med1 = lista[(n // 2) - 1]
        med2 = lista[n // 2]
        media = lc_promedio([med1, med2])
    else:
        media = lista[n // 2]
    return media

def lc_moda(lista):
    """
    Función que regresa una lista con los valores que tienen mayor frecuencia.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        moda: Lista con todos los valores con mayor frecuencia.
    """
    from collections import Counter
    conteo = Counter(lista)
    max_frecuencia = max(conteo.values())
    moda = [key for key, val in conteo.items() if val == max_frecuencia]
    return moda

def lc_rango(lista):
    """
    Función que regresa la diferencia entre el valor máximo y el mínimo.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        rango: Diferencia entre el valor máximo y el mínimo.
    """
    return max(lista) - min(lista)

def lc_varianza(lista):
    """
    Calcula la varianza de una lista de datos.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        varianza: Varianza numérica.
    """
    x = lc_promedio(lista)
    varianza = sum((elem - x) ** 2 for elem in lista) / len(lista)
    return varianza

def lc_desviacion_estandar(lista):
    """
    Calcula la desviación estándar de una lista de datos.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        desviacion: La raíz cuadrada de la varianza.
    """
    var = lc_varianza(lista)
    desviacion = var ** 0.5
    return desviacion

def lc_rango_intercuartilico(lista):
    """
    Calcula el rango intercuartílico de una lista de datos.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        IQR: Rango intercuartílico.
    """
    lista = sorted(lista)
    n = len(lista)
    if n % 2 == 0:
        Q1_index1 = n // 4
        Q1_index2 = Q1_index1 - 1
        Q3_index1 = (n * 3) // 4
        Q3_index2 = Q3_index1 - 1
        Q1 = (lista[Q1_index1] + lista[Q1_index2]) / 2
        Q3 = (lista[Q3_index1] + lista[Q3_index2]) / 2
    else:
        Q1_index = n // 4
        Q3_index = (n * 3) // 4
        Q1 = lista[Q1_index]
        Q3 = lista[Q3_index]
    IQR = Q3 - Q1
    return IQR

def lc_MAD(lista):
    """
    Calcula la desviación mediana absoluta de una lista de datos.
    ---------------------------------------------
    Input:
        lista: Lista con datos numéricos.
    Output:
        mad: Desviación mediana absoluta.
    """
    med = lc_mediana(lista)
    desv_abs = [abs(elem - med) for elem in lista]
    mad = lc_mediana(desv_abs)
    return mad

def lc_covarianza(x, y):
    """
    Calcula la covarianza para dos listas con datos numéricos.
    ---------------------------------------------
    Input:
        x: Lista x con datos numéricos.
        y: Lista y con datos numéricos.
    Output:
        cov: Valor numérico correspondiente a la covarianza de x e y.
    """
    x_prom = lc_promedio(x)
    y_prom = lc_promedio(y)
    N = len(x)
    cov = sum((xi - x_prom) * (yi - y_prom) for xi, yi in zip(x, y)) / N
    return cov

def lc_coeficiente_correlacion(x, y):
    """
    Calcula el coeficiente de correlación entre dos listas con datos numéricos.
    ---------------------------------------------
    Input:
        x: Lista x con datos numéricos.
        y: Lista y con datos numéricos.
    Output:
        r: Valor numérico correspondiente al coeficiente de correlación entre x e y.
    """
    covar = lc_covarianza(x, y)
    varx = lc_varianza(x)
    vary = lc_varianza(y)
    r = covar / ((varx ** 0.5) * (vary ** 0.5))
    return r
