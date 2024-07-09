from datetime import datetime

"""Generating a Meetings Organizer to create and organize possible number of meetings between two people with respect to their working calenders"""

my_calender_list = [] # Initializing an empty list to store the calender data input

while True:
    #first value
    my_calender_first_value = input("Enter your Start Time in HH:MM format (or type 'done' to finish): ")
    if my_calender_first_value.lower() == 'done':
        break

    #second value
    my_calender_second_value = input("Enter your End Time in HH:MM format (or type 'done' to finish): ")
    if my_calender_second_value.lower() == 'done':
        break
    
    my_calender_list.append([my_calender_first_value, my_calender_second_value])


coWorker_calender_list = [] # Initializing an empty list to store the co-worker's calender data input
print("\n")
while True:
  
    #first value
    coWorker_calender_first_value = input("Enter Co-Worker's Start Time in HH:MM format (or type 'done' to finish): ")
    if coWorker_calender_first_value.lower() == 'done':
        break

    #second value
    coWorker_calender_second_value = input("Enter Co-Worker's End Time in HH:MM format (or type 'done' to finish): ")
    if coWorker_calender_second_value.lower() == 'done':
        break
    
    coWorker_calender_list.append([coWorker_calender_first_value, coWorker_calender_second_value])



my_workingHrs_List = []
my_work_first_value = input("\n\nEnter your Working hours Start Time in HH:MM format: ") #first value
my_work_second_value = input("Enter your Working hours End Time in HH:MM format: ") #second value
my_workingHrs_List.append(my_work_first_value) #appending two arguments individually 
my_workingHrs_List.append(my_work_second_value)
print("\n")
coWorker_workingHrs_List = []
coWorker_work_first_value = input("Enter Co-Worker's Working hours Start Time in HH:MM format: ") #first value
coWorker_work_second_value = input("Enter Co-Worker's Working hours End Time in HH:MM format: ") #second value
coWorker_workingHrs_List.append(coWorker_work_first_value) #appending two arguments individually 
coWorker_workingHrs_List.append(coWorker_work_second_value)


#printing all the lists which are stored from the input dataset
print("\n\n")
print("Your Calender list is:", my_calender_list)
print("Your Co-worker's Calender list is:", coWorker_calender_list)
print("YourWorkingHours are from: ", my_workingHrs_List)
print("Your Co_Worker's working hours are from: ", coWorker_workingHrs_List)

# Converting the time values from strings to datetime objects
time_format = "%H:%M"
my_workingHrs_List_times = [datetime.strptime(time, time_format) for time in my_workingHrs_List]
coWorker_workingHrs_List_times = [datetime.strptime(time, time_format) for time in coWorker_workingHrs_List]

combined_times = my_workingHrs_List_times + coWorker_workingHrs_List_times

# Finding the earliest and latest time values
earliest_time = min(combined_times)
latest_time = max(combined_times)

# Converting the earliest and latest time values back to strings
earliest_time_str = earliest_time.strftime(time_format)
latest_time_str = latest_time.strftime(time_format)

# Creating the third list with only the earliest and latest time values
common_workingHrs_List = [earliest_time_str, latest_time_str]

print("\nYour common starting and ending working hours are: ", common_workingHrs_List)


#inputing Meeting Duration time period
print("\n")
meeting_duration = int(input("Now enter your desired meeting duration in MM format: "))
print("Meeting Duration you entered is: ", meeting_duration) #printing the Meeting duration



def time_to_minutes(t):
    """Convert time string to minutes"""
    h, m = map(int, t.split(':'))
    return h * 60 + m

def minutes_to_time(m):
    """Convert minutes to time string."""
    return f"{m // 60:02d}:{m % 60:02d}"

def merge_intervals(intervals):
    """Merge overlapping and adjacent intervals."""
    intervals.sort()
    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))
    return merged


def time_to_minutes(time_str):
    """Convert input common start and end time to minutes"""
    # Spliting the time string into hours and minutes
    hours, minutes = map(int, time_str.split(':'))
    # Converting hours to minutes and add the minutes
    total_minutes = hours * 60 + minutes
    return total_minutes


start_minutes = time_to_minutes(earliest_time_str) # Converting found earliset start time from string format to int format

end_minutes = time_to_minutes(latest_time_str)  # Converting found earliset end time from string format to int format



def find_free_intervals(merged_intervals, start_minutes, end_minutes):
    """Finding free intervals in a day given merged busy intervals."""
    free_intervals = []
    if merged_intervals[0][0] > start_minutes:
        free_intervals.append((start_minutes, merged_intervals[0][0]))
    for i in range(1, len(merged_intervals)):
        if merged_intervals[i-1][1] < merged_intervals[i][0]:
            free_intervals.append((merged_intervals[i-1][1], merged_intervals[i][0]))
    if merged_intervals[-1][1] < end_minutes:
        free_intervals.append((merged_intervals[-1][1], end_minutes))
    return free_intervals

def extract_30_min_intervals(free_intervals):
    """Extract 30-minute intervals from free intervals."""
    free_30_min_intervals = []
    for start, end in free_intervals:
        while start + meeting_duration <= end:
            free_30_min_intervals.append((start, start + meeting_duration))
            start += meeting_duration
    return free_30_min_intervals

def get_free_30_min_intervals(my_calender_list, coWorker_calender_list):
    """Convert time intervals to minutes"""

    intervals1 = [[time_to_minutes(start), time_to_minutes(end)] for start, end in my_calender_list]
    intervals2 = [[time_to_minutes(start), time_to_minutes(end)] for start, end in coWorker_calender_list]
     
    merged_intervals = merge_intervals(intervals1 + intervals2) # Merge the intervals

    free_intervals = find_free_intervals(merged_intervals,start_minutes,end_minutes) # Find free intervals

    free_30_min_intervals = extract_30_min_intervals(free_intervals) # Extract 30-minute intervals from free intervals

    free_30_min_intervals_str = [[minutes_to_time(start), minutes_to_time(end)] for start, end in free_30_min_intervals] # Convert back to time strings

    return free_30_min_intervals_str



free_30_min_intervals = get_free_30_min_intervals(my_calender_list, coWorker_calender_list)
interval = (free_30_min_intervals)
print("\n\n")
print("The possible meeting timings are as follows: ", interval)
print("Number of these meetings are: ",len(free_30_min_intervals))







