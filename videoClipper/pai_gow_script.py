from moviePy_SplitVideo import *

# This is the timeList for the Script video videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4

# Example of a CLIP: 
# CAP 1 3rd cheats 10:56    
# This means a CAP event happens at 10:56
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, the timelist for this is [60*10+56 - 3, 60*10 + 56 + 3]
# We have a note that is 3rd
# And we make the outname "Fee_CAP_1_3rd_" because it is the first CAP event and the note is 3rd

# List of events:
# CAP 1 - 3rd cheats 10:56:18
# CAP 2 -  3rd cheats 10:57:41
# CAP 3 - 3rd cheats 10:59:21
# CAP 4 - 3rd cheats 11:00:34
# CAP 5 - 3rd cheats 11:01:58
# CAP 6 - 1st cheats 11:03:49
# CAP 7 - 1st_and_3rd cheats 11:04:45
# CAP 8 - 1st cheats 11:06:16
# CAP 9 - 1st cheats 11:07:49
# PINCH 1 - 3rd cheats 11:09:14
# PINCH 2 - 3rd cheats 11:10:25
# PINCH 3 - 2nd cheats 11:12:08
# PINCH 4 - 1st cheats 11:21:28
# PINCH 5 - 3rd cheats 11:22:28
# PINCH 6 - 1st cheats 11:23:45
# PINCH 7 - 3rd cheats 11:25:00

event_list = [("10:56:18", "3rd", "CAP"),
                ("10:57:41", "3rd", "CAP"),
                ("10:59:21", "3rd", "CAP"),
                ("11:00:34", "3rd", "CAP"),
                ("11:01:58", "3rd", "CAP"),
                ("11:03:49", "1st", "CAP"),
                ("11:04:45", "1st_and_3rd", "CAP"),
                ("11:06:16", "1st", "CAP"),
                ("11:07:49", "1st", "CAP"),
                ("11:09:14", "3rd", "PINCH"),
                ("11:10:25", "3rd", "PINCH"),
                ("11:12:08", "2nd", "PINCH"),
                ("11:21:28", "1st", "PINCH"),
                ("11:22:28", "3rd", "PINCH"),
                ("11:23:45", "1st", "PINCH"),
                ("11:25:00", "3rd", "PINCH")]



# Next, we parse through each event and convert the time into a timelist with respect to the beginning of the video
# The times in the tuple above are in the format hh:mm:ss, but it is not with respect to the beginning of the video
# The beginning of the script video is at 10:35:51  
video_start_time = "10:35:51"
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
videoFilePath = r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4"
for event in converted_event_list:
    outName = "Script_" + event[2] + "_" + str(event[3]) + "_Note=" + event[1] + "_"
    clippingFromListOfTimes(videoFilePath=videoFilePath, timeList=event[0], startsAtZeroSeconds=False, outName=outName)




