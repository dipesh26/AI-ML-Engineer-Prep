import random
print("----------------------------------")
print("|   Rock, Paper, Scissors Game   |")
print("----------------------------------")
print("This is a computerized version of the classic game.\n"
      "Your opponent is a bot that randomly selects Rock, Paper, or Scissors.\n"
      "Play 10 rounds and try to beat the bot. Good luck!\n")
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
            print("🤝 It's a tie! So close!")

        elif (user_choice == "Rock" and bot_choice == "Scissors") or \
             (user_choice == "Paper" and bot_choice == "Rock") or \
             (user_choice == "Scissors" and bot_choice == "Paper"):
            user_count += 1
            print("✅ Congratulations! You Win! 🏆✨")
            
        else:
            bot_count += 1
            print("😢❌ Oops! The Computer Wins!")

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