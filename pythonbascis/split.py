def max_value(s):
    p=s.split()
    add=int(p[0])+int(p[1])
    mul=int(p[0])*int(p[1])
    if add>mul:
        return add
    else:
        return mul
    return max_value()
