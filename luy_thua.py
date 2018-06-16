def luy_thua():
    n = 0
    mang = []
    while True:
        if 2 ** n < 2015:
            mang.append(2 ** n)
            n += 1
        else:
            break
    return mang