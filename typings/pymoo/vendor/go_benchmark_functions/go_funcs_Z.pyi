"""
This type stub file was generated by pyright.
"""

from .go_benchmark import Benchmark

class Zacharov(Benchmark):
    r"""
    Zacharov objective function.

    This class defines the Zacharov [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Zacharov}}(x) = \sum_{i=1}^{n} x_i^2 + \left ( \frac{1}{2}
                                 \sum_{i=1}^{n} i x_i \right )^2
                                 + \left ( \frac{1}{2} \sum_{i=1}^{n} i x_i 
                                 \right )^4

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-5, 10]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x_i = 0` for
    :math:`i = 1, ..., n`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class ZeroSum(Benchmark):
    r"""
    ZeroSum objective function.

    This class defines the ZeroSum [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{ZeroSum}}(x) = \begin{cases}
                                0 & \textrm{if} \sum_{i=1}^n x_i = 0 \\
                                1 + \left(10000 \left |\sum_{i=1}^n x_i\right|
                                \right)^{0.5} & \textrm{otherwise}
                                \end{cases}

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-10, 10]` for :math:`i = 1, ..., n`.

    *Global optimum*: :math:`f(x) = 0` where :math:`\sum_{i=1}^n x_i = 0`

    .. [1] Gavana, A. Global Optimization Benchmarks and AMPGO retrieved 2015
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Zettl(Benchmark):
    r"""
    Zettl objective function.

    This class defines the Zettl [1]_ global optimization problem. This is a
    multimodal minimization problem defined as follows:

    .. math::

       f_{\text{Zettl}}(x) = \frac{1}{4} x_{1} + \left(x_{1}^{2} - 2 x_{1}
                             + x_{2}^{2}\right)^{2}


    with :math:`x_i \in [-1, 5]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = -0.0037912` for :math:`x = [-0.029896, 0.0]`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Zimmerman(Benchmark):
    r"""
    Zimmerman objective function.

    This class defines the Zimmerman [1]_ global optimization problem. This
    is a multimodal minimization problem defined as follows:

    .. math::

        f_{\text{Zimmerman}}(x) = \max \left[Zh1(x), Zp(Zh2(x))
                                  \textrm{sgn}(Zh2(x)), Zp(Zh3(x))
                                  \textrm{sgn}(Zh3(x)),
                                  Zp(-x_1)\textrm{sgn}(x_1),
                                  Zp(-x_2)\textrm{sgn}(x_2) \right]


    Where, in this exercise:

    .. math::

        \begin{cases}
        Zh1(x) = 9 - x_1 - x_2 \\
        Zh2(x) = (x_1 - 3)^2 + (x_2 - 2)^2 \\
        Zh3(x) = x_1x_2 - 14 \\
        Zp(t) = 100(1 + t)
        \end{cases}


    Where :math:`x` is a vector and :math:`t` is a scalar.

    Here, :math:`x_i \in [0, 100]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = 0` for :math:`x = [7, 2]`

    .. [1] Gavana, A. Global Optimization Benchmarks and AMPGO retrieved 2015

    TODO implementation from Gavana
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    


class Zirilli(Benchmark):
    r"""
    Zettl objective function.

    This class defines the Zirilli [1]_ global optimization problem. This is a
    unimodal minimization problem defined as follows:

    .. math::

        f_{\text{Zirilli}}(x) = 0.25x_1^4 - 0.5x_1^2 + 0.1x_1 + 0.5x_2^2

    Here, :math:`n` represents the number of dimensions and
    :math:`x_i \in [-10, 10]` for :math:`i = 1, 2`.

    *Global optimum*: :math:`f(x) = -0.3523` for :math:`x = [-1.0465, 0]`

    .. [1] Jamil, M. & Yang, X.-S. A Literature Survey of Benchmark Functions
    For Global Optimization Problems Int. Journal of Mathematical Modelling
    and Numerical Optimisation, 2013, 4, 150-194.
    """
    def __init__(self, dimensions=...) -> None:
        ...
    
    def fun(self, x, *args):
        ...
    

