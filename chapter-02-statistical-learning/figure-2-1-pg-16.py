#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Simple demo of tv plot
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
# from scipy.optimize import curve_fit

# def f(x, A, B): # this is your 'straight line' y=f(x)
#    return A*x + B

with open('./dataset/Advertising.csv') as csvfile:
    # csv.QUOTE_NONNUMERIC will automatically convert data to it's appropriate type
    # so any data without quotes "" will be treated as float automatically
    # else you have to carry out conversion manually
    advertising = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    tv = []
    radio = []
    newspaper = []
    sales = []
    for index, row in enumerate(advertising):
        # Skip header
        if index > 0:
            # without csv.QUOTE_NONNUMERIC, you have to manually
            # convert the data for each column into float
            # tv.append(float(row[1]))
            tv.append(row[1])
            radio.append(row[2])
            newspaper.append(row[3])
            sales.append(row[4])
    plt.figure(1)

    # 131 means 1 row, 3 columns, and 1st column
    plt.subplot(131)
    plt.scatter(tv, sales, s=10, c='red', alpha=0.5, marker='o')
    plt.xlabel('TV')
    plt.ylabel('Sales')

    # Method 1:Line of best fit formula
    plt.plot(np.unique(tv), np.poly1d(np.polyfit(tv, sales, 1))(np.unique(tv)))

    # Method 2:It's also possible to compute the line of best fit using scipy
    # slope, intercept = curve_fit(f, tv, sales)[0] # your data x, y to fit
    # best_fit_line = [slope * i + intercept for i in tv]
    # plt.plot(tv, best_fit_line)

    # 132 means 1 row, 3 columns, and 2nd column
    plt.subplot(132)
    plt.scatter(radio, sales, s=10, c='red', alpha=0.5, marker='o')
    plt.xlabel('Radio')
    plt.ylabel('Sales')
    plt.plot(np.unique(radio), np.poly1d(np.polyfit(radio, sales, 1))(np.unique(radio)))
    
    # 133 means 1 row, 3 columns, and 3nd column
    plt.subplot(133)
    plt.scatter(newspaper, sales, s=10, c='red', alpha=0.5, marker='o')
    plt.xlabel('Newspaper')
    plt.ylabel('Sales')
    plt.plot(np.unique(newspaper), np.poly1d(np.polyfit(newspaper, sales, 1))(np.unique(newspaper)))

    plt.show()