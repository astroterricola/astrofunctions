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
      desviacion:

