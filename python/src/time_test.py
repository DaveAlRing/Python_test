seconds_input = ""
user_input = []

while seconds_input.lower() != "done":
    
    seconds_input = input("Enter number of seconds or done when complete: ".title())
    
    if seconds_input.isdigit():

        user_input.append(seconds_input) 
        seconds = int(seconds_input)
        display_hours = seconds // 3600
        display_minutes = (seconds % 3600) // 60
        display_seconds = (seconds % 3600) % 60

        if seconds < 60:
            print("please enter a value greater than 60".upper())
        elif display_hours >= 1:
            print(f"{str(display_hours)} hours, {str(display_minutes)} minutes, and {str(display_seconds)} seconds")
        else:
            print(f"{str(display_minutes)} minutes and {str(display_seconds)} seconds")

    elif str(seconds_input.lower()) == "done":
        print("Your inputs ", user_input)
        print("Thank you!")
    else:
        print("please enter a number".upper())


