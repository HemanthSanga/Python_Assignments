Exercise 1:
Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your
calendar and your co-worker's calendar (both of which contain your respective meetings for the day, in the
form of [startTime,endTime] , as well as both of your daily working hours (i.e., the earliest and latest times
at which you're available for meetings every day, in the form of [earliestStartTime,latestEndTime]
during which you could schedule the meeting.
Write a function that takes in your calendar, your daily working hours, your co-worker's calendar, your coworker's
working hours, and the duration of the meeting that you want to schedule, and that returns a list of
all the time blocks (in the form of [startTime,endTime] during which you could schedule the meeting.
Note that times will be given and should be returned in 24 hour clock. For example: [8:30,23:59] and
meeting durations will always be in minutes

Sample Input:
YourCalendar = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
YourWorkingHours = ['9:00', '20:00']
YourCoWorkersCalendar = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30',
'15:00'], ['16:00', '17:00']]
YourCoWorkersWorkingHours = ['10:00', '18:30']
meetingDuration = 30

Expected output:
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]
