# ackley function
from math import sqrt, sin, cos, exp

def ackley(values):
    # ackley function "constants"
    a = 20
    b = 0.2
    c = 6.14
    d = len(values)

    # calc
    soma1 = 0.0
    soma2 = 0.0

    for x in values:
        soma1 += x*x
        soma2 += cos(c*x)

    soma1 /= d
    soma2 /= d

    # ackley
    result = -a*exp(-b*sqrt(soma1)) - exp(soma2) + a + exp(1)

    # ans
    return result
