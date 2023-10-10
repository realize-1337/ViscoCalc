import math
import sympy as sp


def createEq(a, b, alpha):
    eq = sp.Eq(alpha, 1-c+(a*b*c*(1-c))/(a*c+b*(1-c)))
    return eq

def createViscosity(my, w, g):
    eq = sp.Eq(my, w**a*g**(1-a))
    return eq

def calcMy_g(T):
    return 12100*math.exp((-1233+T)*T/(9900+70*T))

def calcMy_w(T):
    return 1.790*math.exp((-1230-T)*T/(36100+360*T))

if __name__ == '__main__':
    c = sp.Symbol('c')
    a = sp.Symbol('a')
    targetViscosity = float(input('Ziel-Viskosität in mPa s angeben: '))
    T = float(input('Aktuelle Umgebungtemperatur in °C angeben: '))

    print(f'Ziel-Viskosität {targetViscosity} mPa s bei {T} °C')
    
    eq_alpha = createViscosity(targetViscosity, calcMy_w(T), calcMy_g(T))

    alpha = sp.solve(eq_alpha, a)[0]
    eq = createEq(0.671, 2.072, alpha)

    results = [x for x in sp.solve(eq,c) if x <=1 and x >= 0]
    print(f'Bei {T} °C werden für eine Zielviskosität von {targetViscosity} mPa s {"%.2f" % (results[0]*100)} wt-% Glycerin benötigt!')
    input('Bitte Enter zum beednden...')
