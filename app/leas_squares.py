import app.state_matrix as sm
import app.error_calculator as ec
import numpy as np

def calculate_with_error(X, D, lag, pow):
    states = sm.state_matrix(X, D, lag, pow)
    X = X[D * lag:len(X)]
    alpha = np.linalg.lstsq(states, X)
    X_ = np.dot(np.array(states), alpha[0])
    E2 = ec.calculate_error(X, X_, D, lag)
    return X, X_, E2