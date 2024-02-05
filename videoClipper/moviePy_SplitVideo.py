# Import everything needed to edit video clips
from moviepy.editor import *
import time

'''equalRangeClipping will generate equal interval subclips so for settings equalRangeClipping(rangeMin=1, rangeMax=100, clipDuration=60) it will generate 100 clips of 60 seconds each

For clippingFromListOfTimes(timeList, startsAtZeroSeconds=True, outName=""), all timeList elements need to be integers representing the number of seconds into the video 

We use unixTimestamp to keep tack of groups of generated clips, hence we generate this timestamp string before running the loop'''

def equalRangeClipping(videoFilePath, rangeMin=1, rangeMax=100, clipDuration=60, outName=""):
  unixTimestamp = "unix" + str(time.time()).replace(".", "_") + "_"
  #unixTimestamp = "" #can empty unix timestamp if it exceeds your device pathname limit

  for i in range(rangeMin,rangeMax):
    try:
      clip = VideoFileClip(videoFilePath)
      startsecond = 1*i
      endSecond = (1 + clipDuration)*i

      clip = clip.subclip(startsecond, endSecond) 

      clip.write_videofile(f"outClips/{outName}{unixTimestamp}clip_{startsecond}to{endSecond}seconds.mp4")
      print(f"SUCCESS - clipped at for timestamp {startsecond}to{endSecond}seconds")
    except:
      print(f"Nothing left to clip at interval {i}")

def clippingFromListOfTimes(videoFilePath, timeList, startsAtZeroSeconds=True, outName=""):
  unixTimestamp = "unix" + str(time.time()).replace(".", "_") + "_"
  #unixTimestamp = "" #can empty unix timestamp if it exceeds your device pathname limit
  
  if startsAtZeroSeconds:
    previousTime = 0 #initial startsecond, defaults to starting at 0 seconds, throw away useless output later if you dont need it
  else:
    previousTime = timeList[0] #initial startsecond
    timeList = timeList[1:] #excise first element since its written to previousTime
  

  for i in timeList:
    try:
      clip = VideoFileClip(videoFilePath)
      startsecond = previousTime
      endSecond = i

      previousTime = i

      clip = clip.subclip(startsecond, endSecond) 

      clip.write_videofile(f"videoClipper/outClips/{outName}{unixTimestamp}clip_{startsecond}to{endSecond}seconds.mp4")
      print(f"SUCCESS - clipped at for timestamp {startsecond}to{endSecond}seconds")
    except Exception as e:
      print(f"Nothing left to clip at interval {i}")
      print(f"Error: {e}")