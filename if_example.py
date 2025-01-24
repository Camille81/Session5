# you have 3 lives. I roll the dice, If I roll 6 you win
# if not a 6 you loose 1 life

from random import randint

lives = 3
while lives > 0:
    roll = randint (1,6) #make sure to not put a and b
    if roll == 6:
        print ("You rolled a 6, YOU WIN!")
        break # this exists the while even if lives still >0
    else:
        print(f"You rolled a {roll}! You lose a life")
        lives -=1
        print(f"Lives left: {lives}")
if lives == 0:
    print("You lost")
