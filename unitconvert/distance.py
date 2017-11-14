"""
A python module for conversion between miles and kilometers
"""
import numpy as np

def miles_to_kilometers(dm):
    """Convert miles to kilometers.

    PARAMETERS
    ----------
    dm : float
        distance in miles

    RETURNS
    -------
    dk: float
        distance in kilometers
    """

    dk = dm * 1.609344

    return dk


def kilometers_to_miles(dk):
    """Convert kilometers to miles.

    PARAMETERS
    ----------
    dk: float
        distance in kilometers

    RETURNS
    -------
    dm : float
        distance in miles
    """

    dm = dk * 0.62137119224

    return dm