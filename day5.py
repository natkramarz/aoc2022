import re
from collections import deque

# part 1
with open("tests/day5.txt") as f:
    stacks = []
    for line in f:
        processed_line = line.rstrip()
        if re.match("^\s*\[", processed_line):
            for i in range(0, len(processed_line), 4):
                stack_index = i // 4
                if len(stacks) <= stack_index:
                    stacks.append(deque())
                if processed_line[i:i+3] != "   ":
                    stacks[stack_index].appendleft(processed_line[i+1])
        else:
            matched = re.match("^move (\d+) from (\d+) to (\d+)$", processed_line)
            if matched is not None:
                from_index = int(matched.groups()[1]) - 1
                to_index = int(matched.groups()[2]) - 1
                for _ in range(int(matched.groups()[0])):
                    crate = stacks[from_index].pop()
                    stacks[to_index].append(crate)
    print("".join([stack[-1] for stack in stacks]))

# part 2 
with open("tests/day5.txt") as f:
    stacks = []
    for line in f:
        processed_line = line.rstrip()
        if re.match("^\s*\[", processed_line):
            for i in range(0, len(processed_line), 4):
                stack_index = i // 4
                if len(stacks) <= stack_index:
                    stacks.append(deque())
                if processed_line[i:i+3] != "   ":
                    stacks[stack_index].appendleft(processed_line[i+1])
        else:
            matched = re.match("^move (\d+) from (\d+) to (\d+)$", processed_line)
            if matched is not None:
                from_index = int(matched.groups()[1]) - 1
                to_index = int(matched.groups()[2]) - 1
                curr_crates = []
                for _ in range(0, int(matched.groups()[0])):
                    if len(stacks[from_index]) == 0:
                        break
                    crate = stacks[from_index].pop()
                    curr_crates.append(crate)
                for i in reversed(curr_crates):
                    stacks[to_index].append(curr_crates[i])
    print(stacks)
    print("".join([stack[-1] for stack in stacks if len(stack) != 0]))