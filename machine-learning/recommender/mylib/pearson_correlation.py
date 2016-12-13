from math import sqrt
def pearson_correlation(data1, data2):
    '''calculate pearson correlation from 2 data lists'''

    # pic up common data
    both_items = {}
    for item in data1:
        if item in data2:
            both_items[item] = 1

    number_of_ratings = len(both_items)

    # if no common data, return 0
    if (number_of_ratings == 0):
        return 0

    # sum common value
    sum_value1 = sum([data1[item] for item in both_items])
    sum_value2 = sum([data2[item] for item in both_items])

    # sum common squared value
    sum_squared_value1 = sum([data1[item] ** 2 for item in both_items])
    sum_squared_value2 = sum([data2[item] ** 2 for item in both_items])

    # sum product of data1 by data2
    sum_product_value = sum([data1[item] * data2[item] for item in both_items])


    # calculate pearson score
    s_xx = sum_squared_value1 - sum_value1 ** 2 / number_of_ratings
    s_yy = sum_squared_value2 - sum_value2 ** 2 / number_of_ratings
    s_xy = sum_product_value - sum_value1 * sum_value2 / number_of_ratings

    if s_xx * s_yy == 0:
        return 0
    else:
       return s_xy / sqrt(s_xx * s_yy)
