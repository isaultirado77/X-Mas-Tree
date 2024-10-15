# X-Mas Tree Project

class Grid:
    def __init__(self, tree_height: int):
        self.height = tree_height + 2
        self.width = tree_height + 1 + 2
        self.grid = []
        self.build_gird()

    def build_gird(self) -> None:
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append('%')
            self.grid.append(row)

    def set_value(self, i: int, j: int, value: str) -> None:
        if 0 <= i < self.height and 0 <= j < self.width:
            self.grid[i][j] = value
        else:
            print("Error: Enter valid row or col")

    def display(self) -> None:
        print(self)

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.grid)

    @staticmethod
    def create_grid(tree_height: int):
        return Grid(tree_height)


class Tree:

    def __init__(self, tree_height: int):
        self.tree_height = tree_height + 2
        self.grid = Grid.create_grid(tree_height)

    def build_top(self) -> None:
        pass

    def build_trunk(self) -> None:
        pass

    def build_body(self) -> None:
        pass

    def display(self):
        self.grid.display()


def read_height() -> int:
    try:
        height = int(input())
        return height
    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    # height = read_height()

    pass


if __name__ == "__main__":
    main()
