

def gen(num):
    a,b=0,1
    for i in range(0,num):
        yield (a)
        a,b=b,a+b
    for items in gen(10):
        print (items)