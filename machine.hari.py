import random
def carrom_guess_game():
    print("welcome to play carrom boar Guessing Game!")
    print("guess the point scored by the striker(possible value=1,2,3,4,5)!")
    points=[1,2,3,4,5]
    score=0
    round=5 
    for count in range(1,round+1):
        print(f"\n round {count}")
        actual_points=random.choice(points)
        guess=int(input("enter your guess:"))
        if guess==actual_points:
            print(f"correct!the striker scored{actual_points} points")
            score+=10
        if guess not in points:
            print("Invalid guess.Guess the valid number")
            continue
        else:
            print(f"wrong!the striker scored{actual_points} points")
            print("Better luck next time")
    print(f"\n Game over! your total score={score}")
    if score > 30:
        print("great play")
    else:
        print("Good try")
carrom_guess_game()
