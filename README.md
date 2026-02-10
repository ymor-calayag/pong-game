# Pong Game

This project recreates the iconic Pong game with simple controls, ball physics, and score tracking. Players use the keyboard to move paddles vertically, and the ball bounces off paddles and walls with changing angles.

**Technologies Used**

+ ```Python```
+ ```turtle``` module for graphics and animation
+ Object-Oriented Programming (OOP)
+ Basic game physics (collision detection and velocity adjustment)

**Features**

+ Two-player paddle control (arrow keys and W/S keys)
+ Ball movement with bounce off paddles and screen edges
+ Dynamic ball vertical speed adjustment based on paddle hit position
+ Scoreboard for each player displayed on screen
+ Game-over screen declaring the winner

**What Users Can Do**

+ Control the right paddle using arrow keys (Up/Down)
+ Control the left paddle using W (up) and S (down) keys
+ Hit the ball and sink it onto the other players side to score points
+ Race to 10 points to win the game

**The Process / How It’s Built**

+ The game window is created using the ```Turtle``` ```Screen```.
+ Defined Paddle, Ball, and Score classes to encapsulate functionality.
+ Used event listeners for keyboard inputs to move paddles.
+ Implemented a game loop that updates positions, checks for collisions, updates scores, and determines game over.
+ Calculated bounce offsets to make ball movement more dynamic.
