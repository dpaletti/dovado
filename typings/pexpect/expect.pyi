"""
This type stub file was generated by pyright.
"""

class Expecter(object):
    def __init__(self, spawn, searcher, searchwindowsize=...) -> None:
        ...
    
    def do_search(self, window, freshlen):
        ...
    
    def existing_data(self):
        ...
    
    def new_data(self, data):
        ...
    
    def eof(self, err=...):
        ...
    
    def timeout(self, err=...):
        ...
    
    def errored(self):
        ...
    
    def expect_loop(self, timeout=...):
        """Blocking expect"""
        ...
    


class searcher_string(object):
    '''This is a plain string search helper for the spawn.expect_any() method.
    This helper class is for speed. For more powerful regex patterns
    see the helper class, searcher_re.

    Attributes:

        eof_index     - index of EOF, or -1
        timeout_index - index of TIMEOUT, or -1

    After a successful match by the search() method the following attributes
    are available:

        start - index into the buffer, first byte of match
        end   - index into the buffer, first byte after match
        match - the matching string itself

    '''
    def __init__(self, strings) -> None:
        '''This creates an instance of searcher_string. This argument 'strings'
        may be a list; a sequence of strings; or the EOF or TIMEOUT types. '''
        ...
    
    def __str__(self) -> str:
        '''This returns a human-readable string that represents the state of
        the object.'''
        ...
    
    def search(self, buffer, freshlen, searchwindowsize=...):
        '''This searches 'buffer' for the first occurrence of one of the search
        strings.  'freshlen' must indicate the number of bytes at the end of
        'buffer' which have not been searched before. It helps to avoid
        searching the same, possibly big, buffer over and over again.

        See class spawn for the 'searchwindowsize' argument.

        If there is a match this returns the index of that string, and sets
        'start', 'end' and 'match'. Otherwise, this returns -1. '''
        ...
    


class searcher_re(object):
    '''This is regular expression string search helper for the
    spawn.expect_any() method. This helper class is for powerful
    pattern matching. For speed, see the helper class, searcher_string.

    Attributes:

        eof_index     - index of EOF, or -1
        timeout_index - index of TIMEOUT, or -1

    After a successful match by the search() method the following attributes
    are available:

        start - index into the buffer, first byte of match
        end   - index into the buffer, first byte after match
        match - the re.match object returned by a successful re.search

    '''
    def __init__(self, patterns) -> None:
        '''This creates an instance that searches for 'patterns' Where
        'patterns' may be a list or other sequence of compiled regular
        expressions, or the EOF or TIMEOUT types.'''
        ...
    
    def __str__(self) -> str:
        '''This returns a human-readable string that represents the state of
        the object.'''
        ...
    
    def search(self, buffer, freshlen, searchwindowsize=...):
        '''This searches 'buffer' for the first occurrence of one of the regular
        expressions. 'freshlen' must indicate the number of bytes at the end of
        'buffer' which have not been searched before.

        See class spawn for the 'searchwindowsize' argument.

        If there is a match this returns the index of that string, and sets
        'start', 'end' and 'match'. Otherwise, returns -1.'''
        ...
    

