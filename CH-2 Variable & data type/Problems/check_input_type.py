# Check the type of variable assigned using input() function

a = input("Enter a Number: ")

t = type(a)
print(t) # Should print as a String.


a = int(input("Enter a Number: "))

t = type(a)
print(t) #Should Print as an Interger.