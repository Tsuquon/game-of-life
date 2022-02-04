rows, cols = (5, 5)
grid = [[0 for i in range(cols)] for j in range(rows)]
grid[3][1] = 1; grid[2][2] = 1; grid[2][3] = 1; grid[1][2] = 1; grid[0][0] = 1; grid[4][0] = 1; grid[4][2] = 1;

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

            #print(self.count)  # Checks that the loop is detecting and adding properly - debugging

        elif grid[self.i][self.j] == 0:
            #  print(self.count)
            for i_iter in [-1, 0, 1]:
                for j_iter in [-1, 0, 1]:
                    if abs(i_iter) + abs(j_iter) != 0:
                        try:
                            if grid[self.i+i_iter][self.j+j_iter] == 1:  # counts neighbours which are one
                                if self.i+i_iter >= 0 and self.j+j_iter >= 0:
                                        self.count += 1

                        except:
                            pass

            return self.count
            # print(self.count)  # Checks that the loop is detecting and adding properly - debugging



    def change(self):
        if grid[self.i][self.j] == 1:
            if self.count != 2 and self.count != 3:
                grid[self.i][self.j] = 0
        if grid[self.i][self.j] == 0:
            if self.count == 3:
                grid[self.i][self.j] = 1

    def measure(self):
        return print(self.count)


if __name__ == "__main__":
    for rows in grid:
        print(rows)

    # name = IndividualIndex(0, 1)
    # name.counting()
    # name.measure()

    dict = {}
    for down in range(5):
        for right in range(5):
            key = str("grid" + str(down) + str(right))
            dict[key] = IndividualIndex(down, right)

    # print(dict)
    for down in range(5):
        for right in range(5):
            dict[f'grid{down}{right}'].counting()
            # dict[f'grid{down}{right}'].measure()

    for down in range(5):
        for right in range(5):
            dict[f'grid{down}{right}'].change()
            # dict[f'grid{down}{right}'].measure()

    # for key, value in dict.items():
    #     exec(f'{key} = {value}')
    # for down in range(5):
    #     for right in range(5):
    #         f'grid{down}{right}'

    # for down in range(5):  # Test mechanism to see if neighbours still detect.
    #     for right in range(5):
    #         name = IndividualIndex(down, right)
    #         name.counting()
    #         name.measure()
    #
    # print("\n")
    # for loop in range(25):
    #     print(name.measure())
    #     name.change()







    print("\n")
    for rows in grid:
        print(rows)

