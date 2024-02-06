from moviePy_SplitVideo import *

# This is the timeList for the Free video videoClipper\2024_02_01_Pai_Gow_Original_Videos\FREE Pai Gow 2024-02-01_11_35_22_789.mp4

# Example of a CLIP: 
# A CAP event happens at 11:37
# We want to capture 3 seconds before the event and 3 seconds afterwar
# So, the timelist for this is [60*11+37 - 3, 60*11 + 37 + 3]
# We have a note that is 3rd
# And we make the outname "Fee_CAP_1_3rd_" because it is the first CAP event and the note is 3rd

# List of Free Play events starting at 11:36 
# Time      Note        Type
# 11:36:55	3rd          CAP 
# 11:39:03	2nd         PINCH 
# 11:39:13	1st          PINCH	        (Extra note, not to include: LATE PINCH WITH DEALER LOOKING! )
# 11:39:36	3rd          CAP 
# 11:41:10	1st          CAP 
# 11:42:16	1st          CAP 
# 11:42:18	2nd         CAP 
# 11:45:46	2nd         PINCH 
# 11:47:49	2nd         CAP 
# START OF HANDS & BODIES OVER CIRCLES – NOT CHEATING BUT SHOULD BE CALLED OUT BY DEALER – USE AS FASLE POSITIVES 
# 11:49:51	3rd          CAP 
# 11:49:59	2nd         CAP 
# 11:51:22	2nd         CAP 
# 11:51:43	1st          PINCH 
# 11:51:57	3rd         COLLUSION           (Extra note, not to include: COLLUSION DEALER PUSHED 3RD ON TIE (check card values) )
# 11:53:	1st          PINCH (can’t find) 
# 11:53:33	3rd          PINCH 
# 11:55:	1st          CAP (can’t find) 
# 11:55:51	2nd         CAP 
# 11:56:09	1st          CAP 
# 11:56:49	3rd          CAP 
# 11:57:27	3rd          PINCH 
# 11:58:25	2nd          COLLUSION                        (Extra note, can't include: COLLUSION DEALER PUSHED 2ND ON TIE 
# 12:01:04	2nd         CAP 
# 12:01:40	3rd          CAP 
# 12:02:14 	1st	          CAP 
# 12:04:08	2nd         CAP 
# 12:05:20	2nd 	       CAP 
# 12:05:55	1st          CAP                    (Extra note, can't include: dealer got pushed from behind) 
# 12:07:02	2nd         CAP 
# 12:08:00	3rd          CAP 
# 12:09:08	3rd	          NOTIP                 (Extra Note:  DEALER DIDN’T TAKE TIP GAVE BACK TO PLAYER) 
# 12:09:46	3rd          PINCH 
# 12:09:50	1ST         CAP 
# 12:10:32	3rd          CAP 
# 12:11:33	2nd         CAP                     (Extra Note: (LEFT SPLIT ONLY) 
# 12:15:05	Dealer      CHECKPHONE                          DEALER CLEARING HANDS CHECKS PHONE 
# 12:15:33	 1st 	    PINCH 
# 12:15:37	 2nd        COLLUSION                       DEALER PUSHED 2ND ON TIE 
# 12:16:03 1st 	        CAP 
# 12:16:10	Dealer      SCRATCHFACE                 DEALER CLEARING HANDS SCRATCHING FACE 
# 12:16:29	DEALER      CLEARHANDS                  CLEARING HANDS 
# 12:17:20	1ST	        FORM_DROP_LOWER_VALUE_CHIP_CAP      (Extra Note: CAP (MAKE NOTE OF HIS FORM HERE, FLIPPING AND DROPPING A LOWER VALUE CHIP) 
# 12:17:37 	DEALER      TOUCHSHIRT                  DEALER TOUCHES LEFT SHIRT DID NOT CLEAR HANDS 
# 12:17:50	DEALER      SCRATCHFACE                 CLEARING HANDS SCRATCHING FACE 
# 12:17		 1ST 	     CAP (CAN’T FIND) 
# 12:17		DEALER       CHECKPOCKET                   NOT CLEARING HANDS CHECKED POCKET 
# 12:18:12	DEALER       CLEARHANDS                    CLEARED HANDS AFTER CHECKED POCKET 
# 12:18:14	2ND 	       PINCH 
# 12:18:33	2ND	            CAP 
# 12:19:26	3RD	        PINCH 
# 12:19:34	2ND	        CAP 
# 12:19:44	1ST	        CAP 
# 12:21:42	1ST	        CAP 
# 12:21:55	2ND	        CAP 
# END OF FREE PLAY


# Time is given in min:sec:cs.
# Format is ("time", "note", "type")
event_list = [("11:36:55", "3rd", "CAP"),
                ("11:39:03", "2nd", "PINCH"),
                ("11:39:13", "1st", "PINCH"),
                ("11:39:36", "3rd", "CAP"),
                ("11:41:10", "1st", "CAP"),
                ("11:42:16", "1st", "CAP"),
                ("11:42:18", "2nd", "CAP"),
                ("11:45:46", "2nd", "PINCH"),
                ("11:47:49", "2nd", "CAP"),
                ("11:49:51", "3rd", "CAP"),
                ("11:49:59", "2nd", "CAP"),
                ("11:51:22", "2nd", "CAP"),
                ("11:51:43", "1st", "PINCH"),
                ("11:51:57", "3rd", "COLLUSION"),
                ("11:53:00", "1st", "CANTFIND_PINCH"),
                ("11:53:33", "3rd", "PINCH"),
                ("11:55:00", "1st", "CANTFIND_CAP"),
                ("11:55:51", "2nd", "CAP"),
                ("11:56:09", "1st", "CAP"),
                ("11:56:49", "3rd", "CAP"),
                ("11:57:27", "3rd", "PINCH"),
                ("11:58:25", "2nd", "COLLUSION"),
                ("12:01:04", "2nd", "CAP"),
                ("12:01:40", "3rd", "CAP"),
                ("12:02:14", "1st", "CAP"),
                ("12:04:08", "2nd", "CAP"),
                ("12:05:20", "2nd", "CAP"),
                ("12:05:55", "1st", "CAP"),
                ("12:07:02", "2nd", "CAP"),
                ("12:08:00", "3rd", "CAP"),
                ("12:09:08", "3rd", "NOTIP"),
                ("12:09:46", "3rd", "PINCH"),
                ("12:09:50", "1st", "CAP"),
                ("12:10:32", "3rd", "CAP"),
                ("12:11:33", "2nd", "CAP"),
                ("12:15:05", "Dealer", "CHECKPHONE"),
                ("12:15:33", "1st", "PINCH"),
                ("12:15:37", "2nd", "COLLUSION"),
                ("12:16:03", "1st", "CAP"),
                ("12:16:10", "Dealer", "SCRATCHFACE"),
                ("12:16:29", "DEALER", "CLEARHANDS"),
                ("12:17:20", "1st", "FORM_DROP_LOWER_VALUE_CHIP_CAP"),
                ("12:17:37", "DEALER", "TOUCHSHIRT"),
                ("12:17:50", "DEALER", "SCRATCHFACE"),
                ("12:17:00", "1st", "CANTFIND_CAP"),
                ("12:17:00", "DEALER", "CHECKPOCKET"),
                ("12:18:12", "DEALER", "CLEARHANDS"),
                ("12:18:14", "2nd", "PINCH"),
                ("12:18:33", "2nd", "CAP"),
                ("12:19:26", "3rd", "PINCH"),
                ("12:19:34", "2nd", "CAP"),
                ("12:19:44", "1st", "CAP"),
                ("12:21:42", "1st", "CAP"),
                ("12:21:55", "2nd", "CAP")]


# We parse through the event list and populate the converted_event_list
# We also keep track of a counter for each type of event
converted_event_list = []
counters = {}
for event in event_list:
    time = event[0].split(":")
    time = [int(x) for x in time]
    timeList = (60*time[0] + time[1] + time[2]/100 - 3, 60*time[0] + time[1] + time[2]/100 + 3)
    if event[1] not in counters:
        counters[event[1]] = 1
    else:
        counters[event[1]] += 1
    converted_event_list.append((timeList, event[1], event[2], counters[event[1]]))





# Now, our converted_event_list looks like:
# [([starttime, endtime], "type", "note", counter)]

# Now, we clip the video using the converted_event_list

videoFilePath = r"videoClipper\2024_02_01_Pai_Gow_Original_Videos\FREE Pai Gow 2024-02-01_11_35_22_789.mp4"
for event in converted_event_list:
    outName = "Free_" + event[1] + "_" + str(event[3]) + "_Note=" + event[2] + "_"
    clippingFromListOfTimes(videoFilePath=videoFilePath, timeList=event[0], startsAtZeroSeconds=False, outName=outName)





















































