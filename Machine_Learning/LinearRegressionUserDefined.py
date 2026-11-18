import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the Data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : ", X)
    print("Values of Dependent Variables : ", Y)

    XSum = 0
    YSum = 0

    for i in range(len(X)):
        XSum = XSum + X[i]
        YSum = YSum + Y[i]

    Mean_X = XSum / len(X)
    Mean_Y = YSum / len(Y)

    print("X_MEAN is : ", Mean_X)
    print("Y_MEAN is : ", Mean_Y)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()