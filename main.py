rows, cols = (5, 5)
grid = [[0 for i in range(cols)] for j in range(rows)]
grid[3][1] = 1; grid[2][2] = 1; grid[2][3] = 1; grid[1][2] = 1; grid[0][0] = 1
for rows in grid:
    print(rows)

# establish a class for each index then use a counter for each to count its neighbours
# Use trys and exceptions for border numbers

class IndividualIndex():

    def __init__(self, i, j):  # Change the if grid... to individual lines that add to a count and if that count doesn't equal two or three then change the number to zero. This code has to run through all the numbers. Add tries and exceptions (WIP)
        self.count = 0
        self.i = i
        self.j = j
        if grid[i][j] == 1:
            try:
                if grid[i-1][j-1] == 1:
                    self.count += 1
            except:
                pass
            try:
                if grid[i-1][j] == 1:
                    self.count += 1
            except:
                pass
                if grid[i-1][j+1] == 1:
                    self.count += 1
            try:
                if grid[i][j-1] == 1:
                    self.count += 1
            except:
                pass
            try:
                if grid[i][j+1] == 1:
                    self.count += 1
            except:
                pass
            try:
                if grid[i+1][j-1] == 1:
                    self.count += 1
            except:
                pass
            try:
                if grid[i+1][j] == 1:
                    self.count += 1
            except:
                pass
            try:
                if grid[i+1][j+1] == 1:
                    self.count += 1
            except:
                pass

            print(self.count)
        if self.count != 2 and self.count != 3:  # This has to go on the outside of this function
            grid[i][j] = 0

if __name__ == "__main__":
    IndividualIndex(3, 1)
    IndividualIndex(0, 0)
    print("\n")
    for rows in grid:
        print(rows)


