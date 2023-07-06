We can use the concept of branching to have our code alter its execution sequence depending on the values of variables. We can use an if statement to evaluate a comparison. We start with the if keyword, followed by our comparison. We end the line with a colon. The body of the if statement is then indented to the right. If the comparison is True, the code inside the if body is executed. If the comparison evaluates to False, then the code block is skipped and will not be run.

```py

def username_length_checker(username):
  if len(username) < 3:
    print("Invalid Username must be more than three characters")
    elif len(username) > 15:
      print("Invalid Username must be less than fifteen characters")
    else:
      print("Username is valid")

```
