package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Position struct {
	row int
	col int
}

func main() {
	f, err := os.Open("06.txt")
	check(err)
	defer f.Close()

	lab := make(map[Position]string)
	scanner := bufio.NewScanner(f)
	var current_position Position
	r := 0
	for scanner.Scan() {
		columns := strings.Split(scanner.Text(), "")
		for c, item := range columns {
			lab[Position{r, c}] = item
			if item == "^" {
				current_position = Position{r, c}
			}
		}
		r++
	}

	directions := []Position{
		{-1, 0}, // North
		{0, 1},  // East
		{1, 0},  // South
		{0, -1}, // West
	}
	current_direction_index := 0
	current_direction := directions[0]

	turn := func() {
		current_direction_index = (current_direction_index + 1) % len(directions)
		current_direction = directions[current_direction_index]
	}

	patrol := true
	for patrol {
		lab[current_position] = "X"

		var next_position Position
		next_position.row = current_position.row + current_direction.row
		next_position.col = current_position.col + current_direction.col

		if _, ok := lab[next_position]; !ok {
			patrol = false // Stop
		}

		if lab[next_position] == "#" {
			turn()
		} else {
			current_position = next_position
		}
	}

	visited := 0
	visited_positions := []Position{}
	for key, value := range lab {
		if value == "X" {
			visited++
			visited_positions = append(visited_positions, key)
		}
	}
	fmt.Println(visited)
	fmt.Println(visited_positions)
}

// Part 2: Store direction history, loop happens when revisiting the same location whilst going in the same previously-seen direction
