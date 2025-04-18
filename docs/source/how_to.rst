How to use the package?
========================

A simple example of how to use the package is as follows:
-----------------------------


* Import necessary modules

``import matplotlib.pyplot as plt
from portfolio_optimizer.data_utils import data_loader
from portfolio_optimizer.calc_utils import markowitz_optimizer``

* Load data

``df = data_loader("./example_dataset.csv")``

* Run optimizer

``res = markowitz_optimizer(df)``

* Plot the efficient frontier
 
``fig, ax = plt.subplots(figsize=(8, 6))
res.plot_efficient_horizon(ax)``

* Plot the optimal portfolio

``fig, ax = plt.subplots(figsize=(8, 6))
res.plot_optimal_weights(ax)``

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