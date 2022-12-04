package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func Split(r rune) bool {
	return r == '-' || r == ','
}

func main() {
	file, err := os.Open("04.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	var part1 int
	var part2 int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.FieldsFunc(scanner.Text(), Split)
		var s []int
		for _, i := range line {
			x, err := strconv.Atoi(i) // ha
			if err != nil {
				log.Fatal(err)
			}
			s = append(s, x)
		}
		if (s[0] <= s[2]) && (s[1] >= s[3]) || (s[2] <= s[0]) && (s[3] >= s[1]) {
			part1 += 1
		}
		if !(s[1] < s[2] || s[0] > s[3]) {
			part2 += 1
		}
	}
	fmt.Println(part1)
	fmt.Println(part2)
}
