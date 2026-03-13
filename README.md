# SnakeGame
A simple Snake Game implemented using **Python** and **Brython**, rendered in the browser using **HTML5 Canvas**.
## Tech Used
- Python
- Brython
- HTML Canvas
- collections.deque
- random module
## Implementation
- The snake body is stored using **deque** for efficient head insertion and tail removal.
- A **set** is used for fast collision detection with the snake body.
- Food is generated randomly on the grid.
- The game runs using a timer-based loop that updates movement and rendering.
## Run
Open `index.html` in a browser.
## Controls
Arrow keys to move the snake.
