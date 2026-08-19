#!/usr/bin/env python
# coding: utf-8

# In[19]:


list1=["Aarav","Isha","Rohan","Sneha","Kabir"]
print('3rd student:',list1[2])
list1[2] = "Rohan Patil"
print("Updated Student 3: ", list1[2])
list1.append("Ananya")
list1.append("Vihaan")
print("New Students added: ", list1[5:])
list1.remove("Kabir")
print(f"Student removed: Kabir")
print(f"Updated list: {list1}")
print("Total number of students registered: ", len(list1))

if "Isha" in list1:
    print("Isha is registered in the list")
else:
    print("Isha is not in the list")

list1.sort()
print(f"Final list(Alphabetical Order): {list1}")
backup_students = list1.copy()
print(f"Backup Student list: {backup_students}")

list2 = ["Meera", "Arjun", "Isha"]
print(f"AI Hackathon list: {list2}")

all_participants = list1 + list2
print(f"All participants list: {all_participants}")





# In[ ]:




