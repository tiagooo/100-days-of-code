# bite 252. let's play with Pandas Series

import numpy as np
import pandas as pd


def return_at_index(ser, index):
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    return ser.loc[index]


def get_slice(ser, start, end):
    """Return the slice of the given Series in the range between
    start and end.
    """
    loclist = [*range(start, end)]
    return ser.loc[loclist]


def get_slice_inclusive(ser, start, end):
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    loclist = [*range(start, end+1)]
    return ser.loc[loclist]


def return_head(ser, num):
    """Return the first num elements of the given Series.
    """
    return ser.head(num)


def return_tail(ser, num):
    """Return the last num elements of the given Series.
    """
    return ser.tail(num)


def get_index(ser):
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser, even_index):
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    if even_index:  # same as if even_index == True:
        loclist = [*range(0, len(ser.index), 2)]
        series = ser.loc[loclist]
    else:
        loclist = [*range(1, len(ser.index), 2)]
        series = ser.loc[loclist]
    return series
