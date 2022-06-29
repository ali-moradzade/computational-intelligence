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
            input_dict[k] = int(v)

        fuzzy_values = fuzzify(input_dict)
        fuzzy_output_value = inference(fuzzy_values)
        sickness = defuzzifier(fuzzy_output_value)

        return str(sickness)
