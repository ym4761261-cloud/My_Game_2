import random

# تخزين الصور في متغيرات
Rock_ascii = '''
    _ _ _
---'_ _ _)
----(_ _ _)
----(_ _ _ )
----(_ _ _)
--.(_ _ _)
'''
paper_ascii = '''
    _ _ _ _ _ _
---'     _ _ _ _)
---       _ _ _ _ ) 
---        _ _ _ _ )
---       _ _ _ _ )
---._ _ _ _ _ _ _)
'''
scissors_ascii = '''
    _ _ _ 
---'      )_ _ _
---     _ _ _ _ _ _ )
---       _ _ _ _ _ _)
---(_ _ _ _ _)
---(_ _ _ _)
'''

# مرحلة بداء اللعبة
print("\nWelcome to the Rock, Paper, Scissors Game!😍")
confirm = input("Press Enter to start the game or type 'Help' for the rules: ").lower()

if confirm == "help":
    print("""
               **********RULES OF THE GAME********
            1. You choose either Rock, Paper, or Scissors.
            2. Rock smashes Scissors, Scissors -> Rock Wins.
            3. Paper covers Rock, Rock -> Paper Wins.
            4. Scissors cuts Paper, Paper -> Scissors Wins.
""")
User_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()
if User_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please choose Rock, Paper, or Scissors.😡")
else:
    # اختيار الكمبيوتر عشوائياً
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose: {User_choice.capitalize()}")
    print(f"Computer chose: {computer_choice.capitalize()}")

    # عرض الصور بناءً على الاختيار
    if User_choice == "rock":
        print(Rock_ascii)
    elif User_choice == "paper":
        print(paper_ascii)
    elif User_choice == "scissors":
        print(scissors_ascii)

    if computer_choice == "rock":
        print(Rock_ascii)
    elif computer_choice == "paper":
        print(paper_ascii)
    elif computer_choice == "scissors":
        print(scissors_ascii)

    # تحديد الفائز
    if User_choice == computer_choice:
        print("It's a tie! 😐")
    elif (User_choice == "rock" and computer_choice == "scissors") or \
            (User_choice == "paper" and computer_choice == "rock") or \
            (User_choice == "scissors" and computer_choice == "paper"):
        print("Congratulations! You win! 🥳")
    else:
        print("Sorry! You lose. 😢")