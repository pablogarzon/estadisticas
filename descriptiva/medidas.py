# coding=utf-8
import math

def media(arr):
    """
    descripción:
    promedio de la distribución
    #̅x = (∑xᵢ)/n

    retorna:
    número con 2 decimales
    """
    sum_xi = 0
    for xi in arr:
        sum_xi += xi

    return round(sum_xi/len(arr),2)

def mediana(arr):
    """
    descripción:
    el primer valor de la variable que deja por debajo de
    sí al 50% de los valores de la serie
    #(n + 1)/2

    retorna:
    número con 2 decimales
    """
    me=0
    arr.sort()
    x = (len(arr) + 1)/2

    if (len(arr) % 2 == 0):
        #si el largo del array se promedian los valores centrales
        me1 = int(x) - 1
        me2 = math.ceil(x) - 1
        me = (arr[me1] + arr[me2])/2
    else:
        me = arr[x]

    return round(me,2)

def moda(arr):
    """
    descripción:
    máximo relativo de la distribución de frecuencias

    retorna:
    (temporalmente) número con 2 decimales
    """
    max_ = 1
    mode = 0
    dict_ = dict()

    #ordenar el array
    arr.sort()
    for i in list(range(len(arr))):
        #si el valor examinado existe en el diccionario
        if arr[i] in dict_:
            count = dict_[arr[i]]
            #se le suma 1 al contador de ese valor
            count = count + 1
            dict_[arr[i]] = count
            if count > max_:
                max_ = count
                mode = arr[i]
        else:
            #se agrega al diccionario
            dict_[arr[i]] = 1
    return mode

def varianza(arr):
    """
    descripción:
    calcula la media de las diferencias cuadráticas de n puntuaciones
    con respecto a su media aritmética
    #s² = (∑xᵢ²/n) - ̅x²

    retorna:
    número con 2 decimales
    """
    sum_xx = 0
    for xi in arr:
        sum_xx += xi * xi

    return round(sum_xx/len(arr) - (media(arr) * media(arr)),2)

def desv_standard(arr):
    """
    descripción:
    la raíz cuadrada de la varianza
    #√s

    retorna:
    número con 2 decimales
    """
    return round(math.sqrt(varianza(arr)),2)

def coeficiente_variacion(arr):
    """
    descripción:
    coeficiente de variación
    CV = s/̅x * 100

    retorna:
    número con 2 decimales
    - 0% al 19%  variabilidad baja
    - 20% al 59% variabilidad moderada
    - 60% al 89% variabilidad alta
    - 90% y superior variabilidad muy alta
    """
    dv = desv_standard(arr)
    me = media(arr)

    return round(dv/me * 100, 2)

def asimetria(arr):
    """
    descripción:
    coeficiente de asimetria
    determinar si una distribución de frecuencias es simétrica
    # sₖ = (∑(xᵢ - ̅x)³/n)/s³

    retorna:
    número con 2 decimales
    """
    sum_ = 0
    mean = media(arr)
    deviation = desv_standard(arr)

    for xi in arr:
        sum_ += xi - (mean * mean * mean)

    result = (sum_ / len(arr)) / (deviation * deviation * deviation)

    return round(result,2)

def curtosis(arr):
    """
    descripción:
    indica el grado de apuntalamiento de una distribución
    # sₖ = ((∑(xᵢ - ̅x)⁴ * ⨍ᵢ)/n)/s⁴

    retorna:
    g = 0 (g ± 0.5) -> distribución mesocúrtica (dist. normal)
    g > 0 -> distribución leptocúrtica (dist. estrecha)
    g < 0 -> distribución platicúrtica (dist. ancha)
    """
