# Source data (two-dimensional array)
electricity_data = [
    [80, 120, 250],  # Slab 1: Units consumed for each user
    [150, 180, 300],  # Slab 2: Units consumed for each user
    [220, 270, 350]   # Slab 3: Units consumed for each user
]

# Function to calculate and display cost for slab 1
def costSlab1():
    unit_cost = 10
    slab_data = electricity_data[0]
    print("\nSlab 1 Bill:")
    for units in slab_data:
        cost = units * unit_cost
        print(f"User: {units} units, Cost: Rs.{cost}")

# Function to calculate and display cost for slab 2
def costSlab2():
    unit_cost = 15
    slab_data = electricity_data[1]
    print("\nSlab 2 Bill:")
    for units in slab_data:
        cost = units * unit_cost
        print(f"User: {units} units, Cost: Rs.{cost}")

# Function to calculate and display cost for slab 3
def costSlab3():
    unit_cost = 20
    slab_data = electricity_data[2]
    print("\nSlab 3 Bill:")
    for units in slab_data:
        cost = units * unit_cost
        print(f"User: {units} units, Cost: Rs.{cost}")

# Main menu
def main_menu():
    student_id = input("Enter your student ID: ")
    while True:
        print("\nMenu:")
        print("1. Display bill of slab 1 and slab 2")
        print("2. Display bill of slab 3")
        print("Any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            costSlab1()
            costSlab2()
        elif choice == '2':
            costSlab3()
        else:
            print(f"Exiting. Thank you, {student_id}!")
            break

# Run the program
main_menu()
