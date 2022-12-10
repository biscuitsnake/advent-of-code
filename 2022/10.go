package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func incrementCycle(cycle int, X int, strength int, n int) (int, int, int) {
	cycle++
	if cycle == n {
		strength += cycle * X
		n += 40
	}
	return cycle, strength, n
}

func drawPixel(cycle int, X int) string {
	pos := (cycle - 1) % 40
	if (pos == X-1) || (pos == X) || (pos == X+1) {
		return "#"
	} else {
		return "."
	}
}

func main() {
	file, err := os.Open("10.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var pixels []string
	cycle, X, strength, n := 1, 1, 0, 20
	scanner := bufio.NewScanner(file)
	pixels = append(pixels, drawPixel(cycle, X))
	for scanner.Scan() {
		inst := strings.Split(scanner.Text(), " ")
		cycle, strength, n = incrementCycle(cycle, X, strength, n)
		pixels = append(pixels, drawPixel(cycle, X))
		if inst[0] == "addx" {
			value, err := strconv.Atoi(inst[1])
			if err != nil {
				log.Fatal(err)
			}
			X += value
			cycle, strength, n = incrementCycle(cycle, X, strength, n)
			pixels = append(pixels, drawPixel(cycle, X))
		}
	}
	fmt.Println(strength)
	for i := 0; i <= 200; i += 40 {
		fmt.Println(pixels[i : i+40])
	}
}
