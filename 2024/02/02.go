package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func toInts(numbers []string) []int {
	var result []int
	for _, n := range numbers {
		i, err := strconv.Atoi(n)
		check(err)
		result = append(result, i)
	}
	return result
}

func dampened(numbers []int) [][]int {
	var result [][]int

	for i := 0; i < len(numbers); i++ {
		numscpy := make([]int, len(numbers))
		_ = copy(numscpy, numbers)
		damp := append(numscpy[0:i], numscpy[i+1:len(numbers)]...)
		result = append(result, damp)
	}

	return result
}

func isSafe(numbers []int) bool {
	if len(numbers) == 1 {
		return true
	}

	var inc, dec bool
	for i := 0; i < len(numbers)-1; i++ {
		diff := numbers[i+1] - numbers[i]

		if diff == 0 {
			return false
		}

		if diff > 0 {
			inc = true
		}
		if diff < 0 {
			dec = true
		}

		if !((math.Abs(float64(diff)) >= 1) && (math.Abs(float64(diff)) <= 3)) {
			return false
		}
	}

	if inc && dec {
		return false
	}

	return true
}

func main() {
	f, err := os.Open("02.txt")
	check(err)
	defer f.Close()

	safe := 0
	damp := 0

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		s := strings.Fields(scanner.Text())
		numbers := toInts(s)

		if isSafe(numbers) {
			safe++
		} else {
			for _, d := range dampened(numbers) {
				if isSafe(d) {
					damp++
					break
				}
			}
		}
	}

	fmt.Println(safe)
	fmt.Println(safe + damp)
}
