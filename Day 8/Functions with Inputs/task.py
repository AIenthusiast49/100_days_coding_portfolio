# def greet():
#     print(f"Hello {name}")
#     print("2")
#     print("3")
#
# name = ""
#
# greet()

# def greet_with_name():
#     print(f"Hello {name}!")
#     print(f"What it is like in {location}?")
#
#
# name = "Angela"
# location = "Newark"
# greet_with_name()

def calculate_love_score(name1,name2):
    true_points = 0
    love_points = 0
    for letters in name1:
        if letters.lower() == "t":
            true_points += 1
        if letters.lower() == "r":
            true_points += 1
        if letters.lower() == "u":
            true_points += 1
        if letters.lower() == "e":
            true_points += 1
        if letters.lower() == "l":
            love_points += 1
        if letters.lower() == "o":
            love_points += 1
        if letters.lower() == "v":
            love_points += 1
        if letters.lower() == "e":
            love_points += 1
    for letters in name2:
        if letters.lower() == "t":
            true_points += 1
        if letters.lower() == "r":
            true_points += 1
        if letters.lower() == "u":
            true_points += 1
        if letters.lower() == "e":
            true_points += 1
        if letters.lower() == "l":
            love_points += 1
        if letters.lower() == "o":
            love_points += 1
        if letters.lower() == "v":
            love_points += 1
        if letters.lower() == "e":
            love_points += 1
    print(f"{true_points}{love_points}")


calculate_love_score("Michael","Maricar")
