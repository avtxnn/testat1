# Aufgabe 1


def add_numbers(a:float, b:float):
    # Code here
    pass


def rectangle_calculate_area(length:float, width:float):
    # Code here
    pass


def main():
    a, b = 1, 2
    print(f"{a} + {b} = {add_numbers(a, b)}")
    a, b = 1075.046, 3.1415
    print(f"{a} + {b} = {add_numbers(a, b)}")

    a, b = 3, 4
    print(f"Fläche von {a} x {b} cm²: {rectangle_calculate_area(a, b)} cm²")
    a, b = 10.764, 7.432
    print(f"Fläche von {a} x {b} cm²: {rectangle_calculate_area(a, b)} cm²")


if __name__ == "__main__":
    main()
