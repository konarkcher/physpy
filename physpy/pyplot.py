import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator


def plot(x, y, title='', xlabel='x', ylabel='y', save=False):
    fig = plt.figure(figsize=(10, 6))
    axes = plt.axes(title=title, xlabel=xlabel, ylabel=ylabel)

    axes.grid(which='major', visible=True, linewidth=1.0)

    plt.plot(x, y)
    plt.show()

    if save:
        if not title:
            title = 'temp'
        fig.savefig('{}.png'.format(title), dpi=300)
