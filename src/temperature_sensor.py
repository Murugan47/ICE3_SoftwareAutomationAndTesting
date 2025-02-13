# Program Name: In-class Exercise Two
# Program Author: Nezar Mazraie
# Date 1-29-2025
#
# Description: A program that gets a list of different temperatures, and outputs the minimum, maximum and average up to two decimals

# User function that validates how many inputs the user wants to input
def ValidateUserInput():
    while True:
        try:
            usercondition = input("How many temperatures do you want to input: ")

            if usercondition.strip() == "":
                print("No input provided.")
                continue

            usercondition = int(usercondition)

            if usercondition > 0:
                return usercondition
            else:
                print("Out-of-bound value detected.")
                return None  # Exit on invalid input

        except ValueError:
            print("Invalid input detected.")
            return None  # Exit on invalid input

# User function that validates all the users temperatures that they input
def ValidateTemperatures(usercondition):
    temperature = []
    while len(temperature) < usercondition:
        try:
            usertemperature = input("Input a temperature between -50°C and 150°C: ")

            if usertemperature.strip() == "":
                print("No input provided.")
                continue

            usertemperature = float(usertemperature)

            if -50 <= usertemperature <= 150:
                temperature.append(usertemperature)
            else:
                print("Out-of-bound value detected.")
                continue  # Skip invalid temperature but continue loop

        except ValueError:
            print("Invalid input detected.")
            continue  # Skip invalid input but continue loop

    return temperature

# Function that takes the list and returns the min max and the average
def RequiredCalculations(temperatures):
    if not temperatures:
        raise ValueError("Empty list provided. Cannot calculate min, max, or average.")

    try:
        MinimumTemp = min(temperatures)
        MaximumTemp = max(temperatures)
        AverageTemp = sum(temperatures) / len(temperatures)
        return MinimumTemp, MaximumTemp, AverageTemp

    except Exception as e:
        print(f"Error during calculations: {e}")
        raise


# This is where the functions starts
if __name__ == '__main__':
    # Calls the functions and stores it in their respective variables
    userloopnumber = ValidateUserInput()
    temperatureList = ValidateTemperatures(userloopnumber)
    MinimumTemp, MaximumTemp, AverageTemp = RequiredCalculations(temperatureList)

    # Prints out the min, max and mean of the list itself
    print("The minimum tempreature is:", MinimumTemp)
    print("The maximum temperature is:", MaximumTemp)
    print("The average temperature is:", AverageTemp)