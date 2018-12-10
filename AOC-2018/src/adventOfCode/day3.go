package adventofcode

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
)

//Day3 - Run day 3 of advent of code https://adventofcode.com/2018/day/3
func Day3(filename string) {
	fmt.Printf("Advent of Code Day 3\n")
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)
	fabric := make([][]int, 1000)
	for i := range fabric {
		fabric[i] = make([]int, 1000)
	}
	claimSize := 0
	trueClaims := make(map[int]struct{}, 0)
	exists := struct{}{}
	for scanner.Scan() {
		id, fromLeft, fromTop, width, height := parseLine(scanner.Text())
		trueClaim := true
		for row := 0; row < height; row++ {
			for col := 0; col < width; col++ {
				currentClaim := fabric[row+fromTop][col+fromLeft]
				if currentClaim == 0 {
					fabric[row+fromTop][col+fromLeft] = id
				} else if currentClaim > 0 {
					trueClaim = false
					delete(trueClaims, currentClaim)
					fabric[row+fromTop][col+fromLeft] = -1
					claimSize++
				} else {
					trueClaim = false
				}
			}
		}
		if trueClaim {
			trueClaims[id] = exists
		}
	}

	fmt.Printf("Claim size overall: %d\n", claimSize)
	for finalTrueClaimValue := range trueClaims {
		fmt.Printf("The true claim %d\n", finalTrueClaimValue)
	}
}

func parseLine(line string) (int, int, int, int, int) {
	lineRegex := regexp.MustCompile("[\\d]+")
	entries := lineRegex.FindAllString(line, -1)
	id, _ := strconv.Atoi(entries[0])
	fromLeft, _ := strconv.Atoi(entries[1])
	fromTop, _ := strconv.Atoi(entries[2])
	width, _ := strconv.Atoi(entries[3])
	height, _ := strconv.Atoi(entries[4])
	return id, fromLeft, fromTop, width, height
}
