planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets[3] = "Red Planet"
planets.append("Pluto")
planets.pop()
number_of_planets = len(planets)


print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
print("Mars is also known as", planets[3])
print("The last planet is", planets[-1])
print("There are", number_of_planets, "planets in the solar system.")