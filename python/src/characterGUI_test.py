# PySimpleGUI for GUI
import PySimpleGUI as sg

#import random to randomize stats
import random

#set GUI theme
sg.theme("DarkTeal9")

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

def character_print(character_select, character_job):

    global output

    #output to be printed to text file
    output = (
        f"\nYou have chosen {character_select} as a {character_job}!\n".title() +
        f"\nSTRENGTH:{total_strength: >10}\n"
        f"INTELLIGENCE:{total_intelligence: >6}\n"
        f"CHARISMA:{total_charisma: >10}\n"
        f"LUCK:{total_luck: >14}\n"
        f"OVERALL:{overall_stats: >11}\n"
        "\ngood luck!".upper())

    #print output to file
    with open(f"C:\\python\\output\\{character_select}.text", "w") as character_file:
        character_file.write(output)

#create output menu
def character_menu(character_select, character_job):

    character_stats_left_column = [
        [sg.Text("Strength:")],
        [sg.Text("Intelligence:")],
        [sg.Text("Charisma:")],
        [sg.Text("Luck:")],
        [sg.Text("Overall:")],
    ]

    character_stats_right_column = [
        [sg.Text(total_strength)],
        [sg.Text(total_intelligence)],
        [sg.Text(total_charisma)],
        [sg.Text(total_luck)],
        [sg.Text(overall_stats)],
    ]

    #Left colum for strings, right column for int
    layout_stats = [
        [sg.Push(), sg.Text(f"\nYou have chosen {character_select} as a {character_job}!\n".title()), sg.Push()],
        [sg.Push(), sg.Column(character_stats_left_column), sg.VSeperator(), sg.Column(character_stats_right_column), sg.Push()],
        [sg.Push(), sg.Text("Good Luck!".title()), sg.Push()],
        [sg.Push(),sg.Button("OK"), sg.Push()]
    ]

    window_stats = sg.Window("Your Stats", layout_stats, margins = (75, 50))

    #window closes if OK pressed
    while True:
        event, values = window_stats.read()
        if event == "OK" or event == sg.WIN_CLOSED:
            window_stats.close()
            break

    window_stats.close()

#create main menu function
def main_menu():

    #Gives user radio options for characters
    character_column = [
        [sg.Text("Please choose an adventurer".upper())],
        [sg.Radio("Tyler", "radio_character", key = "r_tyler" )],
        [sg.Radio("Zach", "radio_character", key = "r_zach")],
        [sg.Radio("Dave", "radio_character", key = "r_dave")],
        [sg.Radio("Chase", "radio_character", key = "r_chase")],
        [sg.Radio("Slater", "radio_character", key = "r_slater")],
    ]

    #gives user radio options for jobs
    job_column = [
        [sg.Text("Please choose a job".upper())],
        [sg.Radio("Barbarion", "radio_job", key = "r_barbarian")],
        [sg.Radio("Cleric", "radio_job", key = "r_cleric")],
        [sg.Radio("Paladin", "radio_job", key = "r_paladin")],
        [sg.Radio("Mage", "radio_job", key = "r_mage")],
        [sg.Radio("Monk", "radio_job", key = "r_monk")],
    ]

    #defines layout of window
    layout_main = [
        [sg.Push(), sg.Text("Create your character".title()), sg.Push()],
        [
        sg.Column(character_column),
        sg.VSeperator(),
        sg.Column(job_column),
        ],
        [sg.Push(),sg.Button("EXIT"), sg.Button("GENERATE"), sg.Push()]
    ]

    window_main = sg.Window("Simple Character Sheet", layout_main, margins = (75, 50))
    
    #loop to collect inputs
    while True:
        event, values = window_main.read()
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break

        elif event == "GENERATE": #Sets variable to value depending on radio selected
            for i in "radio_character":
                if values["r_tyler"] == True:
                    character_select = "tyler"
                elif values["r_zach"] == True:
                    character_select = "zach"
                elif values["r_dave"] == True:
                    character_select = "dave"
                elif values["r_chase"] == True:
                    character_select = "chase"
                elif values["r_slater"] == True:
                    character_select = "slater"
                else:               #Popup if no radio selected
                    sg.Popup(
                        "Please choose from available characters!".upper(), keep_on_top = True)
                    break

            for x in "radio_job": #Sets variable to value depending on radio selected
                if values["r_barbarian"] == True:
                    character_job = "barbarian"
                elif values["r_cleric"] == True:
                    character_job = "cleric"
                elif values["r_paladin"] == True:
                    character_job = "paladin"
                elif values["r_mage"] == True:
                    character_job = "mage"
                elif values["r_monk"] == True:
                    character_job = "monk"
                else:                #Popup if no radio selected
                    sg.Popup(
                        "Please choose from available characters!".upper(), keep_on_top = True)
                    break
        
            #prints values so output can be seen
            print(event)
            print(values)
            print(character_select)
            print(character_job)

            #running function to generate stats
            character_stats(character_select, character_job)
            
            #Outputs choices to new window
            character_menu(character_select,character_job)

            character_print(character_select, character_job)

            window_main.close()

main_menu()
