c = 0
def f2(x):
    try:
        c+= 1
        b = x + c
        print (c)
        return b
    except NameError:
        c=0
    except SyntaxError:
        print("The value of c is not defined")
try:
    print f2(1)
    print c 
except SyntaxError:
    a=f2(1)
    print(a)
    print(c) 