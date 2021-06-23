#  Dictionaries and Sets are both data collections in Python

#  Dictionaries

#  Dict are another way to manage data but can be a little more Dynamic\
#  Dict work as a KEY AND VALUE
#  KEY = THE REFERENCE OF THE OBJECT
#  VALUE + WHAT THE DATA STORAGE MECHANISM YOU WISH TO USE
#  Dynamic as it we have Lists, and another dict inside a dict
#  Syntax of dicts - dict_name = {}
#  we use {} brackets to declare a Dict

#  key
student_1 = {
    "name": "James",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["data types", "git and github", "operators", "Lists and Tuples"]
}             #  Indexing            0                1              2              3

# Let's check if we have got the syntax right and print the dict
print(student_1)
print(type(student_1))

#  Finding which value applies to which key
print(student_1["stream"])

#  Printing the second last item from completed_lesson_names list
print(student_1["completed_lessons_names"][-2])
#  Or alternatively
print(student_1["completed_lessons_names"][2])

#  Could we apply CRUD on a dict?

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

#  Removing an item from completed_lesson_names
student_1["completed_lessons_names"].remove("operators")
print(student_1["completed_lessons_names"])

#  Built-In Methods to use with dict
#  To print all the keys - keys()
print(student_1.keys())

#  To print all the values only - values()
print(student_1.values())

#  Set are also Data collection
#  Syntax - set_name = ["", "", ""]
#  What is the difference between sets and dict
#  Sets are unordered - no indexing
shopping_list = {"eggs", "milk", "tea"}
#                  0        1       2
print(shopping_list)

car_parts = {"Engine", "Wheels", "Windows"}
print(car_parts)

#  Adding items to a set
car_parts.add("Seats")
print(car_parts)

#  Removing items to a set
car_parts.discard("Wheels")
print(car_parts)

#  Python also has frozen sets
#  Syntax - name = value([1, 2, ""])
planets = (["Mercury", "Saturn", "Neptune"])
print(planets)
