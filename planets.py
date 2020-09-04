planet_list = ["Mercury", "Venus", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Saturn', 'Uranus'])

planet_list.insert(3, 'Earth')

planet_list.append('Pluto')

rocky_planets = planet_list

del rocky_planets[8]
