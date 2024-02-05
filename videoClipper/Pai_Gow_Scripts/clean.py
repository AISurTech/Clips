from moviePy_SplitVideo import *

#example - will generate 3 clips, one from 0-5 seconds, one to 5-65, one to 65-125
timeListTest = [0,5,65,125]
clippingFromListOfTimes(videoFilePath="../2024_02_01_Pai_Gow_Original_Videos/fight1.mp4", timeList=timeListTest, startsAtZeroSeconds=True, outName="fight1example")