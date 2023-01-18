1)	 Check if the first and last number of a list is the same
Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
Given:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
Expected Output:
Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False
=============================
Code:
def check(l1):
    l2=l1
    if l2[0]==l2[-1]:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
print(check(numbers_x))
print(check(numbers_y))
==========================================================================================================================================
2)	 Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those numbers which are divisible by 5
Expected Output:
Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55
========================================
Code:
l1=[10, 20, 33, 46, 55]
for i in l1:
    if i%5==0:
        print(i)
   ============================================================================================================================================
3)	Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.
Given:
str_x = "Emma is good developer. Emma is a writer"
Expected Output:
Emma appeared 2 times
==========================================
Code:
str_x = "Emma is good developer. Emma is a writer"
c=str_x.count("Emma")
print(f"Emma appeared {c} times")
====================================================================================================================================================
4)	 Check Palindrome Number
Write a program to check if the given number is a palindrome number.
A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
Expected Output:
original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
============================================
Code:
val=input(("original number:"))
if(val==val[::-1]):
      print("Yes. given number is palindrome number")
else:
      print("No. given number is not palindrome number")
====================================================================================================================================================
5)	 Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
=================================================
Code:
val=input("enter the number:")
l=[]
for n in val:
    l.append(n)
l.reverse()
s = ''.join(l)
print(s)
