# coding=utf-8
from scipy import stats
import math


def calcular_z(NC=95):
    z_alfa2 = (1 + NC * 1.0 / 100) / 2
    return round(stats.norm.ppf(z_alfa2), 2)


def error(NC, n, s):
    """
    #e = z * σ/√n
    """
    return round((calcular_z(NC) * s) / math.sqrt(n), 2)


def intervalo_confianza(NC, n, x, s):
    """
    #[µ-e , µ+e]
    """
    e = error(NC, n, s)
    l_min = x - e
    l_max = x + e
    arr = [l_min, l_max]
    return arr


def tamanio_muestra(Z, P, e):
    """
    #(Z² * P * Q) / e²

    argumentos:
    @Z -- factor probabilistico
    @P -- valor esperado
    @e -- error max permitido
    """
    Q = 1 - P
    n0 = (Z * Z * P * Q) / (e * e)
    return int(math.ceil(n0))


def tamanio_muestra_ajustado(Z, P, N, e):
    """
    argumentos:
    @Z -- factor probabilistico
    @P -- valor esperado
    @N -- tamaño de población
    @e -- error max permitido
    """

    n0 = tamanio_muestra(Z, P, e)
    # n ajustado
    n1 = n0 / (1 + (n0 - 1) / N)
    return int(math.ceil(n1))
