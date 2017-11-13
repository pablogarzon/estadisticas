# coding=utf-8
from estimacion_estadistica import estimacion_parametros


# ¿A cuantas familias tendriamos que estudiar para conocer la
# preferencia del mercado en cuanto a las marcas de shampoo para
# bebe si se desconoce la población total?
# DATOS:
# Seguridad = 95%
# Precisión = 3%
# Valor esperado = 5%
def ejercicio_1():
    N=10000
    NC=95
    e= 0.03
    P=0.05
    Q= 1 - P

    Z = estimacion_parametros.calcular_z(NC)
    print("tamaño de muestra: " + str(estimacion_parametros.calcular_tamanio_muestra(Z, P, Q, e)))


# Supongamos una población que se distribuye normal, con media igual
# a 500 y desviación tipica igual a 30. Tomamos una muestra de
# 100 unidades y queremos conocer cúal es el riesgo de cometer un error
# de estimacion u, superior a 6
# DATOS:
# población ~N=(500;30)
# N = 100
# |e| > 6
# u = x
def ejercicio_2():
    x0 = 500 - 6
    x1 = 500 + 6




ejercicio_1()
