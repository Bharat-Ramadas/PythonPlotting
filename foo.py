"""
Autodocs4 trial
"""

from typing import Protocol, runtime_checkable, Any, List
from abc import abstractmethod, ABC
from copy import deepcopy
import os
import sys

import pygmo as pg
import pandas as pd
import numpy as np
import pickle

class Foo:
    """This is the Foo class.
    Real time doc update check.
    
    Create powerful Foo objects for generating foobars
    Attributes
    ----------
    power (int): 
        Amount of bar energy contained in this Foo instance.
    Parameters
    ----------
    barPower : int
        The bar energy to be contained in this Foo instance.
    
    Raises
    ------
    AssertError 
        If barPower is less than 6, crap itself.
    """
    
    def __init__(self):
      pass

class Foo2:
    """This is the Foo2 class.
    Real time doc update check.
    
    Create powerful Foo objects for generating foobars
    Attributes
    ----------
    power (int): 
        Amount of bar energy contained in this Foo instance.
    Parameters
    ----------
    barPower : int
        The bar energy to be contained in this Foo instance.
    
    Raises
    ------
    AssertError 
        If barPower is less than 6, crap itself.
    """
    
    def __init__(self):
      pass
