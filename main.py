import time


class IndividualIndex:

    def __init__(self, i, j):
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
    rows, cols = (15, 15)
    grid = [[0 for i in range(cols)] for j in range(rows)]

    def arrow():  # Standard arrow formation - moves on its own
        grid[7][7] = 1; grid[8][8] = 1; grid[9][6] = 1; grid[9][7] = 1; grid[9][8] = 1

    def A_for_all():  # A for all - cyclical
        grid[2][6] = 1; grid[2][7] = 1
        grid[3][5] = 1; grid[3][8] = 1
        grid[4][5] = 1; grid[4][6] = 1; grid[4][7] = 1; grid[4][8] = 1
        grid[5][3] = 1; grid[5][5] = 1; grid[5][8] = 1; grid[5][10] = 1
        grid[6][2] = 1; grid[6][11] = 1
        grid[7][2] = 1; grid[7][11] = 1
        grid[8][3] = 1; grid[8][5] = 1; grid[8][8] = 1; grid[8][10] = 1
        grid[9][5] = 1; grid[9][6] = 1; grid[9][7] = 1; grid[9][8] = 1
        grid[10][5] = 1; grid[10][8] = 1
        grid[11][6] = 1; grid[11][7] = 1

    selection = input("pick a. arrow or b. A for all ")
    if selection == "a":
        arrow()
    elif selection == "b":
        A_for_all()

    iterations = input("How many iterations? ")

    for rows in grid:
        print(rows)

    time.sleep(1)

    dict = {}
    for repeats in range(int(iterations)):
        for down in range(15):
            for right in range(15):
                key = str("grid" + str(down) + str(right))
                dict[key] = IndividualIndex(down, right)
                dict[f'grid{down}{right}'].counting()

    # print(dict)
        for down in range(15):
            for right in range(15):
                dict[f'grid{down}{right}'].change()
                # dict[f'grid{down}{right}'].measure()

        print("\n")
        for rows in grid:
            print(rows)
        time.sleep(1)


