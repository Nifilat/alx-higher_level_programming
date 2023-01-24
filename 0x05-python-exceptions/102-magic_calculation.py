def magic_calculation(a, b):
    varr = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                varr += (a**b)/i
        except Exception:
            varr = (b + a)
            break
    return varr
