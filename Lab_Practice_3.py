#!/usr/bin/env python
# coding: utf-8

# In[2]:


def operations():

    num1 = int(input("Enter first num: "))
    num2 = int(input("Enter second num: "))
    choice = input("Choose the operation (+, -, /, *): ").lower()
    if choice == "add" or choice == "+":
        print(f"Addition is: {num1+num2}") 
    elif choice == "subtract" or choice == "minus" or choice == "-":
        print(f"Subtraction is: {num1-num2}") 
    elif choice == "divide" or choice == "/":
        print(f"Addition is: {num1/num2}") 
    elif choice == "multiply" or choice == "*" or choice == "x":
        print(f"Addition is: {num1*num2}") 

while True:

    operations()

    exit = input("Do you want to quit?" ).lower()

    if exit == "yes":
        break
    elif exit == "no":
        continue
    else:
        print("Invalid Choice")



# In[7]:


num = int(input("Number: "))

if num % 2 == 0:
    print("The number is positive.")
elif num % 2 != 0:
    print("The number is odd.")
elif num == 0:
    print("The number is zero.")



# In[10]:


age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age >= 13 and age <= 19:
    print("You are a teenager.")

elif age <= 20 and age <= 59:
    print("You are an Adult.")

elif age >=  60:
    print("You are on old man.")


# In[1]:


pin = int(input("Enter your pin: "))
master_pin = 1000



def balance():
    acc_balance = 10000000
    print(f"Your account balance is: {acc_balance}")

    amm = int(input("Enter the ammount you wish to withdraw: "))


    if acc_balance >= amm:
        print("You have sufficient balance in your account.")


    elif acc_balance < amm:
        print("Sorry you have insufficient balance in your account.")

        return acc_balance



acc_balance = balance()

def withdraw():
    confirmation =  input("Do you comfirm the withdrawal? ").lower()

    if confirmation == "yes":
        print("Withdrawal successful!\n")
        print(f"New Account Balance is: {acc_balance - amm}")

    elif confirmation == "no":
        print("Withdrawal Canceled by the User!")



if pin == master_pin:
    print("The pin is correct!")
    balance()
    withdraw()

elif pin != master_pin:
    print("Sorry the pin is incorrect.")




# In[5]:


user = int(input("Enter a number: "))
x = range(0 ,user, 2)

print(list(x))


# In[8]:


cars = ["bmw", "benz", "ferrari", "volkswagen"]

x = cars[1]

print(x)


# In[28]:


list1 = []

print("======list1======")
for i in range(5):
    num1 = int(input("Enter the number: "))
    list1.append(num1)

print(list1)

list2 = []
print("======list2======")
for i in range(5):
    num2 = int(input("Enter the number: "))
    list2.append(num2)

print(list2)

final_list = []
result1 = list1[0] + list2[0]
final_list.append(result1)
result2 = list1[1] + list2[1]
final_list.append(result2)
result3 = list1[2] + list2[2]
final_list.append(result3)
result4 = list1[3] + list2[3]
final_list.append(result4)
result5 = list1[4] + list2[4]
final_list.append(result5)

print(f" The final list is: {final_list}")



# In[1]:


matrix1 = []


for i in range(2):
    row1 = []

    for j in range(2):
        num1 = int(input("Enter a number: "))
        row1.append(num1)
    matrix1.append(row1)

print("============MATRIX 1===========")
for row1 in matrix1:
    print(row1)

matrix2 = []


for k in range(2):
    row2 = []

    for k in range(2):
        num2 = int(input("Enter a number: "))
        row2.append(num2)
    matrix2.append(row2)

print("============MATRIX 2===========")
for row2 in matrix2:
    print(row2)


final_matrix = []

for m in range(2):
    result = []
    for n in range(2):
        result1 = matrix1[m][n] + matrix2[m][n]
        result.append(result1)

    final_matrix.append(result)


print("============FINAL MATRIX===========")
for a in final_matrix:
    print(a)



# In[ ]:




