package adventofcode2019

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

//Day2 - Run day 2 of advent of code https://adventofcode.com/2019/day/1
func Day2(filename string) {
	fmt.Printf("Advent of Code Day 1\n")
	file, _ := os.Open(filename)
	var baseProgram []int 
	scanner := bufio.NewScanner(file)
	var programString string
	for scanner.Scan() {
		programString = scanner.Text()
	}
	stringProgram := strings.SplitN(programString, ",", -1)
	for _, strnum := range stringProgram {
		newint, _ := strconv.Atoi(strnum)
		baseProgram = append(baseProgram, newint)
	}
	part1Program := append(baseProgram[:0:0], baseProgram...)
	part1Program[1] = 12
	part1Program[2] = 2
	step := 4
	pos := 0
	for step > 0 {
		step = executeCommand(pos, &part1Program)
		pos = pos + step
	}
	fmt.Printf("Part 1 value: %d\n", part1Program[0])

	for i := 0; i<= 99; i++ {
		for j := 0; j<= 99; j++ {
			part2Program := append(baseProgram[:0:0], baseProgram...)
			part2Program[1] = i
			part2Program[2] = j
			step := 4
			pos := 0
			for step > 0 {
				step = executeCommand(pos, &part2Program)
				pos = pos + step
			}
			if part2Program[0] == 19690720 {
				fmt.Printf("Part 2 Inputs %d - %d\n", i, j)
				i = 100
				j = 100
			}
		}
	}

}

func executeCommand(pos int, program *[]int) int {
	switch (*program)[pos] {
	case 1:
		val1 := (*program)[(*program)[pos+1]]
		val2 := (*program)[(*program)[pos+2]]
		loc := (*program)[pos+3]
		(*program)[loc] = val1 + val2
		return 4
	case 2:
		val1 := (*program)[(*program)[pos+1]]
		val2 := (*program)[(*program)[pos+2]]
		loc := (*program)[pos+3]
		(*program)[loc] = val1 * val2
		return 4
	case 99:
		return 0
	default:
		fmt.Printf("This should not be reached\n")
		return 0
	}
}