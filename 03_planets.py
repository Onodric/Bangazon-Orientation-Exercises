# Python Planet List
## Exercise

# 1. Use `append()` to add Jupiter and Saturn at the end of the list.
# 1. Use the `extend()` method to add another list of the last two planets in our solar system to the end of the list.
# 1. Use `insert()` to add Earth, and Venus in the correct order.
# 1. Use `append()` again to add Pluto to the end of the list.
# 1. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called `rocky_planets`.
# 1. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the `del` operation to remove it from the end of `planet_list`.

# ## Iterating over planets

# 1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. `('Cassini', 'Jupiter')`).
# 1. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited. 
planet_list = ["Mercury", "Mars"]
print(planet_list)
planet_list.append('Jupiter')
print(planet_list)
planet_list.append('Saturn')
print(planet_list)
planet_list.extend(['Uranus', 'Neptune'])
print(planet_list)
planet_list.insert(1, 'Venus')
print(planet_list)
planet_list.insert(2, 'Earth')
print(planet_list)
planet_list.append('Pluto')
print(planet_list)
planet_list.remove('Pluto')
print(planet_list)
rocky_planets = planet_list[0:4]
print(rocky_planets)

spacecraft = [('Cassini', 'Jupiter'), ('Venera', 'Venus'), ('Curiosity', 'Mars'), ('Voyager', 'Saturn')]
for planet in planet_list:
    for craft in spacecraft:
        if craft[1] == planet:
            print(planet + " visited by " + craft[0])