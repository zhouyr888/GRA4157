# update_results.py

from main_code import f

# Call the function f with input value 5
d0, d1, d2 = f(30) # Unpacking the results


with open("results_file.txt", "a") as file:  # Use 'a' for append mode
    content = f"{d0}, {d1}, {d2}\n"  # Adding a newline for each new entry
    file.write(content)

print("Results saved to results_file.txt")
