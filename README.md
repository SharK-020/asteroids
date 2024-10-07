# Asteroids

A Python implementation of a classic asteroids-style arcade game. Players control a spaceship and must avoid or shoot down incoming asteroids while navigating in space.

## Features
- **Asteroid Field**: Randomly generated asteroid fields.
- **Player Control**: Spaceship with full navigation capabilities.
- **Shooting Mechanism**: Players can shoot to destroy asteroids.
- **Collision Detection**: Functional collision between the spaceship, asteroids, and shots.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SharK-020/asteroids.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```
2. Use arrow keys to control the spaceship.
3. Press the spacebar to shoot.
4. Avoid or destroy the asteroids!

## Files Overview

- **`main.py`**: The main script to start the game.
- **`asteroid.py`**: Defines the asteroid behavior.
- **`player.py`**: Controls the player's spaceship.
- **`shot.py`**: Handles shooting mechanics.
- **`asteroidfield.py`**: Manages the generation and movement of the asteroid field.
- **`circleshape.py`**: Utility to represent circular objects in the game.
- **`constants.py`**: Contains game-related constants.

## Requirements

- Python 3.x
- Pygame

## License

This project is licensed under the MIT License.
