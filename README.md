-How to create a new project in PyCharm `click on file` then `enter name_of_file` then `enter`

# Python Data Collections
- Lists
- Tuples
- Dict
- Sets

## Lists (AKA array in other languages)
- E.g. shopping lists - multiple items
- add, edit, delete, update
- What is `CRUD` - `Create` `Read` `Update` `Delete`

### Let's create a shopping list
- `Syntax [] - name_of_list = ["first_item","second_item"]`

```Python
shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
               #    0        1            2            3       4
print(shopping_list)
#  Checking the type of this data with type()
print(type(shopping_list))
```

How can I access eggs using the same concept that we learned yesterday using INDEXING?
```Python
print(shopping_list[1])  #  will display eggs
print(shopping_list[-1])  #  will display bread as it's the last item
```
How can I replace an item in the list?
```Python
shopping_list[0] = "mangoes"
print(shopping_list)
```
How can I add an item to the shopping list?
```Python
shopping_list.append("tuna")
print(shopping_list)
```
How can I remove an item from the shopping list?
```Python
shopping_list.remove("tea")
print(shopping_list)
#  Or alternatively
shopping_list.pop(1)  #  To remove the index in the list
print(shopping_list)
```
We can have multiple data types in the same list
```Python
mix_list = [1, 2.3, "four"]
        #  int, float, string
print(type(mix_list))
```
##  What are Tuples and what is the difference between lists and Tuples
- `Syntax () - name_of_tuple = ("", "", "")`
```Python
essentials = ("paracetamol", "milk", "butter")
print(essentials)
print(type(essentials))
```
- `essentials.pop(1)`    results in an AttributeError

That is because lists are **MUTABLE** and Tuples are **IMMUTABLE**

#  Dictionaries and Sets are both data collections in Python

##  Dictionaries

-  Dict are another way to manage data but can be a little more Dynamic\
-  Dict work as a KEY AND VALUE
    -  KEY = THE REFERENCE OF THE OBJECT
    -  VALUE = WHAT THE DATA STORAGE MECHANISM YOU WISH TO USE
-  Dynamic as it we have Lists, and another dict inside a dict
-  Syntax of dicts - `dict_name = {}`
-  we use {} brackets to declare a Dict

```Python
#  key
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]
}             #  Indexing            0                1              2              3
```

Let's check if we have got the syntax right and print the dict
```Python
print(student_1)
print(type(student_1))
```

Finding which value applies to which key
```Python
print(student_1["stream"])
```

Printing the second last item from completed_lesson_names list
```Python
print(student_1["completed_lessons_names"][-2])
#  Or alternatively
print(student_1["completed_lessons_names"][2])
```
### Could we apply CRUD on a dict?

- Changing or adding data
   - If the key entered is not in the dictionary, then a new key will be added with the corresponding value
```Python
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
```

- Removing an item from completed_lesson_names
```Python
student_1["completed_lessons_names"].remove("operators")
print(student_1["completed_lessons_names"])
```

###  Built-In Methods to use with dict
-  To print all the keys - keys()
```Python
print(student_1.keys())
```

-  To print all the values only - values()
```Python
print(student_1.values())
```

##  Set are also Data collection
-  Syntax - `set_name = ["", "", ""]`

What is the difference between sets and dict
-  Sets are unordered - no indexing
```Python
shopping_list = {"eggs", "milk", "tea"}
#                  0        1       2
print(shopping_list)

car_parts = {"Engine", "Wheels", "Windows"}
print(car_parts)
```

-  Adding items to a set
```Python
car_parts.add("Seats")
print(car_parts)
```

-  Removing items to a set
```Python
car_parts.discard("Wheels")
print(car_parts)
```

###  Python also has frozen sets
- Syntax - `name = value([1, 2, ""])`
```Python
planets = (["Mercury", "Saturn", "Neptune"])
print(planets)
```