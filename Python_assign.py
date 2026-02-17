#Q.1]
 name = '''Hi How are you?
 Starterd learning python.
 It's really interesting.''' 

1]
print(name[:]) 
'''Hi How are you?
Starterd learning python.
It's really interesting. '''

2]
print(name[-10:-5])    #teres

3]
print(name[3:12])   #How are y

4]
print(name[12:3])  #null

5]
print(name[5:6])   #w

6]
print(name[-4:-12])   #null

7]
print(name[::2])  #H o r o?Satr erigpto.I' elyitrsig

8]
print(name[::-2]) .nteen larst nhy nnaldert uyeawHi

Q.2]
L1 =['a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']
a]
print(L1[:])   #['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']

b]
print(L1[::3])  #['a', 30, 300, 'major']

c]
print(L1[::-2])  #['major', 400, 100, 30, 'b']

d]How to extract  value “Happy” based on index and negative index
print(L1[8])
print(L1[-2])

e]How to check type of data in list at 4th position
print(type(L1[4-1]))

f]Extract values for 100, 300, 400 
print(L1[L1.index(100)])
print(L1[L1.index(300)])
print(L1[L1.index(400)])

Q.3]
If l2 =[1,2,3,5,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”] then what is the output of following
L2 =[1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success']
print(L2[4]) #['a', 'b', 'work hard']
print(L2[1:5]) #[2, 3, 5, ['a', 'b', 'work hard']]
print(L2[7]) #Success
print(L2[7][2]) #c
print(L2[7][2:]) #ccess
print(L2[ : 3]) #[1, 2, 3]
print(L2[3:])  #[5, ['a', 'b', 'work hard'], 100, 200, 'Success']

q.4]From the above l2 value ‘b’ must be changed to ‘BEE’.
L2[4][1]='BEE'

q.5]	From l2 “BEE” has to discard.
del L2[4][1]
print(L2)

q.6] In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}

dict={'insect': ['bee', 'moth'] , 'bird ': ['parrot', 'sparrow']}
L2.append(dict)
print(L2)

q.7]From l2 extract insect information.
print(L2[len(L2)-1]['insect'])

q.8]	Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
d1 = {'a':10, 'b':20, 'c' : 30}
L2.insert(2,d1)
print(L2)

q.9] Based on new l2 created here extract the value 10 from l2 dictionary.
print(L2[2]['a'])

q.10]
L2 =[1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success', (200,300, 'Hundreds')] 
       then what is the output of following
'''print(L2[4][2]) #50
print(L2[5:])  #['Python', 400, ['a', 'b', 'work hard'], 100, 200, 'Success', (200, 300, 'Hundreds')]
print(L2[2:]) #[3, 5, (90, 40, 50, 10), 'Python', 400, ['a', 'b', 'work hard'], 100, 200, 'Success', (200, 300, 'Hundreds')]
print(L2[1:5]) #[2, 3, 5, (90, 40, 50, 10)]
print(L2[5]) #Python
print(L2[5][3:-1]) #ho
print(L2[-1])  #(200, 300, 'Hundreds')
print(L2[-4, -3])   #[100]
print(L2[-4: -10])  #[]
print(L2[7][2]) #work hard
print(L2[-7][2:]) #thon
print(L2[ :- 3])  #[1, 2, 3, 5, (90, 40, 50, 10), 'Python', 400, ['a', 'b', 'work hard'], 100]
print(L2[-3:])   #[200, 'Success', (200, 300, 'Hundreds')] '''




#q.11]
'''
class invalidmarks(Exception):
    pass 

def Check_class(m):
    try:
        marks=m
        if (not marks.isalnum() and not marks.isalpha()) or marks.isdigit():                            
            marks=float(marks)
            if marks<=100 and marks>0:
                if marks>80:
                    return 'You got distinction'
                elif marks>=60:
                    return 'You got first class'
                elif marks>=40:
                    return 'You got second class'
                elif marks>=35:
                    return 'pass'
                else:
                    return 'You got fail'
            else:
                raise invalidmarks('Marks are not valid ')
        else:
            raise ValueError('Enter the digits only ')
    except invalidmarks as e:
        print(e)
    except ValueError as e:
        print(e)


marks=input('Enter the marks to check the class: ')
res=Check_class(marks)
print(res) '''

#Q.12]
'''
class Invalidsaldetails(Exception):
    pass

def Sal_rank(s,rat):
    try:
        sal=s
        rating=rat
        if sal.isdigit() and rating.isalpha():
            sal=int(sal)
            if sal<=0 or sal>2300000:
                raise Invalidsaldetails('Salary details are invalid ')
            else:
                inc=0  
                if sal<=500000:
                    inc={"A":0.16,"B":0.12,"C":0.10,"D":0.06}
                elif sal<=10000  00:
                    inc={"A":0.14,"B":0.10,"C":0.08,"D":0.06}
                elif sal<=1500000:
                    inc={"A":0.08,"B":0.06,"C":0.04,"D":0}
                elif sal<=2300000:
                    inc={"A":0.07,"B":0.05,"C":0.04,"D":0}
                if rating in inc:
                    sal+=sal*inc[rating]
                    return int(sal)
                else:
                    raise ValueError('Enter the valid rating')

        else:
            return 'enter valid sal and rating '
    except Invalidsaldetails as e:
        print(e)
    except ValueError as e:
        print(e)


s=input("enter the salary per year: ")
rat=input("enter the rating (A/B/C/D): ").upper()
res=Sal_rank(s,rat)
print("updated salary:",res)


#q.13]
class invalid_course(Exception):
    pass
def Cal_price(sub,l):
    try:
        subject=sub
        L1=l
        if subject not in L1:
            raise invalid_course("Invalid subject entered. Please choose from HR, Finance, Marketing, or DS.")
        else:
            tot_budget=200000
            if subject!='DS':
                analytics=input('Enter yes or no for analytics? (y/n) : ').lower()
                if analytics=='y':                  
                    tot_budget+=200000*0.10
            hostel=input('Do y want to hostel ? (y/n) : ').lower()
            if hostel=='y':
                tot_budget+=200000
            food = input('Is food a requirement? (y/n): ').lower()
            if food == 'y':
                months = int(input('How many months of food service? '))
                tot_budget += (2000 * months)      
            transport=input('Do y want to transport ? (y/n) : ').lower()
            if transport=='y':
                tot_month=int(input('for 1 semester or for annual : '))
                tot_budget+=(13000*tot_month)
            return tot_budget
    except invalid_course as e:
        print(e)
    return None
l= ['HR', 'Finance', 'Marketing', 'DS']
print('Select the courses from here : ')
print(l)
subject=input("enter the subject : ").strip()
tott_budget=Cal_price(subject,l)
print(f"\n--- Total fee ---")
print(f"Subject: {subject}")
print(f"Total Annual Cost: {tott_budget} INR")


#q.14]
class BookStore:
    def __init__(self, books, notebooks):
        self.books = books
        self.notebooks = notebooks
        self.cart = {}
    def ask_for_books(self):
        for a in self.books:
            for b in self.books[a]:
                print(a, '-->', b, '-->', self.books[a][b])
        for a in self.notebooks:
            for b in self.notebooks[a]:
                print(a, '-->', b, '-->', self.notebooks[a][b])
        do_you_books = input("Do you want textbooks (Y/N): ").upper()
        if do_you_books == 'Y':
            std = int(input("Enter the standard: "))
            if 1 <= std <= 4:
                grade = '1st-4th'
            elif 5 <= std <= 8:
                grade = '5th-8th'
            elif 9 <= std <= 10:
                grade = '9th-10th'
            else:
                print("Invalid standard")
                return
            print("\nAvailable textbooks for this standard:")
            for sub in self.books:
                print(sub, "-->", self.books[sub][grade])
            more_books = 'True'
            while more_books == 'True':
                subject = input("Enter subject name: ")
                if subject in self.books:
                    qty = int(input("Enter quantity: "))
                    price = self.books[subject][grade]
                    self.cart[subject] = price * qty
                    print(subject, "-->", price * qty)
                else:
                    print("Subject not available")
                more_books = input("More books (True/False): ")
        wnt_ntb = input("\nDo you want notebooks (Y/N): ").upper()
        if wnt_ntb == 'Y':
            more_notebooks = 'True'
            while more_notebooks == 'True':
                ntb = input("Notebook type: ")
                pages = int(input("Pages (100/200): "))
                if ntb in self.notebooks and pages in self.notebooks[ntb]:
                    qty = int(input("How many notebooks do you want? "))
                    total_price = self.notebooks[ntb][pages] * qty
                    self.cart[ntb] = total_price
                    print(ntb, "-->", total_price)
                else:
                    print("Notebook not available")
                more_notebooks = input("More notebooks (True/False): ")
        return self.cart
    def total_price(self):
        grand_total = 0
        for val in self.cart:
            grand_total += self.cart[val]
        return grand_total
    def print_bill(self, grand_total):
        print('-' * 60)
        print("|{:^58}|".format("Welcome to BOOK STORE"))
        print("|{:^58}|".format("RECEIPT"))
        print("|" + "-" * 58 + "|")
        print("|{:<5s} {:30s} {:>20s}|".format("Sr", "Item", "Amount"))
        print("|" + "-" * 58 + "|")
        for idx, item in enumerate(self.cart, start=1):
            print("|{:<5d} {:30s} {:>20.2f}|".format(
                idx, item, self.cart[item]
            ))
        print("|" + "-" * 58 + "|")
        print("|{:>36s} {:>20.2f}|".format("Total Cost:", grand_total))
        print("-" * 60)
notebooks = {
    'square': {100: 40, 200: 70},
    '4lines': {100: 30, 200: 50},
    '2lines': {100: 30, 200: 50},
    'single lines': {100: 60, 200: 100},
    'A4 notebook': {100: 100, 200: 180}
}
books = {
    'Hindi': {'1st-4th': 60, '5th-8th': 100, '9th-10th': 150},
    'Marathi': {'1st-4th': 60, '5th-8th': 100, '9th-10th': 150},
    'English': {'1st-4th': 80, '5th-8th': 100, '9th-10th': 150},
    'Science': {'1st-4th': 90, '5th-8th': 120, '9th-10th': 200},
    'Maths': {'1st-4th': 100, '5th-8th': 140, '9th-10th': 250}
}
print("Welcome to Book Store")
doyou = input("Do you want to buy something (Y/N): ").upper()
if doyou == 'Y':
    store = BookStore(books, notebooks)
    store.ask_for_books()
    if store.cart:   # changed else logic properly
        grand_total = store.total_price()
        print("\nTotal Amount:", grand_total)
        store.print_bill(grand_total)
    else:
        print("No items selected.")
else:
    print("Thank you! Visit again !!")

#q.15]
from datetime import datetime, timedelta
class FixedDepositCalculator:
    def __init__(self, rate_data):
        self.rate_data = rate_data
    def get_slab(self, days):
        for key in self.rate_data:
            start, end = self.rate_data[key]["range"]
            if start <= days <= end:
                return key
        return None
    def calculate_maturity(self, principal, days, rate):
        time_years = days / 365
        return principal + (principal * rate * time_years / 100)
    def start_fd(self):
        principal = float(input("Enter principal amount: "))
        days = int(input("Enter number of days for FD: "))
        slab = self.get_slab(days)
        if not slab:
            print("Invalid tenure")
            return
        category = input("Enter category (public/senior): ").lower()
        if category not in ["public", "senior"]:
            print("Invalid category")
            return
        print("Select type: 1 or 2")
        rate_type = int(input("Enter type number: "))
        if rate_type not in self.rate_data[slab][category]:
            print("Invalid type")
            return
        rate = self.rate_data[slab][category][rate_type]
        today = datetime.today()
        maturity_date = today + timedelta(days=days)
        maturity_amount = self.calculate_maturity(principal, days, rate)
        self.print_details(principal, rate, today, maturity_date, maturity_amount)
    def print_details(self, principal, rate, start_date, maturity_date, maturity_amount):
        print("\n------ FD DETAILS ------")
        print("Principal:", principal)
        print("Interest Rate:", rate, "%")
        print("Start Date:", start_date.date())
        print("Maturity Date:", maturity_date.date())
        print("Maturity Amount:", round(maturity_amount, 2))

Fd_cal= {
    1: {"range": (7, 45), "public": {1: 5.75, 2: 5.75}, "senior": {1: 6.25, 2: 6.25}},
    2: {"range": (46, 179), "public": {1: 6.25, 2: 6.25}, "senior": {1: 6.75, 2: 6.75}},
    3: {"range": (180, 365), "public": {1: 6.40, 2: 6.40}, "senior": {1: 6.90, 2: 6.90}},
    4: {"range": (366, 730), "public": {1: 7.00, 2: 6.75}, "senior": {1: 7.50, 2: 7.25}},
    5: {"range": (731, 1825), "public": {1: 6.70, 2: 6.60}, "senior": {1: 7.20, 2: 7.10}}
}
print("FD Calculator")
fd = FixedDepositCalculator(Fd_cal)
fd.start_fd()


#16]
# string=In most organized forms of writing, such as essays,
# paragraphs contain a topic sentence. This topic sentence of the 
# paragraph tells the reader what the paragraph will be about. 
# essays usually have multiple paragraphs that make claims to support a thesis statement, 
# which is the central idea of the essay.
# print(string)

#q.17]
a = 100
e = str(a)
print(e)
#b = list(a) #a is not iterable
#print(b)
#c = tuple(a) #'int' object is not iterable
#print(c)
#d = dict(a) #'dict' object is not callable
#print(d)
#m=  set(a) #'int' object is not iterable
#print(m)
h = float(a)
print(h)

#q.18]
city = 'Pune' 
#print(int(city)) invalid literal for int() with base 10: 'Pune'
#print(float(city)) ValueError: could not convert string to float: 'Pune'
print(list(city)) #['P', 'u', 'n', 'e']
print(tuple(city)) #('P', 'u', 'n', 'e')
#print(dict(city))  TypeError: 'dict' object is not callable 
print(set(city)) #{'P', 'e', 'u', 'n'}

#q.19]
l1 = [20,18,15,17,18]
#l2 = int(l1) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
#print(l2)
#print(float(l1)) #TypeError: float() argument must be a string or a real number, not 'list'
print(list(l1)) #[20, 18, 15, 17, 18]
print(tuple(l1)) #(20, 18, 15, 17, 18)
#print(dict(l1))  TypeError: 'dict' object is not callable
print(set(l1)) #{17, 18, 20, 15}
#l2 = float(l1)

#q.10]	Create the empty list snames 
sname=[]
sname.append(20)
sname.extend([30])
sname.append(40)
sname.extend('work')
combo=[1, 'a', 'b' ,2 , 3] 
sname=sname+combo
sname.append(combo)
sname.extend(combo)

#q.11] 
l1=[1,2]
l3=[1,2,3,4,5,6,7]
l3.insert(4,l1)
print(l3)

#q.12]
l1=[1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ]
result = list(map(lambda x: x * 5 if isinstance(x, (int, float)) else '', l1))
l1.remove('Nisha')
index_val = l1.index(20.50)

#q.13.	Create a comprehensive list for square upto 10 
sqr = [x**2 for x in range(1, 11)]


#q.14]
div = [num for num in range(1, 201) if num % 13 == 0]

#q.15]
div4 = [num for num in range(300, 401) if num % 4 == 0]
print(div4)

#q.16]
x = 2
y = 2
combinations = [[i, j] for i in range(x) for j in range(y)]
print(f"For x={x} and y={y}:")
print(combinations)

#q.22]
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
union_res = s1 | s2 
inter_res = s1 & s2  
diff_res = s1 - s2 
sym_diff = s1 ^ s2  
print(f"Union: {union_res}")
print(f"Intersection: {inter_res}")
print(f"Difference (s1-s2): {diff_res}")
print(f"Symmetric Difference: {sym_diff}")

#q.23]
s1 = {1, 2, 3, 4, 5}
l1 = [4, 5, 6, 7]
result = s1.intersection(set(l1))
print(f"Intersection of set s1 and list l1: {result}")

#q.24]
name = input("Enter your Name: ").strip()
dob = input("Enter your DOB (DD-MM-YYYY): ").strip()
password = f"{name[:4].upper()}@{dob[0:2]}{dob[3:5]}"
print(f"Generated Password: {password}")

#q.25]
name = input("Enter your Name: ").strip()
dob = input("Enter your DOB (DD-MM-YYYY): ").strip()
password = f"{name[:4].upper()}@{dob[-4:]}"
print(f"Generated Password: {password}")

#q.26]
for i in range(1, 5):
    print("* " * i)

#q.27]
for i in range(4, 0, -1):
    print("*" * i)

#q.28]
Str_val = "ABCD"
for i in range(1, len(Str_val) + 1):
    print(" ".join(Str_val[:i]))    

#q.29]
letters = "ABCD"
for i in range(len(letters)):
    print(letters[i] * (i + 1))

#q.30]
for i in range(1, 5):
    for j in range(0,i):
      print(i,end="")
    print()

#q.31]
Val = "ABCD"
rev_val = Val[::-1] # "DCBA"
for i in range(1, len(rev_val) + 1):
    print(rev_val[:i])

#q.33]
l1=[]
for i in range(1,11):
  if i%2!=0:
    l1.append(i)
print(l1)

l1=[x for x in range(1,11) if x%2!=0]

#q.34]
for i in range(200,251):
  if i%2==0:
    l1.append(i)
print(l1)

#q.35]
l5 = [2,70,'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
l6 = []
for i in l5:
    if isinstance(i,int) or isinstance(i,float) or isinstance(i,str):
        l6.append(i*2)
    elif isinstance(i,(list,tuple)):
        l6.append(i*2)
    elif isinstance(i, set):
        d = set()
        for x in i:
            d.add(x*2)
        l6.append(d)
    else:
        new_dict = {}
        for k,v in i.items():
            new_dict.update({k:v*2})
        l6.append(new_dict)
print(l6) 
#q.36]
List2= [2,70,'work', 'para', 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
l3=[x*2 for x in List2 if isinstance(x,(int,float))]
print(l3)


#q.37]
def Check_m(marks):
    try:
        if int(marks)<0 or int(marks)>100:
            return 'invalid marks'
        else:
            return marks
    except ValueError as t:
        return 'this is the typeerror'

marks=input('enter the marks :')
val=Check_m(marks)
print(val)

#q.38]

def Validate_name(name):
    if name.isdigit():
        return False
    elif name.isspace():
        return False
    elif not name.isdigit() and not name.isalpha():
        return False
    return True

fname=input('enter the first name : ')
lname=input('enter the last name')
if(Validate_name(fname)):
    print('first name  is valid')
else:
    print('it is not validate')
if(Validate_name(lname)):
    print('second name is valid')
else:
    print('it is not validate')
    
#q.39]Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space

def Validate_num(num):
    if len(num)!=10:
        print('invalid length')
    else:
        if num.isalpha():
            print('invalid number : it contains letters')
        elif ' ' in num:
            print('invalid number :it contains space ')
        elif not num.isalnum() and not num.isspace():
            print('invalid number :it contains special characters ')
        else:
            print(f"Number is correct {num}")

mob_num=input('Enter the mobile number : ')
Validate_num(mob_num)


#q.40]
def generate_password():
    name = input("Enter Name: ").strip()
    dob = input("Enter DOB (DD-MM-YYYY): ").strip()
    first_name = name.split()[0][:4]
    year = dob.split("-")[-1]
    password = first_name + year
    print("Generated Password:", password)
generate_password()


#q.41]
customers = {}
def add_customer():
    sr_no = len(customers) + 1
    name = input("Enter Name: ")
    dob = input("Enter DOB: ")
    mobile = input("Enter Mobile: ")
    customers[sr_no] = {"name": name, "DOB": dob, "mobile": mobile}
    print(customers)

add_customer()


#q.42 & 43]
import os
file = "cust_info.txt"
def load_data():
    if os.path.exists(file) and os.path.getsize(file) > 0:
        with open(file, "r") as f:
            return eval(f.read())
    return {}
def save_data(data):
    with open(file, "w") as f:
        f.write(str(data))

customers = load_data()
def add_customer():
    sr_no = len(customers) + 1
    name = input("Enter Name: ")
    dob = input("Enter DOB: ")
    mobile = input("Enter Mobile: ")
    customers[sr_no] = {"name": name, "DOB": dob, "mobile": mobile}
    save_data(customers)
    print("Saved Successfully!")
add_customer() 

#q.44]database

#q.45]
Dict1 = {"Key":{"subkey":20},"k2":{"sub2":5},"k3":{"sub4":16},"k4":{"sub4":6}}
sorted_dict = dict(sorted(Dict1.items(), key=lambda x: list(x[1].values())[0]))
print(sorted_dict)


#q.46]
from datetime import datetime
import sys
def Check_age(dob):
    try:
        if isinstance(dob,date):
            age=abs(dob.year-datetime.now().year)
            return age
        else:
            raise ValueError('Enter the correct format ')
    except:
        print(sys.exc_info())

dob=input('enter the dob : ')
dob_format=datetime.strptime(dob,'%d-%m-%Y')
print('current age is ',Check_age(dob_format))


# q.47]
from datetime import datetime
import sys
def Check_eligibility(dob,legal_age):
    try:
         if isinstance(legal_age,int):
            if abs(dob.year-datetime.now().year)>=legal_age:
                print('eligible to vote')
            else:
                print('not eligible')
         else:
             raise TypeError('not supported ')
    except:
        print(sys.exc_info())
dob=input('enter the dob : ')
dob_format=datetime.strptime(dob,'%d-%m-%Y')
Check_eligibility(dob_format,18)

#q.48]
def is_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")
is_palindrome("NITIN")


#q.49]
def fibonacci(max):
    a,b=0,1
    for i in range(1,max+2):
        yield a
        # c=a+b
        # a=b
        # b=c
        a,b=b,a+b

res=list(fibonacci(5))
for i in res:
    print(i)

#q.50]
from datetime import datetime
import sys
try:
    signin=input('enter the sign time : [HH:MM]')
    signout=input('enter the signout time : [HH:MM]')
    print(abs(datetime.strptime(signin,'%H:%M')-datetime.strptime(signout,'%H:%M'))) 
except:
     print(sys.exc_info())   

#q.51]
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(factorial(5))


#q.52]
lst = [10,45,78,23]
print("Largest:", max(lst))

#q.53]
lst = [1,2,2,3,3,3,4]
freq = {}
for i in lst:
    freq[i] = freq.get(i,0) + 1
print(freq)

#q.54]
l1 =[1,2,3,4,5]
l2 =[3,2,8,7,9]
common = list(set(l1) & set(l2))
print("Common Elements:", common)


#q.57]
from datetime import datetime
str1='Hotel'
menu=input("Enter the dish you want:")
quant=input("Enter the quantity:")
idli_price = 50
order_price = 0
sr = 1
order_price = int(quant)* idli_price
print('-'*40)
print('{:>20}'.format(str1))
print('-'*40)
print('{0:10}{1:10}{2:<10}{3:<12}'.format('sr','Menu','qunt','price'))
print('{0:<10}{1:<12}{2:10}{3:<16}'.format(sr,menu,quant,idli_price))
print('-'*40)
print('{0:>25}{1:10}'.format('total',order_price))
print('-'*40)

def Printfile(menu,quant):
    f=open('tp.txt','w')
    str1='Hotel'
    idli_price = 50
    order_price = 0
    sr = 1
    order_price = int(quant)* idli_price
    cur_time=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    f.write('-'*70+'\n')
    f.write('{:>20}'.format(str1)+'\n')
    f.write('-'*70+'\n')
    f.write('{:<5}{:<10}{:<10}{:<10}{:<20}'.format('sr','Menu','qunt','price','Billtime')+'\n')
    f.write('{:<5}{:<10}{:<10}{:<10}{:<20}'.format(sr,menu,quant,idli_price,cur_time)+'\n')
    f.write('-'*70+'\n')
    f.write('{:>30}{:>10}'.format('total',order_price)+'\n')
    f.write('-'*70+'\n')


menu=input("Enter the dish you want :")
quant=input("Enter the quantity :")
Printfile(menu,quant)
'''



