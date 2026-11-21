import numpy as np
from sklearn.metrics import mean_squared_error

def main():
    Y_actual = [10, 20, 30, 40, 50]
    Y_predicted = [10, 20, 30, 40, 50]

    MSE = mean_squared_error(Y_actual, Y_predicted)
    RMSE = np.sqrt(MSE)

    print("Actual Values : ", Y_actual)
    print("Predicted Values : ", Y_predicted)
    print("Mean Squared Error : ", MSE)
    print("Root Mean Squared Error : ", RMSE)

if __name__ == "__main__":
    main()