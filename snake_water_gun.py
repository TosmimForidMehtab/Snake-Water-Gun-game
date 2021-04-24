import random
lst = ['s', 'w', 'g']
choices = int(input("How many times do you want to play the game: "))
c_point = 0
h_point = 0
while choices > 0:
    h_inp = input("S for snake W for Water and G for Gun: ").lower()
    c_inp = random.choice(lst)
    # Conditions
    if h_inp == c_inp:
        print("\nYour choice and computer's choice is same")
        print(f"You have {h_point} points and computer has {c_point} points")
        continue
    # If user enters S
    elif h_inp == 's' and c_inp == 'w':
        h_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("You Win this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    elif h_inp == 's' and c_inp == 'g':
        c_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("Computer wins this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    # If user enters W
    elif h_inp == 'w' and c_inp == 'g':
        h_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("You Win this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    elif h_inp == 'w' and c_inp == 's':
        c_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("Computer Wins this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    # If user enters G
    elif h_inp == 'g' and c_inp == 's':
        h_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("You Win this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    elif h_inp == 'g' and c_inp == 'w':
        c_point += 1
        print(f"\nYour guess was {h_inp} and computer's guess was {c_inp}")
        print("Computer wins this round")
        print(f"You have {h_point} points and computer has {c_point} points")
    else:
        print("Invalid Input")
        continue
    choices -= 1
    print(f"\t\tYou have {choices} choices left\n")
print(f"Your total score is {h_point} and Computer's total score is {c_point}")
if c_point > h_point:
    print("\n\t\t\t😞You LOST the game😞")
elif h_point > c_point:
    print("\n\t\t\t🎊You WON the game🎊")
else:
    print("\n\t\t\tIt's a TIE")