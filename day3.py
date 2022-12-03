from itertools import islice

# first part 
with open("tests/day3.txt") as f:
    total_sum = 0
    for line in f:
        processed_line = line.rstrip()
        first, second = processed_line[:len(processed_line)//2], processed_line[len(processed_line)//2:]
        first_types = set()
        for item in first:
            first_types.add(item)
        second_types = set()
        for item in second:
            second_types.add(item)
        common_types = first_types.intersection(second_types)
        total_sum += sum(list(map(lambda item: ord(item) -  96 if ord(item) >= 97 else ord(item) - 38, common_types)))
    print(total_sum)

# second part
with open("tests/day3.txt") as f:
    total_sum = 0
    lines = list(islice(f, 3))
    while lines:
        processed_lines = list(map(lambda line: line.rstrip(), lines))
        first, second, third = processed_lines[0], processed_lines[1], processed_lines[2]
        first_types = set()
        for item in first:
            first_types.add(item)
        second_types = set()
        for item in second:
            second_types.add(item)
        common_types = set()
        common_types = first_types.intersection(second_types)
        third_types = set()
        for item in third:
            third_types.add(item)
        common_types = third_types.intersection(common_types)
        total_sum += sum(list(map(lambda item: ord(item) -  96 if ord(item) >= 97 else ord(item) - 38, common_types)))
        lines = list(islice(f, 3))
    print(total_sum)