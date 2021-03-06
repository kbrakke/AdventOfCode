package adventofcode

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//Day1 - Run day 1 of advent of code https://adventofcode.com/2018/day/1
func Day1(filename string) {
	fmt.Printf("Advent of Code Day 1\n")
	file, _ := os.Open(filename)
	frequencyChanges := make([]int, 0)
	var matchedFrequency = false
	reachedFrequencies := make(map[int]int)
	sum := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineInt, _ := strconv.Atoi(scanner.Text())
		frequencyChanges = append(frequencyChanges, lineInt)
		sum = sum + lineInt
		if reachedFrequencies[sum] > 0 {
			matchedFrequency = true
			fmt.Printf("Matched Frequency %d\n", sum)
		} else {
			reachedFrequencies[sum] = 1
		}
	}
	fmt.Printf("Final frequency %d\n", sum)
	for !matchedFrequency {
		for _, value := range frequencyChanges {
			sum = sum + value
			if reachedFrequencies[sum] == 1 {
				matchedFrequency = true
				fmt.Printf("Matched Frequency %d\n", sum)
				break
			} else {
				reachedFrequencies[sum] = 1
			}
		}
	}
}
