from sklearn import tree

# rough 0
# smooth 1

# tennis 1
# cricket 2

def main():
    # Feature Encoding
    BallFeatures = [[35,0], [47,0], [90,1], [48,0], [90,1], [35,0], [92, 1], [35, 0], [35, 0], [35, 0]]

    # Label Encoding
    BallNames = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    # Model Training
    obj = tree.DecisionTreeClassifier()
    obj = obj.fit(BallFeatures, BallNames)

    # Model Testing
    print(obj.predict([[93, 1], [95, 1], [42, 0], [40, 0]]))

if __name__ == "__main__":
    main()