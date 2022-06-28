import math
from fuzzy.storage.fcl.Reader import Reader


def calculate_Y(p1, p2, x):
    return ((p1[1] - p2[1]) / (p1[0] - p2[0])) * (x - p1[0]) + p1[1]


def membership(structure, point):
    p1 = structure[0]
    p2 = structure[1]
    p3 = structure[2]

    x = point[0]
    y = point[1]

    # ---\
    #     \
    if math.isinf(p1[0])
        if x <= p2[0]:
            return 1
        elif x <= p3[0]:
            return calculate_Y(p2, p3, x)
        else:
            return 0

    #  /---
    # /
    elif math.isinf(p3[0]):
        if x <= p1[0]:
            return 0
        elif x <= p2[0]:
            return calculate_Y(p1, p2, x)
        else:
            return 1

    #  /\
    # /  \
    else:
        if x <= p1[0]:
            return 0
        elif x <= p2[0]:
            return calculate_Y(p1, p2, x)
        elif x <= p3[0]:
            return calculate_Y(p2, p3, x)
        else:
            return 0


age_location = {
    'age_young': (-math.inf, 29, 38),
    'age_mild': (33, 38, 45),
    'age_old': (40, 48, 58),
    'age_veryold': (52, 60, math.inf)
}

bloodPressure_location = {
    'bloodPressure_low': (-math.inf, 111, 134),
    'bloodPressure_medium': (127, 139, 153),
    'bloodPressure_high': (142, 157, 172),
    'bloodPressure_veryhigh': (154, 171, math.inf)
}

bloodSugar_location = {
    'bloodSugar_veryhigh': (105, 120, math.inf)
}

cholesterol_location = {
    'cholesterol_low': (-math.inf, 151, 197),
    'cholesterol_medium': (188, 215, 250),
    'cholesterol_high': (217, 263, 307),
    'cholesterol_veryhigh': (281, 347, math.inf)
}

heartRate_location = {
    'heartRate_low': (-math.inf, 100, 141),
    'heartRate_medium': (11, 152, 194),
    'heartRate_high': (152, 210, math.inf)
}

system = Reader().load_from_file('rules.fcl')


def fuzzify(input_value_dict):
    age = input_value_dict.get('age')
    bloodPressure = input_value_dict.get('bloodPressure')
    bloodSugar = input_value_dict.get('bloodSugar')
    cholesterol = input_value_dict.get('cholesterol')
    heartRate = input_value_dict.get('heartRate')
    sex = input_value_dict.get('sex')

    fuzzy_values_dict = {}

    for k, structure in age_location.items():
        fuzzy_values_dict[k] = membership(structure, age)

    for k, structure in bloodPressure_location.items():
        fuzzy_values_dict[k] = membership(structure, bloodPressure)

    for k, structure in bloodSugar_location.items():
        fuzzy_values_dict[k] = membership(structure, bloodSugar)

    for k, structure in cholesterol_location.items():
        fuzzy_values_dict[k] = membership(structure, cholesterol)

    for k, structure in heartRate_location.items():
        fuzzy_values_dict[k] = membership(structure, heartRate)

    if sex == 0:
        fuzzy_values_dict['male'] = 1
        fuzzy_values_dict['female'] = 0
    else:
        fuzzy_values_dict['male'] = 0
        fuzzy_values_dict['female'] = 1

    return fuzzy_values_dict
