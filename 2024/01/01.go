package main

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func count(element int, slice []int) int {
	total := 0
	for _, v := range slice {
		if v == element {
			total++
		}
	}
	return total
}

func distance(left, right []int) int {
	total := 0
	for i := range left {
		diff := left[i] - right[i]
		if diff < 0 {
			diff = -diff
		}
		total += diff
	}

	return total
}

func similarity(left, right []int) int {
	total := 0
	for _, v := range left {
		total += count(v, right) * v
	}

	return total
}

func main() {
	f, err := os.Open("01.txt")
	check(err)
	defer f.Close()

	var left, right []int

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		numbers := strings.Fields(scanner.Text())

		l, err := strconv.Atoi(numbers[0])
		check(err)
		r, err := strconv.Atoi(numbers[1])
		check(err)

		left = append(left, l)
		right = append(right, r)
	}

	slices.Sort(left)
	slices.Sort(right)

	fmt.Println(distance(left, right))
	fmt.Println(similarity(left, right))
}
