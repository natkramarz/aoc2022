from collections import defaultdict
with open("tests/day6.txt") as f:
    sequence = ""
    buffer = defaultdict(lambda: 0)
    for line in f:
        sequence = line.rstrip()
    marker_len = 14
    for i in range(marker_len):
        buffer[sequence[i]] += 1
    for i in range(marker_len, len(sequence)):
        if len(buffer) == marker_len and sum([val for val in buffer.values()]) == marker_len:
            print(i)
            break
        buffer[sequence[i-marker_len]] -= 1
        if buffer[sequence[i-marker_len]] < 1:
            buffer.pop(sequence[i-marker_len])
        buffer[sequence[i]] += 1
    
