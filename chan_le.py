def chan_le(n):
    mang = []
    for i in range(n):
        if i % 2 == 1:
            mang.append(-1)
        else:
            mang.append(2 - i * 0.25)
    return mang
