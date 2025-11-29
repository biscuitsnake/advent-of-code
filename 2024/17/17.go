package main

import "fmt"

var A, B, C int

func main() {
	program := []int{2, 4, 1, 7, 7, 5, 4, 1, 1, 4, 5, 5, 0, 3, 3, 0}
	A, B, C = 53437164, 0, 0

	var output []int

	var ptr int
	for ptr < len(program) {
		opcode := program[ptr]
		operand := program[ptr+1]

		switch opcode {
		case 0: // adv
			A = A / power(2, combo(operand))
		case 1:
			B = B ^ operand
		case 2:
			B = combo(operand) % 8
		case 3:
			if A != 0 {
				ptr = operand
				continue
			}
		case 4:
			B = B ^ C
		case 5:
			output = append(output, combo(operand)%8)
		case 6:
			B = A / power(2, combo(operand))
		case 7:
			C = A / power(2, combo(operand))
		}

		ptr += 2
	}

	fmt.Println(output)
}

func power(x int, y int) int {
	result := 1
	for i := 0; i < y; i++ {
		result *= x
	}
	return result
}

func combo(operand int) int {
	switch operand {
	case 4:
		return A
	case 5:
		return B
	case 6:
		return C
	default:
		return operand
	}
}
