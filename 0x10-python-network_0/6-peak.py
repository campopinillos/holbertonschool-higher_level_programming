#!/usr/bin/python3
""" Function find_peak """


def find_peak(list_of_integers):
    """ Function find_peak """
    lenght = len(list_of_integers)
    if lenght == 0:
        return None
    else:
        return findPeak(list_of_integers, lenght, 0, lenght - 1)


def findPeak(array, lenght, low, high):
    """ Auxiliar function to find a peak """
    middle = int(low + (high - low)/2)
    if (array[middle - 1] <= array[middle] and
       (middle == lenght - 1 or array[middle + 1] <= array[middle])):
        return middle
    elif (middle > 0 and array[middle - 1] > array[middle]):
        return findPeak(array, low, (middle - 1), lenght)
    else:
        return findPeak(array, (middle + 1), high, lenght)
