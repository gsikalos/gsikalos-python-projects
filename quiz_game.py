print("Welcome to the QUIZ!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play! :)")

answer = input("In what year did Home Alone hit the box office? ")
if answer == "1990":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Is 5 + 5 equal to 10? ")
if answer == "yes":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("Was Abraham Lincoln the 14th President of the USA? ")
if answer == "no":
    print("Good job!")
else:
    print("Go study!!")