# Game ideas

Below are initial ideas for the game - based off a game I made with Scratch almost 10 years ago.

These are pre-development notes and are subject to significant change.

### Player

- Player plays as a purple dot, which is controllable via keyboard (and possibly controller?).
- The player must avoid contact with any enemies or projectiles.
- Using arrow keys or WASD, the player can move up, down, left, right.
- If a key is pressed, the player's sprite increases speed in that direction (until reaching a maximum speed).
- If a key is released, the speed in that corresponding direction is gradually reduced (player decelerates).
- If two adjacent direction keys are pressed (e.g. up and left), the speed is limited using Pythagoras' Theorem so that it remains the same as if only one key were pressed.

### Enemy

- The enemies in the game are red dots.
- The enemy moves towards the players' position, a random amount of times (between 4-8).
- The enemy then chooses one of the following attacks:
    - The enemy will move to a location near the centre of the screen, and spit out small projectiles in a spiral pattern.
    - The enemy will create 1-2 significantly larger versions of itself which will move around the screen aimlessly before shrinking to zero size.
    - The enemy will launch 1-3 homing projectiles which more closely follow the player before detonating.
    - The enemy will create 3-6 duplicates of itself and spread them to random locations on the screen, which will then wait before moving towards the player's location.
- The enemy will increase slightly in size after its attack.
- When the enemy sprite's area is double that of its original value, it will split into two enemies which follow the same behaviour as above, increasing difficulty.