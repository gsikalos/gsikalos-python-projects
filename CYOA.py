answer = input("Would you like to play a little game? (yes/no) ")

if answer.lower().strip() == "yes":

    answer = input("You reach a fork in the road.  Do you go left or right? (left/right) ").lower().strip()
    if answer == "left":
        answer = input("As you head down the dark wooded path, you hear unfamiliar whispers and strange noises.  A creature of unexplainable origins appears before you! You see a large stick nearby. Do you pick up the stick and attack or run? (attack/run) ")
        if answer == "attack":
            print("You quickly grab the stick and swing as hard as you can.  The creature howls in pain and runs away.")
        else:
            print("Wise choice, but your speed is no match for this blood-hungry creature of the night. He attacks you from behind and viciously tears apart your flesh. The End.")

    elif answer == "right":
        answer = input("As you head down the dark wooded path, you see a little child crying.  Do you approach or avoid? (approach/avoid)")
        if answer == "approach":
            print("The child stops sobbing as you draw near. Then it turns arond to reveal itself as a demonic spirit and vaporizes you.  The End.")
        else:
            print("You slunk passed the 'child' and avoid a fate worse than any death. Close one!")

else:
    print("Goodbye, coward!")

