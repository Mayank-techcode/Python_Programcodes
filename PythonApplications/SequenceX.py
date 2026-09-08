PI = 3.14

def CircleArea(Rad):
    Area = PI * Rad * Rad
    return Area

def main():
    print("Enter Radius of Circle: ")
    radius = float(input())

    result = CircleArea(radius)

    print("Area of circle is : ", result)

if __name__ == "__main__":
    main()