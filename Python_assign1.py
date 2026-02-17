# Comprehensive list
#q.1]

l=[x**2 for x in range(1,10)]
print(l)
# q.2] Create a list of even numbers between 1 and 50 using list comprehension.
l=[x for x in range(1,50) if x%2==0]
print(l)
# q.3] Convert all strings in a list to uppercase using list comprehension.
lstr=['hello','My','name','is','john']
l1=[x.upper() for x in lstr]
print(l1)
# q.4] Given a list of integers, create a new list that contains only the positive numbers.
l=[10,5,6,-2,-5,15]
l1=[x for x in l if x > 0]
print(l1)
# q.5] Create a list of tuples (num, num^2) for numbers 1 to 5.
l1=[(x,x**x) for x in range(1,5)]
print(l1)
# q.6] Extract all vowels from a given string using list comprehension.
s='Hello'
l1=[x for x in s if x in ('aeiou')]
print(l1)

#q.7] Flatten a 2D list using list comprehension.
l1=[[1,2,3],[4,5,6]]
l2=[]
l1=[l2.extend(x)for x in l1 if isinstance(x,list)]
print(l2) 
#q.8]Replace all negative numbers in a list with 0 using list comprehension.
l1=[10,-9,20,30,50]
l1=[x if x>0 else 0 for x in l1]
print(l1)
# 9. Given a list of words, create a list of lengths of each word.
l1=['hello','my','name','is']
l=[len(x) for x in l1]
print(l)
# 10. Filter out words that start with the letter 'A' or 'a'.
l=['Apple','and','fruit','mango']
l1=[x for x in l if not x.startswith('A') and not x.startswith('a')]
print(l1)

#q.11] From a list of numbers, generate a list of “even” or “odd” strings using list comprehension.
l=[2,3,4,5,6]
l1=['even ' if x%2==0 else 'odd ' for x in l]
print(l1)

# q.12] Create a list of numbers divisible by both 3 and 5 in range 1–100.
l=[x for x in range(1,100) if x%3==0 and x%5==0]
print(l)
# q.13] Write a nested list comprehension to generate a multiplication table  for 1–5.
l1=[[(x*i) for i in range(1,11)] for x in range(1,6)]
print(l1)
# q.14] Convert a dictionary’s keys into a list using list comprehension.
dict={1:'a',2:'b',3:'c'}
l=[k for k in dict.keys()]
print(l)
# q.15] Extract numeric digits from a string using list comprehension.
s='Abc19@9.0'
l=[s[x] for x in range(0,len(s)) if s[x].isdigit()]
print(l)
# q.16] Use list comprehension to remove all spaces from a string.
s="hello dear ,good evening"
s1=''
l1=['' if s[x]==' ' else s1+s[x] for x in range(0,len(s))]
print(s1.join(l1))
# q.17] Create a list of characters that appear more than once in a string.
s ='mittechnical'
l=[{x for x in s if s.count(x)>1}]
print(l)
# q.18]From a list of sentences, generate a list of all words (split using list  comprehension).
l=["hello dear","good evening"]
l1=[word for s in l for word in s.split()]
print(l1)
# q.19] Create a list of unique elements from a list using list comprehension + condition.
l1=[1,4,22,2,3,4,15,5,5]
l2=[]
l3=[l2.append(x) for x in l1 if x not in l2]
print(l2)
# q.20] Generate all pairs (x, y) where x is from list A and y is from list B  (cartesian product)
l1=[1,2]
l2=['a','b']
pairs=[(x, y) for x in l1 for y in l2]
print(pairs)

#Lambda functions
# q.1] Write a lambda to add two numbers.
x=lambda x,y:x+y
print(x(10,10))
# q.2] Create a lambda to check if a number is even.
x=lambda x:'even' if x%2==0 else 'odd'
print(x(10))
# q.3] Write a lambda to get the last character of a string.
s=lambda x:x[-1]
print(s('hello'))
# q.4] Use lambda with map() to square every number in a list.
n=[1,2,3,4]
dict=list(map(lambda x:x**2,n))
print(dict)
# q.5] Use lambda with filter() to get only odd numbers from a list.
nums=[1,2,3,4,5,6]
odd=list(filter(lambda x:x%2!=0,nums))
print(odd)
#q.6] Use sorted() + lambda to sort a list of tuples by second value.
p=[(1,'pineapple'), (2, 'apple'), (3, 'cherry')]
s=sorted(p,key = lambda x:x[1])
print(s)
#q.7] Create a lambda to check if a string is a palindrome.
s="madam"
p=lambda s:"palindrome" if s == s[::-1] else "not palinrdrome"
print(p(s)) 
#q.8] Use lambda to find maximum of three numbers.
m=lambda a,b,c : max(a,b,c)
print(m(2,3,4))
#q.9] Write a lambda to reverse a string.
str1=lambda s: s[::-1]
print(str1("datta"))

#q.10] Use lambda with map() to convert a list of strings to integers.
l=["str","data","lsls"]
s = list(map(lambda x:int(x),l))
print(s) 

#q.11.] Use lambda with filter() to remove empty strings from a list.

l=["pineapple",'','','banana']
l1=list(filter(lambda x:x!='',l))
print(l1)

#q.12] Use lambda to compute factorial using reduce() (yeah, that one-liner madness).
n=5
value=reduce(lambda x,y: (x*y),range(1,n+1))
print(value)

#q.13] Write a lambda that returns the larger of two numbers.
l=lambda a,b:a if a>b else b
print(l(3,4))

#q.14] Use lambda to check if number is divisible by 5
d=lambda x: "divisible" if x%5 == 0 else "not divisible"
print(d(11))

#q.15] Use lambda + map() to add 10 to each element of a list.
l1=[2,3,4,5]
a=list(map(lambda x: x+10,l1))
print(a)

#q.16] Use lambda to sort a list of dictionaries by a key (like "age").
names=[{"name": "lokesh", "age": 26}, {"name": "morris", "age": 39}, {"name": "Aditya", "age": 29}]
s=sorted(names, key=lambda x: x["age"])
print(s)

#q.17]  Write a lambda that returns True if a character is a vowel.
v=lambda x:x in('aeiouAEIOU')
print(v('E')) 

#q.18] Use lambda + filter to extract words of length > 5 from a list.
l=['ssss','banana','checcke']
b_w=list(filter(lambda x: len(x)>5,l))
print(b_w)

#q.19] Use lambda to calculate the area of a circle (πr²).
area=lambda rad:3.14*(rad**2)
print(area(2)) 

#q.20] Write a lambda to remove duplicates from a list using filter + set.
l=[1,2,3,4,2,3,4,2,1,5]
d=set(filter(lambda x: x,l))
print(d)

#q.21. Use lambda with reduce() to find the product of all numbers in a list.
l=[1,2,3,4]
mul=reduce(lambda x,y:x*y,l)
print(mul)

#q.22. Write a lambda that returns absolute value of a number.
g_s=lambda x: abs(x)
print(g_s(-50))

#q.23. Use lambda to sort a list of strings by their length.
words=["apple", "grapes", "banana", "pear"]
s=sorted(words, key=lambda s:len(s))
print(s)

#q.24. Use lambda to get only uppercase characters from a string
s="sTSYsteM"
s1=''
up=s.join(filter(lambda x:x.isupper(),s1))
print(up)

#q.25. Write a lambda that returns the square if number is even, cube if odd.
l=[1,2,3,4,5,6]
sqr=list(map(lambda x: x**2 if x%2==0 else x**3,l))
print(sqr)

#q.26. Use lambda with map to convert Celsius to Fahrenheit.
t=[10,5,12,19]
t1=list(map(lambda x: (x * 9/5) +32,t))
print(t1)

#q.27] Use lambda to extract only numeric values from a mixed list.
a=lambda a,b:sorted(a.lower())==sorted(b.lower())
print(a("listen", "silent"))

#q.28]Use lambda to extract only numeric values from a mixed list. 
mixed=[1,"a",2.5,"apple",10,True]
num=list(filter(lambda x: isinstance(x, (int, float)) and type(x) != bool, mixed))
print(num)

#q.29]Use lambda inside any() to check if any list element is negative.
nums =[1,2,-3,-4]
neg=any(map(lambda x: x < 0, nums))
print(neg)

#q.30]Use lambda to generate a function that multiplies any number by n 
mult=lambda n: (lambda x: x * n)
double=mult(2)
triple=mult(3)
print(double(10))
print(triple(10))