import random


def play():
    user = input(
        "What's your choice? >> 'r', for rock, 'p', for paper and 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


# Add this to actually run the game when the script is executed
if __name__ == "__main__":
    print(play())
