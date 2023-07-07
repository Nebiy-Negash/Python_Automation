# What are strings

A **string** is a data type in Python that's used to represent a piece of text. It's is written between quotes, either double or single quotes. Mixing double and single quotes will raise a syntax error. A string can be as short as zero characters meaning empty string or really long. we can also operate on strings to get different results like adding a string to another string to make a longer string this action is called **concatenating**, or multiply by a number which multiplies the content of the string that many times.

```py
my_str_1 = "this is an example string"
my_str_2 = 'this is also a string'
```
# Parts of a String

We can access parts of a string using different methods. for example if we have a text that's too long to display and we want to show just a portion of it. Or if we want to make an acronym by taking the first letter of each word in a phrase. We can that through an operation called **string indexing**. This operation lets us access the character in a giving position or index using square brackets and the number of the position we want. ***NOTE*** Python starts counting indexes from 0 not 1

```py
name = "James Smith"
print(name[1])
# this will output the letter a
print(name[0])
# this will out put the letter J
```

Knowing that indexes start at 0, which one will be the last index in the name string? it'll always be one less than the length of the string. In this case our name has 11 characters, yes spaces count us a characters too. So the last index character is h at index 11. what if we don't know the length of the string and want to access the last string in that case we can use -ve indexes to let us access the last character.

```py
example = "a string of characters with unknown length"
print(example[-1])
# this will output the letter h.
```

Another way to get part of a string is **Slicing**. Slicing is the portion of a string that can contain more than one character, also sometimes called a substring. We do that by creating a range using a colon as a separator. The range we use when accessing a slice of a string works just like the one created by the range function. It includes the first number, but goes up to one less than the last number.

```py
example = "a string of characters with unknown length"
# slice 'a string' from above example
sliced_str = example[0 : 9]
print(sliced_str)
# this will output 'a string' 
```
***NOTE*** the length from 'a' to 'g' is 8, but we used [0 : 9] in our code this is because Python gives us up to index 9 but does not include 9.


