# X-Mas Tree Project

class Grid:
    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width
        self.grid = []
        self.build_grid()

    def build_grid(self) -> None:
        for _ in range(self.height):
            row = [' '] * self.width
            self.grid.append(row)

    def set_value(self, i: int, j: int, value: str) -> None:
        if 0 <= i < self.height and 0 <= j < self.width:
            self.grid[i][j] = value
        else:
            print("Error: Enter valid row or col")

    def get_value(self, i: int, j: int) -> str:
        if 0 <= i < self.height and 0 <= j < self.width:
            return self.grid[i][j]
        else:
            print("Error: Enter valid row or col")
            return ''

    def fill_sides(self) -> None:
        for j in range(self.width):
            self.grid[0][j] = '-'  # Top row
            self.grid[-1][j] = '-'  # Bottom row

        for i in range(1, self.height - 1):
            self.grid[i][0] = '|'  # Left column
            self.grid[i][-1] = '|'  # Right column

    def display(self) -> None:
        print(self)

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def get_mid(self) -> int:
        return self.width // 2

    def get_size(self) -> tuple:
        return self.height, self.width


class Tree:
    def __init__(self, tree_height: int, interval: int):
        self.tree_height = tree_height
        self.interval = interval
        height = tree_height + 2
        width = (tree_height - 1) * 2 + 1
        self.grid = Grid(height, width)

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

    def get_value(self, i: int, j: int):
        return self.grid.get_value(i, j)

    def set_value(self, i: int, j: int, value: str):
        return self.grid.set_value(i, j, value)

    def get_mid(self):
        return self.grid.get_mid()

    def get_size(self):
        return self.grid.get_size()

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
    def __init__(self, height: int = 30, width: int = 50):
        self.height = height
        self.width = width
        self.grid = Grid(height, width)
        self.grid.fill_sides()
        self.build_message()

    def build_message(self, msg="Merry Xmas"):
        mid = self.grid.get_mid()
        start_index = mid - len(msg) // 2
        for i, char in enumerate(msg):
            self.grid.set_value(27, start_index + i, char)

    def place_tree(self, tree: Tree, i: int, j: int) -> None:
        mid_tree = tree.get_mid()
        h, w = tree.get_size()
        for l in range(h):
            for m in range(w):
                current_tree_value = tree.get_value(l, m)
                self.grid.set_value(i + l, j + m - mid_tree, current_tree_value)

    def display(self):
        self.grid.display()


def read_inputs():
    try:
        inputs = str(input())
        split_inputs = inputs.split(' ')

    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    tree = Tree.get_tree(5, 2)
    tree.display()
    postal = Postal()
    postal.place_tree(tree, 10, 10)
    postal.display()


if __name__ == "__main__":
    main()
