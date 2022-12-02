from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

with open("tests/day2.txt") as f:
    my_moves = {"X": Move.ROCK, "Y": Move.PAPER, "Z": Move.SCISSORS}
    elf_moves = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSORS}
    total_points = 0 
    for line in f:
        processed_moves = line.rstrip().split()
        elf, me = elf_moves[processed_moves[0]], my_moves[processed_moves[1]]
        curr_score = me.value
        if elf == me:
            curr_score += Result.DRAW.value
        elif (me == Move.ROCK and elf == Move.SCISSORS) or (me == Move.PAPER and elf == Move.ROCK) or (me == Move.SCISSORS and elf == Move.PAPER):
            curr_score += Result.WIN.value
        total_points += curr_score 
    # first part
    print(total_points)


with open("tests/day2.txt") as f:
    result_map = {"X": Result.LOSE, "Y": Result.DRAW, "Z": Result.WIN}
    elf_moves = {"A": Move.ROCK, "B": Move.PAPER, "C": Move.SCISSORS}
    total_points = 0 
    for line in f:
        processed_moves = line.rstrip().split()
        elf, result = elf_moves[processed_moves[0]], result_map[processed_moves[1]]
        curr_score = 0
        if result == Result.DRAW:
            curr_score += elf.value + Result.DRAW.value
        elif result == Result.LOSE:
            if elf == Move.ROCK:
                curr_score += Move.SCISSORS.value
            elif elf == Move.PAPER:
                curr_score += Move.ROCK.value
            else:
                curr_score += Move.PAPER.value
        else:
            if elf == Move.ROCK:
                curr_score += Move.PAPER.value
            elif elf == Move.PAPER:
                curr_score += Move.SCISSORS.value
            else: 
                curr_score += Move.ROCK.value
            curr_score += Result.WIN.value
        total_points += curr_score 
    print(total_points)