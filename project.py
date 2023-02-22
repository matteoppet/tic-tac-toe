import time
from termcolor import colored
import subprocess
import random

import pygame
from pygame import mixer 
from time import sleep

import os


# Clear command for clean the terminal
if os.name == "nt":
    clear_command = "cls"
else:
    clear_command = "clear"


class Sounds:
    try:
        mixer.init()

        @staticmethod
        def opening():
            openingSound = mixer.Sound("audio/opening.wav")
            mixer.Sound.play(openingSound)
            sleep(2)
            mixer.music.stop()

        @staticmethod
        def game_over():
            gameOver = mixer.Sound("audio/game_over.wav")
            mixer.Sound.play(gameOver)
            sleep(2)
            mixer.music.stop()

        @staticmethod
        def win():
            win = mixer.Sound("audio/win.wav")
            mixer.Sound.play(win)
            sleep(2)
            mixer.music.stop()

        @staticmethod
        def typing():
            typing = mixer.Sound("audio/typing.wav")
            mixer.Sound.play(typing)

    except pygame.error:
        pass


class Player:
    def __init__(self, symbols, available_movements, rows):
        self.symbols = symbols
        self.available_movements = available_movements
        self.rows = rows

    def movement(self):
        self.r = True

        print()
        print()

        while self.r:
            try:
                self.number = int(input("\rYour turn -> "))

                if self.number in self.rows:
                    self.available_movements.remove(self.number)
                    position = self.rows.index(self.number)
                    self.rows[position] = self.symbols["Player"]

                    return board(self.rows, self.symbols)

                else:
                    print(colored("\rInvalid input...", "red"), end="")
                    time.sleep(2)

            except ValueError:
                print(colored("\rInvalid input...", "red"), end="")
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
            pass

        if random_movement in self.rows:
            self.available_movements.remove(random_movement)

            position = self.rows.index(random_movement)
            self.rows[position] = self.symbol_bot

            string = f"Computer move: position {random_movement}"

            return string 


def game(dict_symbols):
    rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    available_movements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    last_movement = ""

    first_move = random.choice(['X', 'O'])

    board(rows, dict_symbols)
    print(f"\n> Your symbol: {colored(dict_symbols['Player'], 'green')}")
    print(f"> Bot's symbol: {colored(dict_symbols['Bot'], 'red')}")
    print(first_move_information(first_move, dict_symbols))

    input("\nPress Enter to continue...")

    last_movement = check_first_move(first_move, dict_symbols, available_movements, rows)
    
    r = True
    while r:
        check_tris_bot = check_tris(dict_symbols["Bot"], rows, dict_symbols)
        check_tris_player = check_tris(dict_symbols["Player"], rows, dict_symbols)
        
        if check_tris_bot == None and check_tris_player == None:

            if last_movement == dict_symbols["Player"]:
                text_movement = Bot(dict_symbols["Bot"], available_movements, rows).movement()
                check_tris(dict_symbols["Bot"], rows, dict_symbols)
                last_movement = dict_symbols["Bot"]

                board(rows, dict_symbols)
                movement_bot_message(text_movement)

            else:
                Player(dict_symbols, available_movements, rows).movement()
                check_tris(dict_symbols["Player"], rows, dict_symbols)
                last_movement = dict_symbols["Player"]

                board(rows, dict_symbols)

        else:
            if check_tris_bot != None:
                r = False
                message, symbol = check_tris_bot.split(":")
                print(f"{message}:{colored(symbol, 'red')}")
                print()

                try:
                    Sounds.game_over()
                except AttributeError:
                    pass


                input("Press Enter to restart...")

                subprocess.run(f'{clear_command}', shell=True)
                choose_symbol()

            if check_tris_player != None:
                r = False
                message, symbol = check_tris_player.split(":")
                print(f"{message}:{colored(symbol, 'green')}")
                print()

                try:
                    Sounds.win()
                except AttributeError:
                    pass

                input("Press Enter to restart...")

                subprocess.run(f'{clear_command}', shell=True)
                
                choose_symbol()

            if available_movements == []:
                print("\nNo winners this time! Try Again...")

                input("\nPress Enter to restart...")
                subprocess.run(f'{clear_command}', shell=True)
                choose_symbol()


def first_move_information(first_move, dict_symbols):
    if first_move == dict_symbols["Player"]:
            return f"> First move by: {colored(dict_symbols['Player'], 'green')}"
    else:
        return f"> First move by: {colored(dict_symbols['Bot'], 'red')}"


def check_first_move(first_move, dict_symbols, available_movements, rows):
    if first_move == dict_symbols["Bot"]:
        text_movement = Bot(dict_symbols["Bot"], available_movements, rows).movement()
        board(rows, dict_symbols)
        movement_bot_message(text_movement)

        return dict_symbols["Bot"]

    else:
        Player(dict_symbols, available_movements, rows).movement()
        return dict_symbols["Player"]


def movement_bot_message(text_movement):
    print()

    text_movement_update = ""

    try:
        Sounds.typing()
    except AttributeError:
        pass

    for i in text_movement:
        text_movement_update = text_movement_update + i
        print(f"\r{text_movement_update}", end="")
        time.sleep(0.05)


def check_tris(symbol, rows, dict_symbols):

    if symbol == dict_symbols["Player"]:
        symbol = f'\x1b[32m{symbol}\x1b[0m'
    else:
        symbol = f'\x1b[31m{symbol}\x1b[0m'
    
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


def board(rows, dict_symbols):
    subprocess.run(f'{clear_command}', shell=True)

    for i in rows:
        if i == dict_symbols["Player"]:
            position = rows.index(i)
            rows[position] = colored(dict_symbols["Player"], "green")
        if i == dict_symbols["Bot"]:
            position = rows.index(i)
            rows[position] = colored(dict_symbols["Bot"], "red")


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
    subprocess.run(f'{clear_command}', shell=True)

    print(colored("""
      _____________________________  
    ((                             ))
     )) Welcome to TikTakToe game (( 
    ((                             ))
      -----------------------------  """, "blue"))
          
    print(colored("\n• To exit, press [ctrl+c]", "red"))

    try:
        Sounds.opening()
    except AttributeError:
        pass

    input("\nPress Enter to continue...")

    subprocess.run(f'{clear_command}', shell=True)
    choose_symbol()


if __name__ == "__main__":
    main()