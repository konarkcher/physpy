import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator


def draw_grid(title='', xlabel='x', ylabel='y'):
    fig = plt.figure(figsize=(10, 6))
    axes = plt.axes(title=title, xlabel=xlabel, ylabel=ylabel)

    axes.grid(which='major', visible=True, linewidth=1.0)

    return fig, axes
