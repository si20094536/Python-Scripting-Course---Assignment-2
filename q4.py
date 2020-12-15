import re

def func(txt):
    x = re.search("^digit.*string$", txt)
    y=re.search("^A.*characters$", txt)
    z=re.search("^A.*characters$", txt)
    if (x or y or z):
        print("YES! We have a match!")
    else:
        print("No match")

func("digit at the beginning of the string and a digit at the end of the string")
func("A string that contains only whitespace characters or word characters")
func("A string containing no whitespace characters")