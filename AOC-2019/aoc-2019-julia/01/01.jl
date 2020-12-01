using Printf

println("Advent of Code Day 1")

function simpleFuel(mass)
    return (mass ÷ 3) - 2
end

function recursiveFuel(mass) 
    fuel = simpleFuel(mass)
    fuel > 0 ? fuel + recursiveFuel(fuel) : 0
end

pwd()
input = open("./AOC-2019/aoc-2019-julia/01/01.txt", "r")

part1Fuel = 0
part2Fuel = 0


for massString in eachline(input)
    mass = parse(Int, massString)
    global part1Fuel += simpleFuel(mass)
    global part2Fuel += recursiveFuel(mass)
end

@printf("Fuel for Part 1: %d\n", part1Fuel)
@printf("Fuel for Part 2: %d\n", part2Fuel)

