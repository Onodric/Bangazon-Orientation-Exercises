#--------|---------|---------|---------|---------|---------|---------|---------
# Python Tuples
## Instructions

# 1. Create a tuple named `zoo` that contains your favorite animals.
# 1. Find one of your animals using the `.index(value)` method on the tuple.
# 1. Determine if an animal is in your tuple by using `for value in tuple`.
# 1. Create a variable for each of the animals in your tuple with this cool feature of Python.

#     ```
#     # example
#     (lizard, fox, mammoth) = zoo
#     print(lizard)
#     ```

# 1. Convert your tuple into a list.
# 1. Use `extend()` to add three more animals to your zoo.
# 1. Convert the list back into a tuple.

zoo = ('Kangaroo', "Elephant", "Tortoise", "Snail")
print(zoo)
print(zoo.index("Elephant"))
animal = input("Search the zoo: ")
for value in zoo:
    if value == animal:
        print(animal + " is in the zoo!")

(roo, phunt, turtle, slowy) = zoo
print(roo)
print(phunt)
print(turtle)
print(slowy)

zoo_list = list(zoo)
print(zoo_list)
zoo_list_tuple = tuple(zoo_list)
print(zoo_list_tuple)
