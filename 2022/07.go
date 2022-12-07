package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func part1(scanner *bufio.Scanner) (int, int) {
	dirs := make(map[string]int)
	var pwd []string
	for scanner.Scan() {
		l := strings.Split(scanner.Text(), " ")

		if l[0] == "$" {
			if l[1] == "cd" {
				if l[2] == ".." {
					pwd = pwd[:len(pwd)-1]
				} else {
					pwd = append(pwd, l[2])
				}
			}
		} else if l[0] != "dir" {
			size, err := strconv.Atoi(l[0])
			if err != nil {
				log.Fatal(err)
			}
			for i := 0; i < len(pwd); i++ {
				dirs[strings.Join(pwd[:i+1], "/")] += size
			}
		}
	}

	min := 30000000 - (70000000 - dirs["/"])
	smallest := 30000000
	var part1 int
	for _, val := range dirs {
		if val < 100000 {
			part1 += val
		}
		if val >= min && val < smallest {
			smallest = val
		}
	}

	return part1, smallest
}

func main() {
	file, err := os.Open("07.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	fmt.Println(part1(bufio.NewScanner(file)))
}
