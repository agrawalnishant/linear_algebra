class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


    def add(self, otherVector):
        new_coords = [sc + oc for sc,oc in zip(self.coordinates, otherVector.coordinates)]
        return Vector(new_coords)
    
    def subtract(self, otherVector):
        new_coords = [sc - oc for sc,oc in zip(self.coordinates, otherVector.coordinates)]
        return Vector(new_coords)


    def scalarMultiply(self, scalarVal):
        new_coords = [scalarVal * sc for sc in self.coordinates]
        return Vector(new_coords)
