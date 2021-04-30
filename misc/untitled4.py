# Introduction to numpy:
# Package for scientific computing with Python
# Numerical Python, or "Numpy" for short, is a foundational package on which many of the most common data science packages are built.  Numpy provides us with high performance multi-dimensional arrays which we can use as vectors or matrices.  
# The key features of numpy are:
# 
# - ndarrays: n-dimensional arrays of the same data type which are fast and space-efficient.  There are a number of built-in methods for ndarrays which allow for rapid processing of data without using loops (e.g., compute the mean).
# - Broadcasting: a useful tool which defines implicit behavior between multi-dimensional arrays of different sizes.
# - Vectorization: enables numeric operations on ndarrays.
# - Input/Output: simplifies reading and writing of data from/to file.
#  
# Getting started with ndarray
# 
# **ndarrays** are time and space-efficient multidimensional arrays at the core of numpy.Let's get started by creating ndarrays using the numpy package. <br>
# An object of NumPy can be created as <br>
# NumPy.array( object , dtype=None ,order=None,ndmin=0) # order can be F /C/A ( col/row major)- ndmin specifies min dimensions of array



import numpy as np
a=np.array([1,2,3],dtype=complex)
print(a)


b=np.array([1,2,3,4,5,6],order='C',ndmin=2)
print(b)


# ndarray.shape- returns a tuple consisting of array dimensions <br>
# ndarray.ndim returns the number of array dimensions 
# ndarrary.dtype -returns datatype
# ndarray.size -returnsnumber of elements 

# How to create Rank 1 numpy arrays:

import numpy as np

an_array = np.array([3, 33, 333])  # Create a rank 1 array

print(type(an_array))              # The type of an ndarray is: "<class 'numpy.ndarray'>"




# test the shape of the array we just created, it should have just one dimension (Rank 1)
print(an_array.shape)
print( an_array.size)


# because this is a 1-rank array, we need only one index to accesss each element
print(an_array[0], an_array[1], an_array[2]) 


# In[3]:


an_array[0] =888            # ndarrays are mutable, here we change an element of the array

print(an_array)


# #ways of creating np objects 

import numpy as np
a=np.arange(1,10,2) # like range maethod
print (a)

b=np.linspace(10,20,5) # 5 equally spaced elements from start 10 and stop 20
print (b)


# 
# How to create a Rank 2 numpy array:
# 
# A rank 2 **ndarray** is one with two dimensions.  Notice the format below of [ [row] , [row] ].  2 dimensional arrays are great for representing matrices which are often useful in data science.


another = np.array([[11,12,13],[21,22,23]])   # Create a rank 2 array

print(another)  # print the array

print("The shape is 2 rows, 3 columns: ", another.shape)  # rows x columns                   

print("Accessing elements [0,0], [0,1], and [1,0] of the ndarray: ", another[0, 0], ", ",another[0, 1],", ", another[1, 0])
another.resize(3,3)
print(another)
print(another.T)


# There are many way to create numpy arrays:
# Here we create a number of different size arrays with different shapes and different pre-filled values.  numpy has a number of built in methods which help us quickly and easily create multidimensional arrays.


import numpy as np
x=np.empty((3,2),dtype=int)
print (x)


import numpy as np

# create a 2x2 array of zeros
ex1 = np.zeros((2,2))      
print(ex1)                              


# create a 2x2 array filled with 9.0
ex2 = np.full((2,2), 9.0)  
print(ex2)   


# create a 2x2 matrix with the diagonal 1s and the others 0
ex3 = np.eye(2,2)
print(ex3)  

# create an array of ones
ex4 = np.ones((1,2))
print(ex4)    

# notice that the above ndarray (ex4) is actually rank 2, it is a 2x1 array
print(ex4.shape)

# which means we need to use two indexes to access an element
print()
print(ex4[0,1])


# create an array of random floats between 0 and 1
ex5 = np.random.random((2,2))
print(ex5)    

# Slice indexing:
# 
# Similar to the use of slice indexing with lists and strings, we can use slice indexing to pull out sub-regions of ndarrays.

import numpy as np

# Rank 2 array of shape (3, 4)
an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
print(an_array)


# Use array slicing to get a subarray consisting of the first 2 rows x 2 columns.

a_slice = an_array[:2, 1:3]
print(a_slice)

# When you modify a slice, you actually modify the underlying array.

print("Before:", an_array[0, 1])   #inspect the element at 0, 1  
a_slice[0, 0] = 1000    # a_slice[0, 0] is the same piece of data as an_array[0, 1]
print("After:", an_array[0, 1])    


# Use both integer indexing & slice indexing
# 
# We can use combinations of integer indexing and slice indexing to create different shaped matrices.

# Create a Rank 2 array of shape (3, 4)
an_array = np.array([[11,12,13,14], [21,22,23,24], [31,32,33,34]])
print(an_array)

# Using both integer indexing & slicing generates an array of lower rank
row_rank1 = an_array[1, :]    # Rank 1 view 

print(row_rank1, row_rank1.shape)  # notice only a single []


# Slicing alone: generates an array of the same rank as the an_array
row_rank2 = an_array[1:2, :]  # Rank 2 view 

print(row_rank2, row_rank2.shape)   # Notice the [[ ]]


#We can do the same thing for columns of an array:

print()
col_rank1 = an_array[:, 1]
col_rank2 = an_array[:, 1:2]

print(col_rank1, col_rank1.shape)  # Rank 1
print()
print(col_rank2, col_rank2.shape)  # Rank 2

# Array Indexing for changing elements:

# Sometimes it's useful to use an array of indexes to access or change elements.

# Create a new array
import numpy as np
an_array = np.array([[11,12,13], [21,22,23], [31,32,33], [41,42,43]])

print('Original Array:')
print(an_array)


z=an_array[1:3,1:2]
print (z)


# Create an array of indices
col_indices = np.array([0, 1, 2, 0])
print('\nCol indices picked : ', col_indices)

row_indices = np.arange(4)
print('\nRows indices picked : ', row_indices)


# Examine the pairings of row_indices and col_indices.  These are the elements we'll change next.
for row,col in zip(row_indices,col_indices):
    print(row, ", ",col)


# Select one element from each row
print('Values in the array at those indices: ',an_array[row_indices, col_indices])


# Change one element from each row using the indices selected
an_array[row_indices, col_indices] += 100000

print('\nChanged Array:')
print(an_array)

# Boolean Indexing
# Array Indexing for changing elements:

# create a 3x2 array
an_array = np.array([[11,12], [21, 22], [31, 32]])
print(an_array)


# create a filter which will be boolean values for whether each element meets this condition
filter = (an_array > 15)
filter


# Notice that the filter is a same size ndarray as an_array which is filled with True for each element whose corresponding element in an_array which is greater than 15 and False for those elements whose value is less than 15.



# we can now select just those elements which meet that criteria
print(an_array[filter])

# For short, we could have just used the approach below without the need for the separate filter array.

an_array[(an_array % 2 == 0)]


# What is particularly useful is that we can actually change elements in the array applying a similar logical filter.  Let's add 100 to all the even values.

an_array[an_array % 2 == 0] +=100
print(an_array)


# Datatypes and Array Operations

ex1 = np.array([11, 12]) # Python assigns the  data type
print(ex1.dtype)


ex2 = np.array([11.0, 12.0]) # Python assigns the  data type
print(ex2.dtype)


# you can use this to force floats into integers (using floor function)
ex4 = np.array([11.1,12.7], dtype=np.int64)
print(ex4.dtype)
print()
print(ex4)


# Arithmetic Array Operations: Scalar and vector operations 

x = np.array([[111,112],[121,122]], dtype=np.int)
y = np.array([[211.1,212.1],[221.1,222.1]], dtype=np.float64)

print(x)
print()
print(y)
print ( np.add(x,1))
print(np.subtract(y,2))
print(np.power(x,2))


# add vector 
print(x + y)         # The plus sign works
print()
print(np.add(x, y))  # so does the numpy function "add"


# In[19]:

# subtract
print(x - y)
print()
print(np.subtract(x, y))

# multiply
print(x * y)
print()
print(np.multiply(x, y))

# divide
print(x / y)
print()
print(np.divide(x, y))

# square root
print(np.sqrt(x))


# exponent (e ** x)
print(np.exp(x))


# Statistical Methods, Sorting, and <br> <br> Set Operations:
# Basic Statistical Operations:

# setup a random 2 x 4 matrix
import numpy as np
arr = 10 * np.random.randn(2,5)
print(arr)

# compute the mean for all elements
print(arr.mean())

# sum all the elements
print(arr.sum())
print(arr.min())
print(arr.max())

# compute the medians
print(np.median(arr, axis = 1))


print(np.argmax(arr, axis = 1))

print(np.argmin(arr, axis = 0))

# Sorting:

# create a 10 element array of randoms
unsorted = np.random.randn(10)

print(unsorted)

# create copy and sort
sorted = np.array(unsorted)
sorted.sort()

print(sorted)
print()
print(unsorted)

# inplace sorting
unsorted.sort() 

print(unsorted)

# Finding Unique elements:

array = np.array([1,2,1,4,2,1,4,2])

print(np.unique(array))


import numpy as np

start = np.zeros((4,3))
print(start)


# sum elements in the array
ex1 = np.array([[11,12],[21,22]])

print(np.sum(ex1))          # add all members


print(np.sum(ex1, axis=0))  # columnwise sum


print(np.sum(ex1, axis=1))  # rowwise sum


# Element-wise Functions: </p>
# 
# For example, let's compare two arrays values to get the maximum of 
# random array
x = np.random.randn(8)
x


# another random array
y = np.random.randn(8)
y




# returns element wise maximum between two arrays

np.maximum(x, y)


# Reshaping array:
# grab values from 0 through 19 in an array
arr = np.arange(20)
print(arr)

# reshape to be a 4 x 5 matrix
arr.reshape(4,5)


# Transpose:
ex1 = np.array([[11,12],[21,22]])

ex1.T


# 
# Merging data sets:
# </p>

# In[58]:


K = np.random.randint(low=2,high=50,size=(2,2))
print(K)

print()
M = np.random.randint(low=2,high=50,size=(2,2))
print(M)


# In[59]:


np.vstack((K,M))


# In[60]:


np.hstack((K,M))

# In[61]:

np.concatenate([K, M], axis = 0)  # like vstack



np.concatenate([K, M.T], axis = 1) # like hstack 
