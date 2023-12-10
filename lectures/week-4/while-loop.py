# list
cleanest_cities = ["Lahore", "Quetta", "Hyderabad", "Karachi", "Thatta"]

user_input = ""
while user_input != "q":
    user_input = input("Enter a city, or q to quit: ")
    if user_input != "q":
        for i in cleanest_cities:
            if user_input == i:
                print("It's one of the cleanest cities")
                

