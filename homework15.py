import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# 1. Basic Plotting

x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

plt.figure()
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("f(x) = x² - 4x + 4")
plt.show()


# -----------------------------
# 2. Sine and Cosine Plot

x = np.linspace(0, 2*np.pi, 400)

plt.figure()
plt.plot(x, np.sin(x), linestyle='-', marker='o', color='blue', label='sin(x)')
plt.plot(x, np.cos(x), linestyle='--', marker='x', color='red', label='cos(x)')
plt.xlabel("x")
plt.ylabel("Value")
plt.title("Sine and Cosine")
plt.legend()
plt.show()


# -----------------------------
# 3. Subplots (2x2)

x = np.linspace(0, 2, 400)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x**3, color='purple')
axs[0, 0].set_title("x³")

axs[0, 1].plot(x, np.sin(x), color='green')
axs[0, 1].set_title("sin(x)")

axs[1, 0].plot(x, np.exp(x), color='orange')
axs[1, 0].set_title("eˣ")

axs[1, 1].plot(x, np.log(x + 1), color='brown')
axs[1, 1].set_title("log(x+1)")

for ax in axs.flat:
    ax.set_xlabel("x")
    ax.set_ylabel("y")

plt.tight_layout()
plt.show()


# -----------------------------
# 4. Scatter Plot
# -----------------------------
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

plt.figure()
plt.scatter(x, y, color='blue', marker='o')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Random Scatter Plot")
plt.grid(True)
plt.show()


# -----------------------------
# 5. Histogram
# -----------------------------
data = np.random.normal(0, 1, 1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normal Distribution")
plt.show()


# -----------------------------
# 6. 3D Surface Plot

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("3D Surface Plot: cos(x² + y²)")

fig.colorbar(surface)
plt.show()


# -----------------------------
# 7. Bar Chart

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]

plt.figure()
plt.bar(products, sales, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")
plt.show()


# -----------------------------
# 8. Stacked Bar Chart

time_periods = ['T1', 'T2', 'T3', 'T4']

category_A = [20, 35, 30, 35]
category_B = [25, 32, 34, 20]
category_C = [15, 20, 25, 30]

plt.figure()

plt.bar(time_periods, category_A, label='Category A')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B')
plt.bar(
    time_periods,
    category_C,
    bottom=np.array(category_A) + np.array(category_B),
    label='Category C'
)

plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.title("Stacked Bar Chart")
plt.legend()
plt.show()
