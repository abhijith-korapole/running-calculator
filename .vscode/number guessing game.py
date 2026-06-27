import random 
print("welcome to the number guessing game!")
print("im thinking of a number between 1-100")
difficulty = input("choose the type of difficulty: easy/medium/hard: ").lower()
if difficulty == "easy":
    attempts = 10
elif difficulty == "medium":
    attempts = 7
elif difficulty == "hard":
    attempts = 5
else:
    print("invalid difficulty level. plase choose easy / medium / hard") 
    exit()
computer_choice = random.randint(1,100)
for i in range(attempts,0,-1):
       print(f"you have {i} attempts to guess the number")
       guess = int(input("make a guess: "))
       if guess>computer_choice:
        print("too high")
       elif guess<computer_choice:
        print("too low")
       elif guess == computer_choice:
          print(f"you win!")
          break
else:
         print(f"you loose! the answer was {computer_choice}")
         
       
       