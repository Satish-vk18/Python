import random

def get_choices():
    player_choice = input("Enter a choice (rock , paper , scissor) : ")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)
    choices = {
        "player" : player_choice,
        "computer" : computer_choice
    }
    return choices
    
def get_win(player,computer):
    print(f"you choosen {player} , computer choosen {computer}")
    if player == computer:
        return "It's tie !"
    elif player == 'rock':
        if computer == 'paper':
            return "paper covers rock , you loose !"
        else:
            return "rock smashes scissor , you win !"
    elif player == 'paper':
        if computer == 'rock':
            return "paper covers rock , you win !"
        else:
            return "scissor cuts paper , you loose !"
    elif player == 'scissor':
        if computer == 'rock':
            return "rock smashes scisssor, you loose !"
        else:
            return "scissor cuts paper , you win !"
    else:
        return "you chooses wrong option"

choices = get_choices()
print(get_win(choices["player"],choices["computer"]))
