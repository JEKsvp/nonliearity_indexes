def plot(axes, X, X_, E2, title, lag, D, pow):
    axes.set_title("{0}, D={1}, lag={2}, P={3},"
                         " \n E^2={4}".format(title, str(D), str(lag), str(pow), str(E2)),
                   fontsize=10)
    axes.plot(X)
    axes.plot(X_)
