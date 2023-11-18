package main

import (
	"fmt"
	"strconv"
	"strings"
	"math"
)

func readInt() int {
	var input string
	fmt.Scanln(&input)
	number, _ := strconv.Atoi(input)
	return number
}
func input() string {
	var input string
	fmt.Scanln(&input)
	return input
}

func print(args ...interface{}) {
	fmt.Print(args...)
}

func readIntList(prompt string) []int {
	fmt.Print(prompt)
	var input string
	fmt.Scanln(&input)

	parts := strings.Fields(input)
	numbers := make([]int, len(parts))

	for i, part := range parts {
		num, _ := strconv.Atoi(part)
		numbers[i] = num
	}

	return numbers
}

func main() {
	a := readInt()
	b := readInt()
	c := readInt()
	
}
