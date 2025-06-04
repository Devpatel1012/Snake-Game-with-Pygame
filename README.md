# 🐍 Snakes with Dev 🎮

## A Classic Snake Game Built with Pygame

---

### Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Screenshot](#screenshot)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

### About The Project

"Snakes with Dev" is a simple yet engaging implementation of the timeless Snake game, developed using the Pygame library in Python. This project serves as a foundational exercise in game development, demonstrating concepts like game loops, event handling, collision detection, and score management.

The objective is classic: control the snake, eat the red food squares to grow, and avoid colliding with the boundaries or your own tail. The game keeps track of your current score and a persistent high score, adding a competitive element.

This project was built to:
* Solidify understanding of Pygame fundamentals.
* Practice game loop mechanics and state management.
* Implement basic collision detection.
* Handle user input for game control.
* Manage persistent data (high score) using file I/O.

---

### Features

* **Classic Snake Gameplay:** Grow your snake by eating food.
* **Dynamic Scoring:** Score increases with each food consumed.
* **Persistent High Score:** Your highest score is saved and displayed across game sessions.
* **Boundary and Self-Collision Detection:** Game over when hitting walls or your own body.
* **Restart Option:** Easily restart the game after a "Game Over."
* **Simple and Clean UI:** Focus on core gameplay mechanics.

---

### Screenshot

Catch a glimpse of the game in action!

![Snakes with Dev Gameplay](![image](https://github.com/user-attachments/assets/18742dad-cfa2-4b01-9ee0-8f1cd3d09a02)
)
*Current Score: 90, Highscore: 100*

---

### Getting Started

To get a local copy up and running, follow these simple steps.

#### Prerequisites

Make sure you have Python installed on your system. This project was developed with **Python 3.x**.

* [Python 3.x](https://www.python.org/downloads/)
* `pip` (Python package installer)

#### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/snakes-with-dev.git](https://github.com/your-username/snakes-with-dev.git)
    cd snakes-with-dev
    ```
    (Remember to replace `your-username` with your actual GitHub username and `snakes-with-dev` with the actual repository name you choose.)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(If you haven't created `requirements.txt` yet, run `pip freeze > requirements.txt` before this step. You'll need `pygame` installed to do that: `pip install pygame`)*

---

### How to Play

1.  **Run the game:**
    ```bash
    python devgame.py
    ```
    (Assuming your main game file is `devgame.py` as seen in the screenshot.)

2.  **Controls:**
    * `Right Arrow` Key: Move Right
    * `Left Arrow` Key: Move Left
    * `Up Arrow` Key: Move Up
    * `Down Arrow` Key: Move Down

3.  **Objective:**
    * Guide the black snake to eat the red food (squares).
    * Each food eaten increases your score and the snake's length.!
    * Avoid hitting the screen boundaries or the snake's own body.
    * Press `Enter` after "Game Over!" to restart.

---


