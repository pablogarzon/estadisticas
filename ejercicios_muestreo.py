# coding=utf-8
from inferencial import muestreo
from descriptiva import medidas

arr=[22,21,19,25,26]
print(muestreo.promedio_ponderado([30,20], [20.7, 25.5]))


# ejercicio_2:
#-------------------------------------------------------------
#                       Afijaciones
# ------------------------------------------------------------
# Estrato |  Ni  |   Oi  |   Igual   | Proporcional | Óptima |
# ------------------------------------------------------------
#   1     | 1800 |  4,2  |    ?      |      ?       |    ?
#   2     | 1500 |  5,5  |    ?      |      ?       |    ?
#   3     | 1200 |  7,1  |    ?      |      ?       |    ?
#   4     | 500  |  10,3 |    ?      |      ?       |    ?
#   ∑     | 5000 |       |           |              |

# calculos: n=250

print("\n1)igual:")
print(muestreo.afijacion_igual(250, 4))
print("\n2) proporcional:")
print("n1:" + str(muestreo.afijacion_prop(1800, 5000, 250)))
print("n2:" + str(muestreo.afijacion_prop(1500, 5000, 250)))
print("n3:" + str(muestreo.afijacion_prop(1200, 5000, 250)))
print("n4:" + str(muestreo.afijacion_prop(500, 5000, 250)))
print("\n3) optima:")
print("n1:" + str(muestreo.afijacion_optima([1800,1500,1200,500],[4.2,5.5,7.1,10.3],250,0)))
print("n2:" + str(muestreo.afijacion_optima([1800,1500,1200,500],[4.2,5.5,7.1,10.3],250,1)))
print("n3:" + str(muestreo.afijacion_optima([1800,1500,1200,500],[4.2,5.5,7.1,10.3],250,2)))
print("n4:" + str(muestreo.afijacion_optima([1800,1500,1200,500],[4.2,5.5,7.1,10.3],250,3)))
