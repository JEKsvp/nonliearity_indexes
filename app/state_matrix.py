def state_matrix(X, D, lag, pow):
    def get_current_vector(X, D, lag, i):
        result = []
        for j in range(1, D + 1):
            for k in range(pow):
                p = k + 1
                result.append(X[i - lag * j] ** p)
        return result

    A = []
    for i in range(D * lag, len(X)):
        A.append(get_current_vector(X, D, lag, i))
    return A