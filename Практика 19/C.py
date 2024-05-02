def roman(s):
    roman_num = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
    result = 0
    prev_val = 0

    for char in s:
        val = roman_num[char]
        if val > prev_val:
            result += val - 2 * prev_val
        else:
            result += val
        prev_val = val

    return result


def replace(input_str):
    import re
    pattern = r"[IVXLCDM]+"
    replace_string = re.sub(pattern, lambda x: str(roman(x.group())), input_str)
    return replace_string


input_str = input()
output_str = replace(input_str)
print(output_str)
