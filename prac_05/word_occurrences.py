def main():
    phrase = {}
    string = input("Enter a string: ").lower()
    separate = string.split()
    for word in separate:
        frequency = phrase.get(word, 0)
        phrase[word] = frequency + 1

    words = list(phrase.keys())
    words.sort()
    max_length = max((len(word) for word in words))
    for word in words:
        print("{:{}} : {}".format(word, max_length, phrase[word]))


main()
