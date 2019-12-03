package main

import (
	"./adventofcode2019"
	"fmt"
	"os"
	"time"
)

func main() {
	dir, _ := os.Getwd()
	fmt.Printf("Working Directory: %s", dir)
	dayToRun := "0"
	fileName := "default"
	switch len(os.Args) {
	case 1:
		fmt.Println("usage adventOfCodeMain <day> [test?]")
		os.Exit(1)
	case 2:
		dayToRun = os.Args[1]
		fileName = fmt.Sprintf("./input/day%s.txt", dayToRun)
	case 3:
		dayToRun = os.Args[1]
		fileName = fmt.Sprintf("./input/day%s-test.txt", dayToRun)
	}

	fmt.Printf("Running Advent of Code Day %s\n", dayToRun)
	start := time.Now()
	switch dayToRun {
	case "1":
		adventofcode2019.Day1(fileName)
	case "2":
		adventofcode2019.Day2(filename)
	default:
		fmt.Println("I don't have a solution for that day")
	}
	total := time.Since(start)
	fmt.Printf("Day %s Took %s\n", dayToRun, total)
}
