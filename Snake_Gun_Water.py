import random

Dict = {"s": 1, "w": -1, "g": 0}
reverse_Dict = {1: "Snake", -1: "Water", 0: "Gun"}

while True:
    Your_choice = input("Enter your choice (s, w, g) or 'exit' to quit the game: ").strip().lower()
    
    if Your_choice == "exit":
        print("Thanks for playing!")
        break
    
    if Your_choice not in Dict:
        print("Invalid input. Please enter 's', 'w', 'g', or 'exit'.")
        continue

    Computer = random.choice([1, -1, 0])
    You = Dict[Your_choice]
    Reverse_You = reverse_Dict[You]
    Reverse_Computer = reverse_Dict[Computer]

    print(f"\nYou chose: {Reverse_You}")
    print(f"Computer chose: {Reverse_Computer}")

    if Computer == You:
        print("It's a draw!")
    elif (Computer == 0 and You == -1) or (Computer == -1 and You == 1) or (Computer == 1 and You == 0):
        print("You win!")
    else:
        print("You lose!")
    print("-" * 30)
