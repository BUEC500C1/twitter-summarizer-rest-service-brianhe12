import subprocess
import twitter_api
import test_file
import os
import os.path
from os import path
import time
import shlex

'''
Main Exercise:  
    Using the twitter feed, construct a daily video summarizing a twitter handle day
    Convert text into an image in a frame
    Do a sequence of all texts and images in chronological order.
    Display each video frame for 3 seconds
'''
def gen_daily_video(twitter_handle,nums):
    # Start time
    start_time = time.time()

    # # Exit if no key.py file
    # if not path.exists('keys.py'):
    #     print('\033[31m' + 'File \'keys.py\' does not exist. Please enter your keys in a \'keys.py\' file in this directory. Returning hard coded json results. No video created.' + '\033[0m')
    #     import json

    #     def getJSON(filePathAndName):
    #         with open(filePathAndName, 'r') as fp:
    #             return json.load(fp)
    #     myObj = getJSON('./stub.json')
    #     print(myObj)
    #     quit()

    # Grab Tweets
    queue = twitter_api.get_feed(twitter_handle, int(nums))
    #queue = ["testing11","testing2","testing3"]

    # Open File in Write Mode
    file_obj = open("list.txt","w") 
    for i in range(len(queue)):
        file_obj.write(('file '+ '\'output{i}.mp4\'' + '\n').format(i = i))
    file_obj.close()

    # Generates 3 second .mp4 file given text
    for i in range(len(queue)):
        cmd = 'ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \
        "drawtext=fontfile=/path/to/font.ttf:fontsize=12: \
        fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text={str1}" \
        output{i}.mp4'.format(str1 = queue[i], i=i)

        p1 = subprocess.Popen(shlex.split(cmd))
        p1.wait()

    # Merge
    merge = 'ffmpeg -f concat -safe 0 -i list.txt -c copy output_video.mp4'
    p2 = subprocess.Popen(shlex.split(merge))

    # Wait for subprocess to finish
    p2.wait()

    # Remove Files
    for i in range(len(queue)):
        cmd = ('rm output{i}.mp4').format(i = i)
        p3 = subprocess.Popen(shlex.split(cmd))

    # Wait for subprocess to finish
    p3.wait()

    # Finish
    print('\033[92m' + 'Finished in ' + str(round(time.time() - start_time,2)) + ' seconds' + '\033[0m')



# gen_daily_video("kingjames",3)