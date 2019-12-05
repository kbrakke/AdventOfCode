package adventofcode2019

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"math"
	"strings"
)

type Vertex struct {
	x int
	y int
}

//Day3 - Run day 3 of advent of code https://adventofcode.com/2019/day/3
func Day3(filename string) {
	fmt.Printf("Advent of Code Day 3\n")
	file, _ := os.Open(filename)
	scanner := bufio.NewScanner(file)
	wirePoints := make([][]Vertex, 0)
	wireStrings := make(map[int]string)
	line := 0
	for scanner.Scan() {
		wireStrings[line] = scanner.Text()
		line = line + 1
	}
	for _, v := range wireStrings {
		wirePoints = append(wirePoints, wireStringToPoints(v))
	}
	shortestDistance := float64(999999999999)
	shortestSteps := len(wirePoints[0]) + len(wirePoints[1]) + 1
	for i :=0; i < len(wirePoints[0]); i++ {
		for j := 0; j < len(wirePoints[1]); j++ {
			if wirePoints[0][i] == wirePoints[1][j] {
				distance := math.Abs(float64(wirePoints[0][i].x)) + math.Abs(float64(wirePoints[0][i].y))
				steps := i + j + 2
				if distance < shortestDistance {
					shortestDistance = distance
				}
				if steps < shortestSteps {
					shortestSteps = steps
				}
			}
		}
	}
	fmt.Printf("The Shortest Distance: %f\n", shortestDistance)
	fmt.Printf("The Shortest Steps: %d\n", shortestSteps)

}

func wireStringToPoints(wire string) []Vertex {
	// all maps start at the origin
	points := make([]Vertex, 0)
	head := Vertex{0, 0}
	commands := strings.SplitN(wire, ",", -1)
	for _, command := range commands {
		runeCommand := []rune(command)
		direction := runeCommand[:1]
		distance, _ := strconv.Atoi(string(runeCommand[1:]))
		switch direction[0] {
		case 'U': {
			finalY := head.y + distance
			for val := head.y; val < finalY; val++ {
				points = append(points, Vertex{head.x, val})
			}
			head = Vertex{head.x, finalY}
		}
		case 'R':
			finalX := head.x + distance
			for val := head.x; val < finalX; val++ {
				points = append(points, Vertex{val, head.y})
			}
			head = Vertex{finalX, head.y}
		case 'D':
			finalY := head.y - distance
			for val := head.y; val > finalY; val-- {
				points = append(points, Vertex{head.x, val})
			}
			head = Vertex{head.x, finalY}
		case 'L':
			finalX := head.x - distance
			for val := head.x; val > finalX; val-- {
				points = append(points, Vertex{val, head.y})
			}
			head = Vertex{finalX, head.y}
		}
	}
	return points[1:]
}