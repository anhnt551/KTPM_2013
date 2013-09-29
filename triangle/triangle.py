import math
def tofloat (a,b,c):
    try:
        a=float(a)
        b=float(b)
        c=float(c)
    except ValueError:
        return "except"
def checknumber(a,b,c):
    if((type(a) in [int, float, long]) and (type(b) in [int, float, long]) and (type(c) in [int, float, long]) and (a>0 and a <= 2**32-1) and (b>0 and b <= 2**32-1) and (c>0 and c <= 2**32-1)):
        return 1
    else:
        return 0
def is_triangle(a,b,c):
    if((a + b) >= c)and((a+c) >= c)and((b+c) >= a):
        return 1
    else:   
        return 0
def is_regular(a,b,c):
    if((a==b)and(b==c)and(a==c)):
        return 1
    else:
        return 0
def is_square(a,b,c):
        if((math.fabs(a*a-b*b-c*c) <= 10**-9) or (math.fabs(c*c - a*a-b*b)<= 10**-9) or (math.fabs(b*b - c*c - a*a)<=10**-9)):
            return 1
        else:
            return 0
def is_balance(a,b,c):
    if(a==b)or(b==c)or(c==a):
        return 1
    else:
        return 0
def is_square_balance(a, b,c ):
    if((math.fabs(a*a-b*b-c*c) <= 10**-9 and b==c) or (math.fabs(c*c - a*a-b*b)<= 10**-9 and a==b) or (math.fabs(b*b - c*c - a*a)<=10**-9 and a==c)):
        return 1
    else:
        return 0
def detect_triangle(a,b,c):
    #if tofloat(a,b,c):  
        if checknumber(a,b,c)== 0:
            return "Exception"
        else:
            if is_triangle(a,b,c)==0:
                return "Not triangle"
            else:
                if is_regular(a,b,c):
                    return "triangle is regular"
                elif is_balance(a,b,c):
                    if is_square_balance(a,b,c):
                        return "triangle is square and balance"
                    else:
                        return "triangle is balance"
                elif is_square(a,b,c):
                    return "triangle is square"
                else:
                    return "triangle is normal"

    
