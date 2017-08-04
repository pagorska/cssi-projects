dictionary = { ':-)': 'happy',
    ':)' : 'happy',
    ':(': 'sad',
    ':-(': 'sad'}


def uniqueValues(dict):
    allValues = list(dict.values())
    unique = []
    for i in range(allValues):
        count = 0
        value = allValues[i]
        for val in unique:
            if val == value:
                count +=1
        if (count == 0):
            unique.append(value)
    return unique

uniqueValues(dict)
