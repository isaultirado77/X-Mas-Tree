# X-Mas Tree Project
from typing import Any


class Grid:
    def __init__(self, tree_height: int):
        self.height = tree_height + 2
        self.width = (tree_height - 1) * 2 + 1
        self.grid = []
        self.build_gird()

    def build_gird(self) -> None:
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(' ')
            self.grid.append(row)

    def set_value(self, i: int, j: int, value: str) -> None:
        if 0 <= i < self.height and 0 <= j < self.width:
            self.grid[i][j] = value
        else:
            print("Error: Enter valid row or col")

    def get_value(self, i: int, j: int) -> Any:
        if 0 <= i < self.height and 0 <= j < self.width:
            return self.grid[i][j]
        else:
            print("Error: Enter valid row or col")
            return

    def display(self) -> None:
        print(self)

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def get_mid(self) -> int:
        return self.width // 2

    @staticmethod
    def create_grid(tree_height: int):
        return Grid(tree_height)


class Tree:

    def __init__(self, tree_height: int, interval: int):
        self.tree_height = tree_height
        self.interval = interval
        self.grid = Grid.create_grid(tree_height)

    def build_top(self) -> None:
        mid = self.grid.get_mid()
        self.grid.set_value(0, mid, 'X')  # Add the star

    def build_trunk(self) -> None:
        mid = self.grid.get_mid()
        bottom = self.grid.height - 1
        self.grid.set_value(bottom, mid - 1, '|')
        self.grid.set_value(bottom, mid + 1, '|')

    def build_body(self) -> None:
        h = self.tree_height - 1
        mid = self.grid.get_mid()
        # Put mid top element
        self.grid.set_value(1, mid, '^')
        for k in range(h):
            for l in range(k + 1):
                # Put sides
                self.grid.set_value(2 + k, mid + l + 1, '\\')
                self.grid.set_value(2 + k, mid - l - 1, '/')

                for m in range(l + 1):
                    # Put stars
                    self.grid.set_value(2 + k, mid + m, '*')
                    self.grid.set_value(2 + k, mid - m, '*')
        # Put decorations
        positions = self.find_decorations_positions()
        for position in positions:
            i, j = position
            self.grid.set_value(i, j, 'O')

    def find_decorations_positions(self) -> list:
        mid = self.grid.get_mid()
        h = self.grid.height - 1
        positions = []

        for i in range(3, h):
            num_positions = i - 2
            first_position = mid - num_positions + 1
            for j in range(num_positions):
                pos = first_position + j * 2
                positions.append((i, pos))

        return positions[::self.interval]

    @staticmethod
    def get_tree(height: int, interval: int):
        tree = Tree(height, interval)
        tree.build_top()
        tree.build_body()
        tree.build_trunk()
        return tree

    def display(self):
        self.grid.display()


class Postal:
    def __init__(self):
        pass

    def build_sides(self):
        pass

    def build_message(self):
        pass

    def place_tree(self, tree: Grid, i: int, j: int) -> None:
        pass


def read_inputs():
    try:
        inputs = str(input())
        split_inputs = inputs.split(' ')
        if len(split_inputs) > 2:
            print("Error: Enter a valid inputs. ")
            return -1
        height = int(split_inputs[0])
        interval = int(split_inputs[1])
        if interval < 1:
            print("Error: Interval must be greater or equal than 1. ")
        return height, interval
    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    height, interval = read_inputs()
    tree = Tree.get_tree(height, interval)
    tree.display()
    pass


if __name__ == "__main__":
    main()
