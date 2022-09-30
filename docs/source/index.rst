Calculation of blowdown processes from high pressure gas pipelines
==================================================================

GasBlowdownCalculator is a package for the calculation of blowdown processes from 
high pressure gas pipelines.

When operating gas pipelines it is regularly necessary to empty (blowdown) them via 
purge systems. During this blowdown process the pressure drops until equilibrium with 
the environment. One can differ between two phases: the first critical phase and the second 
subcritical phase. 

Starting from a given gas composition and data of the pipeline under focus and 
the purge system consisting of a pipe, a valve, and optionally an orifice,
GasBlowdownCalculator calculates time dependent curves for pressure, linepack, flow 
rate, and flow velocity. In addition, it outputs the blowdown times in total as well as
those of the two - critical and subcritical - phases.

Everybody is welcome to use GasBlowdownCalculator.

Audience
--------

The audience for GasBlowdownCalculator includes engineers, mathematicians, physicists, 
and anyone else who is interested in gas pipeline dynamics.

License
-------

Copyright (C) 2018 Michael Fischer.

GasBlowdownCalculator is open source software; you can redistribute it and/or modify 
it under the terms of the :doc:`GPL-3.0 </license>`.

History
-------

GasBlowdownCalculator was born in 2018. The software was designed and written by 
Michael Fischer.

Installation
------------

GasBlowdownCalculator requires Python 3.7 or higher and builds upon PyQt5 and pyqtgraph. 
It can be installed from Anaconda prompt
using ``pip``.

.. code:: bash

    pip install gasblowdowncalculator

GasBlowdownCalculator additionally requires the external library 
`LibBlowdownCalc <link URL>`_ 
in order to perform actual calculations.

Nevertheless, the software can installed and run without the library as well. In that case,
only dummy simulations can be performed.

Quick start
-----------

After installation GasBlowdownCalculator can be started from Anaconda prompt by

.. code:: bash

    gasblowdowncalculator

or from Python prompt by

.. code:: python

    >>> import gasblowdowncalculator
    >>> gasblowdowncalculator.gasblowdowncalculator.run()

Tutorial
--------

An exemplary application of the software is presented in the :doc:`tutorial <tutorial>`.



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
