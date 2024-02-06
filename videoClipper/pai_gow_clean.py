from moviePy_SplitVideo import *

# This is the timeList for the Clean video videoClipper\2024_02_01_Pai_Gow_Original_Videos\CLEAN Pai Gow 2024-02-01_12_29_29_363.mp4 

# Example of a CLIP: 
# A CAP event happens at 12:41
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, if the first cap occurs at 12:41, the timelist for this is [60*12 + 41 - 3, 60*12 + 41 + 3]
# And if this cap has a note = "1st", we want to record this in the filename. 

# We define each event as a tuple. The first element is the time the event occurs, the second element is the type of the event,
#  and the third element is the note of event
# Whenever we see the same event, we increment a counter and add it to the name of the event. 

#Events: 
# START OF CLEAN PLAY 
# 12:42:26	1ST	CAP 
# 12:54		INSURANCE 
# 12:57		INSURANCE 

# Time is given in min:sec:cs.
# Format is ("time", "type", "note")
event_list = [("12:42:00", "1st", "CAP"), 
              ("12:54:00", "NoNote", "INSURANCE"), 
              ("12:57:00", "NoNote", "INSURANCE")]
# Next, we parse through each event and convert the time into a timelist with respect to the beginning of the video
# The times in the tuple above are in the format hh:mm:ss, but it is not with respect to the beginning of the video
# The beginning of the clean video is at 12:29:23  
video_start_time = "12:29:23"
video_start_time = video_start_time.split(":")
video_start_time_seconds = 60*60*int(video_start_time[0]) + 60*int(video_start_time[1]) + int(video_start_time[2])

# We parse through the event list and populate the converted_event_list
# We also keep track of a counter for each type of event
converted_event_list = []
counters = {}
for event in event_list:
    # We calculate the time of the event in seconds, and then we subtract the start time of the video
    # That is the time of the event with respect to the beginning of the video
    time = event[0].split(":")
    time = [int(x) for x in time]
    time_respect_to_video = 60*60*time[0] + 60*time[1] + time[2] - video_start_time_seconds
    timeList = (time_respect_to_video - 3, time_respect_to_video + 3)
    if event[2] not in counters:
        counters[event[2]] = 1
    else:
        counters[event[2]] += 1
    converted_event_list.append((timeList, event[1], event[2], counters[event[2]]))

# Now, our converted_event_list looks like:
# [([starttime, endtime], "type", "note", counter)]

# Now, we clip the video using the converted_event_list

videoFilePath = r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/CLEAN Pai Gow 2024-02-01_12_29_29_363.mp4"
for event in converted_event_list:
    outName = "Clean_" + event[2] + "_" + str(event[3]) + "_Note=" + event[1] + "_"
    clippingFromListOfTimes(videoFilePath=videoFilePath, timeList=event[0], startsAtZeroSeconds=False, outName=outName)