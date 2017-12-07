# coding=utf-8
from scipy import stats
import math

def calcular_z(NC=95):
     z_alfa2 = (1 + NC*1.0/100)/2
     return round(stats.norm.ppf(z_alfa2),2)

def calcular_tamanio_muestra(Z, P, e):
    """
    #(Z² * P * Q) / e²

    argumentos:
    @Z -- factor probabilistico
    @P -- valor esperado
    @e -- error max permitido
    """
    Q= 1 - P
    n0= (Z*Z*P*Q)/(e*e)
    return int(math.ceil(n0))

def calcular_tamanio_muestra_ajustado(Z, P, N, e):
    """
    argumentos:
    @Z -- factor probabilistico
    @P -- valor esperado
    @N -- tamaño de población
    @e -- error max permitido
    """
    Q= 1 - P
    n0= calular_tamanio_muestra(Z, P, e)
    #n ajustado
    n1= n0/(1 + (n0 - 1)/N)
    return int(math.ceil(n1))
