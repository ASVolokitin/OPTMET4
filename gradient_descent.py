from utils import df1, df2, f


def gradient_descent(m, h0, e):
    x1_old = m[0]
    x2_old = m[1]
    h_cur = h0

    while True:
        x1_new = x1_old - h_cur * df1(x1_old, x2_old)
        x2_new = x2_old - h_cur * df2(x1_old, x2_old)

        if f(x1_new, x2_new) >= f(x1_old, x2_old): h_cur /= 2
        if abs(f(x1_old, x2_old) - f(x1_new, x2_new)) < e: return x1_new, x2_new

        x1_old = x1_new
        x2_old = x2_new


