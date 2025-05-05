from Module24_Tasks.Task4.Task4 import *

def test_elements_mixing():
    fire = Fire()
    water = Water()
    air = Air()
    earth = Earth()
    assert (fire + water).element_type == Element_Type.STEAM 
    assert (earth + air).element_type == Element_Type.DUST 
    assert (fire + (water + air)).element_type == Element_Type.NONE 