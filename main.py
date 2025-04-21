from coordinate_descent import coordinate_descent
from gradient_descent import gradient_descent
from steepest_descent import steepest_descent
from utils import M_0, H_0, E, print_min_coords, f

coord_x1, coord_x2 = coordinate_descent(M_0, E)
grad_x1, grad_x2 = gradient_descent(M_0, H_0, E)
steep_x1, steep_x2 = steepest_descent(M_0, E)

print("Координатный спуск:")
print_min_coords(coord_x1, coord_x2, f)
print("Градиентный спуск:")
print_min_coords(grad_x1, grad_x2, f)
print("Наискорейший спуск:")
print_min_coords(steep_x1, steep_x2, f)