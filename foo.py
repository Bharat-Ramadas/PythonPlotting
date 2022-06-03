"""
Kobin class
===========
The Kobin instance are callable WSGI Application.
Usage
-----
.. code-block:: python
   from kobin import Kobin, Response
   app = Kobin()
   @app.route('/')
   def index() -> Response:
       return Response('Hello World')
"""
import numpy as np


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
