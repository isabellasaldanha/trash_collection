# Trash Collection Game

## Description

Trash Collection Game is a simple Pygame-based game where the player controls a trash bin to collect falling trash items. The goal is to collect as much trash as possible while avoiding letting any fall off the screen. The game ends if three pieces of trash are lost.

## Features

- **Player Control**: Move the trash bin left and right using arrow keys.
- **Trash Generation**: Trash items fall from the top of the screen and increase in speed over time.
- **Score Tracking**: Collecting trash increases the score.
- **Game Over**: The game ends if three pieces of trash are lost.
- **Sound Effects**: Sound effects for collecting trash and game over events.
- **Score and Lost Trash Display**: Display score and lost trash count on the screen.

## Running the Game

Run the game by executing the following command:
```bash
python main.py
```
## Folder Structure

```
.
├── assets
│   ├── background.png       # Background image for the game
│   ├── bin.png              # Image for the player's trash bin
│   ├── trash.png            # Image for the trash items
│   ├── collect.wav          # Sound effect for collecting trash
│   ├── game_over.wav        # Sound effect for game over
│   └── comic.ttf            # Font file for displaying text
├── README.md                # This file
└── main.py                  # Main Python script to run the game
```

## How to Play

- Use the left and right arrow keys to move the trash bin.
- Collect falling trash to increase your score.
- Avoid letting trash fall off the screen; losing three pieces will end the game.
- Press any key to restart after the game is over.

## Code Structure

- **Initialization**:
  - Initializes Pygame, screen dimensions, and loads assets.
- **Player Class**:
  - Handles player movement and screen boundaries.
- **Trash Class**:
  - Handles trash falling and removing off-screen trash.
- **Game Loop**:
  - Updates game state, checks for collisions, and handles drawing.

