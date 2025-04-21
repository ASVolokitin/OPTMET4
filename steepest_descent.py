from utils import get_vector_norm, get_grad, f, golden_ratio


def steepest_descent(M_0, e):
    X = M_0
    while get_vector_norm(get_grad(X[0], X[1])) >= e:
        dx, dy = get_grad(X[0], X[1])
        dx *= -1
        dy *= -1
        phi = lambda l: f(X[0] + l * dx, X[1] + l * dy)
        alpha = golden_ratio(phi)
        X = X[0] + alpha * dx, X[1] + alpha * dy
    return X


