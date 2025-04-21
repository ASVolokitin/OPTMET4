f = lambda x1, x2 : 6 * x1*x1 + x2*x2 - x1 * x2 + 4 * x1 - 8 * x2 + 1
df1 = lambda x1, x2 : 12 * x1 - x2 + 4
df2 = lambda x1, x2: 2 * x2 - x1 - 8

M_0 = (2, 2)
E = 0.00001
H_0 = 0.25
L_BORDER = -100
R_BORDER = 100

def get_grad(x, y):
    return df1(x, y), df2(x, y)

def get_vector_norm(vector):
    return (vector[0]*vector[0] + vector[1]*vector[1])**0.5

def print_min_coords(x1, x2, func):
    print(f"Минимум функции найден в точке ({round(x1, 5), round(x2, 5)}) и равен {round(func(x1, x2), 5)}")

def golden_ratio(func, accuracy=E, a=L_BORDER, b=R_BORDER):
    # print("Итерация 0")
    x1 = a + 0.382 * (b - a)
    # print(f"x1 = a + 0.382 * (b - a) = {round(x1, 4)}")
    x2 = a + 0.618 * (b - a)
    # print(f"x2 = a + 0.618 * (b - a) = {round(x2, 4)}")
    y1 = func(x1)
    # print(f"y1 = f(x1) = {round(y1, 4)}")
    y2 = func(x2)
    # print(f"y2 = f(x2) = {round(y2, 4)}")
    # print(x1, x2, y1, y2)
    iteration_counter = 1
    while abs(b - a) >= accuracy:
        # print(f"Итерация {iteration_counter}")
        if y1 < y2:
            # print("y1 < y2 => оставляем отрезок [a; x2]")
            # print(f"x2 = x1 = {round(x1, 4)}")
            # print(f"y2 = y1 = {round(y1, 4)}")
            # print(f"b = x2 = {round(x2, 4)}")
            b, x2, y2 = x2, x1, y1
            x1 = a + 0.382 * (b - a)
            # print(f"x1 = a + 0.382 * (b - a) = {round(x1, 4)}")
            y1 = func(x1)
            # print(f"y1 = f(x1) = {round(y1, 4)}")
        else:
            # print("y1 >= y2 => оставляем отрезок [x1; b]")
            a, x1, y1 = x1, x2, y2
            # print(f"a = x1 = {round(x1, 4)}")
            # print(f"x1 = x2 = {round(x2, 4)}")
            # print(f"y1 = y2 = {round(y2, 4)}")
            x2 = a + 0.618 * (b - a)
            # print(f"x2 = a + 0.618 * (b - a) = {round(x2, 4)}")
            y2 = func(x2)
            # print(f"y2 = f(x2) = {round(y2, 4)}")
        iteration_counter += 1

    # print(f"|b - a| = {round(abs(b - a), 4)} < E, то есть условие окончания выполнено, значит значение найдено.")
    return (a + b) / 2