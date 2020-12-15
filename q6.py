class sqroot:
    def func_sqrt(self):
        print("The square - root.:--------")
        input0=int(input("Enter the number"))
        import math
        print(math.sqrt(input0))
class addition:
    def func_add(self):
        print("The sumation.:--------")
        input1=int(input("Enter 1st number"))
        input2=int(input("Enter 2nd number.!!."))
        print (input1+input2)
class subtraction:
    def func_sub(self):
        print("The subtraction.:--------")
        input1=int(input("Enter 1st number"))
        input2=int(input("Enter 2nd number.!!."))
        print(input1-input2)
class multiplication:
    def func_mult(self):
        print("The multiplication.:--------")
        input1=int(input("Enter 1st number"))
        input2=int(input("Enter 2nd number.!!."))
        print (input1*input2)
class division:
    def func_div(self):
        print("The division.:--------")
        input1=int(input("Enter 1st number"))
        input2=int(input("Enter 2nd number.!!."))
        print (input1/input2)
class Mathnew (sqroot,addition,subtraction,multiplication,division):
    def all_the_details(self):
        print("Here are all the details : ")

obj= Mathnew()
obj.all_the_details()

sqroot.func_sqrt(obj)
addition.func_add(obj)
subtraction.func_sub(obj)
multiplication.func_mult(obj)
division.func_div(obj)



    