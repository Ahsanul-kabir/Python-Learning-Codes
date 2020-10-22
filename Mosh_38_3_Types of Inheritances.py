#!/usr/bin/env python
# coding: utf-8

# # Single Inheritance

# <img src="Pictures\11n.PNG" width="200" height="200">

# In[1]:


# Base class 
class Parent: 
	def func1(self): 
		print("This function is in parent class.") 

# Derived class 
class Child(Parent): 
	def func2(self): 
		print("This function is in child class.") 

# Driver's code 
object = Child() 
object.func1() 
object.func2() 


# # Multiple Inheritance

# <img src="Pictures\22n.PNG" width="300" height="300">

# In[2]:


# Base class 
class Mother: 
	mothername = "" 
	def mother(self): 
		print(self.mothername) 

# Base class2 
class Father: 
	fathername = "" 
	def father(self): 
		print(self.fathername) 

# Derived class 
class Son(Mother, Father): 
	def parents(self): 
		print("Father :", self.fathername) 
		print("Mother :", self.mothername) 

# Driver's code 
s1 = Son() 
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents() 


# # Multilevel Inheritance

# <img src="Pictures\33n.PNG" width="300" height="300">

# In[3]:



# Base class 
class Grandfather: 
	grandfathername ="" 
	def grandfather(self): 
		print(self.grandfathername) 

# Intermediate class 
class Father(Grandfather): 
	fathername = "" 
	def father(self): 
		print(self.fathername) 

# Derived class 
class Son(Father): 
	def parent(self): 
		print("GrandFather :", self.grandfathername) 
		print("Father :", self.fathername) 

# Driver's code 
s1 = Son() 
s1.grandfathername = "Srinivas"
s1.fathername = "Ankush"
s1.parent() 


# # Hierarchical Inheritance

# <img src="Pictures\44.PNG" width="300" height="300">

# In[4]:


# Base class 
class Parent: 
	def func1(self): 
		print("This function is in parent class.") 

# Derived class1 
class Child1(Parent): 
	def func2(self): 
		print("This function is in child 1.") 

# Derivied class2 
class Child2(Parent): 
	def func3(self): 
		print("This function is in child 2.") 

# Driver's code 
object1 = Child1() 
object2 = Child2() 
object1.func1() 
object1.func2() 
object2.func1() 
object2.func3() 

