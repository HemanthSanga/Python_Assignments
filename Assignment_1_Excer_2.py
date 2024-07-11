
import array

# Initializing an empty list to hold the subarrays
discs_array = []

# Determining the number of subarrays you want to create
n = int(input("Enter the number of subarrays: "))

# Looping to take input for each subarray
for i in range(n):
    # Prompting the user for three values
    W = int(input(f"Enter value a for subarray {i + 1}: ")) # width
    D = int(input(f"Enter value b for subarray {i + 1}: ")) # depth
    H = int(input(f"Enter value c for subarray {i + 1}: ")) # height
    
    # Create the subarray and append it to the main array
    sub_array = [W, D, H]
    discs_array.append(sub_array)

# Printing the main array to see the result
print("your unorganized discs set is as follows:\n",discs_array)



# Sort the main array in descending order based on the subarray values
sorted_discs_array = sorted(discs_array, key=lambda x: (x[0], x[1], x[2]), reverse=True)

# Print the sorted main array to see the result
print("The sorted main array in descending order is:\n",sorted_discs_array)
