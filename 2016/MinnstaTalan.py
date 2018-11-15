def receiveInput(numbers, count):
    numbers = numbers.split(" ")
    numbers_count = len(numbers)
    if numbers_count >= 3 and numbers_count <= count:
        findSmallest(numbers)

def findSmallest(numbers):
    min_values = []
    for i in range(0, len(numbers)):
        min_value = min(numbers[i])
        min_values.append(min_value)

    print("The smallest number is {}".format(min(min_values)))

def main():
    total_numbers = int(input("How many numbers will you enter?"))
    numbers_input = input("")    
    receiveInput(numbers_input, total_numbers)

main()