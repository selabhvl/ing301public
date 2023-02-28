

def max(a: int, b: int) -> int:
    if a > b:
        return a
    else:
        return b


#print(max.__call__(5, 3))


#print(type(max))
#print(dir(max))



class Point:

    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point3D(Point):

    __slots__ = ['_z']

    def _set_z(self, value):
        print("Prøvde å sette men går ikke")

    def _get_z(self):
        print("Hente ut z")
        return self._z

    z = property(fget=_get_z, fset=_set_z)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self._z = z

p = Point(2,4)

print(p.x)
p.x = 23
print(p.x)


p2 = Point3D(1,2,3)
print(p2.z)

p2.z = -1

print(p2.z)


