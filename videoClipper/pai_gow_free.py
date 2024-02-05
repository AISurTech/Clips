from moviePy_SplitVideo import *

# This is the timeList for the Free video videoClipper\2024_02_01_Pai_Gow_Original_Videos\FREE Pai Gow 2024-02-01_11_35_22_789.mp4

# Example of a CLIP: 
# A CAP event happens at 12:41
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, the timelist for this is [758, 764]

timeList = [758, 764]
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/CLEAN Pai Gow 2024-02-01_12_29_29_363.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Clean_CAP_1")

# First Insurance
timeList = [771, 777]
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/CLEAN Pai Gow 2024-02-01_12_29_29_363.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Clean_INS_1")


# Second Insurance
timeList = [774, 780]
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/CLEAN Pai Gow 2024-02-01_12_29_29_363.mp4",
                         timeList=timeList, startsAtZeroSeconds=False, outName="Clean_INS_2")
