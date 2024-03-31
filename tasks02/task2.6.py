import math

alpha = [54.80, 54.06, 53.34]
beta = [65.59, 64.59, 63.62]
a = 500
t = 1


def fx(alpha, beta):
    return a * (
        math.tan(math.radians(beta))
        / (math.tan(math.radians(beta)) - math.tan(math.radians(alpha)))
    )


def fy(alpha, beta):
    return a * (
        math.tan(math.radians(alpha))
        * math.tan(math.radians(beta))
        / (math.tan(math.radians(beta)) - math.tan(math.radians(alpha)))
    )


def diffe():
    vx = (fx(alpha[2], beta[2]) - fx(alpha[0], beta[0])) / 2 * t
    vy = (
        (fy(alpha[2], beta[2]) - fy(alpha[0], beta[0])) / 2 * t
    )  # f(1)(x)=(f(x+t)-f(x-t))/2*t
    v = (vx**2 + vy**2) ** (0.5)
    gamma = math.degrees(math.atan(vy / vx))
    print(f"Speed of the plane at t = 10s: {v:.2f} m/s")
    print(f"Climb angle at t = 10s: {gamma:.2f} degrees")
    return


diffe()