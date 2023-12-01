package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

type cube struct {
	x int
	y int
	z int
}

func getAdjacent(c cube) [6]cube {
	adj := [6]cube{
		{x: c.x + 1, y: c.y, z: c.z},
		{x: c.x - 1, y: c.y, z: c.z},
		{x: c.x, y: c.y + 1, z: c.z},
		{x: c.x, y: c.y - 1, z: c.z},
		{x: c.x, y: c.y, z: c.z + 1},
		{x: c.x, y: c.y, z: c.z - 1},
	}
	return adj
}

func main() {
	file, err := os.Open("18.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	cubes := make(map[cube]bool)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var x, y, z int
		_, err := fmt.Sscanf(scanner.Text(), "%d,%d,%d", &x, &y, &z)
		if err != nil {
			log.Fatal(err)
		}
		var c cube = cube{x: x, y: y, z: z}
		cubes[c] = true
	}
	var area int
	for i := range cubes {
		for _, a := range getAdjacent(i) {
			if !cubes[a] {
				area++
			}
		}
	}

	fmt.Println(area)
}
