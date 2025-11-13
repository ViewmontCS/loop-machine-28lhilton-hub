import os 
from random import randint
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

score= 100
final_score=score
machine = [[randint(0,9), randint(0,9) , randint(0,9)],[randint(0,9), randint(0,9) , randint(0,9)],[randint(0,9), randint(0,9) , randint(0,9)]]
payouts = [5,10,15,20,25,30,35,40,45,50]
print("WELCOME to \"LETS GO GAMBLING\"")
print(f"you have {score} dollars to gamble with")
print("Each play costs five dollars")
play=input("would you like to play? y/n: ")

if play.lower() == "y":
    while score > 0:
        score = score -5
        for i in range(10):
            clear()
            machine = [[randint(0,9), randint(0,9) , randint(0,9)],[randint(0,9), randint(0,9) , randint(0,9)],[randint(0,9), randint(0,9) , randint(0,9)]]
            for row in machine:    
                for num in row:
                    print(f"|{num}|", end=" ")
                print()
            time.sleep(.1)
        if machine[0][0] == machine [0][1] and machine[0][0] == machine[0][2]:
            score += payouts[machine[0][0]]
            print(f"you won ${payouts[machine[0][0]]}")
        if machine[1][0] == machine [1][1] and machine[1][0] == machine[1][2]:
            score += payouts[machine[1][0]]
            print(f"you won ${payouts[machine[1][0]]}")
        if machine[2][0] == machine [2][1] and machine[2][0] == machine[2][2]:
            score += payouts[machine[2][0]]
            print(f"you won ${payouts[machine[2][0]]}")
        if machine[0][0] == machine [1][1] and machine[0][0] == machine[2][2]:
            score += payouts[machine[0][0]]
            print(f"you won ${payouts[machine[0][0]]}")
        if machine[0][2] == machine [1][1] and machine[0][2] == machine[2][0]:
            score += payouts[machine[0][2]]
            print(f"you won ${payouts[machine[0][2]]}")
        print(f"Your money is ${score}.")
        play= input("would you like to keep playing?: y/n: ")
        if play.lower() == "n":
            final_score = score
            break
        if score == 0:
            final_score = score


print("Big sad, no more gambling")
print(f"Your final amount of money is ${final_score}")
