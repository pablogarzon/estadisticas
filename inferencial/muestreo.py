# coding=utf-8
import math


def promedio_ponderado(arr_N, arr_x):
    """
    @arr_N: array que representa a N de los estratos
    @arrx: array que representa a las medias de los estratos
    """
    #∑(Nᵢ*x)/∑Nᵢ

    Nx=0
    sum_N=0

    for i in list(range(len(arr_N))):
        sum_N += arr_N[i]
        Nx += arr_N[i] * arr_x[i]

    return Nx/sum_N

def afijacion_igual(n, r):
    """
    @n: tamaño de muestra
    @r: cantidad de estratos
    """
    return n/r

def afijacion_prop(Ni, N, n):
    # (Nᵢ/N)*n
    return int((Ni*1.0/N)*n)

def afijacion_optima(arr_N, arr_O, n, estrato):
    """
    @arr_N: array que representa a N de los estratos
    @arr_O: array que representa a la desviacion estandard de los estratos
    @n: n
    @estrato: nro de estrato
    """
    #((Nᵢ*Oᵢ)/∑(Nᵢ*Oᵢ))*n

    sum_NiOi = 0

    for i in list(range(len(arr_N))):
        sum_NiOi += arr_N[i] * arr_O[i]

    return int(((arr_N[estrato]*arr_O[estrato])*1.0/sum_NiOi)*n)
