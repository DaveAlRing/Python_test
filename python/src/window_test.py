import PySimpleGUI as sg

# def character_menu():

character_stats_left_column = [
        [sg.Text("Strength:")],
        [sg.Text("Intelligence:")],
        [sg.Text("Charisma:")],
        [sg.Text("Luck:")],
        [sg.Text("Overall:")],
    ]

character_stats_right_column = [
        [sg.Text("total_strength")],
        [sg.Text("total_intelligence")],
        [sg.Text("total_charisma")],
        [sg.Text("total_luck")],
        [sg.Text("overall_stats")],
    ]

layout_stats = [
        [sg.Push(), sg.Text("""\nYou have chosen {character_select} as a {character_job}!\n""".title()), sg.Push()],
        [sg.Column(character_stats_left_column), sg.VSeperator(), sg.Column(character_stats_right_column)],
        [sg.Push(),sg.Button("OK"), sg.Push()]
    ]

window = sg.Window("Your Stats", layout_stats, margins = (75, 50))

while True:
    events, value = window.read()

# character_menu()