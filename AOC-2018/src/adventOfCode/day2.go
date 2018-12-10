package adventofcode

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

//Day2 - Run day 2 of advent of code https://adventofcode.com/2018/day/2
func Day2(filename string) {
	fmt.Printf("Advent of Code Day 2\n")
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)
	ids := make([]string, 0)
	checkSum := make([]int, 2)
	correctID := ""
	for scanner.Scan() {
		id := scanner.Text()
		ids = append(ids, id)
		checkSumContribution := getChecksumValues(id)
		checkSum[0] += checkSumContribution[0]
		checkSum[1] += checkSumContribution[1]

	}
	fmt.Printf("Checksum %d\n", checkSum[0]*checkSum[1])
	for _, id := range ids {
		for _, id2 := range ids {
			if id != id2 {
				potentalID, isPotential := differByOneCharacter(id, id2)
				if isPotential {
					correctID = potentalID
				}
			}
		}
	}
	fmt.Printf("Correct id %s\n", correctID)
}

func getChecksumValues(id string) []int {
	checkSumContribution := make([]int, 2)
	for _, character := range id {
		count := strings.Count(id, string(character))
		if count == 2 {
			checkSumContribution[0] = 1
		}
		if count == 3 {
			checkSumContribution[1] = 1
		}
		if checkSumContribution[0] > 0 && checkSumContribution[1] > 0 {
			return checkSumContribution
		}
	}
	return checkSumContribution
}

func differByOneCharacter(a string, b string) (string, bool) {
	differentIndex := -1
	for index := range a {
		if a[index] != b[index] {
			if differentIndex >= 0 {
				return "", false
			}
			differentIndex = index
		}
	}
	if differentIndex >= 0 {
		return a[:differentIndex] + a[differentIndex+1:], true
	}
	return "", false
}
