import pandas as pd
import copy
import numpy as np
from itertools import combinations


class Space:
    def __init__(self, coordinates, steps=0):
        self.coordinates = coordinates
        self.first_coordinates = copy.deepcopy(coordinates)
        self.steps = steps
        self.moons = list(coordinates.keys())
        self.axis = list(self.coordinates[self.moons[0]]['position'].keys())
        self.counter = 0
        self.roundtrip = {'x': 0, 'y': 0, 'z': 0}
        self.total_energy = 0

    def _get_cordinates(self, dic):
        return pd.DataFrame.from_dict(
            {(i, j): dic[i][j]
             for i in dic.keys()
             for j in dic[i].keys()},
            orient='index'
        )

    def _get_divident(self, n1, n2):
        r = 1
        while r > 0:
            r = n1 % n2
            n1 = n2
            n2 = r
        return n1

    def _time_step(self, moon1, moon2):
        self._change_valocity(moon1, moon2)

    def _get_combinations(self):
        return list(combinations(self.moons, 2))

    def _change_valocity(self, moon1, moon2):

        for i in self.axis:
            if self.coordinates[moon1]['position'][i] == self.coordinates[moon2]['position'][i]:
                moon1_move = 0
            else:
                moon1_move = 1 if self.coordinates[moon1]['position'][i] < self.coordinates[moon2][
                    'position'][i] else -1
            moon2_move = -1 * moon1_move
            self.coordinates[moon1]['velocity'][i] += moon1_move
            self.coordinates[moon2]['velocity'][i] += moon2_move

    def _change_position(self):
        for moon in self.moons:
            for i in self.axis:
                self.coordinates[moon]['position'][i] += self.coordinates[moon]['velocity'][i]

    def _set_energies(self):
        coordinates = self._get_cordinates(self.coordinates)
        coordinates['energy'] = coordinates[self.axis].abs().sum(axis=1)
        total_energy = 0
        for moon in self.moons:
            kinetic_energy = coordinates['energy'][moon]['velocity']
            potential_energy = coordinates['energy'][moon]['position']
            total_energy += kinetic_energy * potential_energy
        self.total_energy = total_energy

    def run(self):
        combination = self._get_combinations()
        while True:
            self.counter += 1
            for moon1, moon2 in combination:
                self._time_step(moon1, moon2)
            self._change_position()
            for dim in self.axis:
                if self.roundtrip[dim] == 0:
                    repeat = 0
                    for moon in self.moons:
                        if self.coordinates[moon]['velocity'][dim] == 0 and self.coordinates[moon]['position'][dim] == \
                                self.first_coordinates[moon]['position'][dim]:
                            repeat += 1
                    if repeat == len(self.moons):
                        self.roundtrip[dim] = self.counter

            if self.counter > self.steps and 0 not in list(self.roundtrip.values()):
                break
            if self.counter == self.steps:
                self._set_energies()

    def get_total_energy(self):
        return self.total_energy

    def get_total_steps_roundtrip(self):
        return (self.roundtrip['x'] / self._get_divident(self.roundtrip['x'], self.roundtrip['y'])) * \
               (self.roundtrip['y'] / self._get_divident(self.roundtrip['x'], self.roundtrip['z'])) * \
               (self.roundtrip['z'] / self._get_divident(self.roundtrip['z'], self.roundtrip['y'])) * 2


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


obj = Space(dic, steps=1000)

obj.run()

# part 1
print("Total Energy: ", str(obj.get_total_energy()))
print("History repeats itself after steps: ", str(obj.get_total_steps_roundtrip()))
