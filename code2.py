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
import sys

channels = np.array(0)
counts   =np.array(0)

csv_file_path = 'calib.csv'

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

#plt.scatter(channels, counts, marker='o', s=1)
#plt.show()



#██████████████████████████████████████████████████████████████████████████████
'''
            Peak finding
'''
peaks, _ = find_peaks(counts, height=2000, threshold=10, distance=20, prominence=50)
print("The identified peaks channels are = ", peaks,'\n')

#██████████████████████████████████████████████████████████████████████████████
'''
Calibration
    Energy of gamma lines used for the calibration  
'''
energy = np.array([662,1173,1332])

print("Gamma lines used for the calibrations = ", energy,'\n')
channels_calib = np.array(peaks[2:5])
#plt.scatter(channels_calib, energy, marker='o', color='red', label='Expt Data')
#plt.legend()



# Fit a polynomial of degree 2 (quadratic)
degree = 2
coefficients = np.polyfit(channels_calib, energy, degree)

# Create a polynomial function based on the coefficients
poly_func = np.poly1d(coefficients)

# Generate points for the fitted curve
x_fit = np.linspace(min(channels_calib), max(channels_calib), 30)
y_fit = poly_func(x_fit)

#plt.plot(x_fit, y_fit, 'b', label=f'Fitted Polynomial (Degree {degree})')

#plt.legend()
#plt.show()

# Display the coefficients of the fitted polynomial

print('y = a * x^2 + b*x + c')

print(f'Fitted Polynomial Coefficients (Degree {degree}):')
for i, coeff in enumerate(reversed(coefficients)):
    print(f'Coefficient {i}: {coeff}')

#print(coefficients[0],coefficients[1],coefficients[2])
#### unidentified peak at a channel X corresponds to the energy


'''x = input("\n Enter the channel of the unidentified gamma line \n")
x = int(x)
y = coefficients[0]*x*x + coefficients[1]*x + coefficients[2]
print('The Energy of the Line is = ',y,' KeV \n')'''

# Read the background spectra file and find peaks

channels_b = np.array(0)
counts_b   = np.array(0)

csv_file_path_b = 'bg30hrs.csv'

with open(csv_file_path_b, mode='r', newline='') as file_b:
    # Create a CSV reader object
    csv_reader = csv.reader(file_b)

    # Iterate through the rows in the CSV file
    for row in csv_reader:
        # Each row is a list of values
        # You can access individual columns by indexing the list
        #print(row)
        channels_b = np.append(channels_b, int(row[0]))
        counts_b = np.append(counts_b, int(row[1]))

plt.scatter(channels_b, counts_b, marker='o', s=1)
plt.show()

ene = np.empty(0)


'''
            Peak finding
'''
peaks, _ = find_peaks(counts_b, height=250, threshold=5, distance=20, prominence=5)
print("The identified peaks channels are = ", peaks,'\n')

"""
Gamma line of the identifies peaks
"""

for chnl in peaks:
    x = chnl
    y = coefficients[0]*x*x + coefficients[1]*x + coefficients[2]
    print('The gamma line energy for the channel ', chnl, ' is ',round(y), ' KeV')
    
    
#
#print('The Energy of the Line is = ',y,' KeV \n')

sys.exit()