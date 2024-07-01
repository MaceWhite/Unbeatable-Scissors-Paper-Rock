print("Scissors, Paper, or Rock? - ")

user_input = input()

if (user_input == "Scissors" or "scisscors"):
    print("Rock, I win!")
elif (user_input == "Paper" or "paper"):
    print("Scissors, I win!")
elif (user_input == "Rock" or "rock"): 
    print("Paper, I win!")
elif (user_input != "Scissors" or "Paper" or "Rock"):
    print("That's not an option, so I still win!")