#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Voting Eligibility
age = int(input("Enter your age "))
if(age<18):
    print("not eligible for voting")
else:
    print("eligible for voting")


# In[2]:


#2. Even or Odd
n = int(input("Enter the number "))
if n%2==0 :
    print("The number is an EVEN number")
else:
    print("The number is an ODD number")


# In[ ]:


#3. Reverse of  String
s = input("Enter the sting ")
a = s[::-1]
print("The reversed string is ",a)


# In[4]:


#4. Positive or not
n = int(input("Enter a number "))
if n>0:
    print("The number entered is a POSITIVE number")
else:
    print("The number entered is NOT a POSITIVE number")


# In[ ]:


#5. Roots of a Quadratic Equation
z = print("Enter the the quadratic equation's terms respectively")
a=float(input("enter the constant term of x^2 " ))
b=float(input("enter the constant term of x " ))
c=float(input("enter the constant term "))
d = b**2-4*a*c
if(d>0):
    print("The roots are real and distinct")
    print("The roots of the equation are ",(-b+d*0.5)/2*a,",",(-b-d*0.5)/2*a)
elif(d==0):
    print("The roots are real and equal")
    print("The root of the equation is ",-b/2*a)
else:
    print("The roots are imaginary")
    print("The roots of the equation are ",(-b+d*0.5)/2*a,",",(-b-d*0.5)/2*a)


# In[ ]:


#6. Check the number is posivite ,negative or zero
n = int(input("Enter a number "))
if(n>0):
    print("The number entered is a POSITIVE number")
else:
    if(n<0):
        print("The number entered is a NEGATIVE number")
    else:
        print("The number is 0")


# In[6]:


#7. Take numbers and print in words
n = int(input("Enter a number in between 1 to 5 "))
if n==1:
    print("one")
elif n==2:
    print("two")
elif n==3:
    print("three")
elif n==4:
    print("four")
elif n==5:
    print("five")
else:
    print("given number is not in between 1 to 5")


# In[ ]:


#8. Vowel or NOT a Vowel
z = input("Enter a character ")
if(z=='A' or z=='E' or z=='I' or z=='O' or z=='U' or z=='a' or z=='e' or z=='i' or z=='o' or z=='u'):
    print(z, "is a Vowel")
else:
    print(z, "is a NOT a Vowel")

