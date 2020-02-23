import os.path
from os import path
import subprocess

def test_file():
    # Test Open File & Write/Close
    file_obj = open("list.txt","w") 
    file_obj.write(('file ' + '\'output0.mp4\'' + '\n'))
    file_obj.close()

    # Read file
    file_obj = open("list.txt", "r")
    if file_obj.mode == 'r':
        contents = file_obj.read()
        if contents == ('file ' + '\'output0.mp4\'' + '\n'):
            assert True
        else:
            assert False
    file_obj.close()

def test_generate_video():
    # Test generating video given text
    p1 = subprocess.Popen('ffmpeg -f lavfi -i color=c=blue:s=320x240:d=3 -vf \
    "drawtext=fontfile=/path/to/font.ttf:fontsize=12: \
    fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text=Test_Video" \
    output0.mp4')
    p1.wait()

    # Test if .mp4 video exists
    assert path.exists('output100.mp4')
    subprocess.Popen('rm output100.mp4')


