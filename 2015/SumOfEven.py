def readNumbers():
    numbers = []
    for i in range(1,6+1):
        num = int(input("Type number {} : ".format(i)))
        numbers.append(num)
    return numbers

def sumOfEven(numbers):
    return sum(item for item in numbers if item % 2 == 0)

def main():
    print(sumOfEven(readNumbers()))

main()