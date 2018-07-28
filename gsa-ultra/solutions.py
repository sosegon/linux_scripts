def across5(a, b):
    assert len(a) > 0 and len(b) > 0
    n = 0
    while len(a) > 0:
        r = True
        i = 1
        while r and i < len(a):
            r = a[:i] in b
            if r:
                i = i + 1

        if i < len(a):
            a = a[i-1:]
        else:
            a = a[1:]
        n = n + 1

    return n