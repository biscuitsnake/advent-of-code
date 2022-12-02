package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("02.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var part1 int
	var part2 int
	for scanner.Scan() {
		p := []rune(scanner.Text())
		a := int(p[0]) - int('A')
		b := int(p[2]) - int('X')
		part1 += ((b + 1 - a + 3) % 3) * 3 // + 3 because modulus of -ve by +ve returns -ve ???
		part1 += b + 1
		part2 += b * 3
		part2 += ((b + 2 + a) % 3) + 1
	}

	fmt.Println(part1)
	fmt.Println(part2)
}
