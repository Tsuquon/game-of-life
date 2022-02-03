rows, cols = (5, 5)
grid = [[0 for i in range(cols)] for j in range(rows)]
grid[3][1] = 1; grid[2][2] = 1; grid[2][3] = 1; grid[1][2] = 1; grid[0][0] = 1; grid[4][0] = 1;  # grid[1][3] = 1;

# establish a class for each index then use a counter for each to count its neighbours
# Use trys and exceptions for border numbers

class IndividualIndex():

    def __init__(self, i, j):  # Change the if grid... to individual lines that add to a count and if that count doesn't equal two or three then change the number to zero. This code has to run through all the numbers. Add tries and exceptions (WIP)
        self.count = 0
        self.i = i
        self.j = j

    def counting(self):
        # print(self.count + 1)
        if grid[self.i][self.j] == 1:
            for i_iter in [-1, 0, 1]:
                for j_iter in [-1, 0, 1]:
                    if abs(i_iter) + abs(j_iter) != 0:
                        try:
                            if grid[self.i+i_iter][self.j+j_iter] == 1:  # counts neighbours which are one
                                if self.i+i_iter >= 0 and self.j+j_iter >= 0:
                                        self.count += 1
                        except:
                            pass

            print(self.count)  # Checks that the loop is detecting and adding properly - debugging
        else:  # make this one count if its a zero
            pass
        self.change()


    def change(self):
        if self.count != 2 and self.count != 3:  # This has to go on the outside of this function
            grid[self.i][self.j] = 0
        else:
            grid[self.i][self.j] = 1

if __name__ == "__main__":
    for rows in grid:
        print(rows)

    for down in range(5):
        for right in range(5):
            name = IndividualIndex(down, right)
            name.counting()

    # for down in range(5):
    #     for right in range(5):
    #         name.change()
            # f"variable{down}{right}".counting()
            # f"variable{down}{right}".change()

    # grid00 = IndividualIndex(0, 0)
    # grid00.counting()
    # grid31 = IndividualIndex(3, 1)
    # grid31.counting()
    # grid23 = IndividualIndex(2, 3)
    # grid23.counting()
    # grid00.change()

    print("\n")
    for rows in grid:
        print(rows)

