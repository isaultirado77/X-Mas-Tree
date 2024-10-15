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
        for row in self.grid:
            print(row)

    def __str__(self):
        return '\n'.join(' '.join(row) for row in self.grid)

    @staticmethod
    def create_grid(tree_height: int):
        return Grid(tree_height)


class Postal:

    def __init__(self, height: int):
        self.height = height + 2

    def build_top(self) -> None:
        pass

    def build_trunk(self) -> None:
        pass

    def build_body(self) -> None:
        for i in range(self.height):
            stars = '*' * (2 * i + 1)
            spaces = ' ' * (self.height - i - 1)

    def get_tree(self) -> str:
        pass


def read_height() -> int:
    try:
        height = int(input())
        return height
    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    # height = read_height()
    grid = Grid(4)
    print(grid)


if __name__ == "__main__":
    main()
