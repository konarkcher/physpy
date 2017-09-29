import math


class ExperimentValue:
    def __init__(self, value, absolute_error=0.0, relative_error=0.0):
        self.value = value

        if absolute_error and relative_error:
            raise ValueError()

        self.absolute_error = absolute_error
        self.relative_error = relative_error

        if absolute_error:
            self.relative_error = absolute_error / value

        if relative_error:
            self.absolute_error = value * relative_error

    def __add__(self, other):
        sigma = math.sqrt(self.absolute_error**2 + other.absolute_error**2)
        return ExperimentValue(self.value + other.value, sigma)

    def __sub__(self, other):
        sigma = math.sqrt(self.absolute_error**2 + other.absolute_error**2)
        return ExperimentValue(self.value - other.value, sigma)

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __pow__(self, power, modulo=None):
        pass

    def __str__(self):
        pattern = '{}, sigma = {}, eps = {:.2f}%'
        return pattern.format(self.value, self.absolute_error,
                              self.relative_error * 100)


def sqrt(ev):
    pass
