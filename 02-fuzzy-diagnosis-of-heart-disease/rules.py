rules_list = [
    # Rule 1
    ('age_veryold', 'atypical_angina', 'output_sick4'),

    # Rule 2
    ('heartRate_high', 'age_old', 'output_sick4'),

    # Rule 3
    ('male', 'heartRate_medium', 'output_sick3'),
    # Rule 4
    ('female', 'heartRate_medium', 'output_sick2'),

    # Rule 5
    ('non_anginal_pain', 'bloodPressure_high', 'output_sick3'),
    # Rule 6
    ('typical_angina', 'heartRate_medium', 'output_sick2'),

    # Rule 7
    ('bloodSugar_veryhigh', 'age_mild', 'output_sick3'),
    # Rule 8
    ('bloodSugar_not_veryhigh', 'bloodPressure_veryhigh', 'output_sick2'),

    # Rule 9
    ('asymptomatic', 'age_veryold', 'output_sick1'),
    # Rule 10
    ('bloodPressure_high', 'heartRate_low', 'output_sick1'),
    # Rule 11
    ('typical_angina', 'output_healthy'),
    # Rule 12
    ('atypical_angina', 'output_sick1'),
    # Rule 13
    ('non_anginal_pain', 'output_sick2'),
    # Rule 14
    ('asymptomatic', 'output_sick3'),
    # Rule 15
    ('asymptomatic', 'output_sick4'),

    # Rule 16
    ('female', 'output_sick1'),
    # Rule 17
    ('male', 'output_sick2'),

    # Rule 18
    ('bloodPressure_low', 'output_healthy'),
    # Rule 19
    ('bloodPressure_medium', 'output_sick1'),
    # Rule 20
    ('bloodPressure_high', 'output_sick2'),
    # Rule 21
    ('bloodPressure_veryhigh', 'output_sick3'),
    # Rule 22
    ('bloodPressure_veryhigh', 'output_sick4'),

    # Rule 23
    ('cholesterol_low', 'output_healthy'),
    # Rule 24
    ('cholesterol_medium', 'output_sick1'),
    # Rule 25
    ('cholesterol_high', 'output_sick2'),
    # Rule 26
    ('cholesterol_high', 'output_sick3'),
    # Rule 27
    ('cholesterol_veryhigh', 'output_sick4'),

    # Rule 28
    ('bloodSugar_veryhigh', 'output_sick2'),

    # Rule 29
    ('ecg_normal', 'output_healthy'),
    # Rule 30
    ('ecg_normal', 'output_sick1'),
    # Rule 31
    ('ecg_abnormal', 'output_sick2'),
    # Rule 32
    ('ecg_hypertrophy', 'output_sick3'),
    # Rule 33
    ('ecg_hypertrophy', 'output_sick4'),

    # Rule 34
    ('heartRate_low', 'output_healthy'),
    # Rule 35
    ('heartRate_medium', 'output_sick1'),
    # Rule 36
    ('heartRate_medium', 'output_sick2'),
    # Rule 37
    ('heartRate_high', 'output_sick3'),
    # Rule 38
    ('heartRate_high', 'output_sick4'),

    # Rule 39
    ('exercise_suitable', 'output_sick2'),

    # Rule 40
    ('oldPeak_low', 'output_healthy'),
    # Rule 41
    ('oldPeak_low', 'output_sick1'),
    # Rule 42
    ('oldPeak_terrible', 'output_sick2'),
    # Rule 43
    ('oldPeak_terrible', 'output_sick3'),
    # Rule 44
    ('oldPeak_risk', 'output_sick4'),

    # Rule 45
    ('thallium_normal', 'output_healthy'),
    # Rule 46
    ('thallium_normal', 'output_sick1'),
    # Rule 47
    ('thallium_medium', 'output_sick2'),
    # Rule 48
    ('thallium_high', 'output_sick3'),
    # Rule 49
    ('thallium_high', 'output_sick4'),

    # Rule 50
    ('age_young', 'output_healthy'),
    # Rule 51
    ('age_mild', 'output_sick1'),
    # Rule 52
    ('age_old', 'output_2'),
    # Rule 53
    ('age_old', 'output_3'),
    # Rule 54
    ('age_veryold', 'output_sick4'),
]
