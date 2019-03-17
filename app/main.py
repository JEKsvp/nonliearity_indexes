import app.test_sequences as ts
import app.state_matrix as sm
import matplotlib.pyplot as plt
import numpy as np

D = 4
lag = 1
pow = 1

eno = ts.eno(1.4, 0.3, 0, 0, 1000)
X = eno
states = sm.state_matrix(X, D, lag, pow)
X = X[D * lag:len(X)]
alpha = np.linalg.lstsq(states, X)
X_ = np.matmul(np.array(states), alpha[0])
plt.plot(X)
plt.plot(X_)
plt.show()
