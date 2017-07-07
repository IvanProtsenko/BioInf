def sort(string):
    array = []
    array = string.split(", ")
    array.sort()
    string = str(", ".join(array))
    return string
