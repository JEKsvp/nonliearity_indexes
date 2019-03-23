import app.test_sequences as ts
import app.leas_squares as ls
import matplotlib.pyplot as plt
import app.plotter as custom_plt

D = 4
lag = 1
pow = 1

eno = ts.eno(1.4, 0.3, 0, 0, 100)
logistic = ts.logistic(0.4, 2, 100)
XL11, X_L11, E2L11 = ls.calculate_with_error(logistic, D=4, lag=1, pow=1)
XL12, X_L12, E2L12 = ls.calculate_with_error(logistic, D=4, lag=1, pow=2)
XE11, X_E11, E2E11 = ls.calculate_with_error(eno, D=4, lag=1, pow=1)
XE12, X_E12, E2E12 = ls.calculate_with_error(eno, D=4, lag=1, pow=2)

XL21, X_L21, E2L21 = ls.calculate_with_error(logistic, D=4, lag=2, pow=1)
XL22, X_L22, E2L22 = ls.calculate_with_error(logistic, D=4, lag=2, pow=2)
XE21, X_E21, E2E21 = ls.calculate_with_error(eno, D=4, lag=2, pow=1)
XE22, X_E22, E2E22 = ls.calculate_with_error(eno, D=4, lag=2, pow=2)

figure, axes = plt.subplots(nrows=4, ncols=2)
figure.subplots_adjust(hspace=0.6, wspace=.3)

custom_plt.plot(axes[0, 0], XL11, X_L11, E2L11, title="Логистическое отображение", D=4, lag=1, pow=1)
custom_plt.plot(axes[0, 1], XL12, X_L12, E2L12, title="Логистическое отображение", D=4, lag=1, pow=2)
custom_plt.plot(axes[1, 0], XE11, X_E11, E2E11, title="Отображение Эно", D=4, lag=1, pow=1)
custom_plt.plot(axes[1, 1], XE12, X_E12, E2E12, title="Отображение Эно", D=4, lag=1, pow=2)

custom_plt.plot(axes[2, 0], XL21, X_L21, E2L21, title="Логистическое отображение", D=4, lag=2, pow=1)
custom_plt.plot(axes[2, 1], XL22, X_L22, E2L22, title="Логистическое отображение", D=4, lag=2, pow=2)
custom_plt.plot(axes[3, 0], XE21, X_E21, E2E21, title="Отображение Эно", D=4, lag=2, pow=1)
custom_plt.plot(axes[3, 1], XE22, X_E22, E2E22, title="Отображение Эно", D=4, lag=2, pow=2)

plt.show()
