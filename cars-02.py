#--------|---------|---------|---------|---------|---------|---------|---------
# Python Car Sets

# 1. Create an empty set named `showroom`.
# 1. Add four of your favorite car model names to the set.
# 1. Print the length of your set.
# 1. Pick one of the items in your show room and add it to the set again.
# 1. Print your showroom. Notice how there's still only one instance of that model in there.
# 1. Using `update()`, add two more car models to your showroom with another set.
# 1. You've sold one of your cars. Remove it from the set with the `discard()` method.

# ### Acquiring more cars

# 1. Now create another set of cars in a variable `junkyard`. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the `showroom` set.
# 1. Use the `intersection` method to see which cars exist in both the showroom and that junkyard.
# 1. Now you're ready to buy the cars in the junkyard. Use the `union` method to combine the junkyard into your showroom.
# 1. Use the `discard()` method to remove any cars that you acquired from the junkyard that you want in your showroom.

showroom = set()
showroom.add('F150')
showroom.add('Tesla X')
showroom.add('Mini')
showroom.add('Z3')
print(len(showroom))
print(showroom)
showroom.add('Tesla X')
print(showroom)
showroom.update({"Mini Convertible", "Jimmy"})
print(showroom)
showroom.discard('Jimmy')
print(showroom)

junkyard = set()
junkyard.add('Sierra')
junkyard.update({'Sierra', 'LTD'})
junkyard.add('Nova')
junkyard.update({'Mini', 'Tesla X'})
print(junkyard)

print(showroom.intersection(junkyard))
showroom.union(junkyard)
print(showroom)
print(junkyard)
lost = showroom.intersection(junkyard)
for car in lost:
  junkyard.discard(car)
  
print(junkyard)