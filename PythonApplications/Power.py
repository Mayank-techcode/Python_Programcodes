def Power(X, Y):
    result = 1

    for i in range(Y):
        result =  result * X
    
    return result

Ret = Power(10, 7)

print("Result is: ", Ret)