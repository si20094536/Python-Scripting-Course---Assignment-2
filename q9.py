class natural_numbers:
    def __iter__(self):
        self.number = 1
        return self
    def __init__(self, max = 0):
        self.max = max
    def __next__(self):
        if self.max == self.number:
            raise StopIteration
        else:
            number = self.number
            self.number += 1
            return number
numbers=natural_numbers(11)

print("Original list/sequence : ")
for i in numbers:
    print(i)
print("The sequence in the reverse order.!!.    :")
list1=[]
for i in numbers:
    list1.append(i)
print(list1[::-1]) 