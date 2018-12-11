print "hello world"
import math

def distance(a,b):
    x1, y1 = a
    x2, y2 = b
    #x1 = a[0]
    #y1 = a[1]
    #x2 = b[0]
    #y2 = b[1]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

#esercizi
a = 7
pi = math.pi

def isEven(x):
    if(x%2 == 0):
        return True
    else:
        return False

def avg(a,b):
    return (a + b)/2.0

def distanceAvg(a,b):
    avg = avg(a,b)
    return math.sqrt(a**2 - avg**2), math.sqrt(b**2 - avg**2)

a = a*2
b = a -1


def scalarProd(p,s):
    """
    prodotto scalare
    """
    x,y = p
    return x*s, y*s

    
