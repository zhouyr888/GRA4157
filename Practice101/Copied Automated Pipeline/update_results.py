# update_results.py

from main_code import f

# Call the function f with input value 5
d0, d1, d2 = f(29) # Unpacking the results

# Write the results to a file
with open("results_file.txt", "a") as file:
    content = f"{d0}, {d1}, {d2}\n"
    file.write(content)

print("Results saved to results_file.txt")
