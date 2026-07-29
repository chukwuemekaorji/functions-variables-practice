def mostfrequent(list):
    frequency = {}
    for item in list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mostfrequent(list))