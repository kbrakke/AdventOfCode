package adventofcode2019

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

//Day1 - Run day 1 of advent of code https://adventofcode.com/2019/day/1
func Day1(filename string) {
	fmt.Printf("Advent of Code Day 1\n")
	file, _ := os.Open(filename)
	part1Fuel := 0
	part2Fuel := 0
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lineInt, _ := strconv.Atoi(scanner.Text())
		fuel := basicCalcFuelForModule(lineInt)
		totalFuel := recursiveCalcFuelForModule(lineInt)
		fmt.Printf("Module Mass: %d -- Fuel Needed: %d\n", lineInt, fuel)
		fmt.Printf("Module Mass: %d -- Total Fuel Needed: %d\n", lineInt, totalFuel)
		part1Fuel = part1Fuel + fuel
		part2Fuel = part2Fuel + totalFuel
	}

	fmt.Printf("Part 1 - Total Fuel Needed: %d\n", part1Fuel)
	fmt.Printf("Part 2 - Total Fuel Needed: %d\n", part2Fuel)
}

func basicCalcFuelForModule(module int) int {
	return (module / 3) - 2
}

func recursiveCalcFuelForModule(module int) int {
	basicFuel := basicCalcFuelForModule(module)
	if basicFuel <= 0 {
		return 0
	}
	return basicFuel + recursiveCalcFuelForModule(basicFuel)
}
