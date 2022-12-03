package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func readLines(path string) ([]string, error) {
	file, err := os.Open(path)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func part1(lines []string, priorities map[string]int) int {
	var sum int

	for line := 0; line < len(lines); line++ {
		set := make(map[string]int)
		rucksack := strings.Split(lines[line], "")
		first := rucksack[0 : len(rucksack)/2]
		second := rucksack[len(rucksack)/2:]

		for i := 0; i < len(first); i++ {
			set[first[i]] += 1
		}

		var shared string
		for i := 0; i < len(second); i++ {
			if _, ok := set[second[i]]; ok {
				shared = second[i]
			}
		}
		sum += priorities[shared]
	}
	return sum
}

func part2(lines []string, priorities map[string]int) int {
	var sum int

	for line := 0; line < len(lines); line += 3 {
		set1 := make(map[string]int)
		one := strings.Split(lines[line], "")

		for i := 0; i < len(one); i++ {
			set1[one[i]] += 1
		}

		set2 := make(map[string]int)
		two := strings.Split(lines[line+1], "")
		for i := 0; i < len(two); i++ {
			if _, ok := set1[two[i]]; ok {
				set2[two[i]] += 1
			}
		}

		var shared string
		three := strings.Split(lines[line+2], "")
		for i := 0; i < len(three); i++ {
			if _, ok := set2[three[i]]; ok {
				shared = three[i]
			}
		}
		sum += priorities[shared]
	}
	return sum
}

func main() {
	priorities := make(map[string]int)
	p := 1
	for i := 'a'; i <= 'z'; i++ {
		priorities[string(i)] = p
		p++
	}
	for i := 'A'; i <= 'Z'; i++ {
		priorities[string(i)] = p
		p++
	}

	lines, err := readLines("03.txt")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(part1(lines, priorities))
	fmt.Println(part2(lines, priorities))
}
