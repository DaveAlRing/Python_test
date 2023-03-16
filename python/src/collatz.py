import pprint

message = """Three Rings for the Elven-kings under the sky,
    Seven for the Dwarf-lords in their halls of stone,
    Nine for Mortal Men doomed to die,
    One for the Dark Lord on his dark throne
    In the Land of Mordor where the Shadows lie.
    One Ring to rule them all, One Ring to find them,
    One Ring to bring them all, and in the darkness bind them,
    In the Land of Mordor where the Shadows lie."""

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.PrettyPrinter(count)  

