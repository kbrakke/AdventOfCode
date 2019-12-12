package adventofcode2019

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"math"
	"strings"
)

//Day4 - Run day 4 of advent of code https://adventofcode.com/2019/day/4
func Day4(filename string) {

}

func isValidCode(code int) {
	return isAscending(code) && hasDouble(code) && is6Digits(code)
}

func is6Digits(code) {
	return len(strconv.Itoa(code)) == 6
}