"""
This type stub file was generated by pyright.
"""

from statsmodels.base.model import Results
from statsmodels.base.wrapper import ResultsWrapper

class HoltWintersResults(Results):
    """
    Results from fitting Exponential Smoothing models.

    Parameters
    ----------
    model : ExponentialSmoothing instance
        The fitted model instance.
    params : dict
        All the parameters for the Exponential Smoothing model.
    sse : float
        The sum of squared errors.
    aic : float
        The Akaike information criterion.
    aicc : float
        AIC with a correction for finite sample sizes.
    bic : float
        The Bayesian information criterion.
    optimized : bool
        Flag indicating whether the model parameters were optimized to fit
        the data.
    level : ndarray
        An array of the levels values that make up the fitted values.
    trend : ndarray
        An array of the trend values that make up the fitted values.
    season : ndarray
        An array of the seasonal values that make up the fitted values.
    params_formatted : pd.DataFrame
        DataFrame containing all parameters, their short names and a flag
        indicating whether the parameter's value was optimized to fit the data.
    resid : ndarray
        An array of the residuals of the fittedvalues and actual values.
    k : int
        The k parameter used to remove the bias in AIC, BIC etc.
    fittedvalues : ndarray
        An array of the fitted values. Fitted by the Exponential Smoothing
        model.
    fittedfcast : ndarray
        An array of both the fitted values and forecast values.
    fcastvalues : ndarray
        An array of the forecast values forecast by the Exponential Smoothing
        model.
    mle_retvals : {None, scipy.optimize.optimize.OptimizeResult}
        Optimization results if the parameters were optimized to fit the data.
    """
    def __init__(self, model, params, sse, aic, aicc, bic, optimized, level, trend, season, params_formatted, resid, k, fittedvalues, fittedfcast, fcastvalues, mle_retvals=...) -> None:
        ...
    
    @property
    def aic(self):
        """
        The Akaike information criterion.
        """
        ...
    
    @property
    def aicc(self):
        """
        AIC with a correction for finite sample sizes.
        """
        ...
    
    @property
    def bic(self):
        """
        The Bayesian information criterion.
        """
        ...
    
    @property
    def sse(self):
        """
        The sum of squared errors between the data and the fittted value.
        """
        ...
    
    @property
    def model(self):
        """
        The model used to produce the results instance.
        """
        ...
    
    @model.setter
    def model(self, value):
        ...
    
    @property
    def level(self):
        """
        An array of the levels values that make up the fitted values.
        """
        ...
    
    @property
    def optimized(self):
        """
        Flag indicating if model parameters were optimized to fit the data.
        """
        ...
    
    @property
    def slope(self):
        """
        An array of the slope values that make up the fitted values.

        .. deprecated:: 0.12

           Use the trend property instead.
        """
        ...
    
    @property
    def trend(self):
        """
        An array of the trend values that make up the fitted values.
        """
        ...
    
    @property
    def season(self):
        """
        An array of the seasonal values that make up the fitted values.
        """
        ...
    
    @property
    def params_formatted(self):
        """
        DataFrame containing all parameters

        Contains short names and a flag indicating whether the parameter's
        value was optimized to fit the data.
        """
        ...
    
    @property
    def fittedvalues(self):
        """
        An array of the fitted values
        """
        ...
    
    @property
    def fittedfcast(self):
        """
        An array of both the fitted values and forecast values.
        """
        ...
    
    @property
    def fcastvalues(self):
        """
        An array of the forecast values
        """
        ...
    
    @property
    def resid(self):
        """
        An array of the residuals of the fittedvalues and actual values.
        """
        ...
    
    @property
    def k(self):
        """
        The k parameter used to remove the bias in AIC, BIC etc.
        """
        ...
    
    @property
    def mle_retvals(self):
        """
        Optimization results if the parameters were optimized to fit the data.
        """
        ...
    
    @mle_retvals.setter
    def mle_retvals(self, value):
        ...
    
    def predict(self, start=..., end=...):
        """
        In-sample prediction and out-of-sample forecasting

        Parameters
        ----------
        start : int, str, or datetime, optional
            Zero-indexed observation number at which to start forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type. Default is the the zeroth observation.
        end : int, str, or datetime, optional
            Zero-indexed observation number at which to end forecasting, ie.,
            the first forecast is start. Can also be a date string to
            parse or a datetime type. However, if the dates index does not
            have a fixed frequency, end must be an integer index if you
            want out of sample prediction. Default is the last observation in
            the sample.

        Returns
        -------
        forecast : ndarray
            Array of out of sample forecasts.
        """
        ...
    
    def forecast(self, steps=...):
        """
        Out-of-sample forecasts

        Parameters
        ----------
        steps : int
            The number of out of sample forecasts from the end of the
            sample.

        Returns
        -------
        forecast : ndarray
            Array of out of sample forecasts
        """
        ...
    
    def summary(self):
        """
        Summarize the fitted Model

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
    
    def simulate(self, nsimulations, anchor=..., repetitions=..., error=..., random_errors=..., random_state=...):
        r"""
        Random simulations using the state space formulation.

        Parameters
        ----------
        nsimulations : int
            The number of simulation steps.
        anchor : int, str, or datetime, optional
            First period for simulation. The simulation will be conditional on
            all existing datapoints prior to the `anchor`.  Type depends on the
            index of the given `endog` in the model. Two special cases are the
            strings 'start' and 'end'. `start` refers to beginning the
            simulation at the first period of the sample, and `end` refers to
            beginning the simulation at the first period after the sample.
            Integer values can run from 0 to `nobs`, or can be negative to
            apply negative indexing. Finally, if a date/time index was provided
            to the model, then this argument can be a date string to parse or a
            datetime type. Default is 'end'.
        repetitions : int, optional
            Number of simulated paths to generate. Default is 1 simulated path.
        error : {"add", "mul", "additive", "multiplicative"}, optional
            Error model for state space formulation. Default is ``"add"``.
        random_errors : optional
            Specifies how the random errors should be obtained. Can be one of
            the following:

            * ``None``: Random normally distributed values with variance
              estimated from the fit errors drawn from numpy's standard
              RNG (can be seeded with the `random_state` argument). This is the
              default option.
            * A distribution function from ``scipy.stats``, e.g.
              ``scipy.stats.norm``: Fits the distribution function to the fit
              errors and draws from the fitted distribution.
              Note the difference between ``scipy.stats.norm`` and
              ``scipy.stats.norm()``, the latter one is a frozen distribution
              function.
            * A frozen distribution function from ``scipy.stats``, e.g.
              ``scipy.stats.norm(scale=2)``: Draws from the frozen distribution
              function.
            * A ``np.ndarray`` with shape (`nsimulations`, `repetitions`): Uses
              the given values as random errors.
            * ``"bootstrap"``: Samples the random errors from the fit errors.

        random_state : int or np.random.RandomState, optional
            A seed for the random number generator or a
            ``np.random.RandomState`` object. Only used if `random_errors` is
            ``None``. Default is ``None``.

        Returns
        -------
        sim : pd.Series, pd.DataFrame or np.ndarray
            An ``np.ndarray``, ``pd.Series``, or ``pd.DataFrame`` of simulated
            values.
            If the original data was a ``pd.Series`` or ``pd.DataFrame``, `sim`
            will be a ``pd.Series`` if `repetitions` is 1, and a
            ``pd.DataFrame`` of shape (`nsimulations`, `repetitions`) else.
            Otherwise, if `repetitions` is 1, a ``np.ndarray`` of shape
            (`nsimulations`,) is returned, and if `repetitions` is not 1 a
            ``np.ndarray`` of shape (`nsimulations`, `repetitions`) is
            returned.

        Notes
        -----
        The simulation is based on the state space model of the Holt-Winter's
        methods. The state space model assumes that the true value at time
        :math:`t` is randomly distributed around the prediction value.
        If using the additive error model, this means:

        .. math::

            y_t &= \hat{y}_{t|t-1} + e_t\\
            e_t &\sim \mathcal{N}(0, \sigma^2)

        Using the multiplicative error model:

        .. math::

            y_t &= \hat{y}_{t|t-1} \cdot (1 + e_t)\\
            e_t &\sim \mathcal{N}(0, \sigma^2)

        Inserting these equations into the smoothing equation formulation leads
        to the state space equations. The notation used here follows
        [1]_.

        Additionally,

        .. math::

           B_t &= b_{t-1} \circ_d \phi\\
           L_t &= l_{t-1} \circ_b B_t\\
           S_t &= s_{t-m}\\
           Y_t &= L_t \circ_s S_t,

        where :math:`\circ_d` is the operation linking trend and damping
        parameter (multiplication if the trend is additive, power if the trend
        is multiplicative), :math:`\circ_b` is the operation linking level and
        trend (addition if the trend is additive, multiplication if the trend
        is multiplicative), and :math:`\circ_s` is the operation linking
        seasonality to the rest.

        The state space equations can then be formulated as

        .. math::

           y_t &= Y_t + \eta \cdot e_t\\
           l_t &= L_t + \alpha \cdot (M_e \cdot L_t + \kappa_l) \cdot e_t\\
           b_t &= B_t + \beta \cdot (M_e \cdot B_t + \kappa_b) \cdot e_t\\
           s_t &= S_t + \gamma \cdot (M_e \cdot S_t + \kappa_s) \cdot e_t\\

        with

        .. math::

           \eta &= \begin{cases}
                       Y_t\quad\text{if error is multiplicative}\\
                       1\quad\text{else}
                   \end{cases}\\
           M_e &= \begin{cases}
                       1\quad\text{if error is multiplicative}\\
                       0\quad\text{else}
                   \end{cases}\\

        and, when using the additive error model,

        .. math::

           \kappa_l &= \begin{cases}
                       \frac{1}{S_t}\quad
                       \text{if seasonality is multiplicative}\\
                       1\quad\text{else}
                   \end{cases}\\
           \kappa_b &= \begin{cases}
                       \frac{\kappa_l}{l_{t-1}}\quad
                       \text{if trend is multiplicative}\\
                       \kappa_l\quad\text{else}
                   \end{cases}\\
           \kappa_s &= \begin{cases}
                       \frac{1}{L_t}\quad\text{if seasonality is
                                               multiplicative}\\
                       1\quad\text{else}
                   \end{cases}

        When using the multiplicative error model

        .. math::

           \kappa_l &= \begin{cases}
                       0\quad
                       \text{if seasonality is multiplicative}\\
                       S_t\quad\text{else}
                   \end{cases}\\
           \kappa_b &= \begin{cases}
                       \frac{\kappa_l}{l_{t-1}}\quad
                       \text{if trend is multiplicative}\\
                       \kappa_l + l_{t-1}\quad\text{else}
                   \end{cases}\\
           \kappa_s &= \begin{cases}
                       0\quad\text{if seasonality is multiplicative}\\
                       L_t\quad\text{else}
                   \end{cases}

        References
        ----------
        .. [1] Hyndman, R.J., & Athanasopoulos, G. (2018) *Forecasting:
           principles and practice*, 2nd edition, OTexts: Melbourne,
           Australia. OTexts.com/fpp2. Accessed on February 28th 2020.
        """
        ...
    


class HoltWintersResultsWrapper(ResultsWrapper):
    _attrs = ...
    _wrap_attrs = ...
    _methods = ...
    _wrap_methods = ...

