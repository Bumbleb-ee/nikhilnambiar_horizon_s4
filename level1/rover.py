import math

try:
    x1 = float(input("Enter origin x1: "))
    y1 = float(input("Enter origin y1: "))
    x2 = float(input("Enter destination x2: "))
    y2 = float(input("Enter destination y2: "))

    u = float(input("Initial velocity (m/s): "))
    a = float(input("Acceleration (m/s^2): "))
    vmax = float(input("Top speed (m/s): "))

    if u > vmax:
        print("Error: Initial velocity cannot be greater than top speed.")
    else:
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        t1 = (vmax - u) / a
        s = u * t1 + 0.5 * a * (t1**2)

        if s >= distance:
            A = 0.5 * a
            B = u
            C = -distance
            t = (-B + math.sqrt(B**2 - 4 * A * C)) / (2 * A)
        else:
            s1 = distance - s
            t = t1 + s1 / vmax

        print("\nDistance to destination:", round(distance, 2), "m")
        print("Time required:", round(t, 2), "seconds")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Acceleration cannot be zero.")