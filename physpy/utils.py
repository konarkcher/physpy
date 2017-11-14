import numpy as np

import physpy as pp


def linear(x, y, through_zero=True):
    if through_zero:
        k = np.average(x * y) / np.average(x**2)

        under_sqrt = np.average(y**2) / np.average(x**2) - k**2
        sigma = np.sqrt(np.abs(under_sqrt) / len(x))

        return pp.ExperimentValue(k, sigma)

    k = ((np.average(x * y) - np.average(x) * np.average(y)) /
         (np.average(x**2) - np.average(x)**2))
    b = np.average(y) - k * np.average(x)

    under_sqrt = ((np.average(y**2) - np.average(y)**2) /
                  (np.average(x**2) - np.average(x)**2)) - k**2
    sigma_k = np.sqrt(np.abs(under_sqrt) / len(x))
    sigma_b = sigma_k * np.sqrt(np.abs(np.average(x**2) - np.average(x)**2))

    return pp.ExperimentValue(k, sigma_k), pp.ExperimentValue(b, sigma_b)


def diff(theor, real):
    print('diff epsilon = {:.2f}%'.format(abs(theor - real) / theor * 100))
