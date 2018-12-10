package main

import(
	"adventOfCode"
	"fmt"
	"time"
	"os"
)

func main() {
	dayToRun := os.Args[1]
	fmt.Printf("Running Advent of Code Day %s\n", dayToRun)
	start := time.Now()
	switch dayToRun {
	case "1":
		adventOfCode.Day1("./input/day1.txt")
	case "2":
		adventOfCode.Day2("./input/day2.txt")
	case "3":
		adventOfCode.Day3("./input/day3.txt")
	case "4":
		adventOfCode.Day4("./input/day4.txt")
	default:
		fmt.Println("I don't have a solution for that day")
	}
	total := time.Since(start)
	fmt.Printf("Day %s Took %s\n", dayToRun, total)
}