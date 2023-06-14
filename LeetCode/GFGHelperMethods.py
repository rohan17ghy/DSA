#Converting a string representation of array to an array
#Eg: "5 2 -6 10" to [5, 2, -6, 10]
def convertStringToArray(str):
    return list(map(lambda num : int(num), str.split(' ')))