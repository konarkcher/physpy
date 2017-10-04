import math
import copy


class ExperimentValue:
    def __new__(cls, value, sigma=None, epsilon=None, unit=''):
        if isinstance(value, ExperimentValue):
            return value
        return super(ExperimentValue, cls).__new__(cls)

    def __init__(self, value, sigma=None, epsilon=None, unit=''):
        if isinstance(value, ExperimentValue):
            return
        if sigma is not None and epsilon is not None:
            raise ValueError()

        self._value = value

        if sigma is not None:
            self._sigma = abs(sigma)
            self._epsilon = abs(sigma / value)
        elif epsilon is not None:
            self._sigma = abs(value * epsilon)
            self._epsilon = abs(epsilon)
        else:
            self._sigma = 0.0
            self._epsilon = 0.0

        self.unit = unit

    @property
    def value(self):
        return self._value

    @property
    def sigma(self):
        return self._sigma

    @property
    def epsilon(self):
        return self._epsilon

    def __add__(self, other):
        other = ExperimentValue(other)
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value + other.value, sigma, unit=self.unit)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = ExperimentValue(other)
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value - other.value, sigma, unit=self.unit)

    def __rsub__(self, other):
        return ExperimentValue(other) - self

    def __mul__(self, other):
        other = ExperimentValue(other)
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value * other.value, epsilon=eps)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = ExperimentValue(other)
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value / other.value, epsilon=eps)

    def __rtruediv__(self, other):
        return ExperimentValue(other) / self

    def __pow__(self, power, modulo=None):
        # TODO work with power as ExperimentalValue

        if modulo is not None:
            raise ValueError()
        return ExperimentValue(self.value**power, epsilon=self.epsilon * power)

    def __neg__(self):
        return ExperimentValue(-self.value, self.sigma, unit=self.unit)

    def __pos__(self):
        return copy.copy(self)

    def __abs__(self):
        return ExperimentValue(abs(self.value), self.sigma, unit=self.unit)

    def __str__(self):
        pattern = '{:.3e}{:s}, sigma = {:.3e}{:s}, epsilon = {:.2f}%'
        return pattern.format(self.value, self.unit, self.sigma, self.unit,
                              self.epsilon * 100)

    def __repr__(self):
        return self.__str__()


def sqrt(ev):
    return ExperimentValue(math.sqrt(ev.value), epsilon=0.5 * ev.epsilon)
