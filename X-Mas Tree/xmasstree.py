from tree import Tree
from postal import Postal


def read_inputs():
    try:
        inputs = input()
        split_inputs = inputs.split(' ')
        int_inputs = [int(x) for x in split_inputs]
        return int_inputs
    except ValueError:
        print("Error: Enter valid inputs.")


def parse_inputs(inputs: list) -> tuple:
    length = len(inputs)
    if length == 2:
        height, intervals = inputs[0], inputs[1]
        return 'tree', height, intervals
    elif length % 4 == 0:
        total_args = int(length / 4)
        args = []
        for i in range(0, length, 4):
            args.append(tuple(inputs[i:i + 4]))
        return 'postal', args
    else:
        raise ValueError("Error: Invalid set of inputs.")


def handle_tree_creation(height, intervals):
    tree = Tree.get_tree(height, intervals)
    return tree


def handle_postal_creation(args):
    postal = Postal()
    for arg in args:
        H, I, L, C = arg
        tree = Tree.get_tree(H, I)
        postal.place_tree(tree, L, C)
    return postal


def handle_inputs(inputs: list):
    try:
        parsed_data = parse_inputs(inputs)
        if parsed_data[0] == 'tree':
            _, height, intervals = parsed_data
            return handle_tree_creation(height, intervals)
        elif parsed_data[0] == 'postal':
            _, args = parsed_data
            return handle_postal_creation(args)
    except ValueError as e:
        print(str(e))


def main():
    inputs = read_inputs()
    grid = handle_inputs(inputs)
    grid.display()


if __name__ == "__main__":
    main()
