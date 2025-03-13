# Specification

Adversarial turn-based game inspired by the fighting game Footsies.

## Basic rules

A round happens in successive turns, where each of the players select an option. How the options interact determines whether the game continues for another turn, or ends with one of the players winning. Playing the game can happen over multiple rounds or a single one.

## Actions

There are four possible options available at the start of the game : 
- Attack
- Block
- Grab
- Dragon Punch

Block is limited to three uses per round against Attacks, as will be covered in the next section.

## Interaction

Interaction can be summarized by this chart:
![Interaction between possible actions](spec.drawio.png)

Attack wins only against Grabs, and if a player lands two attacks in succession, they win. If the opponent Blocks, the game continues and one use of Block is deducted from them. If the opponent Dragon Punches, the player loses.

Block completely stops both Attacks and Dragon Punches. If the opponent Attacks, the game continues, and one use is consumed, out of three per round. If the opponent Dragon Punches, the player counters it and wins. If the opponent grabs, the player loses.

Grab wins only against Block, and will instantly grant a win. As mentioned earlier, Grabs lose to attacks, and if hit twice, the player loses.

Finally, Dragon Punches are special attacks that win instantly against Attacks and Grabs, and lose instantly to Blocks.

# Implementation

In this repo is a simple implementation of the game in Go, which can be toggled to be against a real opponent for testing, or against a random opponent.

Any recent version of go should be able to run the code, as no dependencies are involved. Go version 1.24 or above is recommended.

To run the game, simply use the command : 
```sh
go run .
```