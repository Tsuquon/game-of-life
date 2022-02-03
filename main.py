rows, cols = (5, 5)
grid = [[0 for i in range(cols)] for j in range(rows)]
grid[2][2] = 1; grid[2][3] = 1; grid[1][2] = 1; grid[0][0] = 1
for rows in grid:
    print(rows)


# Machine needs to run through all numbers before making a change
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == 1:
            if (grid[i-1][j-1] == 1) + (grid[i-1][j] == 1) + (grid[i-1][j+1] == 1) + (grid[i][j-1] == 1) + \
                    (grid[i][j+1] == 1) + (grid[i+1][j-1] == 1) + \
                    (grid[i+1][j] == 1) + (grid[i+1][j+1] == 1) != 2 and 3:
                grid[i][j] = 0
        # elif val == 0:
        #     if (grid[i - 1][j - 1] == 1) + (grid[i - 1][j] == 1) + (grid[i - 1][j + 1] == 1) + (grid[i][j - 1] == 1) + \
        #             (grid[i][j + 1] == 1) + (grid[i + 1][j - 1] == 1) + \
        #             (grid[i + 1][j] == 1) + (grid[i + 1][j + 1] == 1) == 3:
        #         grid[i][j] = 1




print("\n")
for rows in grid:
    print(rows)
            # print(i, j)





# if grid[2][1] == 1:
#     print("hello")
