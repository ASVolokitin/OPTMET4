from utils import f, golden_ratio


def minimise_argument(func, fixed_val, idx):

    def phi(alpha):
        args = [fixed_val, fixed_val]
        args[idx] = alpha
        return func(*args)

    return golden_ratio(phi)


def coordinate_descent(m, e):
    prev_m = (0, 0)
    cur_m = m
    while (prev_m[0] - cur_m[0]) ** 2 + (prev_m[1] - cur_m[1]) ** 2 > e:
        x1 = minimise_argument(f, cur_m[1], 0)
        x2 = minimise_argument(f, x1, 1)

        prev_m = cur_m
        cur_m = (x1, x2)

    return cur_m
