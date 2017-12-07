# coding=utf-8
import math

def media(arr):
    """
    #̅x = (∑xᵢ)/n
    """
    sum_xi = 0
    for xi in arr:
        sum_xi += xi

    return round(sum_xi/len(arr),2)

def mediana(arr):
    """
    #(n + 1)/2
    """
    me=0
    arr.sort()
    x = (len(arr) + 1)/2

    if (len(arr) % 2 == 0):
        me1 = int(x) - 1
        me2 = math.ceil(x) - 1
        me = (arr[me1] + arr[me2])/2
    else:
        me = arr[x]

    return round(me,2)

def moda(arr):
    max_ = 1
    mode = 0
    dict_ = dict()

    arr.sort()
    for i in list(range(len(arr))):
        if arr[i] in dict_:
            count = dict_[arr[i]]
            count = count + 1
            dict_[arr[i]] = count
            if count > max_:
                max_ = count
                mode = arr[i]
        else:
            dict_[arr[i]] = 1
    return mode

def varianza(arr):
    """
    #s² = (∑xᵢ²/n) - ̅x²
    """
    sum_xx = 0
    for xi in arr:
        sum_xx += xi * xi

    return round(sum_xx/len(arr) - (media(arr) * media(arr)),2)

def desv_standard(arr):
    """
    #√s
    """
    return round(math.sqrt(varianza(arr)),2)

def asimetria(arr):
    """
    # sₖ = (∑(xᵢ - ̅x)³/n)/s³
    """
    sum_ = 0
    mean = media(arr)
    deviation = desv_standard(arr)

    for xi in arr:
        sum_ += xi - (mean * mean * mean)

    result = (sum_ / len(arr)) / (deviation * deviation * deviation)

    return round(result,2)
