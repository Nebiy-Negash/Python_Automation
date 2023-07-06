**Functions**

we have seen a few functions so far: the print() function which writes text on the screen, the type() function which tells us the type of a certain value, and the str() function which converts numbers into a string. All those functions come as part of the Python programming language. So now let's look at how we define a function.

```py
def greeting(name): 
    print("Welcome, " + name)

```

here our function takes in the parameter, that parameter is name and prints a greeting for that name. 

To define a function we use the keyword **def**. The name of the function is what comes after the keyword, In this example the functions name is **greeting**. So to call the function later in the script we'll use the word greeting. After the name we have the parameters of the function which are written between parentheses. In this example we only have one parameter, name, followed by a **colon** at the end of the line. After the colon we have the body of the function. That's where we state what we want our function to do. Note how the body is **indented** to the right. This is a key characteristics of Python. In this example, the body contains just one line that calls the print() function. Looks simple, But creating function can actually be super powerful. The body of a function can have as many lines as we want it to and do all sorts of fun stuff. 

**Returning Values**

We've seen how we can pass values into functions as parameters by passing values like the name in the example above. But what about getting values out a function? This is where the concept of **return values** comes into play. The work that functions do can produce new results. Sure, we can print the results on the screen, but what if we wanted to use those results later in our script or didn't want to print them at all? We can do this by returning values from the functions we define ourselves. Let's see an example by calculating the area of a triangle. 

```py
# the area of a triangle is calculated as base times height divided by 2.
# imagine we need to calculate this value several times in our code. 

def area_of_triangle(base, height):
    return base * height / 2

areaA = area_of_triangle(5, 4)
areaB = area_of_triangle(7 , 3)

sum = areaA + areaB

print("The sum of both areas is: " + str(sum))
The sum of both areas is: 28.5
```

This shows the power of the return statement. It allows us to combine calls to functions and to more complex operations which makes our code more reusable. Return statements in python are even more interesting because we can use them to return more than one value. Let's say you have a duration of time in seconds and you want to convert that to the equivalent number of hours, minutes, and seconds.

```Py
def convert_seconds(seconds):

    hours = seconds // 60 # this will give us how many seconds are in an hour

    minutes = (seconds - hours * 3600) // 60 # this will give us how many minutes are left once we subtract the hour

    remainingSeconds = seconds - hours * 3600 - minutes * 60 # then this will give us the remaining seconds after we subtract the hours and minutes.

    return hours, minutes, remainingSeconds 

```

The double slash operator is called floor division. A floor division divides a number and takes the integer part of the division as a result. example 
``` py 
floor = 5 // 2 
2 
# here it gives us two instead of 2.5

```
In our example, the first operation is calculating how many hours are in a given amount of seconds. While the second works out how many minutes are left once we subtract the hours and then how many seconds remain after subtracting minutes. We end up with three numbers as a result. So the function returns all three of them.

```py

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
1 23 20

```
Because we know that the function returns three values, we assign the result of the function to three different variables. There's one last thing we should call out about returning values. It is possible to return nothing and that's perfectly okay.