#!/usr/bin/python3
""" Function find_peak """


def find_peak(list_of_integers):
    """ Function find_peak """
    if len(list_of_integers) == 0:
        return None
    else:
        peak = list_of_integers[0]
        for integer in list_of_integers:
            peak = integer if integer > peak else peak
        return peak
