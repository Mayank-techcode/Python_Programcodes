class Employee:

    CompanyName = "Marvellous"                  # Class variable

    def __init__(self, A, B, C):                # Constructor
        print("---Inside Constructor---")
        self.Name = A                           # Instance variable
        self.Salary = B                         # Instance variable
        self.City = C                           # Instance variable

    def __del__(self):                          # Destructor
        print("---Inside Destructor---")

    def DisplayInfo(self):                      # Instance method
        print("Inside Instance Method DisplayInfo")
        
        print("Employee Name : "+self.Name)
        print("Employee Salary : ",self.Salary)
        print("Employee City : "+self.City)

    @classmethod
    def DisplayCompanyDetails(cls):             # Class Method
        print("Inside Class Method DisplayCompanyDetails")

        print("Company Name: "+cls.CompanyName)

    @staticmethod
    def DisplayCompanyPolicy():
        print("Inside Class Method DisplayCompanyPolicy")

        print("All Employees are 18+")
        print("Working hours are 9 to 6")
        print("Holidays: Saturday & Sunday")

def main():

    print("Class Variable: "+Employee.CompanyName)

    Employee.DisplayCompanyDetails()

    emp1 = Employee('Rahul', 15000, 'Pune')     # Object Creation
    emp2 = Employee('Pooja', 25000, 'Mumbai')   # Object Creation

    print("Employee Name : "+emp1.Name)
    print("Employee Salary : ",emp1.Salary)
    print("Employee City : "+emp1.City)

    emp2.DisplayInfo()

    Employee.DisplayCompanyPolicy()

    del emp1
    del emp2

if __name__ == "__main__":
    main()