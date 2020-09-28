planet_list = ["Mercury", "Venus", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Saturn', 'Uranus'])

planet_list.insert(3, 'Earth')

planet_list.append('Pluto')

rocky_planets = planet_list

del rocky_planets[8]


# Example spacecraft list

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Jelly", "Pluto"),
   ("Bellop", "Uranus"),
   ("Freddy", "Mercury"),
   ("Oki-Doki", "Venus"),
   ("Raptor", "Jupiter"),
   ("Nexus", "Neptun"),
]

for launch_list in spacecraft:
    print('{}: {}'.format(launch_list[0], launch_list[1]))