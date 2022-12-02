with open("tests/day1.txt") as f:
    calories = []
    curr_count = 0 
    for line in f:
        if line == '\n':
            calories.append(curr_count)
            curr_count = 0
        else:
            curr_count += int(line.rstrip())
    # part 1 
    # print(max(calories))
    first_max = max(calories)
    calories.remove(first_max)
    second_max = max(calories)
    calories.remove(second_max)
    third_max = max(calories)
    print(first_max + second_max + third_max)
