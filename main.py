import numpy as np
from matplotlib import pyplot as plt

# Define physical constants
g = 9.8
L = 1
mu = 0.1

# Define initial condition
THETA_0 = np.pi / 3  # 60 degrees
THETA_DOT_0 = 0  # Initial angular velocity

thetas = []
thetas_dots = []

thetas.append(THETA_0)
thetas_dots.append(THETA_DOT_0)

delta_t = 0.001  # time step


# Define the ODE
def get_theta_double_dot(theta_, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta_)


# Solve ODE
def theta(t):
    # Initialize changing values
    theta = THETA_0
    theta_dot = THETA_DOT_0
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(theta, theta_dot)
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
        thetas.append(theta)
        thetas_dots.append(theta_dot)
    return theta

t = 90
theta(t)
t_plt = np.arange(0, t+delta_t, delta_t)

print(len(t_plt))
print(len(thetas))
plt.figure()
plt.plot(t_plt, thetas)
plt.figure()
plt.plot(thetas, thetas_dots)
plt.show()
