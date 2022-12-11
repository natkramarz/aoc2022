def check_tree_in_line_heights(grid, already_visible, start_row, start_col, direction_row, direction_col):
    if direction_row == 0:
        col_indexes = range(1, len(grid[0]) - 1) if direction_col == 1 else range(len(grid[0]) - 2, 0, -1)
        max_prev_height = grid[start_row][0] if direction_col == 1 else grid[start_row][len(grid[0]) - 1]
        for col in col_indexes:
            if max_prev_height < grid[start_row][col]:
                max_prev_height = grid[start_row][col]
                already_visible[start_row][col] = True
    else:
        row_indexes = range(1, len(grid) - 1) if direction_row == 1 else range(len(grid) - 2, 0, -1)
        max_prev_height = grid[0][start_col] if direction_row == 1 else grid[len(grid)-1][start_col]
        for row in row_indexes:
            if max_prev_height < grid[row][start_col]:
                max_prev_height = grid[row][start_col]
                already_visible[row][start_col] = True


def check(grid, start_row, start_col, direction_row, direction_col):
    if direction_row == 0:
        curr_row = [0] * len(grid[0])
        col_indexes = range(len(grid[0])) if direction_col == 1 else range(len(grid[0]) - 1 , -1, -1)
        for col in col_indexes:
            i = col + direction_col * (-1)
            while i >= 0 and i <= len(grid[0]) - 1:
                curr_row[col] += 1
                if grid[start_row][i] >= grid[start_row][col]:
                    break
                i += direction_col * (-1)
        return curr_row
    else:
        curr_col = [0] * len(grid)
        row_indexes = range(len(grid)) if direction_row == 1 else range(len(grid) - 1, -1, -1)
        for row in row_indexes:
            i = row + direction_row * (-1)
            while i >= 0 and i <= len(grid) - 1:
                curr_col[row] += 1
                if grid[i][start_col] >= grid[row][start_col]:
                    break
                i += direction_row * (-1)
        return curr_col


with open("tests/day8.txt") as f:
    grid = []
    for line in f:
        grid.append(list(line.rstrip()))
    
    # part 1
    already_visible = [[True] + [False] * (len(row) - 2) + [True] for row in grid]
    already_visible[0] = [True] * (len(already_visible[0]))
    already_visible[len(grid) - 1] = [True] * (len(already_visible[len(grid) - 1]))

    for row in range(1, len(grid) - 1):
        check_tree_in_line_heights(grid, already_visible, start_row=row, start_col=1, direction_row=0, direction_col=1)
        check_tree_in_line_heights(grid, already_visible, start_row=row, start_col=len(grid[0])-2, direction_row=0, direction_col=-1)

    for col in range(1, len(grid[0]) - 1):
        check_tree_in_line_heights(grid, already_visible, start_col=col, start_row=1, direction_col=0, direction_row=1)
        check_tree_in_line_heights(grid, already_visible, start_col=col, start_row=len(grid) - 2, direction_col=0, direction_row=-1)
    
    visible_tree_count = sum(row.count(True) for row in already_visible)
    print(visible_tree_count)

    # part 2
    scenic_score = [[1] * len(row) for row in grid]
    for row in range(len(grid)):
        scenic_score[row] = [scenic_score[row][i] * x for i, x in  enumerate(check(grid, start_row=row, start_col=0, direction_row=0, direction_col=1))]
        scenic_score[row] = [scenic_score[row][i] * x for i, x in  enumerate(check(grid, start_row=row, start_col=len(grid[0])-1, direction_row=0, direction_col=-1))]

    for col in range(len(grid[0])):
        curr_col = check(grid, start_col=col, start_row=0, direction_col=0, direction_row=1)
        for i in range(len(grid)):
            scenic_score[i][col] *= curr_col[i]
        curr_col = check(grid, start_col=col, start_row=len(grid) - 1, direction_col=0, direction_row=-1)
        for i in range(len(grid)):
            scenic_score[i][col] *= curr_col[i]

    print(max(max(row) for row in scenic_score))