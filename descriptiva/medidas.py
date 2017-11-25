# coding=utf-8
import math

def media(arr):
    #̅x = (∑xi)/n

    sum_xi = 0.0
    for i in (arr):
        sum_xi += i

    return sum_xi/len(arr)

def varianza(arr):
    #s² = (∑xi²/n) - ̅x²

    sum_xx = 0.0;
    for i in (arr):
        sum_xx += i * i

    return sum_xx/len(arr) - (media(arr) * media(arr))

def desv_standard(arr):
    return round(math.sqrt(varianza(arr)),2)
