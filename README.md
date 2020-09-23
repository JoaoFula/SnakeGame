# Snake clone
## Done by: 
[João Fula](joaofula.pythonanywhere.com) ![website logo](https://joaofula.pythonanywhere.com/static/portfolio/logo.png)

This is a project done for **fun** with no profit intention. If you wish to contribute to the project, you may do so, even though an **email** to [hsifula@gmail.com](hsifula@gmail.com) would be nice.
You can find more about the **author** at his [personal website](joaofula.pythonanywhere.com)

## Requirements to run the game
To run the game in its current state it is necessary to have:
> Python3 (Python2 should work but has not been tested)
>
> Pip3
>
> pygame
>
> tkinter

## How to run

The game is ran by typing:
> python3 main.py

## Current state of the game

The game in the current state greets the player with a starting screen with the game **title** and two buttons. One to **play** and one to **quit** the game.
The main menu looks like this:

![Main menu](https://github.com/JoaoFula/SnakeGame/blob/master/main_menu.png "Main menu")

Once the *Play* button is pressed, the game will begin. In green is represented the **snake**, moving at a fixed speed, the static **apple**, in red, and a **grid**.
The game looks like this:

![Game](https://github.com/JoaoFula/SnakeGame/blob/master/game.png "Game")


## Known issues
The are currently **2 bugs** found.

> 1) Within the game, when the snake leaves the screen on every wall and the player presses a direction changing button, while the snake is out of sight. The snake then starts travelling outside the screen.
> 2) In the initial menu, the mouse click is not constantly being read, instead, the game checks its state on every loop. Which means that if the player presses any button fast enough, the function may not read the mouse click. 

## Future plans
* Fix the current known bugs since they are not supposed to be in the game.
* Add a pause menu.
* Add a difficulty option so the player can tone up or down the speed of the snake.
* Add different maps (walls all around, walls spread around the center of the map).
* Create an AI to solve the different difficulties of the game.