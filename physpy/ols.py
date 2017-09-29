import numpy as np
import pandas as pd

from physpy.experimentvalue import ExperimentValue


def through_zero(x, y):
    k = np.average(x * y) / np.average(x**2)

    under_sqrt = np.average(y**2) / np.average(x**2) - k**2
    sigma = np.sqrt(np.abs(under_sqrt) / len(x))

    return ExperimentValue(k, sigma)


def linear(x, y):
    k = ((np.average(x * y) - np.average(x) * np.average(y)) /
         (np.average(x**2) - np.average(x)**2))
    b = np.average(y) - k * np.average(x)

    under_sqrt = ((np.average(y**2) - np.average(y)**2) /
                  (np.average(x**2) - np.average(x)**2)) - k**2
    sigma_k = np.sqrt(np.abs(under_sqrt) / len(x))
    sigma_b = sigma_k * np.sqrt(np.abs(np.average(x**2) - np.average(x)**2))

    return ExperimentValue(k, sigma_k), ExperimentValue(b, sigma_b)
