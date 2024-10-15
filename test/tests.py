from hstest import StageTest, CheckResult, dynamic_test, TestedProgram
from random import randint


class XMassTreeTest3(StageTest):

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
    def output_pos_stage3(out, high, inter):
        out = out.splitlines()[2:-1]
        #  extra condition "ZONK" for empty line to return None
        out_pos = [[n.index(n.strip()) if (n.strip() or "ZONK") in n else None, n.count("*"), len(n.strip()), n.strip()]
                   for n in out]
        exp_pos = [[int(high - n - 1), 2 * n + 1 - 2, 2 * n + 1] for n in range(1, high)]
        for i, value in enumerate(out_pos):
            if value[0] != exp_pos[i][0]:
                return f"Wrong position of line {i + 3}. Expected {exp_pos[i][0]}, founded {value[0]}."
            if value[2] != exp_pos[i][2]:
                return f"Wrong width of the tree in line {i + 3}. Expected {exp_pos[i][2]} chars, founded {value[2]} chars."
            if not value[3].endswith("\\"):
                return f"Tree in line {i + 3} doesn't ends with '\\'. Expected '\\', founded {value[3][-1]}."
            if not value[3].startswith("/"):
                return f"Tree in line {i + 3} doesn't starts with '/'. Expected '/', founded {value[3][0]}."

        #  checking Christmas balls
        star_line = [[(o.strip().strip("/")).strip("\\")[:-1], (o.strip().strip("/")).strip("\\")[-1]] for o in out[1:]]
        balls_line = ''.join(n[0] for n in star_line)
        max_balls = sum(range(1, len(star_line) + 1))
        nr_balls = ((max_balls - 1) // inter) + 1
        if balls_line.count("O") != nr_balls:
            return f"Wrong number of Christmas balls 'O'. Expected {nr_balls}, founded {balls_line.count('O')}."
        balls_pos = [2 * n + 1 for n in range(0, max_balls, inter)]
        for i in balls_pos:
            if balls_line[i] != "O":
                return f"The ball #{i} is not on correct position."

        #  checking nr of stars
        right_line = ''.join(n[1] for n in star_line)
        stars_max = len(balls_line) + len(right_line) - nr_balls
        nr_stars = right_line.count("*") + balls_line.count("*")
        if stars_max != nr_stars:
            return f"Wrong number of stars '*'. Expected {stars_max}, founded {nr_stars}."

        return

    @dynamic_test
    def test1(self):
        for _ in range(3):
            main = TestedProgram()
            main.start()
            high = str(randint(3, 30))
            interval = str(randint(1, 9))
            output = main.execute(f"{high} {interval}")
            check = self.output_len_stage1(output, high)
            if check:
                return CheckResult.wrong(check)
            check = self.output_ext_stage2(output, int(high))
            if check:
                return CheckResult.wrong(check)
            check = self.output_pos_stage3(output, int(high), int(interval))
            if check:
                return CheckResult.wrong(check)

        return CheckResult.correct()


if __name__ == "__main__":
    XMassTreeTest3().run_tests()
