class StudentBilling:
    def __init__(self):
        self.subject_list = ['HR', 'Finance', 'Marketing', 'DS']
        self.annual_subject_cost = 200000
        self.annual_hostel = 0
        self.annual_food = 2000
        self.annual_transport = 0
    
    def acad_fee(self):
        '''
        Docstring for acad_fee
        This function calculates the basic acad fee
        '''
        try:
            subject = input("Enter your subject: ")
            if subject.isalpha():
                if subject == 'HR':
                    analytics = input("Want analytics?? (Y/N): ").upper()
                    if analytics == 'Y':
                        self.annual_subject_cost += 200000 * 0.10
                    else:
                        self.annual_subject_cost = 200000
                elif subject == 'Finance':
                    self.annual_subject_cost = 200000
                elif subject == 'Marketing':
                    analytics = input("Want analytics?? (Y/N): ").upper()
                    if analytics == 'Y':
                        self.annual_subject_cost += 200000 * 0.10
                    else:
                        self.annual_subject_cost = 200000
                elif subject == 'DS':
                    self.annual_subject_cost = 200000
                else:
                    print("Subject is not valid")
            else:
                print("Subject must be alphabets")
        except ValueError:
            print('Enter the valid subject : ')


    def hostel_total(self):
        '''
        Docstring for hostel_total
        
        This function calculates the hoste_total
        '''
        try:
            hostel = input("Want hostel ?? (Y/N): ").upper()
            if hostel.isalpha():
                if hostel == 'Y':
                    self.annual_hostel = 200000
                elif hostel == 'N':
                    self.annual_hostel = 0
                else:
                    print("Please respond in Y or N")
            else:
                print("Non alpha value inserted in hostel")
        except ValueError:
            print('invalid input ')

    def food_total(self):
        '''
        Docstring for food_total
        
        :param self: Object
        this function calculates the food total
        '''
        food = input("Want food?? (Y/N): ").upper()
        if food.isalpha():
            if food == 'Y':
                try:
                    food1 = int(input("Want food how many months?? "))
                    if food1 < 0 or food1 > 24:
                        print("Months invalid")
                    else:
                        self.annual_food = self.annual_food * food1
                except ValueError:
                    print('Enter the proper month ')
            else:
                self.annual_food = 0
        else:
            print("Food must be Y or N")

    def transport_total(self):
        '''
        Docstring for transport_total
        This function calculates the transport of the student
        '''
        transport = input("Transport for sem or full year (1/2): ")
        try:
            if transport.isdigit():
                transport = int(transport)
                if transport == 1 or transport == 2:
                    self.annual_transport = 13000 * transport
                else:
                    print("Enter 1 for sem or 2 for full year")
            else:
                print("Digit is required")
        except ValueError:
            print('Invalid Input ')

    def generate_bill(self):
        '''
        Docstring for generate_bill
        
        This function calculates the total bill by accessing the instance variable
        '''
        total = self.annual_subject_cost+ self.annual_transport+ self.annual_food + self.annual_hostel
        print("\nTotal Bill of student:")
        print("Subject Cost:", self.annual_subject_cost)
        print("Accommodation Cost:", self.annual_hostel)
        print("Transport Cost:", self.annual_transport)
        print("Annual Food:", self.annual_food)
        print("Total Cost:", total)

student = StudentBilling()

student.acad_fee()
student.hostel_total()
student.food_total()
student.transport_total()
student.generate_bill()
