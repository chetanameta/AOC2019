import pandas as pd
from itertools import combinations


class Space:
    def __init__(self, coordinates, steps=0, check_first_position=False):
        self.coordinates = self._get_cordinates(coordinates)
        self.first_coordinates = self._get_cordinates(coordinates)
        self.steps = steps
        self.moons = coordinates.keys()
        self.axis = list(self.coordinates.keys())
        self.check_first_position = check_first_position
        self.counter = 0

    def _get_cordinates(self, dic):
        return pd.DataFrame.from_dict(
            {(i, j): dic[i][j]
             for i in dic.keys()
             for j in dic[i].keys()},
            orient='index'
        )

    def run(self):
        print(self.coordinates)
        combination = self._get_combinations()
        while True:
            for moon1, moon2 in combination:
                self._time_step(moon1, moon2)
            self._change_position()
            if self.check_first_position is True:
                self.counter += 1
                if self.coordinates.equals(self.first_coordinates):
                    break
            else:
                self.counter += 1
                if self.counter == self.steps:
                    break
            print(self.counter)

        print(self.coordinates)

    def get_total_steps(self):
        return self.counter

    def _time_step(self, moon1, moon2):
        self.change_valocity(moon1, moon2)

    def _get_combinations(self):
        return list(combinations(self.moons, 2))

    def change_valocity(self, moon1, moon2):
        for i in self.axis:
            if self.coordinates[i][moon1]['position'] == self.coordinates[i][moon2]['position']:
                moon1_move = 0
            else:
                moon1_move = 1 if self.coordinates[i][moon1]['position'] < self.coordinates[i][moon2][
                    'position'] else -1
            moon2_move = -1 * moon1_move
            self.coordinates.loc[moon1, 'velocity'][i] = self.coordinates[i][moon1]['velocity'] + moon1_move
            self.coordinates.loc[moon2, 'velocity'][i] = self.coordinates[i][moon2]['velocity'] + moon2_move

    def _change_position(self):
        for moon in self.moons:
            self.coordinates.loc[moon, 'position'] = self.coordinates.loc[moon, 'velocity'] + self.coordinates.loc[
                moon, 'position']

    def _set_energies(self):
        self.coordinates['energy'] = self.coordinates[self.axis].abs().sum(axis=1)

    def get_total_energy(self):
        self._set_energies()
        total_energy = 0
        for moon in self.moons:
            kinetic_energy = self.coordinates['energy'][moon]['velocity']
            potential_energy = self.coordinates['energy'][moon]['position']
            total_energy += kinetic_energy * potential_energy
        return total_energy


# main
dic = {
    'io': {
        'position': {'x': -10, 'y': -10, 'z': -13},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'europa': {
        'position': {'x': 5, 'y': 5, 'z': -9},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'ganymede': {
        'position': {'x': 3, 'y': 8, 'z': -16},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'callisto': {
        'position': {'x': 1, 'y': 3, 'z': -3},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    }
}

# other
dic_test = {
    'io': {
        'position': {'x': -1, 'y': 0, 'z': 2},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'europa': {
        'position': {'x': 2, 'y': -10, 'z': -7},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'ganymede': {
        'position': {'x': 4, 'y': -8, 'z': 8},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    },
    'callisto': {
        'position': {'x': 3, 'y': 5, 'z': -1},
        'velocity': {'x': 0, 'y': 0, 'z': 0}
    }
}

obj = Space(dic, steps=0, check_first_position=True)

obj.run()

# part 1
# print(obj.get_total_energy())
print(obj.get_total_steps())
