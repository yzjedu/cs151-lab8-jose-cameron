# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...


1. Ask the user how many times they want to roll the dice.
2. Create a list, sum_counts, with 11 elements, each initialized to 0. This list will count the occurrences of each possible dice sum (from 2 to 12).
3. For each roll (repeat num_rolls times):
   1. Generate two random numbers between 1 and 6, representing the values on each die.
   2. Calculate the sum of these two dice.
   3. Update the corresponding index in sum_counts based on the calculated sum:
   4. If the sum is s, increase sum_counts[s - 2] by 1.
   5. For example, if the sum is 7, increment sum_counts[7 - 2], or sum_counts[5].
4. ouput a header 
5. For each possible sum from 2 to 12:
   6. output the sum 
   7. Append a number of * characters equal to the count stored in sum_counts for that sum.

