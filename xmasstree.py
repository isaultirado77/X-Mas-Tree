# X-Mas Tree Project

def make_tree(height: int) -> None:
    space = ' '
    star = '*'
    for i in range(height):
        stars = star * (2 * i + 1)
        spaces = space * (height - i - 1)
        print(spaces + stars)


def read_height() -> int:
    try:
        height = int(input())
        return height
    except ValueError:
        print("Error: Enter a number.")
        return -1


def main():
    height = read_height()
    make_tree(height)

if __name__ == "__main__":
    main()
