from fuzzification import output_sick_location
from fuzzification import membership

import numpy as np


def calculate_point_value(x, fuzzy_output_values)
    value = 0
    for k, structure in output_sick_location.items():
        x0 = structure[0]
        x2 = structure[2]

        if x0 <= x <= x2:
            temp = membership(structure, x)

            if temp > fuzzy_output_values.get(k):
                temp = fuzzy_output_values.get(k)
            else:
                value = temp

    return value


def calculate_center_of_gravity(point_values_dict, step):
    sum_up = 0
    sum_down = 0

    for x, fx in point_values_dict.items():
        sum_up += x * fx * step
        sum_down += fx * step

    if sum_down != 0:
        return sum_up / sum_down
    else:
        return 0


def defuzzifier(fuzzy_output_values):
    point_values_dict = {}
    step = 0.1

    for x in np.arange(-1, 5, step):
        fx = calculate_point_value(x, output_sick_location, fuzzy_output_values)
        point_values_dict[x] = fx

    return calculate_center_of_gravity(point_values_dict, step)
