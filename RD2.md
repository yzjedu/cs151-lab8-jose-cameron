# Reflection Document

* Drive Full Name  : Jose Carrillo
* Partner Full Name: Cameron
* Student ID: 1867377

The objective of this lab was to integrate lists and functions into a Python program that simulates rolling a pair of dice. By using lists, we could efficiently store and display the frequency of each possible sum (from 2 to 12) resulting from the rolls. Functions were employed to structure the code in a modular and organized way, creating a sleeker and more efficient program. This structure made the program both functional and visually clear, allowing users to see the distribution of sums with a simple, intuitive output.

To solve this problem, we followed a structured approach using lecture notes from class as a guide. We began by defining a main function to coordinate the program’s flow, followed by creating individual functions for each key task: validating user input, simulating dice rolls, and displaying results. Using lists, specifically sum_counts, allowed us to keep track of each possible sum from 2 to 12 by updating the corresponding index for each roll. We simulated the rolls by generating two random numbers to represent dice, calculating their sum, and updating the list. Finally, we used asterisks to represent the frequency of each sum visually, making it easy for the user to observe the outcome distribution.

This lab provided an opportunity to explore fundamental concepts like lists, functions, and visual output formatting. Lists allowed us to efficiently store data and retrieve counts for each sum, while functions helped organize the code logically. By displaying results with asterisks, we added a visual component that made the frequency distribution of dice rolls easy to understand. These elements, combined, contributed to a program that was both functional and engaging for users.

The program worked as expected, though there were some initial surprises. We initially thought the program would prompt the user with “Roll again?” after each roll, but instead, we opted to ask for the number of rolls upfront. This approach streamlined the program significantly and allowed for a smoother user experience. Testing included both normal and extreme cases, such as negative integers and very large numbers for roll counts. The program handled these inputs well, displaying error messages as needed and guiding users toward valid entries.

One challenge we faced was a disruption in workflow when my partner fell ill. Despite this, we managed to stay on track through clear communication, which allowed us to collaborate effectively. We adhered to three core programming principles: simplifying the code with functions, making it efficient by asking for the number of rolls at once, and creating a clean, user-friendly output. A key takeaway was the usefulness of the .isdigit() method for validating input, which enhanced error handling. Working with my partner was a positive experience, and we bonded over our shared effort. Overall, this lab taught us more than expected, and the final code was better than we initially anticipated.


