import re

def thirdHighest(array) :
    if (isinstance(array, list)) :
        if (len(array)<3) :
            print("Minimal array length is 3!")
        elif (len(array)>=3) :
            array.sort()
            print(array[-3])
    elif (array != list):
        print("Parameter should be an array")

thirdHighest([1,5,12,3,51,555])