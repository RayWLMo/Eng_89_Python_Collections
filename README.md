-How to create a new project in PyCharm `click on file` then `enter name_of_file` then `enter`

# Python Data Colelctions
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

```
shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
               #    0        1            2            3       4
print(shopping_list)
#  Checking the type of this data with type()
print(type(shopping_list))
```

How can I access eggs using the same concept that we learned yesterday using INDEXING?
```
print(shopping_list[1])  #  will display eggs
print(shopping_list[-1])  #  will display bread as it's the last item
```
How can I replace an item in the list?
```
shopping_list[0] = "mangoes"
print(shopping_list)
```
How can I add an item to the shopping list?
```
shopping_list.append("tuna")
print(shopping_list)
```
How can I remove an item from the shopping list?
```
shopping_list.remove("tea")
print(shopping_list)
#  Or alternatively
shopping_list.pop(1)  #  To remove the index in the list
print(shopping_list)
```
We can have multiple data types in the same list
```
mix_list = [1, 2.3, "four"]
        #  int, float, string
print(type(mix_list))
```
##  What are Tuples and what is the difference between lists and Tuples
- `Syntax () - name_of_tuple = ("", "", "")`
```
essentials = ("paracetamol", "milk", "butter")
print(essentials)
print(type(essentials))
```
- `essentials.pop(1)`    results in an AttributeError

That is because lists are **MUTABLE** and Tuples are **IMMUTABLE**