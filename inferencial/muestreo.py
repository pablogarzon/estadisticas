# coding=utf-8
import math


def promedio_ponderado(arrN, arrx):
    """
    @arrN: array que representa a N de los estratos
    @arrx: array que representa a las medias de los estratos
    """
    #∑(Ni*x)/∑Ni

    Nx=0
    sumN=0

    for i in list(range(len(arrN))):
        sumN+=arrN[i]
        Nx+=arrN[i]*arrx[i]

    return Nx/sumN

def afijacion_igual(n, r):
    """
    @n: tamaño de muestra
    @r: cantidad de estratos
    """
    return n/r

def afijacion_prop(Ni, N, n):
    # (Ni/N)*n
    return int((Ni*1.0/N)*n)

def afijacion_optima(arrN, arrO, n, estrato):
    """
    @arrN: array que representa a N de los estratos
    @arrO: array que representa a la desviacion estandard de los estratos
    @n: n
    @estrato: nro de estrato
    """
    #((Ni*Oi)/∑(Ni*Oi))*n

    sum_NiOi = 0

    for i in list(range(len(arrN))):
        sum_NiOi += arrN[i]*arrO[i]

    return int(((arrN[estrato]* arrO[estrato])*1.0/sum_NiOi)*n)
