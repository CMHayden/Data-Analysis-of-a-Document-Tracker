import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

def histogram(dict, xlabel, title):
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel("Frequency", fontsize=15)
    plt.title(title, fontsize=20)

    xRange = range(len(dict.keys()))

    plt.xticks(xRange, dict.keys())

    plt.bar(xRange, dict.values(), align='center', color='g')
    plt.show()

dict = {"uk": 3, "mx": 1, "az": 1, "jp": 1}
histogram(dict, "countries", "Counting Stuff")