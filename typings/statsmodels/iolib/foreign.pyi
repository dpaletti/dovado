"""
This type stub file was generated by pyright.
"""

"""
Input/Output tools for working with binary data.

The Stata input tools were originally written by Joe Presbrey as part of PyDTA.

You can find more information here http://presbrey.mit.edu/PyDTA

See Also
--------
numpy.lib.io
"""
_date_formats = ["%tc", "%tC", "%td", "%tw", "%tm", "%tq", "%th", "%ty"]
class _StataVariable(object):
    """
    A dataset variable.  Not intended for public use.

    Parameters
    ----------
    variable_data

    Attributes
    ----------
    format : str
        Stata variable format.  See notes for more information.
    index : int
        Zero-index column index of variable.
    label : str
        Data Label
    name : str
        Variable name
    type : str
        Stata data type.  See notes for more information.
    value_format : str
        Value format.

    Notes
    -----
    More information: http://www.stata.com/help.cgi?format
    """
    def __init__(self, variable_data) -> None:
        ...
    
    def __int__(self) -> int:
        """the variable's index within an observation"""
        ...
    
    def __str__(self) -> str:
        """the name of the variable"""
        ...
    
    @property
    def index(self):
        """the variable's index within an observation"""
        ...
    
    @property
    def type(self):
        """
        The data type of variable

        Possible types are:
        {1..244:string, b:byte, h:int, l:long, f:float, d:double)
        """
        ...
    
    @property
    def name(self):
        """the name of the variable"""
        ...
    
    @property
    def format(self):
        """the variable's Stata format"""
        ...
    
    @property
    def value_format(self):
        """the variable's value format"""
        ...
    
    @property
    def label(self):
        """The variable's label"""
        ...
    


class StataReader(object):
    """
    Stata .dta file reader.

    .. deprecated:: 0.11

       Use pandas.read_stata or pandas.io.stata.StataReader

    Provides methods to return the metadata of a Stata .dta file and
    a generator for the data itself.

    Parameters
    ----------
    file : file-like
        A file-like object representing a Stata .dta file.
    missing_values : bool
        If missing_values is True, parse missing_values and return a
        Missing Values object instead of None.
    encoding : str, optional
        Used for Python 3 only. Encoding to use when reading the .dta file.
        Defaults to `locale.getpreferredencoding`

    See Also
    --------
    statsmodels.iolib.foreign.genfromdta
    pandas.read_stata
    pandas.io.stata.StataReader

    Notes
    -----
    This is known only to work on file formats 113 (Stata 8/9), 114
    (Stata 10/11), and 115 (Stata 12).  Needs to be tested on older versions.
    Known not to work on format 104, 108. If you have the documentation for
    older formats, please contact the developers.

    For more information about the .dta format see
    http://www.stata.com/help.cgi?dta
    http://www.stata.com/help.cgi?dta_113
    """
    _header = ...
    _data_location = ...
    _col_sizes = ...
    _has_string_data = ...
    _missing_values = ...
    DTYPE_MAP = ...
    TYPE_MAP = ...
    MISSING_VALUES = ...
    def __init__(self, fname, missing_values=..., encoding=...) -> None:
        ...
    
    def file_headers(self):
        """
        Returns all .dta file headers.

        out: dict
            Has keys typlist, data_label, lbllist, varlist, nvar, filetype,
            ds_format, nobs, fmtlist, vlblist, time_stamp, srtlist, byteorder
        """
        ...
    
    def file_format(self):
        """
        Returns the file format.

        Returns
        -------
        out : int

        Notes
        -----
        Format 113: Stata 8/9
        Format 114: Stata 10/11
        Format 115: Stata 12
        """
        ...
    
    def file_label(self):
        """
        Returns the dataset's label.

        Returns
        -------
        out: str
        """
        ...
    
    def file_timestamp(self):
        """
        Returns the date and time Stata recorded on last file save.

        Returns
        -------
        out : str
        """
        ...
    
    def variables(self):
        """
        Returns a list of the dataset's StataVariables objects.
        """
        ...
    
    def dataset(self, as_dict=...):
        """
        Returns a Python generator object for iterating over the dataset.


        Parameters
        ----------
        as_dict : bool, optional
            If as_dict is True, yield each row of observations as a dict.
            If False, yields each row of observations as a list.

        Returns
        -------
        Generator object for iterating over the dataset.  Yields each row of
        observations as a list by default.

        Notes
        -----
        If missing_values is True during instantiation of StataReader then
        observations with StataMissingValue(s) are not filtered and should
        be handled by your application.
        """
        ...
    
    def __len__(self):
        """
        Return the number of observations in the dataset.

        This value is taken directly from the header and includes observations
        with missing values.
        """
        ...
    
    def __getitem__(self, k):
        """
        Seek to an observation indexed k in the file and return it, ordered
        by Stata's output to the .dta file.

        k is zero-indexed.  Prefer using R.data() for performance.
        """
        ...
    


_type_converters = { 253: int,252: int }
class StataWriter(object):
    """
    A class for writing Stata binary dta files from array-like objects

    .. deprecated:: 0.11

       Use pandas.read_stata or pandas.io.stata.StataReader

    Parameters
    ----------
    fname : file path or buffer
        Where to save the dta file.
    data : array_like
        Array-like input to save. Pandas objects are also accepted.
    convert_dates : dict
        Dictionary mapping column of datetime types to the stata internal
        format that you want to use for the dates. Options are
        'tc', 'td', 'tm', 'tw', 'th', 'tq', 'ty'. Column can be either a
        number or a name.
    encoding : str
        Default is latin-1. Note that Stata does not support unicode.
    byteorder : str
        Can be ">", "<", "little", or "big". The default is None which uses
        `sys.byteorder`

    Returns
    -------
    writer : StataWriter instance
        The StataWriter instance has a write_file method, which will
        write the file to the given `fname`.

    Examples
    --------
    >>> writer = StataWriter('./data_file.dta', data)
    >>> writer.write_file()

    Or with dates

    >>> writer = StataWriter('./date_data_file.dta', date, {2 : 'tw'})
    >>> writer.write_file()
    """
    DTYPE_MAP = ...
    TYPE_MAP = ...
    MISSING_VALUES = ...
    def __init__(self, fname, data, convert_dates=..., encoding=..., byteorder=...) -> None:
        ...
    
    def write_file(self):
        ...
    


def genfromdta(fname, missing_flt=..., encoding=..., pandas=..., convert_dates=...):
    """
    Returns an ndarray or DataFrame from a Stata .dta file.

    .. deprecated:: 0.11

       Use pandas.read_stata or pandas.io.stata.StataReader

    Parameters
    ----------
    fname : str or filehandle
        Stata .dta file.
    missing_flt : numeric
        The numeric value to replace missing values with. Will be used for
        any numeric value.
    encoding : str, optional
        Used for Python 3 only. Encoding to use when reading the .dta file.
        Defaults to `locale.getpreferredencoding`
    pandas : bool
        Optionally return a DataFrame instead of an ndarray
    convert_dates : bool
        If convert_dates is True, then Stata formatted dates will be converted
        to datetime types according to the variable's format.
    """
    ...

def savetxt(fname, X, names=..., fmt=..., delimiter=...):
    """
    Save an array to a text file.

    This is just a copy of numpy.savetxt patched to support structured arrays
    or a header of names.  Does not include py3 support now in savetxt.

    Parameters
    ----------
    fname : filename or file handle
        If the filename ends in ``.gz``, the file is automatically saved in
        compressed gzip format.  `loadtxt` understands gzipped files
        transparently.
    X : array_like
        Data to be saved to a text file.
    names : list, optional
        If given names will be the column header in the text file.  If None and
        X is a structured or recarray then the names are taken from
        X.dtype.names.
    fmt : str or sequence of strs
        A single format (%10.5f), a sequence of formats, or a
        multi-format string, e.g. 'Iteration %d -- %10.5f', in which
        case `delimiter` is ignored.
    delimiter : str
        Character separating columns.

    See Also
    --------
    save : Save an array to a binary file in NumPy ``.npy`` format
    savez : Save several arrays into a ``.npz`` compressed archive

    Notes
    -----
    Further explanation of the `fmt` parameter
    (``%[flag]width[.precision]specifier``):

    flags:
        ``-`` : left justify

        ``+`` : Forces to preceed result with + or -.

        ``0`` : Left pad the number with zeros instead of space (see width).

    width:
        Minimum number of characters to be printed. The value is not truncated
        if it has more characters.

    precision:
        - For integer specifiers (eg. ``d,i,o,x``), the minimum number of
          digits.
        - For ``e, E`` and ``f`` specifiers, the number of digits to print
          after the decimal point.
        - For ``g`` and ``G``, the maximum number of significant digits.
        - For ``s``, the maximum number of characters.

    specifiers:
        ``c`` : character

        ``d`` or ``i`` : signed decimal integer

        ``e`` or ``E`` : scientific notation with ``e`` or ``E``.

        ``f`` : decimal floating point

        ``g,G`` : use the shorter of ``e,E`` or ``f``

        ``o`` : signed octal

        ``s`` : str of characters

        ``u`` : unsigned decimal integer

        ``x,X`` : unsigned hexadecimal integer

    This explanation of ``fmt`` is not complete, for an exhaustive
    specification see [1]_.

    References
    ----------
    .. [1] `Format Specification Mini-Language
           <http://docs.python.org/library/string.html#
           format-specification-mini-language>`_, Python Documentation.

    Examples
    --------
    >>> savetxt('test.out', x, delimiter=',')   # x is an array
    >>> savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays
    >>> savetxt('test.out', x, fmt='%1.4e')   # use exponential notation
    """
    ...
