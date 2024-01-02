# Constants
BOAT_COUNT = 10


# Function to calculate the money taken for one boat
def calculate_daily_profit(boat_number, boat_data):
    total_money, total_hours_hired = boat_data

    print(f"\nBoat {boat_number}:")

    while True:
        try:
            start_hour = int(input("Enter the start hour (between 10 and 17, inclusive): "))
            if start_hour <10 or start_hour >= 17:
                print("Boat cannot be hired before 10:00 or after 17:00.")
                continue

            duration = float(input("Enter the duration in hours (0.5 for half an hour, 1 for one hour): "))
            if duration != 0.5 and duration != 1:
                print("Invalid duration. Please enter 0.5 for half an hour or 1 for one hour.")
                continue

            end_hour = start_hour + duration
            if end_hour > 17:
                print("Boat cannot be returned after 17:00.")
                continue

            if duration == 0.5:
                payment = 12
            else:
                payment = 20

            total_money += payment
            total_hours_hired += duration

            print(f"Boat hired for {duration} hours. Payment: ${payment:.2f}")

            more_hiring = input("Do you want to hire the boat again? (yes/no): ").lower()
            if more_hiring != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    print(f"\nTotal money taken for Boat {boat_number}: ${total_money:.2f}")
    print(f"Total hours hired for Boat {boat_number}: {total_hours_hired} hours")


# Function to find the next available boat or the earliest available time
def find_next_available(boats_data):
    current_time = int(input("Enter the current hour: "))
    available_boats = []

    for boat_number, boat_data in enumerate(boats_data, start=1):
        _, total_hours_hired = boat_data
        if current_time + total_hours_hired < 17:
            available_boats.append(boat_number)

    if available_boats:
        print(f"\nAvailable boats: {', '.join(map(str, available_boats))}")
    else:
        earliest_available_time = min([17 - boat_data[1] for boat_data in boats_data])
        print(f"No boats available. The earliest available time is {earliest_available_time}.")


# Main program
boats_data = [(0, 0) for _ in range(BOAT_COUNT)]  # Initialize data for all boats

for boat in range(1, BOAT_COUNT + 1):
    calculate_daily_profit(boat, boats_data[boat - 1])

find_next_available(boats_data)
