# video-brianhe12
Created a module that generates a daily video summarzing a twitter handle day. This is done by converting text into an image in a frame, sequencing the images in chronological order, and then using ffmpeg to convert each image into a three second video.

## Built with:

[Tweepy](http://docs.tweepy.org/en/latest/#)

[Ffmpeg](https://www.ffmpeg.org/)

## Try it Out!
Clone this repository and authenticate with [Tweepy](http://docs.tweepy.org/en/latest/#). You will also need to install [Ffmpeg](https://www.ffmpeg.org/) locally.

### Tweepy 
For [Tweepy](http://docs.tweepy.org/en/latest/#), you will need to create a 'keys.py' file with your own generated keys for authentication. 

```python
# keys.py
CONSUMER_KEY = "********"
CONSUMER_SECRET = "********"

ACCESS_TOKEN = "********"
ACCESS_TOKEN_SECRET = "********"
```

## Example Usage
```python
PS C:\..\video-brianhe12> python .\ffmpeg.py
```
The program will ask for user inputs such as Twitter Handle and Number of top tweets the user wants to grab. After inputing valid inputs, a ```mergedfile.mp4``` result will be generated in the current directory.

