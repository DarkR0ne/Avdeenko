def encode_str(s):
    encoded_str = ""
    count = 1

    for i in range(len(s)):
        if i != len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            encoded_str += s[i] + str(count)
            count = 1

    return encoded_str


input_str = input("Введите строку: ")
encoded_str = encode_str(input_str)
print("Закодированная строка:", encoded_str)
