from flask import Flask, redirect, url_for, render_template, request, send_file
import os
app=Flask(__name__)
@app.route('/')
def index():
    folder_path = 'static/music'
    music_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
    return render_template('index.html', music_files=music_files)
@app.route('/add', methods=['POST','GET'])
def add():
    try:
        file = request.files['file']
        uploads_dir = os.path.join(app.root_path, 'C:/Users/DELL/Desktop/music player/static/music')
        if not os.path.exists(uploads_dir):
            os.makedirs(uploads_dir)
        file.save(os.path.join(uploads_dir, file.filename))
    finally:
        return redirect('/')
if __name__=="__main__":
    app.run(debug=True)