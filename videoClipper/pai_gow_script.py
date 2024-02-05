from moviePy_SplitVideo import *

# This is the timeList for the Free video videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4

# Example of a CLIP: 
# CAP 1 3rd cheats 10:56    
# This means a CAP event happens at 10:56
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, the timelist for this is [60*10+56 - 3, 60*10 + 56 + 3]
# We have a note that is 3rd
# And we make the outname "Fee_CAP_1_3rd_" because it is the first CAP event and the note is 3rd

# List of events:
# CAP 1 - 3rd cheats 10:56 
# CAP 2 -  3rd cheats 10:57 
# CAP 3 - 3rd cheats 10:59
# CAP 4 - 3rd cheats 11:00
# CAP 5 - 3rd cheats 11:02
# CAP 6 - 1st cheats 11:03
# CAP 7 - 3rd and 1st cheat 11:04
# CAP 8 - 1st cheats 11:05
# CAP 9 - 1st cheats 11:07
# PINCH 1 - 3rd cheats 11:07
# PINCH 2 - 3rd cheats 11:10
# PINCH 3 - 2nd cheats 11:12
# PINCH 4 - 1st cheats 11:21
# PINCH 5 - 3rd cheats 11:22
# PINCH 6 - 1st cheats 11:23
# PINCH 7 - 3rd cheats 11:24

# Code for each event:
# CAP 1 - 3rd cheats 10:56
timeList = [60*10+56 - 3, 60*10 + 56 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_1" + "_" + note + "_")

# CAP 2 -  3rd cheats 10:57
timeList = [60*10+57 - 3, 60*10 + 57 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_2" + "_" + note + "_")

# CAP 3 - 3rd cheats 10:59
timeList = [60*10+59 - 3, 60*10 + 59 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_3" + "_" + note + "_")

# CAP 4 - 3rd cheats 11:00
timeList = [60*11+0 - 3, 60*11 + 0 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_4" + "_" + note + "_")

# CAP 5 - 3rd cheats 11:02
timeList = [60*11+2 - 3, 60*11 + 2 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_5" + "_" + note + "_")

# CAP 6 - 1st cheats 11:03
timeList = [60*11+3 - 3, 60*11 + 3 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_6" + "_" + note + "_")

# CAP 7 - 3rd and 1st cheat 11:04
timeList = [60*11+4 - 3, 60*11 + 4 + 3]
note = "3rd_and_1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_7" + "_" + note + "_")

# CAP 8 - 1st cheats 11:05
timeList = [60*11+5 - 3, 60*11 + 5 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_8" + "_" + note + "_")

# CAP 9 - 1st cheats 11:07
timeList = [60*11+7 - 3, 60*11 + 7 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_CAP_9" + "_" + note + "_")

# PINCH 1 - 3rd cheats 11:07
timeList = [60*11+7 - 3, 60*11 + 7 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_1" + "_" + note + "_")

# PINCH 2 - 3rd cheats 11:10
timeList = [60*11+10 - 3, 60*11 + 10 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_2" + "_" + note + "_")

# PINCH 3 - 2nd cheats 11:12
timeList = [60*11+12 - 3, 60*11 + 12 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_3" + "_" + note + "_")

# PINCH 4 - 1st cheats 11:21
timeList = [60*11+21 - 3, 60*11 + 21 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_4" + "_" + note + "_")

# PINCH 5 - 3rd cheats 11:22
timeList = [60*11+22 - 3, 60*11 + 22 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_5" + "_" + note + "_")

# PINCH 6 - 1st cheats 11:23
timeList = [60*11+23 - 3, 60*11 + 23 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_6" + "_" + note + "_")

# PINCH 7 - 3rd cheats 11:24
timeList = [60*11+24 - 3, 60*11 + 24 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\SCRIPT Pai Gow 2024-02-01_10_35_57_918.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Script_PINCH_7" + "_" + note + "_")

