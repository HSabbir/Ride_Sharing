

def assignDriverToRider(start, driver):  # start is a list with 2 values , driver is drivers list
    mini = 9e7
    iter = 0
    index = 0

    for d in driver:
        dist = ((start[0] - d[0]) ** 2 + (start[1] - d[1]) ** 2) ** .5
        if dist < mini:
            index = iter

    return index