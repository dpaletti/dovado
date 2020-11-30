"""
This type stub file was generated by pyright.
"""

import numpy as np

def dentonm(indicator, benchmark, freq=..., **kwargs):
    """
    Modified Denton's method to convert low-frequency to high-frequency data.

    Uses proportionate first-differences as the penalty function.  See notes.

    Parameters
    ----------
    indicator : array_like
        A low-frequency indicator series.  It is assumed that there are no
        pre-sample indicators.  Ie., the first indicators line up with
        the first benchmark.
    benchmark : array_like
        The higher frequency benchmark.  A 1d or 2d data series in columns.
        If 2d, then M series are assumed.
    freq : str {"aq","qm", "other"}
        The frequency to use in the conversion.

        * "aq" - Benchmarking an annual series to quarterly.
        * "mq" - Benchmarking a quarterly series to monthly.
        * "other" - Custom stride.  A kwarg, k, must be supplied.
    **kwargs
        Additional keyword argument. For example:

        * k, an int, the number of high-frequency observations that sum to make
          an aggregate low-frequency observation. `k` is used with
          `freq` == "other".

    Returns
    -------
    transformed : ndarray
        The transformed series.

    Examples
    --------
    >>> indicator = [50,100,150,100] * 5
    >>> benchmark = [500,400,300,400,500]
    >>> benchmarked = dentonm(indicator, benchmark, freq="aq")

    Notes
    -----
    Denton's method minimizes the distance given by the penalty function, in
    a least squares sense, between the unknown benchmarked series and the
    indicator series subject to the condition that the sum of the benchmarked
    series is equal to the benchmark. The modification allows that the first
    value not be pre-determined as is the case with Denton's original method.
    If the there is no benchmark provided for the last few indicator
    observations, then extrapolation is performed using the last
    benchmark-indicator ratio of the previous period.

    Minimizes sum((X[t]/I[t] - X[t-1]/I[t-1])**2)

    s.t.

    sum(X) = A, for each period.  Where X is the benchmarked series, I is
    the indicator, and A is the benchmark.

    References
    ----------
    Bloem, A.M, Dippelsman, R.J. and Maehle, N.O.  2001 Quarterly National
        Accounts Manual--Concepts, Data Sources, and Compilation. IMF.
        http://www.imf.org/external/pubs/ft/qna/2000/Textbook/index.htm
    Cholette, P. 1988. "Benchmarking systems of socio-economic time series."
        Statistics Canada, Time Series Research and Analysis Division,
        Working Paper No TSRA-88-017E.
    Denton, F.T. 1971. "Adjustment of monthly or quarterly series to annual
        totals: an approach based on quadratic minimization." Journal of the
        American Statistical Association. 99-102.
    """
    ...

if __name__ == "__main__":
    indicator = np.array([98.2, 100.8, 102.2, 100.8, 99, 101.6, 102.7, 101.5, 100.5, 103, 103.5, 101.5])
    benchmark = np.array([4000, 4161.4])
    x_imf = dentonm(indicator, benchmark, freq="aq")
    imf_stata = np.array([969.8, 998.4, 1018.3, 1013.4, 1007.2, 1042.9, 1060.3, 1051, 1040.6, 1066.5, 1071.7, 1051])
    zQ = np.array([50, 100, 150, 100] * 5)
    Y = np.array([500, 400, 300, 400, 500])
    x_denton = dentonm(zQ, Y, freq="aq")
    x_stata = np.array([64.334796, 127.80616, 187.82379, 120.03526, 56.563894, 105.97568, 147.50144, 89.958987, 40.547201, 74.445963, 108.34473, 76.66211, 42.763347, 94.14664, 153.41596, 109.67405, 58.290761, 122.62556, 190.41409, 128.66959])