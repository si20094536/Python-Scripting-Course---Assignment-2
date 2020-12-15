class First: 
    def method1(self): 
        print("First Class")  
        
class Second(First): 
    def method1(self): 
        print("Second Class") 
  
class Third(First): 
    def method1(self): 
         print("Third Class")      
      
class Fourth(Second, Third): 
    def method1(self): 
        print("Fourth Class")    
  
obj = Fourth() 
obj.method1() 


Third.method1(obj)   
Second.method1(obj) 
First.method1(obj) 