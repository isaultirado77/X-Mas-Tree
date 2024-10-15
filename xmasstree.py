# X-Mas Tree Project

class Grid:
    def __init__(self, tree_height: int):
        self.height = tree_height + 2
        self.width = tree_height + 5
        self.grid = []
        self.build_gird()

    def build_gird(self) -> None:
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append('.')
            self.grid.append(row)

    def set_value(self, i: int, j: int, value: str) -> None:
        if 0 <= i < self.height and 0 <= j < self.width:
            self.grid[i][j] = value
        else:
            print("Error: Enter valid row or col")

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

    def __init__(self, tree_height: int):
        self.tree_height = tree_height
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

        pass

    @staticmethod
    def get_tree(height: int):
        tree = Tree(height)
        tree.build_top()
        tree.build_body()
        tree.build_trunk()
        return tree

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
    tree = Tree.get_tree(4)
    tree.display()
    pass


if __name__ == "__main__":
    main()
