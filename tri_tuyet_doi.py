def tri_tuyet_doi(x):
    sum_abs = 0
    for i in range(len(x)):
        sum_abs += abs(x[i])
    return sum_abs
