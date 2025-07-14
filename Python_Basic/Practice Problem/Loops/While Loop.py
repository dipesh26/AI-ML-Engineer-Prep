# 1: Simple While Loop
i = 0
while (i<=10):
    print(i)
    i += 1
print("While loop End's")

# 2: Guessing Game
# Create a program that allows the user to guess a secret number between 1 and 100.
# The program should keep prompting the user until they guess the correct number.
import random
secret_number = random.randrange(1,101)
print(secret_number)
while True:
    guess_number = int(input("Enter the number b/w 1 to 100: "))
    if guess_number >= 1 and guess_number <= 100:
        if guess_number == secret_number:
            print("✅ Congratulations! You guessed the correct number.")
            break
        else:
            print("❌ Wrong Number, Try again!\n")
    else:
        print("❌ Invlaid Number!")
        print("Please Enter the Number between 1 to 100\n")

# 3: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to a given number of terms.
num = int(input("Enter the Number: "))
a = 0
b = 1
count = 0
while count < num:
    print(a, end=" ")
    a, b = b, a+b
    count += 1

# 4: Rock, Paper, Scissors Game
# Create a program that allows two players to play a game of Rock, Paper, Scissors.
import random
print("----------------------------------")
print("|   Rock, Paper, Scissors Game   |")
print("----------------------------------")
print("Choose the option: [Rock: 0, Paper: 1, Scissors: 2]")
user_count = 0
bot_count = 0
option_list = ["Rock","Paper","Scissors"]
times = 1
while (times <= 10):
    user = int(input("Enter your option(0,1,2): "))
    if user >= 0 and user <= 2:
        user_choice = option_list[user]
        bot_choice = random.choice(option_list)
        print(f"\nYou: \"{user_choice}\"\nComputer: \"{bot_choice}\"")

        if user_choice == bot_choice:
            print("🎌 Tie")

        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Paper" and bot_choice == "Rock") or \
             (user_choice == "Scissors" and bot_choice == "Paper"):
            user_count += 1
            print("✅ Congratulations! You Won🏆 ✨🎉")
            
        else:
            bot_count += 1
            print("❌ You lose! Computer Won ✨🎉")

        print(f"You: {user_count}      Computer: {bot_count}\n")
        times += 1

    else:
        print("\n❗ Invalid input. Please enter 0, 1, or 2 only.\n")

# Final result after 10 rounds
print("------------ Game Over ------------")
if user_count == bot_count:
    print("🎌 Match Tie!")
elif user_count > bot_count:
    print(f"🎉✨ Congratulations! You Won the Match by {user_count - bot_count} points.")
else:
    print(f"❌ You Lost the Match by {bot_count - user_count} points. Better luck next time!")
