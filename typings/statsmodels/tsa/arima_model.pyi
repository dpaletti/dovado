"""
This type stub file was generated by pyright.
"""

import statsmodels.base.wrapper as wrap
from statsmodels.compat.pandas import Appender
from statsmodels.tools.decorators import cache_readonly
from statsmodels.tsa.base import tsa_model

ARIMA_DEPRECATION_WARN = """
statsmodels.tsa.arima_model.ARMA and statsmodels.tsa.arima_model.ARIMA have
been deprecated in favor of statsmodels.tsa.arima.model.ARIMA (note the .
between arima and model) and
statsmodels.tsa.SARIMAX. These will be removed after the 0.12 release.

statsmodels.tsa.arima.model.ARIMA makes use of the statespace framework and
is both well tested and maintained.

To silence this warning and continue using ARMA and ARIMA until they are
removed, use:

import warnings
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARMA',
                        FutureWarning)
warnings.filterwarnings('ignore', 'statsmodels.tsa.arima_model.ARIMA',
                        FutureWarning)
"""
REPEATED_FIT_ERROR = """
Model has been fit using trend={0} and method={1}. These cannot be changed
in subsequent calls to `fit`. Instead, use a new instance of {mod}.
"""
_armax_notes = r"""
    Notes
    -----
    If exogenous variables are given, then the model that is fit is

    .. math::

       \phi(L)(y_t - X_t\beta) = \theta(L)\epsilon_t

    where :math:`\phi` and :math:`\theta` are polynomials in the lag
    operator, :math:`L`. This is the regression model with ARMA errors,
    or ARMAX model. This specification is used, whether or not the model
    is fit using conditional sum of square or maximum-likelihood, using
    the `method` argument in
    :meth:`statsmodels.tsa.arima_model.%(Model)s.fit`. Therefore, for
    now, `css` and `mle` refer to estimation methods only. This may
    change for the case of the `css` model in future versions.
"""
_arma_params = """endog : array_like
        The endogenous variable.
    order : iterable
        The (p,q) order of the model for the number of AR parameters,
        and MA parameters to use.
    exog : array_like, optional
        An optional array of exogenous variables. This should *not* include a
        constant or trend. You can specify this in the `fit` method."""
_arma_model = """\
Autoregressive Moving Average ARMA(p,q) Model

    .. deprecated:: 0.12
       Use statsmodels.tsa.arima.model.ARIMA instead"""
_arima_model = """\
Autoregressive Integrated Moving Average ARIMA(p,d,q) Model

    .. deprecated:: 0.12
       Use statsmodels.tsa.arima.model.ARIMA instead"""
_arima_params = """endog : array_like
        The endogenous variable.
    order : iterable
        The (p,d,q) order of the model for the number of AR parameters,
        differences, and MA parameters to use.
    exog : array_like, optional
        An optional array of exogenous variables. This should *not* include a
        constant or trend. You can specify this in the `fit` method."""
_predict_notes = """
        Notes
        -----
        Use the results predict method instead.
"""
_results_notes = """
        Notes
        -----
        It is recommended to use dates with the time-series models, as the
        below will probably make clear. However, if ARIMA is used without
        dates and/or `start` and `end` are given as indices, then these
        indices are in terms of the *original*, undifferenced series. Ie.,
        given some undifferenced observations::

         1970Q1, 1
         1970Q2, 1.5
         1970Q3, 1.25
         1970Q4, 2.25
         1971Q1, 1.2
         1971Q2, 4.1

        1970Q1 is observation 0 in the original series. However, if we fit an
        ARIMA(p,1,q) model then we lose this first observation through
        differencing. Therefore, the first observation we can forecast (if
        using exact MLE) is index 1. In the differenced series this is index
        0, but we refer to it as 1 from the original series.
"""
_predict = """
        %(Model)s model in-sample and out-of-sample prediction

        Parameters
        ----------
        %(params)s
        start : int, str, or datetime
            Zero-indexed observation number at which to start forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type.
        end : int, str, or datetime
            Zero-indexed observation number at which to end forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out of sample prediction.
        exog : array_like, optional
            If the model is an ARMAX and out-of-sample forecasting is
            requested, exog must be given. exog must be aligned so that exog[0]
            is used to produce the first out-of-sample forecast. The number of
            observation in exog should match the number of out-of-sample
            forecasts produced. If the length of exog does not match the number
            of forecasts, a SpecificationWarning is produced.
        dynamic : bool, optional
            The `dynamic` keyword affects in-sample prediction. If dynamic
            is False, then the in-sample lagged values are used for
            prediction. If `dynamic` is True, then in-sample forecasts are
            used in place of lagged dependent variables. The first forecast
            value is `start`.
        %(extra_params)s

        Returns
        -------
        %(returns)s
        %(extra_section)s
"""
_predict_returns = """predict : ndarray
            The predicted values.

"""
_arma_predict = _predict % { "Model": "ARMA","params": """params : array_like
            The fitted parameters of the model.""","extra_params": "","returns": _predict_returns,"extra_section": _predict_notes }
_arma_results_predict = _predict % { "Model": "ARMA","params": "","extra_params": "","returns": _predict_returns,"extra_section": _results_notes }
_arima_extras = """typ : str {'linear', 'levels'}

            - 'linear' : Linear prediction in terms of the differenced
              endogenous variables.
            - 'levels' : Predict the levels of the original endogenous
              variables.\n"""
_arima_predict = _predict % { "Model": "ARIMA","params": """params : array_like
            The fitted parameters of the model.""","extra_params": _arima_extras,"returns": _predict_returns,"extra_section": _predict_notes }
_arima_results_predict = _predict % { "Model": "ARIMA","params": "","extra_params": _arima_extras,"returns": _predict_returns,"extra_section": _results_notes }
_arima_plot_predict_example = """        Examples
        --------
        >>> import statsmodels.api as sm
        >>> import matplotlib.pyplot as plt
        >>> import pandas as pd
        >>>
        >>> dta = sm.datasets.sunspots.load_pandas().data[['SUNACTIVITY']]
        >>> dta.index = pd.date_range(start='1700', end='2009', freq='A')
        >>> res = sm.tsa.ARMA(dta, (3, 0)).fit()
        >>> fig, ax = plt.subplots()
        >>> ax = dta.loc['1950':].plot(ax=ax)
        >>> fig = res.plot_predict('1990', '2012', dynamic=True, ax=ax,
        ...                        plot_insample=False)
        >>> plt.show()

        .. plot:: plots/arma_predict_plot.py
"""
_plot_extras = """alpha : float, optional
            The confidence intervals for the forecasts are (1 - alpha)%
        plot_insample : bool, optional
            Whether to plot the in-sample series. Default is True.
        ax : matplotlib.Axes, optional
            Existing axes to plot with."""
_plot_predict = """
        Plot forecasts
                      """ + '\n'.join(_predict.split('\n')[2]) % { "params": "","extra_params": _plot_extras,"returns": """fig : Figure
            The plotted Figure instance""","extra_section": '\n' + _arima_plot_predict_example + '\n' + _results_notes }
_arima_plot_predict = """
        Plot forecasts
                      """ + '\n'.join(_predict.split('\n')[2]) % { "params": "","extra_params": _plot_extras,"returns": """fig : Figure
            The plotted Figure instance""","extra_section": '\n' + _arima_plot_predict_example + '\n' + '\n'.join(_results_notes.split('\n')[: 3]) + """
        This is hard-coded to only allow plotting of the forecasts in levels.
""" + '\n'.join(_results_notes.split('\n')[3]) }
def cumsum_n(x, n):
    ...

class ARMA(tsa_model.TimeSeriesModel):
    __doc__ = ...
    def __init__(self, endog, order, exog=..., dates=..., freq=..., missing=...) -> None:
        ...
    
    def score(self, params):
        """
        Compute the score function at params.

        Notes
        -----
        This is a numerical approximation.
        """
        ...
    
    def hessian(self, params):
        """
        Compute the Hessian at params,

        Notes
        -----
        This is a numerical approximation.
        """
        ...
    
    def geterrors(self, params):
        """
        Get the errors of the ARMA process.

        Parameters
        ----------
        params : array_like
            The fitted ARMA parameters
        order : array_like
            3 item iterable, with the number of AR, MA, and exogenous
            parameters, including the trend
        """
        ...
    
    @Appender(_arma_predict)
    def predict(self, params, start=..., end=..., exog=..., dynamic=..., **kwargs):
        ...
    
    def loglike(self, params, set_sigma2=...):
        """
        Compute the log-likelihood for ARMA(p,q) model

        Notes
        -----
        Likelihood used depends on the method set in fit
        """
        ...
    
    def loglike_kalman(self, params, set_sigma2=...):
        """
        Compute exact loglikelihood for ARMA(p,q) model by the Kalman Filter.
        """
        ...
    
    def loglike_css(self, params, set_sigma2=...):
        """
        Conditional Sum of Squares likelihood function.
        """
        ...
    
    def fit(self, start_params=..., trend=..., method=..., transparams=..., solver=..., maxiter=..., full_output=..., disp=..., callback=..., start_ar_lags=..., **kwargs):
        """
        Fits ARMA(p,q) model using exact maximum likelihood via Kalman filter.

        Parameters
        ----------
        start_params : array_like, optional
            Starting parameters for ARMA(p,q). If None, the default is given
            by ARMA._fit_start_params.  See there for more information.
        transparams : bool, optional
            Whether or not to transform the parameters to ensure stationarity.
            Uses the transformation suggested in Jones (1980).  If False,
            no checking for stationarity or invertibility is done.
        method : str {'css-mle','mle','css'}
            This is the loglikelihood to maximize.  If "css-mle", the
            conditional sum of squares likelihood is maximized and its values
            are used as starting values for the computation of the exact
            likelihood via the Kalman filter.  If "mle", the exact likelihood
            is maximized via the Kalman Filter.  If "css" the conditional sum
            of squares likelihood is maximized.  All three methods use
            `start_params` as starting parameters.  See above for more
            information.
        trend : str {'c','nc'}
            Whether to include a constant or not.  'c' includes constant,
            'nc' no constant.
        solver : str or None, optional
            Solver to be used.  The default is 'lbfgs' (limited memory
            Broyden-Fletcher-Goldfarb-Shanno).  Other choices are 'bfgs',
            'newton' (Newton-Raphson), 'nm' (Nelder-Mead), 'cg' -
            (conjugate gradient), 'ncg' (non-conjugate gradient), and
            'powell'. By default, the limited memory BFGS uses m=12 to
            approximate the Hessian, projected gradient tolerance of 1e-8 and
            factr = 1e2. You can change these by using kwargs.
        maxiter : int, optional
            The maximum number of function evaluations. Default is 500.
        tol : float
            The convergence tolerance.  Default is 1e-08.
        full_output : bool, optional
            If True, all output from solver will be available in
            the Results object's mle_retvals attribute.  Output is dependent
            on the solver.  See Notes for more information.
        disp : int, optional
            If True, convergence information is printed.  For the default
            l_bfgs_b solver, disp controls the frequency of the output during
            the iterations. disp < 0 means no output in this case.
        callback : function, optional
            Called after each iteration as callback(xk) where xk is the current
            parameter vector.
        start_ar_lags : int, optional
            Parameter for fitting start_params. When fitting start_params,
            residuals are obtained from an AR fit, then an ARMA(p,q) model is
            fit via OLS using these residuals. If start_ar_lags is None, fit
            an AR process according to best BIC. If start_ar_lags is not None,
            fits an AR process with a lag length equal to start_ar_lags.
            See ARMA._fit_start_params_hr for more information.
        **kwargs
            See Notes for keyword arguments that can be passed to fit.

        Returns
        -------
        statsmodels.tsa.arima_model.ARMAResults class

        See Also
        --------
        statsmodels.base.model.LikelihoodModel.fit : for more information
            on using the solvers.
        ARMAResults : results class returned by fit

        Notes
        -----
        If fit by 'mle', it is assumed for the Kalman Filter that the initial
        unknown state is zero, and that the initial variance is
        P = dot(inv(identity(m**2)-kron(T,T)),dot(R,R.T).ravel('F')).reshape(r,
        r, order = 'F')
        """
        ...
    
    @classmethod
    def from_formula(cls, formula, data, subset=..., drop_cols=..., *args, **kwargs):
        ...
    


class ARIMA(ARMA):
    __doc__ = ...
    def __new__(cls, endog, order, exog=..., dates=..., freq=..., missing=...):
        ...
    
    def __getnewargs__(self):
        ...
    
    def __init__(self, endog, order, exog=..., dates=..., freq=..., missing=...) -> None:
        ...
    
    def fit(self, start_params=..., trend=..., method=..., transparams=..., solver=..., maxiter=..., full_output=..., disp=..., callback=..., start_ar_lags=..., **kwargs):
        """
        Fits ARIMA(p,d,q) model by exact maximum likelihood via Kalman filter.

        Parameters
        ----------
        start_params : array_like, optional
            Starting parameters for ARMA(p,q).  If None, the default is given
            by ARMA._fit_start_params.  See there for more information.
        transparams : bool, optional
            Whether or not to transform the parameters to ensure stationarity.
            Uses the transformation suggested in Jones (1980).  If False,
            no checking for stationarity or invertibility is done.
        method : str {'css-mle','mle','css'}
            This is the loglikelihood to maximize.  If "css-mle", the
            conditional sum of squares likelihood is maximized and its values
            are used as starting values for the computation of the exact
            likelihood via the Kalman filter.  If "mle", the exact likelihood
            is maximized via the Kalman Filter.  If "css" the conditional sum
            of squares likelihood is maximized.  All three methods use
            `start_params` as starting parameters.  See above for more
            information.
        trend : str {'c','nc'}
            Whether to include a constant or not.  'c' includes constant,
            'nc' no constant.
        solver : str or None, optional
            Solver to be used.  The default is 'lbfgs' (limited memory
            Broyden-Fletcher-Goldfarb-Shanno).  Other choices are 'bfgs',
            'newton' (Newton-Raphson), 'nm' (Nelder-Mead), 'cg' -
            (conjugate gradient), 'ncg' (non-conjugate gradient), and
            'powell'. By default, the limited memory BFGS uses m=12 to
            approximate the Hessian, projected gradient tolerance of 1e-8 and
            factr = 1e2. You can change these by using kwargs.
        maxiter : int, optional
            The maximum number of function evaluations. Default is 500.
        tol : float
            The convergence tolerance.  Default is 1e-08.
        full_output : bool, optional
            If True, all output from solver will be available in
            the Results object's mle_retvals attribute.  Output is dependent
            on the solver.  See Notes for more information.
        disp : int, optional
            If True, convergence information is printed.  For the default
            l_bfgs_b solver, disp controls the frequency of the output during
            the iterations. disp < 0 means no output in this case.
        callback : function, optional
            Called after each iteration as callback(xk) where xk is the current
            parameter vector.
        start_ar_lags : int, optional
            Parameter for fitting start_params. When fitting start_params,
            residuals are obtained from an AR fit, then an ARMA(p,q) model is
            fit via OLS using these residuals. If start_ar_lags is None, fit
            an AR process according to best BIC. If start_ar_lags is not None,
            fits an AR process with a lag length equal to start_ar_lags.
            See ARMA._fit_start_params_hr for more information.
        **kwargs
            See Notes for keyword arguments that can be passed to fit.

        Returns
        -------
        `statsmodels.tsa.arima.ARIMAResults` class

        See Also
        --------
        statsmodels.base.model.LikelihoodModel.fit : for more information
            on using the solvers.
        ARIMAResults : results class returned by fit

        Notes
        -----
        If fit by 'mle', it is assumed for the Kalman Filter that the initial
        unknown state is zero, and that the initial variance is
        P = dot(inv(identity(m**2)-kron(T,T)),dot(R,R.T).ravel('F')).reshape(r,
        r, order = 'F')
        """
        ...
    
    @Appender(_arima_predict)
    def predict(self, params, start=..., end=..., exog=..., typ=..., dynamic=...):
        ...
    


class ARMAResults(tsa_model.TimeSeriesModelResults):
    """
    Class to hold results from fitting an ARMA model.

    Parameters
    ----------
    model : ARMA instance
        The fitted model instance
    params : ndarray
        Fitted parameters
    normalized_cov_params : ndarray, optional
        The normalized variance covariance matrix
    scale : float, optional
        Optional argument to scale the variance covariance matrix.

    Attributes
    ----------
    aic : float
        Akaike Information Criterion
        :math:`-2*llf+2* df_model`
        where `df_model` includes all AR parameters, MA parameters, constant
        terms parameters on constant terms and the variance.
    arparams : ndarray
        The parameters associated with the AR coefficients in the model.
    arroots : ndarray
        The roots of the AR coefficients are the solution to
        (1 - arparams[0]*z - arparams[1]*z**2 -...- arparams[p-1]*z**k_ar) = 0
        Stability requires that the roots in modulus lie outside the unit
        circle.
    bic : float
        Bayes Information Criterion
        -2*llf + log(nobs)*df_model
        Where if the model is fit using conditional sum of squares, the
        number of observations `nobs` does not include the `p` pre-sample
        observations.
    bse : ndarray
        The standard errors of the parameters. These are computed using the
        numerical Hessian.
    df_model : ndarray
        The model degrees of freedom = `k_exog` + `k_trend` + `k_ar` + `k_ma`
    df_resid : ndarray
        The residual degrees of freedom = `nobs` - `df_model`
    fittedvalues : ndarray
        The predicted values of the model.
    hqic : float
        Hannan-Quinn Information Criterion
        -2*llf + 2*(`df_model`)*log(log(nobs))
        Like `bic` if the model is fit using conditional sum of squares then
        the `k_ar` pre-sample observations are not counted in `nobs`.
    k_ar : int
        The number of AR coefficients in the model.
    k_exog : int
        The number of exogenous variables included in the model. Does not
        include the constant.
    k_ma : int
        The number of MA coefficients.
    k_trend : int
        This is 0 for no constant or 1 if a constant is included.
    llf : float
        The value of the log-likelihood function evaluated at `params`.
    maparams : ndarray
        The value of the moving average coefficients.
    maroots : ndarray
        The roots of the MA coefficients are the solution to
        (1 + maparams[0]*z + maparams[1]*z**2 + ... + maparams[q-1]*z**q) = 0
        Stability requires that the roots in modules lie outside the unit
        circle.
    model : ARMA instance
        A reference to the model that was fit.
    nobs : float
        The number of observations used to fit the model. If the model is fit
        using exact maximum likelihood this is equal to the total number of
        observations, `n_totobs`. If the model is fit using conditional
        maximum likelihood this is equal to `n_totobs` - `k_ar`.
    n_totobs : float
        The total number of observations for `endog`. This includes all
        observations, even pre-sample values if the model is fit using `css`.
    params : ndarray
        The parameters of the model. The order of variables is the trend
        coefficients and the `k_exog` exogenous coefficients, then the
        `k_ar` AR coefficients, and finally the `k_ma` MA coefficients.
    pvalues : ndarray
        The p-values associated with the t-values of the coefficients. Note
        that the coefficients are assumed to have a Student's T distribution.
    resid : ndarray
        The model residuals. If the model is fit using 'mle' then the
        residuals are created via the Kalman Filter. If the model is fit
        using 'css' then the residuals are obtained via `scipy.signal.lfilter`
        adjusted such that the first `k_ma` residuals are zero. These zero
        residuals are not returned.
    scale : float
        This is currently set to 1.0 and not used by the model or its results.
    sigma2 : float
        The variance of the residuals. If the model is fit by 'css',
        sigma2 = ssr/nobs, where ssr is the sum of squared residuals. If
        the model is fit by 'mle', then sigma2 = 1/nobs * sum(v**2 / F)
        where v is the one-step forecast error and F is the forecast error
        variance. See `nobs` for the difference in definitions depending on the
        fit.
    """
    _cache = ...
    def __init__(self, model, params, normalized_cov_params=..., scale=...) -> None:
        ...
    
    @cache_readonly
    def arroots(self):
        ...
    
    @cache_readonly
    def maroots(self):
        ...
    
    @cache_readonly
    def arfreq(self):
        r"""
        Returns the frequency of the AR roots.

        This is the solution, x, to z = abs(z)*exp(2j*np.pi*x) where z are the
        roots.
        """
        ...
    
    @cache_readonly
    def mafreq(self):
        r"""
        Returns the frequency of the MA roots.

        This is the solution, x, to z = abs(z)*exp(2j*np.pi*x) where z are the
        roots.
        """
        ...
    
    @cache_readonly
    def arparams(self):
        ...
    
    @cache_readonly
    def maparams(self):
        ...
    
    @cache_readonly
    def llf(self):
        ...
    
    @cache_readonly
    def bse(self):
        ...
    
    @cache_readonly
    def cov_params_default(self):
        ...
    
    @cache_readonly
    def aic(self):
        ...
    
    @cache_readonly
    def bic(self):
        ...
    
    @cache_readonly
    def hqic(self):
        ...
    
    @cache_readonly
    def fittedvalues(self):
        ...
    
    @cache_readonly
    def resid(self):
        ...
    
    @Appender(_arma_results_predict)
    def predict(self, start=..., end=..., exog=..., dynamic=..., **kwargs):
        ...
    
    def forecast(self, steps=..., exog=..., alpha=...):
        """
        Out-of-sample forecasts

        Parameters
        ----------
        steps : int
            The number of out of sample forecasts from the end of the
            sample.
        exog : ndarray
            If the model is an ARMAX, you must provide out of sample
            values for the exogenous variables. This should not include
            the constant. The number of observation in exog must match the
            value of steps.
        alpha : float
            The confidence intervals for the forecasts are (1 - alpha) %

        Returns
        -------
        forecast : ndarray
            Array of out of sample forecasts
        stderr : ndarray
            Array of the standard error of the forecasts.
        conf_int : ndarray
            2d array of the confidence interval for the forecast
        """
        ...
    
    def summary(self, alpha=...):
        """Summarize the Model

        Parameters
        ----------
        alpha : float, optional
            Significance level for the confidence intervals.

        Returns
        -------
        smry : Summary instance
            This holds the summary table and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary
        """
        ...
    
    def summary2(self, title=..., alpha=..., float_format=...):
        """
        Experimental summary function for ARIMA Results

        Parameters
        ----------
        title : str, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float, optional
            significance level for the confidence intervals
        float_format : str, optional
            print format for floats in parameters summary

        Returns
        -------
        smry : Summary instance
            This holds the summary table and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary2.Summary : class to hold summary
            results
        """
        ...
    
    @Appender(_plot_predict)
    def plot_predict(self, start=..., end=..., exog=..., dynamic=..., alpha=..., plot_insample=..., ax=...):
        ...
    


class ARMAResultsWrapper(wrap.ResultsWrapper):
    _attrs = ...
    _wrap_attrs = ...
    _methods = ...
    _wrap_methods = ...


class ARIMAResults(ARMAResults):
    @Appender(_arima_results_predict)
    def predict(self, start=..., end=..., exog=..., typ=..., dynamic=...):
        ...
    
    def forecast(self, steps=..., exog=..., alpha=...):
        """
        Out-of-sample forecasts

        Parameters
        ----------
        steps : int
            The number of out of sample forecasts from the end of the
            sample.
        exog : ndarray
            If the model is an ARIMAX, you must provide out of sample
            values for the exogenous variables. This should not include
            the constant. The number of observation in exog must match the
            value of steps.
        alpha : float
            The confidence intervals for the forecasts are (1 - alpha) %

        Returns
        -------
        forecast : ndarray
            Array of out of sample forecasts
        stderr : ndarray
            Array of the standard error of the forecasts.
        conf_int : ndarray
            2d array of the confidence interval for the forecast

        Notes
        -----
        Prediction is done in the levels of the original endogenous variable.
        If you would like prediction of differences in levels use `predict`.
        """
        ...
    
    @Appender(_arima_plot_predict)
    def plot_predict(self, start=..., end=..., exog=..., dynamic=..., alpha=..., plot_insample=..., ax=...):
        ...
    


class ARIMAResultsWrapper(ARMAResultsWrapper):
    ...

