# coding=utf-8
import math

def media(arr):
    #̅x = (∑xᵢ)/n

    sum_xi = 0.0
    for xi in arr:
        sum_xi += xi

    return sum_xi/len(arr)

def varianza(arr):
    #s² = (∑xᵢ²/n) - ̅x²

    sum_xx = 0.0;
    for xi in arr:
        sum_xx += xi * xi

    return sum_xx/len(arr) - (media(arr) * media(arr))

def desv_standard(arr):
    #√s
    return round(math.sqrt(varianza(arr)),2)

def asimetria(arr):
    # sₖ = (∑(xᵢ - ̅x)³/n)/s³

    sum_ = 0.0
    mean = media(arr)
    deviation = desv_standard(arr)

    for xi in arr:
        sum_ += xi - (mean * mean * mean)

    result = (sum_ / len(arr)) / (deviation * deviation * deviation)

    return result
    #γ μ
