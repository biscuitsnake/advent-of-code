package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Stack []string

func (s *Stack) IsEmpty() bool {
	return len(*s) == 0
}

func (s *Stack) Peek() string {
	if s.IsEmpty() {
		return ""
	} else {
		return (*s)[len(*s)-1]
	}
}

func (s *Stack) Push(str string) {
	if !(str == "") {
		*s = append(*s, str)
	}
}

func (s *Stack) Pop() (string, bool) {
	if s.IsEmpty() {
		return "", false
	} else {
		ind := len(*s) - 1
		element := (*s)[ind]
		*s = (*s)[:ind]
		return element, true
	}
}

func main() {
	stacks1 := make([]Stack, 10) // Stack number in input corresponds to slice index (stacks[0] is empty)
	stacks2 := make([]Stack, 10)

	stacks1[1] = []string{"Z", "J", "G"}
	stacks1[2] = []string{"Q", "L", "R", "P", "W", "F", "V", "C"}
	stacks1[3] = []string{"F", "P", "M", "C", "L", "G", "R"}
	stacks1[4] = []string{"L", "F", "B", "W", "P", "H", "M"}
	stacks1[5] = []string{"G", "C", "F", "S", "V", "Q"}
	stacks1[6] = []string{"W", "H", "J", "Z", "M", "Q", "T", "L"}
	stacks1[7] = []string{"H", "F", "S", "B", "V"}
	stacks1[8] = []string{"F", "J", "Z", "S"}
	stacks1[9] = []string{"M", "C", "D", "P", "F", "H", "B", "T"}

	copy(stacks2, stacks1)

	file, err := os.Open("05.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		var no, from, to int
		fmt.Sscanf(scanner.Text(), "move %d from %d to %d", &no, &from, &to)

		var temp []string
		for i := no; i > 0; i-- {
			o, _ := stacks1[from].Pop()
			stacks1[to].Push(o)
			p, _ := stacks2[from].Pop()
			temp = append(temp, p)
		}

		for i := len(temp) - 1; i >= 0; i-- {
			stacks2[to].Push(temp[i])
		}
	}

	var part1 strings.Builder
	var part2 strings.Builder

	for i := 1; i <= 9; i++ {
		part1.WriteString(stacks1[i].Peek())
		part2.WriteString(stacks2[i].Peek())
	}

	fmt.Println(part1.String())
	fmt.Println(part2.String())
}
