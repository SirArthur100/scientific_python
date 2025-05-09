How to use the package?
========================

A simple example of how to use the package is as follows:
-----------------------------


A small demonstration of how to use the package can be found:
-----------------------------
https://colab.research.google.com/drive/1-wyukil-5yji3M3_iwRqz2FK-THGfCP9?usp=sharing

.. code-block::
   :caption: Install package

        !pip install markowitz_portfolio_optimizer


.. code-block::
   :caption: Imports

        import matplotlib.pyplot as plt
        from markowitz_portfolio_optimizer.data_utils import data_loader
        from markowitz_portfolio_optimizer.calc_utils import markowitz_optimizer
        from importlib.resources import files

.. code-block::
   :caption: Load data

       data_path = files("markowitz_portfolio_optimizer.data").joinpath("example_dataset.csv")
       df = data_loader(data_path)

.. code-block::
   :caption: Run optimizer

       res = markowitz_optimizer(df)

.. code-block::
   :caption: Plot efficient horizon

       fig, ax = plt.subplots(figsize=(8, 6))
       res.plot_efficient_horizon(ax)

.. code-block::
   :caption: Plot the optimal portfolio

       fig, ax = plt.subplots(figsize=(8, 6))
       res.plot_optimal_weights(ax)

Extra API
-----------------------------
The data_utils.OptimRes class contains the functions for plotting and
contains every calculated data from the optimization:

* weights: np.ndarray
* means: np.ndarray
* stds: np.ndarray
* sharpe_array: np.ndarray
* return_array: np.ndarray
* variance_array: np.ndarray

Logging
-----------------------------
A log file with INFO level logging is created in the root directory of the project.