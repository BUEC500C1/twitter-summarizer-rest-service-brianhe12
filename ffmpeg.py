import subprocess
'''
Main Exercise:  Using the twitter feed, construct a daily video summarizing a twitter handle day
    Convert text into an image in a frame
    Do a sequence of all texts and images in chronological order.
    Display each video frame for 3 seconds


'''
str2 = 'rian'

# subprocess.Popen('ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \
# "drawtext=fontfile=/path/to/font.ttf:fontsize=30: \
#  fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text={str1} {str2}" \
# output1.mp4'.format(str1 = string1,str2= string2))

# Open File in Write Mode
file_obj = open("list.txt","w") 
for i in range(5):
    file_obj.write(str2+'\n')
file_obj.close()

# subprocess.Popen('ffmpeg -f concat -safe 0 -i list.txt -c copy mergedfile.mp4')
