# Tik Tak Toe Project

This project was done as a Final Project for CS50P

#### Features:
- CLI Game with auto refresh on terminal
- Single Player game
- <details>
  <summary>Sound effects</summary>
  
  There are some issues with sound effects in different machines, __Sound effects not supported on WSL.__

  - Windows: :white_check_mark:
  
  - WSL: :x:
  
  - Linux: :interrobang: ( Not tested yet ) 
  </details>

#### Description of the game:

> __First step__:  At the beginning of the game, as soon as you start, you will see a welcome page with a exit message in case you want to leave the game at any time. Press enter to start.

> __Second step__:  You have now to select the sign you want to use. Your sign will be green and the computer's sign will be red.

> __Third step__: Then you will see another screen with various information, the board and the symbol that starts first will be choosen randomly ( [random](https://docs.python.org/3/library/random.html) library ).

> __Fourth step__: Now you will play against the computer. Each move will be shoved on the board.

> __Fifth step__: if one of the two wins during the match, it will stop and the winner of the match will be transcribed, while if no one wins, it will be transcribed that no one has won. In both cases you can always re-play by clicking the Enter button.

<details><summary>Description of each function</summary>
<p>

  ##### Classes:
- ```Sounds``` > In this class there are 4 functions ( ```opening()```, ```game_over()```, ```win()```, ```typing``` ) and each of these functions, when called activates a sound effect.
  
- ```Player``` > This class contains everything about the player, and also a function ( ```movement()``` ) that manages the player's movement around the board.
  
- ```Bot``` > This class contains everything about the bot, and inside there is a function ( ```movement()``` ) that manages the movement of the bot around the board.

##### Functions:
- ```game()``` > This function is the main part for the game, in this function there are all the functions that are needed for the game and in addition everything related to the moment of the game is performed
  
- ```first_move_information()``` > This function checks for who moves first and then writes it down as information as soon as you start the game.
  
- ```check_first_move()``` > This function checks for who moves first and based on who moves first, the class is called so as to have its move executed, returning the symbol of who moved.
  
- ```movement_bot_message()``` > This function is called only if it's the bot's turn to move, and is called after the bot makes the move so as to be able to transcribe the position chosen by the bot, accompanied by an animation and a sound effect.
  
- ```check_tris()``` > In this function the whole check is performed if one of the two wins, returning the string with the symbol of the winner, red if it is from the bot or green if the player wins.
  
- ```assign_symbol()``` > This function assigns the symbol to each player, if the player chooses X the bot is assigned O, and vice versa, returning a dictionary with the symbol of the player and the bot.
  
- ```board()``` > This function prints the whole table placing the various symbols chosen in their positions.
 
- ```choose_symbol()``` > This function allows the player to choose the symbol, it will always be the player who chooses the symbol first.
  
- ```main()``` > This function is the first to be called and executed when the program starts, this function prints the welcome message and to start the game just press the Enter key.
  
</p>
</details>

</p>
</details>

## Demo

Video link youtube: ###

[![asciicast](https://asciinema.org/a/1mpvEY3OCAQdQCA1AUBklk0iI.svg)](https://asciinema.org/a/1mpvEY3OCAQdQCA1AUBklk0iI)
<div dir="rtl">
Little demo of the game

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the game

```bash
  python project.py
```


## Running Tests

To run tests, run the following commands

install the module
```bash
  pip install pytest
```

Run the module with the file "test_project.py"
```bash
  pytest test_project.py
```

These are the test functions implemented for now:
> test_assign_symbol()

> test_check_tris()

> test_first_move_information()
