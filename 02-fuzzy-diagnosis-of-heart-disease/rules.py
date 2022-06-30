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
    ('typical_angina', 'nothing', 'output_healthy'),
    # Rule 12
    ('atypical_angina', 'nothing', 'output_sick1'),
    # Rule 13
    ('non_anginal_pain', 'nothing', 'output_sick2'),
    # Rule 14
    ('asymptomatic', 'nothing', 'output_sick3'),
    # Rule 15
    ('asymptomatic', 'nothing', 'output_sick4'),

    # Rule 16
    ('female', 'nothing', 'output_sick1'),
    # Rule 17
    ('male', 'nothing', 'output_sick2'),

    # Rule 18
    ('bloodPressure_low', 'nothing', 'output_healthy'),
    # Rule 19
    ('bloodPressure_medium', 'nothing', 'output_sick1'),
    # Rule 20
    ('bloodPressure_high', 'nothing', 'output_sick2'),
    # Rule 21
    ('bloodPressure_veryhigh', 'nothing', 'output_sick3'),
    # Rule 22
    ('bloodPressure_veryhigh', 'nothing', 'output_sick4'),

    # Rule 23
    ('cholesterol_low', 'nothing', 'output_healthy'),
    # Rule 24
    ('cholesterol_medium', 'nothing', 'output_sick1'),
    # Rule 25
    ('cholesterol_high', 'nothing', 'output_sick2'),
    # Rule 26
    ('cholesterol_high', 'nothing', 'output_sick3'),
    # Rule 27
    ('cholesterol_veryhigh', 'nothing', 'output_sick4'),

    # Rule 28
    ('bloodSugar_veryhigh', 'nothing', 'output_sick2'),

    # Rule 29
    ('ecg_normal', 'nothing', 'output_healthy'),
    # Rule 30
    ('ecg_normal', 'nothing', 'output_sick1'),
    # Rule 31
    ('ecg_abnormal', 'nothing', 'output_sick2'),
    # Rule 32
    ('ecg_hypertrophy', 'nothing', 'output_sick3'),
    # Rule 33
    ('ecg_hypertrophy', 'nothing', 'output_sick4'),

    # Rule 34
    ('heartRate_low', 'nothing', 'output_healthy'),
    # Rule 35
    ('heartRate_medium', 'nothing', 'output_sick1'),
    # Rule 36
    ('heartRate_medium', 'nothing', 'output_sick2'),
    # Rule 37
    ('heartRate_high', 'nothing', 'output_sick3'),
    # Rule 38
    ('heartRate_high', 'nothing', 'output_sick4'),


    # Rule 39
    ('exercise_suitable', 'nothing', 'output_sick2'),

    # Rule 40
    ('oldPeak_low', 'nothing', 'output_healthy'),
    # Rule 41
    ('oldPeak_low', 'nothing', 'output_sick1'),
    # Rule 42
    ('oldPeak_terrible', 'nothing', 'output_sick2'),
    # Rule 43
    ('oldPeak_terrible', 'nothing', 'output_sick3'),
    # Rule 44
    ('oldPeak_risk', 'nothing', 'output_sick4'),

    # Rule 45
    ('thallium_normal', 'nothing', 'output_healthy'),
    # Rule 46
    ('thallium_normal', 'nothing', 'output_sick1'),
    # Rule 47
    ('thallium_medium', 'nothing', 'output_sick2'),
    # Rule 48
    ('thallium_high', 'nothing', 'output_sick3'),
    # Rule 49
    ('thallium_high', 'nothing', 'output_sick4'),

    # Rule 50
    ('age_young', 'nothing', 'output_healthy'),
    # Rule 51
    ('age_mild', 'nothing', 'output_sick1'),
    # Rule 52
    ('age_old', 'nothing', 'output_2'),
    # Rule 53
    ('age_old', 'nothing', 'output_3'),
    # Rule 54
    ('age_veryold', 'nothing', 'output_sick4'),
]
