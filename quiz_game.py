print("Welcome to the QUIZ!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play! :)")
score = 0

answer = input("In what year did Home Alone hit the box office? ")
if answer.lower() == "1990":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Is 5 + 5 equal to 10? ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Was Abraham Lincoln the 14th President of the USA? ")
if answer.lower() == "no":
    print("Good job!")
    score += 1
else:
    print("Go study!!")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/3 * 100) + "%.")