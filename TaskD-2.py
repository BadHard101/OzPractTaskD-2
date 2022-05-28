import math

def funZ (x, y):
    return 4.31 * math.log(2 * pow(x, 4), math.exp(1)) + 0.05 * pow(math.cos(y), 2)


def funB (x, a, k, y):
    return ( (math.exp(2 * y)*math.sin(x)) / (math.fabs(math.pow(x, 3)-1)-a*k) + math.atan(2*y) - k * math.log(pow(a,3), 4) )

if __name__ == '__main__':
    print(funZ(2, 3))
    print(funB(2, 5, 4, 6))