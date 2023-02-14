import time # Doesn't need an installationj
from termcolor import colored
import subprocess # Doesn't need an installation
import random # Doesn't need an installation


row_a = [1, 2, 3]
row_b = [4, 5, 6]
row_c = [7, 8, 9]


def automatic_move(symbol, movements):
    random_movement = random.choice(movements) - 1
    movements.remove(random_movement)

    if random_movement in row_a:
        position = row_a.index(random_movement)
        row_a[position] = colored(symbol, "red")
    elif random_movement in row_b:
        position = row_b.index(random_movement)
        row_b[position] = colored(symbol, "red")
    else:
        position = row_c.index(random_movement)
        row_c[position] = colored(symbol, "red")


def TikTakToe():
    subprocess.run('clear', shell=True)

    print(f"\r  {colored('A', 'yellow')}   {colored('B', 'yellow')}   {colored('C', 'yellow')}")
    print(f"\r{colored('A', 'yellow')} {row_a[0]} | {row_a[1]} | {row_a[2]}")
    print("\r  —   —   —")
    print(f"\r{colored('B', 'yellow')} {row_b[0]} | {row_b[1]} | {row_b[2]}")
    print("\r  —   —   —")
    print(f"\r{colored('C', 'yellow')} {row_c[0]} | {row_c[1]} | {row_c[2]}")


def game():
    first_loop = True
    second_loop = True

    available_movements = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    first_move = random.choice(['X', 'O'])

    while first_loop:
        symbol_player = input("\rWhich symbol do you want? (X, O): ")

        if symbol_player == "X":+
        -+
            symbol_bot = "O"
            first_loop = False

        elif symbol_player == "O":
            symbol_bot = "X"
            first_loop = False

        else:
            print(colored("\rInvalid input ", "red"), end="")
            time.sleep(2)


    TikTakToe()
    print(f"\nYour symbol: {symbol_player}")
    print(f"Bot's symbol: {symbol_bot}")
    print(f"First move by: {first_move}")

    input("\nPress enter to start the game...")

    if first_move == symbol_bot:
        automatic_move(symbol_bot, available_movements)

    while second_loop:
        TikTakToe()
        input("-> ")


def menu():
    r = True

    while r:
        start = input("\rLet's begin? (Y,n): ")

        if start == "Y":
            r = False
            game()

        elif start == "n":
            r = False
        else:
            print(colored("\rInvalid input ", "red"), end="")
            time.sleep(2)

def main():
    menu()


if __name__ == "__main__":
    main()