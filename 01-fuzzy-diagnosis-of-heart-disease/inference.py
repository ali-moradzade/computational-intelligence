import rules


def inference(fuzzy_values_dict):
    fuzzy_output_values = {}

    for rule in rules.rules_list:
        item1 = fuzzy_values_dict[rule[0]]

        if rule[1] == 'nothing':
            item2 = 1
        else:
            item2 = fuzzy_values_dict[rule[1]]

        output = rule[2]

        if fuzzy_output_values.get(output) is None:
            fuzzy_output_values[output] = min(item1, item2)

        else:
            if fuzzy_output_values[output] < min(item1, item2):
                fuzzy_output_values[output] = min(item1, item2)

    return fuzzy_output_values
