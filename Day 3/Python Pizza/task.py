#from http.cookiejar import uppercase_escaped_char

small_pizza = 15
medium_pizza = 20
large_pizza = 25
add_pepperoni_small = 2
add_pepperoni_medium = 3
add_pepperoni_large = 3
add_cheese = 1
total_price = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")



#if pizza size is small
if size.upper() == "S":
    total_price = small_pizza
    if pepperoni.upper() == "Y":
        total_price = total_price + add_pepperoni_small
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
    else:
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
        else:
            total_price = total_price


#if pizza size is medium
elif size.upper() == "M":
    total_price = medium_pizza
    if pepperoni.upper() == "Y":
        total_price = total_price + add_pepperoni_medium
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
    else:
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
        else:
            total_price = total_price


#If pizza size is Large
else:
    total_price = large_pizza
    if pepperoni.upper() == "Y":
        total_price = total_price + add_pepperoni_large
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
    else:
        if extra_cheese.upper() == "Y":
            total_price = total_price + add_cheese
        else:
            total_price = total_price

print(f"Your final bill is: ${total_price}.")