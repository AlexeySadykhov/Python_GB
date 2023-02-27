def bubble_sort(array, reverse=False):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if not reverse:
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
            else:
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
    return array


def find_max(array):
    max_value = array[0]
    for item in array:
        if item > max_value:
            max_value = item
    return max_value
