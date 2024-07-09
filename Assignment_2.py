
import array

""" discs_array = array.array('i')


    # width
W = input("Enter the width value of the disc: ")
   
    # depth
D = input("Enter the depth value of the disc: ")
   
    # height
H = input("Enter the Height value of the disc: ")
   
discs_array.append[[W,D,H]]

print("your unorganized discs set is as follows: ",discs_array) """

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

