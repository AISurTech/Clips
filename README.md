# Clips

Theese are the clips based off of Sam's timestamps for the Free, Scripted, and Clean gameplays on 2/01. 

The clips are stored in videoClipper / outClips. The information for each clips is stored in the name, ie: Free_CAP_5_2nd_unix1707126119_0435443_clip_698to704seconds.mp4 represents a CAP executed by 2nd during the FREE game. 



When working with this repo take caution not to work in the directory containing the original source video. We don't want to accidentally overwrite the only readily available copy of the original repo or accidentally overwrite a file which happens to have the same name as one of the moviepy outputs.

Good practice to incorporate the unix timestamp into the output filename so 1) we don't accidentally duplicate filenames as we work with thousands of files and 2) we know what group it was generated with. Replace the decimal in unix timestamp with an underscore: 


    import time
    str(time.time()).replace(".", "_")
