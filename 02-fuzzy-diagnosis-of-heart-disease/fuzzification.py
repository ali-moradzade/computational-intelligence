import math


def calculate_Y(p1, p2, x):
    return ((p1[1] - p2[1]) / (p1[0] - p2[0])) * (x - p1[0]) + p1[1]


def membership(structure, x):
    x1 = structure[0]
    x2 = structure[1]
    x3 = structure[2]

    # ---\
    #     \
    if math.isinf(x1):
        if x <= x2:
            return 1
        elif x <= x3:
            return calculate_Y((x2, 1), (x3, 0), x)
        else:
            return 0

    #  /---
    # /
    elif math.isinf(x3):
        if x <= x1:
            return 0
        elif x <= x2:
            return calculate_Y((x1, 0), (x2, 1), x)
        else:
            return 1

    #  /\
    # /  \
    else:
        if x <= x1:
            return 0
        elif x <= x2:
            return calculate_Y((x1, 0), (x2, 1), x)
        elif x <= x3:
            return calculate_Y((x2, 1), (x3, 0), x)
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
    'bloodSugar_veryhigh': (105, 120, math.inf),
    'bloodSugar_not_veryhigh': (-math.inf, 105, 120)
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

ecg_location = {
    'ecg_normal': (-math.inf, 0, 0.4),
    'ecg_abnormal': (0.2, 1, 1.8),
    'ecg_hypertrophy': (1.4, 1.9, math.inf)
}

oldPeak_location = {
    'oldPeak_low': (-math.inf, 1, 2),
    'oldPeak_risk': (1.5, 2.8, 4.2),
    'oldPeak_terrible': (2.5, 4, math.inf)
}

output_sick_location = {
    'output_sick1': (-math.inf, 0.25, 1),
    'output_sick2': (0, 1, 2),
    'output_sick3': (1, 2, 3),
    'output_sick4': (2, 3, 4),
    'output_healthy': (3, 3.75, math.inf)
}


def fuzzify(input_value_dict):
    age = input_value_dict.get('age')
    bloodPressure = input_value_dict.get('blood_pressure')
    bloodSugar = input_value_dict.get('blood_sugar')
    cholesterol = input_value_dict.get('cholestrol')
    heartRate = input_value_dict.get('heart_rate')
    ecg = input_value_dict.get('ecg')
    oldPeak = input_value_dict.get('old_peak')
    chest_pain = input_value_dict.get('chest_pain')
    sex = input_value_dict.get('sex')
    thallium = input_value_dict.get('thallium_scan')
    exercise = input_value_dict.get('exercise')

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

    for k, structure in ecg_location.items():
        fuzzy_values_dict[k] = membership(structure, ecg)

    for k, structure in oldPeak_location.items():
        fuzzy_values_dict[k] = membership(structure, oldPeak)

    # Converting our crisp values to fuzzy values
    if chest_pain == 1:
        fuzzy_values_dict['typical_angina'] = 1
        fuzzy_values_dict['atypical_angina'] = 0
        fuzzy_values_dict['non_anginal_pain'] = 0
        fuzzy_values_dict['asymptomatic'] = 0
    elif chest_pain == 2:
        fuzzy_values_dict['typical_angina'] = 0
        fuzzy_values_dict['atypical_angina'] = 1
        fuzzy_values_dict['non_anginal_pain'] = 0
        fuzzy_values_dict['asymptomatic'] = 0
    elif chest_pain == 3:
        fuzzy_values_dict['typical_angina'] = 0
        fuzzy_values_dict['atypical_angina'] = 0
        fuzzy_values_dict['non_anginal_pain'] = 1
        fuzzy_values_dict['asymptomatic'] = 0
    else:
        fuzzy_values_dict['typical_angina'] = 0
        fuzzy_values_dict['atypical_angina'] = 0
        fuzzy_values_dict['non_anginal_pain'] = 0
        fuzzy_values_dict['asymptomatic'] = 1

    if sex == 0:
        fuzzy_values_dict['male'] = 1
        fuzzy_values_dict['female'] = 0
    else:
        fuzzy_values_dict['male'] = 0
        fuzzy_values_dict['female'] = 1

    if exercise == 0:
        fuzzy_values_dict['exercise_unsuitable'] = 1
        fuzzy_values_dict['exercise_suitable'] = 0
    else:
        fuzzy_values_dict['exercise_unsuitable'] = 0
        fuzzy_values_dict['exercise_suitable'] = 1

    if thallium == 3:
        fuzzy_values_dict['thallium_normal'] = 1
        fuzzy_values_dict['thallium_medium'] = 0
        fuzzy_values_dict['thallium_high'] = 0
    elif thallium == 6:
        fuzzy_values_dict['thallium_normal'] = 0
        fuzzy_values_dict['thallium_medium'] = 1
        fuzzy_values_dict['thallium_high'] = 0
    else:
        fuzzy_values_dict['thallium_normal'] = 0
        fuzzy_values_dict['thallium_medium'] = 0
        fuzzy_values_dict['thallium_high'] = 1

    return fuzzy_values_dict
