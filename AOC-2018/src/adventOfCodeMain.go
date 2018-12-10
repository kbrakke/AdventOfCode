package main

import(
	"adventOfCode"
	"fmt"
	"time"
)

func main() {
	fmt.Printf("Running Advent of Code Answers\n")
	day1Start := time.Now()
	adventOfCode.Day1("./input/day1.txt")
	day1Total := time.Since(day1Start)
	fmt.Printf("Day 1 Took %s\n", day1Total)
	
	day2Start := time.Now()
	adventOfCode.Day2("./input/day2.txt")
	day2Total := time.Since(day2Start)
	fmt.Printf("Day 2 Took %s\n", day2Total)
	
	day3Start := time.Now()
	adventOfCode.Day3("./input/day3.txt")
	day3Total := time.Since(day3Start)
	fmt.Printf("Day 3 Took %s\n", day3Total)
}