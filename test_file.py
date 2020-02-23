import os.path
from os import path

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
    print('test')


