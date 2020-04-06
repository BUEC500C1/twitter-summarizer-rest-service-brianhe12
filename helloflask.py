from flask import Flask, render_template
import ffmpeg_proj

app = Flask(__name__)

@app.route('/<twitter_handle>', methods=['GET'])
def generate_error_msg(twitter_handle):
    return "Please enter request in the correct format: 127.0.0.1:5000/ExampleTwitterHandle/3"


@app.route('/<twitter_handle>/<string:nums>', methods=['GET'])
def daily_post(twitter_handle,nums):
    ffmpeg_proj.gen_daily_video(twitter_handle,nums)
    return "Video Downloaded. Please open a new incognito tab (ctrl+shift+n) and go to ec500-flask.herokuapp.com to view your generated video"

@app.route("/")
def video():
    html = '''
        <!doctype html>
        <html>
            <head>
                <title>Twitter Summarizer Video</title>
            </head>
            <body style='text-align:center'>
                <video width="720" controls>
                    <source src="./static/output_video.mp4" type="video/mp4">
                </video>
            </body>
        </html>
    '''
    return html
if __name__ == '__main__':
    app.run(debug=True)