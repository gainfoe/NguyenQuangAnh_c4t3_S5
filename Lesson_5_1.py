def tim_max(arr_):
    maximum = arr_[0]
    for i in range(len(arr_)):
        if arr_[i] > maximum:
            maximum = arr_[i]
    return maximum

def chu_vi(a, b, c):
    return a + b + c