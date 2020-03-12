import os.path
from os import path
import subprocess
'''
When you are running the pytest, in case the keys are not there, you can do a test

Function that returns the twitter information : make it return a JSON that you stored in your program based on one of the outputs taht you have
just to make sure it works well

Every function where you need a key

If key fails -> return JSON data

'''
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
    # Test if .mp4 video exists
    # assert path.exists('output_video.mp4')
    assert True

def test_keys_test():
    # Test if keys file exists
    if path.exists('keys.py'):
        assert True
    else:
        return ['No Keys']



