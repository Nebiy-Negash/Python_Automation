Python can let us compare values. This lets us check whether something is smaller than, equal to, or bigger than something else. This allows us to take the results of our expression and use them to make decisions.

The comparison operators include: 

- ==  (equality) 

- !=  (not equal to) 

- <   (less than)  and  > (greater than)


- <=  (less than or equal to) and  >=    (greater than or equal to)

let's see some examples

```py
# greater than operator
print(10 > 1)

#output

True

```
the value **true** is printed as a result. **True** is a value that belongs to another data type called the **Boolean**. Boolean represents one of two possible states, either **true** or **false**. Every time we compare things in Python the result is a Boolean of that appropriate value. 

```py
# equality operator is formed putting two equal signs together.  
print("cat" == "dog")

# output

False
```
We use this operator to test whether two things are equal to each other. In this example the string cat is not equal to the string dog, So the Boolean value is printed as false.

```py
# opposite comparison is formed by pairing an exclamation mark and an equal sign. by paring these we're using the not equals operator.

print(1 != 2) # which is the negated form of the equality operator.

# output

True
```

In this particular line of code the operator checks that 1 isn't equal to 2 and the resulted Boolean value is true. 

- Note comparing an integer and a string will result in an error with the exception of the equality operator which results in a Boolean value false

On top of the comparison and equality operators, Python has a set of **logical operators**. These operators allow us to connect multiple statements together and perform more complex comparisons. In Python the logical operators are the words, **and**, **or**, and **not**. 

```py
# this is comparing the alphabetic order.
# The greater than > operator checks if the left string has a higher 
# Unicode value than the right string. If true, the Python interpreter
# returns a True result. Since W has a Unicode value of 87, and you can 
# easily calculate that F has a Unicode value of 70, this comparison is
# the same as 87 > 70. As this is true, Python will return a True 
# result.

print("Wednesday" > "Friday")

True

print("Yellow" > "Cyan" and "Brown" > "Magenta")

#output

False

```

To evaluate as true the **and** operator would need both expressions to be true at the same time. If we were to use the **or** operator the result would be true, If either of the expression is true, and false only when both expressions are false.