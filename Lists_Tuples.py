# Let's create a shopping list
# Synthax [] - name_of_list = ["first_item","second_item"]

shopping_list = ["apples", "eggs", "dark chocolate", "tea", "bread"]
               #    0        1            2            3       4
print(shopping_list)
#  Checking the type of this data with type()
print(type(shopping_list))

#  How can I access eggs using the same concept that we learned yesterday using INDEXING

print(shopping_list[1]) #  will display eggs
print(shopping_list[-1]) #  will display bread as it's the last item

#  How can I replace an item in the list
shopping_list[0] = "mangoes"
print(shopping_list)

#  How can I add an item to the shopping list
shopping_list.append("tuna")
print(shopping_list)

#  How can I remove an item from the shopping list
shopping_list.remove("tea")
print(shopping_list)
