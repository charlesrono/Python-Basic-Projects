name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()
if answer == "left":
    answer= input("You come to a river, you can walk around it or swim across? Type walk to walk aroung and swim to sim across")

    if answer == "swim":
        print("You swam across and were eated by an alligator")

    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")

    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    print("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
else:
    print('Not a valid option. You lose.')

