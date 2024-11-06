import random


def get_num_rolls():
    # Purpose: Prompt the user for the number of rolls, validating the input to ensure it is a positive integer.
    # Parameters: None
    # Return: Integer representing the validated number of dice rolls the user requested.

    num_rolls = input("How many rolls would you like to do? ")

    # Input validation without using 'while True'
    while num_rolls.isdigit() != True or int(num_rolls) <= 0:
        print("Invalid input. Please enter a positive integer.")
        num_rolls = input("How many rolls would you like to do? ")

    return int(num_rolls)


def roll_dice():
    # Purpose: Simulate rolling two 6-sided dice and calculate their sum.
    # Parameters: None
    # Return: Integer, the sum of two random dice rolls (range 2 to 12).

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2


def simulate_rolls(num_rolls):
    # Purpose: Perform multiple dice rolls and count the occurrences of each possible sum (2 through 12).
    # Parameters:
    #     - num_rolls: Integer, the number of times to roll a pair of dice.
    # Return: List of integers representing the count of each sum from 2 to 12. Each index (0-10) corresponds to sums 2-12.

    sum_counts = [0] * 11  # List to store counts for sums from 2 to 12
    _ = 0
    while _ != num_rolls:
        dice_sum = roll_dice()
        sum_counts[dice_sum - 2] += 1  # Adjust index for sum range (2 to 12)
        _ += 1
    return sum_counts


def display_results(sum_counts):
    # Purpose: Display the frequency of each possible dice sum as a series of asterisks.
    # Parameters:
    #     - sum_counts: List of integers where each element is the count of a sum (2 to 12).
    # Return: None, this function prints the results directly to the console.

    print("\nRolling", sum(sum_counts), "pairs of dice")
    print(sum_counts)
    sum_value = 2
    while sum_value != 13:
        stars = "*" * sum_counts[sum_value - 2]
        print(f"Sum of {sum_value:02}: {stars}")
        sum_value += 1


def main():
    # Purpose: Coordinate the flow of the program by calling the necessary functions in sequence.
    # Parameters: None
    # Return: None, this function serves as the entry point and orchestrates the program.

    num_rolls = get_num_rolls()
    sum_counts = simulate_rolls(num_rolls)
    display_results(sum_counts)


# Run the program
if __name__ == "__main__":
    main()
