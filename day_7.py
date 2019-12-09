import itertools


class Compute:
    def __init__(self, input_val, ac_unit):
        self.input = input_val
        self.ac_unit = ac_unit
        self.ouput = []
        self._is_terminated = False
        self.codes = {'opeocode': 0, 'parameter1_mode': 0, 'parameter2_mode': 0, 'parameter3_mode': 0}
        self.cursor = 0

    def is_terminated(self):
        return self._is_terminated

    def execute(self):
        i = self.cursor
        while True:
            self.set_codes(self.input[i])
            if self.codes['opeocode'] == 99:
                self._is_terminated = True
                break
            parameter1 = self.input[i + 1] if self.codes['parameter1_mode'] == 0 else i + 1
            parameter2 = self.input[i + 2] if self.codes['parameter2_mode'] == 0 else i + 2
            if self.codes['opeocode'] == 1:
                parameter3 = self.input[i + 3] if self.codes['parameter3_mode'] == 0 else i + 3
                self.input[parameter3] = self.input[parameter1] + self.input[parameter2]
                i = i + 4
            elif self.codes['opeocode'] == 2:
                parameter3 = self.input[i + 3] if self.codes['parameter3_mode'] == 0 else i + 3
                self.input[parameter3] = self.input[parameter1] * self.input[parameter2]
                i = i + 4
            elif self.codes['opeocode'] == 3:
                if len(self.ac_unit) == 0:
                    break
                self.input[parameter1] = self.ac_unit.pop(0)
                i = i + 2
            elif self.codes['opeocode'] == 4:
                self.ouput.append(self.input[parameter1])
                i = i + 2

            # part2
            elif self.codes['opeocode'] == 5:
                if self.input[parameter1] != 0:
                    i = self.input[parameter2]
                else:
                    i += 3
            elif self.codes['opeocode'] == 6:
                if self.input[parameter1] == 0:
                    i = self.input[parameter2]
                else:
                    i += 3
            elif self.codes['opeocode'] == 7:
                parameter3 = self.input[i + 3] if self.codes['parameter3_mode'] == 0 else i + 3
                if self.input[parameter1] < self.input[parameter2]:
                    self.input[parameter3] = 1
                else:
                    self.input[parameter3] = 0
                i += 4
            elif self.codes['opeocode'] == 8:
                parameter3 = self.input[i + 3] if self.codes['parameter3_mode'] == 0 else i + 3
                if self.input[parameter1] == self.input[parameter2]:
                    self.input[parameter3] = 1
                else:
                    self.input[parameter3] = 0
                i += 4
        self.cursor = i

    def get_lats_output(self):
        return self.ouput[-1]

    def reset_codes(self):
        self.codes['opeocode'] = 0
        self.codes['parameter1_mode'] = 0
        self.codes['parameter2_mode'] = 0
        self.codes['parameter3_mode'] = 0

    def set_codes(self, num):
        self.reset_codes()
        if num == 0:
            return
        pos_nums = []
        while num != 0:
            pos_nums.append(num % 10)
            num = num // 10
        if len(pos_nums) > 1:
            opcode = int(str(pos_nums[1]) + str(pos_nums[0]))
        else:
            opcode = pos_nums[0]
        self.codes['opeocode'] = opcode
        self.codes['parameter1_mode'] = pos_nums[2] if len(pos_nums) > 2 else 0
        self.codes['parameter2_mode'] = pos_nums[3] if len(pos_nums) > 3 else 0
        self.codes['parameter3_mode'] = pos_nums[4] if len(pos_nums) > 4 else 0


def run_program(code, phase_configuration):
    input_value = 0
    for i in phase_configuration:
        amplifier = Compute(code.copy(), [i, input_value])
        amplifier.execute()
        output = amplifier.get_lats_output()
        output_value = output
        input_value = output_value

    return output_value


def run_feedback_program(code, phase_configuration):
    input_value = 0
    num_amplifiers = len(phase_configuration)

    # initialize amplifiers
    amplifiers = []
    for j in phase_configuration:
        amplifiers.append(Compute(code.copy(), [j]))

    # start first amplifier
    amplifiers[0].ac_unit.append(0)

    j = 0
    while (True):
        amplifiers[j].execute()
        output = amplifiers[j].get_lats_output()
        j = (j + 1) % num_amplifiers
        terminated = amplifiers[j].is_terminated()
        if terminated is False:
            amplifiers[j].ac_unit.append(output)
        else:
            return output


input_val = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 34, 55, 68, 93, 106, 187, 268, 349, 430, 99999, 3, 9, 102, 5, 9, 9,
             1001, 9, 2, 9, 4, 9, 99, 3, 9, 1001, 9, 5, 9, 102, 2, 9, 9, 101, 2, 9, 9, 102, 2, 9, 9, 4, 9, 99, 3, 9,
             101, 2, 9, 9, 102, 4, 9, 9, 4, 9, 99, 3, 9, 101, 4, 9, 9, 102, 3, 9, 9, 1001, 9, 2, 9, 102, 4, 9, 9, 1001,
             9, 2, 9, 4, 9, 99, 3, 9, 101, 2, 9, 9, 1002, 9, 5, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2,
             9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2,
             9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9,
             9, 4, 9, 99, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9,
             1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2,
             9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 102,
             2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101,
             1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9,
             2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9,
             1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9,
             101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 99, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9,
             1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9,
             101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9,
             1002, 9, 2, 9, 4, 9, 99]

max_output = 0
#part 1
for phase_configuration in list(itertools.permutations(range(5))):
    output = run_program(input_val, phase_configuration)
    max_output = max(output, max_output)
print("Max output:", max_output)


max_output = 0
# part 2
for phase_configuration in list(itertools.permutations(range(5, 10))):
    output = run_feedback_program(input_val, phase_configuration)
    max_output = max(output, max_output)
print("Max output:", max_output)
