import math

class MyMath:
    def count_lenght_of_circle(self, radius : int):
        return round(2 * math.pi * radius, 2)
    
    def count_area_of_circle(self, radius : int):
        return round(math.pi * radius**2, 2)

    def count_volume_of_cube(self, side : int):
        return side**3
    
    def count_area_of_sphere_surface(self, radius : int):
        return round(4 * math.pi * radius**2)