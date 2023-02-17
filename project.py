import time # Doesn't need an installationj
from termcolor import colored
import subprocess # Doesn't need an installation
import random # Doesn't need an installation


class Player:
    def __init__(self, symbol_player, available_movements, rows):
        self.symbol_player = symbol_player
        self.available_movements = available_movements
        self.rows = rows

    def movement(self):
        self.r = True

        while self.r:
            try:
                self.number = int(input("\rYour turn -> "))

                if self.number in self.rows:
                    self.available_movements.remove(self.number)
                    position = self.rows.index(self.number)
                    self.rows[position] = self.symbol_player

                    return board(self.rows)

                else:
                    print(colored("\rInvalid input", "red"), end="")
                    time.sleep(2)

            except ValueError:
                print(colored("\rInvalid input", "red"), end="")
                time.sleep(2)


class Bot:
    def __init__(self, symbol_bot, available_movements, rows):
        self.symbol_bot = symbol_bot
        self.available_movements = available_movements
        self.rows = rows

    def movement(self):
        try:
            random_movement = random.choice(self.available_movements)
        except IndexError:
            return ""

        if random_movement in self.rows:
            self.available_movements.remove(random_movement)

            position = self.rows.index(random_movement)
            self.rows[position] = self.symbol_bot

            return board(self.rows)   


def game(dict_symbols):
    rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    available_movements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    last_movement = ""

    first_move = random.choice(['X', 'O'])

    board(rows)
    print(f"\n> Your symbol: {colored(dict_symbols['Player'], 'green')}")
    print(f"> Bot's symbol: {colored(dict_symbols['Bot'], 'red')}")


    if first_move == dict_symbols["Player"]:
        print(f"> First move by: {colored(dict_symbols['Player'], 'green')}")
    else:
        print(f"> First move by: {colored(dict_symbols['Bot'], 'red')}")

    input("\nPress Enter to continue...")

    if first_move == dict_symbols["Bot"]:
        Bot(dict_symbols["Bot"], available_movements, rows).movement()
        last_movement = dict_symbols["Bot"]
    else:
        Player(dict_symbols["Player"], available_movements, rows).movement()
        last_movement = dict_symbols["Player"]
    
    r = True
    while r:

        if last_movement == dict_symbols["Player"]:
            check_tris_bot = check_tris(dict_symbols["Bot"], rows)


            if check_tris_bot == None:
                Bot(dict_symbols["Bot"], available_movements, rows).movement()
                check_tris(dict_symbols["Bot"], rows)
                last_movement = dict_symbols["Bot"]
            else:
                r = False
                message, symbol = check_tris_bot.split(":")
                print(f"{message}:{colored(symbol, 'red')}")
                print()

                for i in range(5, 0, -1):
                    print(f"\rRestart gameplay in {i}...", end="")
                    time.sleep(1)

                subprocess.run('clear', shell=True)
                choose_symbol()
        else:

            check_tris_player = check_tris(dict_symbols["Player"], rows)

            if check_tris_player == None:
                Player(dict_symbols["Player"], available_movements, rows).movement()
                check_tris(dict_symbols["Player"], rows)
                last_movement = dict_symbols["Player"]
            else:
                r = False
                message, symbol = check_tris_player.split(":")
                print(f"{message}:{colored(symbol, 'green')}")
                print()

                for i in range(5, 0, -1):
                    print(f"\rRestart gameplay in {i}...", end="")
                    time.sleep(1)

                subprocess.run('clear', shell=True)
                choose_symbol()


def check_tris(symbol, rows):
    if symbol == "X":
        symbol = '\x1b[32mX\x1b[0m'

    if symbol == "O":
        symbol = '\x1b[31mO\x1b[0m'
    
    victory_message = f"\nThe winner of this game is: {symbol}"

    # Horizontal win
    if rows[0] == symbol and rows[1] == symbol and rows[2] == symbol:
        return victory_message
    elif rows[3] == symbol and rows[4] == symbol and rows[5] == symbol:
        return victory_message
    elif rows[6] == symbol and rows[7] == symbol and rows[8] == symbol:
        return victory_message

    # Vertical Win
    elif rows[0] == symbol and rows[3] == symbol and rows[6] == symbol:
        return victory_message
    elif rows[1] == symbol and rows[4] == symbol and rows[7] == symbol:
        return victory_message
    elif rows[2] == symbol and rows[5] == symbol and rows[8] == symbol:
        return victory_message

    # Diagonal Win
    elif rows[0] == symbol and rows[4] == symbol and rows[8] == symbol:
        return victory_message
    elif rows[2] == symbol and rows[4] == symbol and rows[6] == symbol:
        return victory_message


def assign_symbol(symbol_player):
    symbol_player = symbol_player

    if symbol_player == "X":
        symbol_bot = "O"
        return {"Player": symbol_player, "Bot": symbol_bot}

    elif symbol_player == "O":
        symbol_bot = "X"
        return {"Player": symbol_player, "Bot": symbol_bot}


def board(rows):
    subprocess.run('clear', shell=True)

    for i in rows:
        if i == "X":
            position = rows.index(i)
            rows[position] = colored("X", "green")
        if i == "O":
            position = rows.index(i)
            rows[position] = colored("O", "red")

    print(f" {rows[0]} {colored('|', 'yellow')} {rows[1]} {colored('|', 'yellow')} {rows[2]}")
    print(f" {colored('—', 'yellow')}   {colored('—', 'yellow')}   {colored('—', 'yellow')}")
    print(f" {rows[3]} {colored('|', 'yellow')} {rows[4]} {colored('|', 'yellow')} {rows[5]}")
    print(f" {colored('—', 'yellow')}   {colored('—', 'yellow')}   {colored('—', 'yellow')}")
    print(f" {rows[6]} {colored('|', 'yellow')} {rows[7]} {colored('|', 'yellow')} {rows[8]}")


def choose_symbol():
    r = True
    while r:
        symbol_player = input("\rWhich symbol do you want? (X, O): ").upper()
        dict_symbols = assign_symbol(symbol_player)

        if dict_symbols == None:
            print(colored("\rInvalid input...", "red"), end="")
            time.sleep(2)
        else:
            r = False
            game(dict_symbols)


def main():
    print(colored("""
      _____________________________  
    ((                             ))
     )) Welcome to TikTakToe game (( 
    ((                             ))
      -----------------------------  """, "blue"))
          
    print(colored("\n• If you want exit in any moment, press [ctrl+c], it will exit you from the program. \n  (You should don't care of the message that it will display to you)", "red"))

    input("\nPress Enter to continue...")
    subprocess.run('clear', shell=True)
    choose_symbol()


if __name__ == "__main__":
    main()


# Check if nobody has win