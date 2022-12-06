package main

import (
	"fmt"
	"log"
	"os"
)

func find(s string, l int) int {
	for i := l; i <= len(s); i++ {
		m := make(map[rune]bool)
		for _, j := range s[i-l : i] {
			m[j] = true
		}
		if len(m) == l {
			return i
		}
	}
	return -1
}

func main() {
	//var u int
	input, err := os.ReadFile("06.txt")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(find(string(input), 4))
	fmt.Println(find(string(input), 14))
}
