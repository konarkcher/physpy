import math
import copy


class ExperimentValue:
    def __init__(self, value, sigma=0.0, epsilon=0.0):
        self._value = value  # TODO: add physical rounding

        if sigma and epsilon:
            raise ValueError()

        self._sigma = abs(value * epsilon) if epsilon else abs(sigma)
        self._epsilon = abs(sigma / value) if sigma else abs(epsilon)

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
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value + other.value, sigma)

    def __sub__(self, other):
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value - other.value, sigma)

    def __mul__(self, other):
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value * other.value, epsilon=eps)

    def __truediv__(self, other):
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value / other.value, epsilon=eps)

    def __pow__(self, power, modulo=None):
        if modulo is not None:
            raise ValueError()
        return ExperimentValue(self.value**power, epsilon=self.epsilon * power)

    def __neg__(self):
        return ExperimentValue(-self.value, self.sigma)

    def __pos__(self):
        return copy.copy(self)

    def __abs__(self):
        return ExperimentValue(abs(self.value), self.sigma)

    def __str__(self):
        pattern = '{:.3e}, sigma = {:.3e}, epsilon = {:.2f}%'
        return pattern.format(self.value, self.sigma, self.epsilon * 100)

    def __repr__(self):
        return self.__str__()


def sqrt(ev):
    return ExperimentValue(math.sqrt(ev.value), epsilon=0.5 * ev.epsilon)
