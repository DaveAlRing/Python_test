#print("This is a sentence on one line")

#print("This is a sentence, \nOn two lines")

#print("""This is a sentence,
#On multiple lines
#as a test""")

#heading = "this is the name of my book"
#print(heading.count("book"))

#print("the moon is round".title())

#groceries = "milk, eggs, cheese, bread"
#grocery_list = groceries.split(",")
#print(grocery_list[0])

#mars_temperature = "The Highest temperature on Mars is about -30 C"
#for item in mars_temperature.split():
    #if item.endswith('C'):
        #print("Celsius")

#print("Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
#    .lower().find("saturn"))

#test_string = ["The      lord    ", 
#                "of The", 
 #               "Rings"]
#for word in test_string:
 #   if "lord" in word:
 #       print(word)

#test_string = "101"
#second_string = "YAY!"
#print("There are {number} reasons to learn. All {wow}, {yay}".format(number="many", wow=test_string, yay=second_string))

test_string = "101"
print(f"There are {test_string} reasons to learn.")
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth".title())
