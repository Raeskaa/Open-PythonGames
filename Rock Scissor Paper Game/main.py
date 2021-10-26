import random

player = 0
cpu = 0

print("Three points to win the game!")

while player < 3 and cpu < 3:
    cpu_choice = random.choice(["rock", "paper", "scissor"])
    player_choice = input("Rock, Paper or Scissor: ")

    print(f"CPU: {cpu_choice} VS Player: {player_choice}")

    if player_choice.lower() == cpu_choice:
        print("Tie! No points!")
    elif player_choice.lower() == "rock":
        if cpu_choice == "scissor":
            player += 1
            print(f"Player wins! One Point!")
        elif cpu_choice == "paper":
            cpu += 1
            print(f"CPU wins! One Point!")
    elif player_choice.lower() == "scissor":
        if cpu_choice == "paper":
            player += 1
            print(f"Player wins! One Point!")
        elif cpu_choice == "rock":
            cpu += 1
            print(f"CPU wins! One Point!")
    elif player_choice.lower() == "paper":
        if cpu_choice == "rock":
            player += 1
            print(f"Player wins! One Point!")
        elif cpu_choice == "scissor":
            cpu += 1
            print(f"CPU wins! One Point!")
    else:
        print("Invalid input! New round!!!")

print("Player Wins!" if player > cpu else "CPU Wins!")