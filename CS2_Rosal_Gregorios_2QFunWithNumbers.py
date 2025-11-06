age = int(input("Hi there! Please enter your age: "))
total = 0
for x in range(1, age + 1):
    total = total + x
print("The sum of all numbers from 1 to", age, "is:", total)