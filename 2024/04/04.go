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

func outside(wordsearch [][]string, i, j int) bool {
	return i < 0 || i >= len(wordsearch) || j < 0 || j >= len(wordsearch[0])
}

func xmas(wordsearch [][]string, i, j int) int {
	dirs := [][]int{{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}}

	yes := 0
	for _, dir := range dirs {
		var word []string

		for idx := range 4 {
			a := i + dir[0]*idx
			b := j + dir[1]*idx

			if outside(wordsearch, a, b) {
				continue
			}
			word = append(word, wordsearch[a][b])
		}

		if strings.Join(word, "") == "XMAS" {
			yes++
		}
	}
	return yes
}

func mas(wordsearch [][]string, i, j int) bool {
	if wordsearch[i][j] != "A" {
		return false
	}

	// don't waste your time trying to improve this.

	ne := [2]int{i - 1, j - 1}
	sw := [2]int{i + 1, j + 1}
	primary := !outside(wordsearch, ne[0], ne[1]) && !outside(wordsearch, sw[0], sw[1]) &&
		((wordsearch[ne[0]][ne[1]] == "M" && wordsearch[sw[0]][sw[1]] == "S") ||
			(wordsearch[ne[0]][ne[1]] == "S" && wordsearch[sw[0]][sw[1]] == "M"))

	nw := [2]int{i - 1, j + 1}
	se := [2]int{i + 1, j - 1}
	secondary := !outside(wordsearch, nw[0], nw[1]) && !outside(wordsearch, se[0], se[1]) &&
		((wordsearch[nw[0]][nw[1]] == "M" && wordsearch[se[0]][se[1]] == "S") ||
			(wordsearch[nw[0]][nw[1]] == "S" && wordsearch[se[0]][se[1]] == "M"))

	return primary && secondary
}

func main() {
	f, err := os.Open("04.txt")
	check(err)
	defer f.Close()

	scanner := bufio.NewScanner(f)
	var wordsearch [][]string
	for scanner.Scan() {
		wordsearch = append(wordsearch, strings.Split(scanner.Text(), ""))
	}

	part1 := 0
	part2 := 0
	for i, row := range wordsearch {
		for j := range row {
			part1 += xmas(wordsearch, i, j)
			if mas(wordsearch, i, j) {
				part2++
			}
		}
	}

	fmt.Println(part1)
	fmt.Println(part2)
}
