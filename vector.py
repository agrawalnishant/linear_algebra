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
        selfCoordinates = list(self.coordinates)
        otherCoordinates = list(otherVector.coordinates)
        for count in range(self.dimension):
            print("count: ",count)
            selfCoordinates[count] +=  otherCoordinates[count]
        self.coordinates = tuple(selfCoordinates)
