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
   