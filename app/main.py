import app.test_sequences as ts
import app.state_matrix as sm
import app.error_calculator as ec
import matplotlib.pyplot as plt
import numpy as np

D = 4
lag = 1
pow = 1

eno = ts.eno(1.4, 0.3, 0, 0, 100)
X = eno
states = sm.state_matrix(X, D, lag, pow)
X = X[D * lag:len(X)]
alpha = np.linalg.lstsq(states, X)
X_ = np.dot(np.array(states), alpha[0])
E2 = ec.calculate_error(X, X_, D, lag)
print("E^2 = " + str(E2))
plt.plot(X)
plt.plot(X_)
plt.show()
