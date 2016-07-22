import numpy as np
import pandas as pd

from scipy.optimize import curve_fit


def coeffs(x, y, i, l=15, dx=5):
    df_i = (y[i + dx] - y[i - dx]) / (x[i + dx] - x[i - dx])
    b = -df_i / (y[i] - l)
    a = (y[i] - l) * np.exp(b * x[i])
    return a, b


def dy_dx(x, y, i, dx=5):
    return (y[i + dx] - y[i - dx]) / (x[i + dx] - x[i - dx])


def adj_below(data, l=15):
    if (data > l).all():
        return data

    cross_idx = np.where(data <= l)[0][0]
    x = data.index.values
    y = data.values
    i = cross_idx - 20 if dy_dx(x, y, cross_idx -
                                20) < 0 and cross_idx - 20 > 0 else cross_idx - 10
    assert(dy_dx(x, y, i) < 0)  # must be 0
    a, b = coeffs(x, y, i, l=l)

    f = lambda _: a * np.exp(-b * _) + l
    return np.append(y[:i], f(x)[i:])


def adj_above(data, l=65):
    if (data < l).all():
        return data

    cross_idx = np.where(data >= l)[0][0]
    x = data.index.values
    y = data.values
    i = cross_idx - 20 if dy_dx(x, y, cross_idx -
                                20) > 0 and cross_idx - 20 > 0 else cross_idx - 10
    assert(dy_dx(x, y, i) > 0)  # must be 0
    a, b = coeffs(x, y, i, l=l)

    f = lambda _: a * np.exp(-b * _) + l
    return np.append(y[:i], f(x)[i:])
