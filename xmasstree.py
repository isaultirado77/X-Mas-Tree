# X-Mas Tree Project

class Tree:
    def __init__(self, height: int):
        self.height = height
        self.tree = []

    def build_top(self):
        pass

    def build_crown(self):
        space = ' '
        star = '*'
        for i in range(self.height):
            stars = star * (2 * i + 1)
            spaces = space * (self.height - i - 1)

    def build_trunk(self):
        pass


def read_height() -> int:
    try:
        height = int(input())
        return height
    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    height = read_height()


if __name__ == "__main__":
    main()
