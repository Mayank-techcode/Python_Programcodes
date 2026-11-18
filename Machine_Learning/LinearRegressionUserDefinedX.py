import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : ", X)
    print("Values of Dependent Variables : ", Y)

    Mean_X = np.mean(X)
    Mean_Y = np.mean(Y)

    print("X_MEAN is : ", Mean_X)
    print("Y_MEAN is : ", Mean_Y)

    N = len(X)

    numerator = 0
    denomenator = 0

    # Y = m X + C 
    for i in range(N):
        numerator = numerator + (X[i] - Mean_X) * (Y[i] - Mean_Y)
        denomenator = denomenator + (X[i] - Mean_X) ** 2

    m = numerator / denomenator

    print("Slope of Line (m) is : ", m)

    C = Mean_Y - (m * Mean_X)

    print("Y intercept of line is : ", C)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()