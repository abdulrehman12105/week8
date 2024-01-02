BOAT_COUNT = 10

# Dictionary to store data for each boat
boat_data = {i: {'money_taken': 0, 'total_hours_hired': 0, 'return_time': 10} for i in range(1, BOAT_COUNT + 1)}

# Function to calculate the money taken for all the boats at the end of the day
def calculate_total_money_and_hours():
    total_money_taken = 0
    total_hours_hired = 0
    boats_not_used = []
    most_used_boat = None
    max_hours_used = 0

    # Calculate totals and find unused/most used boat
    for boat_number, data in boat_data.items():
        total_money_taken += data['money_taken']
        total_hours_hired += data['total_hours_hired']

        if data['total_hours_hired'] == 0:
            boats_not_used.append(boat_number)

        if data['total_hours_hired'] > max_hours_used:
            most_used_boat = boat_number
            max_hours_used = data['total_hours_hired']

    # Display report
    print("\nEnd of Day Report:")
    print(f"Total Money Taken for All Boats: ${total_money_taken:.2f}")
    print(f"Total Hours Boats Were Hired: {total_hours_hired} hours")

    if boats_not_used:
        print(f"Boats Not Used Today: {', '.join(map(str, boats_not_used))}")
    else:
        print("All boats were used today.")

    if most_used_boat is not None:
        print(f"Boat {most_used_boat} was used the most with {max_hours_used} hours.")
    else:
        print("No boats were used today.")

# Call the function to calculate the money taken for all the boats at the end of the day
calculate_total_money_and_hours()
