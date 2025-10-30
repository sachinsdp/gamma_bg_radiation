
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import quad

# Define the Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))

# Generate sample data with noise
x_data = np.linspace(0, 10, 100)
y_data = gaussian(x_data, 2.0, 5.0, 1.0) + np.random.normal(0, 0.1, len(x_data))

# Fit the data to the Gaussian function
initial_guess = [1.0, 4.0, 0.5]  # Initial values for amplitude, mean, and standard deviation
params, _ = curve_fit(gaussian, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
amplitude, mean, stddev = params

# Define the range for integration (you can adjust this as needed)
lower_limit = mean - 3 * stddev
upper_limit = mean + 3 * stddev

# Calculate the area under the Gaussian curve using numerical integration
area, _ = quad(gaussian, lower_limit, upper_limit, args=(amplitude, mean, stddev))

print(area)

# Generate the fitted curve
y_fit = gaussian(x_data, amplitude, mean, stddev)

# Plot the original data and the fitted Gaussian curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, 'r', label='Fitted Gaussian')
plt.fill_between(x_data, y_fit, where=(x_data >= lower_limit) & (x_data <= upper_limit), alpha=0.5, color='red', label='AUC')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Gaussian Curve Fit and Area Under the Curve')
plt.grid(True)
plt.show()

# Display the calculated area under the curve
print(f'Area under the Gaussian curve: {area:.2f}')


'''import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))

# Generate sample data with noise
x_data = np.linspace(0, 10, 100)
y_data = gaussian(x_data, 2.0, 5.0, 1.0) + np.random.normal(0, 0.1, len(x_data))

# Fit the data to the Gaussian function
initial_guess = [1.0, 4.0, 0.5]  # Initial values for amplitude, mean, and standard deviation
params, covariance = curve_fit(gaussian, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
amplitude, mean, stddev = params

# Generate the fitted curve
y_fit = gaussian(x_data, amplitude, mean, stddev)

# Plot the original data and the fitted Gaussian curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, 'r', label='Fitted Gaussian')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Gaussian Curve Fit')
plt.grid(True)
plt.show()

# Display the fitted parameters
print(f'Amplitude: {amplitude:.2f}')
print(f'Mean: {mean:.2f}')
print(f'Standard Deviation: {stddev:.2f}')


import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

# Sample data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1.2, 3.1, 7.2, 13.8, 24.5])

# Fit a polynomial of degree 2 (quadratic)
degree = 2
coefficients = np.polyfit(x_data, y_data, degree)

# Create a polynomial function based on the coefficients
poly_func = np.poly1d(coefficients)

# Generate points for the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = poly_func(x_fit)

# Plot the original data and the fitted polynomial curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, 'r', label=f'Fitted Polynomial (Degree {degree})')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Polynomial Curve Fit')
plt.grid(True)
plt.show()

# Display the coefficients of the fitted polynomial
print(f'Fitted Polynomial Coefficients (Degree {degree}):')
for i, coeff in enumerate(reversed(coefficients)):
    print(f'Coefficient {i}: {coeff}')




# Define a linear function
def linear_func(x, a, b):
    return a * x + b

# Generate some sample data with noise
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.1, 3.9, 6.2, 8.1, 9.8])

# Fit the data to the linear function
params, covariance = curve_fit(linear_func, x_data, y_data)

# Extract the coefficients (a and b)
a, b = params

# Generate the fitted curve
y_fit = linear_func(x_data, a, b)

# Plot the original data and the fitted curve
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_fit, 'r', label='Fitted Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear Curve Fit')
plt.grid(True)
plt.show()

# Display the coefficients (slope and intercept)
print("Slope (a):", a)
print("Intercept (b):", b)'''

