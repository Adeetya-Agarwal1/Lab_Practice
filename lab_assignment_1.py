#!/usr/bin/env python
# coding: utf-8

# In[15]:


a= int( input("Enter num1: "))
b= int( input("Enter num2: "))
c=a+b
d=a/b
e=a*b
f=a-b
print("Addition=", c)
print("Subtraction =", f)
print("Divsision =", d)
print("Multiplication =", e)


# In[31]:


record = []

name = input("Name: ")
marks = int(input("Marks: "))
record.append(name)
record.append(marks)
print(record)


# In[36]:


name = input("Enter your name: ")
print(f"Hello! {name}")

fruits = []

fruit1 = input("Fruit 1: ")
fruit2 = input("Fruit 2: ")
fruit3 = input("Fruit 3: ")

fruits.append(fruit1)
fruits.append(fruit2)
fruits.append(fruit3)

print(f"Your list of fruits are: {fruits}")


# In[40]:


list1 = ["banana", "apple", "mango"]
print("List of items are: ", list1)
print("Access list item: ", list1[0])


# In[3]:


list2 = ["cherry", "kiwi", "orange", "banana"]
list2[1:3] = ["blackcurrent", "watermelon"]
print(list2)


# In[4]:


list1=["apple", "banana", "cherry", ]
print('Item List',list1)
print("List item (1) is  :",list1[1])

list1.append( "orange")
print('List of appended items are:', list1)

list1[0]= "black current"
print("the updated list:",list1)

list1.insert(0, "apple")
print("Tnserted item List:", list1)

list1.remove("cherry")
print("Trimmed list", list1)

list1.sort()
print("Alphanumerically sorted list:", list1)

listf= list1.copy()
print('Coppied list:',listf)

list2=['dell', 'lenovo','Hp']
list3=['samsung', 'Apple', "motorolla"]

print('listA',list2)
print('listA',list3)

listb= list2+list3
print('combined list',listb)

C = listb.count("Apple")
print('Number of Apple:',C)

listb.pop(5)
print('poped list:',listb)

listb.reverse()
print('reverse list',listb)

x=listb.index('samsung')
print('Samsung index nunmber:',x)

print('list from 3rd to 5th:',listb[2:5])


# In[ ]:




