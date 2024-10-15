from hstest import StageTest, CheckResult, dynamic_test, TestedProgram
from random import randint


class XMassTreeTest2(StageTest):

    @staticmethod
    def output_len_stage1(out, high):
        out_len = len(out.splitlines())
        if out_len != int(high) + 2:
            return f"Wrong tree height. Expected {int(high) + 2}, founded {out_len}."
        return

    @staticmethod
    def output_ext_stage2(out, high):
        out = out.splitlines()
        ext = [("X", 0, 0), ("^", 1, 0), ("| |", len(out) - 1, -1)]
        for item, i, correction in ext:
            out_pos = [out[i].index(item) if item in out[i] else None,
                       out[i].count(item),
                       len(out[i].strip())]
            exp_pos = [int(high - 1) + correction, 1, len(item)]
            if out_pos[0] != exp_pos[0]:
                return f"Wrong position of {item} in line {i}. Expected {exp_pos[0]}, founded {out_pos[0]}."
            if out_pos[1] != exp_pos[1]:
                return f"Wrong number of {item} in line {i}. Expected {exp_pos[1]}, founded {out_pos[1]}."
            if out_pos[2] != exp_pos[2]:
                return f"Wrong width of the tree in line {i}. " \
                       f"Expected {exp_pos[2]} chars, founded {out_pos[2]} chars."
        return

    @staticmethod
    def output_pos_stage2(out, high):
        out = out.splitlines()[2:-1]
        #  extra condition "ZONK" for empty line to return None
        out_pos = [[n.index(n.strip()) if (n.strip() or "ZONK") in n else None, n.count("*"), len(n.strip()), n.strip()] for n in out]
        exp_pos = [[int(high - n - 1), 2 * n + 1 - 2, 2 * n + 1] for n in range(1, high)]
        for i, value in enumerate(out_pos):
            if value[0] != exp_pos[i][0]:
                return f"Wrong position of line {i + 3}. Expected {exp_pos[i][0]}, founded {value[0]}."
            if value[1] != exp_pos[i][1]:
                return f"Wrong number of '*' in line {i + 3}. Expected {exp_pos[i][1]}, founded {value[1]}."
            if value[2] != exp_pos[i][2]:
                return f"Wrong width of the tree in line {i + 3}. Expected {exp_pos[i][2]} chars, founded {value[2]} chars."
            if not value[3].endswith("\\"):
                return f"Tree in line {i + 3} doesn't ends with '\\'. Expected '\\', founded {value[3][-1]}."
            if not value[3].startswith("/"):
                return f"Tree in line {i + 3} doesn't starts with '/'. Expected '/', founded {value[3][0]}."
        return

    @dynamic_test
    def test1(self):
        for _ in range(3):
            main = TestedProgram()
            main.start()
            high = str(randint(3, 30))
            output = main.execute(high)

            check = self.output_len_stage1(output, high)
            if check:
                return CheckResult.wrong(check)
            check = self.output_ext_stage2(output, int(high))
            if check:
                return CheckResult.wrong(check)
            check = self.output_pos_stage2(output, int(high))
            if check:
                return CheckResult.wrong(check)

        return CheckResult.correct()


if __name__ == '__main__':
    XMassTreeTest2().run_tests()
