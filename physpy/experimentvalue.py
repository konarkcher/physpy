import math
import copy


class ExperimentValue:
    def __init__(self, value, sigma=None, epsilon=None, unit=''):
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

    @staticmethod
    def cast(value):
        if isinstance(value, ExperimentValue):
            return value
        return ExperimentValue(value)

    def _format(self):
        if not self.sigma:
            return '{:.3e}'.format(self.value), '{:.3e}'.format(self.sigma) 
    
        lg = math.floor(math.log(abs(self.value)) / math.log(10))
        sigma_lg = math.floor(math.log(abs(self.sigma)) / math.log(10))
        if sigma_lg > lg:
            lg = sigma_lg
        
        sigma_main = self.sigma * 10**-sigma_lg
        temp = self.value * 10**-sigma_lg
        nums = lg - sigma_lg
        
        sigma_first = round(abs(sigma_main))
        if sigma_first < 4:
            sgima_main = round(sigma_main * 10) / 10
            temp = round(temp * 10) / 10
            nums += 1
        else:
            sigma_main = round(sigma_main)
            temp = round(temp)
            nums
        
        temp *= 10 ** (sigma_lg - lg)
        sigma_main *= 10 ** (sigma_lg - lg)
        
        pattern = '{:.' + str(nums) + 'f}'
        
        if lg:
            return (pattern + 'e{:d}').format(temp, lg), (pattern + 'e{:d}').format(sigma_main, lg)
        else:
            return pattern.format(temp), pattern.format(sigma_main)

    def __add__(self, other):
        other = ExperimentValue.cast(other)
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value + other.value, sigma, unit=self.unit)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = ExperimentValue.cast(other)
        sigma = math.sqrt(self.sigma**2 + other.sigma**2)
        return ExperimentValue(self.value - other.value, sigma, unit=self.unit)

    def __rsub__(self, other):
        return ExperimentValue.cast(other) - self

    def __mul__(self, other):
        other = ExperimentValue.cast(other)
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value * other.value, epsilon=eps)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = ExperimentValue.cast(other)
        eps = math.sqrt(self.epsilon**2 + other.epsilon**2)
        return ExperimentValue(self.value / other.value, epsilon=eps)

    def __rtruediv__(self, other):
        return ExperimentValue.cast(other) / self

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
        val, sig = self._format()
        pattern = '{:s}{:s}, sigma = {:s}{:s}, epsilon = {:.2f}%'
        return pattern.format(val, self.unit, sig, self.unit, self.epsilon * 100)

    def __repr__(self):
        return self.__str__()


def sqrt(ev):
    return ExperimentValue(math.sqrt(ev.value), epsilon=0.5 * ev.epsilon)
