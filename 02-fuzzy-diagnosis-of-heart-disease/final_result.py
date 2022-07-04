from fuzzification import fuzzify
from inference import inference
from defuzzification import defuzzifier


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        # Converting all string values to int
        for k, v in input_dict.items():
            input_dict[k] = float(v)

        fuzzy_values = fuzzify(input_dict)
        fuzzy_output_value = inference(fuzzy_values)
        sickness = defuzzifier(fuzzy_output_value)

        result = ''
        if sickness < 1.78:
            result = 'healthy'

        if 1 <= sickness <= 2.51:
            if result == '':
                result = 'sick1'
            else:
                result = result + " & sick1"
        if 1.78 <= sickness <= 3.25:
            if result == '':
                result = 'sick2'
            else:
                result = result + " & sick2"
        if 1.5 <= sickness <= 4.5:
            if result == '':
                result = 'sick3'
            else:
                result = result + " & sick3"
        if 3.25 < sickness:
            if result == '':
                result = 'sick4'
            else:
                result = result + " & sick4"

        return '{}: {}'.format(result, round(sickness, 2))
