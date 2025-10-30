"""
Sachin Shet
11/10/2023
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
from scipy.integrate import quad

channels = np.array(0)
counts   =np.array(0)

csv_file_path = 'data.csv'

with open(csv_file_path, mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        # You can access individual columns by indexing the list
        #print(row)
        channels = np.append(channels, int(row[0]))
        counts = np.append(counts, int(row[1]))

plt.scatter(channels, counts, marker='o', s=1)
plt.show()

#██████████████████████████████████████████████████████████████████████████████
'''
            Peak finding
'''
peaks, _ = find_peaks(counts, height=5000, threshold=10, distance=50, prominence=50)
print("The identified peaks channels are = ", peaks,'\n')

#██████████████████████████████████████████████████████████████████████████████
'''
Calibration
    Energy of gamma lines used for the calibration  
'''
energy = np.array([662,1173,1332])

print("Gamma lines used for the calibrations = ", energy,'\n')
channels_calib = np.array(peaks[1:4])
plt.scatter(channels_calib, energy, marker='o', color='red', label='Expt Data')
plt.legend()

# Fit a polynomial of degree 2 (quadratic)
degree = 2
coefficients = np.polyfit(channels_calib, energy, degree)

# Create a polynomial function based on the coefficients
poly_func = np.poly1d(coefficients)

# Generate points for the fitted curve
x_fit = np.linspace(min(channels_calib), max(channels_calib), 30)
y_fit = poly_func(x_fit)

plt.plot(x_fit, y_fit, 'b', label=f'Fitted Polynomial (Degree {degree})')

plt.legend()
plt.show()

# Display the coefficients of the fitted polynomial

print('y = a * x^2 + b*x + c')

print(f'Fitted Polynomial Coefficients (Degree {degree}):')
for i, coeff in enumerate(reversed(coefficients)):
    print(f'Coefficient {i}: {coeff}')

#print(coefficients[0],coefficients[1],coefficients[2])
#### unidentified peak at a channel X corresponds to the energy


x = input("\n Enter the channel of the unidentified gamma line \n")
x = int(x)
y = coefficients[0]*x*x + coefficients[1]*x + coefficients[2]
print('The Energy of the Line is = ',y,' KeV \n')

#██████████████████████████████████████████████████████████████████████████████

# For FWHM
fwhm  = np.empty(0)

# Calculate the FWHM for each peak

for peak_index in peaks[1:4]:
    peak_x = channels[peak_index]
    peak_y = counts[peak_index]

    # Find the half-maximum value
    half_max = peak_y / 2.0

    # Find the indices where the data crosses the half-maximum value
    left_idx = np.where(counts[:peak_index] <= half_max)[0][-1]
    right_idx = np.where(counts[peak_index:] <= half_max)[0][0] + peak_index

    # Calculate the FWHM
    
    fwhm = np.append(fwhm,channels[right_idx] - channels[left_idx])
    
print('\n The FWHM for 662, 1172, 1332 KeV gamma lines are = ',fwhm,'\n')

#██████████████████████████████████████████████████████████████████████████████

# Gaussian fit and area under the curve.
# Cs - 137
x1 = 250; x2 = 320

# Define the Gaussian function
def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-(x - mean) ** 2 / (2 * stddev ** 2))

# Generate sample data with noise
x_data = channels[x1:x2]
y_data = counts[x1:x2]

# Fit the data to the Gaussian function
initial_guess = [50000, peaks[1], 0.15]  # Initial values for amplitude, mean, and standard deviation
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
plt.title('Gaussian Curve Fit for 662 KeV photo peak')
plt.grid(True)
plt.show()

#auc = np.trapz(y_data[x1:right_idx + 1], x_data[left_idx:right_idx + 1])

#params, _ = curve_fit(gaussian, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
amplitude, mean, stddev = params

# Define the range for integration (you can adjust this as needed)
lower_limit = mean - 3 * stddev
upper_limit = mean + 3 * stddev

# Calculate the area under the Gaussian curve using numerical integration
area, _ = quad(gaussian, lower_limit, upper_limit, args=(amplitude, mean, stddev))

print(area)

#print(auc)
    
# Display the fitted parameters
print(f'Amplitude: {amplitude:.2f}')
print(f'Mean: {mean:.2f}')
print(f'Standard Deviation: {stddev:.2f}')



'''
x (array-like): The input data in which you want to find peaks.

height (float or None, optional): Minimum height of peaks. Only peaks higher than this value will be considered. If set to None, it doesn't apply any height threshold.

threshold (float or None, optional): The minimum difference between a peak and its surrounding points. Peaks with a difference less than this threshold are ignored. If set to None, it doesn't apply any threshold.

distance (int or array-like or None, optional): Minimum horizontal distance between peaks. Peaks closer than this distance are merged into a single peak. If set to None, it doesn't apply any distance threshold.

prominence (float or None, optional): Minimum prominence of peaks. Prominence is a measure of how much a peak stands out from its surrounding data. If set to None, it doesn't apply any prominence threshold.

width (float or None, optional): The width of the peaks. If set to None, it doesn't apply any width threshold.

wlen (float or None, optional): The width of the convolution kernel for finding peaks. If set to None, it uses the default value of 1.

rel_height (float, optional): Used to calculate the prominence. It's a fraction of the peak's height. By default, it's set to 0.5.

plateau_size (float or None, optional): The minimum number of continuous data points at the peak's prominence level to consider it a plateau. If set to None, it doesn't apply any plateau size threshold.
'''