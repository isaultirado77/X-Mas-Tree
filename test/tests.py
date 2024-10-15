from hstest import StageTest, CheckResult, dynamic_test, TestedProgram
from random import randint


class XMassTreeTest1(StageTest):

    @staticmethod
    def output_len_stage1(out, high):
        out_len = len(out.splitlines())
        if out_len != int(high):
            return f"Wrong tree height. Expected {high}, founded {out_len}."

    @staticmethod
    def output_stars_stage1(out, high):
        out_stars = out.count("*")
        exp_stars = sum([2 * n + 1 for n in range(int(high))])
        if out_stars != exp_stars:
            return f"Wrong number of '*'. Expected {exp_stars}, founded {out_stars}."
        return

    @staticmethod
    def output_pos_stage1(out, high):
        out = out.splitlines()
        out_pos = [[n.index("*") if "*" in n else None, n.count("*"), len(n.strip())] for n in out]
        exp_pos = [[int(high - n - 1), 2 * n + 1, 2 * n + 1] for n in range(high)]
        for i, value in enumerate(out_pos):
            if value[0] != exp_pos[i][0]:
                return f"Wrong position of '*' in line {i}. Expected {exp_pos[i][0]}, founded {value[0]}."
            if value[1] != exp_pos[i][1]:
                return f"Wrong number of '*' in line {i}. Expected {exp_pos[i][1]}, founded {value[1]}."
            if value[2] != exp_pos[i][2]:
                return f"Wrong width of the tree in line {i}. Expected {exp_pos[i][2]} chars, founded {value[2]} chars."
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
            check = self.output_pos_stage1(output, int(high))
            if check:
                return CheckResult.wrong(check)
        return CheckResult.correct()


if __name__ == '__main__':
    XMassTreeTest1().run_tests()
