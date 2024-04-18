def long_word(a) :
    words = a.split()
    word = max(words, key=len)
    return word, len(word)


b = input("Введите строку с произвольными словами и количество пробелов: \n")
word, lenght = long_word(b)
print(f"Самое длинное слово: {word}, его длина составляет: {lenght} символов.")
