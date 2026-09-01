import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def dot_product(a, b):
    
    if len(a) != len(b):
        raise ValueError("Vektör boyutları aynı olmalı!")

    total = 0
    
    for i in range(len(a)):
        total += a[i] * b[i]

    return total


vektor1 = [1, 2, 3]
vektor2 = [4, 5, ]

sonuc = dot_product(vektor1, vektor2)
print("Nokta Çarpım Sonucu:", sonuc)
