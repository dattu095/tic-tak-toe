print("give the coords the square picked(x, y):", end=" ")
coords = input().split(",")

if len(coords) == 2:
    print(f"x_coords: {int(coords[0])}, y_coords: {int(coords[1])}")
