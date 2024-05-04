from math import sqrt, pi, exp

r = 3.05
r_dash = 0.7788 * r

d12 = d16 = d17 = 2 * 2
d14 = 4 * r
d13 = d15 = 2 * sqrt(3) * r

exp1 = (r_dash * 2 * r * 2 * sqrt(3) * r * 4 * r * 2 * sqrt(3) * r * 2 * r * 2 * r) ** 6
exp2 = r_dash * (2 * r) ** 6
gmr = (exp1 * exp2) ** (1 / 49)
print(gmr)

Ac = 1400  # area of conductor in mm^2

gmr2 = exp(1 / 4) * sqrt(Ac / pi)  # sector conductor

print(gmr2)
