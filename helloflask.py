from flask import Flask, render_template
import ffmpeg_proj

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/<twitter_handle>', methods=['GET'])
def generate_error_msg(twitter_handle):
    return "Please enter request in the correct format: 127.0.0.1:5000/ExampleTwitterHandle/3"


@app.route('/<twitter_handle>/<string:nums>', methods=['GET'])
def daily_post(twitter_handle,nums):
    ffmpeg_proj.gen_daily_video(twitter_handle,nums)
    return "Video Downloaded. Please check your current directory for \"output_video.mp4\""

if __name__ == '__main__':
    app.run(debug=True)