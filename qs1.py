# Create a class called Add , it must have __call__ defined. Create an object of that class. 
# When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum 
# of elements in the list. 
# Eg: 
# add = Add() 
# total = add([1,2,3,4,5,6]) 

# Create a class called Add , it must have __call__ defined. Create an object of that class. 
# When the object is directly called with a list of integers - like - obj([1,2,3,4,5]) It must return the sum 
# of elements in the list. 
# Eg: 
# add = Add() 
# total = add([1,2,3,4,5,6]) 

class Add:
    def __init__(self):
        pass

    def __call__(self, numbers):
        if all(isinstance(num, int) for num in numbers):
            return sum(numbers)
        else:
            raise ValueError("Input list must contain only integers.")
add = Add()
try:
    numbers = input("Enter a list of integers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Please enter valid integers separated by spaces.")
    exit()

try:
    total = add(numbers)
    print("Total sum:", total) 
except ValueError as ve:
    print(ve)
