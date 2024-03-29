print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
print(playing)

if playing != "Yes":
    quit()

print("Okay! Let's play :")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Incorrect!")
