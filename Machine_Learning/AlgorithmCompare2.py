from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = tree.DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(prediction, Y_test)

    return accuracy

def MarvellousCalculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.5,random_state=42)

    model = KNeighborsClassifier()

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    accuracy = accuracy_score(prediction, Y_test)

    return accuracy

def main():
    result = MarvellousCalculateAccuracyDecisionTree()
    print("Accuracy of Decision Tree is : ",result*100,"%")

    result = MarvellousCalculateAccuracyKNN()
    print("Accuracy of KNN is : ",result*100,"%")

if __name__ == "__main__":
    main()