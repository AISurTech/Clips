from moviePy_SplitVideo import *

# This is the timeList for the Free video videoClipper\2024_02_01_Pai_Gow_Original_Videos\FREE Pai Gow 2024-02-01_11_35_22_789.mp4

# Example of a CLIP: 
# A CAP event happens at 11:37
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, the timelist for this is [60*11+37 - 3, 60*11 + 37 + 3]
# We have a note that is 3rd
# And we make the outname "Fee_CAP_1_3rd_" because it is the first CAP event and the note is 3rd

# List of events: 
# 11:37	3rd          CAP 
# 11:39	2nd         PINCH 
# 11:39	1st          PINCH 
# 11:39	3rd          CAP 
# 11:41	1st          CAP 
# 11;42	1st          CAP 
# 11:41	2nd         CAP 
# 11:45	2nd         PINCH 
# 11:47	2nd         CAP 
# HANDS & BODIES OVER CIRCLES 
# 11:50	3rd          CAP 
# 11:50	2nd         CAP 
# 11:51	2nd         CAP 
# 11:51	1st          PINCH 
# 11:52	COLLUSION DEALER PUSHED 3RD ON TIE 
# 11:53	1st          PINCH 
# 11:53	3rd          PINCH 
# 11:55	1st          CAP 
# 11:56	2nd         CAP 
# 11:56	1st          CAP 
# 11:57	3rd          CAP 
# 11:57	3rd          PINCH 
# 11:58	COLLUSION DEALER PUSHED 2ND ON TIE 
# 12:01	2nd         CAP 
# 12:01	3rd          CAP 
# 12:02 	1st	CAP 
# 12:04	2nd         CAP 
# 12:06	1st          CAP 
# 12:07	2nd         CAP 
# 12:08	3rd          CAP 
# 12:09	DEALER DIDN’T TAKE TIP 
# 12:09	3rd          PINCH 
# 12:09	1ST         CAP 
# 12:10	3rd          CAP 
# 12:11	2nd         CAP 
# 12:15 DEALER CLEARING HANDS CHECKS PHONE 
# 12:15 1ST 	PINCH 
# 12:15 COLLUSION DEALER PUSHED 2ND ON TIE 
# 12: 16 1st 	CAP 
# 12:16	DEALER CLEARING HANDS SCRATCHING FACE 
# 12:17	1ST	CAP 
# 12:17	DEALER CLEARING HANDS SCRATCHING FACE 
# 12:17 1ST 	CAP 
# 12:17	DEALER NOT CLEARING HANDS CHECKED POCKET 
# 12:18	DEALER CLEARED HANDS AFTER CHECKED POCKET 
# 12:18	2ND 	PINCH 
# 12:18	2ND	CAP 
# 12:19	3RD	PINCH 
# 12:19	2ND	CAP 
# 12:21	1ST	CAP 
# 12:22	2ND	CAP 

# Here is the code for these events:

# First cap occurs at 11:37
timeList = [60*11+37 - 3, 60*11 + 37 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_1" + "_" + note + "_")

# First pinch occurs at 11:39
timeList = [60*11+39 - 3, 60*11 + 39 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_1" + "_" + note + "_")

# Second pinch occurs at 11:39
timeList = [60*11+39 - 3, 60*11 + 39 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_2" + "_" + note + "_")

# Second cap occurs at 11:39
timeList = [60*11+39 - 3, 60*11 + 39 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_2" + "_" + note + "_")

# Third cap occurs at 11:41
timeList = [60*11+41 - 3, 60*11 + 41 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_3" + "_" + note + "_")

# Fourth cap occurs at 11:42
timeList = [60*11+42 - 3, 60*11 + 42 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_4" + "_" + note + "_")

# Fifth cap occurs at 11:41
timeList = [60*11+41 - 3, 60*11 + 41 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_5" + "_" + note + "_")

# Third pinch occurs at 11:45
timeList = [60*11+45 - 3, 60*11 + 45 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_3" + "_" + note + "_")

# Sixth cap occurs at 11:47
timeList = [60*11+47 - 3, 60*11 + 47 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_6" + "_" + note + "_")

# Seventh cap occurs at 11:50
timeList = [60*11+50 - 3, 60*11 + 50 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_7" + "_" + note + "_")

# Eighth cap occurs at 11:50
timeList = [60*11+50 - 3, 60*11 + 50 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_8" + "_" + note + "_")

# Ninth cap occurs at 11:51
timeList = [60*11+51 - 3, 60*11 + 51 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_9" + "_" + note + "_")

# Fourth pinch occurs at 11:51
timeList = [60*11+51 - 3, 60*11 + 51 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_4" + "_" + note + "_")

# First Collusion occurs at 11:52
timeList = [60*11+52 - 3, 60*11 + 52 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_COLL_1" + "_" + note + "_")

# Fifth pinch occurs at 11:53
timeList = [60*11+53 - 3, 60*11 + 53 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_5" + "_" + note + "_")

# Sixth pinch occurs at 11:53
timeList = [60*11+53 - 3, 60*11 + 53 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_6" + "_" + note + "_")

# Tenth cap occurs at 11:55
timeList = [60*11+55 - 3, 60*11 + 55 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_10" + "_" + note + "_")

# Eleventh cap occurs at 11:56
timeList = [60*11+56 - 3, 60*11 + 56 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_11" + "_" + note + "_")

# Twelfth cap occurs at 11:56
timeList = [60*11+56 - 3, 60*11 + 56 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_12" + "_" + note + "_")

# Thirteenth cap occurs at 11:57
timeList = [60*11+57 - 3, 60*11 + 57 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_13" + "_" + note + "_")

# Seventh pinch occurs at 11:57
timeList = [60*11+57 - 3, 60*11 + 57 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_7" + "_" + note + "_")

# Second Collusion occurs at 11:58
timeList = [60*11+58 - 3, 60*11 + 58 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_COLL_2" + "_" + note + "_")

# Fourteenth cap occurs at 12:01
timeList = [60*12+1 - 3, 60*12 + 1 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_14" + "_" + note + "_")

# Fifteenth cap occurs at 12:01
timeList = [60*12+1 - 3, 60*12 + 1 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_15" + "_" + note + "_")

# Sixteenth cap occurs at 12:02
timeList = [60*12+2 - 3, 60*12 + 2 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_16" + "_" + note + "_")

# Seventeenth cap occurs at 12:04
timeList = [60*12+4 - 3, 60*12 + 4 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_17" + "_" + note + "_")

# Eighteenth cap occurs at 12:06
timeList = [60*12+6 - 3, 60*12 + 6 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_18" + "_" + note + "_")

# Nineteenth cap occurs at 12:07
timeList = [60*12+7 - 3, 60*12 + 7 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_19" + "_" + note + "_")

# Twentieth cap occurs at 12:08
timeList = [60*12+8 - 3, 60*12 + 8 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_20" + "_" + note + "_")

# Dealer didn't take tip at 12:09
timeList = [60*12+9 - 3, 60*12 + 9 + 3]
note = "DEALER DIDNT TAKE TIP"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_DEALER_DIDNT_TAKE_TIP" + "_" + note + "_")

# Eighth pinch occurs at 12:09
timeList = [60*12+9 - 3, 60*12 + 9 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_8" + "_" + note + "_")

# Twenty first cap occurs at 12:09
timeList = [60*12+9 - 3, 60*12 + 9 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_21" + "_" + note + "_")

# Twenty second cap occurs at 12:10
timeList = [60*12+10 - 3, 60*12 + 10 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_22" + "_" + note + "_")

# Twenty third cap occurs at 12:11
timeList = [60*12+11 - 3, 60*12 + 11 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_23" + "_" + note + "_")

# Dealer clearing hands checks phone at 12:15
timeList = [60*12+15 - 3, 60*12 + 15 + 3]
note = "DEALER CLEARING HANDS CHECKS PHONE"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_DEALER_CLEARING_HANDS_CHECKS_PHONE" + "_" + note + "_")

# Ninth pinch occurs at 12:15
timeList = [60*12+15 - 3, 60*12 + 15 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_9" + "_" + note + "_")

# Third Collusion occurs at 12:15
timeList = [60*12+15 - 3, 60*12 + 15 + 3]
note = "2nd" 
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_COLL_3" + "_" + note + "_")

# Twenty fourth cap occurs at 12:16
timeList = [60*12+16 - 3, 60*12 + 16 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_24" + "_" + note + "_")

# Dealer clearing hands scratching face at 12:16
timeList = [60*12+16 - 3, 60*12 + 16 + 3]
note = "dealer"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_Scratch" + "_" + note + "_")

# Twenty fifth cap occurs at 12:17
timeList = [60*12+17 - 3, 60*12 + 17 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_25" + "_" + note + "_")

# Dealer clearing hands scratching face at 12:17
timeList = [60*12+17 - 3, 60*12 + 17 + 3]
note = "dealer"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_Scratch" + "_" + note + "_")

# Twenty sixth cap occurs at 12:17
timeList = [60*12+17 - 3, 60*12 + 17 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_26" + "_" + note + "_")

# Dealer not clearing hands checked pocket at 12:17
timeList = [60*12+17 - 3, 60*12 + 17 + 3]
note = "not_clear"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_Check_Pocket" + "_" + note + "_")

# Dealer cleared hands after checked pocket at 12:18
timeList = [60*12+18 - 3, 60*12 + 18 + 3]
note = "clear"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_Clear_Pocket" + "_" + note + "_")

# Tenth pinch occurs at 12:18
timeList = [60*12+18 - 3, 60*12 + 18 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_10" + "_" + note + "_")

# Twenty seventh cap occurs at 12:18
timeList = [60*12+18 - 3, 60*12 + 18 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_27" + "_" + note + "_")

# Eleventh pinch occurs at 12:19
timeList = [60*12+19 - 3, 60*12 + 19 + 3]
note = "3rd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_PINCH_11" + "_" + note + "_")

# Twenty eighth cap occurs at 12:19
timeList = [60*12+19 - 3, 60*12 + 19 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_28" + "_" + note + "_")

# Twenty ninth cap occurs at 12:21
timeList = [60*12+21 - 3, 60*12 + 21 + 3]
note = "1st"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_29" + "_" + note + "_")

# Thirtieth cap occurs at 12:22
timeList = [60*12+22 - 3, 60*12 + 22 + 3]
note = "2nd"
clippingFromListOfTimes(videoFilePath= r"videoClipper/2024_02_01_Pai_Gow_Original_Videos/FREE Pai Gow 2024-02-01_11_35_22_789.mp4",
                        timeList=timeList, startsAtZeroSeconds=False, outName="Free_CAP_30" + "_" + note + "_")















