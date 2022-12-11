from itertools import chain
import re
from enum import Enum

class Duration(Enum):
    ADDX_DURATION_IN_CYCLES = 2
    NOOP_DURATION_IN_CYCLES = 1

with open("tests/day10.txt") as f:
    X = 1
    cycle = 0
    signal_strength = 0
    crt_pixels = [['.'] * 40 for x in range(6)]
    for line in f:
        processed_line = line.rstrip()
        addx = re.match("addx (-?\d+)", processed_line)
        if addx is not None:
            value_to_add = int(addx.groups()[0])
            for _ in range(Duration.ADDX_DURATION_IN_CYCLES.value):
                cycle += 1
                curr_crt_index = ((cycle - 1) // 40, (cycle - 1 ) % 40)
                if X-1 <= curr_crt_index[1] and curr_crt_index[1] <= X + 1:
                    crt_pixels[curr_crt_index[0]][curr_crt_index[1]] = '#'
                else:
                    crt_pixels[curr_crt_index[0]][curr_crt_index[1]] = '.'
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    signal_strength += X * cycle
                if cycle == 20:
                    for i in range(len(crt_pixels)):
                        for j in range(len(crt_pixels[0])):
                            print(crt_pixels[i][j], end='')
                    print()
            X += value_to_add
        else:
            for _ in range(Duration.NOOP_DURATION_IN_CYCLES.value):
                cycle += 1
                curr_crt_index = ((cycle - 1) // 40, (cycle - 1) % 40)
                if X-1 <= curr_crt_index[1] and curr_crt_index[1] <= X + 1:
                    crt_pixels[curr_crt_index[0]][curr_crt_index[1]] = '#'
                else:
                    crt_pixels[curr_crt_index[0]][curr_crt_index[1]] = '.'
                if cycle == 20 or (cycle - 20) % 40 == 0:
                    signal_strength += X * cycle
                if cycle == 20:
                    for i in range(len(crt_pixels)):
                        for j in range(len(crt_pixels[0])):
                            print(crt_pixels[i][j], end='')
                    print()
    print(signal_strength)
    for i in range(len(crt_pixels)):
        for j in range(len(crt_pixels[0])):
            print(crt_pixels[i][j], end='')
        print()
