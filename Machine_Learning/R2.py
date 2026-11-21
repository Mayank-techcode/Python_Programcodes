from sklearn.metrics import r2_score

def main():
    Y_actual = [100, 200, 300, 400, 500]

    Y_predicted = [110, 190, 310, 390, 510]

    r2 = r2_score(Y_actual, Y_predicted)
    
    print("Actual Values : ", Y_actual)
    print("Predicted Values : ", Y_predicted)
    print("R2 value : ", r2)

if __name__ == "__main__":
    main()