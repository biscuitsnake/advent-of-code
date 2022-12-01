package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func sum(array []int) int {
	result := 0
	for _, item := range array {
		result += item
	}
	return result
}

func count() []int {
	file, err := os.Open("01.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var calories []int
	var sum int
	for scanner.Scan() {
		l := scanner.Text()
		if l == "" {
			calories = append(calories, sum)
			sum = 0
		} else {
			i, err := strconv.Atoi(l)
			if err != nil {
				log.Fatal(err)
			}
			sum += i
		}
	}
	sort.Ints(calories)
	return calories

}

func main() {
	calories := count()
	fmt.Println(calories[len(calories)-1])
	fmt.Println(sum(calories[len(calories)-3:]))
}
