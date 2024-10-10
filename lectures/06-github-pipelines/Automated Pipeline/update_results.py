# update_results.py

from main_code import f

# Call the function f with input value 5
d0, d1, d2 = f(10) # Unpacking the results

# Write the results to a file
with open("results_file.txt", "w") as file:
    content = f"{d0}, {d1}, {d2}"
    file.write(content)

print("Results saved to results_file.txt")
