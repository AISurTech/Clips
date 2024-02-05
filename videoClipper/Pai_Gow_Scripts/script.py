from moviePy_SplitVideo import *

#example - will generate 3 clips, one from 0-5 seconds, one to 5-65, one to 65-125
timeListTest = [0,5,65,125]
clippingFromListOfTimes(videoFilePath="fight1.mp4", timeList=timeListTest, startsAtZeroSeconds=True, outName="fight1example")