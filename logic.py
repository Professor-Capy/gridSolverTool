class Node:
    def __init__(self, value: str) -> None:
        self.value = value

    def setNode(self, newVal: str) -> None:
        self.value = newVal

    def __repr__(self):
        # a str() is needed since python
        # typehinting isnt enforced
        return str(self.value)

class Grid:
    def __init__(self, row: int, col: int, emptyVal: str = '#') -> None:
        self.emptyVal = emptyVal

        self.grid = []
        for i in range(0, row):
            temp = []
            for i in range(0, col):
                temp.append(Node(self.emptyVal))
            self.grid.append(temp)

    def findNeighbour(self, row: int, col: int) -> tuple:
        neighbours = []
        # if the current location isnt the top row, add box directly
        # above current box then check the top-left and top-right
        if not row == 0:
            neighbours.append((row - 1, col))
            if not col == 0: # for top-left
                neighbours.append((row - 1, col - 1))
            if not col == len(self.grid[0]) - 1: # for top-right
                neighbours.append((row - 1, col + 1))

        # if current location isnt bottom row, add box
        # directly below current one, then check bottom-left and bottom-right
        if not row == len(self.grid) - 1:
            neighbours.append((row + 1, col))
            if not col == 0: # for bottom-left
                neighbours.append((row + 1, col - 1))
            if not col == len(self.grid[0]) - 1: # for bottom-right
                neighbours.append((row + 1, col + 1))

        # if current location is not to the very left,
        # add box directly to left of current one
        if not col == 0:
            neighbours.append((row, col - 1))

        # if current location is not the the very right,
        # add box directly to the right of current one
        if not col == len(self.grid[0]) - 1:
            neighbours.append((row, col + 1))

        return tuple(neighbours)

    def minimizeMDistance(self) -> tuple:
        pass

    # Change __repr__ magic method so it doesn't include [] and stuff
    def __repr__(self):
        return str(self.grid)

if __name__ == '__main__':
    map = Grid(2, 2)
    print(map)
