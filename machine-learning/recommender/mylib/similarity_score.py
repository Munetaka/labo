from math import sqrt
def similarity_score(data1, data2):
    '''return euclidean distance from two data lists'''

    # pick up common data
    both_items = {}
    for item in data1:
        if item in data2:
            both_items[item] = 1

    # if no common data, return 0
    if len(both_items) == 0:
        return 0


    sum_of_euclidean_distance = []
    for item in data1:
        if item in data2:
            distance = (data1[item] - data2[item]) ** 2
            sum_of_euclidean_distance.append(distance)

    total_of_eclidean_distance = sum(sum_of_euclidean_distance)

    return 1 / (1 + sqrt(total_of_eclidean_distance))
