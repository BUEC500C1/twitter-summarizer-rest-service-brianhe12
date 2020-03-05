from flask import Flask, jsonify
import ffmpeg_proj

app = Flask(__name__)

@app.route("/")
def home():
    # ffmpeg_proj.gen_daily_video()
    # return jsonify({"about": "Hello World"})
    return "Video Downloaded. Please check your current directory for \"output_video.mp4\""

@app.route('/<twitter_handle>/<string:nums>', methods=['GET'])
def daily_post(twitter_handle,nums):
    #do your code here
    return twitter_handle + nums

if __name__ == '__main__':
    app.run(debug=True)