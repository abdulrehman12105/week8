HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_HOUR = 10
CLOSING_HOUR = 17

# Initialize variables
money_taken = 0
total_hours_hired = 0

# Function to validate the time
def validate_time(hour):
    return OPENING_HOUR <= hour <= CLOSING_HOUR

# Function to calculate the money taken for one boat in a day
def calculate_daily_profit():
    global money_taken, total_hours_hired

    while True:
        # Get boat number
        boat_number = int(input("Enter the boat number (1-10): "))

        # Validate boat number
        if 1 <= boat_number <= 10:
            # Get start time
            start_time = int(input("Enter the start time (10-17): "))

            # Validate start time
            if validate_time(start_time):
                # Get duration (in hours)
                duration = float(input("Enter the duration (in hours, 0.5 or 1): "))

                # Validate duration
                if duration == 0.5 or duration == 1:
                    # Calculate cost based on duration
                    if duration == 1:
                        cost = HOURLY_RATE
                    else:
                        cost = HALF_HOUR_RATE

                    # Update money taken and total hours hired
                    money_taken += cost
                    total_hours_hired += duration

                    # Display details
                    print(f"\nBoat {boat_number} hired for {duration} hours.")
                    print(f"Cost: ${cost:.2f}")
                    print(f"Total Money Taken: ${money_taken:.2f}")
                    print(f"Total Hours Hired: {total_hours_hired} hours")

                    # Ask if another boat will be hired
                    another_hire = input("Do you want to hire another boat? (yes/no): ").lower()
                    if another_hire != 'yes':
                        break

                else:
                    print("Error: Invalid duration. Please enter 0.5 or 1.")
            else:
                print("Error: Invalid start time. Boats can only be hired between 10:00 and 17:00.")
        else:
            print("Error: Invalid boat number. Please enter a number between 1 and 10.")

# Call the function to calculate the money taken for one boat in a day
calculate_daily_profit()
