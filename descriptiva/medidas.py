# coding=utf-8
import math
import numpy

def media(arr):
    #x = (∑xi)/n
    return numpy.mean(arr)

def varianza(arr):
    #s² = ∑(xi² -nx²)/n-1
    return round(numpy.var(arr),2)

def desv_standard(arr):
    return round(numpy.std(arr,ddof=1),2)
