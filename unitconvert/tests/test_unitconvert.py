import numpy as np
import pytest

from unitconvert.temperature import fahrenheit_to_celsius, celsius_to_fahrenheit
from unitconvert.distance import miles_to_kilometers,kilometers_to_miles

def test_unitconvert():
    # some known results
    assert fahrenheit_to_celsius(32.0) == 0
    assert celsius_to_fahrenheit(-32.0* 5.0/9.0) == 0

    # check temperature when fahrenheit equals to celsius
    Tf=-40.0
    Tc=-40.0
    Tc_test = fahrenheit_to_celsius(Tf)
    Tf_test = celsius_to_fahrenheit(Tc)
    
    
    dm=2
    dk=100
    dk_test=miles_to_kilometers(dm)
    dm_test=kilometers_to_miles(dk)

    # an approximate version of the above
    np.testing.assert_allclose(Tc_test,Tf_test, rtol=1e-5)
    
    np.testing.assert_allclose(dk_test,3.218688 , rtol=1e-5)
    np.testing.assert_allclose(dm_test, 62.137119224, rtol=1e-5)

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2, 3, 4)
    with pytest.raises(TypeError):   
        celsius_to_fahrenheit(1, 2)
    with pytest.raises(TypeError):   
        miles_to_kilometers(1, 2)
    with pytest.raises(TypeError):   
        kilometers_to_miles(1, 2)