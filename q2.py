def func(a,b):
    try:
        print(a+b)
    except KeyboardInterrupt:
        print ("Interrrupted")
    except NameError:
        print ("Not defined")
    except ArithmeticError:
        print ("Check the expression once again.!!.")
    else:
        print("Nothing went wrong.!!.")
    finally:
        print("This is a cool way to add two numbers.!!.")
func(10,15)
