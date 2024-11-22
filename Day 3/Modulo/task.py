number = input("What is the number? ")
remainder = int(float(number) % float(2))

if remainder == 0:
    print("The number is even")
else:
    print("The number is odd")