using Printf

println("Advent of Code Day 1")

function ()

end

function () 

end

input = open("./AOC-2020/input/01/01-input.txt", "r")

billInts = [ parse(Int, entry) for entry in eachline(input) ];
sort!(billInts);

firstNumber = 0;
secondNumber = 0;

for i in eachindex(billInts)
  firstNumber = billInts[i];
  for j in reverse(eachindex(billInts))
    secondNumber = billInts[j];
    for k in reverse(eachindex(billInts))
      if j == k
        continue
      else
        thirdNumber = billInts[k]
        if firstNumber + secondNumber + thirdNumber == 2020
          println("First Number: ", firstNumber)
          println("Second Number: ", secondNumber)
          println("Third Number: ", thirdNumber)
          println("Product: ", firstNumber * secondNumber * thirdNumber)
          println()
        end
      end
    end
    if (firstNumber + secondNumber) == 2020
      println("First Number: ", firstNumber)
      println("Second Number: ", secondNumber)
      println("Product: ", firstNumber * secondNumber)
      println()
    end
  end
end
