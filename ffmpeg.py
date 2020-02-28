import subprocess
import twitter_api
import test_file
import os
import os.path
from os import path

'''
Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day
    Convert text into an image in a frame
    Do a sequence of all texts and images in chronological order.
    Display each video frame for 3 seconds
'''
# Exit if no key.py file
if not path.exists('keys.py'):
    print('\033[31m' + 'File \'keys.py\' does not exist. Please enter your keys in a \'keys.py\' file in this directory :)' + '\033[0m')
    quit()

# Get User Input
twitter_handle = input("Please enter a twitter handle : ") 
nums = input("How many top tweets would you want to see? : ")

# Grab Tweets
queue = twitter_api.get_feed(twitter_handle, int(nums))

# Open File in Write Mode
file_obj = open("list.txt","w") 
for i in range(len(queue)):
    file_obj.write(('file '+ '\'output{i}.mp4\'' + '\n').format(i = i))
file_obj.close()

# Generates 3 second .mp4 file given text
for i in range(len(queue)):
    p1 = subprocess.Popen('ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \
    "drawtext=fontfile=/path/to/font.ttf:fontsize=12: \
    fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text={str1}" \
    output{i}.mp4'.format(str1 = queue[i], i=i))
    p1.wait()

# Merge
p2 = subprocess.Popen('ffmpeg -f concat -safe 0 -i list.txt -c copy mergedfile.mp4')

# Wait for subprocess to finish
p2.wait()

# Remove Files
for i in range(len(queue)):
    p3 = subprocess.Popen(('rm output{i}.mp4').format(i = i))

# Wait for subprocess to finish
p3.wait()

# Finish
print('\033[92m' + 'Finished' + '\033[0m')

