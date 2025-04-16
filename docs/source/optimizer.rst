Optimizer Internals
===================

The mechanism of the optimizer is the following:

The algorithm uses scipy's SLSQP (Sequential Least Squares Programming) to 
solve the optimization problem, namely, minimize the portfolio's variance for
a given return. This way we sweep through the the efficient frontier.

After taking all elements from the efficient frontier, we can find the optimal
we select the weight of the portfolio that maximizes the Sharpe ratio.

The constraints are the following:
1. The sum of the weights must be equal to 1.
2. The weights must be between 0 and 0.3.
3. The expected return of the portfolio must be equal to the target return.
