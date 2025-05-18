import math


def square(side_length):
    area = side_length * side_length
    return math.ceil(area) if not side_length.is_integer() else area


side = float(input("Введите длину стороны квадрата: "))
result = square(side)
print(f"Площадь квадрата со стороной {side}: {result}")
