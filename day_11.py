from computer import Computer


class Panel:
    def __init__(self, code):
        self.computer = Computer(code, [])
        self.panel = {}
        self.degree = 0
        self.x = 0
        self.y = 0
        self.minx = 0
        self.maxx = 0
        self.miny = 0
        self.maxy = 0

    def set_panel_value(self, value):
        self.panel[(self.x, self.y)] = value

    def execute(self):
        while not self.computer.has_terminated():
            inputval = self.get_panel_color(self.x, self.y)

            self.computer.program_output = []
            self.computer.provide_input(inputval)
            self.computer.run()
            result = self.computer.get_whole_output()
            value = result[0]
            direction = result[1]
            self.set_panel_value(value)
            self.turn(direction)
            self.move_to_next_panel()

    def get_panel_count(self):
        return len(self.panel)

    def turn(self, direction):
        if direction == 0:
            self.degree = (self.degree + 270) % 360
        else:
            self.degree = (self.degree + 90) % 360

    def move_to_next_panel(self):
        if self.degree == 0:
            self.y -= 1
        if self.degree == 90:
            self.x += 1
        if self.degree == 180:
            self.y += 1
        if self.degree == 270:
            self.x -= 1

        self.minx = min(self.minx, self.x)
        self.maxx = max(self.maxx, self.x)
        self.miny = min(self.miny, self.y)
        self.maxy = max(self.maxy, self.y)

    def get_panel_color(self, x, y):
        return 0 if (x, y) not in self.panel else self.panel[(x, y)]

    def print(self):
        for y in range(self.miny, self.maxy + 1):
            panel_color = ""
            for x in range(self.minx, self.maxx + 1):
                panel_color += ' ' if self.get_panel_color(x, y) == 0 else '#'
            print(panel_color)


code = [3, 8, 1005, 8, 350, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8,
        1, 10, 4, 10, 102, 1, 8, 29, 1006, 0, 82, 1006, 0, 40, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0,
        10, 4, 10, 1002, 8, 1, 57, 1, 102, 15, 10, 1, 1005, 14, 10, 1006, 0, 33, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10,
        4, 10, 1008, 8, 0, 10, 4, 10, 102, 1, 8, 90, 1, 1008, 14, 10, 2, 3, 19, 10, 1006, 0, 35, 1006, 0, 21, 3, 8, 102,
        -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 1002, 8, 1, 125, 1, 1105, 11, 10, 2, 1105, 9, 10, 1, 4,
        1, 10, 2, 1, 4, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 101, 0, 8, 164, 1006,
        0, 71, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 0, 10, 4, 10, 1002, 8, 1, 189, 1006, 0, 2, 1, 5,
        17, 10, 1006, 0, 76, 1, 1002, 7, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 1001,
        8, 0, 224, 1, 3, 5, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 250, 1,
        1, 20, 10, 1, 102, 13, 10, 2, 101, 18, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10,
        102, 1, 8, 284, 2, 105, 0, 10, 1, 105, 20, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 1008, 8, 1, 10, 4,
        10, 1002, 8, 1, 315, 1006, 0, 88, 1, 2, 4, 10, 2, 8, 17, 10, 2, 6, 2, 10, 101, 1, 9, 9, 1007, 9, 1056, 10, 1005,
        10, 15, 99, 109, 672, 104, 0, 104, 1, 21102, 1, 847069688728, 1, 21101, 0, 367, 0, 1106, 0, 471, 21102,
        386577216404, 1, 1, 21102, 378, 1, 0, 1105, 1, 471, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0,
        104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 21101, 97952923867, 0, 1, 21102,
        425, 1, 0, 1106, 0, 471, 21101, 0, 29033143319, 1, 21102, 436, 1, 0, 1105, 1, 471, 3, 10, 104, 0, 104, 0, 3, 10,
        104, 0, 104, 0, 21102, 1, 868410614628, 1, 21101, 0, 459, 0, 1105, 1, 471, 21101, 837896909672, 0, 1, 21101, 0,
        470, 0, 1105, 1, 471, 99, 109, 2, 22102, 1, -1, 1, 21101, 40, 0, 2, 21102, 502, 1, 3, 21102, 492, 1, 0, 1106, 0,
        535, 109, -2, 2105, 1, 0, 0, 1, 0, 0, 1, 109, 2, 3, 10, 204, -1, 1001, 497, 498, 513, 4, 0, 1001, 497, 1, 497,
        108, 4, 497, 10, 1006, 10, 529, 1102, 1, 0, 497, 109, -2, 2105, 1, 0, 0, 109, 4, 2101, 0, -1, 534, 1207, -3, 0,
        10, 1006, 10, 552, 21101, 0, 0, -3, 22101, 0, -3, 1, 22101, 0, -2, 2, 21102, 1, 1, 3, 21101, 571, 0, 0, 1106, 0,
        576, 109, -4, 2106, 0, 0, 109, 5, 1207, -3, 1, 10, 1006, 10, 599, 2207, -4, -2, 10, 1006, 10, 599, 21202, -4, 1,
        -4, 1105, 1, 667, 21202, -4, 1, 1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21102, 1, 618, 0, 1106, 0, 576, 21201, 1,
        0, -4, 21101, 0, 1, -1, 2207, -4, -2, 10, 1006, 10, 637, 21102, 0, 1, -1, 22202, -2, -1, -2, 2107, 0, -3, 10,
        1006, 10, 659, 21202, -1, 1, 1, 21101, 659, 0, 0, 106, 0, 534, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5,
        2105, 1, 0]

# Part 1
obj = Panel(code)
obj.execute()
print("Total panel Painted: " + str(obj.get_panel_count()))

# part 2
obj = Panel(code)
obj.set_panel_value(1)
obj.execute()
obj.print()
