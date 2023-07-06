**Data Types**

Most programs need to manipulate some kind of data, and that data can come in a lot of different forms, and we call them data types. A **String** is only one kind of data type found in Python. There's a bunch of others, like **integer** which represents whole numbers without fractions, and **float** which represents numbers with decimal points. Generally computers doesn't know how to mix different data types. for example, adding two integers makes perfect sense to a computer so dose adding two strings we just end up with a longer string that contains the two. But adding a string to an integer will result in an **error**. Errors are a common part of programming. 

**Variables**
Variables are names that we give to certain values in our programs. Those values can be of any data type, numbers, strings or even the results of operations. Let's Think of variables as containers for data. When we create a variable in our code, our computer reserves a chunk of it's own memory to store that value. This let's the computer access the variable later to read or modify the value. 

```py
# Let's see this in action.
# imagine a simple script to calculate the are of a rectangle using the formula area equals length times width.
# Area, Length, and width can all be represented by variables like this:

length = 10

width = 2

area = length * width

print(area)

20

```

In this script we are creating three variables and storing different values in each. The process of storing a value inside a variable is called **assignment**. Here we assign the length variable the value of 10. We assign the width variable the value of two and we assign the area variable with the result of the ***expression*** length times width. An **expression** is a combination of numbers, symbols or other variables that produce a result when evaluated.

**Variable Naming Restrictions**

First, you shouldn't use as variable names any of the key words or functions that Python reserves for its own, like print. Using these reserved terms will make your program confusing to read and will result in errors. Python also has some restrictions on the characters you can use to define a variable. Variable names can't have any spaces and they must start with either a letter or an underscore. Also, they can only be made up of letters, numbers and underscores.

**Expressions, Numbers, and Type Conversion**

What happens when we try to add an integer and a float

```py

print(7 + 8.5)

15.5

```

Python has no problem performing this operation. But why is that? Aren't integers and floats two different data types? They sure are, but there is a lot happening under the hood. Behind the scenes the computer is busy automatically converting our integer into a float. This let's Python then add together the values to return a result that is also a float. This process is called **implicit conversion**. The interpreter automatically converts one data type into another. So what if we really want to combine a string and a number, is it possible? it sure is possible but only with an **explicit conversion**. 

In Python, to convert between one data and another, we call the function with name of the type we're converting to.

In this script, we're first calculating the area of a triangle, area = (base*height)/2 and when printing it we're adding it to a string. print("The area of the triangle is: " + str(area)) To do this, we need to call the str() function to convert a number into a string. 

```py

base = 6
height = 3
area = (base + height) / 2
print("The area of the triangle is: " + str(area))
The area of the triangle is: 9.0 

```
 The area of the triangle is: 9.0 Our number got converted to a string and printed together with the message.

 str() - converts a value (often numeric) to a string data type

int() - converts a value (usually a float) to an integer data type

float() - converts a value (usually an integer) to a float data type

