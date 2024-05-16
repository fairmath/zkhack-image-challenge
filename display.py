import json
import pickle
import matplotlib.pyplot as plt
import numpy as np


def reshape_array(array):
    list_r, list_g, list_b = np.array_split(array, 3)
    rgb = list(zip(list_r, list_g, list_b))
    n = 32
    x = [rgb[i:i + n] for i in range(0, len(rgb), n)]
    return x


def displayImage(file):
    with open(file) as f:
        d = json.load(f)
    a = reshape_array(d['image'])
    plt.figure(figsize=(1, 1))
    plt.imshow(a)
    plt.show()


displayImage(file='pic_from_3')

