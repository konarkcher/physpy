import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import AutoMinorLocator


def draw_grid(title='', xlabel='x', ylabel='y'):
    fig = plt.figure(figsize=(10, 6))
    axes = plt.axes(title=title, xlabel=xlabel, ylabel=ylabel)

    axes.xaxis.set_minor_locator(AutoMinorLocator(5))
    axes.yaxis.set_minor_locator(AutoMinorLocator(5))

    axes.grid(which='minor', visible=True, linewidth=0.5)
    axes.grid(which='major', visible=True, linewidth=1.0)

    return fig, axes
