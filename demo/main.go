package main

import (
	"fmt"
	"maps"
	"math/rand"
	"os"
	"slices"
)

type Move struct {
	value int
	Name  string
}

var options = map[string]Move{
	"a":  {1, "Attack"},
	"b":  {2, "Block"},
	"g":  {4, "Grab"},
	"dp": {8, "Dragon Punch"},
}

const humanPlayer = false

func main() {
	p1block := 3
	p2block := 3
	p1hasAttack := false
	p2hasAttack := false
	p1lose := false
	p2lose := false

	for {
		fmt.Printf("p1 : b%d a%t ; p2 : b%d a%t\n", p1block, p1hasAttack, p2block, p2hasAttack)

		fmt.Print("Player 1 action: ")
		var move1 Move

		input1 := ""
		ok1 := false
		for !ok1 {
			fmt.Scan(&input1)
			move1, ok1 = options[input1]
			if p1block == 0 && move1 == options["g"] {
				ok1 = false
			}
		}

		fmt.Print("Player 2 action: ")
		var move2 Move

		if humanPlayer {
			input2 := ""
			ok2 := false
			for !ok2 {
				fmt.Scan(&input2)
				move2, ok2 = options[input2]
				if p2block == 0 && move2 == options["g"] {
					ok2 = false
				}
			}
		} else {
			move2 = slices.Collect(maps.Values(options))[rand.Intn(len(options))]
			fmt.Println(move2.Name)
		}

		p1hitAttack := false
		p2hitAttack := false
		switch move1.value - move2.value {
		case 0:
			fmt.Println("equal")
		case 1:
			p1block--
		case -1:
			p2block--
		case 2:
			p2lose = true
		case -2:
			p1lose = true
		case 3:
			if p2hasAttack {
				p1lose = true
			}
			p2hitAttack = true
		case -3:
			if p1hasAttack {
				p2lose = true
			}
			p1hitAttack = true
		case -6:
			p2lose = true
		case 6:
			p1lose = true
		default:
			if move1.value > move2.value {
				p2lose = true
			} else {
				p1lose = true
			}
		}

		p1hasAttack = p1hitAttack
		p2hasAttack = p2hitAttack

		if p1lose {
			fmt.Println("player 2 win")
			os.Exit(0)
		}

		if p2lose {
			fmt.Println("player 1 win")
			os.Exit(0)
		}
	}
}
