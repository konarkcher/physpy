import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

import physpy as pp


def create_fig(title='', xlabel='x', ylabel='y'):
    fig = plt.figure(figsize=(10, 6))
    axes = plt.axes(title=title, xlabel=xlabel, ylabel=ylabel)

    axes.xaxis.set_minor_locator(AutoMinorLocator(5))
    axes.yaxis.set_minor_locator(AutoMinorLocator(5))

    axes.grid(which='minor', visible=True, linewidth=0.5)
    axes.grid(which='major', visible=True, linewidth=1.0)

    return fig, axes


def linear(x, y, through_zero=True, points=True, yerr=None, xerr=None):
    if points:
        if yerr is None or xerr is None:
            plt.plot(x, y, 'bo')
        else:
            plt.errorbar(x, y, fmt='b,', yerr=yerr, xerr=xerr)

    plt.plot(*pp.utils.linear_plot(x, y, through_zero=through_zero), 'b-')
    return pp.utils.ols(x, y, through_zero=through_zero)
