#import random to randomize stats
import random

#define variables
character_job = ""
character_select = ""
total_strength = 0
total_intelligence = 0
total_charisma = 0
total_luck = 0
overall_stats = 0
output = ""

#create character class with stat attributes
class Character:

    #dictionary to contain character objects in order to be selected
    character_dict = {}

    def __init__(self, name, strength, intelligence, charisma, luck):
        self.name = name
        self.strength = int(strength)
        self.intelligence = int(intelligence)
        self.charisma = int(charisma)
        self.luck = int(luck)
        self.character_dict[name] = self

#create Job class
class Job:

    job_dict = {}

    def __init__(self, job_name, job_strength, job_intelligence, job_charisma, job_luck):
        self.job_name = job_name
        self.job_strength = int(job_strength)
        self.job_intelligence = int(job_intelligence)
        self.job_charisma = int(job_charisma)
        self.job_luck = int(job_luck)
        self.job_dict[job_name] = self

#function to add character stats and job stats
def character_stats(character_select, character_job):

    global total_strength, total_intelligence, total_charisma, total_luck, overall_stats

    total_strength = (Character.character_dict[character_select].strength
                    + Job.job_dict[character_job].job_strength
                    + random.randint(-2, 2))
    total_intelligence = (Character.character_dict[character_select].intelligence
                    + Job.job_dict[character_job].job_intelligence
                    + random.randint(-2, 2))
    total_charisma = (Character.character_dict[character_select].charisma
                    + Job.job_dict[character_job].job_charisma
                    + random.randint(-2, 2))
    total_luck = (Character.character_dict[character_select].luck
                    + Job.job_dict[character_job].job_luck
                    + random.randint(-2, 2))
    overall_stats = (total_strength + total_intelligence
                    + total_charisma + total_luck)
    return total_strength, total_intelligence, total_charisma, total_luck, overall_stats

#creating function to print character choice and stats
def character_choice(character_select, character_job):

    global output

    #if else to check character choice and compare to character dictionary
    if character_select in Character.character_dict:

        #running function to generate stats
        character_stats(character_select, character_job)

        output = (
            f"\nYou have chosen {character_select} as a {character_job}!\n".title() +
            f"\nSTRENGTH:{total_strength: >10}\n"
            f"INTELLIGENCE:{total_intelligence: >6}\n"
            f"CHARISMA:{total_charisma: >10}\n"
            f"LUCK:{total_luck: >14}\n"
            f"OVERALL:{overall_stats: >11}\n"
            "\ngood luck!".upper())
        return output

    else:
        print("Please choose from available characters!".upper())

def character_print(output):

    print(output)

    with open(f"C:\\python\\output\\{character_select}.text", "w") as character_file:
        character_file.write(output)

#defining character objects
tyler = Character("tyler", 5, 2, 6, 1)
zach = Character("zach", 1, 5, 4, 2)
dave = Character("dave", 7, 6, 0, 0)
chase = Character("chase", -3, 8, 2, 3)
slater = Character("slater", 5, 5, 2, 1)

#defining job objects
barbarian = Job("barbarian", 3, 0, 1, 1)
cleric = Job("cleric", 0, 2, 2, 1)
paladin = Job("paladin", 2, 2, 0, 1)
mage = Job("mage", 0, 3, 0, 2)
monk = Job("monk", 1, 1, 1, 2)

#user prompts to select character and job
character_select = input("\nPlease select your character  \n"
                        "(Tyler, Zach, Dave, Chase, Slater): ".title()).lower()
character_job = input("\nPlease select your job\n" 
                    "(Barbarian, Cleric, Paladin, Mage, or Monk): ".title()).lower()

#running function to produce output
character_choice(character_select, character_job)

#print output to file
character_print(output)
