import math


a = 500

alpha_t_9 = 54.80
beta_t_9 = 65.59

alpha_t11 = 53.34
beta_t11 = 63.62


x = a * (
    math.tan(math.radians(beta_t_9))
    / (math.tan(math.radians(beta_t_9)) - math.tan(math.radians(alpha_t_9)))
)
y = a * (
    math.tan(math.radians(alpha_t_9))
    * math.tan(math.radians(beta_t_9))
    / (math.tan(math.radians(beta_t_9)) - math.tan(math.radians(alpha_t_9)))
)

x1 = a * (
    math.tan(math.radians(beta_t11))
    / (math.tan(math.radians(beta_t11)) - math.tan(math.radians(alpha_t11)))
)
y1 = a * (
    math.tan(math.radians(alpha_t11))
    * math.tan(math.radians(beta_t11))
    / (math.tan(math.radians(beta_t11)) - math.tan(math.radians(alpha_t11)))
)

vx = (x1 - x) / 2
vy = (y1 - y) / 2
v = (vx**2 + vy**2) ** (0.5)

gamma = math.degrees(math.atan(vy / vx))

print(f"Speed of the plane at t = 10s: {v:.2f} m/s")
print(f"Climb angle at t = 10s: {gamma:.2f} degrees")
print(f"Coordinates of the plane at t = 9s: ({x:.2f}, {y:.2f})")
print(f"Coordinates of the plane at t = 11s: ({x1:.2f}, {y1:.2f})")
