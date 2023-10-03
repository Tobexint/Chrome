from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///videos.db'
db = SQLAlchemy(app)
CORS(app)

#Video Model
class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    file = db.Column(db.LargeBinary)

@app.route('/')
def root():
    return("API is active")

#Home Route
@app.route('/home')
def home():
    videos = Video.query.all()
    return render_template('index.html', videos=videos)

#Video upload route
@app.route('/upload', methods=['POST'])
def upload():
    name = request.files['video'].filename
    file = request.files['video'].read()
    video = Video(name=name, file=file)
    db.session.add(video)
    db.session.commit()
    return {"url": f"/play/{video_id}"}

#Video playback route
@app.route('/play/<int:video_id>')
def play(video_id):
    video = Video.query.get(video_id)
    return render_template('play.html', video=video)

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
