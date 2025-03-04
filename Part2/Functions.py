def greet(name="User", repeat=0):
    for i in range(repeat + 1):
        print("Hi there!!", name)

greet("Vedant", 2)


#taking another function example
def square_n(x):
    return x**2
print(square_n(5))   # Output: 25
print(square_n(-3))  # Output: 9
print(square_n(2.5)) # Output: 6.25
