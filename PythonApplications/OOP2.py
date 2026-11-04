class Arithmetic:
    def __init__(self, A, B):
        print("----Inside Constructor----")
        self.No1 = A
        self.No2 = B

    def __del__(self):
        print("----Inside Destructor----")
    
    def Addition(self):

        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

def main():
    obj1 = Arithmetic(10, 11)
    obj2 = Arithmetic(20, 21)

    Ret = obj1.Addition()
    print(Ret)

    Ret = obj2.Addition()
    print(Ret)

if __name__ == "__main__":
    main()