from grid import Grid


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
        self.grid.set_value(1, mid, '^')
        for k in range(h):
            for l in range(k + 1):
                self.grid.set_value(2 + k, mid + l + 1, '\\')
                self.grid.set_value(2 + k, mid - l - 1, '/')
                for m in range(l + 1):
                    self.grid.set_value(2 + k, mid + m, '*')
                    self.grid.set_value(2 + k, mid - m, '*')
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

    def get_mid(self) -> int:
        return self.grid.get_mid()

    def get_size(self):
        return self.grid.get_size()

    def get_value(self, i: int, j: int) -> str:
        return self.grid.get_value(i, j)

    def set_value(self, i: int, j: int, value: str) -> None:
        self.grid.set_value(i, j, value)

    @staticmethod
    def get_tree(height: int, interval: int):
        tree = Tree(height, interval)
        tree.build_top()
        tree.build_body()
        tree.build_trunk()
        return tree

    def display(self):
        self.grid.display()
