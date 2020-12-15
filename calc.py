def factorial(num):
    r=1
    for i in range(2,num+1):
        r=r*i
    return r

def log10(num):
    import math
    return math.log10(num)

def deg_to_rad(num):
    return (3.14/180)*num

def trigo(num):
    import math
    return(math.sin(num),math.cos(num),math.tan(num))

    

