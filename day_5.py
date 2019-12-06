class Day5:
    def __init__(self, input_val, ac_unit):
        self.input = input_val
        self.ac_unit = ac_unit
        self.ouput = []
        self.codes = {'opeocode': 0, 'parameter1_mode': 0, 'parameter2_mode': 0, 'parameter3_mode': 0}

    def get_output(self):
        i = 0
        while True:
            self.set_codes(self.input[i])
            if self.codes['opeocode'] == 99:
                break
            parameter1 = self.input[i + 1] if self.codes['parameter1_mode'] == 0 else i + 1
            parameter2 = self.input[i + 2] if self.codes['parameter2_mode'] == 0 else i + 2
            parameter3 = self.input[i + 3] if self.codes['parameter3_mode'] == 0 else i + 3

            if self.codes['opeocode'] == 1:
                self.input[parameter3] = self.input[parameter1] + self.input[parameter2]
                i = i + 4
            elif self.codes['opeocode'] == 2:
                self.input[parameter3] = self.input[parameter1] * self.input[parameter2]
                i = i + 4
            elif self.codes['opeocode'] == 3:
                self.input[parameter1] = self.ac_unit
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
                if self.input[parameter1] < self.input[parameter2]:
                    self.input[parameter3] = 1
                else:
                    self.input[parameter3] = 0
                i += 4
            elif self.codes['opeocode'] == 8:
                if self.input[parameter1] == self.input[parameter2]:
                    self.input[parameter3] = 1
                else:
                    self.input[parameter3] = 0
                i += 4

        return self.ouput

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


input_val = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1101, 32, 43, 225, 101, 68, 192, 224, 1001, 224, -160,
             224, 4, 224, 102, 8, 223, 223, 1001, 224, 2, 224, 1, 223, 224, 223, 1001, 118, 77, 224, 1001, 224, -87,
             224, 4, 224, 102, 8, 223, 223, 1001, 224, 6, 224, 1, 223, 224, 223, 1102, 5, 19, 225, 1102, 74, 50, 224,
             101, -3700, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 1, 224, 1, 223, 224, 223, 1102, 89, 18, 225,
             1002, 14, 72, 224, 1001, 224, -3096, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 223, 224, 223,
             1101, 34, 53, 225, 1102, 54, 10, 225, 1, 113, 61, 224, 101, -39, 224, 224, 4, 224, 102, 8, 223, 223, 101,
             2, 224, 224, 1, 223, 224, 223, 1101, 31, 61, 224, 101, -92, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224,
             4, 224, 1, 223, 224, 223, 1102, 75, 18, 225, 102, 48, 87, 224, 101, -4272, 224, 224, 4, 224, 102, 8, 223,
             223, 1001, 224, 7, 224, 1, 224, 223, 223, 1101, 23, 92, 225, 2, 165, 218, 224, 101, -3675, 224, 224, 4,
             224, 1002, 223, 8, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1102, 8, 49, 225, 4, 223, 99, 0, 0, 0, 677, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0,
             256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105,
             1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106,
             0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107, 226, 226, 224,
             1002, 223, 2, 223, 1005, 224, 329, 1001, 223, 1, 223, 1007, 677, 226, 224, 1002, 223, 2, 223, 1006, 224,
             344, 1001, 223, 1, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 359, 1001, 223, 1, 223, 7, 226,
             226, 224, 1002, 223, 2, 223, 1005, 224, 374, 101, 1, 223, 223, 107, 677, 677, 224, 1002, 223, 2, 223, 1006,
             224, 389, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 404, 1001, 223, 1, 223,
             1107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 419, 1001, 223, 1, 223, 108, 226, 226, 224, 102, 2, 223,
             223, 1006, 224, 434, 1001, 223, 1, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 449, 1001, 223,
             1, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 464, 1001, 223, 1, 223, 107, 226, 226, 224, 102,
             2, 223, 223, 1006, 224, 479, 1001, 223, 1, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 101,
             1, 223, 223, 7, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 509, 101, 1, 223, 223, 8, 226, 677, 224, 1002,
             223, 2, 223, 1006, 224, 524, 1001, 223, 1, 223, 1007, 226, 226, 224, 1002, 223, 2, 223, 1006, 224, 539,
             101, 1, 223, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006, 224, 554, 101, 1, 223, 223, 1108, 677, 677,
             224, 102, 2, 223, 223, 1006, 224, 569, 101, 1, 223, 223, 1107, 226, 677, 224, 102, 2, 223, 223, 1005, 224,
             584, 1001, 223, 1, 223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 599, 101, 1, 223, 223, 1008, 677,
             226, 224, 102, 2, 223, 223, 1006, 224, 614, 1001, 223, 1, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1005,
             224, 629, 101, 1, 223, 223, 107, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 644, 101, 1, 223, 223, 8, 677,
             677, 224, 102, 2, 223, 223, 1005, 224, 659, 1001, 223, 1, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005,
             224, 674, 101, 1, 223, 223, 4, 223, 99, 226]

# part 1
# obj = Day5(input_val, 1)

# part 2
obj = Day5(input_val, 5)

print(obj.get_output())
