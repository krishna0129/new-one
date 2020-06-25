#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.calculating the length of a string
str=input("enter the string : ")
print("the length of string is : ",len(str))


# In[15]:


#2.calculating the no. of characters in a string
string = input("Enter a string ")  
add = {} 
for i in string: 
    if i in add: 
        add[i] += 1
    else: 
        add[i] = 1  
print ("Count of all characters/n" +str(add))


# In[11]:


#3.getting a single string from two strings and swapping first two characters
str1=input("enter the first string : ")
str2=input("enter the second string : ")
str3=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],str3)
print("combined string after swapping of characters")
print(str1," ",str2)


# In[14]:


#4.displaying strings in uppercase and lowercase
a=input("enter the string : ")
print("the string in upper case is : ",a.upper())
print("the string in lowercase is : ",a.lower())


# In[ ]:


#5.removing a newline from a string
a=input("enter the string")
print("the string is : ",a)
a=a.rstrip("/n")
print("the string after removing newline is : ",a)


# In[18]:


#6.counting the occurrences of substring in a given string
a=input("enter the string : ")
sub=input("enter the substring : ")
count=a.count(sub)
print("the no. of occurrences = ",count)


# In[3]:


#7.converting string in to a list
a=input("enter the string : ")
for x in a:
    print(x)


# In[5]:


#8.program for deletion of a character
a=input("enter the string : ")
i=int(input("enter the index of character you want to delete : "))
a[:i]+a[(i+1):]


# In[10]:


#9.printing every character of a string
a=input("enter the string : ")
for i in range(len(a)):
    print((i+1),".",a[i])


# In[11]:


#10.finding length of string without using length function
str="refrigerator"
count=0
for i in str:
    count=count+1
print("the length of string is : ",count)


# In[ ]:




