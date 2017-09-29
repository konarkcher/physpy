import math
import copy


class ExperimentValue:
    def __init__(self, value, sigma=0.0, eps=0.0):
        self._value = value  # TODO: add physical rounding

        if sigma and eps:
            raise ValueError()

        self._sigma = abs(value * eps) if eps else abs(sigma)
        self._eps = abs(sigma / value) if sigma else abs(eps)

    def get_value(self):
        return self._value

    def get_sigma(self):
        return self._sigma

    def get_eps(self):
        return self._eps

    def __add__(self, other):
        sigma = math.sqrt(self.get_sigma()**2 + other.get_sigma()**2)
        return ExperimentValue(self.get_value() + other.get_value(), sigma)

    def __sub__(self, other):
        sigma = math.sqrt(self.get_sigma()**2 + other.get_sigma()**2)
        return ExperimentValue(self.get_value() - other.get_value(), sigma)

    def __mul__(self, other):
        eps = math.sqrt(self.get_eps()**2 + other.get_eps()**2)
        return ExperimentValue(self.get_value() * other.get_value(), eps=eps)

    def __truediv__(self, other):
        eps = math.sqrt(self.get_eps()**2 + other.get_eps()**2)
        return ExperimentValue(self.get_value() / other.get_value(), eps=eps)

    def __pow__(self, power, modulo=None):
        if modulo is not None:
            raise NotImplementedError()
        return ExperimentValue(self.get_value()**power,
                               eps=self.get_eps() * power)

    def __neg__(self):
        return ExperimentValue(-self.get_value(), self.get_sigma())

    def __pos__(self):
        return copy.copy(self)

    def __abs__(self):
        return ExperimentValue(abs(self.get_value()), self.get_sigma())

    def __str__(self):
        pattern = '{:.3f}, sigma = {:.3f}, eps = {:.2f}%'
        return pattern.format(self.get_value(), self.get_sigma(),
                              self.get_eps() * 100)


def sqrt(ev):
    return ExperimentValue(math.sqrt(ev.get_value()), eps=0.5 * ev.get_eps())
