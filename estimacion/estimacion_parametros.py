# coding=utf-8
from scipy import stats
import math

def calcular_z(NC=95):
     z_alfa2 = (1 + NC*1.0/100)/2
     return round(stats.norm.ppf(z_alfa2),2)

def calcular_tamanio_muestra(Z, P, Q, e):
    """
    @z factor probabilistico
    @PQ varianza de la proporcion
    @e error max permitido
    """
    # (Z² * P * Q) / e²
    n0= (Z*Z*P*Q)/(e*e)
    return int(math.ceil(n0))

def calcular_tamanio_muestra_ajustado(Z, P, Q, e):
    """
    @z factor probabilistico
    @PQ varianza de la proporcion
    @e error max permitido
    """
    n0= calular_tamanio_muestra(Z, P, Q, e)
    #n ajustado
    n1= n0/(1 + (n0 - 1)/N)
    return int(math.ceil(n1))
