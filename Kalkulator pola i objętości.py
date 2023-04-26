import math

def P_kwadrat(a):
    return a*a

def P_kwadrat_przekatne(d):
    return (1/2)*(d*d)

def Ob_kwadrat(a):              ### to to samo co ob rombu
    return 4*a

def P_prostokat(a,b):           ### to to samo co pole rownolegloboku oraz rombu tylko parametr b to h
    return a*b

def Ob_prostokat(a,b):          ### to to samo co ob rownolegloboku oraz deltoidu
    return (2*a)+(2*b)

def P_trapez(a,b,h):
    return ((1/2)*a*b)*h

def Ob_trapez(a,b,c,d):
    return a+b+c+d

def P_romb_przekatne(d,p):      ### to to samo co pole deltoidu
    return (1/2)*d*p

def P_trojkat(a,h):
    return (a*h)/2

def Wysokosc_t_rownobocznego(a):
    return a*(math.sqrt(3/2))

def P_t_rownobocznego(a):
    return a*a*(math.sqrt(3/2))

def P_kola(r):
    return (math.pi)*(r*r)

def V_kuli(r):
    return (4/3)*(math.pi)*(r*r*r)

def P_kuli(r):
    return 4*(math.pi)*(r*r)

def V_stozka(r,H):
    return (1/3)*(math.pi)*(r*r)*H

def P_stozka(r,l):
    return (math.pi)*r*(r+l)

def P_walca(r,H):
    return 2*(math.pi)*r*(r+H)

def V_walca(r,H):
    return (math.pi)*r*r*H

def P_szescianu(a):
    return 6*(a*a)

def V_szescianu(a):
    return a*a*a


