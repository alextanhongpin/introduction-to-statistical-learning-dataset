#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv

with open('./dataset/Income1.csv') as csvfile:
    data = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    x = []
    y = []
    for index, row in enumerate(data):
        if index > 0:
            x.append(row[1])
            y.append(row[2])
    # print curve_fit(f, x, y)[0] # your data x, y to fit
    # a, b, c = sp.polyfit(x, y, 2)
    x = sorted(x)
    y = sorted(y)
    print x
    plt.figure(1)

    # Normal Plot
    plt.subplot(121)
    plt.scatter(x, y, s=10, c='red', alpha=0.5)
    plt.xlabel('Years of Education')
    plt.ylabel('Income')

    # Plot with the polynomial fit to 3 degree and error
    plt.subplot(122)
    # plt.scatter(x, y, s=10, c='red', alpha=0.5)
    plt.xlabel('Years of Education')
    plt.ylabel('Income')
    z = np.poly1d(np.polyfit(x, y, 3))
    error = [z(x[i]) - y[i] for i, _ in enumerate(x)]
    plt.plot(x, z(x))
    plt.errorbar(x, y, yerr=error)
    plt.show()
