class Arithmetic:
    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B
    
    def Addition(self):

        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

def main():
    print("Enter First Number : ")
    value1 = int(input())

    print("Enter Second Number : ")
    value2 = int(input())

    obj = Arithmetic(value1, value2)
    Ret =  obj.Addition()

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()