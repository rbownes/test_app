import random
import operator


class add_problem:
    def __init__(self, scale):
        self.scale = scale
        self.num_list = [i for i in range(10 * self.scale + 1) if i > 0]
        self.q_list = ["Arithmatic", "Operator"]
        self.ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        self.translate_op = {
            "+": "Addition",
            "-": "Subtraction",
            "*": "Multiplication",
            "/": "Division",
        }

    def create_random_problem(self):
        question_seed = random.choice(self.q_list)
        x = random.choice(self.num_list[len(self.num_list) // 2 :])
        y = random.choice(self.num_list[: len(self.num_list) // 2])

        if question_seed == "Operator":
            op = random.choice(list(self.ops.keys()))
            answer = self.ops.get(op)(x, y)
            question = f"{x} __ {y} = {answer}"

            return op, question, question_seed
        else:
            op = random.choice(list(self.ops.keys()))
            answer = self.ops.get(op)(x, y)
            question = f"{x} {op} {y} == __"
            qType = self.translate_op.get(op)

            return answer, question, qType

    def create_arithmatic_problem(self, use_case: str):
        x = random.choice(self.num_list[len(self.num_list) // 2 :])
        y = random.choice(self.num_list[: len(self.num_list) // 2])

        if use_case == "Operator":
            op = random.choice(list(self.ops.keys()))
            answer = self.ops.get(op)(x, y)
            question = f"{x} __ {y} = {answer}"

            return op, question, "Operator"

        else:
            answer = self.ops.get(use_case)(x, y)
            question = f"{x} {use_case} {y} = __"
            qType = self.translate_op.get(use_case)

            return answer, question, qType
