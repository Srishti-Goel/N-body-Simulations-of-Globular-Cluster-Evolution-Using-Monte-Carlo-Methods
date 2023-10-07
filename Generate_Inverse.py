
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Computational constants
STEP_SIZE = 0.0001
LENGTH_SCALE = 1
Inverse_CDF = np.array([0])
# CDF(r) = 1.5(sin(alpha) - sin^3(alpha)/3) where alpha = tan-1(r)
# CDF(r) = 1.5 (1 + (2/3)r**2) r / (r**2 + 1)**1.5


# Save the matrix [x-values] where the index is a multiple of the y-value

# Generate by finding roots of y = F(x) = 0.001 by Bisection method or something

# Finding roots is feasible here because I'm allowed to take forever to generate and save this matrix

def f(r):
    num = (2*r**3) + (3*r*LENGTH_SCALE**2)
    deno = pow(((r**2) + (LENGTH_SCALE**2)), 1.5)

    return .5 * num / deno

# Or do inverse slope
def f_dash(r):
    num = LENGTH_SCALE**4
    deno = pow((r**2 + LENGTH_SCALE**2), 2.5)
    return 1.5 * num / deno

r = 0
cdf_temp = 0
cdf_obtained = []
for i in range(int(1/STEP_SIZE)):
    r += STEP_SIZE / f_dash(r)
    cdf_temp += STEP_SIZE
    Inverse_CDF = np.append(Inverse_CDF, r)
    cdf_obtained.append(i*STEP_SIZE - f(r))
    if abs(f(r) - cdf_temp) > 0.0025:
        print("Error at r=", r, "of", f(r) - cdf_temp)
    # print(CDF)
print(Inverse_CDF)
cdf_oracle = [f(r / 100) for r in range(300)]
# plt.plot(Inverse_CDF, np.array(range(10001))/10000)
# plt.plot(cdf_oracle)
# plt.show()

plt.plot(cdf_obtained)
plt.show()

with open("inverse_CDF_plummer.pickle", "wb") as meow:
    pickle.dump(Inverse_CDF, meow)