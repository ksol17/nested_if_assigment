# Task 1

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

# Task 2 

if place == "forest" and action == "cross a river":
    num_attendees = int(input("Enter the number of attendees:"))
    if num_attendees < 10:
        print("You might need an audio system.")
    elif num_attendees >= 10:
        print("You might need a projector.")

# Task 3
vegetarian_choice = input("Do you want vegetarian food? (yes/no): ").lower()

if vegetarian_choice == "yes":
    print("We recommend Veggie Delight Caterers.")
elif vegetarian_choice == "no":
    print("We recommend Gourmet Meals Caterers.")



