print("Number of letters in your name: " + str(len(input("Enter your name "))))

#The lines of code below is Miko's Code for the line above
ask_for_name = "Type your name: "
no_of_name = "Number of letters in your name: "

name = input(ask_for_name)
length = str(len(name))

print(no_of_name + length)