"""
A python module for conversion between fahrenheit and celsius
"""
import numpy as np

def fahrenheit_to_celsius(Tf):
    """Convert fahrenheit to celsius.

    PARAMETERS
    ----------
    Tf : float
        temperature in fahrenheit

    RETURNS
    -------
    Tc: float
        temperature in celcius 
    """

    Tc = ( Tf - 32.0) * (5.0 / 9.0)

    return Tc


def celsius_to_fahrenheit(Tc):
    """Convert celsius to fahrenheit.

    PARAMETERS
    ----------
    Tc : float
        temperature in celcius

    RETURNS
    -------
    Tf: float
        temperature in fahrenheit
    """

    Tf = Tc * (9.0 / 5.0) + 32.0

    return Tf