import enum

class Element_Type(enum.Enum):
    NONE = 0
    FIRE = 1
    EARTH = 2
    AIR = 3
    WATER = 4
    STORM = 5
    LAVA = 6
    THUNDER = 7
    STEAM = 8
    DIRT = 9
    DUST = 10
    HELLFIRE = 11
    WIND = 12
    WATERFALL = 13
    EARTHWALL = 14

class Element:
    element_type = Element_Type.NONE

class Storm(Element):
    element_type = Element_Type.STORM

class Lava(Element):
    element_type = Element_Type.LAVA

class Steam(Element):
    element_type = Element_Type.STEAM

class Dirt(Element):
    element_type = Element_Type.DIRT

class Dust(Element):
    element_type = Element_Type.DUST

class Thunder(Element):
    element_type = Element_Type.THUNDER

class Hellfire(Element):
    element_type = Element_Type.HELLFIRE

class Waterfall(Element):
    element_type = Element_Type.WATERFALL

class Wind(Element):
    element_type = Element_Type.WIND

class Earthwall(Element):
    element_type = Element_Type.EARTHWALL

class Fire(Element):
    element_type = Element_Type.FIRE

    def __add__(self, other):
        if isinstance(other, Element):
            if other.element_type == Element_Type.AIR:
                return Thunder()
            elif other.element_type == Element_Type.EARTH:
                return Lava()
            elif other.element_type == Element_Type.WATER:
                return Steam()
            elif other.element_type == Element_Type.FIRE:
                return Hellfire()
        return Element()

class Water(Element):
    element_type = Element_Type.WATER

    def __add__(self, other):
        if isinstance(other, Element):
            if other.element_type == Element_Type.AIR:
                return Storm()
            elif other.element_type == Element_Type.EARTH:
                return Dirt()
            elif other.element_type == Element_Type.WATER:
                return Waterfall()
            elif other.element_type == Element_Type.FIRE:
                return Steam()
        return Element()

class Air(Element):
    element_type = Element_Type.AIR

    def __add__(self, other):
        if isinstance(other, Element):
            if other.element_type == Element_Type.AIR:
                return Wind()
            elif other.element_type == Element_Type.EARTH:
                return Dust()
            elif other.element_type == Element_Type.WATER:
                return Storm()
            elif other.element_type == Element_Type.FIRE:
                return Thunder()
        return Element()

class Earth(Element):
    element_type = Element_Type.EARTH

    def __add__(self, other):
        if isinstance(other, Element):
            if other.element_type == Element_Type.AIR:
                return Dust()
            elif other.element_type == Element_Type.EARTH:
                return Earthwall()
            elif other.element_type == Element_Type.WATER:
                return Dirt()
            elif other.element_type == Element_Type.FIRE:
                return Lava()
        return Element()