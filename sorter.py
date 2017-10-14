import collections


def sorter():
    info = input("Select Target File ")
    filehandle = open(info, "r")
    characters = filehandle.read()
    char_counter = collections.Counter(characters)
    s = ""
    for readchar, count2 in char_counter.most_common():
        if (readchar.isalpha() and readchar.islower()) or readchar == '_':
            if readchar == '_':
                break
            s += readchar
    print(s)


sorter()
