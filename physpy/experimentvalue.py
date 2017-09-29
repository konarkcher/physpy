import math
import copy


class ExperimentValue:
    def __init__(self, value, sigma=0.0, eps=0.0):
        self.value = value  # TODO: add physical rounding

        if sigma and eps:
            raise ValueError()

        self.sigma = abs(value * eps) if eps else abs(sigma)
        self.eps = sigma / abs(value) if sigma else abs(eps)

    def __add__(self, other):
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value + other.value, sigma)

    def __sub__(self, other):
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value - other.value, sigma)

    def __mul__(self, other):
        eps = math.sqrt(self.eps**2 + other.eps**2)
        return ExperimentValue(self.value * other.value, eps=eps)

    def __truediv__(self, other):
        eps = math.sqrt(self.eps**2 + other.eps**2)
        return ExperimentValue(self.value / other.value, eps=eps)

    def __pow__(self, power, modulo=None):
        if modulo is not None:
            raise ValueError
        return ExperimentValue(self.value**power, eps=self.eps * power)

    def __neg__(self):
        return ExperimentValue(-self.value, self.sigma)

    def __pos__(self):
        return copy.copy(self)

    def __abs__(self):
        return ExperimentValue(abs(self.value), self.sigma)

    def __str__(self):
        pattern = '{:.3f}, sigma = {:.3f}, eps = {:.2f}%'
        return pattern.format(self.value, self.sigma, self.eps * 100)


def sqrt(ev):
    return ExperimentValue(math.sqrt(ev.value), eps=0.5 * ev.eps)
