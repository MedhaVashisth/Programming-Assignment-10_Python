#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python program to find sum of elements in list

total = 0

# creating a list
list1 = [11, 5, 17, 18, 23]

# Iterate each element in list
# and add them in variable total
for ele in range(0, len(list1)):
	total = total + list1[ele]

# printing total value
print("Sum of all elements in given list: ", total)


# In[2]:


# Python program to multiply all values in the
# list using traversal


def multiplyList(myList):

	# Multiply elements one by one
	result = 1
	for x in myList:
		result = result * x
	return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))


# In[3]:


# Python program to find smallest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the first element
print("Smallest element is:", list1[0])


# In[4]:


# Python program to find largest
# number in a list

# list of numbers
list1 = [10, 20, 4, 45, 99]

# sorting the list
list1.sort()

# printing the last element
print("Largest element is:", list1[-1])


# In[5]:


# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2,n):
	if list1[i] > mx:
		secondmax = mx
		mx = list1[i]
	elif list1[i] > secondmax and 		mx != list1[i]:
		secondmax = list1[i]
	elif mx == secondmax and 		secondmax != list1[i]:
		secondmax = list1[i]

print("Second highest number is : ",	str(secondmax))


# In[6]:


# Python program to find N largest
# element from given list of integers

# Function returns N largest elements
def Nmaxelements(list1, N):
	final_list = []

	for i in range(0, N):
		max1 = 0
		
		for j in range(len(list1)):	
			if list1[j] > max1:
				max1 = list1[j];
				
		list1.remove(max1);
		final_list.append(max1)
		
	print(final_list)

# Driver code
list1 = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

# Calling the function
Nmaxelements(list1, N)


# In[7]:


# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")


# In[13]:


# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
i = 0

# using while loop	
while(i < len(list1)):
	
	# checking condition
	if list1[i] % 2 != 0:
		print(list1[i], end = " ")
	
	# increment i
	i += 1
	


# In[14]:


# Python3 code to Demonstrate Remove empty List
# from List using list comprehension

# Initializing list
test_list = [5, 6, [], 3, [], [], 9]

# printing original list
print("The original list is : " + str(test_list))

# Remove empty List from List
# using list comprehension
res = [ele for ele in test_list if ele != []]

# printing result
print("List after empty list removal : " + str(res))


# In[15]:


# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
	li_copy = li1[:]
	return li_copy


# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# In[16]:


# Python code to count the number of occurrences
def countX(lst, x):
	count = 0
	for ele in lst:
		if (ele == x):
			count = count + 1
	return count


# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,
										countX(lst, x)))


# In[ ]:




