package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	f, err := os.ReadFile("03.txt")
	check(err)
	memory := string(f)

	r, _ := regexp.Compile(`mul\((\d+),(\d+)\)|do\(\)|don't\(\)`)
	found := r.FindAllStringSubmatch(memory, -1)

	enabled := true
	part1, part2 := 0, 0
	for _, f := range found {
		if strings.HasPrefix(f[0], "do()") {
			enabled = true
		} else if strings.HasPrefix(f[0], "don't()") {
			enabled = false
		} else {
			a, _ := strconv.Atoi(f[1])
			b, _ := strconv.Atoi(f[2])
			part1 += (a * b)

			if enabled {
				part2 += (a * b)
			}
		}
	}

	fmt.Println(part1)
	fmt.Println(part2)
}
