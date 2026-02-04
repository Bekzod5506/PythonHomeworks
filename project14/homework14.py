import numpy as np
from PIL import Image


# ============================
# TASK 1 — Fahrenheit to Celsius (vectorize)


def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
vec_convert = np.vectorize(fahrenheit_to_celsius)

temps_c = vec_convert(temps_f)

print("Task 1 — Celsius values:")
print(temps_c)
print()


# ============================
# TASK 2 — Power function (vectorize)


def power(num, p):
    return num ** p

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

vec_power = np.vectorize(power)
result_power = vec_power(numbers, powers)

print("Task 2 — Power results:")
print(result_power)
print()


# ============================
# TASK 3 — Solve linear system


A1 = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B1 = np.array([7, 4, 5])

solution1 = np.linalg.solve(A1, B1)

print("Task 3 — x, y, z:")
print(solution1)
print()


# ============================
# TASK 4 — Electrical currents


A2 = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B2 = np.array([12, -5, 15])

solution2 = np.linalg.solve(A2, B2)

print("Task 4 — I1, I2, I3:")
print(solution2)
print()


# ============================
# IMAGE MANIPULATION SECTION

# Load image using PIL only

image = Image.open("images/birds.jpg")
img_array = np.array(image)


# ---------- Bonus Functions -----------


def flip_image(arr):
    horizontal = np.fliplr(arr)
    vertical = np.flipud(arr)
    return horizontal, vertical


def add_noise(arr, noise_level=25):
    noise = np.random.randint(-noise_level, noise_level, arr.shape)
    noisy = arr + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def brighten_channels(arr, increase=40):
    bright = arr.copy()
    bright[:, :, 0] += increase  
    return np.clip(bright, 0, 255).astype(np.uint8)


def apply_mask(arr, size=100):
    masked = arr.copy()
    h, w, _ = masked.shape

    center_h = h // 2
    center_w = w // 2

    half = size // 2

    masked[
        center_h-half:center_h+half,
        center_w-half:center_w+half
    ] = [0, 0, 0]

    return masked


# ---------- Apply operations -----------

flip_h, flip_v = flip_image(img_array)
noisy_img = add_noise(img_array)
bright_img = brighten_channels(img_array)
masked_img = apply_mask(img_array)




Image.fromarray(flip_h).save("flip_horizontal.jpg")
Image.fromarray(flip_v).save("flip_vertical.jpg")
Image.fromarray(noisy_img).save("noisy.jpg")
Image.fromarray(bright_img).save("brightened.jpg")
Image.fromarray(masked_img).save("masked.jpg")


print("Image processing completed. Files saved:")
print("flip_horizontal.jpg")
print("flip_vertical.jpg")
print("noisy.jpg")
print("brightened.jpg")
print("masked.jpg")
