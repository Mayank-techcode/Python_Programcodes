import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousHeadBrainLinear(Datapath):

    Line = "*"*70
    Design = "-"*70

    df = pd.read_csv(Datapath)

    print(Line)
    print("\tFirst Few Records of the Dataset are : ")
    print(Line)
    print(df.head())
    print(Line)

    print("\tStatistical information of the Dataset : ")
    print(Line)
    print(df.describe())
    print(Line)

    X = df[['Head Size(cm^3)']]
    Y = df[['Brain Weight(grams)']]

    print("Independent Variables are : Head Size")
    print("Dependent Variables are : Brain Weight")

    print(Design)
    print("Total Records in Dataset : ",len(X))
    print(Design)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    print("Dimensions of Training dataset : ", X_train.shape)
    print("Dimensions of Testing dataset : ", X_test.shape)
    print(Design)

    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    Y_pred = model.predict(X_test)

    mse = mean_squared_error(Y_test, Y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y_test, Y_pred)

    print("Mean Squared Error is :", mse)
    print("Root Mean Squared Error is :",rmse)
    print("R Square value is :", r2)
    print(Design)

def main():
    MarvellousHeadBrainLinear("MarvellousHeadBrain.csv")

if __name__ == "__main__":
    main()