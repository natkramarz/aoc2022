def is_fully_container(inner, outer):
    return (inner[0] >= outer[0] and inner[0] <= outer[1]) or (inner[1] >= outer[0] and inner[1] <= outer[1]) 

with open("tests/day4.txt") as f:
    fully_contained_num = 0
    for line in f:
        processed_line = line.rstrip().split(',')
        first = [int(x) for x in processed_line[0].split('-')]
        second = [int(x) for x in processed_line[1].split('-')]
        fully_contained_num += 1 if is_fully_container(first, second) or is_fully_container(second, first) else 0
    print(fully_contained_num)
