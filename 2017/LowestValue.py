def get_lowest_of_two_values(values):
    min_values = []
    for i in range(0, len(values)):
        min_value = min(values[i])
        min_values.append(min_value)

    return min(min_values)

def main():
    
    values = input("Input values : ")
    values = values.split(" ")
    lowest_num = get_lowest_of_two_values(values)
    print(lowest_num)

main()