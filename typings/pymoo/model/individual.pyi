"""
This type stub file was generated by pyright.
"""

class Individual:
    def __init__(self, X=..., F=..., CV=..., G=..., feasible=..., **kwargs) -> None:
        ...
    
    def has(self, key):
        ...
    
    def set(self, key, value):
        ...
    
    def copy(self, deep=...):
        ...
    
    def get(self, *keys):
        ...
    


class eIndividual:
    def __init__(self, **kwargs) -> None:
        ...
    
    def has(self, key):
        ...
    
    def set(self, key, val):
        ...
    
    def get(self, *keys):
        ...
    
    def copy(self, deep=...):
        ...
    
    def __getattr__(self, val):
        ...
    
    def __setattr__(self, key, value):
        ...
    

