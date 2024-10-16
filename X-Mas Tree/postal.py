from grid import Grid
from tree import Tree

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
                if current_tree_value != ' ':
                    self.grid.set_value(i + l, j + m - mid_tree, current_tree_value)

    def display(self):
        self.grid.display()
