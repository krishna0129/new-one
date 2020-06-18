#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.simple calculator for operators
x =int(input("enter the value of x"))
y =int(input("enter the value of y"))
print("sum of two numbers =",x+y)
print("difference of two numbers =",x-y)
print("product of two numbers =",x*y)
print("division of two numbers =",x/y)
print("modulus of two numbers =",x%y)
print("exponent of two numbers =",x**y)
print("floor division of two numbers =",x//y)


# In[12]:


#2.program for calculating simple interest
p=float(input("enter the principle amount"))
t=float(input("enter the time"))
r=float(input("enter the rate of interest"))
print("simple interest =",(p*t*r)/100)


# In[6]:


#3.program for calculating area of circle
r=int(input("enter the radius of circle"))
print("the area of circle =",(22/7)*r**2)


# In[9]:


#4.program for calculating area of triangle
a=int(input("enter of first side of triangle"))
b=int(input("enter the second side of triangle"))
c=int(input("enter the third side of triangle"))
s =(a+b+c)/2
print("the area of triangle =",(s*(s-a)*(s-b)*(s-c))**0.5)


# In[11]:


#5.program for converting celsius to fahrenheit
c=float(input("enter temperature in celsius"))
f=(c*(9/5))+32
print("temperature in fahrenheit =",f)


# In[13]:


#6.program for calculating area of rectangle
l=float(input("enter the length of rectangle"))
b=float(input("enter the breadth of rectangle"))
a=l*b
print("the area of rectangle =",a)


# In[14]:


#7.program for calculating the perimeter of a square
s=float(input("enter the length of side of a square"))
p=4*s
print("the primeter of square =",p)


# In[15]:


#8.program for calculating the circumference of circle
r=float(input("enter the radius of circle"))
c=2*(22/7)*r
print("the circumference of circle =",c)


# In[17]:


#9.program for swapping two numbers
a=int(input("enter the first number"))
b=int(input("enter the second number"))
temp=a
a=b
b=temp
print("the value of a after swapping =",a)
print("the value of b after swapping =",b)


# In[ ]:




